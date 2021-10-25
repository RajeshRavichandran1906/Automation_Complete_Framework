'''
Created on Jul 1, 2019

@author: Aftab
Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2046681
TestCase Name : Verify Rotate feature
'''
import unittest
from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.lib.global_variables import Global_variables
import time

class C2046681_TestClass(BaseTestCase):

    def test_C2046681(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj= Chart(self.driver)
        utils_obj = utillity.UtillityMethods(self.driver)
        core_utils_obj = CoreUtillityMethods(self.driver)
        g_var = Global_variables()
         
        """
            TESTCASE CSS
        """
        querypane_css = "#queryBoxColumn"
        format_css = "#FormatTab"
        c_id = g_var.current_test_case
        project_id = core_utils_obj.parseinitfile('project_id')
        suite_id = core_utils_obj.parseinitfile('suite_id')
        group_id = core_utils_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        riser_css = "#pfjTableChart_1 rect[class*='riser']"
        
        '''
        Step 1 : Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2F
        P251_S9164%2FG159425&tool=chart&master=baseapp/wf_retail_lite
        '''
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        
        '''
        Step 2 : Double click "Cost of Goods", "Product,Category"
        '''
        chart_obj.double_click_on_datetree_item('Cost of Goods', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Cost of Goods")
        chart_obj.double_click_on_datetree_item('Product,Category', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Product,Category") 
         
        '''
        Step 3 : Drag "Revenue" to "Color" bucket
        '''
        chart_obj.drag_field_from_data_tree_to_query_pane('Revenue', 1, 'Color')
        chart_obj.wait_for_visible_text(querypane_css,"Revenue")
         
        '''
        Step 4 : Select Format tab and Expand "Features" group
        Step 5 : Click "Rotate" button
        '''
        chart_obj.select_ia_ribbon_item("Format", "features")
        chart_obj.wait_for_visible_text(format_css, "Features")
        chart_obj.select_ia_ribbon_item("Format", "rotate")
        time.sleep(chart_obj.home_page_short_timesleep)
         
        '''
        Step 6 : Verify the chart is rotated
        '''
        utils_obj.verify_picture_using_sikuli('{0}_Step6'.format(c_id), msg='Step 6: Verify chart is rotated')        
        '''
        Step 7 : Click "Run"
        '''
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text('#jschart_HOLD_0','Accessories')
                 
        '''
        Step 8 : Verify the rotation is preserved
        '''
        utils_obj.verify_picture_using_sikuli('{0}_Step6'.format(c_id), msg='Step 8: Verify chart is rotated')
        chart_obj.switch_to_default_content()
        
        '''
        Step 9 : Click "IA" > "Save" > "C2046681" > "Save".
        '''
        chart_obj.save_as_from_application_menu_item(c_id, target_table_path=folder_path.replace('/', '->'), application_menu_item_name='save')
        
        '''
        Step 10 : Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        '''
        chart_obj.api_logout()
                 
        '''
        Step 11 : Run C2046681.fex .
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252F
        P251_S9164%2FG159425&BIP_item=C2046681.fex
        '''
        chart_obj.run_fex_using_api_url(folder_path, c_id, mrid='mrid', mrpass='mrpass')
        chart_obj.wait_for_visible_text('#jschart_HOLD_0','Accessories')
         
        '''
        Step 12 : Verify the chart runs in a new window
        '''
        utils_obj.verify_picture_using_sikuli('{0}_rotate'.format(c_id), msg='Step 12: Verify chart is rotated')
        
        '''
        Step 13 : Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        '''
        chart_obj.api_logout()
         
        '''
        Step 14 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2F
        P251_S9164%2FG159425%2FC2046681.fex
        '''
        chart_obj.edit_fex_using_api_url(folder_path, fex_name=c_id)
        chart_obj.wait_for_visible_text('#pfjTableChart_1', 'Revenue')

        '''
        Step 15 : Verify IA is launched preserving the chart
        '''
        utils_obj.verify_picture_using_sikuli('{0}_Step6'.format(c_id), msg='Step 15: Verify chart is rotated')
        
        '''
        Step 16 : Logout using API
        http://domain:port/alias/service/wf_security_logout.jsp
        '''
        chart_obj.api_logout()
        
        
if __name__ == '__main__':
    unittest.main()
