"""-------------------------------------------------------------------------------------------
Author : Vishnu_priya
Automated On : 08-August-2019
-------------------------------------------------------------------------------------------"""

from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators
import time

class C5831427_TestClass(BaseTestCase):

    def test_C5831427(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
        
        """
            COMMON VARIABLES
        """
        category_buttons_css = ".sd-category-buttons .sd-category-button"
     
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        login.invoke_home_page('mrid', 'mrpass')
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", homepage.home_page_long_timesleep)
        
        """
            STEP 02 : Under Domain tree >> Click on HOME-1091
        """
        homepage.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, homepage.home_page_short_timesleep)
        homepage.expand_repository_folder("Domains->HOME-1091")
        utils.synchronize_with_visble_text(locator.content_area_css, "My Content", homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Type * in Search box.
        """
        homepage.search_input_box_options(option_type ='write', input_text_msg= "*")
        utils.synchronize_with_visble_text(category_buttons_css, "Shared", homepage.home_page_long_timesleep)
        
        """
            STEP 04: Check Personal tag.
            Verify only 'Report1', 'Report2' and 'Report3' appear under Items.
        
        """
        homepage.check_tags_in_homepage("Personal")
        time.sleep(5)
        homepage.verify_items_in_grid_view(['Report1', 'Report2', 'Report3'],'asequal',msg="Step 04:Verify only 'Report1', 'Report2' and 'Report3' appear under Items ")
        
        """
            STEP 05: Un-Check Personal tag.
            Verify all items are displayed related to Search string (*) set under domain HOME-1091.
        """
        homepage.check_tags_in_homepage("Personal")
        time.sleep(5)
        homepage.verify_items_in_grid_view(['Chart1', 'Chart2', 'Report1', 'Report2', 'Report3', 'ReportA (advanced user)', 'ReportB (advanced user)'],'asequal',msg="Step 04:Verify only 'Report1', 'Report2' and 'Report3' appear under Items ")
        
        """
            STEP 06 : Remove search string by clicking on (X) button.
            Verify the page reloads & displays default home page view of folders/items under HOME-1091.
        """
        homepage.search_input_box_options(option_type ='clear')
        utils.synchronize_until_element_disappear(category_buttons_css,  homepage.home_page_medium_timesleep, pause_time=4)
        homepage.verify_folders_in_grid_view(['My Content', 'Shared Content', 'Hidden Content'], 'asin', "Step 04.01 : Verify the page reloads & displays default home page view of folders/items under HOME-1091")
        
        """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()
        