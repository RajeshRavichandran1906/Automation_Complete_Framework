import sys
import unittest
import re
from scripts.C2222560 import C2222560_TestClass  



import xmlrunner


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((loader.loadTestsFromTestCase(C2222560_TestClass)))#File name.Classname

    f = open('testinfo.txt','w')
    for test in suite:
       ele=test._tests
       testname=re.sub(r'test_','',ele[-1].id().split('.')[-1])
       f.write(testname+"\n")
       
    f.close 								
    testRunner=xmlrunner.XMLTestRunner(output='results')
    testRunner.run(suite)
