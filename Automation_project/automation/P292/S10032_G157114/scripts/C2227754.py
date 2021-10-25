'''
Created on January 29, 2018

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227754
TestCase Name = Report Other: Verify that highlighting can be activated on values and/or rows and unhighlighted.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous
from common.lib import utillity
from common.wftools import active_report

class C2227754_TestClass(BaseTestCase):

    def test_C2227754(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227754'
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        def move_away_from_table():
            table=self.driver.find_element_by_id('TCOL_0_C_0')
            utillobj.default_click(table, 0)
            time.sleep(2)
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266
            Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03 : Verify the report is generated
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """
            Step 04 : Click Highlight Value option on column value. Eg: NY under State
        """
        miscelanousobj.select_field_menu_items('ITableData0', 7, 3, 'Highlight Value')
        move_away_from_table()
        
        """
            Step 04.1 : Verify all the values where State = NY are highlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 5, 'Step 04.1 : Verify all the values where State = NY are highlighted.')
#         utillobj.create_data_set('ITableData0', 'rgb', Test_Case_ID+'_Ds_step04.xlsx')
        utillobj.verify_data_set('ITableData0', 'rgb', Test_Case_ID+'_Ds_step04.xlsx', 'Step 04.2 : Verify highlighted row values')
        
        """
            Step 05 : Click Highlight Row option for the first State value on the report, CA.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 0, 3, 'Highlight Row')
        move_away_from_table()
        
        """
            Step 05.1 : Expect to see the Highlight Row option for row 1 selected.
            Step 06 : Verify that the first row for State = CA is added to the previously highlighted NY States.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 6, 'Step 05.1 : Verify Expect to see the Highlight Row option for row 1 selected.')
#         utillobj.create_data_set('ITableData0', 'rgb', Test_Case_ID+'_Ds_step06.xlsx')
        utillobj.verify_data_set('ITableData0', 'rgb', Test_Case_ID+'_Ds_step06.xlsx', 'Step 05.2 : Verify that the first row for State = CA is added to the previously highlighted NY States')
        
        """
            Step 07: Click on Unhighlight Row option for the first row, for State = CA.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 0, 3, 'Unhighlight Row')
        move_away_from_table()
        
        """
            Step 07.1 : Verify that only the first row has been unhighlighted and all State = NY remain highlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 5, 'Step 06.1 : Verify that only the first row has been unhighlighted and all State')
#         utillobj.create_data_set('ITableData0', 'rgb', Test_Case_ID+'_Ds_step07.xlsx')
        utillobj.verify_data_set('ITableData0', 'rgb', Test_Case_ID+'_Ds_step07.xlsx', 'Step 06.2 : Verify that NY remain highlighted.')
        
        """
            Step 08: Click on Unhighlight All option on the first State = NY row.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 7, 3, 'Unhighlight All')
        move_away_from_table()
        
        """
            Step 08.1 : Verify that all State = NY rows have been unhighlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 0, 'Step 07.1 : Verify that all State = NY rows have been unhighlighted.')
        
        """
            Step 09 : Click on Highlight Value option for the first State = CT.
            Click on Highlight Row option for the first State = FL.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 1, 3, 'Highlight Value')
        miscelanousobj.select_field_menu_items('ITableData0', 2, 3, 'Highlight Row')
        move_away_from_table()
        
        """
            Step 09.1 : Verify that all State = CT are Highlighted and that the first State = CT row is also highlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 7, 'Step 08.1 : Verify that all State = CT are Highlighted and that the first State = CT row is also highlighted.')
#         utillobj.create_data_set('ITableData0', 'rgb', Test_Case_ID+'_Ds_step09.xlsx')
        utillobj.verify_data_set('ITableData0', 'rgb', Test_Case_ID+'_Ds_step09.xlsx', 'Step 08.2 : Verify Highlighted values')
        
        """
            Step 10: Click on the Unhighlight All option first State value that is NOT highlighted, State = GA.
        """
        miscelanousobj.select_field_menu_items('ITableData0', 3, 3, 'Unhighlight All')
        move_away_from_table()
        
        """
            Step 10.1 : Verify that all previous highlighted values/rows have been unhighlighted.
        """
        miscelanousobj.verify_highlighted_rows('ITableData0', 0, 'Step 09.1 : Verify that all previous highlighted values/rows have been unhighlighted.')
        
        """
            Step 11: Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.js
        """
        
if __name__=='__main__' :
    unittest.main()