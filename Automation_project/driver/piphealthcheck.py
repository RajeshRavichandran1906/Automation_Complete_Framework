'''
Created on Mar 13, 2018

@author: ly14557
'''
from selenium import webdriver
import unittest
import subprocess
import filecmp

class PipHealthCheck(unittest.TestCase):
    
    def setUp(self):
        
        self.pip_list_cmd = ['pip', 'list']
        self.good_pip_path = r'qa\selenium\driver\piplistcheck.txt'
        self.bad_pip_path = r'qa\selenium\driver\piplistcheck_bad.txt'
        self.actual_pip_path = 'actualpiplist.txt'
        self.__save_subprocess_output(self.actual_pip_path, self.pip_list_cmd)
    
    def __save_subprocess_output(self, output_file_name, cmd_input):

        output = subprocess.Popen(cmd_input, stdout=subprocess.PIPE)
        byte_output = output.stdout.read()
        file = open(output_file_name, 'w')
        file.write(byte_output.decode("utf-8"))
        file.close()
        
    def test_PipHealthCheck_pipListCompare_match(self):
        
        expected_path = self.good_pip_path
        actual_path = self.actual_pip_path
        self.assertTrue(filecmp.cmp(expected_path, actual_path))
        
    def test_PipHealthCheck_pipListCompare_mismatch(self):
        
        expected_path = self.bad_pip_path
        actual_path = self.actual_pip_path
        self.assertFalse(filecmp.cmp(expected_path, actual_path))
        

if __name__ == '__main__':
    unittest.main()