'''
Created on September 10, 2018

@author: KK14897

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/20072&group_by=cases:section_id&group_id=512959&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6693984
TestCase Name = Date YYMD format to YY format
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6693984_TestClass(BaseTestCase):

    def test_C6693984(self):
        
        """
        TESTCASE Object's
        """
        data_formobj = dataformatdialog.DataFormatDialog(self.driver)
        date_formobj = dataformatdialog.DateType(self.driver)
        
        """ Step 1: Login as a WebFOCUS Basic User
                    Launch http://machine:port/{alias}/junit/dataformatTesterDlgOnly.jsp?
        """
        data_formobj.invoke_dataformattesterdlgonly_jsp()
        
        """ Step 2: Insert YYMD into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('YYMD')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('2')
        data_formobj.verify_selected_datatype('date', '2.1')
        date_formobj.verify_date_format('2018/12/31', '2.2')
        date_formobj.verify_date_separator("'/' (slash)", '2.3')
        
        """ Step 3: Under Date format select 2018
        """
        date_formobj.select_date_format('2018')
        
        """ Step 4: Click on OK
        """
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value('YY', '4')
        
        """ Step 5: Insert YY into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('YY')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('5')
        data_formobj.verify_selected_datatype('date', '5.1')
        date_formobj.verify_date_format('2018', '5.2')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()