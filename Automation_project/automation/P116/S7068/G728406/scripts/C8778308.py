'''
Created on Jan 21, 2019

@author: Vpriya

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8777554
Testcase Name : AHTML: Verify Filter operators against various DATETIME fields(Part 6)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8778308_TestClass(BaseTestCase):

    def test_C8778308(self):

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
        case_id = 'C8778308'
        expected_page_summary = '{0}of1000records,Page1of{1}'
        page_summary_number = '0'
        selection_type = 'Filter'
        filter_button = 'Highlight'
        type_value = "Not equal"
        popup_dialog_number = 1
        row_color_type = 'rgb'
        data_set_message = "Step {0}: Expect all rows except {1} to be Highlighted."
        page_summary_message = "Step {0}: Verify Page summary '1000of1000records,Page1of18' after close dialog."
        
        """
        COMMON CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute the attached AR-RP-141DA.
        Expect to see the following Active Report with various DATETIME fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='2002/12/31 11:59:59PM', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('1'))
        
        """
        Step 2: For the following DATE fields, select Filter, then Not equal and use these values:
        Click the Highlight button instead of the Filter button.
        HYYMDSA - 2011/03/30 10:23:24PM
        HYY Datetime - 2013
        HHISA Datetime - 12:13:14PM
        HYYMDIA Datetime - 10/04/2013 00:00
        HYYMDm Datetime - 2013/01/01 00:00:00.000000
        HYYMDn Datetime - 2013/04/04 00:00:00.000000000
        HYYMDH Datetime - 2013/10/04 00
        HDMtY Datetime - 04 Apr 13
        Verify that the report contains only Highlighted rows that do NOT match the selected value.
        Expect all rows except 2011/03/30 10:23:24PM to be Highlighted.
        Expect all rows except 2013 to be Highlighted.
        Expect all rows except 12:13:14PM to be Highlighted.
        Expect all rows except 10/04/2013 00:00 to be Highlighted.
        Expect all rows except 2013/01/01 00:00:00.000000 to be Highlighted.
        Expect all rows except 2013/04/04 00:00:00.000000000 to be Highlighted.
        Expect all rows except 2013/10/04 00 to be Highlighted.
        Expect all rows except 04 Apr 13 to be Highlighted.
        """
        '''HYYMDSA - 2011/03/30 10:23:24PM'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='2011/03/30 10:23:24PM')
        active_report_obj.filter_button_click('Highlight')
        
        '''Expect all rows except 2011/03/30 10:23:24PM to be Highlighted..''' 
        
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds01.xlsx', data_set_message.format('2', '2011/03/30 10:23:24PM'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.1'))
        
        '''HYY Datetime - 2013'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='2013')
        active_report_obj.filter_button_click(filter_button)
        '''Expect all rows except 2013 to be Highlighted.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds02.xlsx', data_set_message.format('2.2', '2013'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.3'))
        
        '''HHISA Datetime - 12:13:14PM'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='12:13:14PM')
        active_report_obj.filter_button_click(filter_button)
        '''Expect all rows except 12:13:14PM to be Highlighted.''' 
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds03.xlsx', data_set_message.format('2.4', '12:13:14PM'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.5'))
        
        
        '''HYYMDIA Datetime - 10/04/2013 00:00'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='10/04/2013 00:00')
        active_report_obj.filter_button_click(filter_button)
        '''Expect all rows except 10/04/2013 00:00 to be Highlighted.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds04.xlsx', data_set_message.format('2.6', '10/04/2013 00:00'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.7'))
        
        '''HYYMDm Datetime - 2013/01/01 00:00:00.000000'''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='2013/01/01 00:00:00.000000')
        active_report_obj.filter_button_click(filter_button)
        '''Expect all rows not equal to 2013/01/01 00:00:00.000000 to be Highlighted.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds05.xlsx', data_set_message.format('2.8', '2013/01/01 00:00:00.000000'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.9'))
        
        '''HYYMDn Datetime - 2013/04/04 00:00:00.000000000'''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='2013/04/04 00:00:00.000000000')
        active_report_obj.filter_button_click(filter_button)
        '''Expect all rows except 2013/04/04 00:00:00.000000000 to be Highlighted.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds06.xlsx', data_set_message.format('2.10', '2013/04/04 00:00:00.000000000'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.11'))
                
        '''HYYMDH Datetime - 2013/10/04 00'''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='2013/10/04 00')
        active_report_obj.filter_button_click(filter_button)
        '''Expect all rows except 2013/10/04 00 to be Highlighted.'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds07.xlsx', data_set_message.format('2.12', '2013/10/04 00'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.13'))
        
        '''HDMtY Datetime - 04 Apr 13'''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='04 Apr 13')
        active_report_obj.filter_button_click(filter_button)
        '''Expect all rows except 04 Apr 13 to be Highlighted'''
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type,case_id+'_Ds08.xlsx', data_set_message.format('2.14', '04 Apr 13'))
        active_report_obj.close_filter_dialog()
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.15'))
         
         
if __name__ == "__main__":
    unittest.main()