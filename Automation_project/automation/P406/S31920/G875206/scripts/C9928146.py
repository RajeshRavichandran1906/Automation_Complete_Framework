"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 9th January 2020
-----------------------------------------------------------------------------------------------"""

import unittest

from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

from common.pages.vfour_miscelaneous  import Vfour_Miscelaneous
from common.pages.vfour_portal_canvas import Vfour_Portal_Canvas
from common.pages.vfour_portal_properties import Vfour_Portal_Properties
from common.pages.vfour_portal_ribbon import Vfour_Portal_Ribbon

from common.wftools.paris_home_page import ParisHomePage


class C9928146_TestClass(BaseTestCase):
    
    def test_C9928146(self):
        
        """
        TESTCASE OBJECTS
        """
        vfour_misc = Vfour_Miscelaneous(self.driver)
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        vfour_portal_properties = Vfour_Portal_Properties(self.driver)
        vfour_portal_ribbon = Vfour_Portal_Ribbon(self.driver)
        vfour_portal_canvas = Vfour_Portal_Canvas(self.driver)

        """
        TESTCASE VARIABLES
        """
        add_page_capion_css="#dlgTitleExplorer .active.window .window-caption .bi-label"
        navigator_css="div[id*='BipNavigatorButton']"
        panel_content_css = "[id*='BidFolderBlockTree']"
        #workspace = "Workspaces"
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login("mrid", "mrpass")
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
        HomePage.Workspaces.ContentArea.delete_file_if_exists('C9928146')
        HomePage.Workspaces.ContentArea.delete_folder_if_exists('C9928146 Resources')
        utils.capture_screenshot('03.00',Step_03)
        
        Step_04 = """
            Step 04 : Click on 'Other' category button
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        utils.capture_screenshot('04.00',Step_04)
        
        
        Step_05 = """
        Click on 'Portal Page' action bar under 'Other' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Portal Page")
        utils.capture_screenshot('05.00',Step_05)
        
        Step_05_01 = """
            Step 05.01 : Verify Add Page dialog box is displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(add_page_capion_css, 'Add Page',90)
        utils.verify_object_visible(add_page_capion_css, True, "Step 5.01: Verify caption of Add page")
        utils.capture_screenshot('05.01',Step_05_01,expected_image_verify=True)
        
        Step_06 = """
            Step 06 : Select '1 Column' > Create
            Enter the title 'C9928146' and Click 'Create'
            Verify 'C9928165' is displayed
        """
        vfour_misc.select_page_template(page_template='1 Column', Page_title='C9928146', Page_name='C9928146', btn_name="Create")
        utils.synchronize_with_number_of_element(navigator_css,2,45)
        utils.capture_screenshot('06.00',Step_06)
        
        Step_07_01="""verification - Verify 'C9928146' is displayed
        """ 
        vfour_portal_properties.verify_input_control('page','Title', 'textbox','Step 7.01: Verify Title value is shown', textbox_value='C9928146')
        utils.capture_screenshot('06.00',Step_07_01,expected_image_verify=True)
        
        Step_08 ="""
        Press 'F8' and drag and drop 'Retail Samples' to page
        """
        vfour_portal_ribbon.invoke_and_verify_wf_resource_tree(launch_point='keybord')
        vfour_portal_canvas.dragdrop_repository_item_to_canvas('Retail Samples','column',1)
        utils.synchronize_with_visble_text(panel_content_css, 'Retail Samples',90)
        utils.capture_screenshot('08.00',Step_08)
        
        Step_08_01 = """Verification"""
        
        utils.verify_element_text('.bip-panel-pane table>tbody>tr','Retail Samples',"Step 08.01 verify the panel updated with Retail samples")
        utils.capture_screenshot('08.01',Step_08_01)
        
        Step_09 = """
            STEP 09 Click on BIP > Exit > Yes >Ok
        """
        vfour_portal_ribbon.bip_save_and_exit('Yes')
        core_utils.switch_to_previous_window(window_close=False)
        utils.capture_screenshot('09.00',Step_09)
        
        Step_09_01  = """
        STEP 07.01 verification - Verify the created 'C9928146' is displayed in the content area    
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files(["C9928146"],'09.01')
        utils.capture_screenshot('09.01',Step_09_01,expected_image_verify=True)
        
        Step_10 = """
        Right Click on 'C9928146' > Delete > Ok
        """
        HomePage.Workspaces.ContentArea.delete_file('C9928146')
        utils.capture_screenshot('10.00',Step_10)
        
        Step_10_01 = """
        Verify the created 'C9928146' is not displayed in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files(["C9928146"],'10.01',assert_type='asnotin')
        utils.capture_screenshot('10.01',Step_10_01,expected_image_verify=True)
        
    
        Step_11 = """
            Step 09 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('11.00',Step_11)
 
if __name__ == "__main__":
    unittest.main()