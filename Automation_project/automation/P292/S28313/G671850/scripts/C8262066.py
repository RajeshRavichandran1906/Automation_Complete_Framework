"""-------------------------------------------------------------------------------------------
Created on May 27, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262066
Test Case Title =  Maximize Container with OverFlow
-----------------------------------------------------------------------------------------------"""

from common.locators.wf_mainpage_locators import WfMainPageLocators as homepage_locators
from common.wftools.designer_chart import Designer_Chart
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
import time

class C8262066_TestClass(BaseTestCase):

    def test_C8262066(self):
        
        """
            CLASS OBJECTS 
        """
        pd_design = page_designer.Design(self.driver)
        pd_preview = page_designer.Preview(self.driver)
        pd_run = page_designer.Run(self.driver)
        designer_chart = Designer_Chart(self.driver)
        wf_login = Login(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        homepage = Wf_Mainpage(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        LONG_TIME = 60
        MEDIUM_TIME = 30
        PAGE_NAME = "C8262066"
        FOLDER_PATH = "P292_S28313->G671850"
        EXPECTED_TABS = ['Tab 1', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5', 'Tab 6', 'Tab 7', 'Tab 8', 'Tab 9']
        
        """
            STEP 01 : Login WF as domain developer
        """
        wf_login.invoke_home_page("mrid", "mrpass")
        pd_design.wait_for_visible_text(homepage_locators.CONTENT_CSS, "Content", LONG_TIME)
        
        """
            STEP 02 : Click on Content View from side bar
        """
        homepage.select_content_from_sidebar()
        
        """
            STEP 03 : Click on 'P292_S28313' domain -> G671850 folder
        """
        homepage.expand_repository_folder(FOLDER_PATH)
        
        """
            STEP 04 : Click on Workbook action tile from under Designer category
        """
        homepage.select_action_bar_tab("Designer")
        homepage.select_action_bar_tabs_option("Workbook")
        pd_design.wait_for_visible_text(".open-dialog-resources", "Open", MEDIUM_TIME)
        
        """
            STEP 05 : Choose wf_retail_lite.mas and click select
        """
        homepage.select_file_or_folder_from_resource_dialog("baseapp", "double")
        homepage.select_file_or_folder_from_resource_dialog("wf_retail_lite.mas", "double")
        core_utils.switch_to_new_window()
        designer_chart.wait_for_visible_text(".dimension-label", "Dimensions", LONG_TIME)
        
        """
            STEP 06 : Double click add Revenue and Product Category fields
        """
        designer_chart.double_click_on_measures_field("Sales->Revenue")
        designer_chart.wait_for_visible_text("text.yaxis-title", "Revenue", MEDIUM_TIME)
        
        designer_chart.double_click_on_dimension_field("Product->Product->Product,Category")
        designer_chart.wait_for_visible_text("text.xaxisOrdinal-title", "Product Category", MEDIUM_TIME)
        
        """
            STEP 07 : Click on the Embedded Page tab at the left bottom corner
        """
        embedded_page  = self.driver.find_element_by_css_selector("div[title='New embedded page']")
        core_utils.left_click(embedded_page)
        pd_design.wait_for_visible_text(".pd-new-page", "Blank", MEDIUM_TIME)
        
        """
            STEP 08 : Choose blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-title", "Page Heading", LONG_TIME)
        
        """
            STEP 09 : Drag a tab container onto the page
        """
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Tab", 1)
        
        """
            STEP 10 : Add 8 more tabs to panel1 by clicking on Add new tab icon
        """
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon()
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon()
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon()
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon()
        
        pd_design.tab_container("Panel 1").click_tab_overflow_icon()
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon_in_tab_overflow_popup()
        
        pd_design.tab_container("Panel 1").click_tab_overflow_icon()
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon_in_tab_overflow_popup()
        
        pd_design.tab_container("Panel 1").click_tab_overflow_icon()
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon_in_tab_overflow_popup()
        
        pd_design.tab_container("Panel 1").click_tab_overflow_icon()
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon_in_tab_overflow_popup()
        
        """
            STEP 11 : Click on the Overflow icon (Ellipsis)
        """
        pd_design.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 11 : Expected - Verify all Tab1, Tab2, Tab3, Tab4, Tab5, Tab6, Tab7,Tab8 appears and Tab 9 is in bold with a + button
        """
        pd_design.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(EXPECTED_TABS, "11.01")
        pd_design.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 9"], "11.02")
        pd_design.tab_container("Panel 1").verify_new_tab_plus_icon_displayed_in_tab_overflow_popup("11.03")
        
        """
            STEP 12 : Click the Preview button
        """
        pd_design.click_preview()
        
        """
            STEP 13 : Maximize panel1
        """
        pd_preview.tab_container("Panel 1").maximize()
        
        """
            STEP 13 : Expected - Verify ellipsis does not appears as all the tabs can be displayed
        """
        pd_preview.tab_container("Panel 1").verify_tab_overflow_icon_not_displayed("13.01")
        pd_preview.tab_container("Panel 1").verify_tabs(EXPECTED_TABS, "13.02")
        
        """
            STEP 14 : Resize the browser
        """
        self.driver.minimize_window()
        time.sleep(3)
        self.driver.set_window_size(400, 600)
        time.sleep(5)
        
        """
            STEP 14 : Expected - Verify ellipsis now appears 
        """
        pd_preview.tab_container("Panel 1").verify_tab_overflow_icon_displayed("14.01")
        
        """
            STEP 15 : Click on the Overflow icon (Ellipsis)
        """
        pd_preview.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 15 : Expected - Verify user can see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6, Tab7,Tab8, Tab9 and NO + sign as the panel is locked.
        """
        pd_preview.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(EXPECTED_TABS, "15.01")
        pd_preview.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("15.02")
        
        """
            STEP 16 : Resize the browser
        """
        self.driver.maximize_window()
        time.sleep(5)
        
        """
            STEP 16 - Expected - Verify ellipsis does not appears as all the tabs can be displayed
        """
        pd_preview.tab_container("Panel 1").verify_tab_overflow_icon_not_displayed("16.01")
        pd_preview.tab_container("Panel 1").verify_tabs(EXPECTED_TABS, "16.02")
        
        """
            STEP 17 : Close the Preview
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 18 : Save page as 'C8262066' and close designer
        """
        pd_design.save_page_from_toolbar(PAGE_NAME)
        pd_design.switch_to_previous_window()
        
        """
            STEP 18 : Expected - Verify 'C8262066' page appears in the content area
        """
        homepage.expand_repository_folder(FOLDER_PATH)
        homepage.verify_items_in_grid_view([PAGE_NAME], "asin", "Step 18.01 : Verify 'C8262066' page appears in the content area")
        
        """
            STEP 19 : Right click on 'C8262066' and select Run in New Window
        """
        pd_design.run_page_designer_in_new_window(PAGE_NAME, folder_path=FOLDER_PATH)
        
        """
            STEP 20 : Maximize Panel1
        """
        pd_run.tab_container("Panel 1").maximize()
        
        """
            STEP 20 : Expected - Verify ellipsis does not appears as all the tabs can be displayed
        """
        pd_run.tab_container("Panel 1").verify_tab_overflow_icon_not_displayed("20.01")
        pd_run.tab_container("Panel 1").verify_tabs(EXPECTED_TABS, "20.02")
        
        """
            STEP 21 : Resize the browser
        """
        self.driver.minimize_window()
        self.driver.set_window_size(400, 600)
        
        """
            STEP 22 - Click on the Overflow icon (Ellipsis) 
        """
        pd_run.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 22 - Expected - Verify user can see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6, Tab7,Tab8, Tab9 and NO + sign as the panel is locked.
        """
        pd_run.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(EXPECTED_TABS, "22.01")
        pd_run.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("22.02")
        
        """
            STEP 23 : Resize the browser
        """
        self.driver.maximize_window()
        
        """
            STEP 23 - Expected - Verify ellipsis does not appears as all the tabs can be displayed
        """
        pd_run.tab_container("Panel 1").verify_tab_overflow_icon_not_displayed("23.01")
        pd_run.tab_container("Panel 1").verify_tabs(EXPECTED_TABS, "23.02")
        
        """
            STEP 24 : Close page in new window
        """
        pd_run.switch_to_previous_window()
        
        """
            STEP 25 : Signout WF
        """