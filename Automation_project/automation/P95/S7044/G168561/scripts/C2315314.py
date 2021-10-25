'''
Created on January 11, 2019

@author: KK14897

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2315314
TestCase Name = Verify Active Report Window option TAB.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity,core_utility
from common.wftools import active_report
from common.wftools import report

class C2315314_TestClass(BaseTestCase):

    def test_C2315314(self):
        
        """
        Test case Object's
        """
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        report_obj=report.Report(self.driver)
        
        '''
        Variables
        '''
        table_css="TableChart_1"
        Test_Case_ID="C2315314"
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        Folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        
        def verify_tabs(tabs_text,msg):
            otab_val=self.driver.find_element_by_css_selector("#MAINTABLE_0 #MAINTABLE_wmenu0>table>tbody>tr").text
            ocheck=otab_val.strip().split("\n")==tabs_text
            utillity.UtillityMethods.asequal(self,True, ocheck, msg + ": verifying Report and Chart Tabs displayed on top of the Run Report")
                 
        '''       
        Step 01 : Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/P95/S10142
        '''
        ar_obj.invoke_report_tool_using_api("ibisamp/car", mrid="mriddev", mrpass="mrpassdev", repository_path=Folder_path)
        
        '''
        Step 02 :Add fields COUNTRY, CAR & SEATS.
        Select Active Report as the output option.
        Expect to see the following Active report Preview pane.
        '''
        report_obj.double_click_on_datetree_item("COUNTRY", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 7, 20)
        report_obj.double_click_on_datetree_item("CAR", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 18, 20)
        report_obj.double_click_on_datetree_item("SEATS", 1)
        report_obj.wait_for_number_of_element('#'+table_css+' [class*="x"]', 29, 20)
        report_obj.change_output_format_type("active_report")
        report_obj.verify_report_data_set_in_preview(table_css, 10, 3, Test_Case_ID+"_Ds_01.xlsx","Verify Preview")
        util_obj.switch_to_main_window()
        '''
        Step 03 :Click the Format tab, then select Active Report Options.
        Click Display Window down arrow and select TABS.
        Click OK to the Active Reports Options menu
        Click the Run button
        Expect to see the report output with a tab (report) on top of report.
        '''
        report_obj.select_ia_ribbon_item("Format", "active_report_options")
        util_obj.synchronize_with_number_of_element('[class*="bi-window active window "]', 1, 50)
        ar_obj.active_report_options('General',general_window="Tabs", btnOk=True)
        report_obj.select_ia_toolbar_item('toolbar_run')
        util_obj.switch_to_frame()
        util_obj.synchronize_with_number_of_element("#MAINTABLE_wmenu0 [class*='tabPagingTextTabi']", 1, 5)
        verify_tabs(['Report'], "Step 06")
        ar_obj.verify_active_report_dataset(Test_Case_ID+"_Ds_02.xlsx", "Step 3", "#ITableData0")
        
        '''
        Step 04 : Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        '''
        
        
if __name__ == '__main__':
    unittest.main()