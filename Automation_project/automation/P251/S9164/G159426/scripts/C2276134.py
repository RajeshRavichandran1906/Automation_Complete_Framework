'''
Created on July , 2019

@author: Prasanth
Testcase Name : Pie Chart Total and Tool Tip no longer shows comma thousands separator
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2276134

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods

class C2276134_TestClass(BaseTestCase):
    
    def test_C2276134(self):
        
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
        expected_tooltip_list=['Biscotti: 1,174 (12.47%)']
        

        """
        STEP 1:Run C2276134_Base.fex .
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP251_S9164%2FG159426&BIP_item=C2276134_Base.fex
        """
        chart_obj.run_fex_using_api_url(folder_path,fex_name, mrid="mrid", mrpass="mrpass")
        
        """
        STEP 2:Hover on the pie slices
        STEP 3:Verify following tool tip shows the thousands comma separator
        """
        chart_obj.verify_active_chart_tooltip("jschart_HOLD_0", "riser!s0!g0!mwedge!", expected_tooltip_list, msg="Step 03.02 : Verify the following chart tool tip info displayed")
        
        """
        STEP 4 : Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.logout_chart_using_api()
        
if __name__ == '__main__':
    unittest.main()
        
        