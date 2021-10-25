'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 30-JULY-19
Test Case Title : Testing New Menu
-----------------------------------------------------------------------------------------------------'''
from common.lib.basetestcase import BaseTestCase
from common.wftools.page_designer import Design

class C2319869_TestClass(BaseTestCase):
    
    def test_C2319869(self):
        
        """ CLASS OBJECTS """  
        pd_design = Design(self.driver)
        
        """ COMMON VARIABLES """
        case_id = 'C2319869'
        page_name = case_id + "_1"
       
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
        pd_design.save_page_from_application_menu(case_id)
        
        """
            STEP 08 : Click the application menu and click New.
            Verify that the page template appears.
        """
        pd_design.select_option_from_application_menu("New")
        
        """
            STEP 09 : Choose Blank template.
        """
        pd_design.select_page_designer_template("Blank")
        
        """
            STEP 10 : Drag "Test Widget" onto the page canvas.
        """
        pd_design.drag_content_item_to_blank_canvas("Test Widget", 1)
        
        """
            STEP 11 : Click the application menu and click Save. Verify the Save window appears.
            STEP 12 : Enter "C2319869_1" in Title box and click Save.
        """
        pd_design.save_page_from_application_menu(page_name)
        
        """
            STEP 13 : Close Designer.
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STEP 14 : Signout WF
        """