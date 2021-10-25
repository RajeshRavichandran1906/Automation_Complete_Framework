'''
Created on Jan 15, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330300&group_by=cases:section_id&group_order=asc&group_id=681541
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 13)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8330301_TestClass(BaseTestCase):

    def test_C8330301(self):

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
        fex_name="AR-RP-141AL.fex"
        
        """
            CSS
        """
        table_css="ITableData0"
        data_value_css="#"+table_css+" tbody tr:nth-child(4) td:nth-child(2)"
        
        """
        Step 1:Execute AR-RP-141AL.fex from below API to produce the alphanumeric output
        Expect to see the following Active Report.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='000001', repository_path=folder_path)
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following ALPHA fields, select Filter, then Contains, using the Case matching string value:
        .
        .
        ALPHA Edit - b-1
        ALPHA Edit - B-1
        ALPHA Store Code - r1019
        ALPHA Store Code - R1019
        ALPHA Vendor Code - V303
        ALPHA Vendor Name - BAKERIES
        
        ALPHA Vendor Name - Bakeries
        
        ALPHA Product Code - f101
        ALPHA Product Code - F101
        ALPHA Product Descr. - cr
        ALPHA Product Descr. - Cr
        
        Verify that the report contains only those rows that Contain the string value.
        Case does not apply to fields with numeric digits only.
        
        """
        """ ALPHA Edit - b-1 """
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='b-1')
        active_report_obj.filter_button_click('Filter')
        """ Expect 0 rows - containing 'b-1' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 2.1: Expect 0 rows - containing 'b-1' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Edit - B-1"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='B-1')
        active_report_obj.filter_button_click('Filter')
        """ Expect 335 rows - containing 'B-1' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '335of1000records,Page1of6', "Step 2.2: Expect 335 rows - containing 'B-1' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Store Code - r1019    """
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='r1019')
        active_report_obj.filter_button_click('Filter')
        """ Expect 0 rows - containing 'r1019' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 2.3: Expect 0 rows - containing 'r1019' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Store Code - R1019    """
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='R1019')
        active_report_obj.filter_button_click('Filter')
        """ Expect 90 rows - containing 'R1019' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '90of1000records,Page1of2', "Step 09.4: Expect 90 rows - containing 'R1019' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Code - V303"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='V303')
        active_report_obj.filter_button_click('Filter')
        """ Expect 66 rows - containing 'V303' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '66of1000records,Page1of2', "Step 09.5: Expect 66 rows - containing 'V303' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Name - BAKERIES"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='BAKERIES')
        active_report_obj.filter_button_click('Filter')
        """ Expect 0 rows - containing 'BAKERIES' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09.6: Expect 0 rows - containing 'BAKERIES' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Name - Bakeries"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='Bakeries')
        active_report_obj.filter_button_click('Filter')
        """ Expect 183 rows - containing 'Bakeries' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '183of1000records,Page1of4', "Step 09.7: Expect 183 rows - containing 'Bakeries' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Code - f101"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='f101')
        active_report_obj.filter_button_click('Filter')
        """ Expect 0 rows - containing 'f101' anywhere in the field. """
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09.8: Expect 0 rows - containing 'f101' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Code - F101"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='F101')
        active_report_obj.filter_button_click('Filter')
        """ Expect 84 rows - containing 'F101' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '84of1000records,Page1of2', "Step 09.9: Expect 84 rows - containing 'F101' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Descr. - cr"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='cr')
        active_report_obj.filter_button_click('Filter')
        """ Expect 0 rows - containing 'cr' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '0of1000records,Page1of1', "Step 09.10: Expect 0 rows - containing 'cr' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Descr. - Cr"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Contains (match case)')        
        active_report_obj.create_filter(1, 'Contains (match case)',  value1='Cr')
        active_report_obj.filter_button_click('Filter')
        """ Expect 148 rows - containing 'Cr' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '148of1000records,Page1of3', "Step 09.11: Expect 148 rows - containing 'Cr' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        
if __name__ == '__main__':
    unittest.main()     
        
        
        