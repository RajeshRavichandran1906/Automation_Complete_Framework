"""-------------------------------------------------------------------------------------------
Created on July 31, 2019
@author: Niranjan

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/5823630&group_by=cases:section_id&group_id=170586&group_order=asc
Test Case Title =  Edit page with filter controls
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design,Run
from common.wftools.wf_mainpage import Wf_Mainpage, Run as R
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools.chart import Chart
from selenium.webdriver import ActionChains
import time

class C5823630_TestClass(BaseTestCase):

    def test_C5823630(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        pd_run = Run(self.driver)
        main_page = Wf_Mainpage(self.driver)
        main_run = R(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = WfMainPageLocators()
        chart = Chart(self.driver)
        ac = ActionChains(self.driver)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"
        
        """
            STEP 1 : Login WF as domain developer;
            Click on Content view from side bar.
        """
        login.invoke_home_page('mrid', 'mrpass')
        
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        """
            STEP 2 : Expand 'P292_S10660' domain;
            Click on 'G192933' folder and choose Page action tile from under designer category.
        """
        main_page.expand_repository_folder("P292_S10660->G192933")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
        
        """
            STEP 3 : Choose the Grid 2-1 template.
        """
        pd_design.select_page_designer_template("Grid 2-1")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
            
        """
            STEP 4 : Click on "G192933 > P292_S10660" domain to two level up;
            Navigate to Retail samples --> Portal --> Small Widgets folder.
        """
        pd_design.select_option_from_carousel_items("Content")
        pd_design.collapse_content_folder("G192933")
        pd_design.collapse_content_folder("P292_S10660")
        pd_design.expand_content_folder("Retail Samples->Portal->Small Widgets")
        
        """
            STEP 5 : Drag and drop Category Sales report on to the Panel 1.
        """
        source_element = utils.validate_and_get_webdriver_object("div[class*='tnode-is-container']:nth-child(1)", "Category sales css")
        target_element = utils.validate_and_get_webdriver_object("div[class*='ui-resizable ui-resizable-autohide'][data-gs-x='0'][data-gs-height='6']", "Panel 1 css")
        
        ac.drag_and_drop(source_element, target_element).perform()
        pd_design.wait_for_visible_text(".ibxtool-filter-notif-popup.pop-top", "You")
        
        """
            STEP 5.1 : Verify pop-up appears in the page after adding report with parameters.
        """
        pd_design.verify_notification_popup_message("You have filters that are not bound to a control. Click the icon above to add them to the page.", "5.1")
        
        """
            STEP 6 : Save and Close the designer.
        """
        pd_design.save_as_page_from_application_menu("C5823630")
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STEP 7 : Run the page.
        """
        main_page.right_click_folder_item_and_select_menu("C5823630", "Run")
        time.sleep(10)
        main_run.switch_to_frame()
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        """
            STEP 7.1 : Verify no issues        
        """ 
        page_designer_run_obj = utils.validate_and_get_webdriver_object("div[class*='runner']", "Page Designer Run css")
        actual_result = page_designer_run_obj.is_displayed()
        msg = "Step 7.1 : Verify no issues "
        utils.asequal(True, actual_result, msg)
        
        pd_run.verify_containers_title(['Category Sales', 'Panel 2', 'Panel 3'], "Step 7.2 : Verify no issues")
        pd_run.switch_to_container_frame("Category Sales")
        chart.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 7.3 : Verify no issues")
        
        """
            STEP 8 : Close Run window.
        """
        pd_design.switch_to_default_page()
        main_run.close()
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 9 : Edit the page.
        """
        main_page.right_click_folder_item_and_select_menu("C5823630", "Edit")
        time.sleep(10)
        core_utils.switch_to_new_window()
        
        """
            STEP 10 : Click the quick filter icon
        """
        pd_design.click_quick_filter()
        pd_design.wait_for_visible_text("div[class*='pd-regular-filter-wrapper']", "Category:")
        
        """
            STEP 10.1 : Verify the filter grid appears
        """
        pd_design.verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], "Step 10.1 : Verify the filter grid appears")
        
        """
            STEP 11 : Save and Close the designer.
        """
        pd_design.click_toolbar_save()
        time.sleep(10)
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STEP 12 : Run the page.
        """
        main_page.right_click_folder_item_and_select_menu("C5823630", "Run")
        time.sleep(10)
        main_run.switch_to_frame()
        
        """
            STEP 12.1 : Verify no issues.
        """
        page_designer_run_obj = utils.validate_and_get_webdriver_object("div[class*='runner']", "Page Designer Run css")
        actual_result = page_designer_run_obj.is_displayed()
        msg = "Step 12.1 : Verify no issues "
        utils.asequal(True, actual_result, msg)
        
        pd_run.verify_containers_title(['Category Sales', 'Panel 2', 'Panel 3'], "Step 12.2 : Verify no issues")
        pd_run.verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], "Step 12.3 : Verify the filter grid appears")
        pd_run.switch_to_container_frame("Category Sales")
        chart.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg="Step 12.4 : Verify no issues")
        
        """
            STEP 13 : Close Run window.
        """
        pd_design.switch_to_default_page()
        main_run.close()
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """    
            STEP 14 : Edit the page.
        """
        main_page.right_click_folder_item_and_select_menu("C5823630", "Edit")
        time.sleep(15)
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class*='pd-regular-filter-wrapper']", "Category:")
        
        """
            STEP 14.1 : Verify the filter grid appears
        """
        pd_design.verify_filter_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], "Step 14.1 : Verify the filter grid appears")
        
        """
            STEP 15 : Close Designer.
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        
        """
            STEP 16 : Sign out WF.
        """
        main_page.signout_from_username_dropdown_menu()
 
if __name__ == '__main__':
    unittest.main()