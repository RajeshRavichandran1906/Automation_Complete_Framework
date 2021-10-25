'''
Created on September 07, 2018

@author: KK14897

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/20072&group_by=cases:section_id&group_order=asc&group_id=512956
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6668614
TestCase Name = Sceintific notation format D12.2E
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wfcomponent import dataformatdialog

class C6668614_TestClass(BaseTestCase):

    def test_C6668614(self):
        
        """
        TESTCASE Object's
        """
        data_formobj = dataformatdialog.DataFormatDialog(self.driver)
        custom_formobj = dataformatdialog.CustomType(self.driver)
        
        """ Login as a WebFOCUS Basic User
            Launch http://machine:port/{alias}/junit/dataformatTesterDlgOnly.jsp?
        """
        data_formobj.invoke_dataformattesterdlgonly_jsp()
        
        """ Step 2: Insert D12.3E into the Format to parse (input) and click Show data format
        """
        data_formobj.set_text_to_format_to_parse_input_box('D12.3E')
        data_formobj.click_show_data_format_button()
        data_formobj.verify_data_format_dialog_is_visible('2')
        
        """ Step 3: Verify it is a custom format.
        """
        data_formobj.verify_selected_datatype('custom', '3')
        custom_formobj.verify_format('D12.3E', '3.1')
        
        """ Step 4: click ok
        """
        data_formobj.close_data_format_dialog_using_ok_button()
        data_formobj.verify_output_format_value('D12.3E', '4')
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()