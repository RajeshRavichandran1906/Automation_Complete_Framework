"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 13-07-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9946261_TestClass(BaseTestCase):
    
    def test_C9946261(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
       
        """
            TESTCASE VARIABLES
        """
        PORTAL_NAME="V5Portal_Context"
        
        STEP_01 = """
            STEP 01.00 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02.00 : Click on 'My Workspaces' view
        """
        HomePage.Banner.click_my_workspace()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Right-click on 'V5Portal_Context' and click 'Add to Favorites'
        """
        HomePage.MyWorkspace.right_click_on_item(PORTAL_NAME)
        HomePage.ContextMenu.select("Add to Favorites")
        HomePage.NotifyPopup.wait_for_visible()
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verify that Favorite added popup opens with a background transparent green layer over the popup.
        """
        HomePage.NotifyPopup.verify_text('Favorite added', '03.01')
#         HomePage.NotifyPopup.verify_background_color('03.02') pop up gets closing soon, color validated in the previous case.
        HomePage.NotifyPopup.verify_transparent('03.03')
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
        
        STEP_04 = """
            STEP 04.00 : Click on 'WebFOCUS Home' tab, Under 'FAVORITES' section carousel > Right-click on 'V5 Context Menu Testing2'
        """
        HomePage.Banner.click_home()
        HomePage.Home.Favorites.right_click_on_item(PORTAL_NAME)
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that 'V5 Context Menu Testing2' appears
        """
        expected_context_menu = ['Run', 'Edit', 'Remove from Favorites', 'Properties']
        HomePage.ContextMenu.verify(expected_context_menu, '04.01')
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05.00 : Right-click on 'V5 Context Menu Testing2' > Click Remove from Favorites
        """
        HomePage.ContextMenu.select('Remove from Favorites')
        HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify that 'Portal for Context Menu Testing2' favorite has been removed
        """
        HomePage.Home.Favorites.verify_items([PORTAL_NAME], '05.01', 'asnotin')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)