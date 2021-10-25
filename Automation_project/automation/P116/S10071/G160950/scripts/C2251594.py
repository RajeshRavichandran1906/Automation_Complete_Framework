'''
Created on Jan 18, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251594
TestCase Name = Dashboard with global Filtering and Radio Button (ACT-68).
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,ia_run
from common.lib import utillity


class C2251594_TestClass(BaseTestCase):

    def test_C2251594(self):
        """
        Step 01: Execute the attached repro act-68.fex
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_misobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        utillobj.active_run_fex_api_login('act-68.fex','S10071_1','mrid','mrpass')
        utillobj.synchronize_with_number_of_element("#ITableData0 ", 1, 10)
        
        """
        Expect to see the following Active Dashboard, with Global Filter set to England, two reports with England data and a 
        Radio Button showing only cars for England. 
        Notice that the All Radio button refers to the data specified in the Global Filter value of England.
        """
        def verify(r1,r1_sum,r1_col,r2,r2_sum,r2_col,radio,radio_defau,drop,step):
            #1st Report
            active_misobj.verify_page_summary(r1,r1_sum,step+'.1a: Verify the Report Heading of 1st Report')
            active_misobj.verify_column_heading('ITableData'+str(r1), r1_col, step+'.1b: Verify the column heading')
#             ia_runobj.create_table_data_set('#ITableData'+str(r1), 'C2251594_Ds'+step+'.1.xlsx')
            ia_runobj.verify_table_data_set('#ITableData'+str(r1), 'C2251594_Ds'+step+'.1.xlsx', step+'.1c: Verify data.')
            #2nd Report
            active_misobj.verify_page_summary(r2,r2_sum,step+'.2a: Verify the Report Heading of 2nd Report')
            active_misobj.verify_column_heading('ITableData'+str(r2), r2_col, step+'.2b: Verify the column heading')
#             ia_runobj.create_table_data_set('#ITableData'+str(r2), 'C2251594_Ds'+step+'.2.xlsx')
            ia_runobj.verify_table_data_set('#ITableData'+str(r2), 'C2251594_Ds'+step+'.2.xlsx', step+'.2c: Verify data.')
            #Global Filter
            utillobj.verify_dropdown_value(".arDashboardMergeDropdown",expected_default_selected_value=drop ,default_selection_msg=step+".3: Verify Global FILTER IS SHOWING")
        r1_col=['COUNTRY','CAR','DEALER_COST']
        r2_col=['COUNTRY','CAR','MODEL','RETAIL_COST']
        radio=['[All]','JAGUAR','JENSEN','TRIUMPH']
        radio_defau=['[All]']
        drop="ENGLAND"
        verify(0,'3of10records,Page1of1',r1_col,1,'4of18records,Page1of1',r2_col,radio,radio_defau,drop,"Step01")
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#RADIO1_cs",radio_defau, "Step01.4: Verify Radio button")
        
        """
        Step02: Click JAPAN in the Global Filter drop down at the top of the Dashboard.
        Expect to see the following Dashboard, now only with Japan data on the reports and Cars for Japan in the Radio Button list.
        """
        utillobj.select_dropdown(".arDashboardMergeDropdown","visible_text",'JAPAN')
        r1_col=['COUNTRY','CAR','DEALER_COST']
        r2_col=['COUNTRY','CAR','MODEL','RETAIL_COST']
        radio=['[All]','DATSUN','TOYOTA']
        radio_defau=['[All]']
        drop="JAPAN"
        verify(0,'2of10records,Page1of1',r1_col,1,'2of18records,Page1of1',r2_col,radio,radio_defau,drop,"Step02")
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#RADIO1_cs",radio_defau, "Step02.4: Verify Radio button")
        
        """
        Step03: Click the Radio button for Datsun.
        Expect to see the reports further filtered so that only Datsun data is shown for Japan.
        """
        ia_runobj.select_active_dashboard_prompts("radio","#RADIO1_cs",["DATSUN"])
        r1_col=['COUNTRY','CAR','DEALER_COST']
        r2_col=['COUNTRY','CAR','MODEL','RETAIL_COST']
        radio=['[All]','DATSUN','TOYOTA']
        radio_defau=['DATSUN']
        drop="JAPAN"
        verify(0,'1of10records,Page1of1',r1_col,1,'1of18records,Page1of1',r2_col,radio,radio_defau,drop,"Step03")
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#RADIO1_cs",radio_defau, "Step03.4: Verify Radio button")
         
        """
        Step04: Click the All Radio Button.
        Expect to see all cars for Japan once again on the reports.
        """
        ia_runobj.select_active_dashboard_prompts("radio","#RADIO1_cs",['[All]'])
        r1_col=['COUNTRY','CAR','DEALER_COST']
        r2_col=['COUNTRY','CAR','MODEL','RETAIL_COST']
        radio=['[All]','DATSUN','TOYOTA']
        radio_defau=['[All]']
        drop="JAPAN"
        verify(0,'2of10records,Page1of1',r1_col,1,'2of18records,Page1of1',r2_col,radio,radio_defau,drop,"Step04")
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#RADIO1_cs",radio_defau, "Step04.4: Verify Radio button")
         
        """
        Step05: Click the Radio button for Toyota.
        Expect to see the reports further filtered so that only Toyota data is shown for Japan.
        """
        ia_runobj.select_active_dashboard_prompts("radio","#RADIO1_cs",['TOYOTA'])
        r1_col=['COUNTRY','CAR','DEALER_COST']
        r2_col=['COUNTRY','CAR','MODEL','RETAIL_COST']
        radio=['[All]','DATSUN','TOYOTA']
        radio_defau=['TOYOTA']
        drop="JAPAN"
        verify(0,'1of10records,Page1of1',r1_col,1,'1of18records,Page1of1',r2_col,radio,radio_defau,drop,"Step05")
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#RADIO1_cs",radio_defau, "Step05.4: Verify Radio button")
         
        """
        Step06: Click W GERMANY in the Global Filer drop down,
        Expect to see only data for W GERMANY.Also expect to see the Radio button reflect Cars for 
        W GERMANY and the button reset to [All].
        """
        utillobj.select_dropdown(".arDashboardMergeDropdown","visible_text",'W GERMANY')
        r1_col=['COUNTRY','CAR','DEALER_COST']
        r2_col=['COUNTRY','CAR','MODEL','RETAIL_COST']
        radio=['[All]','AUDI','BMW']
        radio_defau=['[All]']
        drop="W GERMANY"
        verify(0,'2of10records,Page1of1',r1_col,1,'7of18records,Page1of1',r2_col,radio,radio_defau,drop,"Step06")
        ia_runobj.verify_selected_value_in_active_dashboard_prompts("radio","#RADIO1_cs",radio_defau, "Step06.4: Verify Radio button")
        
        
if __name__ == '__main__':
    unittest.main()


