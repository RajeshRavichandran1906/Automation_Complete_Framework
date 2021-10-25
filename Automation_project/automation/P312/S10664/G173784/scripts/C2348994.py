'''
Created on Jan 02, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2050428
Test_Case Name : Paperclipping in Line Chart
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2348994_TestClass(BaseTestCase):

    def test_C2348994(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2348994'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        def verify_line_chart_output(step_no):
            visul_result.verify_xaxis_title('MAINTABLE_wbody1_f', 'Sale Year', 'Step '+step_no+'.1 : Verify X-Axis title')
            visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Revenue', 'Step '+step_no+'.2 : Verify Y-Axis title')
            visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', ['2011', '2012', '2013', '2014', '2015', '2016'], ['0', '100M', '200M', '300M', '400M', '500M'], 'Step '+step_no+'.3 :')
            visul_result.verify_riser_legends('MAINTABLE_wbody1_f', ['PRODUCT_CATEGORY_1', 'Accessories and Camcorder and Computers and 4 more'], 'Step '+step_no+'.4 : Verify legend labels')
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 1, 'Step '+step_no+'.5 : Verify number of risers', custome_css=" svg g.risers >g>path[class^='riser']")
            visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 6, 'Step '+step_no+'.6 : Verify number of marker', custome_css="  svg circle[class^='marker']")
            utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s0!g0!mline!', 'bar_blue', 'Step '+step_no+'.7 : Verify line chart riser color',attribute_type='stroke')
             
        """
            1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#pfjTableChart_1 svg text", 1, 120, string_value='DropMeasuresorSortsintotheQueryPane', with_regular_exprestion=True)
        time.sleep(3)
        
        """
            Step 02 : Double click "Revenue", "Sale,Year" to add fields
        """
        metadata.datatree_field_click('Revenue',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='yaxis-title']", 1, 80, string_value='Revenue')
        
        metadata.datatree_field_click('Sale,Year',2,1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 1, 80, string_value='Sale Year')
        time.sleep(2)
        
        """
            Step 03 : Click Change drop down > Line chart
        """
        visul_ribbon.change_chart_type('line')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg path[class^='riser']", 1, 80)
        
        """
            Step 04 : Drag and drop "Product,Category" to Color bucket
        """
        metadata.drag_drop_data_tree_items_to_query_tree('Product,Category', 1, 'Color', 0)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 80, string_value='Product Category')
        time.sleep(3)
        
        """
            Step 05 : Verify following preview displayed
        """
        visul_result.verify_xaxis_title('MAINTABLE_wbody1_f', 'Sale Year', 'Step 05.1 : Verify X-Axis title')
        visul_result.verify_yaxis_title('MAINTABLE_wbody1_f', 'Revenue', 'Step 05.2 : Verify Y-Axis title')
        visul_result.verify_riser_chart_XY_labels('MAINTABLE_wbody1_f', ['2011', '2012', '2013', '2014', '2015', '2016'], ['0', '30M', '60M', '90M', '120M', '150M'], 'Step 05.3 :')
        visul_result.verify_riser_legends('MAINTABLE_wbody1_f', ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], 'Step 05.4 : Verify legend labels')
        visul_result.verify_number_of_riser('MAINTABLE_wbody1_f', 1, 7, 'Step 05.5 : Verify number of risers', custome_css=" svg g.risers >g>path[class^='riser']")
        utillobj.verify_chart_color('MAINTABLE_wbody1_f', 'riser!s6!g0!mline!', 'periwinkle_gray', 'Step 05.6 : Verify line chart riser color',attribute_type='stroke')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_05', 'actual')
        
        """
            Step 06 : Select data points of 2015 and 2016 in lines
            Step 07 : Click "Group Product,Category selection"
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f path[class='riser!s4!g0!mline!']")
        source_cord=utillobj.get_object_screen_coordinate(source_element, 'top_right', x_offset=25, y_offset=-10)
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g4!mgroupLabel!']")
        target_cord=utillobj.get_object_screen_coordinate(target_element, 'left', x_offset=-40, y_offset=-40)
        utillobj.drag_drop_on_screen(sx_offset=source_cord['x'],sy_offset=source_cord['y'],tx_offset=target_cord['x'],ty_offset=target_cord['y'])
        visul_result.select_or_verify_lasso_filter(verify=['14 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection'], msg='Step 06.1 : Verify lasso values', select='Group Product,Category Selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        time.sleep(3)
        
        """
            Step 08 : Verify the preview
        """
        verify_line_chart_output('08')
        screenshot_element=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_element, Test_Case_ID+'_Actual_Step_08', 'actual')
        
        """
            Step 09 : Hover on line and verify tool tip values
        """
        marker_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f svg circle[class='marker!s0!g3!mmarker!']")
        utillobj.click_on_screen(marker_element, 'middle',javascript_marker_enable=True,mouse_duration=2.5, pause=2)
        expected_tooltip=['Sale Year:2014', 'Revenue:$126,675,660.19', 'PRODUCT_CATEGORY_1:Accessories and Camcorder and Computers and 4 more', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1', None,expected_tooltip, msg="Step 09.1 : Verify tool tip values",default_move=True)     
        
        """
            Step 10 : Click Save in the toolbar > Save as "C2348994" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 11 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 12 : Run fex from Resource tree using API http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2348994.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10664_paperclipping_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 12.1 : Verify chart output
        """
        verify_line_chart_output('12')
        utillobj.take_browser_screenshot(Test_Case_ID+'_Actual_Step_12', 'actual')
        
        """
            Step 13 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 14 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348994.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10664_paperclipping_2',mrid='mrid', mrpass='mrpass')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f text[class='legend-title']", 1, 120, string_value='PRODUCT_CATEGORY_1')
        time.sleep(2)
        
        """
            Step 14.1 : Verify chart in preview
        """
        verify_line_chart_output('14')
        
        """
            Step 15 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()