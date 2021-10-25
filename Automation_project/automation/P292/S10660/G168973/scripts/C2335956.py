"""-------------------------------------------------------------------------------------------
Created on August 26, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2335956
Test Case Title =  Insight - Show Data Label feature
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart
from common.wftools.designer_chart import Designer_Insight
from common.lib.utillity import UtillityMethods

class C2335956_TestClass(BaseTestCase):

    def test_C2335956(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        insight = Designer_Insight(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        qwerty_tree_css = "#queryTreeWindow"
        chart_css = "#pfjTableChart_1"
        
        """
            STEP 1 : Launch IA Chart using wf_retail_lite.mas in developer user.
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10660%2FG168204%2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite", mrid="mrid", mrpass="mrpass", folder_path="P292_S10660%2FG168204")
        chart.wait_for_visible_text(chart_css, "Group 0")
        
        """
            STEP 2 : Double click "Cost of Goods" & "Product, Category"
        """
        chart.double_click_on_datetree_item("Cost of Goods", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Cost of Goods")
        
        chart.double_click_on_datetree_item("Product,Category", 1)
        chart.wait_for_visible_text(qwerty_tree_css, "Product,Category")
        
        """
            STEP 2.1 : Fields added to query pane and canvas updated.
        """
        chart.verify_all_fields_in_query_pane(['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Cost of Goods', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate'], "Step 2.1 : Fields added to query pane and canvas updated.")
        chart.verify_x_axis_label_in_preview(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg = 'Step 2.2 : Fields added to query pane and canvas updated')
        chart.verify_x_axis_title_in_preview(['Product Category'], msg= 'Step 2.3 : Fields added to query pane and canvas updated.')
        chart.verify_y_axis_label_in_preview(['0', '40M', '80M', '120M', '160M', '200M', '240M'], msg = 'Step 2.4 : Fields added to query pane and canvas updated')
        chart.verify_y_axis_title_in_preview(['Cost of Goods'], msg = 'Step 2.5 : Fields added to query pane and canvas updated')
        chart.verify_number_of_risers('#pfjTableChart_1 rect', 1, 7, 'Step 2.6 : Fields added to query pane and canvas updated')
        
        """
            STEP 3 : Select Format tab > Run with > Enable "Insight".
        """
        chart.select_ia_ribbon_item("Format", "run_with")
        chart.select_ia_ribbon_item("Format", "insight")
        
        """
            STEP 4 : Click Run button.
        """
        chart.run_report_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text("div.header-box", "Vertical")
        
        """
            STEP 4.1 : Chart displayed in run time.
        """
        chart.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css = "#runbox_id", msg="Step 4.1 : Chart displayed in run time")
        chart.verify_y_axis_label_in_run_window(['0', '40M', '80M', '120M', '160M', '200M', '240M'], parent_css = "#runbox_id", msg="Step 4.2 : Chart displayed in run time")
        chart.verify_x_axis_title_in_run_window(['Product Category'], parent_css = "#runbox_id", msg = "Step 4.3 : Chart displayed in run time")
        chart.verify_y_axis_title_in_run_window(['Cost of Goods'], parent_css = "#runbox_id", msg = "Step 4.4 : Chart displayed in run time")
        chart.verify_number_of_risers("#runbox_id rect", 1, 7, msg = "Step 4.5")
        chart.verify_chart_color('runbox_id', "riser!s0!g0!ay1!mbar!", 'bar_blue', msg = 'STEP 4.6 : Chart displayed in run time')
        
        """
            STEP 5 : Hover over the three vertical dots until you see the tool tip "More Options" and then click on the icon
            STEP 6 : Select "Show Data Label" options.
        """
        more_options_obj = utils.validate_and_get_webdriver_object('div.more-options-button', "More Option css")
        actual_result = more_options_obj.get_attribute('title')
        msg = 'Step 5.1 : Hover over the three vertical dots until you see the tool tip "More Options" and then click on the icon'
        utils.asequal('More Options', actual_result, msg)
        
        insight.select_more_options_in_preview("Show Data Label")
        chart.wait_for_visible_text("#runbox_id", "89.8M")
        
        """
            STEP 6.1 : The Data label value is displayed at top of each riser.
        """
        data_labels_list = ['89.8M', '104.9M', '69.8M', '190.2M', '205.1M', '61.6M', '40.1M', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Product Category', '0', '40M', '80M', '120M', '160M', '200M', '240M', 'Cost of Goods']
        chart.verify_x_axis_label_in_run_window(data_labels_list, parent_css= '#runbox_id', xyz_axis_label_css="text", msg = 'STEP 6.1 : The Data label value is displayed at top of each riser')
        
        """
            STEP 7 : Click on "Change chart" option > select chart type "Pie" chart.
        """
        insight.select_chart_from_chartpicker("Ring Pie")
        chart.wait_for_visible_text("#runbox_id", "761.4M")
        
        """
            STEP 7.1 : Vertical bar is converted to Pie chart and Data labels changes from the value to Percentage.
        """
        chart.verify_x_axis_label_in_run_window(['12%', '14%', '9%', '25%', '27%', '8%', '5%', 'Cost of Goods', '761.4M', 'Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css= '#runbox_id', xyz_axis_label_css="text", msg = 'Step 7.1 : Vertical bar is converted to Pie chart and Data labels changes from the value to Percentage')
        chart.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css = '#runbox_id', msg = 'Step 7.2 : Vertical bar is converted to Pie chart and Data labels changes from the value to Percentage')
        chart.verify_number_of_pie_segments('#runbox_id', 1, 7, msg = 'Step 7.3 : Vertical bar is converted to Pie chart and Data labels changes from the value to Percentage.')
        chart.verify_chart_color('runbox_id', 'riser!s4!g0!mwedge!', 'brick_red', msg = 'Step 7.4 : Vertical bar is converted to Pie chart and Data labels changes from the value to Percentage')
        
        """
            STEP 8 : Click on More Options >> Un-check "Show Data Label"
        """
        insight.select_more_options_in_preview("Show Data Label")
        utils.synchronize_until_element_disappear("text[class='dataLabels!s5!g0!mdataLabels!']", chart.home_page_medium_timesleep)
        
        """
            STEP 8.1 : Data Labels are removed for Pie Chart.
        """
        chart.verify_x_axis_label_in_run_window(['Cost of Goods', '761.4M', 'Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css= '#runbox_id', xyz_axis_label_css="text", msg = 'Step 8.1 : Data Labels are removed for Pie Chart')
        
        """
            STEP 9 : Again click on More Options > Check "Show Data Label" option
        """
        insight.select_more_options_in_preview("Show Data Label")
        utils.synchronize_until_element_is_visible("text[class='dataLabels!s5!g0!mdataLabels!']", chart.home_page_medium_timesleep)
        
        """
            STEP 9.1 : Data Labels are enabled for Pie Chart and values displayed as percentage.
        """
        chart.verify_x_axis_label_in_run_window(['12%', '14%', '9%', '25%', '27%', '8%', '5%', 'Cost of Goods', '761.4M', 'Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css= '#runbox_id', xyz_axis_label_css="text", msg = 'Step 9.1 : Vertical bar is converted to Pie chart and Data labels changes from the value to Percentage')
        chart.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css = '#runbox_id', msg = 'Step 9.2 : Data Labels are enabled for Pie Chart and values displayed as percentage.')
        chart.verify_number_of_pie_segments('#runbox_id', 1, 7, msg = 'Step 9.3 : Data Labels are enabled for Pie Chart and values displayed as percentage.')
        chart.verify_chart_color('runbox_id', 'riser!s4!g0!mwedge!', 'brick_red', msg = 'Step 9.4 : Data Labels are enabled for Pie Chart and values displayed as percentage.')
        
        """
            STEP 10 : Click on "Change chart" option > Select "Vertical Bar" chart.
        """
        insight.select_chart_from_chartpicker("Vertical Bar")
        chart.wait_for_visible_text("#runbox_id", "89.8M")
        
        """
            STEP 10.1 : Pie chart is converted to Vertical Bar Chart & Data Labels changes from Percentage to Values.
        """
        data_labels_list = ['89.8M', '104.9M', '69.8M', '190.2M', '205.1M', '61.6M', '40.1M', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Product Category', '0', '40M', '80M', '120M', '160M', '200M', '240M', 'Cost of Goods']
        chart.verify_x_axis_label_in_run_window(data_labels_list, parent_css= '#runbox_id', xyz_axis_label_css="text", msg = 'Step 10.1 : Pie chart is converted to Vertical Bar Chart & Data Labels changes from Percentage to Values.')
        chart.verify_x_axis_label_in_run_window(['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css = "#runbox_id", msg="Step 10.2 : Pie chart is converted to Vertical Bar Chart & Data Labels changes from Percentage to Values.")
        chart.verify_y_axis_label_in_run_window(['0', '40M', '80M', '120M', '160M', '200M', '240M'], parent_css = "#runbox_id", msg="Step 10.3 : Pie chart is converted to Vertical Bar Chart & Data Labels changes from Percentage to Values.")
        chart.verify_x_axis_title_in_run_window(['Product Category'], parent_css = "#runbox_id", msg = "Step 10.4 : Pie chart is converted to Vertical Bar Chart & Data Labels changes from Percentage to Values.")
        chart.verify_y_axis_title_in_run_window(['Cost of Goods'], parent_css = "#runbox_id", msg = "Step 10.5 : Pie chart is converted to Vertical Bar Chart & Data Labels changes from Percentage to Values.")
        chart.verify_number_of_risers("#runbox_id rect", 1, 7, msg = "Step 10.6")
        chart.verify_chart_color('runbox_id', "riser!s0!g3!mbar!", 'bar_blue', msg = 'STEP 10.7 : Pie chart is converted to Vertical Bar Chart & Data Labels changes from Percentage to Values.')
        chart.switch_to_default_content()
        
        """
            STEP 11 : Click Save icon from the toolbar > Enter title as "C2335956" > Click Save button.
        """
        chart.select_item_in_top_toolbar('save')
        chart.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        
        chart.save_file_in_save_dialog("C2335956")
        utils.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", chart.home_page_medium_timesleep)
        
        """
            STEP 12 : Logout:
            http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        chart.api_logout()

if __name__ == '__main__':
    unittest.main()  