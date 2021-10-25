"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh
Automated On : 09-February-2021
-------------------------------------------------------------------------------------------"""
import time
from common.lib.basetestcase import BaseTestCase
from common.locators.charts.common import Legend
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage

class C9928248_TestClass(BaseTestCase):
    
    def test_C9928248(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        Designer = DesignerPage()
        
        """
        TEST CASE VAIABLES
        """
        content_name = 'G875212->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales'
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User.
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G875212' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G875212')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        Designer._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on Grid 2-1 template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Click on Format tab;
            Select Midnight in Theme dropdown.
        """
        Designer.PropertiesPanel.select('Format')
        Designer.PropertiesPanel.Format.PageFormat.click_theme_dropdown()
        Designer.PropertiesPanel.Format.PageFormat.ThemeDropdown.select('Midnight')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Midnight theme is applied in the designer.
        """
        time.sleep(7)
        Designer.PageCanvas.verify_theme('Midnight', '04')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)
        
        STEP_05 = """
            STEP 05 : Navigate two level up in the Content tree;
            Navigate to Retail Samples > Portals > Small Widgets folder.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_name, 'Container 1')
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("05", STEP_05)
        STEP_06 = """
            STEP 06 : Drag and drop 'Category Sales' onto the Panel 1.
        """
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click Containers tab;
            Drag and drop the grid container onto the Panel 2.
        """
        Designer.SideBar.Container.click()
        Designer.ResourcesPanel.Containers.drag_to_container('Grid', 'Container 2')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click on Filters side tab
        """
        Designer.SideBar.Filters.click()
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Drag and drop Region, Store Type, From and To controls to the cells in Grid container
        """
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'Region:', 1)
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'Store Type:', 2)
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'From:', 3)
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'To:', 4)
        Designer._utils.capture_screenshot("09", STEP_09)
        
        STEP_09 = """
            STEP 09 - Expected : Verify filter controls added into the grid container.
        """
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_control_labels(['Region:', 'Store Type:', 'From:', 'To:'], '09.01', )
        Designer._utils.capture_screenshot("09", STEP_09)
        
        STEP_10 = """
            STEP 10 : Click Add all filters to page
        """
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify filter controls added into the filter bar.
        """
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:'], '10.01')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)
    
        STEP_11 = """
            STEP 11 : Select Outline tab, click on Filter bar under Visualizations 1 in Outline tree.
        """
        Designer.SideBar.Outline.click()
        Designer.ResourcesPanel.Outline.click_on_item('Visualization 1->Filter bar')
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Click on Style 2 under Grid Style.
        """
        Designer.PropertiesPanel.Format.GridStyle.Style.select('Style 2')
        time.sleep(5)
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify that the Style 2 applied over the whole filter control.
        """
        Designer.PageCanvas.FilterGrid.verify_grid_style_color('dark_blue2', '12')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Click on the Filter bar under Panel 1 in Outline tree;
            Select Style 3.
        """
        Designer.ResourcesPanel.Outline.click_on_item('Section 1->Container 2->Filter bar')
        Designer.PropertiesPanel.Format.GridStyle.Style.select('Style 3')
        time.sleep(5)
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify that the whole filter bar grid area has now Style 2 and the grid container has Style 3 format and page has Midnight theme.
        """
        Designer.PageCanvas.FilterGrid.verify_grid_style_color('dark_blue2', '13.01')
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('ice_blue', '13.02')
        Designer.PageCanvas.verify_theme('Midnight', '13.03')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click the Run in new window icon in the toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text('Page', time_out=180)
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify that applied grid styles are retained in run window in both filter bar and grid container.
        """
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=120)
        Designer.RunMode.PageCanvas.FilterGrid.verify_grid_style_color('dark_blue2', '14.01')
        Designer.RunMode.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('ice_blue', '14.02')
        Designer.RunMode.PageCanvas.verify_theme('Midnight', '14.03')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Close the run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Click on Save button and enter 'C9928248' in Title and click Save.
        """
        Designer.ToolBar.save('C9928248')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Close the Designer.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer._utils.capture_screenshot("17", STEP_17)
        Designer.ContextMenu.select('Close')

        STEP_18 = """
            STEP 18 : Right click on 'C9928248' designer and select Run.
        """
        Designer._core_utils.switch_to_previous_window(window_close=False)
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('C9928248')
        Designer.ContextMenu.select('Run')
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.wait_for_page_loads(120)
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_18_EXPECTED = """
            STEP 18 - Expected : Verify that applied grid styles are retained in run time in both filter bar and grid container.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.wait_for_text('Page', time_out=180)
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=120)
        Designer.RunMode.PageCanvas.FilterGrid.verify_grid_style_color('dark_blue2', '18.01')
        Designer.RunMode.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('ice_blue', '18.02')
        Designer.RunMode.PageCanvas.verify_theme('Midnight', '18.03')
        HomePage.RunWindow.switch_to_default_content()
        Designer._utils.capture_screenshot("18 - Expected", STEP_18_EXPECTED, True)

        STEP_19 = """
            STEP 19 : Close the designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.RunWindow.switch_to_default_content()
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_20 = """
            STEP 20 : Restore 'C9928248' designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('C9928248')
        Designer.ContextMenu.select('Edit')
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_20_EXPECTED = """
            STEP 20 - Expected : Verify that applied grid styles are retained in both filter bar and grid container.
        """
        Designer._core_utils.switch_to_new_window()
        Designer.PageCanvas.wait_for_text('Page', time_out=180)
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=120)
        Designer.PageCanvas.FilterGrid.verify_grid_style_color('dark_blue2', '20.01')
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('ice_blue', '20.02')
        Designer.PageCanvas.verify_theme('Midnight', '20.03')
        Designer._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)

        STEP_21 = """
            STEP 21 : Close the designer.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        Designer._core_utils.switch_to_previous_window(window_close=False)
        Designer._utils.capture_screenshot("21", STEP_21)

        STEP_22 = """
            STEP 22 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        Designer._utils.capture_screenshot("22", STEP_22)

