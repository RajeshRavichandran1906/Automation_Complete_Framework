'''
Created on Jan 24, 2019

@author: Varun
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8784525
Testcase Name : AHTML: Verify Filter operators against various PACKED data fields(Part 3)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8784525_TestClass(BaseTestCase):
    
    def test_C8784525(self):
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
        filter_condition = "Equals"
        button_click = 'Highlight'
        first_page_summary='Step {0}: {1}of1000records,Page1of{2}'
        row_color_type = 'rgb'
        data_set_message = "Step {0}: Expect to see row(s) with value {1} Highlighted."
        case_id = 'C8784525'
        
        """
        CSS
        """
        table_id='ITableData0'
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        """
        Step 1 : Expected Result
        Execute the attached AR-RP-141DT
        Expect to see the following Active Report with various DATETIME fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='1', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'), first_page_summary.format('1','1000','18'))
        
        """
        Step 2: For the following PACKED data fields, select Filter, then Equals and use these values:
        Click the Highlight button instead of the Filter button.
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR 
        P9.2% Unit Price - 76.00%
        
        Verify that the report contains only Highlighted rows that match the selected value.
        .
        .
        Expect to see only 1 row with value 5 Highlighted.
        Expect to see only rows with value $13.00 Highlighted.
        Expect to see only rows with value 17.00 Highlighted.
        Expect to see only rows with value $000,026.00 Highlighted.
        Expect to see only rows with value (28.00) Highlighted.
        Expect to see only rows with value 58.00 CR Highlighted.
        Expect to see only rows with value 76.00% Highlighted.
        """
        
        """ Packed Order - 5 """
        active_report_obj.select_menu_items(table_id, "1", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,'large',value1='5')
        active_report_obj.filter_button_click(button_click)
        """ Expect to see only 1 row with value 5 Highlighted. """
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type, case_id+'_ds21.xlsx', data_set_message.format('2.1', '5'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2M Unit Price - $13.00 """
        active_report_obj.select_menu_items(table_id, "2", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$13.00')
        active_report_obj.filter_button_click(button_click)
        """ Expect to see only rows with value $13.00 Highlighted. """
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type, case_id+'_ds22.xlsx', data_set_message.format('2.2', '$13.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2C Unit Price - 17.00 """
        active_report_obj.select_menu_items(table_id, "3", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='17.00')
        active_report_obj.filter_button_click(button_click)
        """ Expect to see only rows with value 17.00 Highlighted """
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type, case_id+'_ds23.xlsx', data_set_message.format('2.3', '17.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2Lc Unit Price - $000,026.00 """
        active_report_obj.select_menu_items(table_id, "4", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$000,026.00')
        active_report_obj.filter_button_click(button_click)
        """ Expect to see only rows with value $000,026.00 Highlighted """
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type, case_id+'_ds24.xlsx', data_set_message.format('2.4', '$000,026.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2B Unit Price - (28.00) """
        active_report_obj.select_menu_items(table_id, "5", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='(28.00)')
        active_report_obj.filter_button_click(button_click)
        """ Expect to see only rows with value (28.00) Highlighted """
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type, case_id+'_ds25.xlsx', data_set_message.format('2.5', '28.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2R Unit Price - 58.00 CR  """
        active_report_obj.select_menu_items(table_id, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='58.00 CR')
        active_report_obj.filter_button_click(button_click)
        """ Expect to see only rows with value 58.00 CR Highlighted """
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type, case_id+'_ds26.xlsx', data_set_message.format('2.6', '58.00 CR'))
        active_report_obj.close_filter_dialog()
 
        """ P9.2% Unit Price - 76.00% """
        active_report_obj.select_menu_items(table_id, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='76.00%')
        active_report_obj.filter_button_click(button_click)
        """ Expect to see only rows with value 76.00% Highlighted """
        active_report_obj.verify_data_set_using_table_rowid(table_id,row_color_type, case_id+'_ds27.xlsx', data_set_message.format('2.7', '76.00%'))
        active_report_obj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()