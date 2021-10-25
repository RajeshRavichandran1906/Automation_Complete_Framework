"""-------------------------------------------------------------------------------------------
Author Name  : RR25087
Automated On : 14-September-2021
-------------------------------------------------------------------------------------------"""
from common.pages.charts import Bar, Pie, HtmlContent, Area, Map
from common.wftools.reports import Reports
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer import Designer as DesignerPage

class C9947192_TestClass(BaseTestCase):
    
    def test_C9947192(self):
        
        """
        TEST CASE OBJECTS
        """
        MapChart = Map()
        PieChart = Pie()
        BarChart = Bar()
        AreaChart = Area()
        HtmlContentChart = HtmlContent()
        Designer = DesignerPage()
        HtmlReport = Reports().HTML5()
        HomePage = ParisHomePage(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        file_name = 'C9947192'
        data_set = file_name  +"_DataSet01"
        data_set2 = file_name  +"_DataSet02"
        content_name = 'drill_with_multiple_procedures'
        content_name2 = 'drill_from_multi_parameters'
        content_path = 'G866552->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales'
        content_path2 = 'Small Widgets->Test Widgets->Blue'
        
        STEP_01 = """
            STEP 01 : Login WF as domain developer
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Select Workspaces and navigate to 'P452_S31923/G866552' folder;
            Click on '+' button in top bar and select Assemble Visualizations.
        """
        HomePage.Banner.click_workspaces(True)
        HomePage.Workspaces.ResourcesTree.select('P452_S31923->G866552')
        HomePage.Workspaces.ContentArea.delete_file_if_exists('C9947191')
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Banner.ToolListMenu.select_tool('Assemble Visualizations')
        HomePage.Home._core_utils.switch_to_new_window()
        Designer._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Choose Grid 2-1 template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Grid 2-1')
        Designer._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Drag and drop 'drill_with_multiple_procedures' onto the Panel 1.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_name, 'Container 1')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Drag and drop 'drill_from_multi_parameters' onto the Panel 1.
            Select Add content as new accordion area.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_name2, content_name)
        Designer.Dialog.AddContent.wait_until_visible(30)
        Designer.Dialog.AddContent.click_dropdown()
        Designer.ContextMenu.select('Add content as new accordion area')
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify accordion area created without error.
        """
        Designer.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').verify_areas_title(['drill_with_multiple_procedures', 'drill_from_multi_parameters'], '05')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click on Containers in side tab;
            Drag and drop Tab container onto the Panel 2.
        """
        Designer.SideBar.Container.click()
        Designer.ResourcesPanel.Containers.drag_to_container('Tab', 'Container 2')
        Designer._utils.wait_for_page_loads(30)
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Enter 'TestDrill1' in the Classes textbox under Content properties.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.Classes.enter_text('TestDrill1')
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_08 = """
            STEP 08 : Select Content;
            Drag and drop Category Sales onto the tab container form Retail Samples > Portal > Small Widgets folder.
        """
        Designer.SideBar.Content.click()
        Designer.ResourcesPanel.Content.drag_to_container(content_path, 'Container 2')
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Drag and drop Blue onto the tab container form Retail Samples > Portal > Test Widgets folder.
            Select Add content.
        """
        Designer.ResourcesPanel.Content.drag_to_container(content_path2, 'Container 2')
        Designer.Dialog.AddContent.wait_until_visible(30)
        Designer.Dialog.AddContent.select('Add content')
        Designer.Dialog.AddContent.wait_until_invisible(30)
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Enter 'TestDrill2' in the Classes textbox under Content properties for Blue tab.
        """
        Designer.PropertiesPanel.Settings.ContentSettings.Classes.enter_text('TestDrill2')  
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click New tab button in Tab container.
            Enter 'TestDrill3' in the Classes textbox under Content properties for Tab 3.
        """
        Designer.PageCanvas.Containers.Tab('Container 2').add_new_tab()
        Designer.PropertiesPanel.Settings.ContentSettings.Classes.enter_text('TestDrill3')
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_12 = """
            STEP 12 : Select Panel 3 content;
            Enter 'QtySoldDetailPanel' in the Classes textbox under Content properties.
        """
        Designer.PageCanvas.Containers.Basic('Container 3').select(location='middle')
        Designer.PropertiesPanel.Settings.ContentSettings.Classes.enter_text('QtySoldDetailPanel')
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click on Run in new window icon in the toolbar
        """
        Designer.VisualizationToolBar.RunInNewWindow.click()
        Designer._core_utils.switch_to_new_window()
        Designer.RunMode.PageCanvas.wait_for_text('Page Heading')
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify page loads successfully with added contents.
        """
        Designer.RunMode.PageCanvas.Containers.verify_containers_title(['drill_with_multiple_procedures', 'Container 2', 'Container 3'], '13.01')
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').verify_areas_title(['drill_with_multiple_procedures', 'drill_from_multi_parameters'], '13.02')
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').switch_to_frame('drill_with_multiple_procedures')
        HtmlReport.wait_for_text('SALES')
#         HtmlReport.convert_to_excel(data_set)
        HtmlReport.verify_data(data_set, '13.03')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').expand_area('drill_from_multi_parameters')
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').switch_to_frame('drill_from_multi_parameters')
        HtmlReport.wait_for_text('EMEA')
#         HtmlReport.convert_to_excel(data_set2)
        HtmlReport.verify_data(data_set2, '13.04')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '13.05')
        PieChart.verify_legend_title(['Product Category'], '13.06')
        PieChart.verify_number_of_risers(7, '13.07')
        PieChart.verify_total_lables(['1.1B'], '13.08')
        PieChart.verify_riser_color([(1, 'bar_blue')], '13.09')
        PieChart.verify_pie_labels(['Revenue'], '13.10')
        Designer._core_utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Blue')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        HtmlContentChart.verify_content_background('blue', '13.11')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on ENGLAND in drill_with_multiple_procedures.
        """
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').expand_area('drill_with_multiple_procedures')
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').switch_to_frame('drill_with_multiple_procedures')
        HtmlReport.wait_for_text('SALES')
        HtmlReport.click_on_hyperlink_cell(2, 1)
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Click on each tab in Panel 2, verify drill down procedures is displayed with ENGLAND values.
        """
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Category Sales')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        BarChart.wait_for_text('CAR', 60)
        BarChart.verify_xaxis_title(['CAR'], '14.01')
        BarChart.verify_xaxis_labels(['JAGUAR', 'JENSEN', 'TRIUMPH'], '14.02')
        BarChart.verify_yaxis_title(['DEALER_COST'], '14.03')
        BarChart.verify_yaxis_labels(['0', '4K', '8K', '12K', '16K', '20K'], '14.04')
        BarChart.verify_number_of_risers(3, '14.05')
        BarChart.verify_riser_color([(1, 'bar_blue')], '14.06')
        Designer._utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Blue')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        AreaChart.verify_number_of_risers(1, '14.07')
        AreaChart.verify_xaxis_labels(['JAGUAR', 'JENSEN', 'TRIUMPH'], '14.08')
        AreaChart.verify_xaxis_title(['CAR'], '14.09')
        AreaChart.verify_yaxis_title(['DEALER_COST'], '14.10')
        AreaChart.verify_yaxis_labels(['0', '4K', '8K', '12K', '16K', '20K'], '14.11')
        AreaChart.verify_riser_color([(1, 'bar_blue')], '14.12')
        Designer._utils.switch_to_default_content()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Tab 3')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        PieChart.wait_for_text('DEALER_COST', 120)
        PieChart.verify_legend_labels(['JAGUAR', 'JENSEN', 'TRIUMPH'], '14.13')
        PieChart.verify_legend_title(['CAR'], '14.14')
        PieChart.verify_number_of_risers(3, '14.15')
        PieChart.verify_riser_color([(1, 'bar_blue')], '14.16')
        PieChart.verify_pie_labels(['DEALER_COST'], '14.17')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Select drill_from_multi_parameters area.
            Click on '46,386' value in North America.
        """
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').expand_area('drill_from_multi_parameters')
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').switch_to_frame('drill_from_multi_parameters')
        HtmlReport.wait_for_text('EMEA')
        HtmlReport.click_on_hyperlink_cell(4, 2)
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify panel 3 updated with drill down procedure.
        """
        Designer.RunMode.PageCanvas.Containers.Basic('Container 3').switch_to_frame()
        MapChart.wait_for_text('2016', 150)
        # MapChart.verify_number_of_risers(33, '15.01')
        MapChart.verify_legend_title(['Gross Profit'], '15.02')
        MapChart.verify_legend_labels(['0.7K', '149.3K', '297.9K', '446.5K', '595K', '743.7K', '892.3K', '892.3K'], '15.03')
        MapChart.verify_map_title(['2016 North America Sales Profitability'], '15.04')
        MapChart.verify_scale_title(['Quantity Sold'], '15.05')
        MapChart.verify_scale_values(['10.8K', '5.4K', '0K'], '15.06')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Close the run window.
        """
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Click Save and enter C9947192 in Title and click Save;
            Close the designer.
        """
        Designer.ToolBar.save(file_name)
        Designer._core_utils.switch_to_previous_window()
        Designer._utils.capture_screenshot("17", STEP_17)

        STEP_18 = """
            STEP 18 : Right click on 'C9947192' and select Run.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.right_click_on_file(file_name)
        HomePage.ContextMenu.select('Run')
        HomePage.RunWindow.switch_to_frame()
        Designer._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Click on W GERMANY in 'drill_with_procedure' panel.
        """
        Designer.RunMode.PageCanvas.wait_for_text('Page Heading')
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').switch_to_frame('drill_with_multiple_procedures')
        HtmlReport.wait_for_text('SALES')
        HtmlReport.click_on_hyperlink_cell(6, 1)
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify only W GERMANY values are visible in panel 2.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Category Sales')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        BarChart.wait_for_text('CAR', 60)
        BarChart.verify_xaxis_title(['CAR'], '19.01')
        BarChart.verify_xaxis_labels(['AUDI', 'BMW'], '19.02')
        BarChart.verify_yaxis_title(['DEALER_COST'], '19.03')
        BarChart.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '19.04')
        BarChart.verify_number_of_risers(2, '19.05')
        BarChart.verify_riser_color([(1, 'bar_blue')], '19.06')
        Designer._utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Blue')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        AreaChart.wait_for_text('CAR', 100)
        AreaChart.verify_number_of_risers(1, '19.07')
        AreaChart.verify_xaxis_labels(['AUDI', 'BMW'], '19.08')
        AreaChart.verify_xaxis_title(['CAR'], '19.09')
        AreaChart.verify_yaxis_title(['DEALER_COST'], '19.10')
        AreaChart.verify_yaxis_labels(['0', '10K', '20K', '30K', '40K', '50K', '60K'], '19.11')
        AreaChart.verify_riser_color([(1, 'bar_blue')], '19.12')
        Designer._utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Tab 3')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        PieChart.wait_for_text('DEALER_COST', 120)
        PieChart.verify_legend_labels(['AUDI', 'BMW'], '19.13')
        PieChart.verify_legend_title(['CAR'], '19.14')
        PieChart.verify_number_of_risers(2, '19.15')
        PieChart.verify_riser_color([(1, 'bar_blue')], '19.16')
        PieChart.verify_pie_labels(['DEALER_COST'], '19.17')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Click Options in Panel 2 and click Refresh.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').ToolBar.Options.click()
        Designer.ContextMenu.select('Refresh')
        Designer._utils.capture_screenshot("20", STEP_20)

        STEP_20_EXPECTED = """
            STEP 20 - Expected : Verify restored back to original chart.
        """
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Category Sales')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        PieChart.wait_for_text('Revenue', 120)
        PieChart.verify_legend_labels(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '20.01')
        PieChart.verify_legend_title(['Product Category'], '20.02')
        PieChart.verify_number_of_risers(7, '20.03')
        PieChart.verify_total_lables(['1.1B'], '20.04')
        PieChart.verify_riser_color([(1, 'bar_blue')], '20.05')
        PieChart.verify_pie_labels(['Revenue'], '20.06')
        Designer._core_utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Blue')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        HtmlContentChart.verify_content_background('blue', '20.07')
        Designer._utils.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').select('Tab 3')
        Designer.RunMode.PageCanvas.Containers.Tab('Container 2').switch_to_frame()
        PieChart.wait_for_text('DEALER_COST', 120)
        PieChart.verify_legend_labels(['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH'], '20.08')
        PieChart.verify_legend_title(['CAR'], '20.09')
        PieChart.verify_number_of_risers(10, '20.10')
        PieChart.verify_riser_color([(1, 'bar_blue')], '20.11')
        PieChart.verify_pie_labels(['DEALER_COST'], '20.12')
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("20 - Expected", STEP_20_EXPECTED, True)

        STEP_21 = """
            STEP 21 : Select drill_from_multi_parameters area.
            Click on '165' value in Oceania.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').expand_area('drill_from_multi_parameters')
        Designer.RunMode.PageCanvas.Containers.Accordion('drill_with_multiple_procedures').switch_to_frame('drill_from_multi_parameters')
        HtmlReport.wait_for_text('EMEA')
        HtmlReport.click_on_hyperlink_cell(5, 3)
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify Panel 3 updated with drilldown procedure.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Containers.Basic('Container 3').switch_to_frame()
        MapChart.wait_for_text('2017', 150)
        MapChart.verify_number_of_risers(7, '21.01')
        MapChart.verify_legend_title(['Gross Profit'], '21.02')
        MapChart.verify_legend_labels(['128', '315.8', '503.6', '691.4', '879.2', '1,067', '1,254.7'], '21.03')
        MapChart.verify_map_title(['2017 Oceania Sales Profitability'], '21.04')
        MapChart.verify_scale_title(['Quantity Sold'], '21.05')
        MapChart.verify_scale_values(['16', '2'], '21.06')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Click Refresh icon in the page toolbar.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.switch_to_frame()
        Designer.RunMode.PageCanvas.Heading.Refresh.click()
        Designer._utils.capture_screenshot("22", STEP_22)

        STEP_22_EXPECTED = """
            STEP 22 - Expected : Verify Panel 3 restored back to original state.
        """
        Designer.RunMode.PageCanvas.Containers.Basic('Container 3').switch_to_frame()
        Designer._webelement.verify_elements_text(Designer._utils.validate_and_get_webdriver_objects("body[style^='font-family']", "Container 3 content"), ['Select a Quantity Sold value to see this report...'], '22', 'Container 3 content')
        Designer._utils.switch_to_default_content()
        Designer._utils.capture_screenshot("22 - Expected", STEP_22_EXPECTED, True)

        STEP_23 = """
            STEP 23 : Close the designer.
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Workspaces.switch_to_default_content()
        Designer._utils.capture_screenshot("23", STEP_23)

        STEP_24 = """
            STEP 24 : Sign out WF.
        """
        HomePage.Banner.click_user()
        HomePage.Banner.sign_out()
        Designer._utils.capture_screenshot("24", STEP_24)

