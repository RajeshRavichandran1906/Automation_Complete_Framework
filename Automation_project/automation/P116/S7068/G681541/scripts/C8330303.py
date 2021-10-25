'''
Created on Jan 16, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330303
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 16)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8330303_TestClass(BaseTestCase):

    def test_C8330303(self):

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
        Step 2: For the following ALPHA fields, select Filter, then Omits, using the Case matching string value:
        Case does not apply to fields with numeric digits only.
        
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
        .
        . 
        """
        """ALPHA Edit - b-1"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='b-1')
        active_report_obj.filter_button_click('Filter')
        """ Expect 1000 rows - omitting 'b-1' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 2.1: Expect 100 rows - containing 'b-1' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Edit - B-1"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='B-1')
        active_report_obj.filter_button_click('Filter')
        """ Expect 665 rows - omitting 'B-1' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '665of1000records,Page1of12', "Step 2.2: Expect 665 rows - containing 'B-1' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Store Code - r1019    """
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='r1019')
        active_report_obj.filter_button_click('Filter')
        """ Expect 1000 rows - omitting 'r1019' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 2.3: Expect 1000 rows - containing 'r1019' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Store Code - R1019    """
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='R1019')
        active_report_obj.filter_button_click('Filter')
        """ Expect 910 rows - omitting 'R1019' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '910of1000records,Page1of16', "Step 2.4: Expect 910 rows - containing 'R1019' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Code - V303"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='V303')
        active_report_obj.filter_button_click('Filter')
        """ Expect 934 rows - omitting 'V303' anywhere in the field. """
        active_report_obj.verify_page_summary(0, '934of1000records,Page1of17', "Step 2.5: Expect 934 rows - containing 'V303' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Name - BAKERIES"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='BAKERIES')
        active_report_obj.filter_button_click('Filter')
        """ Expect 1000 rows - omitting 'BAKERIES' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 2.6: Expect 1000 rows - containing 'BAKERIES' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Name - Bakeries"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='Bakeries')
        active_report_obj.filter_button_click('Filter')
        """ Expect 817 rows - omitting 'Bakeries' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '817of1000records,Page1of15', "Step 2.7: Expect 817 rows - containing 'Bakeries' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Code - f101"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='f101')
        active_report_obj.filter_button_click('Filter')
        """ Expect 1000 rows - omitting 'f101' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 2.8: Expect 0 rows - containing 'f101' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Code - F101"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='F101')
        active_report_obj.filter_button_click('Filter')
        """ Expect 916 rows - omitting 'F101' anywhere in the field. """
        active_report_obj.verify_page_summary(0, '916of1000records,Page1of17', "Step 2.9: Expect 916 rows - containing 'F101' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Descr. - cr"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='cr')
        active_report_obj.filter_button_click('Filter')
        """ Expect 1000 rows - omitting 'cr' anywhere in the field. """
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 2.10: Expect 1000 rows - containing 'cr' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Descr. - Cr"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Omits (match case)')        
        active_report_obj.create_filter(1, 'Omits (match case)',  value1='Cr')
        active_report_obj.filter_button_click('Filter')
        """ Expect 852 rows - containing 'Cr' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '852of1000records,Page1of15', "Step 2.11: Expect 852 rows - containing 'Cr' anywhere in the field")
        active_report_obj.close_filter_dialog()


if __name__ == "__main__":
    unittest.main()