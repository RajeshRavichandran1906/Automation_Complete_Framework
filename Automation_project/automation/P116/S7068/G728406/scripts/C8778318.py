'''
Created on Jan 22, 2019

@author: Varun
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8778318
Testcase Name : AHTML: Verify Filter operators against various DATETIME fields(Part 16)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8778318_TestClass(BaseTestCase):

    def test_C8778318(self):

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
        type_value = "Omits (match case)"
        page_summary_message = "Step {0}: Expect {1} rows - all omitting the string {2}"
        
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
        Step 2: For the following DATE fields, select Filter, 
        then Omits(match case), then enter the strings below.
        Exact case match is required for filtering
        Only fields containing multiple alphanumeric characters are included.
        HYYMDSA - pm
        HYYMDSA - PM
        HHISA Datetime - am
        HHISA Datetime - AM
        HDMtY Datetime - apr
        HDMtY Datetime - Apr
        
        Verify that the report contains only those rows that Omit the alphanumeric string entered. Case sensitive.
        .
        .
        .
        .
        Expect 1000 rows - all omitting the string 'pm'
        Expect 985 rows - all omitting the string 'PM'
        Expect 1000 rows - all omitting the string 'am'
        Expect 15 rows - all omitting the string 'AM'
        Expect 1000 rows - all omitting the string 'apr'
        Expect 995 rows - all omitting the string 'Apr'
        """
        '''Expect 1000 rows - all omitting the string 'pm' '''
        active_report_obj.select_menu_items( table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(1, type_value, value1='pm')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', page_summary_message.format('2.1','1000','pm'))
        active_report_obj.close_filter_dialog()
        
        '''Expect 985 rows - all omitting the string 'PM'''
        active_report_obj.select_menu_items( table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(1, type_value, value1='PM')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '985of1000records,Page1of18', page_summary_message.format('2.2','985','PM'))
        active_report_obj.close_filter_dialog()
        
        '''Expect 1000 rows - all omitting the string 'am'''
        active_report_obj.select_menu_items( table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(1, type_value, value1='am')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', page_summary_message.format('2.3','1000','am'))
        active_report_obj.close_filter_dialog()
        
        '''Expect 15 rows - all omitting the string 'AM'''
        active_report_obj.select_menu_items( table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(1, type_value, value1='AM')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '15of1000records,Page1of1', page_summary_message.format('2.4','15','AM'))
        active_report_obj.close_filter_dialog()
        
        '''Expect 1000 rows - all omitting the string 'apr'''
        active_report_obj.select_menu_items( table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(1, type_value, value1='apr')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', page_summary_message.format('2.5','1000','apr'))
        active_report_obj.close_filter_dialog()
        
        '''Expect 995 rows - all omitting the string 'Apr'''
        active_report_obj.select_menu_items( table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(1, type_value ,value1='Apr')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '995of1000records,Page1of18', page_summary_message.format('2.6','995','Apr'))
        active_report_obj.close_filter_dialog()
        
if __name__ == "__main__":
    unittest.main()