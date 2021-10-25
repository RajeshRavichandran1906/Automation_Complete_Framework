"""-------------------------------------------------------------------------------------------
Created on June 4th, 2019
@author: Varun\Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262065
Test Case Title =  Workbook with Unlocked Tab Container
-----------------------------------------------------------------------------------------------"""

from common.wftools.designer_chart import Designer_Chart
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.locators import wf_mainpage_locators
from common.pages.portal_canvas import Portal_canvas
from common.lib import utillity
import time

class C8262065_TestClass(BaseTestCase):

    def test_C8262065(self):
        
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
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        portal_canvas = Portal_canvas(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        LONG_TIME = 60
        MEDIUM_TIME = 30
        PAGE_NAME = "C8262065"
        FOLDER_PATH = "P292_S28313->G671850"
        ACTION_TILE = 'Designer'
        ACTION_BAR = 'Workbook'
        
        """
            STEP 01 : Login WF as domain developer
        """
        wf_login.invoke_home_page("mrid", "mrpass")
        
        """
            STEP 02 : Click on Content View from side bar
        """
        homepage.select_content_from_sidebar()
        
        """
            STEP 03 : Click on 'P292_S28313' domain -> G671850 folder
        """
        homepage.expand_repository_folder(FOLDER_PATH)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, ACTION_TILE, homepage.home_page_medium_timesleep)
        
        """
            STEP 04 : Click on Workbook action tile from under Designer category
        """
        homepage.select_action_bar_tab(ACTION_TILE)
        homepage.select_action_bar_tabs_option(ACTION_BAR)
        pd_design.wait_for_visible_text(".open-dialog-resources", "Open", MEDIUM_TIME)
        
        """
            STEP 05 : Choose wf_retail_lite.mas and click select
        """
        pd_design.resource_dialog().select_file("wf_retail_lite.mas", "baseapp")
        pd_design.resource_dialog().click_button("Select")
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
            STEP 10 : Add 4 more tabs to the same panel using + icon in tab panel
        """
        for _ in range(4) :
            pd_design.tab_container("Panel 1").click_new_tab_plus_icon()
            
        """
            STEP 10 : Expected - Verify Panel 1 has 5 tabs as shown below
        """
        pd_design.tab_container("Panel 1").verify_tabs(["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5"], "10.01")
        
        """
            STEP 11 : Click on the Overflow icon (Ellipsis)
        """
        pd_design.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 11 : Expected - Verify Tab1, Tab2, Tab3, Tab4 and Tab5 are listed as below
        """
        pd_design.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5"], "11.01")
        
        """
            STEP 12 : Click the + button
        """
        pd_design.tab_container("Panel 1").click_new_tab_plus_icon_in_tab_overflow_popup()
        
        """
            STEP 12 : Expected - Verify Tab 6 is added
        """
        pd_design.tab_container("Panel 1").verify_tabs(["Tab 6"], "12.01", "asin")
        
        """
            STEP 13 : Click on the Overflow icon (Ellipsis)
        """
        pd_design.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 13 : Expected - Verify user see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6 and the + sign
        """
        pd_design.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5", "Tab 6"], "13.01")
        pd_design.tab_container("Panel 1").verify_new_tab_plus_icon_displayed_in_tab_overflow_popup("13.02")
        
        """
            STEP 14 : Click the Preview button
        """
        pd_design.click_preview()
        
        """
            STEP 15 : Click on the Overflow icon (Ellipsis)
        """
        pd_preview.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 15 : Expected - Verify user see Tab1, Tab2, Tab3, Tab4, Tab5, Tab6 but NO + sign because the panel is locked.
        """
        pd_preview.tab_container("Panel 1").verify_tabs_in_tab_overflow_popup(["Tab 1", "Tab 2", "Tab 3", "Tab 4", "Tab 5", "Tab 6"], "15.01")
        pd_preview.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("15.02")
        
        """
            STEP 16 : Click on Tab 1
        """
        pd_preview.tab_container("Panel 1").select_tab_from_tab_overflow_popup("Tab 1")
        
        """
            STEP 16 - Expected - Verify Tab 1 is now in View
        """
        pd_preview.tab_container("Panel 1").verify_selected_tab(["Tab 1"], "16.01")
        
        """
            STEP 17 : Click on the Overflow icon (Ellipsis)
        """
        pd_preview.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 17 - Expected - Verify that Tab1 is in bold
        """
        pd_preview.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 1"], "17.01")
        
        """
            STEP 18 : Close the Preview
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 19:Select Panel1 and click open the properties pane
        """
        pd_design.select_container("Panel 1")
        pd_design.click_property()
        
        """
            STEP 20:In the content customization section Turn off Lock Content switch
        """
        check_box_objs=util_obj.validate_and_get_webdriver_objects("div[data-ibx-type='ibxGrid']>div[class^='pd-ps'][role='checkbox']", "Check box objects")
        lock_content=check_box_objs[3]
        core_utils.left_click(lock_content)
        
        """
            STEP 20 - Expected:Verify that now all the items under that section are enabled;
            Verify that now You see a + in the middle of each tab
        """
        pd_design.tab_container("Panel 1").verify_add_content_button_displayed("20.01")
        time.sleep(15)
        
        """
            STEP 21:Hover over + sign
            Verify 'Add Content' tool tip appears
        """        
        add_button_obj = util_obj.validate_and_get_webdriver_object("div[class^='pd-page-acc-section'] div[class$='tpg-selected'] div[class^='cont-es-button']", "plus button css")
        portal_canvas.verify_canvas_button_tooltip(add_button_obj, "Add content", "Step 21.01 : Verify 'Add Content' tool tip appears")
        
        """
            STEP 22:Go to Preview
        """
        pd_design.click_preview()
        
        """
            STEP 23:Click on the Overflow icon (Ellipsis)
        """
        pd_design.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 23.01:Verify that Tab1 is in bold and you see a + sign at the bottom
        """
        pd_design.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 1"], "23.01")
        pd_design.tab_container("Panel 1").verify_add_content_button_displayed("23.02")
        
        """
            STEP 24: Click the + button
        """
        pd_design.tab_container("Panel 1").click_add_content_button()
        
        """
            STEP 24.01: Verify Select Item dialog opens with Domains open
        """
        homepage.verify_resource_dialog_is_visible(True, "Step 24.01 : Verify Select Item dialog opens with Domains open")
        
        """
            STEP 25: Navigate to Retail Samples --> Portal --> Small widget. Choose 'Category sales'
        """
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Category Sales")
        
        """
            STEP 26: Click the Add button
        """
        pd_design.resource_dialog().click_button("Add")
        
        """
        STEP 26 - Expected:Verify that the report appears and now the quick filter icon appeared next to refresh
        """
        expected_tabs_list=['Category Sales', 'Tab 2', 'Tab 3', 'Tab 4', 'Tab 5']
        pd_design.tab_container("Panel 1").verify_tabs(expected_tabs_list, "26.01")
        pd_design.verify_page_header_visible_buttons(['Refresh', 'Show filters'], "Step 26.02 : quick filter icon appeared next to refresh")
        
        """
            STEP  27: Click on back to get back to page design mode
        """
        pd_run.go_back_to_design_from_preview()
        
        """
            STEP 28 : Save page as 'C8262065' and close Designer
        """
        pd_design.save_page_from_toolbar(PAGE_NAME)
        pd_design.switch_to_previous_window()
        
        """
            STEP 28 - Expected - Verify the page appears in the content area
        """
        homepage.expand_repository_folder(FOLDER_PATH)
        homepage.verify_items_in_grid_view([PAGE_NAME], "asin", "Step 28.01 : Verify the page appears in the content area")
        
        """
            STEP 29 : Right click on 'C8262065' and choose Run in new window menu
        """
        homepage.right_click_folder_item_and_select_menu(PAGE_NAME,"Run in new window")
        core_utils.switch_to_new_window()
        pd_run.wait_for_visible_text(".pd-page-title", "Page Heading", MEDIUM_TIME)
        
        """
            STEP 29 - Expected - Verify the page appears and you see the overflow icon at the top right corner
        """
        pd_run.tab_container("Panel 1").verify_tab_overflow_icon_displayed("29.01")
        
        """
            STEP 30 : Click on the Overflow icon (Ellipsis)
        """
        pd_run.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 30 - Expected : Verify that Tab1 is in bold and you see a + sign at the bottom
        """
        pd_run.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Category Sales"], "30.01")
        pd_run.tab_container("Panel 1").verify_new_tab_plus_icon_displayed_in_tab_overflow_popup("30.02")
        
        """
            STEP 31 - Click Remove
        """
        pd_run.select_container_option("Panel 1", "Remove")
        
        """
            STEP 31 - Expected : Verify Category Sales has been removed and title becomes Tab1
        """
        pd_run.tab_container("Panel 1").verify_selected_tab(["Tab 1"], "31.01")
       
        """
            STEP 32 : Click on (+) in the middle of Panel1 and Choose 'Category Sales' from Retail Samples -> Portal -> Small widget
        """
        pd_run.tab_container("Panel 1").click_add_content_button()
        pd_design.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->Portal->Small Widgets", "Category Sales")
        pd_design.resource_dialog().click_button("Add")
        
        """
            STEP 32 - Expected : Verify 'Category Sales' has been added to the panel
        """
        pd_run.tab_container("Panel 1").verify_selected_tab(["Category Sales"], "32.01")
        
        """
            STEP 33 : Click on the Overflow icon (Ellipsis)
        """
        pd_run.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 33 - Expected : Verify that Tab1 is in bold and  + icon
        """
        pd_run.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Category Sales"], "33.01")
        pd_run.tab_container("Panel 1").verify_new_tab_plus_icon_displayed_in_tab_overflow_popup("33.02")
        
        """
            STEP 34 - Click Replace
        """
        pd_run.select_container_option("Panel 1", "Replace")
        
        """
            Step 35: Navigate to 'Retail Samples' --> Portal --> Small widget , Select 'Regional sales trend' and click on Add button
        """
        pd_design.resource_dialog().navigate_to_folder_and_select_file(None, "Regional Sales Trend")
        pd_design.resource_dialog().click_button("Add")
        
        """
            STEP 35 - Expected : Verify 'Regional sales trend' has been added
        """
        pd_run.tab_container("Panel 1").verify_selected_tab(["Regional Sales Trend"], "35.01")
        
        """
            STEP 36 : Close page in new window
        """
        pd_run.switch_to_previous_window()
        
        """
            STEP 37 : Sign out WF
        """
        