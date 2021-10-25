"""-------------------------------------------------------------------------------------------
Author Name  : Rajesh
Automated On : 12-February-2021
-------------------------------------------------------------------------------------------"""
import time
from common.lib.basetestcase import BaseTestCase
from common.locators.charts.common import Legend
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage

class C9928251_TestClass(BaseTestCase):
    
    def test_C9928251(self):
        
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
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
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
            Click on Panel 1, select  Style 2 in Properties panel;
            Click on Panel 2, select Style 3 in Properties panel;
            Click on Panel 3, select Style 4 in Properties panel.
        """
        Designer.PropertiesPanel.select('Format')
        Designer.PageCanvas.Containers.Basic('Container 1').select()
        Designer.PropertiesPanel.Format.ContainerFormat.Style.select('Style 2')
        Designer.PageCanvas.Containers.Basic('Container 2').select()
        Designer.PropertiesPanel.Format.ContainerFormat.Style.select('Style 3')
        Designer.PageCanvas.Containers.Basic('Container 3').select()
        Designer.PropertiesPanel.Format.ContainerFormat.Style.select('Style 4')
        Designer._utils.capture_screenshot("04", STEP_04)
        
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
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Right click on the cell in Panel 2 and select Add filter controls.
        """
        Designer.SideBar.Filters.click()    
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Uncheck BUSINESS_REGION, STORE_TYPE, TIME_DATE and TIME_DATE_TO.
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
            STEP 10 : Click on Add filter controls button.
        """
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify filter controls added into the grid container and quick filters shows 4 inside the red circle.
        """
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:'], '10.01')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Select Outline tab, click on Filter bar under Visualizations 1 in Outline tree.
        """
        Designer.SideBar.Outline.click()
        Designer.ResourcesPanel.Outline.click_on_item('Visualization 1->Filter bar')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Choose Style 3 in Grid Style.
        """
        Designer.PropertiesPanel.Format.GridStyle.Style.select('Style 3')
        time.sleep(5)
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify Style 3 is applied in the filter bar.
        """
        Designer.PageCanvas.FilterGrid.verify_grid_style_color('fern2', '13')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on the Filter bar under Panel 1 in Outline tree;
            Select Style 4.
        """
        Designer.ResourcesPanel.Outline.click_on_item('Section 1->Container 2->Filter bar')
        Designer.PropertiesPanel.Format.GridStyle.Style.select('Style 4')
        time.sleep(5)
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify that Style 4 is applied in the grid container.
        """
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('Sea_Serpent', '14.01')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Click the preview button.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text("Page", time_out=120)
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("15", STEP_15)
        
        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify that applied grid styles are retained in preview in both filter bar and grid container.
        """
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=180)
        Designer.RunMode.PageCanvas.FilterGrid.verify_grid_style_color('fern2', '15.01')
        Designer.RunMode.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('Sea_Serpent', '15.02')
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').verify_style_color('curious_blue', '15.03')
        Designer.RunMode.PageCanvas.Containers.Basic('Container 2').verify_style_color('fern2', '15.04')
        Designer.RunMode.PageCanvas.Containers.Basic('Container 3').verify_style_color('Sea_Serpent', '15.05')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)
        
        STEP_16 = """
            STEP 16 : Close the preview.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("16", STEP_16)
        
        STEP_17 = """
            STEP 17 : Click on Save button and enter 'C9928251' in Title and click Save.
        """
        Designer.ToolBar.save('C9928251')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Close the Designer.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer._utils.capture_screenshot("18", STEP_18)
        Designer.ContextMenu.select('Close')
        
        STEP_19 = """
            STEP 19 : Right click on 'C9928251' designer and select Run in new window.
        """
        Designer._core_utils.switch_to_previous_window(window_close=False)
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('C9928251')
        Designer.ContextMenu.select('Run')
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify that applied grid styles are retained in run time in both filter bar and grid container.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.wait_for_text("Page", time_out=120)
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=180)
        Designer.RunMode.PageCanvas.FilterGrid.verify_grid_style_color('fern2', '19.01')
        Designer.RunMode.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('Sea_Serpent', '19.02')
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').verify_style_color('curious_blue', '19.03')
        Designer.RunMode.PageCanvas.Containers.Basic('Container 2').verify_style_color('fern2', '19.04')
        Designer.RunMode.PageCanvas.Containers.Basic('Container 3').verify_style_color('Sea_Serpent', '19.05')
        HomePage.RunWindow.switch_to_default_content()
        Designer._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Close the designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.RunWindow.switch_to_default_content()
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Restore 'C9928248' designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('C9928251')
        Designer.ContextMenu.select('Edit')
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify that applied grid styles are retained in both filter bar and grid container.
        """ 
        Designer._core_utils.switch_to_new_window()
        Designer.PageCanvas.wait_for_text("Page", time_out=120)
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer.PageCanvas.FilterGrid.wait_for_text('Category:', time_out=180)
        Designer.PageCanvas.FilterGrid.verify_grid_style_color('fern2', '21.01')
        Designer.PageCanvas.Containers.Grid('Container 2').FilterGrid.verify_grid_style_color('Sea_Serpent', '21.02')
        Designer.PageCanvas.Containers.Basic('Category Sales').verify_style_color('curious_blue', '21.03')
        Designer.PageCanvas.Containers.Basic('Container 2').verify_style_color('fern2', '21.04')
        Designer.PageCanvas.Containers.Basic('Container 3').verify_style_color('Sea_Serpent', '21.05')
        Designer._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Close the designer.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        Designer._core_utils.switch_to_previous_window(window_close=False)
        Designer._utils.capture_screenshot("22", STEP_22)

        STEP_23 = """
            STEP 23 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        Designer._utils.capture_screenshot("23", STEP_23)

