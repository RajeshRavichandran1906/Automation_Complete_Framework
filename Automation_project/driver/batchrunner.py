'''
Created on March 19, 2018
@author: Lawrence Yu
This script is for running batch files. Initially it'll be used to start health tests, but should be extendable.
'''

import os
import sys

index = 0
parameters_msg = ''
for arg in sys.argv:
    parameters_msg += "arg index " + str(index) + " [" + arg + "]\n"
    index += 1

batch_file_param=sys.argv[1]

batch_file_list = batch_file_param.split(',')

for batch_file in batch_file_list:
    print(batch_file)
    if batch_file.endswith('.bat'):
        try:
            os.system(batch_file)
        except:
            msg = "The requested batch file does not exist in this directory."
            raise RuntimeError(msg)
    else: 
        msg = "Input doesn't match the batch file name scheme."
        raise RuntimeError(msg)