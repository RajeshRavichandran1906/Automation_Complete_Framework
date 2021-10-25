'''
Created on Jan 21, 2019

@author: Vpriya

Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8778309
Testcase Name : AHTML: Verify Filter operators against various DATETIME fields(Part 8)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8778310_TestClass(BaseTestCase):

    def test_C8778310(self):

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
        filter_button = 'Filter'
        type_value = "Greater than or equal to"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - all Greater than or equal to {2}.."
        
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
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), "Step:1 verify the page summary")
        
        """
        Step 2: For the following DATETIME fields, select Filter, then Greater than and use these values:
        HYYMDSA - 2011/03/30 10:23:24PM
        HYY Datetime - 2002
        HHISA Datetime - 12:13:14PM
        HYYMDIA Datetime - 01/01/2013 00:00
        HYYMDm Datetime - 2013/04/04 00:00:00.000000 
        HYYMDn Datetime - 2013/01/01 00:00:00.000000000 
        HYYMDH Datetime - 2013/04/04 00
        HDMtY Datetime - 14 Jul 13
        Verify that the report contains only those rows that are Greater than or equal the selected value.
        Expect 990 rows - all Greater than or equal to 2011/03/30 10:23:24PM
        Expect 10000 rows - all Greater than or equal to 2002
        Expect 15 rows - all Greater than or equal to 12:13:14PM 
        Expect 1000 rows - all Greater than or equal to 01/01/2013 00:00
        Expect 20 rows - all Greater than or equal to 2013/04/04 00:00:00.000000 
        Expect 10 rows - all Greater than or equal to 2013/10/04 00:00:00.000000000
        Expect 15 rows - all Greater than or equal to 2013/07/14 00
        Expect 20 rows - all Greater than or equal to 04 Apr 13.
        """
        '''HYYMDSA - 2011/03/30 10:23:24PM'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='2011/03/30 10:23:24PM')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 990 rows - all Greater than or equal to 2011/03/30 10:23:24PM.''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('990', '18'), page_summary_message.format('2.1','990','2011/03/30 10:23:24PM'))
        active_report_obj.close_filter_dialog()
        
        ''' HYY Datetime - 2002'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='2002')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 10000 rows - all Greater than or equal to 2002.'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.3','10000','2002'))
        active_report_obj.close_filter_dialog()
        
        '''HHISA Datetime - 12:13:14PM'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='12:13:14PM')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 15 rows - all Greater than or equal to 12:13:14PM''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('15', '1'), page_summary_message.format('2.5','15','12:13:14PM'))
        active_report_obj.close_filter_dialog()
        
        '''HYYMDIA Datetime - 01/01/2013 00:00'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='01/01/2013 00:00')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 1000 rows - all Greater than or equal to 01/01/2013 00:00'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), page_summary_message.format('2.7','1000','01/01/2013 00:00'))
        active_report_obj.close_filter_dialog()
        
        '''HYYMDm Datetime - 2013/04/04 00:00:00.000000 '''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='2013/04/04 00:00:00.000000')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 20 rows - all Greater than or equal to 2013/04/04 00:00:00.000000 '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('20', '1'), page_summary_message.format('2.9','20','2013/04/04 00:00:00.000000'))
        active_report_obj.close_filter_dialog()
        
        '''HYYMDn Datetime - 2013/10/04 00:00:00.000000000 '''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='2013/10/04 00:00:00.000000000')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 10 rows - all Greater than or equal to 2013/10/04 00:00:00.000000000 '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('10', '1'), page_summary_message.format('2.11','10','2013/10/04 00:00:00.000000000'))
        active_report_obj.close_filter_dialog()   
             
        '''HYYMDH Datetime - 2013/07/14 00'''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='2013/07/14 00')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 15 rows - all Greater than or equal to 2013/07/14 00'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('15', '1'), page_summary_message.format('2.13','15','2013/07/14 00'))
        active_report_obj.close_filter_dialog()
        
        '''HDMtY Datetime - 04 Apr 13'''
        active_report_obj.select_menu_items(table_id, "8", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='04 Apr 13')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 20 rows - all Greater than or equal to 04 Apr 13'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('20', '1'), page_summary_message.format('2.15','20','04 Apr 13'))
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()