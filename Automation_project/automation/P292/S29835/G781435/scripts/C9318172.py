"""-------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 11-September-2019
-------------------------------------------------------------"""
from common.wftools.designer_chart import Designer_Chart
from common.lib.basetestcase import BaseTestCase

class C9318172_TestClass(BaseTestCase):
    
    def test_C9318172(self):
        
        """
            CLASS OBJECTS
        """
        designer_chart = Designer_Chart(self.driver)
        
        """
            VARIABLES
        """
        xaxis_title = ['COUNTRY']
        yaxis_title = ['RETAIL_COST']
        preview_chart_css = "[id*='chartpreview']"
        run_chart_css = "#jschart_HOLD_0"
        xaxis_labels = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        yaxis_labels = ['0', '10K', '20K', '30K', '40K', '50K', '60K', '70K']
        legends = ['SALES', '0', '14.7K', '29.4K', '44K', '58.8K', '73.5K', '88.2K']
        
        """
            STEP 01 : Create new designer chart with CAR using API call
            http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG730863%2F&master=ibisamp%2Fcar&tool=chart
        """
        designer_chart.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart.wait_for_visible_text(preview_chart_css, "Group", designer_chart.chart_long_timesleep)
        
        """
            STEP 02 : Double click COUNTRY & RETAIL_COST
        """
        designer_chart.double_click_on_dimension_field('COUNTRY')
        designer_chart.wait_for_visible_text(preview_chart_css, "COUNTRY", designer_chart.chart_short_timesleep)
        
        designer_chart.double_click_on_measures_field('COMP->CARREC->BODY->RETAIL_COST')
        designer_chart.wait_for_visible_text(preview_chart_css, "RETAIL_COST", designer_chart.chart_short_timesleep)
        
        """
            STEP 03 : Drag SALES to Color bucket
        """
        designer_chart.drag_measure_field_to_query_bucket('SALES', 'Color')
        designer_chart.wait_for_visible_text(preview_chart_css, "SALES", designer_chart.chart_short_timesleep)
        
        """
            STEP 03 - Expected : Verify preview chart
        """
        designer_chart.verify_number_of_risers(preview_chart_css + " rect", 1, 5, "Step 03.01")
        designer_chart.verify_x_axis_title_in_preview(xaxis_title, msg="Step 03.02")
        designer_chart.verify_y_axis_title_in_preview(yaxis_title, msg="Step 03.03")
        designer_chart.verify_x_axis_label_in_preview(xaxis_labels, msg="Step 03.04")
        designer_chart.verify_y_axis_label_in_preview(yaxis_labels, msg="Step 03.05")
        designer_chart.verify_legends_in_preview(legends, msg="Step 03.06")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", "Solitude", msg="Step 03.07 ")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g2!mbar!']", "French_Pass", msg="Step 03.08 ")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g4!mbar!']", "Cobalt", msg="Step 03.09 ")
        
        """
            STEP 04 : Right click SALES in Color bucket > Set color range
        """
        designer_chart.select_query_bucket_field_context_menu("Color", "SALES", "Set color ranges...")
        
        """
            STEP 04 - Expected : Verify "Set Colors Ranges" dialog displayed
        """
        designer_chart.set_color_ranges_dialog().verify_title("04.01")
        
        """
            STEP 05 : Expand Color in dialog > Select Red/Orange
        """
        designer_chart.set_color_ranges_dialog().select_color("Red/Orange")
        designer_chart.set_color_ranges_dialog().click_ok_button()
        designer_chart.wait_for_visible_text(preview_chart_css, "70.6K", designer_chart.chart_short_timesleep)
        
        """
            STEP 05 - Expected : Verify preview chart 
        """
        legends = ['SALES', '0', '17.6K', '35.3K', '53K', '70.6K', '88.2K']
        designer_chart.verify_number_of_risers(preview_chart_css + " rect", 1, 5, "Step 05.01")
        designer_chart.verify_x_axis_title_in_preview(xaxis_title, msg="Step 05.02")
        designer_chart.verify_y_axis_title_in_preview(yaxis_title, msg="Step 05.03")
        designer_chart.verify_x_axis_label_in_preview(xaxis_labels, msg="Step 05.04")
        designer_chart.verify_y_axis_label_in_preview(yaxis_labels, msg="Step 05.05")
        designer_chart.verify_legends_in_preview(legends, msg="Step 05.06")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", "woundering", msg="Step 05.07 ")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g2!mbar!']", "kournikova1", msg="Step 05.08 ")
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g4!mbar!']", "venetian_red", msg="Step 05.09 ")
        
        """
            STEP 06 : Run
        """
        designer_chart.click_toolbar_item('preview')
        designer_chart.switch_to_run_preview_frame()
        designer_chart.wait_for_visible_text(run_chart_css, "SALES", designer_chart.chart_medium_timesleep)
        
        """
            STEP 06 - Expected : Verify run chart
        """
        designer_chart.verify_number_of_risers(run_chart_css + " rect", 1, 5, "Step 06.01")
        designer_chart.verify_x_axis_title_in_preview(xaxis_title, msg="Step 06.02", parent_css=run_chart_css)
        designer_chart.verify_y_axis_title_in_preview(yaxis_title, msg="Step 06.03", parent_css=run_chart_css)
        designer_chart.verify_x_axis_label_in_preview(xaxis_labels, msg="Step 06.04", parent_css=run_chart_css)
        designer_chart.verify_y_axis_label_in_preview(yaxis_labels, msg="Step 06.05", parent_css=run_chart_css)
        designer_chart.verify_legends_in_preview(legends, msg="Step 05.06", parent_css=run_chart_css)
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", "woundering", msg="Step 06.07 ", parent_css=run_chart_css)
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g2!mbar!']", "kournikova1", msg="Step 06.08 ", parent_css=run_chart_css)
        designer_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g4!mbar!']", "venetian_red", msg="Step 06.09 ", parent_css=run_chart_css)
        
        """
            STEP 07 : Logout using API
        """
        designer_chart.switch_to_default_content()