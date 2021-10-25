import sys
import unittest
import re
import xmlrunner

from scripts.C2050639 import C2050639_TestClass  
from scripts.C2050642 import C2050642_TestClass
from scripts.C2055525 import C2055525_TestClass 
from scripts.C2055526 import C2055526_TestClass
from scripts.C2055527 import C2055527_TestClass  
 

 



if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((loader.loadTestsFromTestCase(C2050639_TestClass),
 								loader.loadTestsFromTestCase(C2050642_TestClass),
 								loader.loadTestsFromTestCase(C2055525_TestClass),
 								loader.loadTestsFromTestCase(C2055526_TestClass),
 								loader.loadTestsFromTestCase(C2055527_TestClass)
 								 ))

    f = open('testinfo.txt','w')
    for test in suite:
       ele=test._tests
       testname=re.sub(r'test_','',ele[-1].id().split('.')[-1])
       f.write(testname+"\n")
       
    f.close 								
    testRunner=xmlrunner.XMLTestRunner(output='results')
    testRunner.run(suite)
