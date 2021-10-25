import sys
import unittest
import re
import xmlrunner

from scripts.C2050428 import C2050428_TestClass  
from scripts.C2050429 import C2050429_TestClass
from scripts.C2050430 import C2050430_TestClass 
from scripts.C2050433 import C2050433_TestClass
from scripts.C2050434 import C2050434_TestClass
from scripts.C2050435 import C2050435_TestClass
from scripts.C2050436 import C2050436_TestClass
from scripts.C2050437 import C2050437_TestClass
from scripts.C2050438 import C2050438_TestClass
from scripts.C2050439 import C2050439_TestClass
from scripts.C2050440 import C2050440_TestClass
from scripts.C2050441 import C2050441_TestClass
from scripts.C2050442 import C2050442_TestClass
from scripts.C2050443 import C2050443_TestClass
from scripts.C2050444 import C2050444_TestClass
from scripts.C2050447 import C2050447_TestClass
from scripts.C2050448 import C2050448_TestClass
from scripts.C2050449 import C2050449_TestClass
from scripts.C2050450 import C2050450_TestClass
from scripts.C2050451 import C2050451_TestClass
from scripts.C2050452 import C2050452_TestClass
from scripts.C2050453 import C2050453_TestClass
from scripts.C2050454 import C2050454_TestClass
from scripts.C2050455 import C2050455_TestClass
from scripts.C2055764 import C2055764_TestClass
from scripts.C2056244 import C2056244_TestClass
from scripts.C2061409 import C2061409_TestClass

  
 

 



if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((loader.loadTestsFromTestCase(C2050428_TestClass),
 								loader.loadTestsFromTestCase(C2050429_TestClass),
 								loader.loadTestsFromTestCase(C2050430_TestClass),
 								loader.loadTestsFromTestCase(C2050433_TestClass),
                                loader.loadTestsFromTestCase(C2050434_TestClass),
                                loader.loadTestsFromTestCase(C2050435_TestClass),
                                loader.loadTestsFromTestCase(C2050436_TestClass),                                                              
                                loader.loadTestsFromTestCase(C2050437_TestClass),
                                loader.loadTestsFromTestCase(C2050438_TestClass),
                                loader.loadTestsFromTestCase(C2050439_TestClass),
                                loader.loadTestsFromTestCase(C2050440_TestClass),
                                loader.loadTestsFromTestCase(C2050441_TestClass),
                                loader.loadTestsFromTestCase(C2050442_TestClass),
                                loader.loadTestsFromTestCase(C2050443_TestClass),
                                loader.loadTestsFromTestCase(C2050444_TestClass),
                                loader.loadTestsFromTestCase(C2050447_TestClass),
                                loader.loadTestsFromTestCase(C2050448_TestClass),
                                loader.loadTestsFromTestCase(C2050449_TestClass),
                                loader.loadTestsFromTestCase(C2050450_TestClass),
                                loader.loadTestsFromTestCase(C2050451_TestClass),
                                loader.loadTestsFromTestCase(C2050452_TestClass),
                                loader.loadTestsFromTestCase(C2050453_TestClass),
                                loader.loadTestsFromTestCase(C2050454_TestClass),
                                loader.loadTestsFromTestCase(C2050455_TestClass),
                                loader.loadTestsFromTestCase(C2055764_TestClass),
                                loader.loadTestsFromTestCase(C2056244_TestClass),
                                loader.loadTestsFromTestCase(C2061409_TestClass)
                                ))

    f = open('testinfo.txt','w')
    for test in suite:
        ele=test._tests
        testname=re.sub(r'test_','',ele[-1].id().split('.')[-1])
        f.write(testname+"\n")
       
    f.close 								
    testRunner=xmlrunner.XMLTestRunner(output='results')
    testRunner.run(suite)
