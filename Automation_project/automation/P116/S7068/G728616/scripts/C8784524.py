'''
Created on Jan 24, 2019

@author: Vpriya

Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8784524
Testcase Name : AHTML: Verify Filter operators against various PACKED data fields(Part 2)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8784524_TestClass(BaseTestCase):

    def test_C8784524(self):

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
        filter_button = 'Filter'
        type_value = "Equals"
        popup_dialog_number = 1
        page_summary_message = "Step {0}: Expect {1} rows - only one Equal to {2} or {3}..'."
        
        """
        COMMON CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute the attached AR-RP-141PA.fex.
        Expect to see the following Active Report containing various PACKED data fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='1', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('1000', '18'),"Step 1: verify the page summary")
        
        """
        Step 2: For the following PACKED data fields, select Filter, then Equals and use these values:
        Packed Order - 5 & 10 & 15
        P9.2M Unit Price - $13.00 & $17.00
        P9.2C Unit Price - 17.00 & 26.00 
        P9.2Lc Unit Price - $000,026.00 & $000.028.00
        P9.2B Unit Price - (28.00) & (58.00)
        P9.2R Unit Price - 58.00 CR & 76.00 CR
        P9.2% Unit Price - 76.00% & 81.00%
        Verify that the report contains only those rows that Equals the selected value
        Expect 3 rows - only one Equal to 5 or 10 or 15
        Expect 183 rows - all Equal to $13.00 or $17.00
        Expect 233 rows - all Equal to 17.00 or 26.00
        Expect 282 rows - all Equal to $000,026.00 or $000,028.00
        Expect 232 rows - all Equal to (28.00) or (58.00)
        Expect 117 rows - all Equal to 58.00 CR or 76.00 CR
        Expect 251 rows - all Equal to 76.00% or 81.00%
        """
        
        '''Packed Order - 5 & 10 & 15'''
        active_report_obj.select_menu_items(table_id, "1", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,'large',value1='5',value2='10',value3='15')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 3 rows - only one Equal to 5 or 10 or 15''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('3', '1'), page_summary_message.format('2.1','3','5','10'))
        active_report_obj.close_filter_dialog()
        
        ''' P9.2M Unit Price - $13.00 & $17.00'''
        active_report_obj.select_menu_items(table_id, "2", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='$13.00',value2='$17.00')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 183 rows - all Equal to $13.00 or $17.00'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('183', '4'), page_summary_message.format('2.2','183','$13.00','$17.00'))
        active_report_obj.close_filter_dialog()
        
        '''P9.2C Unit Price - 17.00 & 26.00'''
        active_report_obj.select_menu_items(table_id, "3", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='17.00',value2='26.00')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 233 rows - all Equal to 17.00 or 26.00 ''' 
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('233', '5'), page_summary_message.format('2.3','233','17.00','26.00'))
        active_report_obj.close_filter_dialog()
        
        '''P9.2Lc Unit Price - $000,026.00 & $000.028.00'''
        active_report_obj.select_menu_items(table_id, "4", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='$000,026.00',value2='$000,028.00')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 282 rows - all Equal to $000,026.00 or $000,028.00'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('282', '5'), page_summary_message.format('2.4','282','$000,026.00','$000,028.00'))
        active_report_obj.close_filter_dialog()
        
        '''P9.2B Unit Price - (28.00) & (58.00) '''
        active_report_obj.select_menu_items(table_id, "5", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='(28.00)',value2='(58.00)')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 232 rows - all Equal to (28.00) or (58.00)'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('232', '5'), page_summary_message.format('2.5','232','(28.00)','(58.00)'))
        active_report_obj.close_filter_dialog()
        
        '''P9.2R Unit Price - 58.00 CR & 76.00 CR  '''
        active_report_obj.select_menu_items(table_id, "6", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value, value1='58.00 CR',value2='76.00 CR')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 117 rows - all Equal to 58.00 CR or 76.00 CR '''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('117', '3'), page_summary_message.format('2.6','117','58.00 CR','76.00 CR'))
        active_report_obj.close_filter_dialog()   
             
        '''P9.2% Unit Price - 76.00% & 81.00%'''
        active_report_obj.select_menu_items(table_id, "7", selection_type, type_value)
        active_report_obj.create_filter(popup_dialog_number, type_value,value1='76.00%',value2='81.00%')
        active_report_obj.filter_button_click(filter_button)
        '''Expect 251 rows - all Equal to 76.00% or 81.00%'''
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary.format('251', '5'), page_summary_message.format('2.7','251','76.00%','81.00%'))
        active_report_obj.close_filter_dialog()
        
if __name__ == "__main__":
    unittest.main()