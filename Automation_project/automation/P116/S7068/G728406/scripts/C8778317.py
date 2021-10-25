'''
Created on Jan 22, 2019

@author: AA14564
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8778317
Testcase Name : AHTML: Verify Filter operators against various DATETIME fields(Part 15)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8778317_TestClass(BaseTestCase):

    def test_C8778317(self):

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
        fex_name="AR-RP-141DT.fex"
        expected_page_summary = '{0}of1000records,Page1of{1}'
        page_summary_number = '0'
        selection_type = 'Filter'
        type_value = "Omits"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - all omitting the string '{2}'"
        
        """
            CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute the attached AR-RP-141DT
                Expect to see the following Active Report with various DATETIME fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='2002/12/3111:59:59PM', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), "Step 1: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following DATE fields, select Filter, then Omits, then enter the strings below.
                Case does not need to match.
                Only fields containing multiple alphanumeric characters are included.
                HYYMDSA - PM
                HHISA Datetime - AM
                HDMtY Datetime - Apr
                Verify that the report contains only those rows that Omit the alphanumeric string entered.
                Expect 985 rows - all omitting the string 'PM'
                Expect 15 rows - all omitting the string 'AM'
                Expect 995 rows - all omitting the string 'Apr'
        """
        ''' HYYMDSA - PM '''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='PM')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 985 rows - all omitting the string 'PM' ''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('985', '18'), page_summary_message.format('2', '0', 'PM'))
        active_report_obj.close_filter_dialog()
        
        ''' HHISA Datetime - AM '''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='AM')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 15 rows - all omitting the string 'AM' '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('15', '1'), page_summary_message.format('2.1', '15', 'AM'))
        active_report_obj.close_filter_dialog()
                 
        ''' HDMtY Datetime - Apr '''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='Apr')
        active_report_obj.filter_button_click(selection_type)
        ''' Expect 995 rows - all omitting the string 'Apr' ''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('995', '18'), page_summary_message.format('2.2', '995', 'Apr'))
        active_report_obj.close_filter_dialog()
        
if __name__ == "__main__":
    unittest.main()