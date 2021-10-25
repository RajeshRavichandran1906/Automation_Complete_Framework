'''
Created on Jan 09, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349042
Test_Case Name : Paperclipping in Heatmap
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2349042_TestClass(BaseTestCase):

    def test_C2349042(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349042'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        def verify_heatmap_chart(expected_xaxis_titles, expected_xaxis_labels, expected_legends, total_risers, riser_css, step_num):
            
            actaul_xaxis_titles=[title.text.strip() for title in self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1_f svg text[class='xaxisOrdinal-title']")]
            utillobj.asequal(expected_xaxis_titles, actaul_xaxis_titles, 'Step ' + step_num + '.1 : Verify X-Axis titles')
            visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', expected_xaxis_labels, [], 'Step ' + step_num + '.2 :', z_expected_labels=['EMEA', 'North America', 'Oceania', 'South America'])
            visul_result.verify_riser_legends('MAINTABLE_wbody1_f', expected_legends, 'Step ' + step_num + '.3 : Verify legend labels')
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, total_risers, 'Step ' + step_num + '.4 : Verify number of risers', custome_css=" svg g>rect[class^='riser']")
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', riser_css, 'cinnabar', 'Step ' + step_num + '.5 : Verify bar chart riser color')
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 2, 'Step ' + step_num + '.6 : Verify number of legend risers', custome_css=" svg g.legend rect")
             
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
         
        """
            Step 02 : Click Change drop down > Heatmap chart
        """ 
        visul_ribbon.change_chart_type('heatmap')
        visul_result.wait_for_property("#pfjTableChart_1 svg text[class='xaxisOrdinal-labels!g3!mgroupLabel!']", 1, 80, string_value='Dddd')
         
        """
            Step 03 : Double click "Store,Business,Region", "Gross Profit"
        """
        metadata.datatree_field_click('Store,Business,Region',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Store Business Region')
        
        metadata.datatree_field_click('Gross Profit',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='colorScaleLegend-title']", 1, 80, string_value='Gross Profit')
        
        """
            Step 04 : Drag and drop "Product,Category" to Horizontal axis
        """
        metadata.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Horizontal Axis', 0)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g0!mgroupLabel!']", 1, 80, string_value='Accessories')
        
        """
            Step 05 : Verify following preview displayed
        """
        expected_xaxis_titles=['Product Category', 'Store Business Region']
        expected_axis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_legend_labels=['Gross Profit', '0M', '12.3M', '24.6M', '37M', '49.2M']
        verify_heatmap_chart(expected_xaxis_titles, expected_axis_labels, expected_legend_labels, 28, 'riser!s3!g4!mbar!', '05')
        
        """
            Step 06 : Select several cells across several columns
            Step 07 : Click "Group Product,Category selection"
        """
        visul_result.create_lasso('MAINTABLE_wbody1_f', 'rect', 'riser!s0!g1!mbar!', target_tag='rect', target_riser='riser!s2!g3!mbar!')
        expected_lasso=['9 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_lasso, msg='Step 06.1 : Verify lasso values', select='Group Product,Category Selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg g.legend text[class='colorScale-labels!m1!']", 1, 80, string_value='20M')
        
        """
            Step 08 : Verify following preview displayed
            Group "PRODUCT_CATEGORY_1" is created in Horizontal Axis , the columns selected are combined to one column.
        """
        expected_xaxis_titles=['PRODUCT_CATEGORY_1', 'Store Business Region']
        expected_axis_labels=['Accessories', 'Camcorder and Computers and Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_legend_labels=['Gross Profit', '0M', '20M', '40.1M', '60.2M', '80.2M']
        verify_heatmap_chart(expected_xaxis_titles, expected_axis_labels, expected_legend_labels, 20, 'riser!s3!g1!mbar!', '08')
        
        """
            Step 09 : Hover on grouped riser and verify tooltip values
        """
        expected_tooltip=['Gross Profit:$80,226,013.73', 'Store Business Region:North America', 'PRODUCT_CATEGORY_1:Camcorder and Computers and Media Player', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s1!g1!mbar!', expected_tooltip, 'Step 09.1 : Verify tool tip values')
        
        """
            Step 10 : Click run
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg g.legend text[class='colorScale-labels!m1!']", 1, 80, string_value='20M')
        
        """
            Step 10.1. : Verify run window
        """
        verify_heatmap_chart(expected_xaxis_titles, expected_axis_labels, expected_legend_labels, 20, 'riser!s3!g1!mbar!', '10')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_10', 'actual')
        
        """
            Step 11 : Hover on "North America - Televisions" and verify tool tip val
        """
        expected_tooltip=['Gross Profit:$9,358,461.12', 'Store Business Region:North America', 'PRODUCT_CATEGORY_1:Televisions', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s1!g3!mbar!', expected_tooltip, 'Step 11.1 : Verify tool tip values')
        
        """
            Step 12 : Close run window
        """
        self.driver.close()
        utillobj.switch_to_window(0)
        
        """
            Step 13 : Click Save in the toolbar > Save as "C2349042" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 14 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 15 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349042.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg g.legend text[class='colorScale-labels!m1!']", 1, 120, string_value='20M')
        time.sleep(3)
        
        """
            Step 15.1 : Verify preview and query pane
        """
        verify_heatmap_chart(expected_xaxis_titles, expected_axis_labels, expected_legend_labels, 20, 'riser!s3!g1!mbar!', '15')
        expected_query_pane=['Heatmap1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Store,Business,Region', 'Horizontal Axis', 'PRODUCT_CATEGORY_1', 'Marker', 'Color', 'Gross Profit']
        expected_data_pane=['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'PRODUCT_CATEGORY_1']
        metadata.verify_query_panel_all_field(expected_query_pane, 'Step 15.7 : Verify query panel')
        metadata.verify_all_data_panel_fields(expected_data_pane, 'Step 15.8 : Verify data panel')
        
        """
            Step 16 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    
    unittest.main()