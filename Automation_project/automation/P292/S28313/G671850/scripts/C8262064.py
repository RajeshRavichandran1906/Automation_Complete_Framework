"""-------------------------------------------------------------------------------------------
Created on May 28, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8262064
Test Case Title =  Workbook with Locked Tab Container
-----------------------------------------------------------------------------------------------"""

from common.locators.wf_mainpage_locators import WfMainPageLocators as homepage_locators
from common.wftools.designer_chart import Designer_Chart
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.lib.utillity import UtillityMethods

class C8262064_TestClass(BaseTestCase):

    def test_C8262064(self):
        
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
        utils = UtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        LONG_TIME = 60
        MEDIUM_TIME = 30
        PAGE_NAME = "C8262064"
        FOLDER_PATH = "P292_S28313->G671850"
        
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
            STEP 19 : Save page as 'C8262064' and close Designer
        """
        pd_design.save_page_from_toolbar(PAGE_NAME)
        pd_design.switch_to_previous_window()
        
        """
            STEP 19 : Expected - Verify the page appears in the content area
        """
        homepage.expand_repository_folder(FOLDER_PATH)
        homepage.verify_items_in_grid_view([PAGE_NAME], "asin", "Step 19.01 : Verify the page appears in the content area")
        
        """
            STEP 20 : Right click on 'C8262064' and select Run
        """
        pd_design.run_page_designer(PAGE_NAME, FOLDER_PATH)
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text(".pd-page-title", "Page Heading", MEDIUM_TIME)
        
        """
            STEP 20 - Expected - Verify the page appears and you see the overflow icon at the top right corner
        """
        pd_run.tab_container("Panel 1").verify_tab_overflow_icon_displayed("20.01")
        
        """
            STEP 21 : Click on the Overflow icon (Ellipsis)
        """
        pd_run.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 21 - Expected : Verify that Tab1 is in bold and NO + button
        """
        pd_run.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 1"], "21.01")
        pd_run.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("21.02")
        
        """
            STEP 22 - Choose Tab 4
        """
        pd_run.tab_container("Panel 1").select_tab_from_tab_overflow_popup("Tab 4")
        
        """
            STEP 22 - Expected - Verify Tab 4 is now in view
        """
        pd_run.tab_container("Panel 1").verify_selected_tab(["Tab 4"], "22.01")
        
        """
            STEP 23 : Click on the Overflow icon (Ellipsis)
        """
        pd_run.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 23 - Expected - Verify that Tab 4 is in bold and NO + button
        """
        pd_run.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 4"], "23.01")
        pd_run.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("23.02")
        
        """
            STEP 24 : Click the Open in new Window button
        """
        pd_run.switch_to_default_page()
        new_wind = self.driver.find_element_by_css_selector("[title='Open in new window']")
        core_utils.left_click(new_wind)
        core_utils.switch_to_new_window()
        pd_run.wait_for_visible_text(".pd-page-title", "Page Heading", LONG_TIME)
        
        """
            STEP 25 : Click on the Overflow icon (Ellipsis)
        """
        pd_run.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 25 - Expected : Verify that Tab1 is in bold and NO + button
        """
        pd_run.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 1"], "25.01")
        pd_run.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("25.02")
        
        """
            STEP 26 : Choose Tab 4
        """
        pd_run.tab_container("Panel 1").select_tab_from_tab_overflow_popup("Tab 4")
        
        """
            STEP 26 - Expected - Verify Tab 4 is now in view
        """
        pd_run.tab_container("Panel 1").verify_selected_tab(["Tab 4"], "26.01")
        
        """
            STEP 27 : Click on the Overflow icon (Ellipsis)
        """
        pd_run.tab_container("Panel 1").click_tab_overflow_icon()
        
        """
            STEP 27 - Expected : Verify that Tab 4 is in bold and NO + button
        """
        pd_run.tab_container("Panel 1").verify_selected_tab_in_tab_overflow_popup(["Tab 4"], "27.01")
        pd_run.tab_container("Panel 1").verify_new_tab_plus_icon_not_displayed_in_tab_overflow_popup("27.02")
        
        """
            STEP 28 : Close page in new window
        """
        pd_run.switch_to_previous_window()
        utils.synchronize_with_visble_text(homepage_locators().CONTENT_CSS, "Content", homepage.home_page_long_timesleep)
        
        """
            STEP 29 : Sign out WF
        """
        homepage.signout_from_username_dropdown_menu()