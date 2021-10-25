'''
Created on Jan 16, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330302&group_by=cases:section_id&group_id=681541&group_order=asc
Testcase Name :  AHTML: Verify Filter operators against various Alphanumeric fields(Part 15)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8330302_TestClass(BaseTestCase):

    def test_C8330302(self):

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
        Step 2: For the following ALPHA fields, select Filter, then Omits, using the string value:
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
        """
        active_report_obj.select_menu_items(table_css, 1, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='00001')
        active_report_obj.filter_button_click('Filter')
        """ Expect 989 rows - omitting '00001' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '989of1000records,Page1of18', "Step 2.1: Expect 989 rows - containing '00001' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA ANV - 27"""
        active_report_obj.select_menu_items(table_css, 2, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='27')
        active_report_obj.filter_button_click('Filter')
        """ Expect 980 rows - omitting '27' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '980of1000records,Page1of18', "Step 2.2: Expect 980 rows - containing '27' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA TEXT - 000010"""
        active_report_obj.select_menu_items(table_css, 3, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='000010')
        active_report_obj.filter_button_click('Filter')
        """ Expect 999 rows - omitting '000010' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '999of1000records,Page1of1', "Step 2.3: Expect 999 row - containing '000010' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA A80 - 00000"""
        active_report_obj.select_menu_items(table_css, 4, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='00000')
        active_report_obj.filter_button_click('Filter')
        """ Expect 991 rows - omitting '00000' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '991of1000records,Page1of18', "Step 2.4: Expect 991 rows - containing '00000' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Edit - b-1"""
        active_report_obj.select_menu_items(table_css, 5, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='b-1')
        active_report_obj.filter_button_click('Filter')
        """ Expect 665 rows - omitting 'b-1' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '665of1000records,Page1of12', "Step 2.5: Expect 665 rows - containing 'b-1' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Store Code - 44"""
        active_report_obj.select_menu_items(table_css, 6, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='44')
        active_report_obj.filter_button_click('Filter')
        """ Expect 835 rows - omitting '44' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '835of1000records,Page1of15', "Step 2.6: Expect 835 rows - containing '44' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Code - V082"""
        active_report_obj.select_menu_items(table_css, 7, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='V082')
        active_report_obj.filter_button_click('Filter')
        """Expect 916 rows - omitting 'V082' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '916of1000records,Page1of17', "Step 2.7: Expect 916 rows - containing 'V082' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Vendor Name - Bakeries"""
        active_report_obj.select_menu_items(table_css, 8, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='Bakeries')
        active_report_obj.filter_button_click('Filter')
        """ Expect 817 rows - omitting 'Bakeries' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '817of1000records,Page1of15', "Step 2.8: Expect 817 rows - containing 'Bakeries' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Code - F1"""
        active_report_obj.select_menu_items(table_css, 9, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='F1')
        active_report_obj.filter_button_click('Filter')
        """ Expect 669 rows - omitting 'F1' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '669of1000records,Page1of12', "Step 2.9: Expect 669 rows - containing 'F1' anywhere in the field")
        active_report_obj.close_filter_dialog()
        
        """ALPHA Product Descr. - COFFEE"""
        active_report_obj.select_menu_items(table_css, 10, 'Filter','Omits')        
        active_report_obj.create_filter(1, 'Omits',  value1='COFFEE')
        active_report_obj.filter_button_click('Filter')
        """ Expect 867 rows - omitting 'COFFEE' anywhere in the field."""
        active_report_obj.verify_page_summary(0, '867of1000records,Page1of16', "Step 2.10: Expect 867 rows - containing 'COFFEE' anywhere in the field")
        active_report_obj.close_filter_dialog()
        


if __name__ == "__main__":
    unittest.main()