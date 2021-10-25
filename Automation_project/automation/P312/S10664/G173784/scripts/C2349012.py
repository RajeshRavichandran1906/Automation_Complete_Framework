'''
Created on Jan 04, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349012
Test_Case Name : Paperclipping in Scatter
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import metadata, visualization_metadata, visualization_resultarea, visualization_ribbon, visualization_run, ia_run
from common.lib import utillity

class C2349012_TestClass(BaseTestCase):

    def test_C2349012(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349012'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata_obj = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        visul_run=visualization_run.Visualization_Run(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        
        def verify_scatter_chart(expected_xaxis_lables, expected_xaxis_titles, expected_column_header, expected_column_labels, total_circles, step_num):
            expected_yaxis_lables=['0', '2M', '4M', '6M', '8M', '']
            expected_legends=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
            visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Revenue', 'Step '+ step_num + '.1 : Verify Y-Axis title')
            actaul_xaxis_titles=[title.text.strip() for title in self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1_f svg text[class='xaxisNumeric-title']")]
            utillobj.asequal(actaul_xaxis_titles, expected_xaxis_titles, 'Step '+ step_num + '.2 : Verify X-Axis titles')
            visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', expected_xaxis_lables, expected_yaxis_lables, 'Step ' + step_num + '.3 :')
            visul_result.verify_riser_legends('MAINTABLE_wbody1_f', expected_legends, 'Step ' + step_num + '.4 : Verify legend labels')
            actaul_column_labels=[collab.text.strip() for collab in self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1_f svg g[class='scrollColLbl-clip'] text[class*='colLabel']")]
            utillobj.asequal(actaul_column_labels, expected_column_labels, 'Step '+ step_num + '.5 : Verify column labels')
            actaul_column_header=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg g[class='gVertTitle'] text[class='colHeader-label!']").text.strip()
            utillobj.asequal(actaul_column_header, expected_column_header, 'Step '+ step_num + '.6 : Verify column header title')
            visul_result.verify_number_of_circle('MAINTABLE_wbody1_f', 400, total_circles+1, 'Step ' + step_num + '.7 : Verify number of circles in chart')
            
        """
            1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
        
        """
            Step 02 : Click Change drop down > Scatter chart
        """
        visul_ribbon.change_chart_type('scatter')
        visul_result.wait_for_property("#pfjTableChart_1 svg [class^='riser']", 17, 80)
        
        """
            Step 03 : Double click "Revenue", "Model"
        """
        metadata_obj.datatree_field_click('Revenue',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-title']", 1, 80, string_value='Revenue')
        
        metadata_obj.datatree_field_click('Model',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-labels!m4!']", 1, 80, string_value='16M')
        
        """
            Step 04 : Drag and drop "Cost of Goods" to Horizontal axis,
        """
        metadata_obj.drag_drop_data_tree_items_to_query_tree('Cost of Goods', 1, 'Horizontal Axis', 0)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisNumeric-title']", 1, 80, string_value='Cost of Goods')
        
        """
            Step 05 : Drag and drop "Product,Category" to Color bucket and "Store,Business,Region" to Columns bucket
        """
        metadata_obj.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Color', 0)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 80, string_value='Product Category')
        
        metadata_obj.drag_drop_data_tree_items_to_query_tree('Store,Business,Region', 1, 'Columns', 0)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='colHeader-label!']", 1, 80, string_value='Store Business Region')
        time.sleep(3)
        
        """
            Step 06 : Verify following preview displayed
        """
        expected_xaxis_lables=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '']
        verify_scatter_chart(expected_xaxis_lables, ['Cost of Goods', 'Cost of Goods', 'Cost of Goods', 'Cost of Goods'], 'Store Business Region', ['EMEA', 'North America', 'Oceania', 'South America'], 580, '06')
        element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(element, Test_Case_ID+'_Actual_step_06', 'actual')
        
        """
            Step 07 : Lasso values from Oceania and South America
            Step 08 : Select "Group Store,Business,Region selection"
        """
        visul_result.create_lasso('MAINTABLE_wbody1_f', 'circle', 'riser!s6!g5!mmarker!r0!c2!', target_tag='text', target_riser='legend-labels!s6!')
        expected_lasso=['266 points', 'Filter Chart', 'Exclude from Chart', 'Group Store,Business,Region Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_lasso, msg='Step 05.1 : Verify lasso values', select='Group Store,Business,Region Selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='colHeader-label!']", 1, 80, string_value='BUSINESS_REGION_1')
        
        """
            Step 09 : Verify data, query and preview updated with group
        """
        metadataobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metadataobj.collapse_data_field_section('Product')
        time.sleep(5)
        metadataobj.collapse_data_field_section('Store')
        time.sleep(5)
        expected_xaxis_lables=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '', '0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '']
        verify_scatter_chart(expected_xaxis_lables, ['Cost of Goods', 'Cost of Goods', 'Cost of Goods'], 'BUSINESS_REGION_1', ['EMEA', 'North America', 'Oceania and South America'], 468, '09')
        expected_query_pane=['Scatter1', 'Matrix', 'Rows', 'Columns', 'BUSINESS_REGION_1', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Cost of Goods', 'Marker', 'Size', 'Detail', 'Model', 'Color BY', 'Product,Category', 'Tooltip']
        expected_data_pane=['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'BUSINESS_REGION_1']
        metadata_obj.verify_all_data_panel_fields(expected_data_pane, 'Step 09.8 : Verify data panel')
        metadata_obj.verify_query_panel_all_field(expected_query_pane, 'Step 09.9 : Verify query panel')
        element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(element, Test_Case_ID+'_Actual_step_09', 'actual')
        
        """
            Step 10 : Click Run
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='colHeader-label!']", 1, 120, string_value='BUSINESS_REGION_1')
        
        """
            Step 10.1 : Verify output
        """
        verify_scatter_chart(expected_xaxis_lables, ['Cost of Goods', 'Cost of Goods', 'Cost of Goods'], 'BUSINESS_REGION_1', ['EMEA', 'North America', 'Oceania and South America'], 468, '10')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_10', 'actual')
        
        """
            Step 11 : Hover on group values and verify tool tip values
        """
        expected_tooltip=['BUSINESS_REGION_1:North America', 'Cost of Goods:$6,565,020.00', 'Revenue:$8,527,064.40', 'Product Category:Televisions', 'Model:Sony KDL46HX800', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory', 'Drill down to']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s5!g14!mmarker!r0!c1!', expected_tooltip, 'Step 10.1 : Verify tool tip values')
        
        """
            Step 12 : Click Arrow at right bottom and click grid icon to show data
        """
        visul_run.select_run_menu_option('MAINTABLE_menuContainer1', 'show_report')
        visul_result.wait_for_property("#MAINTABLE_wbody2 table[class='arPivot'] table>tbody>tr:nth-child(1)>td:nth-child(3)>span", 1, 120, string_value='BUSINESS_REGION_1')
        
        """
            Step 12.1 : Verify show data 
        """
        #iarun.create_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table", Test_Case_ID+'_DataSet_Step_12.xlsx', desired_no_of_rows=50)
        iarun.verify_table_data_set("#MAINTABLE_wbody2 table[class='arPivot'] table", Test_Case_ID+'_DataSet_Step_12.xlsx', 'Step 12.1 : Verify show data', desired_no_of_rows=50)
        
        """
            Step 13 : Close run window
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """
            Step 14 : Click Save in the toolbar > Save as "C2349012" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 15 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 16 : Restore saved fex using API : http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349012.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='colHeader-label!']", 1, 120, string_value='BUSINESS_REGION_1')
        
        """
            Step 16.1 : Verify preview
        """
        verify_scatter_chart(expected_xaxis_lables, ['Cost of Goods', 'Cost of Goods', 'Cost of Goods'], 'BUSINESS_REGION_1', ['EMEA', 'North America', 'Oceania and South America'], 468, '16')
        expected_query_pane=['Scatter1', 'Matrix', 'Rows', 'Columns', 'BUSINESS_REGION_1', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Cost of Goods', 'Marker', 'Size', 'Detail', 'Model', 'Color BY', 'Product,Category', 'Tooltip']
        expected_data_pane=['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'BUSINESS_REGION_1']
        metadata_obj.verify_all_data_panel_fields(expected_data_pane, 'Step 16.8 : Verify data panel')
        metadata_obj.verify_query_panel_all_field(expected_query_pane, 'Step 16.9 : Verify query panel')
        
        """
            Step 17 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()