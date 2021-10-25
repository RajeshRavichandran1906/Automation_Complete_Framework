'''
Created on 22 June, 2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10674&group_by=cases:section_id&group_id=171932&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511887
TestCase Name = Toggle tree to not appear and part of Properties window appears on right of browser
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.lib import utillity, core_utility
from selenium.common.exceptions import NoSuchElementException


class C2511887_TestClass(BaseTestCase):

    def test_C2511887(self):
        """
        TESTCASE VARIABLES
        """
        wf_login = login.Login(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj=core_utility.CoreUtillityMethods(self.driver)
        home_page_css=".explore-box .ibfs-tree .home-tree-node .ibx-label-text"
        repository_tree_css=".right-main-panel .explore-box .left-pane"
        repository_tree_toggle_button_close_css="{0} .tree-button-box".format(repository_tree_css)
        repository_tree_panel_css="{0} .ibfs-tree".format(repository_tree_css)
        repository_tree_toggle_button_open_css=".explore-box .tree-showcollapse-button"
        property_dialog_css='.properties-page.propPage'
        
        """ Step 1: Login to WebFOCUS as a Developer
        """
        wf_login.invoke_home_page('mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(home_page_css, 'Domains', 290)
        
        """ Step 2: Click on toggle button so the repository tree does not appear
                    Verify no part of Properties window appears in browser:
        """
        try:
            repository_tree_toggle_button_elem=self.driver.find_element_by_css_selector(repository_tree_toggle_button_close_css)
            core_utilobj.left_click(repository_tree_toggle_button_elem)
        except NoSuchElementException:
            raise AttributeError("Repository tree toggle button does not appear.")  
        repository_tree_appear_status = self.driver.find_element_by_css_selector(repository_tree_panel_css).is_displayed()
        utillobj.asequal(False, repository_tree_appear_status, "Step 2: Verify Repository tree does not appear.")
        repository_tree_appear_status = self.driver.find_element_by_css_selector(property_dialog_css).is_displayed()
        utillobj.asequal(False, repository_tree_appear_status, "Step 2.1: Verify no part of Properties window appears in browser.")
        
        """ Step 3: Click on toggle button to make tree reappear.
        """
        try:
            repository_tree_toggle_button_elem=self.driver.find_element_by_css_selector(repository_tree_toggle_button_open_css)
            core_utilobj.left_click(repository_tree_toggle_button_elem)
        except NoSuchElementException:
            raise AttributeError("Repository tree toggle button does not appear.")  
        repository_tree_appear_status = self.driver.find_element_by_css_selector(repository_tree_panel_css).is_displayed()
        utillobj.asequal(True, repository_tree_appear_status, "Step 3: Verify Repository tree reappear.")
        
        """ Step 4: Sign out.
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()