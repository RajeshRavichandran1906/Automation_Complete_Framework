'''
Created on Jan 24, 2019

@author: Varun
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8784533
Testcase Name : AHTML: Verify Filter operators against various PACKED data fields(Part 11)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8784533_TestClass(BaseTestCase):
    
    def test_C8784533(self):
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
        filter_condition = "Between"
        page_summary_message = "Step {0}: Expect {1} rows - all between {2} and {3}"
        first_page_summary='Step {0}: {1}of1000records,Page1of{2}'
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
        Step 2: For the following PACKED data fields, select Filter, then Between and use the pair of values:
        Packed Order - 5 & 10
        P9.2M Unit Price - $13.00 & $17.00
        P9.2C Unit Price - 17.00 & 26.00
        P9.2Lc Unit Price - $000,026.00 & $000,028.00
        P9.2B Unit Price - (58.00) & (28.00) in that order
        P9.2R Unit Price - 76.00 CR & 58.00 CR in that order
        P9.2% Unit Price - 76.00% & 81.00%
        
        Verify that the report contains only those rows that are Between the selected values.
        
        Expect 6 rows - all between 5 and 10
        Expect 183 rows - all between than $13.00 & $17.00
        Expect 233 rows - all between 17.00 & 26.00
        Expect 282 rows - all between $000,026.00 & $000,028.00
        Expect 232 rows - all between (58.00) & (28.00) 
        Expect 117 rows - all between 76.00 CR & 58.00 CR 
        Expect 251 rows - all between 76.00% & 81.00%
        """
        """ Packed Order - 5 & 10 """
        active_report_obj.select_menu_items(table_id, "1", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,'large',value1='5',value2='10')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 6 rows - all between 5 and 10 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('6', '1'), page_summary_message.format('2.1','6','5','10'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2M Unit Price - $13.00 & $17.00 """
        active_report_obj.select_menu_items(table_id, "2", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$13.00',value2='$17.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 183 rows - all between than $13.00 & $17.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('183', '4'), page_summary_message.format('2.2','183','$13.00','$17.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2C Unit Price - 17.00 & 26.00 """
        active_report_obj.select_menu_items(table_id, "3", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='17.00', value2='26.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 233 rows - all between 17.00 & 26.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('233', '5'), page_summary_message.format('2.3','233','17.00','26.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2Lc Unit Price - $000,026.00 & $000,028.00 """
        active_report_obj.select_menu_items(table_id, "4", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$000,026.00', value2='$000,028.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 282 rows - all between $000,026.00 & $000,028.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('282', '5'), page_summary_message.format('2.4','282','$000,026.00','$000,028.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2B Unit Price - (58.00) & (28.00) in that order """
        active_report_obj.select_menu_items(table_id, "5", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='(58.00)', value2='(28.00)')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 282 rows - all between (58.00) & (28.00)"""
        active_report_obj.verify_page_summary(0, expected_page_summary.format('232', '5'), page_summary_message.format('2.5','232','(58.00)','(28.00)'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2R Unit Price - 76.00 CR & 58.00 CR in that order """
        active_report_obj.select_menu_items(table_id, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='76.00 CR', value2='58.00 CR')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 117 rows - all between 76.00 CR & 58.00 CR"""
        active_report_obj.verify_page_summary(0, expected_page_summary.format('117', '3'), page_summary_message.format('2.6','117','76.00 CR','58.00 CR'))
        active_report_obj.close_filter_dialog()
 
        """ P9.2% Unit Price - 76.00% & 81.00% """
        active_report_obj.select_menu_items(table_id, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='76.00%',value2='81.00%')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 251 rows - all between 76.00% & 81.00% """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('251', '5'), page_summary_message.format('2.7','251','76.00%', '81.00%'))
        active_report_obj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()