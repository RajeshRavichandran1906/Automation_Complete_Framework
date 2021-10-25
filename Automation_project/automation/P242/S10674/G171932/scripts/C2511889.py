'''
Created on 29 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511889
TestCase Name = Select Fav/Mobile Fav, truncated Properties window when browser maximized
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import wf_mainpage
from common.wftools import login
from common.lib import utillity


class C2511889_TestClass(BaseTestCase):

    def test_C2511889(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        property_dialog_css='.properties-page.propPage'
        favorites_crum_css=".right-main-panel .crumb-box .ibx-label-text"
        
        """ Step 1: Maximize browser.
        """
        """ Step 2: Login to WebFOCUS as a Developer .
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 3: From the new Home Page click on Favorites or Mobile Favorites from side bar.
                    Verify truncated Properties window does not appear
        """
        wf_mainobj.select_left_panel('Favorites')
        utillobj.synchronize_with_visble_text(favorites_crum_css, 'Favorites', 190)
        repository_tree_appear_status = self.driver.find_element_by_css_selector(property_dialog_css).is_displayed()
        utillobj.asequal(False, repository_tree_appear_status, "Step 2: Verify truncated Properties window does not appear.")
        
        """ Step 4: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()