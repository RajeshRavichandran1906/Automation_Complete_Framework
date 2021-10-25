"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 08-September-2021
-------------------------------------------------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.pages.charts import Pie, TreeMap, Line
from common.wftools.paris_home_page import ParisHomePage
from common.locators.designer import page_canvas as Locator
from common.wftools.designer import Designer as DesignerPage

class C9950462_TestClass(BaseTestCase):
    
    def test_C9950462(self):
        
        """
        TEST CASE OBJECTS
        """
        PieChart = Pie()
        LineChart = Line()
        TreeMapChart = TreeMap() 
        Designer = DesignerPage()
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        content_path = "G875160->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales"
        
        STEP_01 = """
            STEP 01 : Login WF as developer user.
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G875160' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G875160')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify Grid 2-1 Side template is visible in the Choose Template dialog.
        """
        Designer._core_utils.switch_to_new_window()
        Designer.Dialog.ChooseTemplate.Common.verify(['Blank', 'Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1', 'InfoApp 1', 'Workbench'], '02')
        Designer._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Choose 'Grid 2-1 Side' template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1 Side')  
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify page canvas for 'Grid 2-1 Side' template appears as below.
        """
        Designer.PageCanvas.Containers.verify_containers_title(['Container 1', 'Container 2', 'Container 3'], '03')
        Designer._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Navigate to 'Retail Samples' domain > Portal >Small Widgets folder.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_path, 'Container 1')
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Drag and drop 'Category Sales', 'Regional Sales Trend' and 'Discount by Region' to Panel 1, Panel 2 and Panel 3 respectively.
        """
        Designer.ResourcesPanel.Content.drag_to_container('Regional Sales Trend', 'Container 3')
        Designer.ResourcesPanel.Content.drag_to_container('Discount by Region', 'Container 2')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify the page Canvas.
        """
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '05.01')
        PieChart.verify_number_of_risers(7, '05.02')
        PieChart.verify_total_lables(['1.1B'], '05.03')
        PieChart.verify_riser_color([(1, 'bar_blue')], '05.04')
        PieChart.verify_pie_labels(['Revenue'], '05.05')
        Designer._core_utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Basic('Discount by Region').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '05.06')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '05.07')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '05.08')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '05.09')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '05.10')
        Designer._core_utils.switch_to_default_content()
        Designer.PageCanvas.Containers.Basic('Regional Sales Trend').switch_to_frame()
        LineChart.wait_for_text('Revenue', 120)
        LineChart.verify_xaxis_title(['Month'], '05.11')
        LineChart.verify_yaxis_title(['Revenue'], '05.12')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '05.13')
        LineChart.verify_number_of_risers(4, '05.14')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '05.15', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click the 'Run in new window' icon in Toolbar.
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_window()
        Designer._core_utils.update_window_handles_list(update='add')
        Designer._driver.maximize_window()
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify page appears as below.
        """
        Designer._utils.wait_for_page_loads(120)
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '06.01')
        PieChart.verify_legend_title(['Product Category'], '06.02')
        PieChart.verify_number_of_risers(7, '06.03')
        PieChart.verify_total_lables(['1.1B'], '06.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '06.05')
        PieChart.verify_pie_labels(['Revenue'], '06.06')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Basic('Discount by Region').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '06.07')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '06.08')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '06.09')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '06.10')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '06.11')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Basic('Regional Sales Trend').switch_to_frame()
        LineChart.wait_for_text('Revenue', 120)
        LineChart.verify_xaxis_title(['Month'], '06.12')
        LineChart.verify_yaxis_title(['Revenue'], '06.13')
        LineChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '06.14')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '06.15')
        LineChart.verify_number_of_risers(4, '06.16')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '06.17', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Close the run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Click in the section area and select 'Style 2' format.
        """
        Designer.PageCanvas.Section.select(1, element_location='top_left')
        Designer.PropertiesPanel.select('Format')
        Designer.PropertiesPanel.Format.SectionFormat.Style.select('Style 2')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify styling applied on the page as below.
        """
        Designer.PageCanvas.Section.verify_style_color('curious_blue', '08')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Select Filters side tab;
            Click on Add all filters to page button.
        """
        Designer.SideBar.Filters.click()  
        Designer.ResourcesPanel.Filters.click_add_all_filters_to_page_button()
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the cell padding (empty space) should appear below filter bar.
        """
        Designer.PageCanvas.FilterGrid.wait_for_text('Category:', 60)
        filter_obj = Designer.PageCanvas.FilterGrid._parent_object
        fil_location = filter_obj.location
        fil_size = filter_obj.size
        filter_bottom = fil_location['y'] + fil_size['height']
        sec_obj = Designer.PageCanvas.Section._get_section_object(1)
        sec_loc = sec_obj.location
        sec_top = sec_loc['y']
        cell_padding = sec_top - filter_bottom
        value = True if int(cell_padding) in range(5,15) else False
        msg = 'Step 09: Verify the cell padding (empty space) should appear below filter bar, padding expected 10 and actual {0}'.format(cell_padding)
        Designer._utils.asequal(True, value, msg)
        Designer._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Add another section
        """
        Designer.PageCanvas.Section.right_click(1, element_location='top_left', xoffset=2)
        Designer.ContextMenu.select('Insert section below')
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Add all container types there
        """
        Designer._javascript.scrollIntoView(Designer.PageCanvas.Section._get_section_grid_object(2))
        Designer.SideBar.Container.click()
        Designer.ResourcesPanel.Containers.drag_to_page_section('Basic', 2)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Tab', 2, section_location='top_middle', x=85, y=15)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Carousel', 2, section_location='bottom_left', y=-15)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Accordion', 2, section_location='middle', x=85, y=50)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Grid', 2, section_location='bottom_left', y=-15)
        Designer._javascript.scrollIntoView(Designer.PageCanvas.Containers.Grid('Container 5')._get_container_object())
        Designer.ResourcesPanel.Containers.drag_to_page_section('Panel group', 2, section_location='bottom_middle', x=85, y=-150)
        Designer.ResourcesPanel.Containers.drag_to_page_section('Link tile', 2, section_location='bottom_left', y=-15)
        Designer._javascript.scrollIntoView(Designer.PageCanvas.Containers.LinkTile()._get_container_object())
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify that the titles are all Container #
        """
        Designer.PageCanvas.Containers.verify_containers_title(['Category Sales', 'Discount by Region', 'Regional Sales Trend', 'Container 1', 'Container 2', 'Container 3', 'Container 4', 'Container 5'], '11')
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Click 'Save' in toolbar Enter 'C9944738' and Click 'Save' button.
        """
        Designer.ToolBar.save('C9950462')
        Designer._utils.wait_for_page_loads(100)
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click the Application menu and Select 'Close'.
        """
        Designer.ToolBar.ApplicationMenu.click()
        Designer.ContextMenu.select('Close')
        Designer._core_utils.switch_to_previous_window(window_close=False)
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_14 = """
            STEP 14 : Right click on 'C8262176' and Select 'Run'
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file('C9950462')
        HomePage.ContextMenu.select('Run')
        HomePage.RunWindow.switch_to_frame()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify styling and cell padding applied on the page appears as below.
        """ 
        Designer._utils.wait_for_page_loads(120)
        Designer._webelement.wait_for_element_text(Locator.PAGE, 'Page', 180)
        Designer.RunMode.PageCanvas.FilterGrid.wait_for_text('Category:', 120)
        filter_obj = Designer.RunMode.PageCanvas.FilterGrid._parent_object
        fil_location = filter_obj.location
        fil_size = filter_obj.size
        filter_bottom = fil_location['y'] + fil_size['height']
        sec_obj = Designer.RunMode.PageCanvas.Section._get_section_object(1)
        sec_loc = sec_obj.location
        sec_top = sec_loc['y']
        cell_padding = sec_top - filter_bottom
        value = True if int(cell_padding) in range(5,15) else False
        msg = 'Step 14: Verify the cell padding (empty space) should appear below filter bar, padding expected 10 and actual {0}'.format(int(cell_padding))
        Designer._utils.asequal(True, value, msg)
        Designer.RunMode.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '14.01')
        PieChart.verify_legend_title(['Product Category'], '14.02')
        PieChart.verify_number_of_risers(7, '14.03')
        PieChart.verify_total_lables(['1.1B'], '14.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '14.05')
        PieChart.verify_pie_labels(['Revenue'], '14.06')
        Designer._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Basic('Discount by Region').switch_to_frame()
        TreeMapChart.wait_for_text('EMEA', 120)
        TreeMapChart.verify_number_of_risers(16, '14.07')
        TreeMapChart.verify_xaxis_labels(['1', '2', '3', '4'], '14.08')
        TreeMapChart.verify_yaxis_labels(['EMEA', 'North America', 'Oceania', 'South America'], '14.09')
        TreeMapChart.verify_xaxis_title(['Sale Quarter', 'Store Region'], '14.10')
        TreeMapChart.verify_riser_color([(1, 'light_blue3'), (9, 'Cobalt')], '14.11')
        Designer._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Basic('Regional Sales Trend').switch_to_frame()
        LineChart.wait_for_text('Revenue', 120)
        LineChart.verify_xaxis_title(['Month'], '14.12')
        LineChart.verify_yaxis_title(['Revenue'], '14.13')
        LineChart.verify_xaxis_labels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], '14.14')
        LineChart.verify_yaxis_labels(['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], '14.15')
        LineChart.verify_number_of_risers(4, '14.16')
        LineChart.verify_riser_color([(1, 'bar_blue'), (2, 'pale_green')], '14.17', attribute='stroke')
        Designer._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Section.verify_style_color('curious_blue', '14.18')
        Designer.RunMode.PageCanvas.Containers.verify_containers_title(['Category Sales', 'Discount by Region', 'Regional Sales Trend', 'Container 1', 'Container 2', 'Container 3', 'Container 4', 'Container 5'], '14.19')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Close the Run window.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_16 = """
            STEP 16 : Logout WF.
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("16", STEP_16)