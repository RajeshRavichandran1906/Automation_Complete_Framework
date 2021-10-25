"""-------------------------------------------------------------------------------------------
Created on August 09, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5831429
Test Case Title =  Verify unchecking Shared tag deselects items shared with user
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.core_utility import CoreUtillityMethods
import time

class C5831429_TestClass(BaseTestCase):

    def test_C5831429(self):
        
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
        main_page.select_option_from_crumb_box("Domains")
        utils.synchronize_with_visble_text(locator.content_area_css, 'Public', main_page.home_page_long_timesleep)
        
        """
            STEP 3 : Type * in Search box.
        """
        main_page.search_input_box_options(option_type ='write', input_text_msg= "*")
        utils.synchronize_with_visble_text(".sd-category-buttons", 'Shared', main_page.home_page_long_timesleep*2)
        
        """
            STEP 4 : Check on Shared tag.
        """     
        shared_tag_obj = utils.validate_and_get_webdriver_object(shared_css, "Shared tag")
        core_utils.python_move_to_element(shared_tag_obj)
        time.sleep(3)
        core_utils.python_left_click(shared_tag_obj)
        utils.synchronize_with_visble_text(locator.content_area_css, 'ahtml_001', main_page.home_page_long_timesleep*2, condition_type='asnotin')
        
        """
            STEP 4.1 : Verify only 'ReportA (advanced user)', 'ReportB (advanced user)' and 'Visual1 (advanced user)' items appear.
        """
        main_page.verify_items_in_grid_view(['ReportA (advanced user)', 'ReportB (advanced user)', 'Visual1 (advanced user)'], 'asequal', "Step 04.01 : Verify only 'ReportA (advanced user)', 'ReportB (advanced user)' and 'Visual1 (advanced user)' items appear.")
        
        """
            STEP 5 : Un-Check Shared tag
        """
        core_utils.python_left_click(shared_tag_obj)
        utils.synchronize_with_visble_text(locator.content_area_css, 'ahtml_001', main_page.home_page_long_timesleep*2)
        
        """
            STEP 5.1 : Verify all items are displayed related to Search string (*)
        """ 
        options = ['138356dyntable', '180625020', '2017-01-19-CHART-2212-autodrillLineChart', '22083556', '61862521c', 'Accesible LaunchPage (Public)', 'ahtml_001', 'Angular', 'AR_AHTML_001', 'arc1', 'arc2', 'arc3', 'arc4', 'ASesriMap12-30-16', 'bad_colors', 'Bar', 'Bubble', 'C2035228', 'C6668722_base', 'carinst', 'Chart']
        main_page.verify_items_in_grid_view(options, 'asin', "Step 05.01 : Verify all items are displayed related to Search string (*)")
        
        """
            STEP 6 : Remove search string by clicking on (X) button.
        """
        main_page.search_input_box_options(option_type ='clear')
        utils.synchronize_with_visble_text(locator.content_area_css, 'ahtml_001', main_page.home_page_long_timesleep*2, condition_type='asnotin')
        
        """
            STEP 6.1 : Verify the page reloads & displays default home page Folder view.
        """ 
        main_page.verify_folders_in_grid_view(['HOME-1091', 'HOME-1091A', 'Public'], 'asin', "Step 06.01 : Verify the page reloads & displays default home page Folder view.")
        
        """
            STEP 7 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
