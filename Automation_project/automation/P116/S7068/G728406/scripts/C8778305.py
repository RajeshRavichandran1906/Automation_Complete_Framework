'''
Created on Jan 23, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8778305
Testcase Name : AHTML: Verify Filter operators against various DATETIME fields(Part 2)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools.active_report import Active_Report

class C8778305_TestClass(BaseTestCase):
    
    def test_C8778305(self):
        
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
        selection_type = "Filter"
        filter_condition = "Equals"
        highlight_button='Highlight'
        page_summary_message = "Step {0}: Expect only rows with value {1} to be Highlighted"
        first_page_summary='Step {0}: {1}of1000records,Page1of{2}'
        Test_Case_ID="C8778305"
        
        """
        CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1:Execute the attached AR-RP-141DT
        Expect to see the following Active Report with various DATETIME fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='2002/12/31 11:59:59PM', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), first_page_summary.format('1','1000','18'))
        
        """
        Step 2: For the following DATE fields, select Filter, then Equals and use these values:
        Click the Highlight button instead of the Filter button.
        
        HYYMDSA - 2011/03/30 10:23:24PM
        .
        HYY Datetime - 2013
        HHISA Datetime - 12:13:14PM
        HYYMDIA Datetime - 10/04/2013 00:00
        .
        HYYMDm Datetime - 2013/01/01 00:00:00.000000
        .
        HYYMDn Datetime - 2013/04/04 00:00:00.000000000
        .
        HYYMDH Datetime - 2013/10/04 00
        .
        HDMtY Datetime - 04 Apr 13
        
        Verify that the report contains only Highlighted rows that match the selected value.
        .
        .
        Expect only rows with value 2011/03/30 10:23:24PM to be Highlighted.
        Expect only rows with value 2013 to be Highlighted.
        Expect only rows with value 12:13:14PM to be Highlighted.
        Expect only rows with value 10/04/2013 00:00 to be Highlighted.
        Expect only rows with value 2013/01/01 00:00:00.000000 to be Highlighted.
        Expect only rows with value 2013/04/04 00:00:00.000000000 to be Highlighted.
        Expect only rows with value 2013/10/04 00 to be Highlighted.
        Expect only rows with value 04 Apr 13 to be Highlighted.
        """
        """HYYMDSA - 2011/03/30 10:23:24PM"""
        active_report_obj.select_menu_items(table_id, 1, selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='2011/03/30 10:23:24PM')
        active_report_obj.filter_button_click(highlight_button)
        """Expect only rows with value 2011/03/30 10:23:24PM to be Highlighted."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,'rgb',Test_Case_ID+'_Ds01.xlsx', page_summary_message.format('2.1','2011/03/30 10:23:24PM'))
        active_report_obj.close_filter_dialog()
            
        """HYY Datetime - 2013"""
        active_report_obj.select_menu_items(table_id, 2, selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='2013')
        active_report_obj.filter_button_click(highlight_button)
        """Expect only rows with value 2011/03/30 10:23:24PM to be Highlighted."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,'rgb',Test_Case_ID+'_Ds02.xlsx', page_summary_message.format('2.2','2011/03/30 10:23:24PM'))
        active_report_obj.close_filter_dialog()
            
        """HHISA Datetime - 12:13:14PM"""
        active_report_obj.select_menu_items(table_id, 3, selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='12:13:14PM')
        active_report_obj.filter_button_click(highlight_button)
        """Expect only rows with value 12:13:14PM to be Highlighted."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,'rgb',Test_Case_ID+'_Ds03.xlsx', page_summary_message.format('2.3','12:13:14PM'))
        active_report_obj.close_filter_dialog()
             
        """HYYMDIA Datetime - 10/04/2013 00:00"""
        active_report_obj.select_menu_items(table_id, 4, selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='10/04/2013 00:00')
        active_report_obj.filter_button_click(highlight_button)
        """Expect only rows with value 10/04/2013 00:00 to be Highlighted."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,'rgb',Test_Case_ID+'_Ds04.xlsx', page_summary_message.format('2.4','10/04/2013 00:00'))
        active_report_obj.close_filter_dialog()
        
        """HYYMDm Datetime - 2013/01/01 00:00:00.000000"""
        active_report_obj.select_menu_items(table_id, 5, selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='2013/01/01 00:00:00.000000')
        active_report_obj.filter_button_click(highlight_button)
        """Expect only rows with value 2013/01/01 00:00:00.000000 to be Highlighted."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,'rgb',Test_Case_ID+'_Ds05.xlsx', page_summary_message.format('2.5','2013/01/01 00:00:00.000000'))
        active_report_obj.close_filter_dialog()
            
        """HYYMDn Datetime - 2013/04/04 00:00:00.000000000"""
        active_report_obj.select_menu_items(table_id, 6, selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='2013/04/04 00:00:00.000000000')
        active_report_obj.filter_button_click(highlight_button)
        """Expect only rows with value 2013/04/04 00:00:00.000000000 to be Highlighted."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,'rgb',Test_Case_ID+'_Ds06.xlsx', page_summary_message.format('2.6','2013/04/04 00:00:00.000000000'))
        active_report_obj.close_filter_dialog()
            
        """HYYMDH Datetime - 2013/10/04 00"""
        active_report_obj.select_menu_items(table_id, 7, selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='2013/10/04 00')
        active_report_obj.filter_button_click(highlight_button)
        """Expect only rows with value 2013/10/04 00 to be Highlighted."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,'rgb',Test_Case_ID+'_Ds07.xlsx', page_summary_message.format('2.7','2013/10/04 00'))
        active_report_obj.close_filter_dialog()
        
        """HDMtY Datetime - 04 Apr 13"""
        active_report_obj.select_menu_items(table_id, 8, selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='04 Apr 13')
        active_report_obj.filter_button_click(highlight_button)
        """Expect only rows with value 04 Apr 13 to be Highlighted."""
        active_report_obj.verify_data_set_using_table_rowid(table_id,'rgb',Test_Case_ID+'_Ds08.xlsx', page_summary_message.format('2.8','04 Apr 13'))
        active_report_obj.close_filter_dialog()
        
        
if __name__ == "__main__":
    unittest.main()