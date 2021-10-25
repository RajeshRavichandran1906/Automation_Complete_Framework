'''
Created on Jan 24, 2019

@author: Magesh

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8784532
Testcase Name : AHTML: Verify Filter operators against various PACKED data fields(Part 10)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8784532_TestClass(BaseTestCase):
    
    def test_C8784532(self):
        """
        CLASS OBJECTS
        """ 
        utillobj = utillity.UtillityMethods(self.driver)
        active_report_obj=Active_Report(self.driver)
        project_id=utillobj.parseinitfile('project_id')
        suite_id=utillobj.parseinitfile('suite_id')
        folder_path=project_id+"/"+suite_id
        
        """
        TESTCASE VARIABLES
        """
        fex_name="AR-RP-141PA.fex"
        expected_page_summary = '{0}of1000records,Page1of{1}'
        page_summary_number = '0'
        selection_type = 'Filter'
        filter_condition = "Less than or equal to"
        page_summary_message = "Step {0}: Expect {1} rows - all less than or equal to {2}"
        first_page_summary='Step {0}: {1}of1000records,Page1of{2}'
        
        """
        COMMON CSS
        """
        table_id='ITableData0'
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1 : Expected Result
        Execute the attached AR-RP-141PA
        Expect to see the following Active Report with various PACKED data fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='1', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), first_page_summary.format('1','1000','18'))
        
        """
        Step 2: For the following PACKED data fields, select Filter, then Less than or equal to and use these values:
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR
        P9.2% Unit Price - 76.00%
        
        Verify that the report contains only those rows that are Less than or equal to the selected value.
        Expect 5 rows - all less than 5
        Expect 84 rows - none are less than $13.00
        Expect 183 rows - all less than 17.00
        Expect 317 rows - all less than $000,026.00
        Expect 683 rows - all less than (28.00)
        Expect 535 rows - all less than 58.00 CR
        Expect 582 rows - all less than 76.00%
        """
        """ Packed Order - 5 """
        active_report_obj.select_menu_items(table_id, "1", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,'large', value1='5')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 5 rows - all less than 5 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('5', '1'), page_summary_message.format('2.1','5','5'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2M Unit Price - $13.00 """
        active_report_obj.select_menu_items(table_id, "2", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$13.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 84 rows - none are less than $13.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('84', '2'), page_summary_message.format('2.2','84','$13.00'))
        active_report_obj.close_filter_dialog()

        """ P9.2C Unit Price - 17.00 """
        active_report_obj.select_menu_items(table_id, "3", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='17.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 183 rows - all less than 17.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('183', '4'), page_summary_message.format('2.3','183','17.00'))
        active_report_obj.close_filter_dialog()

        """ P9.2Lc Unit Price - $000,026.00 """ 
        active_report_obj.select_menu_items(table_id, "4", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$000,026.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 317 rows - all less than $000,026.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('317', '6'), page_summary_message.format('2.4','317','$000,026.00'))
        active_report_obj.close_filter_dialog()
        
        """ P9.2B Unit Price - (28.00) """
        active_report_obj.select_menu_items(table_id, "5", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='(28.00)')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 683 rows - all less than (28.00) """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('683', '12'), page_summary_message.format('2.5','683','(28.00)'))
        active_report_obj.close_filter_dialog()

        """ P9.2R Unit Price - 58.00 CR """
        active_report_obj.select_menu_items(table_id, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='58.00 CR')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 535 rows - all less than 58.00 CR """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('535', '10'), page_summary_message.format('2.6','535','58.00 CR'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2% Unit Price - 76.00% """
        active_report_obj.select_menu_items(table_id, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='76.00%')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 582 rows - all less than 76.00% """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('582', '11'), page_summary_message.format('2.7','582','76.00%'))
        active_report_obj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()