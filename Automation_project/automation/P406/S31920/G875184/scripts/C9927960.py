"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_priya
Automated On : 17 December 2019
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927960_TestClass(BaseTestCase):
    
    def test_C9927960(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Admin User.
        """
        HomePage.invoke_with_login("mradmid", "mradmpass")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step_02) 
         
        Step_03 = """Right click on "P406_S31920" workspace from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.right_click('P406_S31920')
        utils.capture_screenshot('03.00', Step_03) 
        
        Step_03_01 = """ Verify the following Context Menu:
        Expand/Collapse.
        Paste Ctrl+V (Grayed out).
        Delete DEL.
        Refresh.
        General access (All Users/Workspace groups[Default Selection]).
        Publish/Unpublish.
        Show/Hide.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(['Expand', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'General access', 'Unpublish', 'Hide', 'Security', 'Properties'],'03.01')
        utils.capture_screenshot('03.01',Step_03_01,expected_image_verify=True) 

        Step_04 = """Click "Expand" option.
        """
        HomePage.ContextMenu.select("Expand")
        utils.capture_screenshot('04.00', Step_04)
        
        Step_05 = """From the Resource Tree > Right click on "My Content" folder under "P406_S31920" workspace.
        """
        HomePage.Workspaces.ResourcesTree.right_click('P406_S31920->My Content')
        utils.capture_screenshot('05.00', Step_05)

        Step_05_01 = """
        Verify the following Context Menu:
        Expand/Collapse.
        Paste Ctrl+V (Grayed out).
        Delete DEL.
        Refresh.
        Security (Rules on this resource.../Effective Policy.../Owner).
        Share/Unshare.
        Share with...
        Properties.
        """
        HomePage.ContextMenu.verify(['Expand', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Security', 'Share', 'Share with...', 'Properties'],'05.01')
        utils.capture_screenshot('05.01', Step_05_01,expected_image_verify=True)
        
        Step_06 = """From the Resource Tree > Right click on "Hidden Content" folder under "P406_S31920" workspace.
        """
        HomePage.ContextMenu.close()
        HomePage.Workspaces.ResourcesTree.right_click('P406_S31920->Hidden Content')
        utils.capture_screenshot('06.01', Step_06)
        
        Step_06_01 = """
        Verify the following Context Menu:
        Expand/Collapse.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Paste Ctrl+V (Grayed out).
        Delete DEL.
        Refresh.
        Unpublish/Publish.
        Show/Hide.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(['Expand', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Show', 'Security', 'Properties'],"06.01")
        utils.capture_screenshot('06.01',Step_06_01,expected_image_verify=True)
        
        Step_07 = """From the Resource Tree > Right click on "G784912"folder under "P406_S31920" workspace.
        """
        HomePage.ContextMenu.close()
        HomePage.Workspaces.ResourcesTree.right_click("P406_S31920->G784912")
        utils.capture_screenshot('07.00', Step_07)

        Step_07_01 = """
        Verify the following Context Menu:
        Expand/Collapse.
        Duplicate.
        Cut Ctrl+X.
        Copy Ctrl+C.
        Paste Ctrl+V (Grayed out).
        Delete DEL.
        Refresh.
        Unpublish/Publish.
        Show/Hide.
        Security (Rules.../Rules on this resource.../Effective Policy.../Owner...).
        Properties.
        """
        HomePage.ContextMenu.verify(['Expand', 'Duplicate', 'Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL', 'Refresh', 'Unpublish', 'Hide', 'Security', 'Properties'],"07.01")
        utils.capture_screenshot('07.01', Step_07_01,expected_image_verify=True)
        
        Step_08 = """
            Step 8 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('08.00', Step_08)
        
    if __name__ == "__main__":
        unittest.main()