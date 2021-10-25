'''
Created on September 11, 2018

@author: KK14897

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/20072&group_by=cases:section_id&group_order=asc&group_id=512960
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6667881
TestCase Name = Integer Format to Currency Format, locale, floating, 1000 separator
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6667881_TestClass(BaseTestCase):

    def test_C6667881(self):
        
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
        data_formobj.verify_data_format_dialog_is_visible('2.1')
        data_formobj.verify_selected_datatype('numeric', '2.2')
        numeric_formobj.verify_selected_numeric_datatype('integer', '2.3')
        numeric_formobj.verify_max_length('9', '2.4')
        numeric_formobj.verify_decimal_place('2', '2.5')
        numeric_formobj.verify_negative_numbers('2.6', expected_selected_value='-123')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show 1000 separator', False, '2.7')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show leading zero', False, '2.8')
        
        """ Step 3: Click on Type $ tab, click on Floating button under Symbol position, click on box next to Show 1000 separator, click OK
        """
        numeric_formobj.select_numeric_type('currency')
        numeric_formobj.verify_symbol_position('3.1', 'Fixed')
        numeric_formobj.verify_currency_symbol('Base on locale', '3.2')
        numeric_formobj.select_symbol_position('Floating')
        numeric_formobj.select_checkbox_inside_numeric_dataformat_dialog('show_1000_separator', False)
        data_formobj.close_data_format_dialog_using_ok_button()
         
        """ Step 4: Verify text in the output window
        """
        data_formobj.verify_output_format_value("D9.2C:C(CURRENCY_DISPLAY='LEFT_FLOAT',CURRENCY_ISO_CODE='default')", '4')
        
        """ Step 5: Insert D9.2C:C(CURRENCY_DISPLAY='LEFT_FLOAT',CURRENCY_ISO_CODE='default') into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box("D9.2C:C(CURRENCY_DISPLAY='LEFT_FLOAT',CURRENCY_ISO_CODE='default')")
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('5.1')
        data_formobj.verify_selected_datatype('numeric', '5.2')
        numeric_formobj.verify_selected_numeric_datatype('currency', '5.3')
        numeric_formobj.verify_max_length('9', '5.4')   
        numeric_formobj.verify_decimal_place('2', '5.5') 
        numeric_formobj.verify_negative_numbers('5.6', expected_selected_value='-123') 
        numeric_formobj.verify_currency_symbol('Base on locale', '5.7')
        numeric_formobj.verify_symbol_position('5.8', 'Floating')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show 1000 separator', True, '5.9')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show leading zero', False, '5.10')
        data_formobj.close_data_format_dialog_using_ok_button()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()