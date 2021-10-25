'''
Created on Mar 13, 2018

@author: ly14557
@Usage: This program deletes all directories or files that match a provided regular expression and before a specified time frame. 
This has been made mandatory for now as it reduces the risk of an accidental and incorrect usage. Example time frames are days, weeks, and hours.
'''

import datetime
import os
import glob
import shutil
import sys

EXIT_MESSAGE = "Exiting program."
if len(sys.argv) < 3:
    print("Lacking a required parameter. ", EXIT_MESSAGE)
    sys.exit(1)

sys_regex = sys.argv[1]

try:
    sys_time_diff = dict([arg.split('=', maxsplit=1) for arg in sys.argv[2:]])
    for key in sys_time_diff:
        sys_time_diff[key] = int(sys_time_diff[key])
    print(sys_time_diff)
except:
    print("Incorrect formatting of time difference. ", EXIT_MESSAGE)
    sys.exit(1)

class CleanDirectory(): 
    def clean_directory(self, regex, time_difference):
        files = sorted(glob.glob(regex), key=os.path.getmtime)
        if len(files) > 0:
            curr_time = datetime.datetime.fromtimestamp(os.path.getmtime(files[len(files)-1]))
            for f in files:
                try:
                    mod_time = os.stat(f).st_mtime
                    mod_time_adjusted = datetime.datetime.fromtimestamp(mod_time)
                    cut_off_time = curr_time - time_difference
                    if mod_time_adjusted < cut_off_time:
                        print(f, mod_time_adjusted, "Deleting file/directory")
                        shutil.rmtree(f)
                except:
                    print("Error - unable to delete file " + str(f))
                    print("This file will be skipped over")
                    continue
            
def main():
    regex = sys_regex #"D:\\*_*_*_*_*\\"
    time_diff_dict = sys_time_diff
    diff = datetime.timedelta(**time_diff_dict) #weeks=4
    CleanDirectory().clean_directory(regex, diff)  

if __name__ == '__main__':
    main()