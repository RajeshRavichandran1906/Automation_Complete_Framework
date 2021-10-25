'''
Created on July , 2019

@author: Prasanth
Testcase Name : Pie Data text labels showing incorrect format
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2276129

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods

class C2276129_TestClass(BaseTestCase):
    
    def test_C2276129(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj = chart.Chart(self.driver)
        core_util_obj=CoreUtillityMethods(self.driver)
        glb_variables=Global_variables()
        
        """
            CLASS VARIABLES
        """
        project_id=core_util_obj.parseinitfile("project_id")
        suite_id=core_util_obj.parseinitfile("suite_id")
        group_id=core_util_obj.parseinitfile("group_id")
        folder_path=project_id+"_"+suite_id+"/"+group_id
        fex_name=glb_variables.current_test_case+"_Base"
        expected_datalabel=['14%', '4%', '39%', '21%', '6%', '17%']
        expected_tooltip_list=['JAGUAR: 5.8% / 12,000']

        """
        STEP 1:Run the base fex C2276129_Base.fex
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP251_S9164%2FG159426&BIP_item=C2276129_Base.fex
        """
        chart_obj.run_fex_using_api_url(folder_path,fex_name, mrid="mrid", mrpass="mrpass")
        
        """
        STEP 2:Hover on the pie slices
        STEP 3:Verify following Data text labels chart displayed with the tool tip
        """
        chart_obj.verify_data_labels("jschart_HOLD_0", expected_datalabel, custom_css="text[class*='mdataLabels']", msg="Step 03.01 : Verify following Data text labels chart displayed")
        chart_obj.verify_active_chart_tooltip("jschart_HOLD_0", "riser!s4!g0!mwedge!", expected_tooltip_list, msg="Step 03.02 : Verify the following chart tool tip info displayed")
        
        """
        STEP 4 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()
        
        