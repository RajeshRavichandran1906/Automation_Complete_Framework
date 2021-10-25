'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 31-JULY-19
Test Case Title : Testing Preview
-----------------------------------------------------------------------------------------------------'''
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design, Preview
import time

class C2319870_TestClass(BaseTestCase):
    
    def test_C2319870(self):
        
        """ CLASS OBJECTS """  
        pd_design = Design(self.driver)
        pd_preview = Preview(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        case_id = 'C2319870'
        page_name = case_id + """~!@#$%^&*()_+=-`{}|][":;'?><,./"""
        expected_container_titles = ['Blue', 'Gray', 'Green', 'Red']
        resource_pane_css = ".pd-left-pane"
        properties_pane_css = ".pd-right-pane"
        
        """
            STEP 01 : Login WF as domain developer. Click on Content view from side bar.
            STEP 02 : Expand 'P292_S10660' domain. Click on 'G192933' folder and choose Page action tile from designer category.
            STEP 03 : Create a page with Blank template.
        """
        pd_design.invoke_page_designer_and_select_template("Blank",  from_designer_group=True)
        
        """
            STEP 04 : Click on "G192932 > P292_S10660" domain to go two level up;
            Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        pd_design.collapse_content_folder("G192932->P292_S10660")
        pd_design.expand_content_folder("Retail Samples->Portal->Test Widgets")
        
        """
            STEP 05 : Drag Blue, Gray, Green and Red onto the page canvas respectively.
        """
        pd_design.drag_content_item_to_blank_canvas("Blue", 1)
        pd_design.drag_content_item_to_blank_canvas("Gray", 4)
        pd_design.drag_content_item_to_blank_canvas("Green", 7)
        pd_design.drag_content_item_to_blank_canvas("Red", 10)
        
        """
            STEP 06 : Click the application menu and click Save.
            Enter "C2319868" in Title box and click Save button.
        """
        pd_design.save_page_from_application_menu(case_id)
        time.sleep(10)
        
        """
            STEP 07 : Open Properties and click the Preview button
            Verify that Resource selector and Properties panel are not visible in preview, only added content is visible.
        """
        pd_design.click_property()
        pd_design.click_preview()
        pd_preview.verify_preview_is_displayed("Step 07.01 : Verify that Resource selector and Properties panel are not visible in preview, only added content is visible")
        pd_preview.verify_containers_title(expected_container_titles, "Step 07.02 : Verify containers title")
        
        """
            STEP 08 :Click the blue arrow present in top of the page in live preview
            Verify that the Resource selector and Properties panel are now visible in the page.
        """
        pd_preview.go_back_to_design_from_preview()
        resource_pane = self.driver.find_element_by_css_selector(resource_pane_css)
        properties_pane = self.driver.find_element_by_css_selector(properties_pane_css)
        screen_width = coreutils.get_current_screen_specification()['screen_width']
        properties_pane_status = (int(properties_pane.location['x']) + int(properties_pane.size['width'])) == screen_width
        utils.asequal(int(resource_pane.location['x']), 0, "Step 08.01 : Verify Resource panel now visible in the page")
        utils.asequal(properties_pane_status, True, "Step 08.02 : Verify Properties panel now visible in the page")
        
        """
            STEP 09 : Click the application menu and click Save as...
            Enter "C2319870~!@#$%^&*()_+=-`{}|][":;'?><,./" in Title box and click Save as button.
        """
        pd_design.save_as_page_from_application_menu(page_name)
        
        """
            STEP 10 : Close page designer
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STEP 11 : Edit "C2319870~!@#$%^&*()_+=-`{}|][":;'?><,./" page. 
        """
        pd_design.edit_page_designer(page_name)
        
        """
            STEP 12 : Open Properties.
        """
        pd_design.click_property()
        
        """
            STEP 13 : Click the preview button.
            Verify that Resource selector and Properties panel are not visible in preview, only added content is visible. 
        """
        pd_design.click_preview()
        pd_preview.verify_preview_is_displayed("Step 13.01 : Verify that Resource selector and Properties panel are not visible in preview, only added content is visible")
        pd_preview.verify_containers_title(expected_container_titles, "Step 13.02 : Verify containers title")
        
        """
            STEP 14 : Click the blue arrow present in top of the page in live preview.
            Verify that the Resource selector and Properties panel are now visible in the page.
        """
        pd_preview.go_back_to_design_from_preview()
        resource_pane = self.driver.find_element_by_css_selector(resource_pane_css)
        properties_pane = self.driver.find_element_by_css_selector(properties_pane_css)
        screen_width = coreutils.get_current_screen_specification()['screen_width']
        properties_pane_status = (int(properties_pane.location['x']) + int(properties_pane.size['width'])) == screen_width
        utils.asequal(int(resource_pane.location['x']), 0, "Step 14.01 : Verify Resource panel now visible in the page")
        utils.asequal(properties_pane_status, True, "Step 14.02 : Verify Properties panel now visible in the page")
        
        """
            STEP 15 : Close Page Designer and sign out WF.
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)