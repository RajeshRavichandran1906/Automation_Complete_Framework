import sys
import unittest
import re
import xmlrunner

from scripts.C2054053 import C2054053_TestClass  
from scripts.C2056255 import C2056255_TestClass
from scripts.C2071437 import C2071437_TestClass 





if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((loader.loadTestsFromTestCase(C2054053_TestClass),
 								loader.loadTestsFromTestCase(C2056255_TestClass),
                                loader.loadTestsFromTestCase(C2071437_TestClass)))

    f = open('testinfo.txt','w')
    for test in suite:
        ele=test._tests
        testname=re.sub(r'test_','',ele[-1].id().split('.')[-1])
        f.write(testname+"\n")
       
    f.close 								
    testRunner=xmlrunner.XMLTestRunner(output='results')
    testRunner.run(suite)
