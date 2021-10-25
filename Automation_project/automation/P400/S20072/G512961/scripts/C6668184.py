'''
Created on Nov 9, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6668184
Testcase Name :  Alpha Format - use A4080 and then spinner up to max
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6668184_TestClass(BaseTestCase):

    def test_C6668184(self):
        
        """
        TESTCASE Object's
        """
        data_formobj = dataformatdialog.DataFormatDialog(self.driver)
        data_form_obj = dataformatdialog.AlphaType(self.driver)
        
        """ Step 1: Login as a WebFOCUS Basic User
                    Launch http://machine:port/{alias}/junit/dataformatTesterDlgOnly.jsp?
        """
        data_formobj.invoke_dataformattesterdlgonly_jsp()
        
        """ Step 2: Insert A4096 into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('A4096')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('2')
        data_formobj.verify_selected_datatype('alpha', '2.1')
        data_form_obj.verify_length_inside_dataformat_dialog('4096', '2.2')
        data_form_obj.verify_variable_length_checkbox_inside_dataformat_dialog('Variable length', False, '2.3')
    
        """ Step 3: Click ok button to see what is returned
        """
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value('A4096', '3')
        

if __name__ == "__main__":
    unittest.main()