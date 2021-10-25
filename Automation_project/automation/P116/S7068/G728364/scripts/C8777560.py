'''
Created on Jan 18, 2019

@author: Varun
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8777560
Testcase Name : AHTML: Verify Filter operators against various DATE fields(Part 7)
'''
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report

class C8777560_TestClass(BaseTestCase):

    def test_C8777560(self):

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
        
        """
            CSS
        """
        table_id="ITableData0"
        data_value_css="#{0} tbody tr:nth-child(4) td:nth-child(2)".format(table_id)
        
        """
        Step 1: Execute AR-RP-141DE.fex from below API to produce the decimal output
                Expect to see the following Active Report containing DATE fields.
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=data_value_css, synchronize_visible_element_text='19960101', repository_path=folder_path)
        active_report_obj.verify_page_summary(page_summary_number, expected_page_summary, "Step 1: Expect to see the following Active Report. - page summary verification")
        
        """
        Step 2: For the following DATE fields, select Filter, then Greater than and use these values:
        YYMD Order Date - 19960201
        MTRDYY Order Date - MARCH 1, 1996
        YYJUL Order Date - 1996/001
        JULIAN Order Date - 96/092
        QYY Order Date - Q1 1996 
        wrMtrYY Order Date - Monday, Apr 1 1996
        Mtr Order Date - May
        Wtr Order Date - Wednesday
        
        Verify that the report contains only those rows that are Greater than the selected value.
        Expect 640 rows - later than 19960201
        Expect 460 rows - later than MARCH 1, 1996
        Expect 820 rows - later than 1996/001
        Expect 280 rows - later than 96/092
        Expect 460 rows - later than Q1 1996
        Expect 280 rows - later than Monday, Apr 1 1996
        Expect 100 rows - later than May
        Expect 460 rows - later than Wednesday
        """
        '''Expect 640 rows - later than 19960201'''
        active_report_obj.select_menu_items("ITableData0", "1", "Filter","Greater than")
        active_report_obj.create_filter(1, 'Greater than',value1='19960201')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '640of1000records,Page1of12', "Step 02: Expect 640 rows - later than 19960201")
        active_report_obj.close_filter_dialog()
          
        #Expect 460 rows - later than MARCH 1, 1996
        active_report_obj.select_menu_items("ITableData0", "2", "Filter","Greater than")
        active_report_obj.create_filter(1, 'Greater than',value1='MARCH 1, 1996')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '460of1000records,Page1of9', "Step 02: Expect 460 rows - later than MARCH 1, 1996")
        active_report_obj.close_filter_dialog()
          
        #Expect 820 rows - later than 1996/001
        active_report_obj.select_menu_items("ITableData0", "3", "Filter","Greater than")
        active_report_obj.create_filter(1, 'Greater than',value1='1996/001')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '820of1000records,Page1of15', "Step 02: Expect 820 rows - later than 1996/001")
        active_report_obj.close_filter_dialog()
          
        #Expect 280 rows - later than 96/092
        active_report_obj.select_menu_items("ITableData0", "4", "Filter","Greater than")
        active_report_obj.create_filter(1, 'Greater than',value1='96/092')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '280of1000records,Page1of5', "Step 02: Expect 280 rows - later than 96/092")
        active_report_obj.close_filter_dialog()
          
        #Expect 460 rows - later than Q1 1996
        active_report_obj.select_menu_items("ITableData0", "5", "Filter","Greater than")
        active_report_obj.create_filter(1, 'Greater than',value1='Q1 1996')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '460of1000records,Page1of9', "Step 02: Expect 460 rows - later than Q1 1996")
        active_report_obj.close_filter_dialog()
          
        #Expect 280 rows - later than Monday, Apr 1 1996
        active_report_obj.select_menu_items("ITableData0", "6", "Filter","Greater than")
        active_report_obj.create_filter(1, 'Greater than',value1='Monday, April 1 1996')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '280of1000records,Page1of5', "Step 02: Expect 280 rows - later than Monday, Apr 1 1996")
        active_report_obj.close_filter_dialog()
  
        #Expect 100 rows - later than May
        active_report_obj.select_menu_items("ITableData0", "7", "Filter","Greater than")
        active_report_obj.create_filter(1, 'Greater than',value1='May')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '100of1000records,Page1of2', "Step 02: Expect 100 rows - later than May")
        active_report_obj.close_filter_dialog()
          
        #Expect 460 rows - later than Wednesday
        active_report_obj.select_menu_items("ITableData0", "8", "Filter","Greater than")
        active_report_obj.create_filter(1, 'Greater than',value1='Wednesday')
        active_report_obj.filter_button_click('Filter')
        active_report_obj.verify_page_summary(0, '460of1000records,Page1of9', "Step 02:Expect 460 rows - later than Wednesday")
        active_report_obj.close_filter_dialog()
         
if __name__ == "__main__":
    unittest.main()