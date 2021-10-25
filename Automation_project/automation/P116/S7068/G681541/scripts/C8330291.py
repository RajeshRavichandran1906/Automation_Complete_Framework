'''
Created on Jan 8, 2019

@author: BM13368
Testcase ID :
Testcase Name :
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.pages import active_filter_selection
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report


class C8330291_TestClass(BaseTestCase):

    def test_C8330291(self):

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
        
        Test_Case_ID = 'C8330291'
        fex_name="AR-RP-141AL.fex"
        long_wait=60
        
        """
            CSS
        """
        table_css="#ITableData0"
        data_value_css=table_css+" tbody tr:nth-child(4) td:nth-child(2)"
        
        """
        Step 1:Execute AR-RP-141AL.fex from below API to produce the alphanumeric output
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S7068/G146859&BIP_item=AR-RP-141AL.fex
        Expect to see the following Active Report.
        """
        utillobj.active_run_fex_api_login(fex_name, "S7068", 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text(data_value_css, '000001', long_wait)
        miscelanousobj.verify_page_summary(0, '1000of1000records,Page1of18', "Step 1:01: Expect to see the following Active Report. - page summary verification")

        """
        Step 2:For the following ALPHA fields, select Filter, then Not equal and use these values:

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

        Verify that the report contains only those rows that do Not match the selected value.
        .
        Expect 999 rows - not value 000001
        Expect 999 rows - not value 000005
        Expect 999 rows - not value 000010
        Expect 999 rows - not value 000015
        Expect 933 rows - not value G-104
        Expect 910 rows - not value R1020
        Expect 916 rows - not value V102
        Expect 933 rows - not value Thermo Tech, Inc
        Expect 866 rows - not value G100
        Expect 782 rows - not value French Roast
        """
        #Expect 999 rows - not value 000001
         
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large', value1='000001')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 2:01: Expect 999 rows - not value 000001")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds01.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds01.xlsx", "Step 2:02: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 999 rows - not value 000005
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter" ,"Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large',value1='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 2:03: Expect 999 rows - not value 000005")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds02.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds02.xlsx", "Step 2:04: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
        #Expect 999 rows - not value 000010
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large', value1='000010')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 2:05: Expect 999 rows - not value 0000102")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds03.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds03.xlsx", "Step 2:06: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 999 rows - not value 000015
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal','large', value1='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '999of1000records,Page1of18', "Step 2:07: Expect 418 rows - value (81.00)")
        #time.sleep(5)
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds04.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds04.xlsx", "Step 2:08: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        filterselectionobj.close_filter_dialog()
        #Expect 933 rows - not value G-104
         
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='G-104')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '933of1000records,Page1of17', "Step 2:09: Expect 933 rows - not value G-104")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds05.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds05.xlsx", "Step 2:10: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        
        #Expect 910 rows - not value R1020
         
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='R1020')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '910of1000records,Page1of16', "Step 2:11: Expect 910 rows - not value R1020")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds06.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds06.xlsx", "Step 2:12: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        
        #Expect 916 rows - not value V102
         
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='V102')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '916of1000records,Page1of17', "Step 05: Expect 916 rows - not value V102")
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
         
         
        # Expect 933 rows - not value Thermo Tech, Inc
         
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '933of1000records,Page1of17', "Step 2:13: Expect 933 rows - not value Thermo Tech, Inc")
        #time.sleep(5)
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds07.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds07.xlsx", "Step 2:14: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        filterselectionobj.close_filter_dialog()
         
        # Expect 866 rows - not value G100
         
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='G100')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
         
        miscelanousobj.verify_page_summary(0, '866of1000records,Page1of16', "Step 2:15: Expect 866 rows - not value G100")
        #time.sleep(5)
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds08.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds08.xlsx", "Step 2:16: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        filterselectionobj.close_filter_dialog()
 
        #  Expect 782 rows - not value French Roast
         
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Not equal")
         
        filterselectionobj.create_filter(1, 'Not equal',value1='French Roast')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
        miscelanousobj.verify_page_summary(0, '782of1000records,Page1of14', "Step 2:17: Expect 782 rows - not value French Roast")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds09.xlsx", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds09.xlsx", "Step 2:18: Verify report data set", table_css=table_css, desired_no_of_rows=5, starting_rownum=1)
         
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()


if __name__ == "__main__":
    unittest.main()