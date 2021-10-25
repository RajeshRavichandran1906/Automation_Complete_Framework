"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 2nd March 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944829_TestClass(BaseTestCase):
    
    def test_C9944829(self):
        
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
 
        Step_04_01 = """Verify the following:
        New Shortcut as title
        Type - Repository file radio button (By default selected) and Master file radio button (not selected)
        Target path should be read-only with a Browse button
        Title text box should be empty
        Summary text box should be empty
        Cancel button gets enabled and OK button gets disabled by default
        """
        HomePage.ModalDailogs.Shortcut.verify_title("New Shortcut",'04.01')
        HomePage.ModalDailogs.Shortcut.Type.RepositoryFile.verify_checked('04.02')
        HomePage.ModalDailogs.Shortcut.Type.MasterFile.verify_unchecked('04.03')
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_disabled('04.04')
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.verify_text("Browse",'04.05')
        HomePage.ModalDailogs.Shortcut.Title.verify_text("",'04.06')
        HomePage.ModalDailogs.Shortcut.Summary.verify_text("",'04.07')
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled("04.08")
        HomePage.ModalDailogs.Shortcut.OKButton.verify_disabled("04.09")
        HomePage.Home._utils.capture_screenshot('04.01', Step_04_01,expected_image_verify=True)

        Step_05 = """Click on 'Master file'
        """
        HomePage.ModalDailogs.Shortcut.Type.MasterFile.click()
        HomePage.Home._utils.capture_screenshot('05.00', Step_05)

        Step_05_01="""
        Verify the following:
        New Shortcut as title
        Type - Repository file radio button (not selected) and Master file radio button (gets selected)
        Target path should be read-only with a Browse button
        Title text box should be empty
        Summary text box should be empty
        Cancel button gets enabled and OK button gets disabled by default
        """
        HomePage.ModalDailogs.Shortcut.verify_title("New Shortcut",'05.01')
        HomePage.ModalDailogs.Shortcut.Type.RepositoryFile.verify_unchecked('05.02')
        HomePage.ModalDailogs.Shortcut.Type.MasterFile.verify_checked('05.03')
        HomePage.ModalDailogs.Shortcut.TargetPath.verify_disabled('05.04')
        HomePage.ModalDailogs.Shortcut.TargetPath.BrowseButton.verify_text("Browse",'05.05')
        HomePage.ModalDailogs.Shortcut.Title.verify_text("",'05.06')
        HomePage.ModalDailogs.Shortcut.Summary.verify_text("",'05.07')
        HomePage.ModalDailogs.Shortcut.CancelButton.verify_enabled("05.08")
        HomePage.ModalDailogs.Shortcut.OKButton.verify_disabled("05.09")
        HomePage.Home._utils.capture_screenshot('05.01', Step_05_01,expected_image_verify=True)
        
        Step_06 = """Click Cancel to close the Shortcut dialog
        """
        HomePage.ModalDailogs.Shortcut.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('06.00', Step_06)
        
        STEP_07 = """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)