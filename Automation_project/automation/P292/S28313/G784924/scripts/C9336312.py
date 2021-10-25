"""
Created on Sep 7, 2019

@author: Niranjan
Test rail title: New Bucketized Funnel chart
Test rail link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9336312
"""
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
import unittest, time

class C9336312_TestClass(BaseTestCase):

    def test_C9336312(self):
    
        """
            CLASS OBJECTS
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
       
        """
            VARIABLES
        """
        case_id = "C9336312"
        preview_chart_id = "pfjTableChart_1"
        preview_chart_css = "#"  +preview_chart_id
        run_chart_id = "jschart_HOLD_0"
        run_chart_css = "#" + run_chart_id
        riser_css = "riser!s0!g0!mriser!"
        
        STEP_01 = """
            STEP 01 : Launch IA Chart using wf_retail_lite.mas in developer user.
                      http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671912%2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        chart.invoke_chart_tool_using_api('baseapp/wf_retail_lite')
        chart.wait_for_visible_text(preview_chart_css, "Group", chart.chart_long_timesleep)
        utils.capture_screenshot("01", STEP_01)
        
        STEP_02 = """
            STEP 02 : Select Format tab > Chart Type > Other > Special > Select "Funnel chart" > Click OK button
            STEP 02.01 : The following Funnel chart Preview and query pane buckets.
        """
        legends = ['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4']
        data_labels = ['Group 0', 'Group 1']
        chart.select_ia_ribbon_item("Format", "other")
#        utils.synchronize_until_element_is_visible("#ChartTypeGroup_Special img", chart.home_page_long_timesleep)
        utils.synchronize_with_visble_text("#ChartTypeGroup_Special", 'Special', chart.home_page_long_timesleep)
        time.sleep(3) #giving time to locate properly
        chart.select_other_chart_type("special", "funnel", 6, verify_selection=False)
        utils.synchronize_until_element_is_visible(preview_chart_css + " path[class*='riser']", chart.chart_short_timesleep)
        utils.capture_screenshot("02", STEP_02, True)
        chart.verify_number_of_risers(preview_chart_css + " path", 2, 5, "Step 02.01")
        chart.verify_legends_in_preview(legends, msg="Step 02.02")
        chart.verify_chart_color(preview_chart_id, riser_css, "bar_blue", "Step 02.03 : Verify bar riser color")
        chart.verify_data_labels(preview_chart_id, data_labels, "Step 02.04 : Verify data labels", custom_css=".chartPanel text")
        
        STEP_03 = """
            STEP 03 : Double click "Cost of Goods" to add the field to Measure bucket.
        """
        chart.double_click_on_datetree_item("Cost of Goods", 1)
        chart.wait_for_visible_text(preview_chart_css, "Cost of Goods", chart.chart_short_timesleep)
        utils.capture_screenshot("03", STEP_03)
        
        STEP_04 = """
            STEP 04 : Drag and drop "Sale, Year" to Color BY bucket
            STEP 04.01 : Fields added to appropriate bucket and canvas updated.
        """
        legends = ['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016'] 
#         legends = ['Sale Year', '2016', '2017', '2018', '2019', '2020', '2021'] 
        data_labels = ['Cost of Goods']
        chart.drag_field_from_data_tree_to_query_pane("Sale,Year", 1, "Color BY")
        chart.wait_for_visible_text(preview_chart_css, "Sale Year", chart.chart_short_timesleep)
        utils.capture_screenshot("04", STEP_04, True)
        chart.verify_number_of_risers(preview_chart_css + " path", 1, 6, "Step 04.01")
        chart.verify_legends_in_preview(legends, msg="Step 04.02")
        chart.verify_chart_color(preview_chart_id, riser_css, "bar_blue", "Step 04.03 : Verify bar riser color")
        chart.verify_data_labels(preview_chart_id, data_labels, "Step 04.04 : Verify data labels", custom_css=".chartPanel text")
        
        STEP_05 = """
            STEP 05 : Click Run and Hover on chart.
            STEP 05.01 : The following run time chart and tooltip value displayed
        """
        tooltip = ['Sale Year:2011', 'Cost of Goods:$34,631,123.00  (4.55%)']
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(run_chart_css, "Sale Year", chart.chart_short_timesleep)
        utils.capture_screenshot("05", STEP_05, True)
        chart.verify_number_of_risers(run_chart_css + " path", 1, 6, "Step 05.01")
        chart.verify_legends_in_run_window(legends, msg="Step 05.02")
        chart.verify_chart_color(run_chart_id, riser_css, "bar_blue", "Step 05.03 : Verify bar riser color")
        chart.verify_data_labels(run_chart_id, data_labels, "Step 05.04 : Verify data labels", custom_css=".chartPanel text")
        chart.verify_tooltip_in_run_window(riser_css, tooltip, "Step 05.05 : Verify tooltip")
        chart.switch_to_default_content()
        
        STEP_06 = """
            STEP 06 : Close the output.
        """
        chart.close_run_preview_window()
        utils.capture_screenshot("06", STEP_06)
        
        STEP_07 = """
            STEP 07 : Right click on "Revenue" in data pane "Add To Query" > Click Measure
                      Right click on "Gross Profit" in data pane "Add To Query" > Click Tooltip.
        """
        chart.right_click_on_datetree_item("Revenue", 1, "Add To Query->Measure")
        chart.wait_for_visible_text(preview_chart_css, "Revenue", chart.chart_short_timesleep)
            
        chart.right_click_on_datetree_item("Gross Profit", 1, "Add To Query->Tooltip")
        chart.wait_for_visible_text("#queryTreeColumn", "Gross Profit", chart.chart_short_timesleep)
        utils.capture_screenshot("07", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Fields added to appropriate bucket and canvas updated.
        """
        legends =['Sale Year', '2011', '2012', '2013', '2014', '2015', '2016']
#         legends = ['Sale Year', '2016', '2017', '2018', '2019', '2020', '2021']
        data_labels = ['Cost of Goods', 'Revenue']
        chart.verify_number_of_risers(preview_chart_css + " path", 2, 6, "Step 07.01")
        chart.verify_legends_in_preview(legends, msg="Step 07.02")
        chart.verify_chart_color(preview_chart_id, riser_css, "bar_blue", "Step 07.03 : Verify bar riser color")
        chart.verify_data_labels(preview_chart_id, data_labels, "Step 07.04 : Verify data labels", custom_css=".chartPanel text")
        utils.capture_screenshot("07.01", STEP_07_01)
        
        STEP_08 = """
            STEP 08 : Click Run and Hover on chart.
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(run_chart_css, "Sale Year", chart.chart_short_timesleep)
        utils.capture_screenshot("08", STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : The following run time chart and tooltip value displayed.
                         Expect to see Revenue and Gross Profit added.
        """
        tooltip = ['Sale Year:2014', 'Revenue:$126,675,660.19  (11.94%)', 'Gross Profit:$36,298,871.19']
#         tooltip = ['Sale Year:2019', 'Revenue:$126,675,660.19 (11.94%)', 'Gross Profit:$36,298,871.19']
        chart.verify_number_of_risers(run_chart_css + " path", 2, 6, "Step 08.01")
        chart.verify_legends_in_run_window(legends, msg="Step 08.02")
        chart.verify_chart_color(run_chart_id, riser_css, "bar_blue", "Step 08.03 : Verify bar riser color")
        chart.verify_data_labels(run_chart_id, data_labels, "Step 08.04 : Verify data labels", custom_css=".chartPanel text")
        chart.verify_tooltip_in_run_window("riser!s3!g1!mriser!", tooltip, "Step 08.05 : Verify tooltip")
        chart.switch_to_default_content()
        utils.capture_screenshot("08.01", STEP_08_01)
        
        STEP_09 = """
            STEP 09 : Click Save icon from the toolbar > Enter title as "C9336312" > Click Save button
        """
        chart.save_as_chart_from_menubar(case_id)
        utils.capture_screenshot("09", STEP_09)
        
        STEP_10 = """
            STEP 10 : Logout using API
        """
        chart.api_logout()
        utils.capture_screenshot("10", STEP_10)
        
        STEP_11 = """
            STEP 11 : Restore the C9336312.fex using API (edit the domain, port and alias of the URL - do not use the URL as is)
        """
        chart.edit_fex_using_api_url(None, fex_name=case_id)
        chart.wait_for_visible_text(preview_chart_css, "Sale Year", chart.chart_long_timesleep)
        utils.capture_screenshot("11", STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Chart restored successfully without error
        """
        chart.verify_number_of_risers(preview_chart_css + " path", 2, 6, "Step 11.01")
        chart.verify_legends_in_preview(legends, msg="Step 11.02")
        chart.verify_chart_color(preview_chart_id, riser_css, "bar_blue", "Step 11.03 : Verify bar riser color")
        chart.verify_data_labels(preview_chart_id, data_labels, "Step 11.04 : Verify data labels", custom_css=".chartPanel text")
        utils.capture_screenshot("11.01", STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Logout using API
        """
        chart.api_logout()
        utils.capture_screenshot("12", STEP_12)
        
if __name__ == "__main__":
    unittest.main()