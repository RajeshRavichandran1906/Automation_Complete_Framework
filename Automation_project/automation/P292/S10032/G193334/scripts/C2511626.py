'''
Created on Jun 25, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2511626&group_by=cases:section_id&group_id=193334&group_order=asc
Testcase Name : Report-Other: Verify that drop-down menu options from second report does not cause any errors.(82xx)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,active_filter_selection, ia_run
from common.lib import utillity, core_utility
from common.wftools import active_report
from common.lib.global_variables import Global_variables

class C2511626_TestClass(BaseTestCase):

    def test_C2511626(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2511626'
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj=core_utility.CoreUtillityMethods(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        filterobj=active_filter_selection.Active_Filter_Selection(self.driver)
        iarun_obj = ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name = "ahtmltab.fex"
        
        """        
            Step 01:Sign in to WebFOCUS 
            http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G193334
            Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G193334%252FAHTMLON&BIP_item=ahtmltab.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="COUNTRY")
        Global_variables.current_working_area_browser_y=self.driver.execute_script('return screen.availHeight - window.innerHeight')
        
        """
           Step 03 : Verify the report is generated.
        """
        expected_list=[['COUNTRY', 'SALES', 'CAR', 'SALES', 'BODYTYPE', 'SALES'],['COUNTRY', 'CAR', 'BODYTYPE', 'SALES'],['COUNTRY', 'Country Sales', 'CAR', 'Company Sales'],['SALES', 'CAR', 'BODYTYPE', 'MODEL', 'FUEL_CAP', 'DEALER_COST', 'DEALER_COST', 'DEALER_COST', 'DEALER_COST', 'DEALER_COST', 'DEALER_COST', 'DEALER_COST', 'DEALER_COST', 'DEALER_COST', 'DEALER_COST']]
        miscelanousobj.verify_column_heading('ITableData0', expected_list[0], msg='Step 3.1 : Verify column heading')
        miscelanousobj.verify_column_heading('ITableData1', expected_list[1], msg='Step 3.2 : Verify column heading')
        miscelanousobj.verify_column_heading('ITableData2', expected_list[2], msg='Step 3.3 : Verify column heading')
        miscelanousobj.verify_column_heading('ITableData3', expected_list[3], msg='Step 3.4 : Verify column heading')
         
        miscelanousobj.verify_page_summary(0, '13of13records,Page1of1', "Step 3.5:  13of13records,Page1of1 Active Report. - page summary verification of table 1")
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', "Step 3.6:  18of18records,Page1of1 Active Report. - page summary verification of table 2")
        miscelanousobj.verify_page_summary(2, '10of10records,Page1of1', "Step 3.7:  10of10records,Page1of1 Active Report. - page summary verification of table 3")
        miscelanousobj.verify_page_summary(3, '18of18records,Page1of1', "Step 3.8:  18of18records,Page1of1 Active Report. - page summary verification of table 4")
        
        """
            Verify correct output displayed on run.
            All four ahtml reports appear on the same output report: 
            Multiverb Report, Simple by Report, Across Test, SubTotal Test.  
        """
        table_css="#ITableData0"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx", "Step 01:01::Verify first report data")
#         utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds01.xlsx")
        table_css="#ITableData1"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx", "Step 01:02::Verify second report data")
#         utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds02.xlsx")
        table_css="#ITableData2"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds03.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds03.xlsx", "Step 01:03::Verify third report data")
#         utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds03.xlsx")
        table_css="#ITableData3"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds04.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds04.xlsx", "Step 01:04::Verify four report data")
#         utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds04.xlsx")
        
        """
            Step 04 : Click on the Country drop-down option on 2nd report
            Verify the column heading drop-down shows report menu options correctly.
        """
        ele=self.driver.find_element_by_css_selector("#ITableData1 #popid1_0 img")
        core_utillobj.left_click(ele)
        time.sleep(1)
        
        list_obj = self.driver.find_elements_by_css_selector("#dt1_0_0 >table>tbody>tr span[id^='set']")
        expected_menu_list=['Sort Ascending', 'Sort Descending', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Export', 'Print', 'Window', 'Restore Original']

        elems=[i.text.strip() for i in list_obj if i.text.strip()!='']
        utillobj.asequal(expected_menu_list, elems, "Step 04 : 01: Verify list of menus")
        time.sleep(1)
        
        """
            Step 05 : From Country column heading, select Global Filter option.
           Verify Global filter pop up is opened.
        """
        #select_menu_items function is not working for ahtmltab fex. so given in script level to select menu
        
        elem = self.driver.find_element_by_css_selector("#dt1_0_0[style*='block'] table tr#t1_0_0_3")
        core_utillobj.left_click(elem)
        utillobj.synchronize_with_number_of_element("#wall1", 1, 15)

        """ 
            Step 06: Click Add Condition under Global Filter and select Car column
            Verify Car column is displayed in the pop up with filter option 'Equal'.
        """
        filterobj.add_global_condition_field('CAR')
        time.sleep(2)
        var1="√"
        filterobj.create_filter(1,'Equals', value1='ALFA ROMEO', value2='AUDI', value3='BMW')
        time.sleep(2)
        filter_val_elem=self.driver.find_element_by_css_selector("#wall1 div#ftp1_1_0")
        core_utillobj.left_click(filter_val_elem)
        utillobj.synchronize_with_number_of_element("table tbody tr#t0_ftp1_1_0_x__0_9", 1, 8)
        verify_tick_mark=self.driver.find_element_by_css_selector("[id='et0_ftp1_1_0_x__0_1i_t'] span").text.replace(var1, '(Checked)')
        print(verify_tick_mark)
        
        """ 
            Step 07 : Select values like: ALFA ROMEO, AUDI and BMW and click Filter button.
            Verify drop down shows checkmarks next to selected values.
            Verify all four reports have been changed accordingly; the returned reports display the data for selected values: ALFA ROMEO, AUDIO and BMW.
            Notice that Subtotals are no longer provided on reports after Filtering has been performed.
        """
        filterobj.filter_button_click('Filter')
        time.sleep(2)
        
        table_css="#ITableData0"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds05.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds05.xlsx", "Step 07:01::Verify rollup report data")
        
        table_css="#ITableData1"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds06.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds06.xlsx", "Step 07:02::Verify rollup report data")
        
        table_css="#ITableData2"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds07.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds07.xlsx", "Step 07:03::Verify rollup report data")
        
        table_css="#ITableData3"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds08.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds08.xlsx", "Step 07:04::Verify rollup report data")
        
        miscelanousobj.verify_page_summary(0, '5of13records,Page1of1', "Step 7.5:  5of13records,Page1of1 Active Report. - page summary verification of table 1")
        miscelanousobj.verify_page_summary(1, '10of18records,Page1of1', "Step 7.6:  10of18records,Page1of1 Active Report. - page summary verification of table 2")
        miscelanousobj.verify_page_summary(2, '3of10records,Page1of1', "Step 7.7:  3of10records,Page1of1 Active Report. - page summary verification of table 3")
        miscelanousobj.verify_page_summary(3, '10of18records,Page1of1', "Step 7.8:  10of18records,Page1of1 Active Report. - page summary verification of table 4")
        
        """ 
            Step 08 : Click Clear All button, then close Global Filter dialog box by clicking X to close the pop up
            Verify original chart is restored.
        """
        filterobj.filter_button_click('Clear All')
        time.sleep(2)
        filterobj.close_filter_dialog('wall1')
        
        """ 
            Step 09 : Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        time.sleep(5)
                
if __name__ == '__main__':
    unittest.main()