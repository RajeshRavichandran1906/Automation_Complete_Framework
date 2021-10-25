'''
Created on Mar 13, 2018
@author: ly14557
Usage: This code takes two pip lists and compares them to make sure that they match up. One list is saved and should be identical to that of serunner000's while the other is from
the runner box being tested on (prior to the run).
'''
import unittest
from savecmdoutput import SaveCmdOutput

class PipHealthCheck(unittest.TestCase):
    
    def setUp(self):
        
        self.pip_list_cmd = ['pip', 'list']
        self.good_pip_path = r'qa\selenium\driver\runnerhealthcheck\piplistcheck.txt'
        self.actual_pip_path = 'actualpiplist.txt'
        SaveCmdOutput.save_subprocess_output(self, self.actual_pip_path, self.pip_list_cmd)
          
    def test_piplist_match(self):
        
        expected_path = self.good_pip_path
        actual_path = self.actual_pip_path
        msg = "The generated pip list file did not match the expected file."
        
        #file1 = open(expected_path)
        #file_str1 = file1.read()
        try:
            #unicode1 = file_str1.decode("utf-8-sig")
            #file_str1 = unicode1.encode("utf-8")
            file_str1 = open(expected_path, mode='r', encoding='utf-8-sig').read()
            open(expected_path, mode='w', encoding='utf-8').write(file_str1)
        except:
            pass
        expected_list = []
        
        for line in file_str1:
            if line != "\n":
                expected_list.append(line)
        
        #file2 = open(actual_path)
        #file_str2 = file2.read()
        try:
            #unicode2 = file_str2.decode("utf-8-sig")
            #file_str2 = unicode2.encode("utf-8")
            file_str2 = open(actual_path, mode='r', encoding='utf-8-sig').read()
            open(actual_path, mode='w', encoding='utf-8').write(file_str2)
        except:
            pass
        actual_list = []
        
        for line in file_str2:
            if line != "\n":
                actual_list.append(line)
        
        print(expected_list)
        print(actual_list)
        self.assertEqual(expected_list, actual_list, msg)
        

if __name__ == '__main__':
    unittest.main()