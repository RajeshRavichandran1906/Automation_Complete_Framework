import sys
import unittest
import re
import xmlrunner

from scripts.C2054132 import C2054132_TestClass  
from scripts.C2054133 import C2054133_TestClass
from scripts.C2054134 import C2054134_TestClass 
from scripts.C2054135 import C2054135_TestClass
from scripts.C2054136 import C2054136_TestClass  
from scripts.C2054137 import C2054137_TestClass
from scripts.C2054138 import C2054138_TestClass
from scripts.C2054139 import C2054139_TestClass
from scripts.C2064087 import C2064087_TestClass
from scripts.C2071281 import C2071281_TestClass
from scripts.C2072864 import C2072864_TestClass
from scripts.C2108674 import C2108674_TestClass
from scripts.C2157176 import C2157176_TestClass
from scripts.C2157184 import C2157184_TestClass
 





if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((loader.loadTestsFromTestCase(C2054132_TestClass),
 								loader.loadTestsFromTestCase(C2054133_TestClass),
 								loader.loadTestsFromTestCase(C2054134_TestClass),
 								loader.loadTestsFromTestCase(C2054135_TestClass),
 								loader.loadTestsFromTestCase(C2054136_TestClass),
 								loader.loadTestsFromTestCase(C2054137_TestClass),
 								loader.loadTestsFromTestCase(C2054138_TestClass),
 								loader.loadTestsFromTestCase(C2054139_TestClass),
 								loader.loadTestsFromTestCase(C2064087_TestClass),
 								loader.loadTestsFromTestCase(C2071281_TestClass),
 								loader.loadTestsFromTestCase(C2072864_TestClass),
 								loader.loadTestsFromTestCase(C2108674_TestClass),
 								loader.loadTestsFromTestCase(C2157176_TestClass),
 								loader.loadTestsFromTestCase(C2157184_TestClass)
 								 ))

    f = open('testinfo.txt','w')
    for test in suite:
       ele=test._tests
       testname=re.sub(r'test_','',ele[-1].id().split('.')[-1])
       f.write(testname+"\n")
       
    f.close 								
    testRunner=xmlrunner.XMLTestRunner(output='results')
    testRunner.run(suite)
