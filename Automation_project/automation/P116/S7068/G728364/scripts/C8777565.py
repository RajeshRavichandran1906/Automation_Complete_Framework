'''
Created on Jan 18, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/tests/view/21601210&group_by=cases:section_id&group_order=asc&group_id=728364
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 12) 
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777565_TestClass(BaseTestCase):

    def test_C8777565(self):

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
        fex_name="AR-RP-141DA.fex"
        expected_page_summary = '1000of1000records,Page1of18'
        page_summary_number = '0'
        selection_type = "Filter"
        filter_condition="Not Between"
        """
            CSS
        """
        table_css='ITableData0'
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_css)
        """
        Step 1: Execute AR-RP-141DA.fex from below API to produce the decimal output
                Expect to see the following Active Report containing DATE fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='19960101', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary, "Step 1: Expect to see the following Active Report. - page summary verification")
        """
        Step 2: For the following DATE fields, select Filter, then Not Between the pair of values:
            YYMD Order Date - 19960201 & 19960301
            MTRDYY Order Date - MARCH 1, 1996 & MAY 1, 1996
            YYJUL Order Date - 1996/001 & 1996/092
            JULIAN Order Date - 96/092 & 96/153
            QYY Order Date - Q1 1996 & Q2 1996
            wrMtrYY Order Date - Monday, Apr 1 1996 & Wednesday, May 1 1996
            Mtr Order Date - May & June
            Wtr Order Date - Wednesday & Friday
            
            Verify that the report contains only those rows that are filter_condition the pair of selected values.
        """
        """ Expect 640 rows - filter_condition 19960201 and 19960301 """
        active_report_obj.select_menu_items(table_css, "1", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='19960201', value2='19960301')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '640of1000records,Page1of12', "Step 2:1: Expect 767 rows - values 17.00 & 26.00")
        active_report_obj.close_filter_dialog()
        
        """ Expect 460 rows - filter_condition MARCH 1, 1996 & MAY 1, 1996 """
        active_report_obj.select_menu_items(table_css, "2", selection_type , filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='MARCH 1, 1996', value2='MAY 1, 1996')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '460of1000records,Page1of9', "Step 2:2: Expect 460 rows - filter_condition MARCH 1, 1996 & MAY 1, 1996")
        active_report_obj.close_filter_dialog()

        """ Expect 280 rows - filter_condition 1996/001 & 1996/092 """
        active_report_obj.select_menu_items(table_css, "3", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='1996/001', value2='1996/092')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '280of1000records,Page1of5', "Step 2:3: Expect 280 rows - filter_condition 1996/001 & 1996/092")
        active_report_obj.close_filter_dialog()

        """ Expect 540 rows - filter_condition 96/092 & 96/153"""
        active_report_obj.select_menu_items(table_css, "4", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='96/092',value2='96/153')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '540of1000records,Page1of10', "Step 2:4: Expect 540 rows - filter_condition 96/092 & 96/153")
        active_report_obj.close_filter_dialog()
         
        """ Expect 0 rows - filter_condition Q1 1996 & Q2 1996"""
        active_report_obj.select_menu_items(table_css, "5", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='Q1 1996', value2='Q2 1996')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 2:5: Expect 0 rows - filter_condition Q1 1996 & Q2 1996")
        active_report_obj.close_filter_dialog()
        
        """ Expect 640 rows - filter_condition Monday, Apr 1 1996 & Wednesday, May 1 1996 """
         
        active_report_obj.select_menu_items(table_css, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='Monday, April 1 1996', value2='Wednesday, May 1 1996')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '640of1000records,Page1of12', "Step 2:6: Expect 640 rows - filter_condition Monday, Apr 1 1996 & Wednesday, May 1 1996")
        active_report_obj.close_filter_dialog()
 
        """ Expect 720 rows - filter_condition May & June """
        active_report_obj.select_menu_items(table_css, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='May', value2='June')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '720of1000records,Page1of13', "Step 2:7: Expect 867 rows - values 140.00CR & 125.00CR")
        active_report_obj.close_filter_dialog()
         
        """ Expect 460 rows - filter_condition Wednesday & Friday """
        active_report_obj.select_menu_items(table_css, "8", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='Wednesday', value2='Friday')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '460of1000records,Page1of9', "Step 2:8: Expect 460 rows - filter_condition Wednesday & Friday")
        active_report_obj.close_filter_dialog()
                              

if __name__ == "__main__":
    unittest.main()