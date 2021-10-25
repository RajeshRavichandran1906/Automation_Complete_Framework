"""-------------------------------------------------------------------------------------------
Created on May 29, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262110
Test Case Title = Search Tree
-----------------------------------------------------------------------------------------------"""
from common.locators.wf_mainpage_locators import WfMainPageLocators as homepage_locators
from common.locators.page_designer_design import ContentTab as ContentTab_Locators
from common.lib.javascript import JavaScript
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.login import Login
from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer

class C8262110_TestClass(BaseTestCase):

    def test_C8262110(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design = page_designer.Design(self.driver)
        home_page = Wf_Mainpage(self.driver)
        login_page = Login(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        javascript = JavaScript(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        LONG_TIME = 60
        MEDIUM_TIME = 30
        FOLDER_PATH = "P292_S28313->G671862"
        COLLAPSE_FOLDER_PATH = "G671862->P292_S28313"
        
        """
            STEP 01 : Login WF as domain developer
        """
        login_page.invoke_home_page("mrid", "mrpass")
        pd_design.wait_for_visible_text(homepage_locators.CONTENT_CSS, "Content", LONG_TIME)
        
        """
            STEP 02 : Click on Content View from side bar
        """
        home_page.select_content_from_sidebar()
        
        """
            STEP 03 : Click on P292_S28313 domain -> G671862 folder
        """
        home_page.expand_repository_folder(FOLDER_PATH)
        
        """
            STEP 04 : Click on Page action tile from under Designer category
        """
        home_page.select_action_bar_tab("Designer")
        home_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text(".pd-new-page", "Blank", LONG_TIME)
        
        """
            STEP 05 : Choose blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-title", "Page Heading", LONG_TIME)
        
        """
            STEP 06 : Navigate to Domains node in the tree
        """
        pd_design.collapse_content_folder(COLLAPSE_FOLDER_PATH)
        
        """
            STEP 07 : Type 'Category' in the search box
        """
        pd_design.search_content("Category")
        pd_design.wait_for_visible_text(ContentTab_Locators.EXPANDED_CONTENT_ITEMS_CSS, "Category", MEDIUM_TIME)
        
        """
            STEP 07 - Expected : Verify list of fexes having category in their title shows up
        """
        pd_design.verify_content_items_contain_specific_text("Category", "07.01")
        
        """
            STEP 08 : Scroll down the list
            STEP 08 - Expected :  Verify user can scroll down with no issues
        """
        content_items_list = self.driver.find_elements_by_css_selector(ContentTab_Locators.EXPANDED_CONTENT_ITEMS_CSS)
        last_content_item_text = javascript.get_elements_text(content_items_list)[-1]
        pd_design.find_content_item_and_scroll_into_view(last_content_item_text)
        
        """
            STEP 09 : Type 'margin' in the search box
        """
        pd_design.click_clear_content_search()
        pd_design.search_content("margin")
        pd_design.wait_for_visible_text(ContentTab_Locators.EXPANDED_CONTENT_ITEMS_CSS, "Margin", MEDIUM_TIME)
        
        """
            STEP 09 - Expected : Verify list of fexes having margin in their title shows up
        """
        pd_design.verify_content_items_contain_specific_text("margin", "09.01")
        
        """
            STEP 10 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        
        """
            STEP 11 : Signout WF
        """