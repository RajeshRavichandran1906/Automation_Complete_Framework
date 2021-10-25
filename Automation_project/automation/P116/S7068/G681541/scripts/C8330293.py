'''
Created on Jan 9, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330293
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 6)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report


class C8330293_TestClass(BaseTestCase):

    def test_C8330293(self):

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
        Test_Case_ID="C8330293"
        fex_name="AR-RP-141AL.fex"
        
        """
            CSS
        """
        table_css="ITableData0"
        data_value_css="#"+table_css+" tbody tr:nth-child(4) td:nth-child(2)"
        
        """
        Step 1: Execute AR-RP-141AL.fex from below API to produce the alphanumeric output
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='000001', repository_path=folder_path)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")
    
        """
        Step 2:For the following ALPHA fields, select Filter, then Not Equals and use these values:
        Select the Highlight option for this test.
        After each field Highlight, close the Filter panel for the next field.
        
        ALPHA ORDER - 000001
        ALPHA ANV - 000005 
        ALPHA TEXT - 000010
        ALPHA A80 - 000015 
        ALPHA Edit - G-104 
        ALPHA Store Code - R1020
        
        ALPHA Vendor Code - V102
        
        ALPHA Vendor Name - Thermo Tech, Inc
        
        ALPHA Product Code - G100 
        ALPHA Product Descr. - French Roast

        Verify that the report Highlights only those rows that do Not match the selected values.
        .
        .
        .
        Expect 999 rows highlighted - only value 000001 is not
        Expect 999 rows highlighted - only value 000005 is not 
        Expect 999 rows highlighted - only value 000010 is not
        Expect 999 rows highlighted - only value 000015 is not
        Expect only G-104 rows Not highlighted, page down to verify
        Expect only R1020 rows Not highlighted, page down to verify
        Expect only V102 rows Not highlighted, page down to verify
        Expect only Thermo Tech, Inc rows Not highlighted, page down to verify
        Expect only G100 rows Not highlighted, page down to verify
        Expect only French Roast rows Not highlighted, page down to verify
        """

        """Expect 999 rows highlighted - only value 000001 is not"""
        active_report_obj.select_menu_items(table_css, "1", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal', 'large', value1='000001')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds01.xlsx',"Step 2:01: Expect 1 row highlighted - value 000001")
        active_report_obj.close_filter_dialog()
        
        """Expect 999 rows highlighted - only value 000005 is not"""
        active_report_obj.select_menu_items(table_css, "2", "Filter" , "Not equal")
        active_report_obj.create_filter(1, 'Not equal','large',value1='000005')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds02.xlsx',"Step 2:02: Expect 999 rows highlighted - only value 000005 is not")
        active_report_obj.close_filter_dialog()
        
        """Expect 999 rows highlighted - only value 000010 is not"""
        active_report_obj.select_menu_items(table_css, "3", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal','large',value1='000010')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds03.xlsx',"Step 2:03: Expect 999 rows highlighted - only value 000010 is not")
        active_report_obj.close_filter_dialog()
        
        """Expect 999 rows highlighted - only value 000015 is not"""
        active_report_obj.select_menu_items(table_css, "4", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal','large',value1='000015')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds04.xlsx',"Step 2:04: Expect 999 rows highlighted - only value 000015 is not")
        active_report_obj.close_filter_dialog()
        
        """Expect only G-104 rows Not highlighted, page down to verify"""
        active_report_obj.select_menu_items(table_css, "5", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='G-104')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds05.xlsx',"Step 2:05: Expect only G-104 rows Not highlighted, page down to verify")
        active_report_obj.close_filter_dialog()
        
        """Expect only R1020 rows Not highlighted, page down to verify"""
        active_report_obj.select_menu_items(table_css, "6", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='R1020')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds06.xlsx',"Step 2:06: Expect only R1020 rows Not highlighted, page down to verify")
        active_report_obj.close_filter_dialog()
        
        """ Expect only V102 rows Not highlighted, page down to verify"""
        active_report_obj.select_menu_items(table_css, "7", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='V102')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds07.xlsx',"Step 2:07: Expect only V102 rows Not highlighted, page down to verify")
        active_report_obj.close_filter_dialog()
        
        """ Expect only Thermo Tech, Inc rows Not highlighted, page down to verify"""
        active_report_obj.select_menu_items(table_css, "8", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='ThermoTech, Inc')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds08.xlsx',"Step 2:08: Expect only Thermo Tech, Inc rows Not highlighted, page down to verify")
        active_report_obj.close_filter_dialog()
        
        """ Expect only G100 rows Not highlighted, page down to verify"""
        active_report_obj.select_menu_items(table_css, "9", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='G100')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds09.xlsx',"Step 2:09: Expect only G100 rows Not highlighted, page down to verify")
        active_report_obj.close_filter_dialog()

        """ Expect only French Roast rows Not highlighted, page down to verify"""
        active_report_obj.select_menu_items(table_css, "10", "Filter","Not equal")
        active_report_obj.create_filter(1, 'Not equal',value1='French Roast')
        active_report_obj.filter_button_click('Highlight')
        active_report_obj.verify_data_set_using_table_rowid(table_css,'rgb',Test_Case_ID+'_Ds10.xlsx',"Step 2:10: Expect only French Roast rows Not highlighted, page down to verify")
        active_report_obj.close_filter_dialog()


if __name__ == "__main__":
    unittest.main()