"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 04-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9928125_TestClass(BaseTestCase):
    
    def test_C9928125(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Homepage as developer user
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces view
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P406_S31920' workspace > Click on 'G875203' folder
        """
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875202")
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on 'Application' category button > Click on 'Portal' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab("APPLICATION")
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.ModalDailogs.V5Portal.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify the new portal dialog appears with maximum width set to 100% by default and is greyed out as below
        """
        HomePage.ModalDailogs.V5Portal.verify_title("New Portal", "04.01")
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "04.02")
        HomePage.Home._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Click inside 'Maximum width' text box
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.click()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that inside 'Maximum width' text box is editable
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_editable("05.01")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click anywhere outside of the text box
        """
        HomePage.ModalDailogs.V5Portal.Title.click()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify that it reverts back to 100% and nothing has changed in appearance
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "06.01")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Choose 'Three level' navigation
        """
        HomePage.ModalDailogs.V5Portal.Navigation.select("Three-level")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the Maximum width is still 100%
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "07.01")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click inside 'Maximum width' text box
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.click()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify that inside 'Maximum width' text box is editable
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_editable("08.01")
        HomePage.Home._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Click anywhere outside of the text box
        """
        HomePage.ModalDailogs.V5Portal.Title.click()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that inside 'Maximum width' text box reverts back to 100% and nothing has changed in appearance
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "09.01")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Choose 'Two level Top 'navigation
        """
        HomePage.ModalDailogs.V5Portal.Navigation.select("Two-level top")
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify the Maximum width is still 100%
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "10.01")
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click inside 'Maximum width' text box
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.click()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that inside 'Maximum width' text box it is editable
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_editable("11.01")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click anywhere outside of the box
        """
        HomePage.ModalDailogs.V5Portal.Title.click()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify that it reverts back to 100% and nothing has changed in appearance
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_placeholder("100%", "12.01")
        HomePage.Home._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click inside 'Maximum width' text box
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.click()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Enter 75 then click anywhere outside the box
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.enter_text("75", False)
        HomePage.ModalDailogs.V5Portal.Title.click()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify the maximum width value automatically picks up px (75px) and the % disappeared.
        """
        HomePage.ModalDailogs.V5Portal.MaximumWidth.verify_text("75px", "14.01")
        HomePage.Home._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click Cancel
        """
        HomePage.ModalDailogs.V5Portal.CancelButton.click()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Signout WF
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("16", STEP_16)