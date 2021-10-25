'''
Created on Jan 7, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330288&group_by=cases:section_id&group_order=asc&group_id=681541
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 1)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.pages import active_filter_selection
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report


class C8330288_TestClass(BaseTestCase):

    def test_C8330288(self):

        """
           CLASS OBJECTS
        """ 
        
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        filterselectionobj = active_filter_selection.Active_Filter_Selection(self.driver)
        active_report_obj=Active_Report(self.driver)
        
        """
            TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C8330288'
        fex_name="AR-RP-141AL.fex"
        long_wait=60
        
        """
            CSS
        """
        table_css="#ITableData0"
        data_value_css=table_css+" tbody tr:nth-child(4) td:nth-child(2)"
        
        """
            Step 01:Execute AR-RP-141AL to produce the alphanumeric output..
        """
        utillobj.active_run_fex_api_login(fex_name, "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(data_value_css, '000001', long_wait)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds01.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds01.xlsx", "Step 1:02: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
          
        """Step 02 : For the following ALPHA fields, select Filter, then Equals and use these values:
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
        """
          
        #Expect 1 row - value 000001
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000001')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 2:01: Expect 1 row - value 000001")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds02.xlsx", table_css=table_css,desired_no_of_rows=4,starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds02.xlsx", "Step 2:02: Verify report dataset", table_css=table_css,desired_no_of_rows=4,starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        #Expect 1 row - value 000005
          
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 2:03: Expect 1 row - value 000005")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds03.xlsx", table_css=table_css,desired_no_of_rows=4,starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds03.xlsx", "Step 2:04: Verify report dataset", table_css=table_css,desired_no_of_rows=4,starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 1 row - value 000010
          
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
           
        filterselectionobj.create_filter(1, 'Equals','large',value1='000010')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
           
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 2:05: Expect 1 row - value 000010")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds04.xlsx", table_css=table_css,desired_no_of_rows=4,starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds04.xlsx", "Step 2:06: Verify report dataset", table_css=table_css,desired_no_of_rows=4,starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog() 
          
        # Expect 1 row - value 000015
          
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large', value1='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '1of1000records,Page1of1', "Step 2:07: Expect 1 row - value 000015")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds05.xlsx", table_css=table_css,desired_no_of_rows=4,starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds05.xlsx", "Step 2:08: Verify report dataset", table_css=table_css,desired_no_of_rows=4,starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 67 row - value G-104 
          
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='G-104')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '67of1000records,Page1of2', "Step 2:09: Expect 67 row - value G-104 ")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds06.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds06.xlsx", "Step 2:10: Verify report dataset", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 90 rows - value R1020
          
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='R1020')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '90of1000records,Page1of2', "Step 2:11: Expect 90 rows - value R1020")
        #time.sleep(5)
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds07.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds07.xlsx", "Step 2:12: Verify report dataset", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        filterselectionobj.close_filter_dialog()

        #Expect 84 rows - value V102
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='V102')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '84of1000records,Page1of2', "Step 2:13: Expect 84 rows - value V102")
        #time.sleep(5)
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds08.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds08.xlsx", "Step 2:14: Verify report dataset", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        filterselectionobj.close_filter_dialog()
          
        # Expect 67 rows - value Thermo Tech, Inc
          
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '67of1000records,Page1of2', "Step 2:15: Expect 90 rows - value R1020")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds09.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds09.xlsx", "Step 2:16: Verify report dataset", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
    
        # Expect 134 rows - value G100
          
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='G100')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '134of1000records,Page1of3', "Step 2:17: Expect 134 rows - value G100")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds10.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds10.xlsx", "Step 2:18: Verify report dataset", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
  
        # Expect 218 rows - value French Roast
          
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='French Roast')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '218of1000records,Page1of4', "Step 2:19: Expect 218 rows - value French Roast")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds11.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds11.xlsx", "Step 2:20: Verify report dataset", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()