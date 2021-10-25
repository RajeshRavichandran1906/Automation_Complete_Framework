"""-------------------------------------------------------------------------------------------
Author Name  : AH14645
Automated On : 16-December-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage
from common.locators.designer.components import properties_panel as Locators

class C9947765_TestClass(BaseTestCase):
    
    def test_C9947765(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPage()
        """
        TEST CASE VAIABLES
        """

        content_name = 'Category Sales'
        panel1 = 'Container 1'
        iframe_content_id_css = 'div.pd-cont-iframe iframe.ibx-iframe-frame'
        
        STEP_01 = """
            STEP 01 : Login WF as domain developer
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G866552' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G866552')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Choose Grid 2-1 template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag and drop Category Sales report onto the page canvas from Retail Samples > Portal > Small Widget folder.
        """
        Designer.ResourcesPanel.Content.select('G866552->P452_S31923->Retail Samples->Portal->Small Widgets')
        Designer.ResourcesPanel.Content.wait_for_text(content_name, 10)
        Designer.ResourcesPanel.Content.drag_to_container(content_name, panel1)
        Designer._utils.wait_for_page_loads(10)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Open browsers Developer tools (WebConsole) by pressing Ctrl+Shift+i.
            Select Elements tab.
        """
        HomePage.Home._utils.capture_screenshot("05", STEP_05)
        STEP_06 = """
            STEP 06 : Click on Inspect icon and select Category Sales content.
        """
        HomePage.Home._utils.capture_screenshot("06", STEP_06)
        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify iframe name and Content id are same.
        """
        content_id1 = Designer._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.content_id, "Content id").get_attribute("value").strip()
        iframe_name = Designer._utils.validate_and_get_webdriver_object(iframe_content_id_css, "iFrame name").get_attribute("name").strip()
        Designer._utils.asequal(content_id1, iframe_name, "STEP 06: Verify iframe name and Content id are same.")
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Click Application menu;
            Select New.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select("New")
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Select Grid 2-1 template.
        """
        Designer._core_utils.switch_to_new_window()
        Designer.Dialog.ChooseTemplate.wait_for_text('Grid 2-1')
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Drag and drop Category Sales report onto the page canvas from Retail Samples > Portal > Small Widget folder.
        """
        Designer.ResourcesPanel.Content.select('G866552->P452_S31923->Retail Samples->Portal->Small Widgets')
        Designer.ResourcesPanel.Content.wait_for_text(content_name, 10)
        Designer.ResourcesPanel.Content.drag_to_container(content_name, panel1)
        Designer._utils.wait_for_page_loads(10)
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify ID in Content Settings is not same for page 1 and 2.
        """
        content_id2 = Designer._utils.validate_and_get_webdriver_object_using_locator(Locators.Settings.content_id, "Content id").get_attribute("value").strip()
        Designer._utils.as_not_equal(content_id1, content_id2, "STEP 09: Verify ID in Content Settings is not same for page 1 and 2.")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Open browsers Developer tools (WebConsole) by pressing Ctrl+Shift+i.
            Select Elements tab.
        """
        HomePage.Home._utils.capture_screenshot("10", STEP_10)
        STEP_11 = """
            STEP 11 : Click on Inspect icon and select Category Sales content.
        """
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify iframe name and Content id are same.
        """
        iframe_name = Designer._utils.validate_and_get_webdriver_object(iframe_content_id_css, "iFrame name").get_attribute("name").strip()
        Designer._utils.asequal(content_id2, iframe_name, "STEP 11: Verify iframe name and Content id are same")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the designer without saving..
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Sign out WF.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)