'''
This program deletes all the automation workspace directories, which are more than two days older. 
This program does not require any parameter, as we are fixing the maximum number of days as 2. Means all the folder which are more than two days older will be deleted.
'''
import os
import shutil
import time
import sys

numberof_files_deleted = 0
numberof_folders_deleted = 0
now_time=time.time()
max_days=3

try:
    raw_input = sys.argv[1]
    max_days = int(raw_input.strip())
except Exception as e:
    print("max_day input {} is not a valid integer - using default 3 days".format(raw_input))
   
max_old_time=now_time - max_days*24*60*60
job_directories=[]
is_failure = False
work_dir="D:\\Jenkins\\workspace\\" #default

# files = sorted(os.listdir('path'),key=os.path.getctime)

try:
    job_directories = os.listdir(work_dir)
    print('sorted: ', job_directories)
except Exception as e:
    print(str(e))
    is_failure = True

for job_directory in job_directories:
    job_dir = os.path.join(work_dir, job_directory)
    print(job_dir)
    job_directory_list = os.listdir(job_dir)
    print(job_directory_list)
    for item in job_directory_list:
        print(item)
        item_path=os.path.join(job_dir, item)
        print(item_path)
        last_modification_time=os.stat(job_dir).st_ctime
        if last_modification_time < max_old_time:
            try:
                shutil.rmtree(item_path)
                numberof_folders_deleted += 1
            except Exception as e:
                print("Error: %s : %s" % (job_dir, e))
print('Number of folders removed : ', numberof_folders_deleted)

#     job_dir = os.path.join(work_dir, job)
#     builds = []
#     try:
#         builds = os.listdir(job_dir)
#     except Exception as e:
#         print(str(e))
#         is_failure = True
        
#     for item in builds: 
#         item_path=os.path.join(job_dir, item) 
#         last_modification_time=os.stat(item_path).st_ctime
#         if last_modification_time < max_old_time: 
#             try:
#                 if os.path.isdir(item_path):
#                     shutil.rmtree(item_path)
#                     numberof_folders_deleted += 1
#                 else:
#                     os.remove(item_path)
#                     numberof_files_deleted += 1
#             except Exception as e:
#                 print(str(e))
#                 is_failure = True
# 
# if is_failure:
#     sys.exit("Something went wrong - check printed messages")

