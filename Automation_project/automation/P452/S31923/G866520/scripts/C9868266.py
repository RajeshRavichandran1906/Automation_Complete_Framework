"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 29-December-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPaege

class C9868266_TestClass(BaseTestCase):
    
    def test_C9868266(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPaege()

        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Create a new Assemble Visualizations under G866520 using blank template.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select("P452_S31923->G866520")
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool("Assemble Visualization")
        Designer._core_utils.switch_to_new_window()
        Designer.Dialog.ChooseTemplate.Common.select("Blank")
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click Containers tab;
            Drag and drop Link Tile Widget on to the page canvas.
        """
        Designer.SideBar.Container.click()
        Designer.ResourcesPanel.Containers.drag_to_page_section('Link tile')
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify that Link Tile properties 
            Background & Content having Textbox and ellipsis buttons.
        """
        background_css = "div.pd-ps-background-path-edit + div.pd-ps-background-path-btn div.fa-ellipsis-h"
        content_css = "div.pd-ps-content-path-edit + div.pd-ps-content-path-btn div.fa-ellipsis-h"
        label_css = "div.df-accordion-page-content-link-tile div.df-ps-name"
        background_visible = self.driver.find_element_by_css_selector(background_css).is_displayed()
        content_visible = self.driver.find_element_by_css_selector(content_css).is_displayed()
        Designer._utils.asequal(True, background_visible, 'Step 03.01 : Verify  Background text box having ellipsis button')
        Designer._utils.asequal(True, content_visible, 'Step 03.02 : Verify  Content text box having ellipsis button')
        labels = [label.text.strip() for label in self.driver.find_elements_by_css_selector(label_css)]
        Designer._utils.list_values_verification(['Background', 'Content', 'Target'], labels, '03.03', 'Link Tile properties', 'equal')
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Click on Application menu > Click Close > Click No to close the visualizations.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select("Close")
        Designer.Dialog.Alert.wait_until_visible()
        Designer.Dialog.Alert.No.click()
        Designer._core_utils.switch_to_previous_window(False)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)