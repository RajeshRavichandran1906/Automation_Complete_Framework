"""--------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 30-September-2019
--------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools import page_designer
from common.wftools.chart import Chart

class C8262176_TestClass(BaseTestCase):

    def test_C8262176(self):
        
        """
            CLASS OBJECTS
        """
        pd_design = page_designer.Design(self.driver)
        pd_preview = page_designer.Preview(self.driver)
        pd_run = page_designer.Run(self.driver)
        chart = Chart(self.driver)
        
        """
            VARIABLES
        """
        case_id = 'C8262176'
        filter_control_labels = ['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:']
        panels = ['Panel 1', 'Panel 3', 'Panel 2']
        contents = ['Category Sales', 'Discount by Region', 'Regional Sales Trend']
        chart_css = "#jschart_HOLD_0"
        canvas_css = ".pd-page-canvas"
        
        def verify_line_chart(step_num):
            chart.wait_for_visible_text(chart_css, 'Revenue', chart.chart_long_timesleep)
            x_axis = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            y_axis = ['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
            chart.verify_number_of_risers(chart_css + " path[class^='riser']", 1, 4, msg="Step " + step_num + ".01")
            chart.verify_x_axis_label_in_run_window(x_axis, msg="Step " + step_num + ".02")
            chart.verify_y_axis_label_in_run_window(y_axis, msg="Step " + step_num + ".03")
            chart.verify_x_axis_title_in_run_window(['Month'], msg="Step " + step_num + ".04")
            chart.verify_y_axis_title_in_run_window(['Revenue'], msg="Step " + step_num + ".05")
        
        def verify_pie_chart(step_num):
            chart.wait_for_visible_text(chart_css, 'Computers', chart.chart_long_timesleep)
            legends = ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
            chart.verify_number_of_risers(chart_css + " path[class^='riser']", 1, 7, msg="Step " + step_num + ".01")
            chart.verify_legends_in_run_window(legends, msg="Step " + step_num + ".02")
        
        def verify_tree_map_chart(step_num):
            chart.wait_for_visible_text(chart_css, 'EMEA', chart.chart_long_timesleep)
            x_axis = ['1', '2', '3', '4']
            z_axis = ['EMEA', 'North America', 'Oceania', 'South America']
            chart.verify_number_of_risers(chart_css + " rect[class^='riser']", 1, 16, msg="Step " + step_num + ".01")
            chart.verify_x_axis_label_in_run_window(x_axis, msg="Step " + step_num + ".02")
            chart.verify_z_axis_label_in_run_window(z_axis, msg="Step " + step_num + ".03")
            chart.verify_x_axis_title_in_run_window(['Sale Quarter', 'Store Region'], msg="Step " + step_num + ".04")
            
        """
            STEP 01 : Login WF as developer user.
            STEP 02 : Click on Content view from side bar.
            STEP 03 : Navigate to "P292_S28313" domain and Click on "G671868" folder
            STEP 04 : Click on "Page" action tile from under Designer tab
            STEP 05 : Choose "Grid 2-1 Side" template
        """
        pd_design.invoke_page_designer_and_select_template('Grid 2-1 Side')
        
        """
            STEP 05 - Expected : Verify page canvas for "Grid 2-1 Side" template appears as below
        """
        pd_design.verify_containers_title(panels, "Step 05.01 : Verify page canvas for 'Grid 2-1 Side' template appears")
        
        """
            STEP 06 : Navigate to "Retail Samples" domain > Portal >Small Widgets folder
        """
        pd_design.collapse_content_folder('G671868->P292_S28313')
        pd_design.expand_content_folder('Retail Samples->Portal->Small Widgets')
        
        """
            STEP 07 : Drag and drop "Category Sales", "Regional Sales Trend" and "Discount by Region" to Panel 1, Panel 2 and Panel 3 respectively
        """
        pd_design.drag_content_item_to_container(contents[0], panels[0], content_folder_path="")
        pd_design.drag_content_item_to_container(contents[2], panels[2], content_folder_path="")
        pd_design.drag_content_item_to_container(contents[1], panels[1], content_folder_path="")
        
        """
            STEP 07 - Expected : Verify the page Canvas
        """
        pd_design.verify_containers_title(contents, "Step 07.01 : Verify page canvas contains title")
        
        pd_design.switch_to_container_frame(contents[0])
        verify_pie_chart("07.02")
        pd_design.switch_to_default_page()
        
        pd_design.switch_to_container_frame(contents[2])
        verify_line_chart("07.03")
        pd_design.switch_to_default_page()
        
        pd_design.switch_to_container_frame(contents[1])
        verify_tree_map_chart("07.04")
        pd_design.switch_to_default_page()
        
        """
            STEP 08 : Click the "Preview" button in Toolbar
        """
        pd_design.click_preview()
        pd_design.wait_for_visible_text(canvas_css, contents[0], 120)
        
        """
            STEP 08 - Expected : Verify page appears as below
        """
        pd_preview.verify_containers_title(contents, "Step 08.01 : Verify page canvas contains title")
        
        pd_preview.switch_to_container_frame(contents[0])
        verify_pie_chart("08.02")
        pd_preview.switch_to_default_page()
        
        pd_preview.switch_to_container_frame(contents[2])
        verify_line_chart("08.03")
        pd_preview.switch_to_default_page()
        
        pd_preview.switch_to_container_frame(contents[1])
        verify_tree_map_chart("08.04")
        pd_preview.switch_to_default_page()
        
        """
            STEP 09 : Return back to designer using blue arrow in preview.
        """
        pd_preview.go_back_to_design_from_preview()
        
        """
            STEP 10 : Click in the section area and Click "Properties" in Toolbar
        """

        pd_design.select_page_section(1)
        pd_design.click_property()
        
        """
            STEP 11 : Click on "Style" tab and Select "Style 2" option.
        """
        pd_design.select_property_tab('Style')
        pd_design.select_section_style('Style 2')
        
        """
            STEP 11 - Expected : Verify styling applied on the page as below.
        """
        pd_design.verify_page_section_style_color(1, 'curious_blue', "11.01")
        
        """
            STEP 12 : Click on "Quick filter" icon in Toolbar
        """
        pd_design.click_quick_filter()
        
        """
            STEP 12 - Expected : Verify the cell padding (empty space) should appear below filter bar
        """
        pd_design.verify_filter_control_labels(filter_control_labels, "Step 12.01 : Verify the cell padding (empty space) should appear below filter bar")
        
        """
            STEP 13 : Click "Save" in toolbar Enter "C8262176" and Click "Save" button.
        """
        pd_design.save_page_from_toolbar(case_id)
        
        """
            STEP 14 : Click the Application menu and Select "Close"
        """
        pd_design.close_page_designer_from_application_menu()
        pd_design.switch_to_previous_window(driver_close=False)
        
        """
            STEP 15 : Right click on "C8262176" and Select "Run"
        """
        pd_design.run_page_designer(case_id)
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.wait_for_visible_text(canvas_css, contents[0], 120)
        
        """
            STEP 15 : Expected : Verify styling and cell padding applied on the page appears as below 
        """
        pd_run.verify_containers_title(contents, "Step 15.01 : Verify page canvas contains title")
        pd_run.verify_page_section_style_color(1, 'curious_blue', "15.01")
        pd_run.switch_to_container_frame(contents[0])
        verify_pie_chart("15.02")
        pd_run.switch_to_default_page()
        
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.switch_to_container_frame(contents[2])
        verify_line_chart("15.03")
        pd_run.switch_to_default_page()
        
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.switch_to_container_frame(contents[1])
        verify_tree_map_chart("15.04")
        pd_run.switch_to_default_page()
        
        pd_run.swtich_to_homepage_runwindow_frame()
        pd_run.verify_filter_control_labels(filter_control_labels, "Step 15.05 : Verify the cell padding (empty space) should appear below filter bar")
        pd_run.switch_to_default_page()
         
        """
            STEP 16 : Close the Run window.
        """
        pd_run.close_homepage_run_window()
        pd_run.switch_to_default_page()
        
        """
            STEP 17 : Logout WF
        """