'''
Created on Nov 9, 2018

@author: BM13368
Test Suite ID : http://172.19.2.180/testrail/index.php?/cases/view/6668192&group_by=cases:section_id&group_id=512959&group_order=asc
Test Case Name :  Date YYMD format, space separator

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6668192_TestClass(BaseTestCase):

    def test_C6668192(self):
        
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
        
        """ Step 3: Under Date separator select (space), Click on OK
        """
        date_formobj.select_date_separator("'.' (dot)")
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value('YYMD.', '3')
        
        """ Step 4: Insert YYMD. into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('YYMD.')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('4')
        data_formobj.verify_selected_datatype('date', '4.1')
        date_formobj.verify_date_format('2018/12/31', '4.2')
        date_formobj.verify_date_separator("'.' (dot)", '4.3')
        
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()