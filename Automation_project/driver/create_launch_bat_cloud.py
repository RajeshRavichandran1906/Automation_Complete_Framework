'''
Created on March 8, 2018
@author: Elena Martinez
simple text manipulation
'''
import sys
import copy

launch_method = "wget"
launch_key_prefix  = '"'
launch_key_suffix = '"'

runid_key = "run_id"
configid_key = "config_id"
suite_subsection_key = "subfolder"
suite_key = "suite_id"
subsection_key = "subsection"
projectid_key = "project_id"
result_key = "result"
result_success= "success"
asconf_key = "asconf"

key_list = []
key_list.append(runid_key)
key_list.append(configid_key)
key_list.append(suite_subsection_key)
key_list.append(subsection_key)
key_list.append(projectid_key)
key_list.append(suite_key)
key_list.append(result_key)
key_list.append(asconf_key)

keys_dict = {}
for key in key_list:
    keys_dict[key] = None

index = 0
parameters_msg = ''
for arg in sys.argv:
    parameters_msg += "arg index " + str(index) + " [" + arg + "]\n"
    index += 1

expected_count = 20
params_num = len(sys.argv)

if (params_num < expected_count):
    msg = "Parameters required is " + str(params_num) + ". Unexpected number of parameters received: " + parameters_msg
    raise RuntimeError(msg)
print(parameters_msg)

jenkins_user = sys.argv[1]
jenkins_pwd = sys.argv[2]
jenkins_url = sys.argv[3]
jenkins_job_name = sys.argv[4]
token = sys.argv[5]
product = sys.argv[6]
release = sys.argv[7]
package = sys.argv[8]
tool = sys.argv[9]
test_status_to_test = sys.argv[10]
infile_name = sys.argv[11]
outfile_name = sys.argv[12]
build_number = sys.argv[13]
cvs_track = sys.argv[14]
browser = sys.argv[15]
plan = sys.argv[16]
runner_group = sys.argv[17]
instance_type = sys.argv[18]
cloud_provider = sys.argv[19]

build_user="None"
if params_num > expected_count:
    build_user = sys.argv[20]

launch_credentials = "--auth-no-challenge --delete-after --http-user=" + jenkins_user + " --http-password=" + jenkins_pwd + " "
launch_alias = "job/" + jenkins_job_name + "/buildWithParameters?"
launch_params =  "token=" + token + "&pkg=" + package + "&tool=" + tool  + "&testStatusToTest=" + test_status_to_test +"&rel=" + release + "&product=" + product + "&upstreamUser=" + build_user + "&cvsBuild=" + build_number + "&cvsTrack=" + cvs_track
launch_cmd = launch_method + " " + launch_credentials + launch_key_prefix + jenkins_url + launch_alias + launch_params

keys = list(keys_dict)
line_info = []
file_object  = open(infile_name, 'r')
for line in file_object: 
    line_pieces = line.split(',') 
    current_dict = copy.deepcopy(keys_dict)
    for line_piece in line_pieces:
        kvpair = line_piece.split('=')
        current_key = kvpair[0]
        current_value = kvpair[1].strip()
        if current_key not in keys:
            continue
        current_dict[current_key] = current_value
    line_info.append(current_dict)
file_object.close()

output_info = []
for line_dict in line_info:
    result = line_dict[result_key]
    if result != result_success:
        continue
    conf = "&conf=" + str(line_dict[configid_key])
    project = "&project=P" + str(line_dict[projectid_key])
    suite = "&suite=S" + str(line_dict[suite_key])
    subsection = "&subsection=" + str(line_dict[subsection_key])
    runid = "&runid=" + str(line_dict[runid_key])
    
    br = "&br=" + browser
    plan_id = "&plan_id=" + plan
    runner_grp = "&RunnerGroup=" + runner_group
    instance = "&instance_type=" + instance_type
    provider = "&cloud_provider=" + cloud_provider
    if str(line_dict[asconf_key]) != None:
        asconf = "&asconf=" + str(line_dict[asconf_key])
        msg = launch_cmd + conf + br + project + suite + subsection + runid + plan_id + runner_grp + instance + provider + asconf + launch_key_suffix
    else:
        msg = launch_cmd + conf + br + project + suite + subsection + runid + plan_id + runner_grp + launch_key_suffix 
    
    output_info.append(msg)
    
file_object  = open(outfile_name, 'w') 
for info in output_info:
    line = info + '\n'
    file_object.write(line)
file_object.close()

