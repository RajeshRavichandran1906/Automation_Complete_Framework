"""-------------------------------------------------------------------------------------------
Author : Prabhakaran
Automated On : 08-August-2019
-------------------------------------------------------------------------------------------"""

from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C5831426_TestClass(BaseTestCase):

    def test_C5831426(self):
        
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
        purple_rgba = "rgba(147, 112, 219, 0.3)"
        blue_rgba = "rgba(35, 183, 229, 0.3)"
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
            Verify Shared and Personal tags appear in 'Purple'.
            Verify A,B,C,D,E,F and G tags appear in 'Blue'.
        """
        homepage.search_input_box_options(option_type ='write', input_text_msg= "*")
        utils.synchronize_with_visble_text(category_buttons_css, "Shared", homepage.home_page_long_timesleep)
        
        category_objects = utils.validate_and_get_webdriver_objects(category_buttons_css, "Home page category buttons")
        actual_purple_tags = [category.text.strip() for category in category_objects if category.value_of_css_property("background-color") == purple_rgba]
        actual_blue_tags = [category.text.strip() for category in category_objects if category.value_of_css_property("background-color") == blue_rgba]
        
        expected_purple_tags = ['Shared', 'Personal']
        expected_blue_tags = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        utils.verify_list_values(expected_purple_tags, actual_purple_tags, "Step 03.01 : Verify Shared and Personal tags appear in 'Purple'", "asin")
        utils.verify_list_values(expected_blue_tags, actual_blue_tags, "Step 03.02 : Verify A,B,C,D,E,F and G tags appear in 'Blue'", "asin")
        
        """
            STEP 04 : Remove search string by clicking on (X) button.
            Verify the page reloads & displays default home page view of folders/items under HOME-1091.
        """
        homepage.search_input_box_options(option_type ='clear')
        utils.synchronize_until_element_disappear(category_buttons_css,  homepage.home_page_medium_timesleep, pause_time=4)
        homepage.verify_folders_in_grid_view(['My Content', 'Shared Content', 'Hidden Content'], 'asin', "Step 04.01 : Verify the page reloads & displays default home page view of folders/items under HOME-1091")
        
        """
            STEP 05 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()
        