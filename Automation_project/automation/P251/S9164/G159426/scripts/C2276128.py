'''
Created on July , 2019

@author: Prasanth
Testcase Name : Pie tooltip no longer shows percentage. Shows full numeric i/o condensed
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2276128

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib.core_utility import CoreUtillityMethods
from common.lib.global_variables import Global_variables
from common.lib.utillity import UtillityMethods

class C2276128_TestClass(BaseTestCase):
    
    def test_C2276128(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        core_util_obj=CoreUtillityMethods(self.driver)
        util_obj=UtillityMethods(self.driver)
        glb_variables=Global_variables()
        
        """
            CLASS VARIABLES
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        fex_name=glb_variables.current_test_case+"_Base"
        expected_tooltip_list_1=['Gifts: 5.8M (25.44%)']
        expected_tooltip_list_2=['Category:  Gifts', 'Dollar Sales:  5814059  (25.44%)']

        """
        STEP 1:Run C2276128_Base.fex .
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP251_S9164%2FG159426&BIP_item=C2276128_Base.fex
        """
        chart_obj.run_fex_using_api_url(folder_path,fex_name, mrid="mrid", mrpass="mrpass")
        util_obj.synchronize_with_visble_text("text[class*='pieLabel']", "Dollar Sales", chart_obj.chart_long_timesleep)
        
        """
        STEP 2:Hover the mouse over any of the pie slices
        STEP 3:Verify the following chart tool tip info displayed
        """
        chart_obj.verify_active_chart_tooltip("jschart_HOLD_0", "riser!s2!g0!mwedge!", expected_tooltip_list_1, msg="Step 03.01 : Verify the following chart tool tip info displayed")
        
        """
        STEP 4 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
        """
        STEP 5 : Launch the IA API C2276128_Base.fex in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP251_S9164%2FG159426%2FC2276128_Base.fex
        """
        chart_obj.edit_fex_using_api_url(folder_path,fex_name="C2276128_Base")
        chart_obj.wait_for_visible_text("#singleReportPanel", "Live Preview")
        
        """
        STEP 6: Click Run 
        """
        chart_obj.run_report_from_toptoolbar()
        chart_obj.switch_to_frame()
        chart_obj.wait_for_visible_text("#jschart_HOLD_0","Category")
        
        """
        STEP 7:Hover the mouse over the same pie slice as before
        STEP 7.01:Verify the following chart tool tip info displayed
        """
        chart_obj.verify_active_chart_tooltip("jschart_HOLD_0", "riser!s2!g0!mwedge!", expected_tooltip_list_2, msg="Step 07.01 : Verify the following chart tool tip info displayed")
        
        """
        STEP 8 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()
        
        