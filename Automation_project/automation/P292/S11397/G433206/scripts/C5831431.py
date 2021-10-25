"""-------------------------------------------------------------------------------------------
Created on August 08, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831431
Test Case Title =  Verify unchecking Personal tag deselects all user's reports
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.core_utility import CoreUtillityMethods
import time

class C5831431_TestClass(BaseTestCase):

    def test_C5831431(self):
        
        """
            Test case objects    
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            Test case css
        """
        parent_css = ".sd-category-buttons"
        shared_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(1)"
            
        """
            STEP 1 : Sign into WebFOCUS Home Page as Developer User.
        """
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 2 : Click Domains in tree.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        main_page.expand_repository_folder("Domains->HOME-1091")
        time.sleep(10)
        
        """
            STEP 3 : Type * in Search box.
        """
        main_page.search_input_box_options(option_type ='write', input_text_msg= "*")
        utils.synchronize_until_element_is_visible(parent_css, main_page.home_page_long_timesleep)
        
        """
            STEP 4 : Check Shared tag
        """
        shared_tag_obj = utils.validate_and_get_webdriver_object(shared_css, "Shared tag css")
        core_utils.python_left_click(shared_tag_obj)
        time.sleep(5)
        
        """
            STEP 4.1 : Verify only 'ReportA (advanced user)', 'ReportB (advanced user)' and 'Visual1 (advanced user)' items appear.
        """
        main_page.verify_items_in_grid_view(['ReportA (advanced user)', 'ReportB (advanced user)'], 'asequal', "Step 4.1 : Verify only 'ReportA (advanced user)', 'ReportB (advanced user)' and 'Visual1 (advanced user)' items appear")
        
        """
            STEP 5 : Un-Check Shared tag
        """
        personal_tag_obj = utils.validate_and_get_webdriver_object(shared_css, "Shared tag css")
        core_utils.python_left_click(personal_tag_obj)
        time.sleep(5)
        
        """
            STEP 5.1 : Verify all items are displayed related to Search string (*) set under domain HOME-1091.
        """
        main_page.verify_items_in_grid_view(['Chart1', 'Chart2', 'Report1', 'Report2', 'Report3', 'ReportA (advanced user)', 'ReportB (advanced user)'], 'asin', "Step 5.1 : Verify all items are displayed related to Search string (*)")
        
        """
            STEP 6 : Remove search string by clicking on (X) button.
        """
        main_page.search_input_box_options(option_type ='clear')
        utils.synchronize_until_element_disappear(parent_css, main_page.home_page_long_timesleep)
        
        """
            STEP 6.1 : Verify the page reloads & displays default home page Folder view.
        """
        main_page.verify_folders_in_grid_view(['My Content', 'Shared Content', 'Hidden Content'], 'asin', "Step 6.1 : Verify the page reloads & displays default home page Folder view.")
        
        """
            STEP 7 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()