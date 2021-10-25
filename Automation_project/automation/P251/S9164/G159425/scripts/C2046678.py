'''
Created on Jul 2, 2019

@author: Aftab
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2046678
TestCase Name : Verify creating Bar chart
'''

import unittest
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.pages.core_metadata import CoreMetaData

class C2046678_TestClass(BaseTestCase):

    def test_C2046678(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj= Chart(self.driver)
        utils_obj = utillity.UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        coremeta_obj = CoreMetaData(self.driver)
        
        """
            TESTCASE CSS
        """
        querypane_css = "#queryBoxColumn"
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
                        
        '''        
        Step 1 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159425&tool=chart&master=baseapp/wf_retail_lite
        '''
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
         
        '''
        Step 2 : Verify buckets in Query pane are displayed correctly
        '''
        expected_fields=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Horizontal Axis', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        chart_obj.verify_all_fields_in_query_pane(expected_fields, "step 2: Verify buckets in Query pane")
        
        '''
        Step 3 : Double click "Cost of Goods", "Product,Category"
        '''
        chart_obj.double_click_on_datetree_item('Cost of Goods', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Cost of Goods")
        chart_obj.double_click_on_datetree_item('Product,Category', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Product,Category")
         
        '''
        Step 4 : Drag "Revenue" to "Color" bucket
        '''
        chart_obj.drag_field_from_data_tree_to_query_pane('Revenue', 1, 'Color')
        chart_obj.wait_for_visible_text(querypane_css,"Revenue") 
         
        '''
        5 : Verify the chart is displayed correctly
        '''
        chart_obj.verify_x_axis_title_in_preview(["Product Category"],'#pfjTableChart_1', msg="step 5.01")
        chart_obj.verify_y_axis_title_in_preview(["Cost of Goods"], '#pfjTableChart_1',msg="step 5.02")
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 1, 7, msg="step 5.03")
        expected_listx = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_preview(expected_listx,'#pfjTableChart_1', msg="step 5.04")
        expected_listy = ['0', '40M', '80M', '120M','160M','200M','240M']
        chart_obj.verify_y_axis_label_in_preview(expected_listy,'#pfjTableChart_1', msg="step 5.05")
        chart_obj.verify_data_labels('pfjTableChart_1',['Revenue', '58M', '116.4M', '174.7M', '233M', '291.3M'],msg="step 5.06: Verify data label",custom_css=' text[class*="colorScale"]')
             
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g4!mbar!']", "elf_green",'#pfjTableChart_1', msg="step 5.07: ")
        
        '''
        Step 6 : Drag "Sale,Year" to "Matrix" > "Rows" bucket
        '''
        chart_obj.drag_field_from_data_tree_to_query_pane('Sale,Year', 1, 'Rows')
        chart_obj.wait_for_visible_text(querypane_css,'Sale,Year')
        
        '''
        Step 7 : Verify the chart preview is displayed correctly
        '''
        chart_obj.verify_x_axis_title_in_preview(["Product Category"],'#pfjTableChart_1', msg="step 7.01")
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 1, 42, msg="step 7.02")
        expected_listx1 = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_preview(expected_listx1,'#pfjTableChart_1', msg="step 7.03")
        expected_listy1 = ['0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M']
        chart_obj.verify_y_axis_label_in_preview(expected_listy1,'#pfjTableChart_1', msg="step 7.04")
        chart_obj.verify_data_labels('pfjTableChart_1',['Revenue', '1.4M', '30.7M', '60M', '89.3M', '118.6M'],msg="step 7.05: Verify data labels",custom_css=' text[class*="colorScale"]')
        
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g4!mbar!r5!c0!']", "elf_green",'#pfjTableChart_1', msg="step 7.05: ")
        
        '''
        Step 8 : Drag "Store Type" to "Matrix" > "Columns"
        '''
        coremeta_obj.collapse_data_field_section('Filters and Variables')
        chart_obj.drag_field_from_data_tree_to_query_pane('Store->Store->Store Name->Attributes->Store Type', 1, 'Columns') 
        chart_obj.wait_for_visible_text(querypane_css,'Store Type')
         
        '''
        Step 9 : Verify the chart preview is displayed correctly
        '''
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 1, 77, msg="step 9.01")
        expected_listx2 =['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...']
        chart_obj.verify_x_axis_label_in_preview(expected_listx2,'#pfjTableChart_1', msg="step 9.02")
        expected_listy2 = ['0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M']
        chart_obj.verify_y_axis_label_in_preview(expected_listy2,'#pfjTableChart_1', msg="step 9.03")
        chart_obj.verify_data_labels('pfjTableChart_1',['Revenue', '0.2M', '18M', '35.9M', '53.7M', '71.5M'],msg="step 9.04 : Verify data labels",custom_css=' text[class*="colorScale"]')
        
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g4!mbar!r5!c0!']", "elf_green",'#pfjTableChart_1', msg="step 9.04: ")
        
        ''' 
        Step 10 : Hold "Ctrl" and select "Gross Profit","Revenue", "Quantity,Sold"
        Step 11 : Drag these values into "Tooltip" bucket
        '''       
        chart_obj.drag_multiple_data_fields_to_query_tree(['Gross Profit', 'Revenue', 'Quantity,Sold'], 'Tooltip')
        chart_obj.wait_for_visible_text(querypane_css,'Gross Profit')     
         
        '''
        Step 12 : Verify all fields are displayed in the Query pane
        '''
        expected_fields1=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Sale,Year', 'Columns', 'Store Type', 'Axis', 'Vertical Axis', 'Cost of Goods', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Revenue', 'Size', 'Tooltip', 'Gross Profit', 'Revenue', 'Quantity,Sold', 'Multi-graph', 'Animate']
        chart_obj.verify_all_fields_in_query_pane(expected_fields1, "step 12: Verify buckets in Query pane")
        
        '''
        Step 13 : Click "Run"
        '''
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
         
        '''
        Step 14 : Verify the chart output is correctly displayed
        '''
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 77, msg="step 14.01")
        expected_listx4 =['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...']
        chart_obj.verify_x_axis_label_in_run_window(expected_listx4,'#jschart_HOLD_0', msg="step 14.02")
        expected_listy4 = ['0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M']
        chart_obj.verify_y_axis_label_in_run_window(expected_listy4,'#jschart_HOLD_0', msg="step 14.03")
        chart_obj.verify_data_labels('jschart_HOLD_0',['Revenue', '0.2M', '18M', '35.9M', '53.7M', '71.5M'],msg="step 14.04: Verify data label",custom_css=' text[class*="colorScale"]')
           
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g4!mbar!r5!c0!']", "elf_green",'#jschart_HOLD_0', msg="step 14.05")
            
        '''
        Step 15 : Click "IA" > "Save" > "C2046678" > "Save".
        '''
        chart_obj.switch_to_default_content()
        chart_obj.save_as_from_application_menu_item(file_name='C2046678', target_table_path=repository_folder.replace('/', '->'), application_menu_item_name='save')
                 
        '''
        Step 16 : Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        '''
        chart_obj.api_logout()
         
        '''
        Step 17 : Run C2046678.fex .
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP251_S9164%2FG159425&BIP_item=C2046678.fex
        '''
        chart_obj.run_fex_using_api_url(repository_folder,'C2046678', mrid='mrid', mrpass='mrpass')
        chart_obj.wait_for_visible_text('#jschart_HOLD_0','Revenue')
         
        '''
        Step 18 : Verify the chart runs in a new window
        '''
        chart_obj.verify_number_of_risers("#jschart_HOLD_0 rect", 1, 77, msg="step 18.01")
        expected_listx4 =['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_run_window(expected_listx4,'#jschart_HOLD_0', msg="step 18.02")
        expected_listy4 = ['0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M']
        chart_obj.verify_y_axis_label_in_run_window(expected_listy4,'#jschart_HOLD_0', msg="step 18.03")
        chart_obj.verify_data_labels('jschart_HOLD_0',['Revenue', '0.2M', '18M', '35.9M', '53.7M', '71.5M'],msg="step 18.04: Verify data label",custom_css=' text[class*="colorScale"]')
           
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("rect[class='riser!s0!g4!mbar!r5!c0!']", "elf_green",'#jschart_HOLD_0', msg="step 18.05")
                
        '''
        Step 19 : Hover over a riser
        Step 20 : Verify tooltip
        '''
        tooltips = ['Sale Year:  2011', 'Store Type:  Store Front', 'Product Category:  Accessories', 'Cost of Goods:  $3,480,670.00', 'Revenue:  $5,039,297.57', 'Gross Profit:  $1,558,627.57', 'Revenue:  $5,039,297.57', 'Quantity Sold:  20,152']
        chart_obj.verify_active_chart_tooltip('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', tooltips, "Step:20.01 Verify tooltips")
        
        '''
        Step 21 : Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        '''
        chart_obj.api_logout()
         
        '''
        Step 22 : Edit C2046678.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159425%2FC2046678.fex
        '''
        chart_obj.edit_fex_using_api_url(repository_folder, fex_name='C2046678')
        chart_obj.wait_for_visible_text('#pfjTableChart_1','Revenue')
                 
        '''
        Step 23 : Verify IA is launched preserving the chart
        '''
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 1, 77, msg="step 23.01")
        expected_listx5 =['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Sys...', 'Televisions', 'Video Prod...']
        chart_obj.verify_x_axis_label_in_preview(expected_listx5,'#pfjTableChart_1', msg="step 23.02")
        expected_listy5 = ['0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M', '0', '10M', '20M', '30M', '40M', '50M', '60M']
        chart_obj.verify_y_axis_label_in_preview(expected_listy5,'#pfjTableChart_1', msg="step 23.03")
        chart_obj.verify_data_labels('pfjTableChart_1',['Revenue', '0.2M', '18M', '35.9M', '53.7M', '71.5M'],msg="step 23.04: Verify data label",custom_css=' text[class*="colorScale"]')
        
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g4!mbar!r5!c0!']", "elf_green",'#pfjTableChart_1', msg="step 23.05")
        
        '''
        Step 24 : In the Query pane, right click "Store Type" > "Delete"
        '''
        chart_obj.right_click_on_field_under_query_tree('Store Type', 1, 'Delete')
        utils_obj.synchronize_until_element_disappear('#pfjTableChart_1 text[class="colHeader-label!"]', 9)
         
        '''
        Step 25 : Verify the field is removed from the query pane as well as the chart
        '''
        expected_fields1=['Chart (wf_retail_lite)', 'Matrix', 'Rows', 'Sale,Year', 'Columns', 'Axis', 'Vertical Axis', 'Cost of Goods', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Revenue', 'Size', 'Tooltip', 'Gross Profit', 'Revenue', 'Quantity,Sold', 'Multi-graph', 'Animate']
        chart_obj.verify_all_fields_in_query_pane(expected_fields1, "step 25.00: Verify buckets in Query pane")
        
        chart_obj.verify_x_axis_title_in_preview(["Product Category"],'#pfjTableChart_1', msg="step 25.01")
        chart_obj.verify_number_of_risers("#pfjTableChart_1 rect", 1, 42, msg="step 25.02")
        expected_listx6 = ['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        chart_obj.verify_x_axis_label_in_preview(expected_listx6,'#pfjTableChart_1', msg="step 25.03")
        expected_listy6 = ['0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M', '0', '20M', '40M', '60M', '80M', '100M']
        chart_obj.verify_y_axis_label_in_preview(expected_listy6,'#pfjTableChart_1', msg="step 25.04")
        chart_obj.verify_data_labels('pfjTableChart_1',['Revenue', '1.4M', '30.7M', '60M', '89.3M', '118.6M'],msg="step 25.05: Verify data label",custom_css=' text[class*="colorScale"]')
    
        chart_obj.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g4!mbar!r5!c0!']", "elf_green",'#pfjTableChart_1', msg="step 25.06")
        
        '''
        Step 26 : Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        '''
        chart_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main() 