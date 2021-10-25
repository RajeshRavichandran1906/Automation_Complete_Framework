'''
Created on Sept 17, 2019

@author: ml12793

@description: CICD-159: Re-architect SuiteSectionRunner 
'''

import sys
import re
import os
import subprocess
import glob
import json
import shutil
import traceback
import xml.etree.ElementTree as ET
from datetime import datetime
from testrail_dao import TR_DAO 

def get_psg_id(psg):
	psg_trimmed = psg.strip()
	if re.match(re.compile(r'^[PSG]\d+'), psg_trimmed):
		return psg_trimmed[1:]
	elif re.match(re.compile(r'\d+'), psg_trimmed):
		return psg
	else:
		raise ValueError('{} is not a valid Plan/Suite/Group.'.format(psg))

class Suite_Section_Runner(object):
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		self.total_cases_ran = 0
		self.total_cases_failed = 0
		self.total_cases_in_error = 0
		self.total_cases_passed = 0
		self.total_cases_failed_to_run = 0
		self.total_cases_known = 0
		self.start_time = datetime.now()
		self.group_dir = os.path.join(os.getcwd(), 'qa/selenium/S{}/G{}'.format(suite_id, group_id))
		os.chdir(self.group_dir)

	def print_run_settings(self):
		print('\n')
		print('Test run started: ' + self.start_time.strftime('%y/%m/%d %H:%M:%S'))
		print('Test run info:')
		print('-----------------------------------')
		print('project: P' + self.project_id)
		print('suite: S' + self.suite_id)
		print('group: G' + self.group_id)
		print('plan: R' + self.plan_id)
		print('run: R' + self.run_id)
		print('browser: ' + self.browser)
		print('product: ' + self.product_id)
		print('conf id: ' + self.conf_id)
		print('release: ' + self.release_id)
		print('pkgname: ' + self.pkgname)
		print('runner box: ' + self.runner_box)
		print('number of cases to be run ' + str(len(cases_to_run_dict)))
		print('cases to be run: ' + str(self.case_list))
		print('-----------------------------------', flush=True)

	def print_run_stats(self):
		print('\n')
		print('Test run summary:')
		print('---------------------------------')
		print('Cases found in run and group : ' + str(self.cases_to_run))
		print('Cases failed to run          : ' + str(self.total_cases_failed_to_run))
		print('Cases ran                    : ' + str(self.total_cases_ran))
		print('Cases passed                 : ' + str(self.total_cases_passed))
		print('Cases failed                 : ' + str(self.total_cases_failed))
		print('Cases in error               : ' + str(self.total_cases_in_error))
		print('Cases known                  : ' + str(self.total_cases_known))
		print('---------------------------------')
		print('\n')
		end_time = datetime.now()
		print('Test run ended: '+ end_time.strftime('%y/%m/%d %H:%M:%S'))
		run_duration = end_time - self.start_time
		print('Duration of test run: ' + str(run_duration))

	def run_case(self, case_id):
		if sys.platform == 'linux':
			case_run_cmd = ['sudo', 'python3', 'singlerunner.py', 'C{}'.format(case_id)]
		else:
			case_run_cmd = 'python singlerunner.py C{}'.format(case_id)
		failed_msg = 'Case C{} could not be run with command: {}. '.format(case_id, case_run_cmd)
		try:
			res = subprocess.call(case_run_cmd)
		except Exception as e: 
			print(failed_msg + str(e))
			return 0

		if res == 0:
			self.total_cases_ran += 1
			return 1
		else:
			print(failed_msg + str(res))
			self.total_cases_failed_to_run += 1
			return 0

	def parse_result_xml(self, case_id):
		BUILD_COMMENT = '[{}] has launched this build, running on node [{}]'.format(self.build_credit, self.runner_box)
		PASSING_COMMENT = 'Passing test.'
		for name in glob.glob(self.group_dir + '/results/*C{}*.xml'.format(case_id)):
			tree = ET.parse(name)
			root = tree.getroot()
			case_failures = root.attrib.get('failures')
			case_errors = root.attrib.get('errors')
			case_start_time = root.attrib.get('runner_start_time')
			case_end_time = root.attrib.get('runner_end_time')
			case_comment = ''

			if case_failures != '0':
				case_status = 'Failed'
				self.total_cases_failed += 1
				for failure_node in root.iter('failure'):
					failure_message = failure_node.attrib.get('message')
					failure_type = failure_node.attrib.get('type')
					case_comment += ' ' + failure_message + ' ' + failure_type
				case_comment = BUILD_COMMENT + '\n' + case_comment
			elif case_errors != '0':
				case_status = 'Failed'
				self.total_cases_in_error += 1
				for error_node in root.iter('error'):
					error_message = error_node.attrib.get('message')
					error_type = error_node.attrib.get('type')
					case_comment += ' ' + error_message + ' ' + error_type
				case_comment = BUILD_COMMENT + '\n' + case_comment
			else:
				case_status = 'Passed'
				self.total_cases_passed += 1
				case_comment = BUILD_COMMENT + '\n' + PASSING_COMMENT
		return case_status, case_comment, case_start_time, case_end_time

	def generate_caserun_file(self, case_id, project_name, suite_name, group_name, case_name, case_status, case_comment, case_start_time, case_end_time):
			if self.test_tool_name == 'se':
				test_tool_name = 'Selenium'
			if sys.platform == 'linux':
				run_user = 'seluser'
			else:
				if self.runner_box[:3]=='na1':
					run_user = "svcfocqaauto@tibco.com"
				else:
					runner_num = int(self.runner_box[-3:])
					if runner_num <= 14:
						run_user = 'qaauto'
					else:
						run_user = 'qarunner1'
			if case_status == 'Passed':
				status = 'pass'
			else:
				status = 'fail'

			content_list = []
			content_list.append('job_id ' + self.build_number + '\n')
			content_list.append('runner_id ' + self.runner_box + '\n')
			content_list.append('browser_id ' + self.browser[:2].upper() + '\n')
			content_list.append('auto_tool_name ' + test_tool_name + '\n')
			content_list.append('dispatch_tool ' + 'Jenkins' + '\n')
			content_list.append('conf_id ' + self.conf_id + '\n')
			content_list.append('prodid ' + self.product_id + '\n')
			content_list.append('relid ' + self.release_id + '\n')
			content_list.append('pkgname ' + self.pkgname + '\n')
			content_list.append('plan_id ' + 'R' + self.plan_id + '\n')
			content_list.append('run_id ' + 'R' + self.run_id + '\n')
			content_list.append('run_user ' + run_user + '\n')
			content_list.append('project_id ' + 'P' + self.project_id + '\n')
			content_list.append('project_name ' + project_name + '\n')
			content_list.append('suite_id S' + self.suite_id + '\n')
			content_list.append('suite_name ' + suite_name + '\n')
			content_list.append('section_id G' + self.group_id + '\n')
			content_list.append('section_name ' + group_name + '\n')
			content_list.append('case_id ' + 'C' + case_id + '\n')
			content_list.append('case_name ' + case_name + '\n')
			content_list.append('start_time ' + case_start_time.split('.')[0] + '\n')
			content_list.append('end_time ' + case_end_time.split('.')[0] + '\n')
			content_list.append('status ' + status + '\n')
			content_list.append('count ' + str(self.cases_to_run) + '\n')
			if status == 'fail':
				comment_lines = case_comment.split('\n')
				for j in range(len(comment_lines)):
					content_list.append('comment ' + comment_lines[j] + '\n')
			full_content = ''.join(content_list)
			caserun_file = '{}_{}_{}_{}_{}_{}_S{}_R{}_R{}.caserun'.format(self.product_id, self.release_id, self.pkgname, self.conf_id, self.runner_box, self.build_number, self.suite_id, self.plan_id, self.run_id)
			with open(caserun_file, 'a') as f:
				f.write(full_content)
				f.write('\n')
			return caserun_file

	def generate_caseresult_file(self, case_id, configuration_key, run_mode_key, release_key, product_key, browser_key, case_status_id, case_comment):
		result_data_dict = {
							'custom_pkgname': self.pkgname,
							'custom_browsers': browser_key,
							'custom_configurations': configuration_key,
							'custom_run_mode': run_mode_key,
							'custom_release': release_key,
							'custom_prodid': product_key,
							'custom_atm_issues': 1,
							'run_id': self.run_id,
							'case_id': case_id,
							'status_id': case_status_id,
							'comment': case_comment,
							'defects': None 
								}
		caseresult_file = '{}_{}_{}_{}_{}_{}_S{}_R{}_R{}_C{}.caseresult'.format(self.product_id, self.release_id, self.pkgname, self.conf_id, self.runner_box, self.build_number, self.suite_id, self.plan_id, self.run_id, case_id)
		with open(caseresult_file, 'w') as f:
			f.write(json.dumps(result_data_dict))
		return caseresult_file

	def generate_htmlresult_folder(self, case_id):		
		htmlresult_folder = '{}_{}_{}_{}_{}_{}_{}_S{}_R{}_R{}_C{}'.format(self.product_id, self.release_id, self.pkgname, self.conf_id, self.runner_box, self.browser, self.build_number, self.suite_id, self.plan_id, self.run_id, case_id)
		test_case_id = 'C' + case_id
		
		#create htmlresult folder
		try:
			os.makedirs(htmlresult_folder)
		except:
			print('Unable to create case result directory locally: ' + htmlresult_folder)        
		
		#copy result xml file locally to case result directory
		try:
			caseresult_xml = test_case_id + '.xml'
			name = glob.glob(os.getcwd() + '/results/*{}*.xml'.format(test_case_id))[0]
			os.rename(name, os.getcwd() + '/results/' + caseresult_xml)
			shutil.copy('./results/' + caseresult_xml, htmlresult_folder)
		except:
			print('Unable to copy file ' + caseresult_xml + ' locally to ' + htmlresult_folder)

		#copy verification screenshots to case result directory
		try:
			verification_image_path = os.path.join(os.getcwd(), glob.glob(test_case_id)[0])        
			for png in glob.glob(os.path.join(verification_image_path, '*'+test_case_id+'*.png')):
				try:
					shutil.copy(png, htmlresult_folder)
				except:
					print('Unable to copy file ' + png + ' locally to ' + htmlresult_folder)
					del verification_image_path, png
		except Exception as e:
			try:
				exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
				if 'index' in exception_[0]:
					print('No such file *'+str(test_case_id)+'*.png found in ' + test_case_id + ' directory to copy locally to ' + htmlresult_folder)
				else:
					print(Exception(e))
			except Exception as e:
				print(Exception(e))

		#copy index HTML file to case result directory
		try:
			verification_image_path = os.path.join(os.getcwd(), glob.glob(test_case_id)[0])        
			for html in glob.glob(os.path.join(verification_image_path, 'index.html')):
				try:
						shutil.copy(html, htmlresult_folder)
				except:
					print('Unable to copy file ' + html + ' locally to ' + htmlresult_folder)
					del verification_image_path, html
		except Exception as e:
			try:
				exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
				if 'index' in exception_[0]:
					print('No such file '+str(test_case_id)+'_verificaiton.html found in ' + test_case_id + ' directory to copy locally to ' + htmlresult_folder)
				else:
					print(Exception(e))
			except Exception as e:
				print(Exception(e))
		
		#copy step screenshots to case result directory
		try:
			verification_image_path = os.path.join(os.getcwd(), glob.glob('actual_images')[0])
			for png in glob.glob(os.path.join(verification_image_path, test_case_id+'_actual_image_*.png')):
				try:
					shutil.copy(png, htmlresult_folder)
				except:
					print('Unable to copy file ' + png + ' locally to ' + htmlresult_folder)
					del verification_image_path, png
		except Exception as e:
			try:
				exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
				if 'index' in exception_[0]:
					print('No such file '+str(test_case_id)+'_actual_image_*.png found in actual_images directory to copy locally to ' + htmlresult_folder)
				else:
					print(Exception(e))
			except Exception as e:
				print(Exception(e))
		
		#copy step HTML file to case result directory
		try:
			verification_image_path = os.path.join(os.getcwd(), glob.glob('actual_images')[0])        
			for png in glob.glob(os.path.join(verification_image_path, test_case_id+'*.html')):
				try:
					shutil.copy(png, htmlresult_folder)
				except:
					print('Unable to copy file ' + png + ' locally to ' + htmlresult_folder)
		except Exception as e:
			try:
				exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
				if 'index' in exception_[0]:
					print('No such file '+str(test_case_id)+'.html found in actual_images directory to copy locally to ' + htmlresult_folder)
				else:
					print(Exception(e))
			except Exception as e:
				print(Exception(e))
		
		#copy step expected screenshots to case result directory
		try:
			verification_image_path = os.path.join(os.getcwd(), glob.glob('images*')[0])        
			for png in glob.glob(os.path.join(verification_image_path, test_case_id+'_expected_image_*.png')):
				try:
					shutil.copy(png, htmlresult_folder)
				except:
					print('Unable to copy file ' + png + ' locally to ' + htmlresult_folder)
		except Exception as e:
			try:
				exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
				if 'index' in exception_[0]:
					print('No such file '+str(test_case_id)+'_expected_image_*.png found in images* directory to copy locally to ' + htmlresult_folder)
				else:
					print(Exception(e))
			except Exception as e:
				print(Exception(e))
		
		#copy failure screenshot  to case result directory
		try:
			failure_capture_file = os.path.join(os.path.join(os.getcwd(), glob.glob('failure_capture*')[0]), 'test_' + test_case_id + '.png')        
			if os.path.isfile(failure_capture_file):
				try:
					shutil.copy(failure_capture_file, htmlresult_folder)
				except:
					print('Unable to copy file ' + failure_capture_file + ' locally to ' + htmlresult_folder)
		except Exception as e:
			try:
				exception_ = traceback.format_exception_only(type(Exception(e)), Exception(e))
				if 'index' in exception_[0]:
					print('No such file test_'+str(test_case_id)+'.png found in failure_capture* directory to copy locally to ' + htmlresult_folder)
				else:
					print(Exception(e))
			except Exception as e:
				print(Exception(e))
		
		return htmlresult_folder
	
	@staticmethod
	def copy_result_file_or_folder(directory, file_or_folder):
		if sys.platform == 'linux':				
			if os.path.isfile(file_or_folder):
				subprocess.call(['sudo', '-u', 'nobody', 'cp', file_or_folder, directory])
			else:
				subprocess.call(['sudo', '-u', 'nobody', 'cp', '-r', file_or_folder, directory])
			subprocess.call(['sudo', '-u', 'nobody', 'chmod', '-R', '777', os.path.join(directory, file_or_folder)])
		else:
			if os.path.isfile(file_or_folder):
				shutil.copy(file_or_folder, directory)
			else:
				shutil.copytree('./' + file_or_folder, os.path.join(directory, file_or_folder))

	def copy_result_files(self, caserun_file, caseresult_file, htmlresult_folder):
		if sys.platform == 'linux':
			cd_data_dir = '/bigshare.ibi.com/cd_data/temp'
			tr_data_dir = '/bigshare.ibi.com/tr_data/temp'
			jenkins_data_dir = '/bigshare.ibi.com/jenkins_data/temp'
		else:
			cd_data_dir = '\\\\na1prdfs01.tibco.com\\foc\\data\\bigshare\\cd_data\\temp'
			tr_data_dir = '\\\\na1prdfs01.tibco.com\\foc\\data\\bigshare\\tr_data\\temp'
			jenkins_data_dir = '\\\\na1prdfs01.tibco.com\\foc\\data\\bigshare\\jenkins_data\\temp'
			
		try:
			Suite_Section_Runner.copy_result_file_or_folder(tr_data_dir, caseresult_file)
		except:
			print('Unable to copy case result file {} to {}.'.format(caseresult_file, tr_data_dir))
	
		caserun_file_copy_status = caserun_file + '.done'
		try:
			Suite_Section_Runner.copy_result_file_or_folder(cd_data_dir, caserun_file)
			try:
				with open(caserun_file_copy_status, 'a') as f:
					f.write(' ')
				Suite_Section_Runner.copy_result_file_or_folder(cd_data_dir, caserun_file_copy_status)
			except:
				print('Unable to copy caserun status file {} to {}.'.format(caserun_file_copy_status, cd_data_dir))
		except:
			print('Unable to copy caserun file {} to {}.'.format(caserun_file, cd_data_dir))
	
		htmlresult_folder_copy_status = htmlresult_folder + '.done'
		with open(htmlresult_folder_copy_status, 'w') as f:
			f.write('')
		try:
			Suite_Section_Runner.copy_result_file_or_folder(jenkins_data_dir, htmlresult_folder)
			try:
				Suite_Section_Runner.copy_result_file_or_folder(jenkins_data_dir, htmlresult_folder_copy_status)
			except:
				print('Unable to copy html status file {} to {}.'.format(htmlresult_folder_copy_status, jenkins_data_dir))
		except:
			print('Unable to copy html result folder {} to {}'.format(htmlresult_folder, jenkins_data_dir))		

if __name__ == '__main__':
	product_id = sys.argv[1]
	release_id = sys.argv[2]
	conf_id = sys.argv[3]
	pkgname = sys.argv[4]
	project_id = get_psg_id(sys.argv[5])
	suite_id = get_psg_id(sys.argv[6])
	group_id = get_psg_id(sys.argv[7])
	plan_id = sys.argv[8]
	run_id = sys.argv[9]
	browser = sys.argv[10]
	case_status_to_test = sys.argv[11]
	test_result_status_name = sys.argv[12]
	test_tool_name = sys.argv[13] 
	runner_box = sys.argv[14]
	build_credit = sys.argv[15]
	build_number = sys.argv[16]

	tr = TR_DAO()	
	if test_result_status_name == 'None':
		case_status_to_test_id = tr.get_case_field('Automation Status')[case_status_to_test]
		cases_to_run_dict = tr.get_section_run_cases(group_id, run_id, cases_custom_automation_status = case_status_to_test_id)
	else:
		test_result_status_id = tr.get_status_id_by_label(test_result_status_name)[0]['id']	
		case_status_to_test_id = tr.get_case_field('Automation Status')[case_status_to_test]
		cases_to_run_dict = tr.get_section_run_cases(group_id, run_id, tests_status_id = test_result_status_id, cases_custom_automation_status = case_status_to_test_id) 
	project_name = tr.get_project_attr(int(project_id), 'name')['name']
	suite_name = tr.get_suite_attr(int(suite_id), 'name')['name']
	group_name = tr.get_group_attr(int(group_id), 'name')['name']
	configuration_key = [value for key, value in tr.get_result_field('Configurations').items() if conf_id + ':' in key][0]
	run_mode_key = tr.get_result_field('Run Mode')[test_tool_name]
	release_key = tr.get_result_field('Release')[release_id]
	product_key = tr.get_result_field('Prodid')[product_id]
	browser_key = tr.get_result_field('Browsers')[browser]
	ssr = Suite_Section_Runner(
								product_id = product_id,
								release_id = release_id,
								conf_id = conf_id,
								pkgname = pkgname,
								project_id = project_id,
								suite_id = suite_id,
								group_id = group_id,
								plan_id = plan_id,
								run_id = run_id,
								browser = browser,
								case_status_to_test = case_status_to_test,
								test_result_status_name = test_result_status_name,
								test_tool_name = test_tool_name, 
								runner_box = runner_box,
								build_credit = build_credit,
								build_number = build_number,
								cases_to_run = len(cases_to_run_dict),
								case_list = [case['id'] for case in cases_to_run_dict]
								)
	ssr.print_run_settings()
	case_status_dict = {status['name']:status['id'] for status in tr.get_status_id_by_label('Passed, Failed')}
	for case in cases_to_run_dict:
		case_id = case['id']
		case_name = case['name']
		run_case = ssr.run_case(case_id)
		if run_case:
			case_status, case_comment, case_start_time, case_end_time = ssr.parse_result_xml(case_id)
			caserun_file = ssr.generate_caserun_file(case_id, project_name, suite_name, group_name, case_name, case_status, case_comment, case_start_time, case_end_time)
			case_status_id = case_status_dict[case_status]
			htmlresult_folder = ssr.generate_htmlresult_folder(case_id)
			case_comment += '\n\\\\na1prdfs01.tibco.com\\foc\\data\\bigshare\\jenkins_data\\temp\\{}\\index.html'.format(htmlresult_folder)
			caseresult_file = ssr.generate_caseresult_file(case_id, configuration_key, run_mode_key, release_key, product_key, browser_key, case_status_id, case_comment)
			ssr.copy_result_files(caserun_file, caseresult_file, htmlresult_folder)
	ssr.print_run_stats()