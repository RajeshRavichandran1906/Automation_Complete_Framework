"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 2nd April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944830_TestClass(BaseTestCase):
    
    def test_C9944830(self):
        
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
        Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G878309' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces->P406_S31920->G878309")
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04="""Click on 'Other' category button > Click on 'Shortcut' action tile
        """
        HomePage.Workspaces.ContentArea.delete_file_if_exists('Testing URL Action Tile')
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Shortcut")
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
 
        STEP_05 = """
        Click on the 'Browse' button
        """
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
        Verify 'Title' and 'Name' boxes should be non-editable
        """
        HomePage.ModalDailogs.Resources.Title.verify_disabled('05.01')
        HomePage.ModalDailogs.Resources.Name.verify_disabled('05.02')
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01,expected_image_verify=True)
        
        STEP_06 ="""
        Click Cancel
        """
        HomePage.ModalDailogs.Resources.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_07 = """
        Click on 'Master file' radio button > Click on the 'Browse' button
        """
        HomePage.ModalDailogs.Shortcut.Type.MasterFile.click()
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.click()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07,expected_image_verify=True)
        
        STEP_07_01 = """
        Verify 'Title' and 'Name' boxes should be non-editable
        """
        HomePage.ModalDailogs.Resources.Title.verify_disabled('07.01')
        HomePage.ModalDailogs.Resources.Name.verify_disabled('07.02')
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07_01)
        
        Step_08 = """Click Cancel to close the Shortcut dialog
        """
        HomePage.ModalDailogs.Resources.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', Step_08)
        
        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)