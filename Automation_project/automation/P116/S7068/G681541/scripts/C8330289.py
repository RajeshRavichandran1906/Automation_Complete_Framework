'''
Created on Jan 8, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8330289&group_by=cases:section_id&group_id=681541&group_order=asc
Testcase Name : AHTML: Verify Filter operators against various Alphanumeric fields(Part 2)
'''
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.pages import active_filter_selection
from common.lib import utillity
import unittest
from common.wftools.active_report import Active_Report


class C8330289_TestClass(BaseTestCase):

    def test_C8330289(self):

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
        
        Test_Case_ID = 'C8330289'
        fex_name="AR-RP-141AL.fex"
        
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
        utillobj.synchronize_with_visble_text(data_value_css, '000001', miscelanousobj.home_page_medium_timesleep)

        """
        Step 2:For the following ALPHA fields, select Filter, then Equals and use these multiple values:
        ALPHA ORDER - 000001 & 000005
        ALPHA ANV - 000010 & 000015
        ALPHA TEXT - 000020 & 000025
        ALPHA A80 - 000030 & 000035
        ALPHA Edit - B-141, B-142 & B-144
        ALPHA Store Code - R1100 & R1109
        ALPHA Vendor Code - V081, V100 & V303
        ALPHA Vendor Name - Coffee Connection & Thermo Tech, Inc
        ALPHA Product Code - B144, F101 & G121
        ALPHA Product Descr. - Coffee Grinder & Coffee Pot

        Verify that the report contains only those rows that match the selected value.

        Expect 2 rows - value 000001 & 000005
        Expect 2 rows - value 000010 & 000015
        Expect 2 rows - value 000020 & 000025
        Expect 2 rows - value 000030 & 000035
        Expect 335 rows - value B-141, B-142 & B-144
        Expect 161 rows - value R1100 & R1109
        Expect 198 rows - value V081, V100 & V303
        Expect 151 rows - value Coffee Connection & Thermo Tech, Inc
        Expect 184 rows - value B144, F101 & G121
        Expect 133 rows - value Coffee Grinder & Coffee Pot
        """
        # Expect 2 rows - value 000001 & 000005
          
        miscelanousobj.select_menu_items("ITableData0", "1", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000001', value2='000005')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 2:01: Expect 2 rows - value 000001 & 000005")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds01.xlsx", table_css=table_css)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds01.xlsx", "Step 2:02: Verify report data set", table_css=table_css, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 2 rows - value 000010 & 000015
        miscelanousobj.select_menu_items("ITableData0", "2", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000010',value2='000015')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 2:03: Expect 2 rows - value 000010 & 000015")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds02.xlsx", table_css=table_css,desired_no_of_rows=5,starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds02.xlsx", "Step 2:04: Verify report data set", table_css=table_css,desired_no_of_rows=5,starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 2 rows - value 000020 & 000025
        miscelanousobj.select_menu_items("ITableData0", "3", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000020', value2='000025')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 2:05: Expect 2 rows - value 000020 & 000025")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds03.xlsx", table_css=table_css,desired_no_of_rows=5,starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds03.xlsx", "Step 2:06: Verify report data set", table_css=table_css,desired_no_of_rows=5,starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 2 rows - value 000030 & 000035
          
        miscelanousobj.select_menu_items("ITableData0", "4", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals','large',value1='000030', value2='000035')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '2of1000records,Page1of1', "Step 2:07: Expect 2 rows - value 000030 & 000035")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds04.xlsx", table_css=table_css,desired_no_of_rows=5,starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds04.xlsx", "Step 2:08: Verify report data set", table_css=table_css,desired_no_of_rows=5,starting_rownum=2)
        
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        #Expect 335 rows - value B-141, B-142 & B-144
          
        miscelanousobj.select_menu_items("ITableData0", "5", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='B-141', value2='B-142', value3='B-144')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '335of1000records,Page1of6', "Step 2:09: Expect 335 rows - value B-141, B-142 & B-144")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds05.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds05.xlsx", "Step 2:10: Verify report data set", table_css=table_css,desired_no_of_rows=5, starting_rownum=2)
        
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        #Expect 161 rows - value R1100 & R1109
          
        miscelanousobj.select_menu_items("ITableData0", "6", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='R1100', value2='R1109')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '161of1000records,Page1of3', "Step 2:11: Expect 161 rows - value R1100 & R1109")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds06.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds06.xlsx", "Step 2:12: Verify report data set", table_css=table_css,desired_no_of_rows=5, starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
          
        #Expect 198 rows - value V081, V100 & V303
          
        miscelanousobj.select_menu_items("ITableData0", "7", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='V081', value2='V100', value3='V303')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '198of1000records,Page1of4', "Step 2:13: Expect 198 rows - value V081, V100 & V303")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds07.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds07.xlsx", "Step 2:14: Verify report data set", table_css=table_css,desired_no_of_rows=5, starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        # Expect 151 rows - value Coffee Connection & Thermo Tech, Inc
          
        miscelanousobj.select_menu_items("ITableData0", "8", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='Coffee Connection',value2='ThermoTech, Inc')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '151of1000records,Page1of3', "Step 2:15: Expect 151 rows - value Coffee Connection & Thermo Tech, Inc")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds08.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=2)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds08.xlsx", "Step 2:16: Verify report data set", table_css=table_css,desired_no_of_rows=5, starting_rownum=2)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
          
        # Expect 184 rows - value B144, F101 & G121
          
        miscelanousobj.select_menu_items("ITableData0", "9", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='B144',value2='F101',value3='G121')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '184of1000records,Page1of4', "Step 2:17: Expect 134 rows - value G100")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds09.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds09.xlsx", "Step 2:18: Verify report data set", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
  
        # Expect 133 rows - value Coffee Grinder & Coffee Po
          
        miscelanousobj.select_menu_items("ITableData0", "10", "Filter","Equals")
          
        filterselectionobj.create_filter(1, 'Equals',value1='Coffee Grinder',value2='Coffee Pot')
        #time.sleep(3)
        filterselectionobj.filter_button_click('Filter')
        #time.sleep(3)
          
        miscelanousobj.verify_page_summary(0, '133of1000records,Page1of3', "Step 2:19: Expect 133 rows - value Coffee Grinder & Coffee Po")
#         active_report_obj.create_active_report_dataset(Test_Case_ID+"_Ds10.xlsx", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        active_report_obj.verify_active_report_dataset(Test_Case_ID+"_Ds10.xlsx", "Step 2:20: Verify report data set", table_css=table_css,desired_no_of_rows=5, starting_rownum=1)
        #time.sleep(5)
        filterselectionobj.close_filter_dialog()
        

if __name__ == "__main__":
    unittest.main()