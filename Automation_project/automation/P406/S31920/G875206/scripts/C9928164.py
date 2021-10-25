"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 9th January 2020
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.pages.vfour_miscelaneous  import Vfour_Miscelaneous
from common.pages.vfour_portal_ribbon import Vfour_Portal_Ribbon
from common.wftools.paris_home_page import ParisHomePage


class C9928164_TestClass(BaseTestCase):
    
    def test_C9928164(self):
        
        """
        TESTCASE OBJECTS
        """
        vfour_misc = Vfour_Miscelaneous(self.driver)
        vfour_portal_ribbon = Vfour_Portal_Ribbon(self.driver)
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)

        """
        TESTCASE VARIABLES
        """
        add_page_capion_css="#dlgTitleExplorer .active.window .window-caption .bi-label"
        navigator_css="div[id*='BipNavigatorButton']"
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as dev User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot('01.00',Step_01)
        
        Step_02 = """
            Step 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot('02.00',Step_02)
        
        Step_03 = """
            Step 03 : Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Workspaces.ContentArea.delete_file_if_exists('C9928164')
        HomePage.Workspaces.ContentArea.delete_folder_if_exists('C9928164 Resources')
        utils.capture_screenshot('03.00',Step_03)
        
        Step_04 = """
            Step 04 : Click on 'Other' category button > 'Collaborative Portal' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Collaborative Portal")
        utils.capture_screenshot('04.00',Step_04)
        
        Step_04_01  = """
            Step 04.01 : Verification - Verify 'New Portal' dialog box opens
            Title box should be empty
            Name box should empty
            The path should be IBFS:/WFC/Repository/Retail_Samples
            URL should be /ibi_apps/portal/Retail_Samples
        """
        HomePage.ModalDailogs.CollaborativePortal.verify_title('New Portal','04.01')
        HomePage.ModalDailogs.CollaborativePortal.Title.verify_text('','04.02')
        HomePage.ModalDailogs.CollaborativePortal.Name.verify_text('','04.03')
        HomePage.ModalDailogs.CollaborativePortal.Path.verify_text('IBFS:/WFC/Repository/Retail_Samples','04.04')
        HomePage.ModalDailogs.CollaborativePortal.URL.verify_text('/ibi_apps/portal/Retail_Samples','04.05')
        utils.capture_screenshot('04.01',Step_04_01,expected_image_verify=True)
        
        Step_05 = """
            Step 05 : Enter title 'C9928164' > Create
        """
        HomePage.ModalDailogs.CollaborativePortal.Title.enter_text('C9928164')
        HomePage.ModalDailogs.CollaborativePortal.CreateButton.click()
        utils.capture_screenshot('05.00',Step_05)
        
        Step_05_01 = """
            Step 05.01 : Verify Add Page dialog box is displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(add_page_capion_css, 'Add Page',90)
        utils.verify_object_visible(add_page_capion_css, True, "Step 5: Verify caption of Add page")
        utils.capture_screenshot('05.01',Step_05_01)
        
        Step_06 = """
            Step 06 : Select '1 Column' > Create
        """
        vfour_misc.select_page_template(page_template='1 Column', Page_title='C9928145', Page_name='C9928145', btn_name="Create")
        utils.synchronize_with_number_of_element(navigator_css,2,45)
        utils.capture_screenshot('06.00',Step_06,expected_image_verify=True)
        
        Step_07 = """
            STEP 07 Click on BIP > Exit > Yes >Ok
        """
        vfour_portal_ribbon.bip_save_and_exit('Yes')
        core_utils.switch_to_previous_window(window_close=False)
        utils.capture_screenshot('07.00',Step_07)
        
        Step_07_01  = """
        STEP 07.01 verification - Verify the created 'C9928164' is displayed in the content area    
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files(["C9928164"],'07.01')
        utils.capture_screenshot('07.01',Step_07_01,expected_image_verify=True)
        
        Step_08 = """
        Right Click on 'C9928164' > Delete > Ok
        """
        HomePage.Workspaces.ContentArea.delete_file('C9928164')
        utils.capture_screenshot('08.00',Step_08)
        
        Step_08_01 = """
        Verify the created 'C9928164' is not displayed in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files(["C9928164"],'08.01',assert_type='asnotin')
        utils.capture_screenshot('08.01',Step_08_01,expected_image_verify=True)
        
    
        Step_09 = """
            Step 09 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('09.00',Step_09)
 
if __name__ == "__main__":
    unittest.main()