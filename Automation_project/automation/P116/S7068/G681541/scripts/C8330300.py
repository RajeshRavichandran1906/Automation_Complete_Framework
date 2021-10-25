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

class C8330300_TestClass(BaseTestCase):

    def test_C8330300(self):

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
        Step 2:For the following ALPHA fields, select Filter, then Contains, using the string value:
        Case does NOT matter.
        
        ALPHA ORDER - 00001
        ALPHA ANV - 27
        ALPHA TEXT - 000010
        ALPHA A80 - 00000
        ALPHA Edit - b-1
        ALPHA Store Code - 44
        ALPHA Vendor Code - V082
        ALPHA Vendor Name - Bakeries
        ALPHA Product Code - F1
        ALPHA Product Descr. - COFFEE
        
        Verify that the report contains only those rows that Contain the string value.
        .
        .
        Expect 11 rows - containing '00001' anywhere in the field.
        Expect 20 rows - containing '27' anywhere in the field.
        Expect 1 row - containing '000010' anywhere in the field.
        Expect 9 rows - containing '00000' anywhere in the field.
        Expect 335 rows - containing 'b-1' anywhere in the field.
        Expect 165 rows - containing '44' anywhere in the field.
        Expect 84 rows - containing 'V082' anywhere in the field.
        Expect 183 rows - containing 'Bakeries' anywhere in the field. 
        Expect 331 rows - containing 'F1' anywhere in the field. 
        Expect 133 rows - containing 'Coffee' anywhere in the field.
        """
        
        """ Expect 11 rows - containing '00001' anywhere in the field."""
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='00001')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '11of1000records,Page1of1', "Step 2.1: Expect 11 rows - containing '00001' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA ANV - 27"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='27')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '20of1000records,Page1of1', "Step 2.2: Expect 20 rows - containing '27' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA TEXT - 000010"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='000010')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '1of1000records,Page1of1', "Step 2.3: Expect 1 row - containing '000010' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA A80 - 00000"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='00000')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '9of1000records,Page1of1', "Step 2.4: Expect 9 rows - containing '00000' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Edit - b-1"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='b-1')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '335of1000records,Page1of6', "Step 2.5: Expect 335 rows - containing 'b-1' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Store Code - 44"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='44')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '165of1000records,Page1of3', "Step 2.6: Expect 165 rows - containing '44' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Code - V082"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='V082')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '84of1000records,Page1of2', "Step 2.7: Expect 84 rows - containing 'V082' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Name - Bakeries"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='Bakeries')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '183of1000records,Page1of4', "Step 2.8: Expect 183 rows - containing 'Bakeries' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Code - F1"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='F1')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '331of1000records,Page1of6', "Step 2.9: Expect 331 rows - containing 'F1' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Descr. - COFFEE"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Contains')        
        active_report_obj.create_filter(1, 'Contains',  value1='COFFEE')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '133of1000records,Page1of3', "Step 2.10: Expect 133 rows - containing 'COFFEE' anywhere in the field")
        active_report_obj.close_filter_dialog()


if __name__ == "__main__":
    unittest.main()
    