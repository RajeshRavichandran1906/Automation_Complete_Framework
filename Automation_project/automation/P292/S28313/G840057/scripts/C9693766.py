"""---------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 23-August-2019
---------------------------------------------------------------------------------------"""
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase

class C9693766_TestClass(BaseTestCase):

    def test_C9693766(self):
    
        """
            CLASS OBJECTS
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
       
        """
            VARIABLES
        """
        case_id = "C9693766"
        preview_chart_id = "pfjTableChart_1"
        preview_chart_css = "#"  +preview_chart_id
        run_chart_id = "jschart_HOLD_0"
        run_chart_css = "#" + run_chart_id
        x_axis_title = ['COUNTRY']
        y_axis_title = ['DEALER_COST']
        x_axis_lables = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        y_axis_lables = ['0%', '20%', '40%', '60%', '80%', '100%']
        data_labels = ['100', '100', '100', '100', '100']
        tooltip = ['COUNTRY:ITALY', 'DEALER_COST:41,235']
        riser_css = "riser!s0!g2!mbar!"
        
        STEP_01 = """
            STEP 01 : Launch the IA API with chart - http://domain.com:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG840057&tool=chart&master=ibisamp/car
        """
        chart.invoke_chart_tool_using_api('ibisamp/car')
        chart.wait_for_visible_text(preview_chart_css, "Group", chart.chart_long_timesleep)
        utils.capture_screenshot("01", STEP_01)
        
        STEP_02 = """
            STEP 02 : Double click "COUNTRY", "DEALER_COST"
        """
        chart.double_click_on_datetree_item("COUNTRY", 1)
        chart.wait_for_visible_text(preview_chart_css, "COUNTRY", chart.chart_short_timesleep)
        
        chart.double_click_on_datetree_item("DEALER_COST", 1)
        chart.wait_for_visible_text(preview_chart_css, "DEALER_COST", chart.chart_short_timesleep)
        
        utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Click Format tab > Other > Bar > Select "Vertical Percent Bars"
            STEP 04 : Click OK button
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.select_other_chart_type("bar", "vertical_percent_bars", 3, verify_selection=False)
        chart.wait_for_visible_text(preview_chart_css, "100%", chart.chart_short_timesleep)
        utils.capture_screenshot("04", STEP_03)
        
        STEP_05 = """
            STEP 05 : Click Series tab > Enable "Data Labels"
            Verify Chart preview
        """
        chart.select_ia_ribbon_item("Series", "data_labels")
        chart.wait_for_visible_text(preview_chart_css + " .datalabels", "100", chart.chart_short_timesleep)
        utils.capture_screenshot("05", STEP_05, True)

        chart.verify_number_of_risers(preview_chart_css + " rect", 1, 5, "Step 05.01")
        chart.verify_x_axis_title_in_preview(x_axis_title, msg="Step 05.02")
        chart.verify_y_axis_title_in_preview(y_axis_title, msg="Step 05.03")
        chart.verify_x_axis_label_in_preview(x_axis_lables, msg="Step 05.04")
        chart.verify_y_axis_label_in_preview(y_axis_lables, msg="Step 05.05")
        chart.verify_data_labels(preview_chart_id, data_labels, "Step 05.06 : Verify data labels", custom_css="text[class^='dataLabels']")
        chart.verify_chart_color(preview_chart_id, riser_css, "bar_blue", "Step 05.07 : Verify bar riser color")
        
        STEP_06 = """
            STEP 06 : Click Run
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(run_chart_css, "100%", chart.chart_short_timesleep)
        utils.capture_screenshot("06", STEP_06, True)
        
        STEP_07 = """
            STEP 07 : Hover over chart riser
            STEP 07.01 : Tooltip value displayed 
        """
        chart.verify_number_of_risers(run_chart_css + " rect", 1, 5, "Step 07.01")
        chart.verify_x_axis_title_in_run_window(x_axis_title, msg="Step 07.02")
        chart.verify_y_axis_title_in_run_window(y_axis_title, msg="Step 07.03")
        chart.verify_x_axis_label_in_run_window(x_axis_lables, msg="Step 07.04")
        chart.verify_y_axis_label_in_run_window(y_axis_lables, msg="Step 07.05")
        chart.verify_data_labels(run_chart_id, data_labels, "Step 07.06 : Verify data labels", custom_css="text[class^='dataLabels']")
        chart.verify_chart_color(run_chart_id, riser_css, "bar_blue", "Step 07.07 : Verify bar riser color")
        chart.verify_tooltip_in_run_window(riser_css, tooltip, msg="Step 07.08 : Verify Tooltip value displayed ")
        utils.capture_screenshot("07", STEP_07, True)
        
        """
            STEP 08 : Close chart output window.
        """
        chart.switch_to_default_content()
        
        STEP_09 = """
            STEP 09 : Click Format tab > Other > Bar > Select "Horizontal Percent Bars"
            STEP 10 : Click OK button
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.select_other_chart_type("bar", "horizontal_percent_bars", 20, verify_selection=False)
        utils.wait_for_page_loads(chart.chart_short_timesleep)
        utils.capture_screenshot("10", STEP_09)
        
        STEP_11 = """
           STEP 11 : Click Run.
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(run_chart_css, "100%", chart.chart_short_timesleep)
        utils.capture_screenshot("11", STEP_11, True)
        
        STEP_12 = """
            STEP 12 : Hover over chart riser
            STEP 12.01 : Tooltip value displayed
        """ 
        chart.verify_number_of_risers(run_chart_css + " rect", 1, 5, "Step 12.01")
        chart.verify_x_axis_title_in_run_window(x_axis_title, msg="Step 12.02")
        chart.verify_y_axis_title_in_run_window(y_axis_title, msg="Step 12.03")
        chart.verify_x_axis_label_in_run_window(x_axis_lables, msg="Step 12.04")
        chart.verify_y_axis_label_in_run_window(y_axis_lables, msg="Step 12.05")
        chart.verify_data_labels(run_chart_id, data_labels, "Step 12.06 : Verify data labels", custom_css="text[class^='dataLabels']")
        chart.verify_chart_color(run_chart_id, riser_css, "bar_blue", "Step 12.07 : Verify bar riser color")
        chart.verify_tooltip_in_run_window(riser_css, tooltip, msg="Step 12.08 : Verify Tooltip value displayed ")
        utils.capture_screenshot("12", STEP_12, True)
        
        """
            STEP 13 : Close the output window
        """
        chart.switch_to_default_content()
        
        STEP_14 = """
            STEP 14 : Click Save > Enter title as "C9693766" > Click "Save"
        """
        chart.save_as_chart_from_menubar(case_id)
        utils.capture_screenshot("14", STEP_14)
        
        STEP_15 = """
            STEP 15 : Launch the IA API to logout.
        """
        chart.api_logout()
        utils.capture_screenshot("15", STEP_15)