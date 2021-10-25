import sys
import unittest
import xmlrunner
test=sys.argv[1]

try:
    exec("from scripts."+test+" import "+test+"_TestClass")
except:
    exit()
    
if __name__ == '__main__':
    print('loading test...'+test)
    loader = unittest.TestLoader()
    testcase = unittest.TestSuite((loader.loadTestsFromTestCase(eval(test+"_TestClass"))))
    testRunner=xmlrunner.XMLTestRunner(output='results')
    testRunner.run(testcase)