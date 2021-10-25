'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 29-JULY-19
Test Case Title : Testing Open
-----------------------------------------------------------------------------------------------------'''
from common.pages.page_designer_design import PageDesignerDesign
from common.lib.basetestcase import BaseTestCase
from common.wftools.page_designer import Design
from common.lib.utillity import UtillityMethods

class C2319868_TestClass(BaseTestCase):
    
    def test_C2319868(self):
        
        """ CLASS OBJECTS """  
        pd_design = Design(self.driver)
        pd_designer = PageDesignerDesign(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        case_id = 'C2319868'
        dialog_msg_css = ".pop-top .pd-warning-dirty-label .ibx-label-text"
    
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
            STEP 07 : Enter "C2319868" in Title box and click Save button.
        """
        pd_design.save_as_page_from_application_menu(case_id)
        
        """
            STEP 08 : Add Yellow under the Blue panel.
            Verify Yellow added in second row.
        """
        pd_design.drag_content_item_to_blank_canvas("Yellow", 49)
        blue_container_x = int(pd_designer.get_container_object("Blue").location['x'])
        yello_container_x = int(pd_designer.get_container_object("Yellow").location['x'])
        utils.asequal(blue_container_x, yello_container_x,"Step 08.01 : Verify Yellow added in second row")
        
        """
            STEP 09 : Click application menu and click Open.
            Verify that you get a pop up asking "Do you want to save changes to current page?".
        """
        pd_design.select_option_from_application_menu("Open...")
        pd_design.wait_for_visible_text(dialog_msg_css, "Do you want", 20)
        actual_msg = self.driver.find_element_by_css_selector(dialog_msg_css).text.strip()
        expected_msg = "Do you want to save changes to current page?"
        utils.asequal(expected_msg, actual_msg, "Step 09.01 : Verify that you get a pop up asking 'Do you want to save changes to current page?'")
        
        """
            STEP 10 : Click Yes.
            Verify that Open browse window appears.
        """
        pd_design.click_dialog_box_button("Yes")
        pd_design.wait_for_visible_text(".pop-top", "Open", 20)
        pd_design.resource_dialog().verify_caption_title("Open", "10.01")
        
        """
            STEP 11 : Enter "pageDesigner" in Title and click Open.
            Verify File not found error message appears.
        """
        pd_design.resource_dialog().enter_title("pageDesigner")
        pd_design.resource_dialog().click_button("Open")
        actual_msg = self.driver.find_element_by_css_selector(".pop-top .ibx-dialog-content").text.strip()
        expected_msg = "File not found: pagedesigner"
        utils.asequal(expected_msg, actual_msg, "Step 11.01 : Verify File not found error message appears")
        
        """
            STEP 12 : Click OK to close the dialog.
        """
        pd_design.click_dialog_box_button("OK")
        
        """
            STEP 13 : Select "C2319868" in Open dialog and click Open.
            Verify the page open with no issues.
        """
        pd_design.resource_dialog().select_file(case_id)
        pd_design.resource_dialog().click_button("Open")
        pd_design.wait_for_visible_text(".pd-page-canvas", "Blue", 20)
        expected_title = ['Blue', 'Gray', 'Green', 'Red', 'Yellow']
        pd_design.verify_containers_title(expected_title, "Step 13.01 : Verify the page open with no issues")
        
        """
            STEP 14 : Close Designer and sign out WF.
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)