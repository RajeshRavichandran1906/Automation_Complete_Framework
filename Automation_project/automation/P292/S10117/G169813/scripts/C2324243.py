'''
Created on 27-Sep-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10117
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2324243
TestCase Name = Cleanup : Clear_Browser_Cache_and_reopen
'''
import unittest, os, subprocess
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import time

class C2324243_TestClass(BaseTestCase):

    def test_C2324243(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        
        """ Step 1: Close and reopen browser.
                    Clear browser cache.
        """
        driver.get("about:blank")
        time.sleep(3)
        browser = utillobj.parseinitfile('browser')
        subprocess.Popen(os.getcwd()+"\\common\\lib\\Open_clear_history_window.exe "+str(browser))
        utillobj.asequal('Browser_Cache_clear', 'Browser_Cache_clear', 'Step 1: Clear browser History and cache Passed.')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()  