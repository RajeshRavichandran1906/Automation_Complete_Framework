'''
Created on August 27, 2018

@author: AA14564

Test Suite = hhttp://lnxtestrail.ibi.com/testrail//index.php?/suites/view/20072&group_by=cases:section_id&group_id=512961&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6668168
TestCase Name = Alpha Format - change length to larger value
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6668168_TestClass(BaseTestCase):

    def test_C6668168(self):
        
        """
        TESTCASE Object's
        """
        data_formobj = dataformatdialog.DataFormatDialog(self.driver)
        data_form_obj = dataformatdialog.AlphaType(self.driver)
        
        """ Step 1: Login as a WebFOCUS Basic User
                    Launch http://machine:port/{alias}/junit/dataformatTesterDlgOnly.jsp?
        """
        data_formobj.invoke_dataformattesterdlgonly_jsp()
        
        """ Step 2: Insert A25 into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('A25')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('2')
        data_formobj.verify_selected_datatype('alpha', '2.1')
        data_form_obj.verify_length_inside_dataformat_dialog('25', '2.2')
        data_form_obj.verify_variable_length_checkbox_inside_dataformat_dialog('Variable length', False, '2.3')
        
        """ Step 3: Change Length from 25 to 50, click OK
        """
        data_form_obj.modify_length_value_using_keybord_input_inside_dataformat_dialog('50')
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value('A50', '3')
        
        """ Step 4: Insert A50 into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('A50')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('4')
        data_formobj.verify_selected_datatype('alpha', '4.1')
        data_form_obj.verify_length_inside_dataformat_dialog('50', '4.2')
        data_form_obj.verify_variable_length_checkbox_inside_dataformat_dialog('Variable length', False, '4.3')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()