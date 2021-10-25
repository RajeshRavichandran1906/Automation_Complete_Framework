'''
Created on Mar 13, 2018

@author: ly14557
'''
import subprocess, sys

class SaveCmdOutput(object):
       
    def save_subprocess_output(self, output_file_name, cmd_input):

        output = subprocess.Popen(cmd_input, stdout=subprocess.PIPE)
        sys.stdout.flush()
        byte_output = output.stdout.read()
        file = open(output_file_name, 'w')
        file.write(byte_output.decode("utf-8"))
        file.close()        
