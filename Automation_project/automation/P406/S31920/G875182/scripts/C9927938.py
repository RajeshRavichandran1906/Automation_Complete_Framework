"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 23 December 2019
-------------------------------------------------------------------------------------------"""

from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927938_TestClass(BaseTestCase):
    
    def test_C9927938(self):
        
        """
            TESTCASE OBJECTS
        """
        Utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
    
        STEP_01 = """
            Step 01.00 : Sign into WebFOCUS Home Page as Advanced User
        """
        HomePage.invoke_with_login("mridadv", "mrpassadv")
        Utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            Step 02.00 : From WebFOCUS Home tab, Under 'PORTALS' section carousel >Click 'VIEW ALL' button
        """
        HomePage.Home.Portals.click_view_all()
        Utils.capture_screenshot("02.00", STEP_02)
            
        STEP_03 = """
            Step 03.00 : Right-click on 'V5 Context Menu Testing'
        """
        HomePage.Home.ViewAll.right_click_on_item("V5 Context Menu Testing")
        Utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            Step 03.01 : Verify that the following context menus are displayed[Run, Add to Favorites, Properties]
        """
        expected_menus = ['Run', 'Add to Favorites', 'Properties']
        HomePage.ContextMenu.verify(expected_menus, "03.01")
        Utils.capture_screenshot("03.01", STEP_03_01, expected_image_verify = True)
        
        STEP_04 = """
            Step 04.00 : Click on 'Left arrow' to go back to 'Home tab'
        """
        HomePage.Home.ViewAll.click_left_arrow()
        Utils.capture_screenshot("04.00", STEP_04)
        
        STEP_05 = """
            Step 05.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        Utils.capture_screenshot("05.00", STEP_05)