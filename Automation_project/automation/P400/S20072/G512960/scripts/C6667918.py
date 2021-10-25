'''
Created on September 12, 2018

@author: Varun

Test Suite = hhttp://lnxtestrail.ibi.com/testrail//index.php?/suites/view/20072&group_by=cases:section_id&group_id=512956&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667918
TestCase Name = Integer Format to Currency Format, euro, floating
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6667918_TestClass(BaseTestCase):

    def test_C6667918(self):
        
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
        
        """Step 3: Click on Type $ tab, click on drop down under Currency symbol and select Euro, click on Floating button under Symbol position, click OK
        """
        numeric_formobj.select_numeric_type('currency')
        numeric_formobj.select_currency_symbol('Euro')
        numeric_formobj.select_symbol_position('Floating')
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value("D9.2c:E", '3')
               
        """Step 4: Insert D9.2:E into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('D9.2c:E')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('5')
        data_formobj.verify_selected_datatype('numeric', '5.1')
        numeric_formobj.verify_selected_numeric_datatype('currency', '5.2')
        numeric_formobj.verify_max_length('9', '5.3')
        numeric_formobj.verify_decimal_place('2', '5.4')
        numeric_formobj.verify_negative_numbers('5.5', expected_selected_value='-123')
        numeric_formobj.verify_currency_symbol( 'Euro', '5.6')
        numeric_formobj.verify_symbol_position('5.7', expected_selected_value='Floating')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show 1000 separator', False, '5.8')
        numeric_formobj.verify_checkbox_inside_numeric__dataformat_dialog('Show leading zero', False, '5.9')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()