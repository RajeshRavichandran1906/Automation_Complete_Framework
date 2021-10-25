import pandas
import sys
import re
from datetime import datetime

class result_processing(object):

	@staticmethod
	def read_stats_csv(path, relid, pkgname, machine, runtime):
		with open(path + relid + '_' + pkgname + '_' + machine + '_' + runtime + 'mins_users1_requests.csv', newline='') as csvfile:
			df = pandas.read_csv(csvfile, delimiter=',', usecols=['Name', 'Average response time'])
			df.columns = ['UrlRequest', '1 user']
			df = df.head(len(df.index)-1)
			for i in range(len(df.index)):
				df.at[i, 'URL ID'] = df.at[i,'UrlRequest'][:df.at[i,'UrlRequest'].index(':')]
				df.at[i, 'UrlName'] = df.at[i,'UrlRequest'][df.at[i,'UrlRequest'].index(':')+2:]
			df = df[['URL ID', 'UrlName', '1 user']]

		users = [5, 10, 20, 30, 40, 50]
		for i in users:
			with open(path + relid + '_' + pkgname + '_' + machine + '_' + runtime + 'mins_users' + str(i) + '_requests.csv', newline='') as csvfile2:
				df2 = pandas.read_csv(csvfile2, delimiter=',', usecols=['Average response time'])
				df2 = df2.head(len(df2.index)-1)
			df[str(i) + ' users'] = df2
		new_index = []
		for i in range(len(df.index)):
			new_index.append(df.index[df['URL ID'] == 'URL' + str(i+1)][0])
		df_reindexed = df.reindex(new_index)
		return df_reindexed

	@staticmethod
	def compare_baseline(prodid, relid, machine, confid, pkgname, runtime, baseline_relid, baseline_pkg):
		if sys.platform == 'linux':
			path = '/bigshare/bipg_perf_data/{0}_{1}_{2}_{3}_{4}/data/'.format(prodid, baseline_relid, machine, confid, baseline_pkg)
		else:
			path = '\\\\bigscmstr\\bigshare\\bipg_perf_data\\{0}_{1}_{2}_{3}_{4}\\data\\'.format(prodid, baseline_relid, machine, confid, baseline_pkg)
		df_baseline = result_processing.read_stats_csv(path, baseline_relid, baseline_pkg, machine, runtime)
		df_current_pkg = result_processing.read_stats_csv('', relid, pkgname, machine, runtime)
		df_report_styling = df_baseline.copy()
		df_report_styling['1 user'] = round(df_current_pkg['1 user'] / df_baseline['1 user'] * 100, 0)

		users = [5, 10, 20, 30, 40, 50]
		for i in users:
			df_report_styling[str(i) + ' users'] = round(df_current_pkg[str(i) + ' users'] / df_baseline[str(i) + ' users'] * 100, 0)
		return df_current_pkg, df_baseline, df_report_styling

	@staticmethod
	def read_locust_log(*argv):
		if len(argv) == 0:
			path = ''
		else:
			if sys.platform == 'linux':
				path = '/bigshare/bipg_perf_data/{0}_{1}_{2}_{3}_{4}/locust_logs/'.format(prodid, baseline_relid, machine, confid, baseline_pkg)
			else:
				path = '\\\\bigscmstr\\bigshare\\bipg_perf_data\\{0}_{1}_{2}_{3}_{4}\\locust_logs\\'.format(prodid, baseline_relid, machine, confid, baseline_pkg)
		users = [1, 5, 10, 20, 30, 40, 50]
		user_time = {}
		user_failure = {}
		for i in users:
			with open(path + 'locust_users' + str(i) + '.log', 'r') as logfile:
				timeframe = ''
				line = logfile.readline()
				while line:
					if '/INFO/locust.runners: All locusts hatched:' in line:
						start_time = line.split(']')[0] + ']'
						timeframe += start_time + ' - '
					if '/INFO/locust.main: Running teardowns...' in line:
						end_time = line.split(']')[0] + ']'
						timeframe += end_time
					if 'Total' in line and '%)' in line:
						nums = re.findall(r'\d+', line.split('(')[0])
						failure_rate = round(int(nums[1])/int(nums[0]), 4)
						if failure_rate != 0:
							user_failure[i] = failure_rate
					line = logfile.readline()
				user_time[i] = timeframe
		return user_time, user_failure

	@staticmethod
	def generate_html(df_current_pkg, df_baseline, df_report_styling, confid, prodid, relid, pkgname, machine, port, case, runtime, baseline_relid, baseline_pkg, threshold):
		with open('mail.html', 'w') as htmlfile:
			html_start = 'Content-Type: text/html;charset="ISO-8859-1"\nSubject: WebFOCUS automated performance test results for release: {0} pkgname: {1}\n<html>\n'.format(relid, pkgname)
			html_end = '</body></html>'
			htmlfile.write(html_start)
			htmlfile.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
			htmlfile.write('<body>\n')
			htmlfile.write('<style>\n')
			htmlfile.write('.false{color:red}\n')
			htmlfile.write('.table_title{font-weight:bold}\n')
			htmlfile.write('.baseline{float:left;width:50%}\n')
			htmlfile.write('.current_pkg{float:left;width:50%}\n')
			htmlfile.write('@media screen and (max-width: 800px) {.baseline, .current_pkg {width: 100%; }\n')
			htmlfile.write('</style>\n')
			htmlfile.write('<br><a href="file:///\\\\bigscmstr\\bigshare\\bipg_perf_data\\{0}_{1}_{2}_{3}_{4}\\email\\mail.html">View Report in Browser</a><br>'.format(prodid, relid, machine, confid, pkgname))
			htmlfile.write('<div>&nbsp</div>')
			htmlfile.write('<div>Script ran {0} minutes for each set of concurrent users, table shows average http request response time in milliseconds.</div>'.format(runtime))
			htmlfile.write('<div>Wait time before first URL to run for each user: 0 - 5 seconds.</div>')
			htmlfile.write('<div>Wait time between URLs for each user: 2.5 - 7.5 seconds.</div><br>')
			df_baseline.to_html('table_baseline.html', index=False, justify='left')
			#current run result table
			df_current_pkg.to_html('table.html', index=False, justify='left')
			df_report_styling.to_html('report_styling.html', index=False, justify='left')
			htmlfile.write('<div class="current_pkg">')
			htmlfile.write('<div class="table_title">' + 'Test run report: {0}_{1}_{2}_{3}:{4}_{5}</div>\n'.format(prodid, relid, pkgname, machine, port, case))
			htmlfile.write('<div>Any average response time over {0}% of baseline will display in red.</div>\n'.format(threshold))
			with open('table.html', 'r') as table, open('report_styling.html', 'r') as styling:
				tablelines = table.readlines()
				stylinglines = styling.readlines()
				for i in range(len(tablelines)):
					percentage = re.search(r'\d+.0', stylinglines[i])
					if percentage != None and float(percentage.group(0)) > float(threshold):
						htmlfile.write(tablelines[i].replace('<td>', '<td class="false">').replace('</td>', '(' + str(int(float(percentage.group(0)))) + '%)</td>'))
					else:
						htmlfile.write(tablelines[i])
			user_time, user_failure = result_processing.read_locust_log()
			if len(user_failure) == 0:
				htmlfile.write('<br><div>There was no failure occurred.</div>')		
			else:
				htmlfile.write('<br><div>Failures occurred for following set of concurrent users:</div>')
				for key in user_failure.keys():
					if key == 1:
						htmlfile.write('<div>' + str(key) + ' user: ' + str(user_failure[key]*100) + '%</div>')
					else:
						htmlfile.write('<div>' + str(key) + ' users: ' + str(user_failure[key]*100) + '%</div>')
			htmlfile.write('<br><a href="file:///\\\\bigscmstr\\bigshare\\bipg_perf_data\\{0}_{1}_{2}_{3}_{4}\\logs\\monitor.html">monitor.log</a><br>'.format(prodid, relid, machine, confid, pkgname))
			htmlfile.write('<a href="file:///\\\\bigscmstr\\bigshare\\bipg_perf_data\\{0}_{1}_{2}_{3}_{4}\\logs\\requests.html">requests.log</a><br><br>'.format(prodid, relid, machine, confid, pkgname))
			htmlfile.write('<div>Run timeframes:</div>')
			for key in user_time.keys():
				if key == 1:
					htmlfile.write('<div>' + str(key) + ' user: ' + user_time[key] + '</div>')
				else:
					htmlfile.write('<div>' + str(key) + ' users: ' + user_time[key] + '</div>')
			htmlfile.write('<div>&nbsp</div>')
			htmlfile.write('</div>')
			#baseline table
			htmlfile.write('<div class="baseline">')
			htmlfile.write('<div class="table_title">' + 'Baseline table: {0}_{1}_{2}_{3}:{4}_{5}</div><br>\n'.format(prodid, baseline_relid, baseline_pkg, machine, port, case))
			with open('table_baseline.html') as table_baseline:
				for line in table_baseline.readlines():
					htmlfile.write(line)
			htmlfile.write('<br><a href="file:///\\\\bigscmstr\\bigshare\\bipg_perf_data\\{0}_{1}_{2}_{3}_{4}\\logs\\monitor.html">monitor.log</a><br>'.format(prodid, baseline_relid, machine, confid, baseline_pkg))
			htmlfile.write('<a href="file:///\\\\bigscmstr\\bigshare\\bipg_perf_data\\{0}_{1}_{2}_{3}_{4}\\logs\\requests.html">requests.log</a><br><br>'.format(prodid, baseline_relid, machine, confid, baseline_pkg))
			user_time, user_failure = result_processing.read_locust_log(prodid, baseline_relid, machine, confid, baseline_pkg)
			htmlfile.write('<div>Run timeframes:</div>')
			for key in user_time.keys():
				if key == 1:
					htmlfile.write('<div>' + str(key) + ' user: ' + user_time[key] + '</div>')
				else:
					htmlfile.write('<div>' + str(key) + ' users: ' + user_time[key] + '</div>')
			# htmlfile.write('<div>&nbsp</div>')
			htmlfile.write('</div>')
			htmlfile.write('<div>&nbsp</div><div>&nbsp</div><div>&nbsp</div><div>Page generated: ' + str(datetime.now().strftime('%m/%d/%Y %H:%M:%S')) + '</div>')
			htmlfile.write(html_end)

if __name__ == '__main__':
	confid = sys.argv[1]
	prodid = sys.argv[2]
	relid = sys.argv[3]
	pkgname = sys.argv[4]
	machine = sys.argv[5]
	port = sys.argv[6]
	case = sys.argv[7]
	runtime = sys.argv[8]
	baseline_relid = sys.argv[9]
	baseline_pkg = sys.argv[10]
	threshold = sys.argv[11]
	df_current_pkg, df_baseline, df_report_styling = result_processing.compare_baseline(prodid, relid, machine, confid, pkgname, runtime, baseline_relid, baseline_pkg)
	result_processing.generate_html(df_current_pkg, df_baseline, df_report_styling, confid, prodid, relid, pkgname, machine, port, case, runtime, baseline_relid, baseline_pkg, threshold)
	
