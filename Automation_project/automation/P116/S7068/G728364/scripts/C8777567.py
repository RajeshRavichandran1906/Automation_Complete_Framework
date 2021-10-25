'''
Created on Jan 18, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8777567
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 14)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777567_TestClass(BaseTestCase):

    def test_C8777567(self):

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
        filter_condition="Contains (match case)"
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
        Step 2: For the following DATE fields, select Filter, then Contains(case match), then enter the strings below.
        Case matters for these tests, the string must match exactly.
        Only fields containing multiple alphanumeric characters are included.

        MTRDYY Order Date - April
        MTRDYY Order Date - APRIL
        wrMtrYY Order Date - june
        wrMtrYY Order Date - June
        
        Mtr Order Date - JAN
        Mtr Order Date - Jan
        Wtr Order Date - sAT
        Wtr Order Date - Sat
        
        Verify that the report contains only those rows that Contain the exact Case string value entered.
        .
        """
        """ Expect 0 rows - no dates contain 'April' """
        active_report_obj.select_menu_items(table_css, "2", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='April')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 2:1: Expect 0 rows - no dates contain 'April'")
        active_report_obj.close_filter_dialog()
        
        """ Expect 180 rows - dates of APRIL 1, 1996 contain 'APRIL' """
        active_report_obj.select_menu_items(table_css, "2", selection_type , filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='APRIL')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '180of1000records,Page1of4', "Step 2:2: Expect 180 rows - dates of APRIL 1, 1996 contain 'APRIL'")
        active_report_obj.close_filter_dialog()
        
        """ Expect 0 rows - no dates contain 'june' """
        active_report_obj.select_menu_items(table_css, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='june')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 2:3: Expect 0 rows - no dates contain 'june'")
        active_report_obj.close_filter_dialog()
        
        """ Expect 100 rows - dates of Saturday, June 1 1996 containing 'June'"""
        active_report_obj.select_menu_items(table_css, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='June')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '100of1000records,Page1of2', "Step 2:4: Expect 100 rows - dates of Saturday, June 1 1996 containing 'June' ")
        active_report_obj.close_filter_dialog()
        
        """ Expect 0 rows - no dates contain 'JAN' """
        active_report_obj.select_menu_items(table_css, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='JAN')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 2:5: Expect 0 rows - no dates contain 'JAN'")
        active_report_obj.close_filter_dialog()
        
        """ Expect 180 rows - dates of January containing 'Jan' """
        active_report_obj.select_menu_items(table_css, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='Jan')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '180of1000records,Page1of4', "Step 2:6: Expect 180 rows - dates of January containing 'Jan'")
        active_report_obj.close_filter_dialog()

        """ Expect 0 rows - no dates contain 'sAT' """
        active_report_obj.select_menu_items(table_css, "8", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='sAT')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 2:7: Expect 0 rows - no dates contain 'sAT'")
        active_report_obj.close_filter_dialog()
        
        """ Expect 100 rows - dates of Saturday containing 'Sat' """
        active_report_obj.select_menu_items(table_css, "8", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='Sat')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '100of1000records,Page1of2', "Step 2:8: Expect 100 rows - dates of Saturday containing 'Sat' ")
        active_report_obj.close_filter_dialog()

if __name__ == "__main__":
    unittest.main()