"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 17-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928043_TestClass(BaseTestCase):
    
    def test_C9928043(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        
        STEP_01 = """
            STEP 01 : Login WF as wfpendev1/owasp!@630
        """

        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree Expand the 'Workspaces' from the tree.
        """

        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on 'V5 Domain Testing' -> 'v5portal1' and choose Folder tile from action bar
        """

        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Enter title 'v5folder1' and click ok
        """

        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Right click on  'v5folder1' and select Publish
        """

        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on 'v5folder1' from tree and choose Folder tile from action bar
        """

        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Enter title 'v5subfolder1' and click ok
        """

        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Right click on 'v5subfolder1' and select Publish
        """

        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on 'V5 Domain Testing' -> v5portal1 -> v5folder1 -> v5subfolder1 from tree and Click '+' menu button on the top toolbar.
        """

        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click on 'Assemble Visualizations'.
        """

        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Choose blank template.
        """

        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on Format tab.
        """

        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click on Theme drop down
        """

        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify Theme drop down shows below options
    
            Designer 2018
            Light
            Midnight
            Custom Theme2
        """

        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click save and Click on V5 Domain Testing from bread crumb
        """

        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Double click on v5portal1 -> v5folder1 -> v5subfolder1 folder.
        """

        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Enter 'Page_Default' in Title text box and click on 'Save' button.
        """

        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Exit designer
        """

        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Right click on 'Page Default' and select Publish.
        """

        HomePage.Home._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Log out WF
        """

        HomePage.Home._utils.capture_screenshot("19", STEP_19)

