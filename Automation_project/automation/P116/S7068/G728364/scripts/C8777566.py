'''
Created on Jan 18, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8777566
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 13)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777566_TestClass(BaseTestCase):

    def test_C8777566(self):

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
        filter_condition="Contains"
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
        Step 2 : For the following DATE fields, select Filter, then Contains, then enter the strings below.
        Case does NOT matter for these tests
        YYMD Order Date - 9602
        MTRDYY Order Date - April
        YYJUL Order Date - 6/15
        JULIAN Order Date - 96/00
        QYY Order Date - Q2 
        wrMtrYY Order Date - june
        Mtr Order Date - Feb
        Wtr Order Date - SAT
        Verify that the report contains only those rows that Contain the string value entered.
        """
        """ Expect 180 rows - dates of 19960201 containing '9602' """
        active_report_obj.select_menu_items(table_css, "1", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='9602')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '180of1000records,Page1of4', "Step 2:1: Expect 180 rows - dates of 19960201 containing '9602'")
        active_report_obj.close_filter_dialog()
         
        """ Expect 180 rows - dates of APRIL 1, 1996 containing 'April' """
        active_report_obj.select_menu_items(table_css, "2", selection_type , filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='April')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '180of1000records,Page1of4', "Step 2:2: Expect 180 rows - dates of APRIL 1, 1996 containing 'April'")
        active_report_obj.close_filter_dialog()
         
        """ Expect 100 rows - dates of 96/153 containing '6/15' """
        active_report_obj.select_menu_items(table_css, "3", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='6/15')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '100of1000records,Page1of2', "Step 2:3: Expect 100 rows - dates of 96/153 containing '6/15'")
        active_report_obj.close_filter_dialog()
         
        """ Expect 180 rows - dates of 96/001 containing '96/00' """
        active_report_obj.select_menu_items(table_css, "4", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='96/00')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '180of1000records,Page1of4', "Step 2:4: Expect 180 rows - dates of 96/001 containing '96/00'")
        active_report_obj.close_filter_dialog()
         
        """ Expect 460 rows - dates of Q2 1996 containing 'Q2' """
        active_report_obj.select_menu_items(table_css, "5", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='Q2')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '460of1000records,Page1of9', "Step 2:5: Expect 460 rows - dates of Q2 1996 containing 'Q2'")
        active_report_obj.close_filter_dialog()
         
        """ Expect 100 rows - dates of Saturday, June 1 1996 containing 'june' """
        active_report_obj.select_menu_items(table_css, "6", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='june')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '100of1000records,Page1of2', "Step 2:6: Expect 100 rows - dates of Saturday, June 1 1996 containing 'june'")
        active_report_obj.close_filter_dialog()
 
        """ Expect 180 rows - dates of February containing 'Feb' """
        active_report_obj.select_menu_items(table_css, "7", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='Feb')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '180of1000records,Page1of4', "Step 2:7: Expect 180 rows - dates of February containing 'Feb' ")
        active_report_obj.close_filter_dialog()

        """ Expect 100 rows - dates of Saturday containing 'SAT' """
        active_report_obj.select_menu_items(table_css, "8", selection_type,filter_condition)
        active_report_obj.create_filter(1, filter_condition,value1='SAT')
        active_report_obj.filter_button_click(selection_type)
        active_report_obj.verify_page_summary(0, '100of1000records,Page1of2', "Step 2:8: Expect 100 rows - dates of Saturday containing 'SAT'")
        active_report_obj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()