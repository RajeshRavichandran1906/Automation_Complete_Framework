'''
Created on Jun 21, 2019

@author: Varun/Prasanth
Testcase Name : Bar chart incorrectly defaults to showing data labels
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2509761

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import core_utility
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C2509761_TestClass(BaseTestCase):
    
    def test_C2509761(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        util_obj=utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        global_var_obj=Global_variables()
        
        """
        Test case variables
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        case_id=global_var_obj.current_test_case
        folder_path=project_id+"_"+suite_id+"/"+group_id
        
        """
        STEP 1:Launch the API to create new Chart.
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite", mrid="mrid", mrpass="mrpass", folder_path=folder_path)
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 2:Add "Product, Category" and "Revenue".
        """
        chart_obj.double_click_on_datetree_item("Product,Category", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel","Product Category")
        chart_obj.double_click_on_datetree_item("Revenue", 1)
        chart_obj.wait_for_visible_text("#singleReportPanel","Revenue")
        
        """
        STEP 3: Verify no data labels are displayed in chart live preview
        """
        actual_data_lables=len(self.driver.find_elements_by_css_selector("#TableChart_1 text[class*='dataLabels']"))
        util_obj.asequal(0, actual_data_lables, "Step 03.01 : Verify no data labels are displayed in chart live preview")
        
        """
        STEP 4: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text("#jschart_HOLD_0","Product Category")
        
        """
        STEP 5: Verify no data labels are displayed in run time chart
        """
        actual_data_lables=len(self.driver.find_elements_by_css_selector("#jschart_HOLD_0 text[class*='dataLabels']"))
        util_obj.asequal(0, actual_data_lables, "Step 05.01 : Verify no data labels are displayed in run time chart")
        
        """
        STEP 6 : Select Format > Run with > Insight
        """
        chart_obj.switch_to_default_content()
        chart_obj.select_ia_ribbon_item('Format', "run_with")
        chart_obj.select_ia_ribbon_item('Format', "insight")
        
        """
        STEP 7: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text(".main-box","Vertical Axis")
        
        """
        STEP 8: Verify no data labels are displayed in insight chart
        """
        actual_data_lables=len(self.driver.find_elements_by_css_selector(".main-box text[class*='dataLabels']"))
        util_obj.asequal(0, actual_data_lables, "Step 08.01 : Verify no data labels are displayed in insight chart")
        
        """
        STEP 9: Click Save in the toolbar > Save as "C2509761" > Click Save
        """
        chart_obj.switch_to_default_content()
        chart_obj.select_item_in_top_toolbar("save")
        chart_obj.save_file_in_save_dialog(case_id)
        
        """
        STEP 10 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
        """
        STEP 11 : Run the fex from the BIP using API
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP309_S10666%2FG169735&BIP_item=C2509761.fex
        """
        chart_obj.run_fex_using_api_url(folder_path, case_id, mrid="mrid", mrpass="mrpass", run_chart_css="#runbox_id")
        chart_obj.wait_for_visible_text("#runbox_id", "Revenue")
        
        """
        STEP 12: Verify no data labels are displayed in insight chart
        """
        actual_data_lables=len(self.driver.find_elements_by_css_selector("#runbox_id text[class*='dataLabels']"))
        util_obj.asequal(0, actual_data_lables, "Step 12.01 : Verify no data labels are displayed in insight chart")
        
        """
        STEP 13 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()




