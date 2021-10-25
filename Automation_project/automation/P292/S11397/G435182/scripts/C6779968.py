'''
Created on Sept 26 , 2018

@author: Varun
Test Case ID : http://172.19.2.180/testrail/index.php?/cases/view/6779968 
Test Case Name : Verify Matrix chart workflow, preview & run
'''
import unittest
from common.lib import utillity,base
from common.lib.basetestcase import BaseTestCase
from common.pages import ia_ribbon, metadata, visualization_resultarea
from common.wftools import visualization,chart

class C6779968_TestClass(BaseTestCase):

    def test_C6779968(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C6779968"
        visual_obj = visualization.Visualization(self.driver)
        chart_obj = chart.Chart(self.driver)
        base_obj = base.BasePage(self.driver)
        metadata_obj=metadata.MetaData(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        resultobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        x_axis_css = "svg g text[class*='xaxisNumeric-labels']"
        y_axis_css= "svg g text[class*='yaxis-labels']"
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        expected_header_1="Sale Year/Quarter"
        
        """
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%P292_S11397%2FG435181&tool=chart&master=baseapp/wf_retail_lite
        """
        chart_obj.invoke_chart_tool_using_api('baseapp/wf_retail_lite')
                     
        """ 
            Step 02:Select Format > Scatter (from Chart Types group).
        """ 
        visual_obj.select_ribbon_item("Format","Scatter")
        chart_obj.wait_for_number_of_element(y_axis_css, 7, base_obj.chart_short_timesleep)
        
        """ 
            Step 03:Double click Gross Profit (to add to Vertical Axis bucket).
        """ 
        chart_obj.double_click_on_datetree_item("Sales->Gross Profit", 1)
        chart_obj.wait_for_number_of_element(y_axis_css,8,base_obj.chart_short_timesleep)

        """ 
            Step 04:Drag Discount to Horizontal Axis bucket.
        """ 
        visual_obj.drag_field_from_data_tree_to_query_pane("Discount", 1, "Horizontal Axis")
        visual_obj.wait_for_number_of_element(x_axis_css, 7, base_obj.chart_medium_timesleep)
        visual_obj.wait_for_visible_text("#TableChart_1 [class='xaxisNumeric-title']", "Discount", base_obj.chart_short_timesleep)

        """ 
            Step 05:Double click Model (to add to Detail bucket).
        """ 
        chart_obj.double_click_on_datetree_item("Dimensions->Product->Product->Model",1)
        chart_obj.wait_for_number_of_element("#TableChart_1 [class*='riser']", 157, base_obj.chart_long_timesleep)
            
        """ 
            Step 06:Drag Product,Category to Color bucket.
        """ 
        visual_obj.drag_field_from_data_tree_to_query_pane("Product,Category", 1, "Color")
        color_product_css = "#queryTreeColumn tbody tr:nth-child(15) td"
        chart_obj.wait_for_visible_text(color_product_css, 'Product,Category', base_obj.chart_short_timesleep)
        chart_obj.verify_field_listed_under_querytree('Color BY', 'Product,Category', 1, "Step 06::01: Verify Product Category is visible underneath Color bucket")
           
        """ 
            Step 07:Drag Quantity,Sold to Size bucket.
        """
        visual_obj.drag_field_from_data_tree_to_query_pane("Quantity,Sold", 1, "Size")
        color_product_css = "#queryTreeColumn tbody tr:nth-child(12) td"
        chart_obj.wait_for_visible_text(color_product_css, 'Quantity,Sold',base_obj.chart_short_timesleep)
        chart_obj.verify_field_listed_under_querytree('Size', 'Quantity,Sold', 1, "Step 07::01: Verify Quantity Sold is visible underneath Size bucket")
            
        """   
            Step 08:Drag Store,Business,Region to Matrix > Columns bucket
        """  
        
        metadata_obj.collapse_data_field_section("Measure Groups")  
        metadata_obj.expand_data_field_section("Store->Store", 1)
        visual_obj.drag_field_from_data_tree_to_query_pane("Store,Business,Region", 1, "Columns")
        chart_obj.wait_for_number_of_element(x_axis_css, 20, base_obj.chart_short_timesleep)
        chart_obj.verify_field_listed_under_querytree('Columns', "Store,Business,Region", 1, "Step 08::01: Verify Store, Business, Region is added underneath Columns bucket")
           
        """ 
            Step 09:Drag Store,Business,Region to filter pane>Get Values>All>Select EMEA & North America>Move to right pane of filter>OK>OK
        """ 
        visual_obj.drag_and_drop_from_data_tree_to_filter("Store,Business,Region", 1)
#         visual_obj.
        ia_ribbonobj.create_constant_filter_condition('All',['EMEA', 'North America'])
        
        """
            Verify the created scatter chart in the preview
        """

        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 09:01") 
        visual_obj.verify_x_axis_title(["Discount"], "#TableChart_1", msg="Step 09:02:Verify xaxis title")
        visual_obj.verify_y_axis_title(["Gross Profit"], "#TableChart_1", msg="Step 09:03:Verify yaxis title")
        expected_xval_list=['0', '112.5K', '225K', '337.5K', '','0', '112.5K', '225K', '337.5K']
        expected_yval_list=['0', '0.9M', '1.8M', '2.6M']
        visual_obj.verify_x_axis_label(expected_xval_list, '#TableChart_1', xyz_axis_label_css=x_axis_css,msg= 'Step 09:04: Verify X labels')
        visual_obj.verify_y_axis_label(expected_yval_list, '#TableChart_1', msg='Step 09:05: Verify Y axis labels')
        visual_obj.verify_chart_color_using_get_css_property("circle[class='riser!s4!g12!mmarker!r0!c1!']", "brick_red", "#TableChart_1",  msg="Step 09:06: Verify the scatter color")
        
        """ 
            Step 10:Click Run.
        """ 
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_frame()
        utillobj.synchronize_with_visble_text("jschart_HOLD_0 [class='yaxis-title']", "Gross Profit", 30)
             
        """ 
            Step 11:Verify chart displays just EMEA and North America.
        """ 
        resultobj.verify_visualization_row_column_header_labels("jschart_HOLD_0",'columns',expected_header,expected_label,"Step 11:01") 
        visual_obj.verify_x_axis_title(["Discount"], "#jschart_HOLD_0", msg="Step 11:02:Verify xaxis title")
        visual_obj.verify_y_axis_title(["Gross Profit"], "#jschart_HOLD_0", msg="Step 11:03:Verify yaxis title")
        expected_xval_list=['0', '112.5K', '225K', '337.5K', '','0', '112.5K', '225K', '337.5K']
        expected_yval_list=['0', '0.9M', '1.8M', '2.6M']
        visual_obj.verify_x_axis_label(expected_xval_list, '#jschart_HOLD_0', xyz_axis_label_css=x_axis_css,msg= 'Step 11:04: Verify X labels')
        visual_obj.verify_y_axis_label(expected_yval_list, '#jschart_HOLD_0', msg='Step 11:05: Verify X and Y axis labels')
        visual_obj.verify_chart_color_using_get_css_property("circle[class='riser!s4!g12!mmarker!r0!c1!']", "brick_red", "#jschart_HOLD_0",  msg="Step 11:06: Verify the scatter color")
        visual_obj.switch_to_default_content()
            
        """ 
            Step 12:Click Save in the toolbar > Save as "C6779968" > Click Save.
        """ 
        visual_obj.save_visualization_from_top_toolbar(Test_Case_ID)

        """   
            Step 13:Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual_obj.logout_visualization_using_api()
             
        """ 
            Step 14:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2FC6779968.fex
        """ 
        chart_obj.invoke_chart_in_edit_mode_using_api(Test_Case_ID)
             
        """ 
            Step 15:Drag "Transaction Date,Component" > "Sale,Year/Quarter" to Matrix Rows bucket
        """ 
        metadata_obj.expand_data_field_section("Sales_Related->Transaction Date, Components", 1)
        visual_obj.drag_field_from_data_tree_to_query_pane("Sale,Year/Quarter", 1, "Rows")
        visual_obj.wait_for_number_of_element(y_axis_css, 10, base_obj.chart_short_timesleep)
        chart_obj.verify_field_listed_under_querytree('Rows', 'Sale,Year/Quarter', 1, "Step 15::01: Verify Sale,Year/Quarter is added underneath Rows bucket")
        
        """ 
            Verify preview chart
        """
        row_header=util_obj.validate_and_get_webdriver_object("#TableChart_1 [class^='rowHeader']", "Title" ).text.strip()
        util_obj.asequal(row_header,expected_header_1, "Step 15:01:Verify row header value")
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 15:02")
        visual_obj.verify_number_of_circles("#TableChart_1", 1, 501, 'Step 15:03: Verify number of Circle displayed')
        visual_obj.verify_x_axis_title(["Discount"], "#TableChart_1", msg="Step 15:04:Verify xaxis title")
        visual_obj.verify_y_axis_title(["Gross Profit"], "#TableChart_1", msg="Step 15:05:Verify yaxis title") 
        expected_xval_list=['0', '1,750', '3,500', '5,250', '','0', '1,750', '3,500', '5,250']
        expected_yval_list=['0', '15K', '30K', '45K']
        visual_obj.verify_x_axis_label(expected_xval_list, '#TableChart_1', xyz_axis_label_css=x_axis_css,msg= 'Step 15:06: Verify X labels')
        visual_obj.verify_y_axis_label(expected_yval_list, '#TableChart_1', msg='Step 15:07: Verify X and Y axis labels')
        visual_obj.verify_chart_color_using_get_css_property("circle[class='riser!s4!g12!mmarker!r0!c1!']", "brick_red", "#TableChart_1",  msg="Step 15:08: Verify the scatter color")
        
        """
            Step 16 :Select Home ribbon, type 150 in the Records inbox (do not use a value from the dropdown) > click ENTER.
        """
        ia_ribbonobj.set_record_limit_homepage(150)
        visual_obj.wait_for_number_of_element("#TableChart_1 [class^='riser']", 150, base_obj.chart_short_timesleep )
             
        """ 
            Step 17:Right click Sale,Year/Quarter>Sort>Descending.
        """ 
        visual_obj.right_click_on_field_under_query_tree("Sale,Year/Quarter", 1, "Sort->Sort->Descending")
        visual_obj.wait_for_number_of_element("#TableChart_1 circle[class^='riser']", 150, base_obj.chart_short_timesleep)
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 17:01")
        row_header=util_obj.validate_and_get_webdriver_object("#TableChart_1 [class^='rowHeader']", "Title" ).text.strip()
        util_obj.asequal(row_header,expected_header_1, "Step 17:02:Verify row header value")
        visual_obj.verify_number_of_circles("#TableChart_1", 1, 501, 'Step 17:03: Verify number of Circle displayed')
        visual_obj.verify_x_axis_title(["Discount"], "#TableChart_1", msg="Step 17:04:Verify xaxis title")
        visual_obj.verify_y_axis_title(["Gross Profit"], "#TableChart_1", msg="Step 17:05:Verify yaxis title") 
        expected_xval_list=['0', '17.5K', '35K', '52.5K', '','0', '17.5K', '35K', '52.5K']
        expected_yval_list=['0', '112.5K', '225K', '337.5K']
        visual_obj.verify_x_axis_label(expected_xval_list, '#TableChart_1', xyz_axis_label_css=x_axis_css,msg= 'Step 17:06: Verify X labels')
        visual_obj.verify_y_axis_label(expected_yval_list, '#TableChart_1', msg='Step 17:07: Verify X and Y axis labels')
        visual_obj.verify_chart_color_using_get_css_property("circle[class='riser!s4!g10!mmarker!r0!c0!']", "brick_red", "#TableChart_1",  msg="Step 17:08: Verify the scatter color")
        
        """ 
            Step 18:Click Run.
        """ 
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_frame()
        visual_obj.wait_for_number_of_element("jschart_HOLD_0 [class='yaxis-title']", "Gross Profit", base_obj.chart_medium_timesleep)
             
        """ 
            Step 19:Verify the following chart displays.
        """
        resultobj.verify_visualization_row_column_header_labels('jschart_HOLD_0','columns',expected_header,expected_label,"Step 19:01")
        row_header=util_obj.validate_and_get_webdriver_object("#jschart_HOLD_0 [class^='rowHeader']", "Title" ).text.strip()
        util_obj.asequal(row_header,expected_header_1, "Step 19:01:Verify row header value")
        visual_obj.verify_number_of_circles("#jschart_HOLD_0", 1, 5144, 'Step 19:03: Verify number of Circle displayed')
        visual_obj.verify_x_axis_title(["Discount"], "#jschart_HOLD_0", msg="Step 19:04:Verify xaxis title")
        visual_obj.verify_y_axis_title(["Gross Profit"], "#jschart_HOLD_0", msg="Step 19:05:Verify yaxis title") 
        expected_xval_list=['0', '17.5K', '35K', '52.5K', '','0', '17.5K', '35K', '52.5K']
        expected_yval_list=['0', '125K', '250K', '375K']
        visual_obj.verify_x_axis_label(expected_xval_list, '#jschart_HOLD_0', xyz_axis_label_css=x_axis_css,msg= 'Step 19:06: Verify X labels')
        visual_obj.verify_y_axis_label(expected_yval_list, '#jschart_HOLD_0', msg='Step 09:05: Verify X and Y axis labels')
        visual_obj.verify_chart_color_using_get_css_property("circle[class='riser!s4!g12!mmarker!r0!c1!']", "brick_red", "#jschart_HOLD_0",  msg="Step 19:07: Verify the scatter color")
        visual_obj.switch_to_default_content()
            
        """   
            Step 20:Right click "Model" from Query pane > Delete.
        """ 
        visual_obj.right_click_on_field_under_query_tree("Model", 1, "Delete")
        chart_obj.wait_for_visible_text("#queryTreeColumn tbody tr:nth-child(17) td", 'Product,Category', base_obj.chart_short_timesleep)
        chart_obj.verify_field_availability_in_querytree('Size', 'Model', 'Color BY', "Step 20:01:Verify Model is feld is deleted", availability=False)
        visual_obj.verify_number_of_circles("#TableChart_1", 1, 151, 'Step 20:02: Verify number of Circle displayed')
        expected_header="Store Business Region"
        expected_label=['EMEA', 'North America']
        expected_header_1="Sale Year/Quarter"
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 20:03")
        row_header=util_obj.validate_and_get_webdriver_object("#TableChart_1 [class^='rowHeader']", "Title" ).text.strip()
        util_obj.asequal(row_header,expected_header_1, "Step 15:01:Verify row header value")
        
        """ 
            Step 21:Double click Store > "Store,City" (to add to Detail bucket).
        """ 
        visual_obj.double_click_on_datetree_item("Store->Store->Store,City", 1)
        visual_obj.wait_for_visible_text("#queryTreeColumn table tr:nth-child(16)", "Store,City", base_obj.chart_short_timesleep)
           
        """ 
            Step 22:Double click Query Variables/Store Front (to add to filter pane with Is True).
        """ 
        metadata_obj.collapse_data_field_section("Dimensions")
        visual_obj.double_click_on_datetree_item("Filters and Variables->Store Front", 1)
        visual_obj.wait_for_visible_text("#qbFilterBox table>tbody>tr:nth-child(2) td","Store Front Is true",base_obj.report_long_timesleep)
             
        """ 
            Step 23:Select Home ribbon > Records dropdown > 500.
        """
        ia_ribbonobj.set_record_limit_homepage(500)
        visual_obj.wait_for_number_of_element("#TableChart_1 circle[class^='riser']", 500, base_obj.chart_short_timesleep)
              
        """ 
            Step 24:Verify the following chart displays.
        """
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 24:01")
        row_header=util_obj.validate_and_get_webdriver_object("#TableChart_1 [class^='rowHeader']", "Title" ).text.strip()
        util_obj.asequal(row_header,expected_header_1, "Step 24:02:Verify row header value")
        visual_obj.verify_number_of_circles("#TableChart_1", 1, 501, 'Step 24:03: Verify number of Circle displayed')
        visual_obj.verify_x_axis_title(["Discount"], "#TableChart_1", msg="Step 24:04:Verify xaxis title")
        visual_obj.verify_y_axis_title(["Gross Profit"], "#TableChart_1", msg="Step 24:05:Verify yaxis title") 
        expected_xval_list=['0', '11.3K', '22.5K', '33.8K', '','0', '11.3K', '22.5K', '33.8K']
        expected_yval_list=['0', '70K', '140K', '210K']
        visual_obj.verify_x_axis_label(expected_xval_list, '#TableChart_1', xyz_axis_label_css=x_axis_css,msg= 'Step 24:06: Verify X labels')
        visual_obj.verify_y_axis_label(expected_yval_list, '#TableChart_1', msg='Step 24:07: Verify X and Y axis labels')
        visual_obj.verify_chart_color_using_get_css_property("circle[class='riser!s4!g14!mmarker!r0!c1!']", "brick_red", "#TableChart_1",  msg="Step 24:08: Verify the scatter color")
        
        """ 
            Step 25:Run.
        """ 
        visual_obj.run_visualization_from_toptoolbar()
        visual_obj.switch_to_frame()
            
        """ 
            Step 26:Verify the following chart displays.
        """ 
        resultobj.verify_visualization_row_column_header_labels('jschart_HOLD_0','columns',expected_header,expected_label,"Step 26:01")
        row_header=util_obj.validate_and_get_webdriver_object("#jschart_HOLD_0 [class^='rowHeader']", "Title" ).text.strip()
        util_obj.asequal(row_header,expected_header_1, "Step 26:02:Verify row header value")
        visual_obj.verify_number_of_circles("#jschart_HOLD_0", 1, 6234, 'Step 26:03: Verify number of Circle displayed')
        visual_obj.verify_x_axis_title(["Discount"], "#jschart_HOLD_0", msg="Step 26:04:Verify xaxis title")
        visual_obj.verify_y_axis_title(["Gross Profit"], "#jschart_HOLD_0", msg="Step 26:05:Verify yaxis title") 
        expected_xval_list=['0', '11.3K', '22.5K', '33.8K', '','0', '11.3K', '22.5K', '33.8K']
        expected_yval_list=['0', '70K', '140K', '210K']
        visual_obj.verify_x_axis_label(expected_xval_list, '#jschart_HOLD_0', xyz_axis_label_css=x_axis_css,msg= 'Step 26:06: Verify X labels')
        visual_obj.verify_y_axis_label(expected_yval_list, '#jschart_HOLD_0', msg='Step 26:07: Verify Y axis labels')
        visual_obj.verify_chart_color_using_get_css_property("circle[class='riser!s4!g12!mmarker!r0!c1!']", "brick_red", "#jschart_HOLD_0",  msg="Step 26:08: Verify the scatter color")
        visual_obj.switch_to_default_content()
            
        """ 
            Step 27:Click Save > click Ok.
        """ 
        visual_obj.select_item_in_top_toolbar('save')
             
        """ 
            Step 28:Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """ 
        visual_obj.logout_visualization_using_api()
             
        """ 
            Step 29:Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2FC6779968.fex
        """
        chart_obj.invoke_chart_in_edit_mode_using_api(Test_Case_ID)
        
        """    
            Step 30:Verify chart restores without error.
        """
        resultobj.verify_visualization_row_column_header_labels('TableChart_1','columns',expected_header,expected_label,"Step 30:01")
        row_header=util_obj.validate_and_get_webdriver_object("#TableChart_1[class^='rowHeader']", "Title" ).text.strip()
        util_obj.asequal(row_header,expected_header_1, "Step 30:02:Verify row header value")
        visual_obj.verify_number_of_circles("#TableChart_1", 1, 501, 'Step 30:03: Verify number of Circle displayed')
        visual_obj.verify_x_axis_title(["Discount"], "#TableChart_1", msg="Step 30:04:Verify xaxis title")
        visual_obj.verify_y_axis_title(["Gross Profit"], "#TableChart_1", msg="Step 30:05:Verify yaxis title") 
        expected_xval_list=['0', '11.3K', '22.5K', '33.8K', '','0', '11.3K', '22.5K', '33.8K']
        expected_yval_list=['0', '70K', '140K', '210K']
        visual_obj.verify_x_axis_label(expected_xval_list, '#TableChart_1', xyz_axis_label_css=x_axis_css,msg= 'Step 30:06: Verify X labels')
        visual_obj.verify_y_axis_label(expected_yval_list, '#TableChart_1', msg='Step 30:07: Verify X and Y axis labels')
        visual_obj.verify_chart_color_using_get_css_property("circle[class='riser!s4!g14!mmarker!r0!c1!']", "brick_red", "#TableChart_1",  msg="Step 30:08: Verify the scatter color")
            
        """ 
            Step 31:Launch the IA API to logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()