'''
Created on Jan 23, 2019

@author: Varun
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8784526
Testcase Name : AHTML: Verify Filter operators against various PACKED data fields(Part 4)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8784526_TestClass(BaseTestCase):
    
    def test_C8784526(self):
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
        filter_condition = "Not equal"
        page_summary_message = "Step {0}: Expect {1} rows - all not equal to {2}"
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
        Step 2: For the following PACKED data fields, select Filter, then Not equal and use these values:
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR 
        P9.2% Unit Price - 76.00%
        
        Verify that the report contains only those rows that Equals the selected value.
        Expect 999 rows - all Not equal to 5
        Expect 916 rows - all Not equal to $13.00
        Expect 901 rows - all Not equal to 17.00
        Expect 866 rows - all Not equal to $000,026.00
        Expect 852 rows - all Not equal to (28.00) 
        Expect 916 rows - all Not equal to 58.00 CR 
        Expect 967 rows - all Not equal to 76.00% CR
        """
        """ Packed Order - 5"""
        active_report_obj.select_menu_items(table_id, "1", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,'large',value1='5')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 999 rows - all Not equal to 5 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('999', '18'), page_summary_message.format('2.1','999','5'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2M Unit Price - $13.00 """
        active_report_obj.select_menu_items(table_id, "2", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$13.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 916 rows - all Not equal to $13.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('916', '17'), page_summary_message.format('2.2','916','$13.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2C Unit Price - 17.00 """
        active_report_obj.select_menu_items(table_id, "3", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='17.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 901 rows - all Not equal to 17.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('901', '16'), page_summary_message.format('2.3','901','17.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2Lc Unit Price - $000,026.00 """
        active_report_obj.select_menu_items(table_id, "4", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$000,026.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 866 rows - all Not equal to $000,026.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('866', '16'), page_summary_message.format('2.4','866','$000,026.00'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2B Unit Price - (28.00) """
        active_report_obj.select_menu_items(table_id, "5", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='(28.00)')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 852 rows - all Not equal to (28.00) """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('852', '15'), page_summary_message.format('2.5','852','(28.00)'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2R Unit Price - 58.00 CR  """
        active_report_obj.select_menu_items(table_id, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='58.00 CR')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 916 rows - all Not equal to 58.00 CR """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('916', '17'), page_summary_message.format('2.6','916','58.00 CR'))
        active_report_obj.close_filter_dialog()
 
        """ P9.2% Unit Price - 76.00% """
        active_report_obj.select_menu_items(table_id, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='76.00%')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 967 rows - all Not equal to 76.00% CR """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('967', '17'), page_summary_message.format('2.7','967','76.00% CR'))
        active_report_obj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()