'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 01-AUGUEST-19
Test Case Title : Testing Preview
-----------------------------------------------------------------------------------------------------'''
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.page_designer import Design
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage

class C2319871_TestClass(BaseTestCase):
    
    def test_C2319871(self):
        
        """ CLASS OBJECTS """  
        pd_design = Design(self.driver)
        homepage = Wf_Mainpage(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        case_id = 'C2319870'
        page_name = case_id + """~!@#$%^&*()_+=-`{}|][":;'?><,./"""
        title_textbox_css = ".open-dialog-resources.pop-top .sd-form-field-text-title>input"
        
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
            STEP 06 : Click the application menu and click Close
            Verify that you get the save confirmation popup.
        """
        pd_design.select_option_from_application_menu("Close")
        
        """
            STEP 07 : STEP 07 : Click Yes.
        """
        pd_design.click_dialog_box_button("Yes")
        utils.synchronize_until_element_is_visible(title_textbox_css, 10)
        
        """
            STEP 08 : Enter "C2319871~!@#$%^&*()_+=-`{}|][":;'?><,./" in Title box and click Save.
            Verify Page is closed.
        """
        title_textbox = self.driver.find_element_by_css_selector(title_textbox_css)
        coreutils.left_click(title_textbox)
        title_textbox.clear()
        title_textbox.send_keys(page_name)
        pd_design.resource_dialog().click_button("Save")
        try : pd_design.click_dialog_box_button("OK") 
        except : pass
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STEP 09 : Edit "C2319871~!@#$%^&*()_+=-`{}|][":;'?><,./" page.
        """
        pd_design.edit_page_designer(page_name)
        
        """
            STEP 10 : Click on "G192932 > P292_S10660" domain to go two level up;
            Navigate to Retail samples --> Portal --> Test Widgets folder.
        """
        pd_design.collapse_content_folder("G192932->P292_S10660")
        pd_design.expand_content_folder("Retail Samples->Portal->Test Widgets")
        
        """
            STEP 11 : Drag Silver on to the page canvas.
        """
        source = 'div[role="treeitem"] [style*="Silver.html?"]'
        target = "[data-ibx-type='pdContent'][data-ibxp-file='Red.html']"
        source_elem = self.driver.find_element_by_css_selector(source)
        target_elem = self.driver.find_element_by_css_selector(target)
        utils.drag_drop_using_pyautogui(source_elem, target_elem)
        
        """
            STEP 12 : Click the application menu and click Close
            Verify that you get the save confirmation popup.
        """
        pd_design.select_option_from_application_menu("Close")
        
        """
            STEP 13 : Click Yes.
            Verify page closed and "C2319871~!@#$%^&*()_+=-`{}|][":;'?><,./" page is not published in Home Page.
        """ 
        pd_design.click_dialog_box_button("Yes")
        pd_design.switch_to_previous_window(driver_close=False)
        msg = "Step 13.01 : Verify page closed and C2319871~!@#$%^&*()_+=-`{}|][ page is not published in Home Page"
        homepage.verify_content_area_item_publish_or_unpublish(page_name, 'unpublish', msg)
        
        """
            STEP 14 : Sign out WF.
        """