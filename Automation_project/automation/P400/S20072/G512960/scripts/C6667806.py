'''
Created on September 12, 2018

@author: AA14564

Test Suite = hhttp://lnxtestrail.ibi.com/testrail//index.php?/suites/view/20072&group_by=cases:section_id&group_id=512956&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667806
TestCase Name = Integer Format to Decimal Format, Negative Bracket
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6667806_TestClass(BaseTestCase):

    def test_C6667806(self):
        
        """
        TESTCASE Object's
        """
        data_formobj = dataformatdialog.DataFormatDialog(self.driver) 
        numeric_formobj = dataformatdialog.NumericType(self.driver)
        
        """ Step 1: Login as a WebFOCUS Basic User
                    Launch http://machine:port/{alias}/junit/dataformatTesterDlgOnly.jsp?
        """
        data_formobj.invoke_dataformattesterdlgonly_jsp()
        
        """ Step 2: Insert I9 into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('I9')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('2')
        data_formobj.verify_selected_datatype('numeric', '2.1')
        numeric_formobj.verify_selected_numeric_datatype('integer', '2.2')
        numeric_formobj.verify_max_length('9', '2.3')
        numeric_formobj.verify_negative_numbers('2.4', expected_selected_value='-123')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show 1000 separator', False, '2.5')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show leading zero', False, '2.6')
        
        """Step 3: Click Type 11.11 tab, Select the right box with brackets under Negative number, click OK
        """
        numeric_formobj.select_numeric_type('decimal')
        numeric_formobj.select_negative_numbers('(123)')
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value('D12.2Bc', '3')
        
        """ Step 4: Insert D12.2B into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('D12.2B')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('4')
        data_formobj.verify_selected_datatype('numeric', '4.1')
        numeric_formobj.verify_selected_numeric_datatype('decimal', '4.2')
        numeric_formobj.verify_max_length('12', '4.3')
        numeric_formobj.verify_decimal_place('2', '4.4')
        numeric_formobj.verify_negative_numbers('4.5', expected_selected_value='(123)')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show 1000 separator', True, '4.6')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show leading zero', False, '4.7')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()