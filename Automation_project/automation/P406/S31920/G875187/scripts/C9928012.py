"""-------------------------------------------------------------------------------------------
Author Name : Vishnu_Priya
Automated On : 13 February 2020
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928012_TestClass(BaseTestCase):
    
    def test_C9928012(self):
        
        """
        TESTCASE VARIABLES
        """
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        Step_01 = """
            Step 01 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login("mridbas", "mrpassbas")
        utils.capture_screenshot('01.00', Step_01)
        
        Step_02 = """
            Step 02 : Click on "Workspaces" tab > Click on "Workspaces" from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00', Step_02)
        
        Step_03 = """
            Step 03 : Click on "Workspaces" in the Resource Tree.
        """
        HomePage.Workspaces.ResourcesTree.select('Workspaces')
        utils.capture_screenshot('03.00', Step_03)
         
        Step_04 = """
            Step 04 : Expand "P406_S31920" workspace from the resource tree > Click on "G784912" folder > Double click on folder "Image/URL/Blog/TextEditor".
        """
        HomePage.Workspaces.ResourcesTree.expand('P406_S31920')
        HomePage.Workspaces.ResourcesTree.select('G784912')
        HomePage.Workspaces.ContentArea.double_click_on_folder('Images/URL/Blog/TextEditor')
        utils.capture_screenshot('04.00', Step_04)
              
        Step_05 = """
            Step 05 : Right click on uploaded image "Image_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Image_Context')
        utils.capture_screenshot('05.00', Step_05)
        
        Step_05_01 = """
            Step 05 : Verification - Verify context menu,
            View.
            View in new window.
            Properties.
        """
        expected_menus = ['View', 'View in new window','Properties']
        HomePage.ContextMenu.verify(expected_menus, '05.01')
        utils.capture_screenshot('05.01', Step_05_01, expected_image_verify= True)
        
        Step_06 = """
            Step 06 : Right click on "URL_Context" in the content area..
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('URL_Context')
        utils.capture_screenshot('06.00', Step_06)
        
        Step_06_01 = """
            Step 06 : Verification - Verify context menu,
            View.
            View in new window.
            Add to Favorites.
            Properties.
        """
        expected_menus = ['View', 'View in new window','Add to Favorites','Properties']
        HomePage.ContextMenu.verify(expected_menus, '06.01')
        utils.capture_screenshot('06.01', Step_06_01, expected_image_verify= True)
        
        Step_07 = """
            Step 07 : Right click on "Blog_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('Blog_Context')
        utils.capture_screenshot('07.00', Step_07)
        
        Step_07_01 = """
            Step 07 : Verification - Verify context menu,
            Comments (View comments).
            Properties.
        """
        expected_menus = ['Comments','Properties']
        HomePage.ContextMenu.verify(expected_menus, '07.01')
        HomePage.Workspaces.ContentArea.right_click_on_file('Blog_Context')
        expected_menus = ['View comments']
        HomePage.ContextMenu.verify(expected_menus, '07.02', menu_path='Comments')
        utils.capture_screenshot('07.01', Step_07_01, expected_image_verify= True)
        
        Step_08 = """
            Step 08 : Right click on "TextEditor_Context" in the content area.
        """
        HomePage.Workspaces.ContentArea.right_click_on_file('TextEditor_Context')
        utils.capture_screenshot('08.00', Step_08)
        
        Step_08_01 = """
            Step 08 : Verification - Verify context menu,
            Run.
            Run (Run in new window/Run deferred).
            Add to Favorites.
            Properties.
        """
        expected_menus = ['Run', 'Run...','Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, '08.01')  
        HomePage.Workspaces.ContentArea.right_click_on_file('TextEditor_Context')
        expected_menus = ['Run in new window', 'Run deferred']
        HomePage.ContextMenu.verify(expected_menus, '08.02', menu_path='Run...')  
        utils.capture_screenshot('08.01', Step_08_01,expected_image_verify= True)
        
        Step_09 = """
            Step 9 : In the banner link, click on the top right username > Click Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('09.00', Step_09)
        
    if __name__ == "__main__":
        unittest.main()