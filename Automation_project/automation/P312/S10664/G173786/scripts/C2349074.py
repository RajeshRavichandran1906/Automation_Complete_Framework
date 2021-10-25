'''
Created on Jan 11, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349074
Test_Case Name : Undo/Redo group
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity


class C2349074_TestClass(BaseTestCase):

    def test_C2349074(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349074'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        def verify_bar_chart(xaxis_title, xaxis_labels, yaxis_labels, total_risers, step_num):
            visul_result.verify_xaxis_title('MAINTABLE_wbody1_f', xaxis_title, 'Step ' + step_num + '.1 : Verify X-Axis title')
            visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Revenue', 'Step ' + step_num + '.2 : Verify Y-Axis title')
            visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', xaxis_labels, yaxis_labels, 'Step ' + step_num + '.3 :')
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, total_risers, 'Step ' + step_num + '.4 : Verify number of bar chart risers')
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mbar!', 'lochmara', 'Step ' + step_num + '.5 : Verify bar chart riser color')
            
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
            
        """
            Step 02 : Double click "Revenue", "Product,Category"
        """    
        metadata.datatree_field_click('Revenue',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-title']", 1, 30, string_value='Revenue')
        
        metadata.datatree_field_click('Product,Category',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 30, string_value='Product,Category')
        
        """
            Step 02.1 : Verify preview
        """
        xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        verify_bar_chart('Product Category', xaxis_labels, yaxis_labels, 7, '02')
        
        """
            Step 03 : Lasso last four risers
        """
        visul_result.create_lasso('MAINTABLE_wbody1_f', 'rect', 'riser!s0!g3!mbar!', target_tag='rect', target_riser='riser!s0!g6!mbar!')
        
        """
            Step 04 : Click "Group Product,Category Selection"
        """
        visul_result.select_or_verify_lasso_filter(verify=['4 points' ,'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection'], select='Group Product,Category Selection',  msg='Step 04.1 : Verify lasso tooltip')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 30, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 05 : Verify preview updated with group field
        """ 
        xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player and Stereo Systems and Televisions and 1 more']
        yaxis_labels=['0', '100M', '200M', '300M', '400M', '500M', '600M', '700M', '800M']  
        verify_bar_chart('PRODUCT_CATEGORY_1', xaxis_labels, yaxis_labels, 4, '05')
#         expected_tooltip=['PRODUCT_CATEGORY_1:Media Player and Stereo Systems and Televisions and 1 more', 'Revenue:$673,802,402.32', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category'] changed 'Revenue:$673,802,402.31'
        expected_tooltip=['PRODUCT_CATEGORY_1:Media Player and Stereo Systems and Televisions and 1 more', 'Revenue:$673,802,402.31', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g3!mbar!', expected_tooltip, 'Step 05.6 : Verify tooltip')
        
        """
            Step 06 : Click Undo icon in tool bar menu
        """
        visul_ribbon.select_top_toolbar_item('toolbar_undo')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 40, string_value='Product Category')
        
        """
            Step 07 : Verify data,query and preview updated
        """
        xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']   
        yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']  
        verify_bar_chart('Product Category', xaxis_labels, yaxis_labels, 7, '07')
        expected_tooltip=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g3!mbar!', expected_tooltip, 'Step 07.6 : Verify tooltip')
        metadata.verify_all_data_panel_fields(['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer'], 'Step 07.7 : Verify data pane update')
        metadata.verify_query_panel_all_field(['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Size', 'Tooltip'], 'Step 07.8 : Verify query pane update')
        
        """
            Step 08 : Lasso first two risers >Click "Group Product,Category Selection"
        """
        visul_result.create_lasso('MAINTABLE_wbody1_f', 'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g1!mbar!')
        visul_result.select_or_verify_lasso_filter(verify=['2 points' ,'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection'], select='Group Product,Category Selection', msg='Step 08.1 : Verify lasso tooltip')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 40, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 09 : Verify preview updated with group field
        """
        xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']   
        yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']  
        verify_bar_chart('PRODUCT_CATEGORY_1', xaxis_labels, yaxis_labels, 6, '09')
        expected_tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g0!mbar!', expected_tooltip, 'Step 07.6 : Verify tooltip')
        metadata.verify_all_data_panel_fields(['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'PRODUCT_CATEGORY_1'], 'Step 09.7 : Verify data pane update')
        metadata.verify_query_panel_all_field(['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'PRODUCT_CATEGORY_1', 'Marker', 'Color', 'Size', 'Tooltip'], 'Step 09.8 : Verify query pane update')
        
        """
            Step 10 : Click Undo icon in tool bar menu
        """
        visul_ribbon.select_top_toolbar_item('toolbar_undo')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 30, string_value='Product Category')
        
        """
            Step 11 : Verify Group is removed from query and data panes, Horizontal Axis contains Product,Category
        """
        xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']   
        yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']  
        verify_bar_chart('Product Category', xaxis_labels, yaxis_labels, 7, '11')
        expected_tooltip=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g3!mbar!', expected_tooltip, 'Step 11.6 : Verify tooltip')
        metadata.verify_all_data_panel_fields(['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer'], 'Step 11.7 : Verify Group is removed from data panes')
        metadata.verify_query_panel_all_field(['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Size', 'Tooltip'], 'Step 11.8 : Verify Group is removed from query')
        
        """
            Step 12 : Verify fex does not have following group define
        """
        expected_syntax_list=["PRODUCT_CATEGORY_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ( 'Accessories' 'Accessories and Camcorder' 'Camcorder' 'Accessories and Camcorder' ELSE 'Default');", "PRODUCT_CATEGORY_1 = IF PRODUCT_CATEGORY_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ELSE PRODUCT_CATEGORY_1;"]
        iaresult.verify_syntax_not_in_fexcode(expected_syntax_list, 'Step 12.1 : Verify fex does not have following group define')
        
        """
            Step 13 : Click Redo in tool bar menu
        """
        visul_ribbon.select_top_toolbar_item('toolbar_redo')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 40, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 14 : Verify Group shows in query and data panes, preview shows one riser for "Accessories and Camcorder group value
        """
        xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']   
        yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']  
        verify_bar_chart('PRODUCT_CATEGORY_1', xaxis_labels, yaxis_labels, 6, '14')
        expected_tooltip=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Revenue:$284,074,040.77', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g0!mbar!', expected_tooltip, 'Step 14.6 : Verify tooltip')
        metadata.verify_all_data_panel_fields(['Query Variables', 'Measures', 'Sales', 'Shipments', 'Dimensions', 'Sales_Related', 'Product', 'Shipments_Related', 'Store', 'Customer', 'PRODUCT_CATEGORY_1'], 'Step 14.7 : Verify data pane update')
        metadata.verify_query_panel_all_field(['Bar Stacked1', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Revenue', 'Horizontal Axis', 'PRODUCT_CATEGORY_1', 'Marker', 'Color', 'Size', 'Tooltip'], 'Step 14.8 : Verify query pane update')
        element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(element, Test_Case_ID+'_Actual_Step_14')
        
        """
            Step 15 : Click Save in the toolbar > Save as "C2349074" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 16 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()