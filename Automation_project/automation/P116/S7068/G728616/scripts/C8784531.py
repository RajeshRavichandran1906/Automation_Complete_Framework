'''
Created on Jan 24, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8784531
Testcase Name : AHTML: Verify Filter operators against various PACKED data fields(Part 9)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8784531_TestClass(BaseTestCase):

    def test_C8784531(self):

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
        type_value = "Less than"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - only one Equal {2}"
        
        """
            CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute the attached AR-RP-141PA
                Expect to see the following Active Report containing various PACKED data fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='1', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), "Step 1: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following PACKED data fields, select Filter, then Less than and use these values:
                Packed Order - 5
                P9.2M Unit Price - $13.00
                P9.2C Unit Price - 17.00
                P9.2Lc Unit Price - $000,026.00
                P9.2B Unit Price - (28.00)
                P9.2R Unit Price - 58.00 CR 
                P9.2% Unit Price - 76.00%
                Verify that the report contains only those rows that are Less than the selected value.
                Expect 4 rows - all less than 5
                Expect 0 rows - none are less than $13.00
                Expect 84 rows - all less than 17.00
                Expect 183 rows - all less than $000,026.00
                Expect 535 rows - all less than (28.00) 
                Expect 451 rows - all less than 58.00 CR 
                Expect 549 rows - all less than 76.00%
        """
        ''' Packed Order - 5 '''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, 'large',value1='5')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 4 rows - all less than 5 ''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('4', '1'), page_summary_message.format('2', '4', '5'))
        active_report_obj.close_filter_dialog()
        
        ''' P9.2M Unit Price - $13.00 '''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='$13.00')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 0 rows - none are less than $13.00 '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('0', '1'), page_summary_message.format('2.1', '0', '$13.00'))
        active_report_obj.close_filter_dialog()
                 
        ''' P9.2C Unit Price - 17.00 '''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='17.00')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 84 rows - all less than 17.00 ''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('84', '2'), page_summary_message.format('2.2', '84', '17.00'))
        active_report_obj.close_filter_dialog()
        
        ''' P9.2Lc Unit Price - $000,026.00 '''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='$000,026.00')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 183 rows - all less than $000,026.00 '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('183', '4'), page_summary_message.format('2.3', '183', '$000,026.00'))
        active_report_obj.close_filter_dialog()
        
        ''' P9.2B Unit Price - (28.00) '''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='(28.00)')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 535 rows - all less than (28.00) '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('535', '10'), page_summary_message.format('2.4', '535', '(28.00)'))
        active_report_obj.close_filter_dialog()
           
        ''' P9.2R Unit Price - 58.00 CR '''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='58.00 CR')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 451 rows - all less than 58.00 CR '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('451', '8'), page_summary_message.format('2.5', '451', '58.00 CR'))
        active_report_obj.close_filter_dialog()
        
        ''' P9.2% Unit Price - 76.00% '''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='76.00%')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 549 rows - all less than 76.00% '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('549', '10'), page_summary_message.format('2.6', '549', '76.00%'))
        active_report_obj.close_filter_dialog()
                
if __name__ == "__main__":
    unittest.main()