'''
Created on Jan 23, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8784530
Testcase Name : Filter operators against various PACKED data fields
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8784530_TestClass(BaseTestCase):
    
    def test_C8784530(self):
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
        filter_condition = "Greater than or equal to"
        page_summary_message = "Step {0}: Expect {1} rows - all greater than or equal to {2}"
        first_page_summary='Step {0}: {1}of1000records,Page1of{2}'
        """
        CSS
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
        Step 2: 
        For the following PACKED data fields, select Filter, then Greater than or equal to and use these values:
        Packed Order - 5
        P9.2M Unit Price - $13.00
        P9.2C Unit Price - 17.00
        P9.2Lc Unit Price - $000,026.00
        P9.2B Unit Price - (28.00)
        P9.2R Unit Price - 58.00 CR 
        P9.2% Unit Price - 76.00%
        
        Verify that the report contains only those rows that are Greater tan or equal to the selected value.
        
        Expect 996 rows - all greater than or equal to 5
        Expect 1000 rows - all are greater than or equal to $13.00
        Expect 916 rows - all greater than or equal to 17.00
        Expect 817 rows - all greater than or equal to $000,026.00
        Expect 465 rows - all greater than or equal to (28.00) 
        Expect 549 rows - all greater than or equal to 58.00 CR 
        Expect 451 rows - all greater than or equal to 76.00% CR
        """
        """ Packed Order - 5 """
        active_report_obj.select_menu_items(table_id, "1", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,'large', value1='5')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 996 rows - all greater than or equal to 5 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('996', '18'), page_summary_message.format('2.1','996','5'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2M Unit Price - $13.00 """
        active_report_obj.select_menu_items(table_id, "2", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$13.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 1000 rows - all are greater than or equal to $13.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('1000', '18'), page_summary_message.format('2.2','1000','$13.00'))
        active_report_obj.close_filter_dialog()

        """ P9.2C Unit Price - 17.00 """
        active_report_obj.select_menu_items(table_id, "3", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='17.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 916 rows - all greater than or equal to 17.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('916', '17'), page_summary_message.format('2.3','916','17.00'))
        active_report_obj.close_filter_dialog()

        """ P9.2Lc Unit Price - $000,026.00 """ 
        active_report_obj.select_menu_items(table_id, "4", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='$000,026.00')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 817 rows - all greater than or equal to $000,026.00 """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('817', '15'), page_summary_message.format('2.4','817','$000,026.00'))
        active_report_obj.close_filter_dialog()
        
        """ P9.2B Unit Price - (28.00) """
        active_report_obj.select_menu_items(table_id, "5", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='(28.00)')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 465 rows - all greater than or equal to (28.00) """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('465', '9'), page_summary_message.format('2.5','465','(28.00)'))
        active_report_obj.close_filter_dialog()

        """ P9.2R Unit Price - 58.00 CR """
        active_report_obj.select_menu_items(table_id, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='58.00 CR')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 549 rows - all greater than or equal to 58.00 CR """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('549', '10'), page_summary_message.format('2.6','549','58.00 CR'))
        active_report_obj.close_filter_dialog()
         
        """ P9.2% Unit Price - 76.00% """
        active_report_obj.select_menu_items(table_id, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='76.00%')
        active_report_obj.filter_button_click(selection_type)
        """ Expect 451 rows - all greater than or equal to 76.00% CR """
        active_report_obj.verify_page_summary(0, expected_page_summary.format('451', '8'), page_summary_message.format('2.7','451','76.00%'))
        active_report_obj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()