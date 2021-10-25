'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 25-JULY-19
Test Case Title : Edit Menu
-----------------------------------------------------------------------------------------------------'''

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer, wf_mainpage 
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods
from common.locators.page_designer_locators import PageDesigner as PD_LOCATORS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class C2319888_TestClass(BaseTestCase):
    
    def test_C2319888(self):
        
        """ CLASS OBJECTS """  
        pd_design = page_designer.Design(self.driver)
        pd_run = page_designer.Run(self.driver)
        homepage = wf_mainpage.Wf_Mainpage(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        case_id = 'C2319888'
    
        """
            STEP 01 : Login WF as domain developer. Click on Content view from side bar.
            STEP 02 : Expand 'P292_S10660' domain. Click on 'G192933' folder and choose Page action tile from designer category.
            STEP 03 : Create a page with Blank template.
        """
        pd_design.invoke_page_designer_and_select_template("Blank")
        
        """
            STEP 04 : Click Save in toolbar, enter "C2319888" in Title and click Save
        """
        pd_design.save_page_from_toolbar(case_id)
        
        """
            STEP 05 : Close the page.
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STPE 06 : Right click on "C2319888" page.
            Verify that there is no Edit with text editor option available
        """
        homepage.verify_repository_folder_item_context_menu(case_id, ['Edit with text editor'], msg='Step 06.01', comparision_type='asnotin')
        
        """
            STEP 07 : Choose Edit
            Verify page loaded successfully
        """
        pd_design.edit_page_designer(case_id)
        msg = "Step 07.01 : Verify blank template opened with 'Page Heading' title"
        pd_design.verify_page_heading_title(['Page Heading'], msg)
        
        """
            STEP 08 : Replace the page header with "Header testing"
        """
        if Global_variables.browser_name in ["Chrome", "chrome", "cr"] :
            title_obj=self.driver.find_element(*PD_LOCATORS.PAHE_HEADER_TITLE).find_element_by_css_selector(".ibx-label-text")
            ActionChains(self.driver).double_click(title_obj).send_keys("Header testing").send_keys(Keys.ENTER).perform()
        elif Global_variables.browser_name in ["Firefox", "firefox", "ff"] : 
            title_obj=self.driver.find_element(*PD_LOCATORS.PAHE_HEADER_TITLE).find_element_by_css_selector(".ibx-label-text")
            coreutils.double_click(title_obj)
            title_obj.send_keys("Header testing")
            title_obj.send_keys(Keys.ENTER)
        
        """
            STEP 09 : Close the page designer and Save the page
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.click_dialog_box_button("Yes")
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STEP 10 : Run the page
            Verify that the header has changed
        """
        pd_design.run_page_designer(case_id)
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text(".pd-page-header", "Header testing", 80)
        msg = "Step 10.01 : Verify page designer page run with 'Header testing' heading"
        pd_run.verify_page_heading_title(['Header testing'], msg)
        pd_run.switch_to_default_page()
        
        """
            STEP 11 : Close the Run window
        """
        pd_run.close_homepage_run_window()
        
        """
            STEP 12 : Sign out WF.
        """