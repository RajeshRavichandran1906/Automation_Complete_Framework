"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 30 January 2020
-----------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.wftools.designer_portal import Two_Level_Side
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.wf_mainpage import Wf_Mainpage
from common.locators.portal_designer import Vfive_Designer


class C9928092_TestClass(BaseTestCase):
    
    def test_C9928092(self):
        
        """"
        TESTCASE OBJECTS
        """
        utils     =  UtillityMethods(self.driver)
        HomePage  =  ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        two_level_portal = Two_Level_Side(self.driver)
        old_homepage = Wf_Mainpage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        PROJECT_ID    =  utils.parseinitfile('project_id')
        SUITE_ID      =  utils.parseinitfile('suite_id')
        GROUP_ID    =  utils.parseinitfile('group_id')
        FOLDER_PATH =  PROJECT_ID + "_" + SUITE_ID+'->'+GROUP_ID
        PAGE_FOLDER = 'My Pages'
        NEW_PAGE_TEMPLATE_WINDOW_CSS  = ".pop-top .ibx-dialog-main-box .np-open"
        LINK_WINDOW_CSS = ".sd-files-box-files .folder-div .image-text .ibx-label-text"
        EXPECTED_PAGE_TEMPLATES = ['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1']
        
        STEP_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mrdevid", "mrdevpass")
        utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02 :  Click on 'Workspaces' tab > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            Step 03 : Navigate to 'P406_S31920' workspace > Double click on 'G875201' folder.
        """
        HomePage.Workspaces.ResourcesTree.select(FOLDER_PATH)
        utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            Step 04 : Right click on 'V5_Sharing' from the content area > Select Run
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder('V5_Sharing')
        HomePage.ContextMenu.select('Run')
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(Vfive_Designer.page_header_css, 'Page', 120)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05 : Click the + sign in the sidebar
        """
        two_level_portal.click_on_plus_icon_under_the_folder_in_left_sidebar(PAGE_FOLDER)
        utils.synchronize_with_visble_text(NEW_PAGE_TEMPLATE_WINDOW_CSS, 'Link to an existing page',90)
        utils.capture_screenshot("05.00",STEP_05)
        
        STEP_05_01 = """
            Step 05.01 Verify 'New Page' dialog appears with 'Link to an existing page' and 'four templates'
        """
        two_level_portal.verify_new_page_templates(EXPECTED_PAGE_TEMPLATES, 'Step 05.01 : Verify you see 4-page templates (Grid 2-1, Grid 2-1 side, Grid 3-3-3, and Grid 4-2-1)')
        utils.capture_screenshot("05.01",STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
            Step 06 Select 'Link to an existing page'
        """
        
        two_level_portal.click_on_link_to_an_existing_page_button()
        utils.synchronize_with_visble_text(LINK_WINDOW_CSS, 'V5_Sharing',90)
        utils.capture_screenshot("06.00",STEP_06)
        
        STEP_06_01 = """
        Verify 'Select' window opens
        """
        old_homepage.resource_dialog().verify_caption_title("Select",'06.01')
        utils.capture_screenshot("06.01",STEP_06_01,expected_image_verify=True)
        
        STEP_07 ="""
        Click 'Workspaces' > Double click Retail Samples domain > InfoApps folder > Select 'Sales Dashboard (Filtered)' page > Click on 'Select' button
        """
        old_homepage.resource_dialog().click_crumb_item("Workspaces")
        old_homepage.resource_dialog().navigate_to_folder_and_select_file("Retail Samples->InfoApps", "Sales Dashboard (Filtered)")
        old_homepage.resource_dialog().click_button("Select")
        utils.capture_screenshot("07.00",STEP_07)
        
        
        STEP_07_01 = """
        Verify 'Sales Dashboard (Filtered)' appear in the sidebar and 'Retail Sales Dashboard' appear as a title in the canvas.
        Also, verify that it does not display share icon in the personal page toolbar
        """
        utils.wait_for_page_loads(time_out=45, pause_time=20)
        two_level_portal.verify_page_header_all_buttons(["Refresh","Show filters","Delete"],'Step 07.01 : verify share button is not appear')
        two_level_portal.verify_page_header_title("Retail Sales Dashboard","Step 07.02 : verify the page heading")
        two_level_portal.verify_pages_under_the_folder_in_left_sidebar('My Pages',['Page 1', 'Sales Dashboard (Filtered)', '+'], "Step 07.03 : verify 'Sales Dashboard (Filtered)' appear in the sidebar ")
        utils.capture_screenshot("07.01",STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
           STEP 08.00 : Close the portal run window
        """
        core_utils.switch_to_previous_window()
        utils.capture_screenshot("08.00", STEP_08)
        
        STEP_09 = """
            STEP 09.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot("09.00", STEP_09)