"""-------------------------------------------------------------------------------------------
Created on August 07, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831422
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

class C5831422_TestClass(BaseTestCase):

    def test_C5831422(self):
        
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
        personel_css = ".sd-category-buttons div[data-ibx-type='ibxButton']:nth-child(2)"
            
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
        main_page.select_option_from_crumb_box("Domains")
        time.sleep(10)
        
        """
            STEP 3 : Type * in Search box.
        """
        main_page.search_input_box_options(option_type ='write', input_text_msg= "*")
        utils.synchronize_until_element_is_visible(".sd-category-buttons", main_page.home_page_long_timesleep)
        
        """
            STEP 4 : Check Personal tag
        """
        personal_tag_obj = utils.validate_and_get_webdriver_object(personel_css, "Personal tag css")
        core_utils.python_left_click(personal_tag_obj)
        time.sleep(5)
        
        """
            STEP 4.1 : Verify only 'Report1', 'Report2', 'Report3' and 'Document1' appear under Items.
        """
        main_page.verify_items_in_grid_view(['Document1', 'Report1', 'Report2', 'Report3'], 'asequal', "Step 4.1 : Verify only 'Report1', 'Report2', 'Report3' and 'Document1' appear under Items.")
        
        """
            STEP 5 : Un-Check Personal tag
        """
        personal_tag_obj = utils.validate_and_get_webdriver_object(personel_css, "Personal tag css")
        core_utils.python_left_click(personal_tag_obj)
        time.sleep(5)
        
        """
            STEP 5.1 : Verify all items are displayed related to Search string (*)
        """
        main_page.verify_items_in_grid_view(['138356dyntable', '180625020', '2017-01-19-CHART-2212-autodrillLineChart', '22083556', '61862521c', 'Accesible LaunchPage (Public)', 'ahtml_001', 'Angular', 'AR_AHTML_001', 'arc1', 'arc2', 'arc3', 'arc4', 'ASesriMap12-30-16', 'bad_colors', 'Bar', 'Bubble', 'C2035228', 'C6668722_base', 'carinst', 'Chart'], 'asin', "Step 5.1 : Verify all items are displayed related to Search string (*)")
        
        """
            STEP 6 : Remove search string by clicking on (X) button.
        """
        main_page.search_input_box_options(option_type ='clear')
        utils.synchronize_until_element_disappear(parent_css, main_page.home_page_long_timesleep)
        
        """
            STEP 6.1 : Verify the page reloads & displays default home page Folder view.
        """
        main_page.verify_folders_in_grid_view(['HOME-1091', 'HOME-1091A', 'Public'], 'asin', "Step 6.1 : Verify the page reloads & displays default home page Folder view.")
        
        """
            STEP 7 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()