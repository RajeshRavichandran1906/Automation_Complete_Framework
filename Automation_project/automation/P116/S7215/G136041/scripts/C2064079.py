'''
Created on Jan 10, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7215
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2064079
TestCase_Name : ARFILTER_ACTIVE doesn't work w/ date fmt MTYY or YYMT (ACT-198)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.wftools import report
from common.lib import utillity

class C2064079_TestClass(BaseTestCase):

    def test_C2064079(self):
        
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        active_reportobj = Active_Report(self.driver)
        report_obj = report.Report(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 40
        run_parent_css="ITableData0"
        fex_name="act-198"
        folder_name='P116/S7215'
        
        """
        Step 01: Execute the attached repro - ACT-198.fex
        """
        report_obj.run_fex_using_api_url(folder_name, fex_name, 'mrid', 'mrpass', run_table_css="#"+run_parent_css, no_of_element=1, wait_time=MEDIUM_WAIT_TIME)
        
        """
        Step 01.1: Expect to see the following Active Report with 72 records and an Combo Box selection pane.
        Expect to see the initial Combo Box value of 'JAN, 2002'
        """
        active_reportobj.verify_page_summary(0, '72of5595records,Page1of4', "Step 01.1: Expect to see the following Active Report with 72 records")
        time.sleep(3)
        combo_box_css = "[id='combobox_dsCOMBOBOX1']"
        utillobj.verify_element_visiblty(element_css=combo_box_css, visible=True, msg='Step 01.2: Verify Combo Box selection pane')
        utillobj.verify_dropdown_value("[id='combobox_dsCOMBOBOX1']",expected_default_selected_value='JAN, 2002', default_selection_msg="Step 01.3: Expect to see the initial Combo Box value of 'JAN, 2002'")
        column_list=['Date Of Order:', 'Order Number:', 'YR_MO', 'Store Name:', 'Product Number#:', 'Product Number:', 'Quantity:']
        active_reportobj.verify_column_heading(run_parent_css, column_list, 'Step 01.4: Verify all columns listed on the report act-198.fex')
#         active_reportobj.create_data_set_using_table_rowid(run_parent_css,'I0r','act-198.xlsx')
        active_reportobj.verify_data_set_using_table_rowid(run_parent_css, 'I0r', 'act-198.xlsx', 'Step 01.5: Verify data set')

        """
        Step 02: From the Combo Box, select the first value of DEC, 2000
        """
        time.sleep(3)
        utillobj.select_dropdown("[id='combobox_dsCOMBOBOX1']", 'visible_text', 'DEC, 2000')
        
        """
        Step 02.1: Expect to see the Active Report with 5 records and now displaying data for 'DEC, 2000'
        """
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        active_reportobj.wait_for_visible_text(parent_css, '2000/12/31', MEDIUM_WAIT_TIME)
        time.sleep(2)
        active_reportobj.verify_page_summary(0, '5of5595records,Page1of1', "Step 02.1: Expect to see the Active Report with 5 records and now displaying data for 'DEC, 2000'")
#         active_reportobj.create_data_set_using_table_rowid(run_parent_css,'I0r','C2064079_Ds01.xlsx')
        active_reportobj.verify_data_set_using_table_rowid(run_parent_css, 'I0r', 'C2064079_Ds01.xlsx','Step 02.2: Expect to see displaying data for DEC, 2000')

        """
        Step 03: From the Combo Box, select the last value of DEC, 2002
        """
        utillobj.select_dropdown("[id='combobox_dsCOMBOBOX1']", 'visible_text', 'DEC, 2002')
        
        """
        Step 03.1: Expect to see the Active Report with 71 records and now displaying data for 'DEC, 2002'
        """
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        active_reportobj.wait_for_visible_text(parent_css, '2002/12/01', MEDIUM_WAIT_TIME)
        time.sleep(2)
        active_reportobj.verify_page_summary(0, '71of5595records,Page1of4', "Step 03.1: Expect to see the Active Report with 71 records and now displaying data for 'DEC, 2002'")
#         active_reportobj.create_data_set_using_table_rowid(run_parent_css,'I0r','C2064079_Ds02.xlsx')
        active_reportobj.verify_data_set_using_table_rowid(run_parent_css, 'I0r', 'C2064079_Ds02.xlsx','Step 03.2: Expect to see displaying data for DEC, 2002')

        """
        Step 04: From the Combo Box, select the last value of [All] at the top.
        """
        utillobj.select_dropdown("[id='combobox_dsCOMBOBOX1']", 'visible_text', '[All]')
       
        """
        Step 04.1: Expect to see all 5595 records from the [All] request.
        """
        parent_css="#ITableData0 tr:nth-child(2) td:nth-child(1)"
        active_reportobj.wait_for_visible_text(parent_css, '2000/12/31', MEDIUM_WAIT_TIME)
        time.sleep(2)
        active_reportobj.verify_page_summary(0, '5595of5595records,Page1of280', "Step 04.1: Expect to see all 5595 records from the [All] request")
#         active_reportobj.create_data_set_using_table_rowid(run_parent_css,'I0r','C2064079_Ds03.xlsx')
        active_reportobj.verify_data_set_using_table_rowid(run_parent_css, 'I0r', 'C2064079_Ds03.xlsx','Step 04.2: Expect to see displaying data for [All]')

if __name__ == "__main__":
    unittest.main()