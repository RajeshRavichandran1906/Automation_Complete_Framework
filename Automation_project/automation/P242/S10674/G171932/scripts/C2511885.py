'''
Created on 19 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511885
TestCase Name = Maximized window displays truncated Properties window
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.lib import utillity
from selenium.common.exceptions import NoSuchElementException


class C2511885_TestClass(BaseTestCase):

    def test_C2511885(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        property_dialog_css='.properties-page.propPage'
        
        """ Step 1: Open new browser window
        """
        """ Step 2: Maximize window
        """
        """ Step 3: Login to WebFOCUS as a Developer
                    Verify Properties panel does not appear
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        '''Verify Properties panel does not appear'''
        try:
            temp_status=self.driver.find_element_by_css_selector(property_dialog_css).is_displayed()
            if temp_status == False:
                status=True
            else:
                status=False 
        except NoSuchElementException:
            status=False
        utillobj.asequal(True, status, "Step 3: Verify Properties panel does not appear")
            
        """ Step 4: Sign out
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()