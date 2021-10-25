"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh
Automated On : 18-February-2021
-------------------------------------------------------------------------------------------"""

import time
from common.lib.basetestcase import BaseTestCase
from common.locators.charts.common import Legend
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage

class C9928254_TestClass(BaseTestCase):
    
    def test_C9928254(self):
        
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
            STEP 04 : Click on section on the page canvas.;
            Select Format.
        """
        Designer.PageCanvas.Section.select(1, yoffset=-50)
        Designer.PropertiesPanel.select('Format')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_04_EXPECTED = """
            STEP 04 - Expected : Verify Style appears under Section Format.
        """
        Designer.PropertiesPanel.Format.SectionFormat.Style.verify_options(['Default', 'Style 2', 'Style 3', 'Style 4', 'Style 5', 'Style 6', 'Style 7', 'Style 8'], '04')
        Designer._utils.capture_screenshot("04 - Expected", STEP_04_EXPECTED, True)

        STEP_05 = """
            STEP 05 : Select Style 2
        """
        Designer.PropertiesPanel.Format.SectionFormat.Style.select('Style 2')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_06 = """
            STEP 06 : Navigate two level up in the Content tree;
            Navigate to Retail Samples > Portals > Small Widgets folder.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_name, 'Container 1')
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("06", STEP_06)
        STEP_07 = """
            STEP 07 : Drag and drop 'Category Sales' onto the Panel 1.
        """
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click Containers tab;
            Drag and drop the grid container onto the Panel 2.
        """
        Designer.SideBar.Container.click()
        Designer.ResourcesPanel.Containers.drag_to_container('Grid', 'Container 2')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Right click on the cell in Panel 2 and select Add filter controls.
        """
        Designer.SideBar.Filters.click()  
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Uncheck BUSINESS_REGION, STORE_TYPE, TIME_DATE and TIME_DATE_TO controls.
        """
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'Region:', 1)
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'Store Type:', 2)
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'From:', 3)
        Designer.ResourcesPanel.Filters.drag_to_container_grid('Container 2', 'To:', 4)
        Designer._utils.capture_screenshot("09", STEP_10)
        
        STEP_10_EXPECTED = """
            STEP 10 - Verify filter controls added into the grid container.
        """
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_control_labels(['Region:', 'Store Type:', 'From:', 'To:'], '10.01' )
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on Add filter controls button.
        """
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify filter controls added into the grid container and quick filters shows 4 inside the red circle.
        """
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:'], '11.01')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Select Outline tab, click on Filter bar under Visualizations 1 in Outline tree.
        """
        Designer.SideBar.Outline.click()
        Designer.ResourcesPanel.Outline.click_on_item('Visualization 1->Filter bar')
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Choose Style 3 in Grid Style.
        """
        Designer.PropertiesPanel.Format.GridStyle.Style.select('Style 3')
        time.sleep(5)
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify Style 3 is applied in the filter bar.
        """
        Designer.PageCanvas.FilterGrid.verify_grid_style_color('fern2', '14')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click on the Filter bar under Panel 1 in Outline tree;
            Select Style 4.
        """
        Designer.ResourcesPanel.Outline.click_on_item('Section 1->Container 2->Filter bar')
        Designer.PropertiesPanel.Format.GridStyle.Style.select('Style 4')
        time.sleep(5)
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify that Style 4 is applied in the grid container.
        """
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('Sea_Serpent', '15.01')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Click the preview button.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer._utils.wait_for_page_loads(90)
        Designer.RunMode.PageCanvas.wait_for_text('Page', time_out=120)
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("16", STEP_16)
        
        STEP_16_EXPECTED = """
            STEP 16 - Expected : Verify all the changes are retained in page preview.
        """
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=180)
        Designer.RunMode.PageCanvas.FilterGrid.verify_grid_style_color('fern2', '16.01')
        Designer.RunMode.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('Sea_Serpent', '16.02')
        Designer.RunMode.PageCanvas.Section.verify_style_color('curious_blue', '16.03')
        Designer._utils.capture_screenshot("16 - Expected", STEP_16_EXPECTED, True)

        STEP_17 = """
            STEP 17 : Close the preview.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Click on Save button and enter 'C9928251' in Title and click Save.
        """
        Designer.ToolBar.save('C9928251')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Close the designer.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer._utils.capture_screenshot("19", STEP_19)
        Designer.ContextMenu.select('Close')
        
        STEP_20 = """
            STEP 20 : Right click on 'C9928251' designer and select Run in new window.
        """
        Designer._core_utils.switch_to_previous_window(window_close=False)
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('C9928251')
        Designer.ContextMenu.select('Run')
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.wait_for_page_loads(120)
        
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_20_EXPECTED = """
            STEP 20 - Expected : Verify that applied grid styles and section style are retained in run time.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.wait_for_text('Page', time_out=120)
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=120)
        Designer.RunMode.PageCanvas.FilterGrid.verify_grid_style_color('fern2', '20.01')
        Designer.RunMode.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('Sea_Serpent', '20.02')
        Designer.RunMode.PageCanvas.Section.verify_style_color('curious_blue', '20.03')
        HomePage.RunWindow.switch_to_default_content()
        Designer._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)

        STEP_21 = """
            STEP 21 : Close the designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.RunWindow.switch_to_default_content()
        Designer._utils.capture_screenshot("21", STEP_21)

        STEP_22 = """
            STEP 22 : Restore 'C9928248' designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('C9928251')
        Designer.ContextMenu.select('Edit')
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify that applied grid styles and section style are retained.
        """
        Designer._core_utils.switch_to_new_window()
        Designer.PageCanvas.wait_for_text('Page', time_out=120)
        Designer.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=120)
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer.PageCanvas.FilterGrid.verify_grid_style_color('fern2', '22.01')
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('Sea_Serpent', '22.02')
        Designer.PageCanvas.Section.verify_style_color('curious_blue', '22.03')
        Designer._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : Close the designer.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        Designer._core_utils.switch_to_previous_window(window_close=False)
        Designer._utils.capture_screenshot("23", STEP_23)

        STEP_24 = """
            STEP 24 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        Designer._utils.capture_screenshot("24", STEP_24)

