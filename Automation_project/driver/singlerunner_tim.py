import sys
sys.path.append("../../")
import unittest
import re
from driver.case_runner import Test_Runner
from datetime import datetime
test=sys.argv[1]


exec("from scripts."+test+" import "+test+"_TestClass")

if __name__ == '__main__':
    print('loading test...'+test)
    print('Case start time: ' + str(datetime.now()))
    loader = unittest.TestLoader()
    testcase = unittest.TestSuite((loader.loadTestsFromTestCase(eval(test+"_TestClass"))))
    testRunner = Test_Runner(output='results')
    testRunner.run(testcase)
    print('Case end time: ' + str(datetime.now()))
