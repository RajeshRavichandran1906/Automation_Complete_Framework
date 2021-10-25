'''
Created on Aug 26, 2019

@author: Robert
Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852451
Test case name: Edit format of PCT.CNT field display chart with correct data
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.chart import Chart

class C5852451_TestClass(BaseTestCase):
    
    def test_C5852451(self):
        
        """
        TESTCASE VARIABLES
        """
        chart_ = Chart(self.driver)
        
        '''
        Test case CSS 
        '''
        run_parent_css="#jschart_HOLD_0"
        
        '''
        Step 1 : Launch IA Chart using car.mas in developer user.
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10660%2FG168204%2F&master=ibisamp%2Fcar&tool=chart
        '''
        chart_.invoke_chart_tool_using_api('ibisamp/car', mrid='mrid', mrpass='mrpass')        
        
        '''
        Step 2 : Double click "COUNTRY" and "DEALER_COST"
        '''
        chart_.double_click_on_datetree_item('COUNTRY',1)
        chart_.wait_for_visible_text('#queryTreeColumn', 'COUNTRY', chart_.chart_long_timesleep)
        chart_.double_click_on_datetree_item('DEALER_COST',1)
        chart_.wait_for_visible_text('#queryTreeColumn', 'DEALER_COST', chart_.chart_long_timesleep)
        
        '''
        Step 3 : Right click "DEALER_COST" > More > Aggregation > "Percent of Count"
        '''
        chart_.right_click_on_field_under_query_tree('DEALER_COST', field_position=1, context_menu_path = 'More->Aggregation Functions->Percent of Count')
        chart_.wait_for_visible_text('#queryTreeColumn','PCT.CNT.DEALER_COST', chart_.chart_long_timesleep)
         
        '''
        Step 4 : Right click PCT.CNT.DEALER_COST in query pane > Click "Edit Format"
        '''
        chart_.right_click_on_field_under_query_tree('PCT.CNT.DEALER_COST', field_position=1, context_menu_path = 'Edit Format')
        chart_.wait_for_visible_text('#fmtDlgCancel', 'Cancel', chart_.chart_long_timesleep)
         
        '''
        Step 5 : Select Percent(%) check box > Click Ok.
        Chart preview.
        '''
        self.driver.find_element_by_xpath("//div[@id= 'percentRadioBtn']").click()
        self.driver.find_element_by_css_selector('#fmtDlgOk').click()
        
        chart_.wait_for_number_of_element('#pfjTableChart_1 rect[class="riser!s0!g1!mbar!"]', 1)
        chart_.verify_x_axis_title_in_preview(['COUNTRY'],msg='Step 05.00')
        chart_.verify_y_axis_title_in_preview(['PCT.CNT DEALER_COST'],msg='Step 05.01')
        expected_label_x = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        chart_.verify_x_axis_label_in_preview(expected_label_x, msg='Step 05.02')
        expected_label_y = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
        chart_.verify_y_axis_label_in_preview(expected_label_y, msg='Step 05.03')
        chart_.verify_chart_color('pfjTableChart_1', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 05.04 : Verify chart color', attribute_type='fill')
        
        '''
        Step 6 : Click Run button.
        Chart tooltip valued displayed with % symbol.
        '''
        chart_.run_chart_from_toptoolbar()
        chart_.switch_to_frame()
        chart_.verify_tooltip_in_run_window('riser!s0!g0!mbar', ['COUNTRY:ENGLAND', 'PCT.CNT DEALER_COST:22%'], 'Step 06.00 : Verify tooltip')
        chart_.switch_to_default_content()      
         
        '''
        Step 7 : Click Save icon from the toolbar > Enter title as "C5852451" > Click Save button.
        '''
        chart_.select_item_in_top_toolbar('save')
        chart_.save_file_in_save_dialog('C5852451') 
                 
        '''
        Step 8 : Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        '''
        chart_.api_logout()
        
        '''
        Step 9 : Run chart using API code :
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10660%252FG168204%252F&BIP_item=C5852451.fex
        Chart displayed in run time and tooltip valued displayed with % symbol.
        '''
        chart_.run_fex_using_api_url(folder_name='P292_S10660/G168204', fex_name='C5852451', mrid='mrid', mrpass='mrpass')
        chart_.verify_x_axis_title_in_preview(['COUNTRY'], parent_css=run_parent_css, msg='Step 09.00')
        chart_.verify_y_axis_title_in_preview(['PCT.CNT DEALER_COST'], parent_css=run_parent_css, msg='Step 09.01')
        expected_label_x = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        chart_.verify_x_axis_label_in_preview(expected_label_x, parent_css=run_parent_css, msg='Step 09.02')
        expected_label_y = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
        chart_.verify_y_axis_label_in_preview(expected_label_y, parent_css=run_parent_css, msg='Step 09.03')
        chart_.verify_chart_color('jschart_HOLD_0', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 09.04 : Verify chart color', attribute_type='fill')
        chart_.verify_tooltip_in_run_window('riser!s0!g0!mbar', ['COUNTRY:ENGLAND', 'PCT.CNT DEALER_COST:22%'], 'Step 09.05 : Verify tooltip')
        
        '''
        Step 10 : Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        '''
        chart_.api_logout()
        
        '''
        Step 11 : Launch the API to Edit chart:
        http://domain.com:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S10660%2FG168204%2FC5852451.fex
        Chart restored successfully without error.
        '''
        chart_.edit_fex_using_api_url(folder_name='P292_S10660/G168204', fex_name='C5852451')
        chart_.wait_for_number_of_element('#pfjTableChart_1 rect[class="riser!s0!g1!mbar!"]', 1, chart_.chart_long_timesleep)
        chart_.verify_x_axis_title_in_preview(['COUNTRY'], msg='Step 11.00')
        chart_.verify_y_axis_title_in_preview(['PCT.CNT DEALER_COST'], msg='Step 11.01')
        expected_label_x = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        chart_.verify_x_axis_label_in_preview(expected_label_x, msg='Step 11.02')
        expected_label_y = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45']
        chart_.verify_y_axis_label_in_preview(expected_label_y, msg='Step 11.03')
        chart_.verify_chart_color('pfjTableChart_1', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 11.04 : Verify chart color', attribute_type='fill')
        
        '''
        Step 12 : Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        '''
        
if __name__ == '__main__':
    unittest.main()