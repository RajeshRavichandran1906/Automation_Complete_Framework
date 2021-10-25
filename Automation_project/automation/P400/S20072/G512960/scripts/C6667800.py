'''
Created on September 11, 2018

@author: KK14897

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/20072&group_by=cases:section_id&group_order=asc&group_id=512960
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6667800
TestCase Name = Integer Format to Same Length Variable Length Format (AnV)
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6667800_TestClass(BaseTestCase):

    def test_C6667800(self):
        
        """
        TESTCASE Object's
        """
        data_formobj = dataformatdialog.DataFormatDialog(self.driver)
        numeric_formobj = dataformatdialog.NumericType(self.driver)
        alp_formobj = dataformatdialog.AlphaType(self.driver)
        
        """ Step 1: Login as a WebFOCUS Basic User
                    Launch http://machine:port/{alias}/junit/dataformatTesterDlgOnly.jsp?
        """
        data_formobj.invoke_dataformattesterdlgonly_jsp()
        
        """ Step 2: Insert I9 into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('I9')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('2.1')
        data_formobj.verify_selected_datatype('numeric', '2.2')
        numeric_formobj.verify_selected_numeric_datatype('integer', '2.3')
        numeric_formobj.verify_max_length('9', '2.4')
        numeric_formobj.verify_negative_numbers('2.5', expected_selected_value='-123')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show 1000 separator', False, '2.6')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show leading zero', False, '2.7')
        
        """ Step 3: Click on Data type Abc tab, change Length from 100 to 9, click on the box next to Variable Length and click OK
        """
        data_formobj.select_datatype('alpha')
        alp_formobj.modify_length_value_using_keybord_input_inside_dataformat_dialog('9')
        alp_formobj.select_variable_length_checkbox_inside_dataformat_dialog('Variable length', False)
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value('A9V', '3')
        
        """ Step 4: Insert A9V into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('A9V')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('4.1')
        data_formobj.verify_selected_datatype('alpha', '4.2')
        alp_formobj.verify_length_inside_dataformat_dialog('9', '4.3')
        alp_formobj.verify_variable_length_checkbox_inside_dataformat_dialog('Variable length', True, '4.4')
        data_formobj.close_data_format_dialog_using_ok_button()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()