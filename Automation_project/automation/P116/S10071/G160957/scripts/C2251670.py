'''
Created on Jan 18, 2018
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251669
@author: BM13368
'''

import unittest, time, pyautogui
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run
from common.lib import utillity

class C2251670_TestClass(BaseTestCase):

    def test_C2251670(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251670'
        active_fex_name ='arfilter_showtitle.fex'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)        
        
        """
            Step 01:Execute the attached repro - arfilter_showtitle.fex, which is a Compound Fex containing report and each of the 5 current Filter Control boxes.
            Expect to see the initial Document display of a 10 row CAR report and 5 Filter Control boxes.
            On the right-side of the Dashboard, on the first row will be Drop Down, List Box & Check Box Filters.
            On the right-side of the Dashboard, on the second row will be a Radio Button and Text Entry Box.
            Expect to see the Filter Box Title above and in blue for AHTML, no color for FLEX/APDF.
        """
        utillobj.active_run_fex_api_login(active_fex_name, "S10071_3", 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#combobox_dsPROMPT_1", 1, 65)
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01:01: Execute the arfilter_showtitle.fex and Verify the Report Heading')
        column_list=['COUNTRY','CAR','DEALER_COST','RETAIL_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 01.02: Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 01.03: Verify report data")
        """ 
            Step 02:For the Drop Down Filter Box, select ENGLAND.
        """
        expected_value='[All]'
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value=expected_value, default_selection_msg="Step 02:01:Verify default selected value shows All in the first dropdown")
        utillobj.select_dropdown("#combobox_dsPROMPT_1", "visible_text", "ENGLAND")
        time.sleep(2)
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value="ENGLAND", default_selection_msg="Step 02:02:Verify default selected value shows ENGLAND in the first dropdown")
         
        """
            Expect to see the report display the 3 lines for ENGLAND.
        """
        miscelanousobj.verify_page_summary(0, '3of10records,Page1of1', 'Step 02:03: Expect to see the report heading 3of 10 records')
        column_list=['COUNTRY','CAR','DEALER_COST','RETAIL_COST']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 02.04:Verify the column heading')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds02.xlsx","Step 02.05: Verify report data")
         
        """
            Reset the Filter by selecting the ALL option for the new Filter test.
            Expect to see the original 10 line report after resetting with the ALL option.
        """
        select_drop_down_value='[All]'
        utillobj.select_dropdown("#combobox_dsPROMPT_1", "visible_text", select_drop_down_value)
        time.sleep(2)
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value=select_drop_down_value, default_selection_msg="Step 02:06:Verify default selected value shows All in the first dropdown")
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 01:01: Verify the Report Heading shows 10 of 10 records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 02.07: Verify report data")
         
        """   
            Step 03:For the List Box Filter, select FRANCE.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_2_cs', ['FRANCE'])
        time.sleep(15)
        ia_runobj.verify_active_dashboard_prompts('listbox','#PROMPT_2_cs', ['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], "Step 03:01:Verify the list of values in listbox")
        """
            Expect to see the report display the 1 line for FRANCE.
        """
        miscelanousobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 03:02: Expect to see the report heading 1of 10 records')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds03.xlsx","Step 03.03: Verify report data")
         
        """
            Reset the Filter by selecting the ALL option for the new Filter test.
            Expect to see the original 10 line report after resetting with the ALL option
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_2_cs', ['[All]'])
        time.sleep(5)
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_2_cs', ['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], "Step 03:04:Verify the list of values in listbox")
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 03:05: Verify the Report Heading shows 10 of 10 records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 03.06: Verify report data")
        """    
            Step 04:For the Check Box Filter, select ITALY.
            Expect to see the report display the 2 lines for ITALY.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_3_cs', ['ITALY'])
        time.sleep(5)
        ia_runobj.verify_active_dashboard_prompts( 'checkbox', '#PROMPT_3_cs', ['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], "Step 04:01:Verify the list of values in checkbox")
        miscelanousobj.verify_page_summary(0, '2of10records,Page1of1', 'Step 04:02: Expect to see the report heading 1of 10 records')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds04.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds04.xlsx","Step 04.03: Verify report data")
        """
            Reset the Filter by selecting the ALL option for the new Filter test.
            Expect to see the original 10 line report after resetting with the ALL option.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_3_cs', ['[All]'])
        time.sleep(5)
        ia_runobj.verify_active_dashboard_prompts('checkbox', '#PROMPT_3_cs', ['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], "Step 04:04:Verify the list of values in checkbox", default_selected_check='[All]')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 04:05: Verify the Report Heading shows 10 of 10 records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 04.06: Verify report data")
        """    
            Step 05:For the Radio Button Filter, select JAPAN.
        """
        ia_runobj.select_active_dashboard_prompts('radiobutton', '#PROMPT_4_cs', ['JAPAN'])
        time.sleep(5)
        ia_runobj.verify_active_dashboard_prompts('radiobutton', '#PROMPT_4_cs', ['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], "Step 05:01:Verify the list of values in radiobutton")
        """
            Expect to see the report display the 2 lines for JAPAN.
        """
        miscelanousobj.verify_page_summary(0, '2of10records,Page1of1', 'Step 05:02: Expect to see the report heading 2of 10 records')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds05.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds05.xlsx","Step 05.03: Verify report data")
        """
            Reset the Filter by selecting the ALL option for the new Filter test.
            Expect to see the original 10 line report after resetting with the ALL option.
        """
        ia_runobj.select_active_dashboard_prompts('radiobutton', '#PROMPT_4_cs', ['[All]'])
        time.sleep(5)
        ia_runobj.verify_active_dashboard_prompts('radiobutton', '#PROMPT_4_cs', ['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], "Step 05:04:Verify the list of values in radiobutton", default_selected_check='[All]')
        miscelanousobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 05:05: Verify the Report Heading shows 10 of 10 records')
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds01.xlsx","Step 05.06: Verify report data")
        """
            Step 06:For the Text Filter Box, enter 'W GERMANY' in upper case. Hit enter to filter the report.
            The Text Box does not currently reset to all rows!
            Expect to see the report display the 2 lines for W GERMANY.
        """
        txt_css=driver.find_element_by_css_selector("#PROMPT_5_cs input")
        utillobj.set_text_field_using_actionchains(txt_css, "W GERMANY")
        time.sleep(2)
        pyautogui.hotkey('enter')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '2of10records,Page1of1', 'Step 06:01: Expect to see the report heading 2of 10 records')
#         utillobj.create_data_set('ITableData0','I0r', Test_Case_ID+"_Ds06.xlsx")
        utillobj.verify_data_set('ITableData0','I0r', Test_Case_ID+"_Ds06.xlsx","Step 06.02: Verify report data")

if __name__ == "__main__":
    unittest.main()