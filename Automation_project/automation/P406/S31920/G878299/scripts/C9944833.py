"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 7th April 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944833_TestClass(BaseTestCase):
    
    def test_C9944833(self):
        
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
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
        Expand the 'Workspaces' > 'P406_S31920' Workspace > Click on 'G878309' folder from the resource tree > 
        Click on 'Shortcut Testing'
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces->P406_S31920->G878309->Shortcut Testing")
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
        
        STEP_06 = """
        Click on P406_S31920 in breadcrumb > Double click on G784912 > Double click on 'Portal/Pages' folder
        """
        HomePage.ModalDailogs.Resources.NavigationBar.BreadCrumb.select('P406_S31920')
        HomePage.ModalDailogs.Resources.GridView.Folders.double_click('G784912->Portal/Pages')
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
        Verify that List of folders (V4_Portal_Context_Resources and V5Portal_Context) and items(Page_Context and V4_Portal_Context) are showing in the 
        select dialog that belongs to the domain/folder the short cut launched from
        """
        HomePage.ModalDailogs.Resources.GridView.Folders.verify(['V4_Portal_Context Resources', 'V5Portal_Context'],'06.01')
        HomePage.ModalDailogs.Resources.GridView.Files.verify(['Page_Context', 'V4_Portal_Context'],'06.02')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01,expected_image_verify=True)
        
        STEP_07 = """
        Click the 'Cancel' button to close the 'Select' dialog
        """
        HomePage.ModalDailogs.Resources.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
    
        STEP_08 = """
        Click the 'Cancel' button to close the 'Shortcut' dialog
        """
        HomePage.ModalDailogs.Shortcut.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
    
        STEP_09 = """
            STEP 09 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)