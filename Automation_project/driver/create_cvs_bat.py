'''
Created on March 8, 2018
@author: Elena Martinez
simple text manipulation
'''
import sys
import subprocess

qa_key = 'scm'
result_key = "result"
result_success= "success"
result_failed="failed"

index = 0
parameters_msg = ''
for arg in sys.argv:
    parameters_msg += "arg index " + str(index) + " [" + arg + "]\n"
    index += 1

expected_count = 7
params_num = len(sys.argv)

if (params_num < expected_count):
    msg = "Parameters required is " + str(params_num) + ". Unexpected number of parameters received: " + parameters_msg
    raise RuntimeError(msg)
url = sys.argv[1]
branch = sys.argv[2]
infile_name = sys.argv[3]
outfile_name = sys.argv[4]
checkout_list_file_name = sys.argv[5]
inventory_list_file_name = sys.argv[6]
failed_list_file_name = "failed_" +  inventory_list_file_name

cvs_command = 'cvs -Q -d :pserver:bigscm@cvs.ibi.com:/home/cvs/webfocus checkout -r ' + branch 
cvs_login = "cvs -Q -d " + url + " login"

input_info = []
success_info = []
failed_info = []
original_contents = {}
pass_fail = {}
cvs_dict = {}

file_object  = open(infile_name, 'r')
output_file = open(checkout_list_file_name, 'w') 
for line in file_object: 
    input_info.append(line)
    line_pieces = line.split(',') 
    for line_piece in line_pieces:
        kvpair = line_piece.split('=')
        if kvpair[0] == qa_key:
            value = kvpair[1]
            original_contents[value] = line
            pass_fail[value] = False
            cvs_content = cvs_command + " " + value
            cvs_dict[value] = cvs_content
            output_file.write(cvs_content + "\n")
file_object.close()
output_file.close()

print(cvs_login)
resp=subprocess.call(cvs_login)
if (resp != 0):
    msg = "Could not log into cvs with these parameters: " + cvs_login
    raise RuntimeError(msg)

for cvs_key, cvs_content in cvs_dict.items():
    comma_sep_content = None
    msg =  msg = "," + result_key + "="
    try:
        resp=subprocess.call(cvs_content)
        if (resp != 0):
            failed_info.append(cvs_content)
            msg += result_failed
        else:
            success_info.append(cvs_content)
            msg += result_success
    except Exception as e:
        failed_info.append(cvs_content)
        msg += result_failed
    comma_sep_content = original_contents[cvs_key].strip() + msg
    original_contents[cvs_key] = comma_sep_content  
         
file_object = open(inventory_list_file_name, 'w') 
for info in success_info:
    file_object.write(info + "\n")
file_object.close()

file_object = open(failed_list_file_name, 'w') 
for info in failed_info:
    file_object.write(info + "\n")
file_object.close()
    
file_object = open(outfile_name, 'w') 
for key, value in original_contents.items():
    print("for key " + key + " value is " + value)
    file_object.write(value + "\n")
file_object.close()   