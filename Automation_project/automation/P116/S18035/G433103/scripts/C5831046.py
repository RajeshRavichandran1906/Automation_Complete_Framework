'''
Created on January 4, 2019

@author: KK14897

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5831046
TestCase Name = Add same field to tooltip and any other bucket, display tooltip value 3 times (ACT-1439)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_chart

class C5831046_TestClass(BaseTestCase):
    
    def test_C5831046(self):
        
        ac_obj=active_chart.Active_Chart(self.driver)
        expected_tooltip_list=['SALES:208420', 'SALES:208420']
        '''
        Step 1 : Sign in to WebFOCUS as a developer user
        http://machine:port/{alias}
        Step 2 : Create new chart using below API
        http://machine:port/{alias}/ia?tool=Chart&master=ibisamp/car&item=IBFS%3A%2FWFC%2FRepository%2FS18035
        '''
        ac_obj.invoke_chart_tool_using_api("ibisamp/car", mrid='mrid', mrpass='mrpass')
        
        '''
        Step 3 : Change output format to Active format.
        '''
        ac_obj.change_output_format_type("active_report")
        '''
        Step 4 : Double click Sales and add Sales to Tooltip.
        '''
        ac_obj.double_click_on_datetree_item('SALES',1)
        ac_obj.drag_field_from_data_tree_to_query_pane('SALES', 1, 'Tooltip', 1)
        
        '''
        Step 5 : Click run
        '''
        ac_obj.run_chart_from_toptoolbar()
        '''
        Step 6 : Hover over any bar, and verify tooltip value is displaying properly
        '''
        ac_obj.switch_to_frame()
        ac_obj.verify_tooltip_in_run_window("riser!s0!g0!mbar!", expected_tooltip_list, 'STep 06 : Verify Tolltip', parent_css='#MAINTABLE_0')
        '''
        Step 7 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        '''
        ac_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()