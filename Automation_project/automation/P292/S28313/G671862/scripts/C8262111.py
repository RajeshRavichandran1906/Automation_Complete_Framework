"""-------------------------------------------------------------------------------------------
Created on May 30, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262111
Test Case Title = Search Tree
-----------------------------------------------------------------------------------------------"""
from common.locators.wf_mainpage_locators import WfMainPageLocators as homepage_locators
from common.locators.page_designer_design import ContentTab as ContentTab_Locators
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.javascript import JavaScript
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.login import Login
from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
import time

class C8262111_TestClass(BaseTestCase):

    def test_C8262111(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design = page_designer.Design(self.driver)
        home_page = Wf_Mainpage(self.driver)
        login_page = Login(self.driver)
        utils = UtillityMethods(self.driver)
        javascript = JavaScript(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
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
            Click on Page action tile from under Designer category
        """
        home_page.expand_repository_folder(FOLDER_PATH)
        home_page.select_action_bar_tab("Designer")
        home_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text(".pd-new-page", "Grid 2-1", LONG_TIME)
        
        """
            STEP 04 : Choose Grid 2-1 template
        """
        pd_design.select_page_designer_template("Grid 2-1")
        pd_design.wait_for_visible_text(".pd-page-title", "Page Heading", LONG_TIME)
        
        """
            STEP 05 : Navigate to Domains node in the tree
        """
        pd_design.collapse_content_folder(COLLAPSE_FOLDER_PATH)
        
        """
            STEP 06 : Type 'Category' in the search box
        """
        pd_design.search_content("Category")
        pd_design.wait_for_visible_text(ContentTab_Locators.EXPANDED_CONTENT_ITEMS_CSS, "Category", MEDIUM_TIME)
        
        """
            STEP 06 - Expected : Verify list of fexes having category in their title shows up
        """
        pd_design.verify_content_items_contain_specific_text("Category", "06.00")
        
        """
            STEP 07 : Hover over 'Category Sales' report
             Expected - Verify the tool tip shows the location of the fex as below
        """
        expected_tooltip = "IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Category_Sales.fex"
        content_item_css = "div[title='{0}']".format(expected_tooltip)
        content_item_obj = self.driver.find_element_by_css_selector(content_item_css)
        javascript.scrollIntoView(content_item_obj)
        time.sleep(2)
        utils.verify_object_visible(content_item_css, True, "Step 07.00 : Verify tooltip displayed after hover mouse on category sales")
        
        """
            STEP 08 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
        
        """
            STEP 09 : Signout WF
        """