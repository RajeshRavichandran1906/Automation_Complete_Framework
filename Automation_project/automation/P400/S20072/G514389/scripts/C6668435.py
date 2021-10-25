'''
Created on August 31, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/20072&group_by=cases:section_id&group_id=512959&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6668435
TestCase Name = Date/Time Formatted field
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6668435_TestClass(BaseTestCase):

    def test_C6668435(self):
        
        """
        TESTCASE Object's
        """
        data_formobj = dataformatdialog.DataFormatDialog(self.driver)
        custom_formobj = dataformatdialog.CustomType(self.driver)
        
        """ Step 1: Login as a WebFOCUS Basic User
                    Launch http://machine:port/{alias}/junit/dataformatTesterDlgOnly.jsp?
        """
        data_formobj.invoke_dataformattesterdlgonly_jsp()
        
        """ Step 2: Insert HYYMDm into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('HYYMDm')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('2')
        
        """ Step 3: Should show as a Custom date format
        """
        data_formobj.verify_selected_datatype('custom', '3')
        custom_formobj.verify_format('HYYMDm', '3.1')
        
        """ Step 4: Click OK
        """
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value('HYYMDm', '4')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()