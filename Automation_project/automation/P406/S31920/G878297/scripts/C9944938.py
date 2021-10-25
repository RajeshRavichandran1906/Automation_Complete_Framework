"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 1st April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944938_TestClass(BaseTestCase):
    
    def test_C9944938(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login('mriddev','mrpassdev')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
        Expand the 'Workspaces' > 'P406_S31920' Workspace
        Click on 'G878309' folder from the resource tree > Double click on 'URL Testing' folder from the content area
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces->P406_S31920")
        HomePage.Workspaces.ResourcesTree.select('G878309')
        HomePage.Workspaces.ContentArea.double_click_on_folder('URL Testing')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
        Right-click on 'C9944938' > Click on 'Edit
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('C9944938')
        HomePage.ContextMenu.select('Edit')
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_05 = """
        Change the title into "URL {}[]`!@#$%^&*()-=+_|;:'",<.>/?"
        """
        Edited_title = """URL {}[]`!@#$%^&*()-=+_|;:'",<.>/?"""
        HomePage.ModalDailogs.URL.Title.enter_text(Edited_title)
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
        Verify the following in the 'Edit URL' dialog box:
        Title entry box gets highlighted
        Inside the 'Title' entry box 'URL {}[]`!@#$%^&*()-=+_|;:'",<.>/?' is available
        Name entry box should be in read-only format
        Inside the 'Name' entry box 'URL_`!_-_' is available
        Summary entry box should be empty and URL should be 'http://www.google.com/'
        'Update' button is disabled (until user make a change) and the 'Cancel' button is enabled by default
        """
        HomePage.ModalDailogs.URL.Title.verify_border_color('malibu','05.01')
        HomePage.ModalDailogs.URL.Title.verify_text(Edited_title,'05.02')
        HomePage.ModalDailogs.URL.Name.verify_disabled('05.03')
        '''
        Script updated based on https://bipgjira.ibi.com/browse/HOME-3518
        '''
        HomePage.ModalDailogs.URL.Name.verify_text('URL_{}[]`!@_$_^_-_','05.04')
        HomePage.ModalDailogs.URL.Summary.verify_text('','05.05')
        HomePage.ModalDailogs.URL.URL.verify_text('http://www.google.com','05.06')
        HomePage.ModalDailogs.URL.UpdateButton.verify_enabled('05.07')
        HomePage.ModalDailogs.URL.CancelButton.verify_enabled('05.08')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01,expected_image_verify=True)
        
        STEP_06 ="""
        Click 'Update'
        """
        HomePage.ModalDailogs.URL.UpdateButton.click()
        HomePage.Home._utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """
        Verify that 'URL {}[]`!@#$%^&*()-=+_|;:'"...' URL appears in the content area
        """
        HomePage.Workspaces.ContentArea.verify_files([Edited_title],'06.01')
        HomePage.Home._utils.capture_screenshot('06.01',STEP_06_01,expected_image_verify=True)
        
        STEP_07 = """
        Right-click on 'URL {}[]`!@#$%^&*()-=+_|;:'"...' > Click on 'View in new window'
        """
        File_css = ".files-box .file-item div[title*= 'URL {}']"
        File_elem = HomePage.Home._utils.validate_and_get_webdriver_object(File_css,"File_css")
        HomePage.Home._core_utils.right_click(File_elem)
        HomePage.ContextMenu.select('View in new window')
        HomePage.Home._utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """
        Verify 'Google' opens in a new window without any issue
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_tab_name("Google","Step:07.01 verify the new window")
        HomePage.Home._utils.capture_screenshot('07.01',STEP_07_01,expected_image_verify=True)
        
        STEP_08 = """
        Close the 'Google' URL window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('08.00',STEP_08)
        
        STEP_09= """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)