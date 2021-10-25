"""-------------------------------------------------------------------------------------------
Created on August 01, 2019
@author: Niranjan

Test Case Link  =  http://172.19.2.180/testrail/index.php?/tests/view/22268188&group_by=cases:section_id&group_id=408157&group_order=asc
Test Case Title =  Tree toggle button overlaps item icons in List View
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
import time

class C2511541_TestClass(BaseTestCase):

    def test_C2511541(self):
        
        """
            Test case objects    
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
            
        """
            STEP 1 : Sign into WebFOCUS Home Page as Developer User
        """
        login.invoke_home_page('mrid', 'mrpass')
        
        """
            STEP 2 : Click Content View from the sidebar > Click on Domains from the resource tree
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        main_page.select_option_from_crumb_box("Workspaces")
        time.sleep(5)
        
        """
            STEP 3 : Click on "Retail Samples" domain from the tree.
        """
        main_page.expand_repository_folder("Retail Samples")
        
        """
            STEP 3.1 : Verify that Collapse resource tree icon does not overlapped to any folders or items in the content area.
        """
        resource_tree_obj = utils.validate_and_get_webdriver_object("div[class*='left-pane']", "Resource tree css")
        resource_tree_x = resource_tree_obj.location['x']
        width = resource_tree_obj.size['width']
        resource_tree_width = resource_tree_x + width
        
        collapse_button_css = utils.validate_and_get_webdriver_object("div[class*='tree-collapse-button']", "Collapse button css")
        collapse_button_x = collapse_button_css.location['x']
        width = collapse_button_css.size['width']
        collapse_button_width = collapse_button_x + width
        
        file_box_area = utils.validate_and_get_webdriver_object("#files-box-area", "File box area")
        file_box_x = file_box_area.location['x']
        status = collapse_button_x in range(int(resource_tree_width)-5, int(resource_tree_width)) and collapse_button_width in range(int(file_box_x), int(file_box_x) + 20)
        msg = "Step 3.1 : Verify that Collapse resource tree icon does not overlapped to any folders or items in the content area"
        utils.asequal(True, status, msg)
        
        """
            STEP 4 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()