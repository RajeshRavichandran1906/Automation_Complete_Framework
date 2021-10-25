"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 13-September-2021
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage

class C9952244_TestClass(BaseTestCase):
    
    def test_C9952244(self):
        
        """
            TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        HomePage = ParisHomePage(self.driver)
        
        
        STEP_01 = """
            STEP 01 : Login WebFOCUS as developer user.
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on Workspaces.
        """
        HomePage.Banner.click_workspaces(True)
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Expand 'P452_S31923' domain and Click on 'G784935' folder.
        """
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G784935')
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on '+' button and Select 'Assemble Visualizations'.
        """
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Choose the Blank template.
        """
        Designer._core_utils.switch_to_new_window()
        Designer.Dialog.ChooseTemplate.Common.select('Blank')  
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Click on the application menu hamburger in the designer toolbar.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Close menu is available.
        """
        Designer.ContextMenu.verify_options(['Close'], '06', assert_type='in')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click on Close.
        """
        Designer.ContextMenu.select('Close')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Assemble Visualizations closed without any error.
        """
        Designer._core_utils.switch_to_previous_window(window_close=False)
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on Visualize data from HOME.
        """
        HomePage.Banner.click_visualize_data()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Select ibisamp/car.mas.
        """
        Designer.Dialog.SelectDataSource.wait_for_text('ibisamp', 120)
        Designer.Dialog.SelectDataSource.ListView.select_masterfile('ibisamp->car.mas')
        Designer.Dialog.SelectDataSource.SelectButton.click()
        Designer.Dialog.SelectDataSource.wait_until_invisible(time_out=10, pause_time=5)
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click on the application menu hamburger in the designer toolbar.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify Close menu is available.
        """
        Designer.ContextMenu.verify_options(['Close'], '10', assert_type='in')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on Convert to page icon in the toolbar.
        """
        Designer.VisualizationToolBar.ConvertToPage.click()
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on the application menu hamburger in the designer toolbar.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify Close menu is available.
        """
        Designer.ContextMenu.verify_options(['Close'], '12', assert_type='in')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on Close.
            Click on No in Save popup dialog.
        """
        Designer.ContextMenu.select('Close')
        Designer.Dialog.Alert.No.click()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify Visualizations closed without any error.
        """
        Designer._core_utils.switch_to_previous_window(window_close=False)
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.click_user()
        HomePage.Banner.sign_out()
        Designer._utils.capture_screenshot("14", STEP_14)