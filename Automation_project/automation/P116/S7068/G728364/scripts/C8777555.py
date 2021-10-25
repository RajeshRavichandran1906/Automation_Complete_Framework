'''
Created on Jan 18, 2019

@author: Magesh

Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8777555
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 2)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777555_TestClass(BaseTestCase):

    def test_C8777555(self):

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
        Test_Case_ID="C8777555"
        fex_name="AR-RP-141DA.fex"
        expected_page_summary = '1000of1000records,Page1of18'
        page_summary_number = '0'
        
        """
        COMMON CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute the attached AR-RP-141DA.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='19960101', repository_path=folder_path)
        
        """
        Step 1.1: Expect to see the following Active Report of DATE fields
        """
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary, "Step 1.01: Expect to see the following Active Report page summary verification")
        
        """
        Step 2: For the following DATE fields, select Filter, then Equals and use these values:
        YYMD Order Date - 19960201 & 1996061
        MTRDYY Order Date - MARCH 1, 1996 & APRIL 1, 1996
        YYJUL Order Date - 1996/001 & 1996/061 & 1996/122
        JULIAN Order Date - 96/032 & 96/061
        QYY Order Date - Q1 1996 & Q2 1996
        wrMtrYY Order Date - Thursday, February 1 1996 & Monday, April 1 1996
        Mtr Order Date - January & February
        Wtr Order Date - Thursday & Friday

        Step 2.1: Verify that the report contains only those rows that match the selected values.
        Expect 280 rows - values 19960201 & 19960601
        Expect 360 rows - values MARCH 1, 1996 & APRIL 1, 1996
        Expect 540 rows - values 1996/001 & 1996/061 & 1996/122
        Expect 360 rows - values 96/032 & 96/061
        Expect 1000 rows - values Q1 1996 & Q2 1996
        Expect 360 rows - values Thursday, February 1 1996 & Monday, April 1 1996
        Expect 360 rows - values January & February
        Expect 360 rows - values Thursday & Friday
        """
        
        '''Expect 280 rows - values 19960201 & 19960601'''
        active_report_obj.select_menu_items(table_id, "1", "Filter", "Equals")
        active_report_obj.create_filter(1, 'Equals', value1='19960201', value2='19960601')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '280of1000records,Page1of5', "Step 02.1: Expect 280 rows - values 19960201 & 19960601")
        active_report_obj.close_filter_dialog()
           
        '''Expect 360 rows - values MARCH 1, 1996 & APRIL 1, 1996'''
        active_report_obj.select_menu_items(table_id, "2", "Filter", "Equals")
        active_report_obj.create_filter(1, 'Equals', value1='MARCH 1, 1996', value2='APRIL 1, 1996')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '360of1000records,Page1of7', "Step 02.2: Expect 360 rows - values MARCH 1, 1996 & APRIL 1, 1996")
        active_report_obj.close_filter_dialog()
           
        '''Expect 540 rows - values 1996/001 & 1996/061 & 1996/122'''
        active_report_obj.select_menu_items(table_id, "3", "Filter", "Equals")
        active_report_obj.create_filter(1, 'Equals', value1='1996/001', value2='1996/061', value3='1996/122')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '540of1000records,Page1of10', "Step 02.3: Expect 540 rows - values 1996/001 & 1996/061 & 1996/122")
        active_report_obj.close_filter_dialog()
           
        '''Expect 360 rows - values 96/032 & 96/061'''
        active_report_obj.select_menu_items(table_id, "4", "Filter", "Equals")
        active_report_obj.create_filter(1, 'Equals', value1='96/032', value2='96/061')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '360of1000records,Page1of7', "Step 02.4: Expect 360 rows - values 96/032 & 96/061")
        active_report_obj.close_filter_dialog()
          
        '''Expect 1000 rows - values Q1 1996 & Q2 1996'''
        active_report_obj.select_menu_items(table_id, "5", "Filter", "Equals")
        active_report_obj.create_filter(1, 'Equals', value1='Q1 1996', value2='Q2 1996')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 02.5: Expect 1000 rows - values Q1 1996 & Q2 1996")
        active_report_obj.close_filter_dialog()
          
        '''Expect 360 rows - values Thursday, February 1 1996 & Monday, April 1 1996'''
        active_report_obj.select_menu_items(table_id, "6", "Filter", "Equals")
        active_report_obj.create_filter(1, 'Equals', value1='Thursday, February 1 1996', value2='Monday, April 1 1996')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '360of1000records,Page1of7', "Step 02.6: Expect 360 rows - values Thursday, February 1 1996 & Monday, April 1 1996")
        active_report_obj.close_filter_dialog()
  
        '''Expect 360 rows - values January & February'''
        active_report_obj.select_menu_items(table_id, "7", "Filter", "Equals")
        active_report_obj.create_filter(1, 'Equals', value1='January', value2='February')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '360of1000records,Page1of7', "Step 02.7: Expect 360 rows - values January & February")
        active_report_obj.close_filter_dialog()
          
        '''Expect 360 rows - values Thursday & Friday'''
        active_report_obj.select_menu_items(table_id, "8", "Filter", "Equals")
        active_report_obj.create_filter(1, 'Equals', value1='Thursday', value2='Friday')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '360of1000records,Page1of7', "Step 02.8: Expect 360 rows - values Thursday & Friday")
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()