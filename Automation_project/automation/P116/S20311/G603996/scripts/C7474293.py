'''
Created on January 09, 2019

@author: KK14897

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/7474293
Test Case Title =  HIDENULLACRS ON behavior with Auto Prompt
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_report
from common.wftools import chart, report
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods

class C7474293_TestClass(BaseTestCase):

    def test_C7474293(self):
       
        """
        CLASS OBJECTS
        """
        ar_obj=active_report.Active_Report(self.driver)
        chart_obj=chart.Chart(self.driver)
        report_obj=report.Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = CoreUtillityMethods(self.driver)
        
        """
        COMMON VARIABLES
        """
        project_id = core_utilobj.parseinitfile('project_id')
        suite_id = core_utilobj.parseinitfile('suite_id')
        group_id = core_utilobj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        Test_Case_ID='C7474293'
        Table_ID="#ITableData0"
        fex_off="IDA_HIDENULLACRS_OFF.fex"
        fex_on = "IDA_HIDENULLACRS_ON.fex"
        Col_css=".autop-title"
        visible_text="Filter Values"
        
        """
        
        STEP 01: Login to WF as Developer.
        STEP 02: Run IDA_HIDENULLACRS_OFF.fex.
        A report prompting panel appears.
        """
        ar_obj.run_active_report_using_api(fex_off, column_css=Col_css, synchronize_visible_element_text=visible_text, repository_path=folder_path)
        
        """
        STEP 03 : Under Filter Values, leave Product Category selected at All Values. Click on the "Run with filter values" arrow.
        
        An Active Report appears with a Product,Category selection box set to Accessories, a table, and a pie chart. 
        The table contains about 20 columns, but only 3 are populated; the rest show "missing". Scroll the table to the right until all 3 have appeared. 
        (The pie chart contains slices for only these 3 entries.)
        """
        report_obj.run_auto_prompt_report()
        core_utilobj.switch_to_frame(frame_css="iframe[class='autop-wf-output']")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds01.xlsx", 'Step 03: Verify data set', table_css=Table_ID) 
        
        """
        STEP 04 :Change Product,Category to Computers.
        There are still about 20 columns in the table, but only 2 are non-missing.
        """
        pie_parent_css="#MAINTABLE_wbody1"
        utillobj.select_dropdown('.arDashboardMergeDropdown', 'value', 'Computers')
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds02.xlsx", 'Step 04: Verify data set', table_css=Table_ID)
        chart_obj.verify_x_axis_title_in_run_window(['Group 0'], parent_css=pie_parent_css,  x_or_y_axis_title_css="[class='pieLabel!g0!mpieLabel!']",msg='Step 04.01: Verify x-axis title')
        chart_obj.verify_number_of_chart_segment('MAINTABLE_wbody1', 2, "Step 04:02: Verify number of chart segments in run window")
        
        """
        STEP 05 : Close the report.
        """
        report_obj.api_logout()
        
        """
        STEP 06 : Run IDA_HIDENULLACRS_ON.fex.
        The same prompting panel appears.
        Under Filter Values, leave Product Category selected at All Values.
        Click on the "Run with filter values" arrow.
        An Active Report appears very much like the previous one, but only the 3 non-missing columns are present.

        """
        ar_obj.run_active_report_using_api(fex_on, column_css=Col_css, synchronize_visible_element_text=visible_text, repository_path=folder_path)
        report_obj.run_auto_prompt_report()
        core_utilobj.switch_to_frame(frame_css="iframe[class='autop-wf-output']")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds03.xlsx", 'Step 06: Verify data set', table_css=Table_ID)
        
        """
        Step 07 : Change Product,Category to Computers.
        Only the 2 non-missing columns are present.
        """
        utillobj.select_dropdown('.arDashboardMergeDropdown', 'value', 'Computers')
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds04.xlsx", 'Step 07: Verify data set', table_css=Table_ID)
        
        """
        STEP 08 : Close the report.
        Logoff WF.
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()