'''
Created on July 2 , 2019

@author: Niranjan/Prasanth
Testcase Name : Explode Pie slice is leaving artifacts and not working correctly
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5852746

'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib.global_variables import Global_variables
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods

class C5852746_TestClass(BaseTestCase):
    
    def test_C5852746(self):
        
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
        expected_datalabel=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        
        """
        STEP 1:Run the chart from Bip
        http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP251_S10661%2FG170888%252F&BIP_item=C5852746_base.fex
        """
        chart_obj.run_fex_using_api_url(folder_path,fex_name, mrid="mrid", mrpass="mrpass")
        
        """
        STEP 1.01:Expected
        """
        chart_obj.verify_number_of_pie_segments("#jschart_HOLD_0", 1, 14, msg="Step 01.01 ")
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mwedge!", "cerulean_blue", msg="Step 01.02 : Verify Pie slice color")
        chart_obj.verify_chart_color("jschart_HOLD_0", "riser!s4!g0!mwedge!", "gold_drop", msg="Step 01.03 : Verify Pie slice color")
        chart_obj.verify_riser_pie_labels_and_legends("jschart_HOLD_0", ["Cost of Goods"], msg="Step 01.04 :")
        chart_obj.verify_data_labels("jschart_HOLD_0", expected_datalabel, custom_css="[class*='legend-labels']", msg="Step 01.05 : Verify_data_labels")
        
        """
        STEP 2:Click on 'Camcorder' Slicer and verify chart is displaying like below.
        """
        camcorder=util_obj.validate_and_get_webdriver_object("path[class='riser!s1!g0!mwedge!']", "Camcorder")
        location1=camcorder.location
        core_util_obj.left_click(camcorder)
        location2=camcorder.location
        actual_status = (location1.get('x')<location2.get('x') and location1.get("y")>location2.get("y"))
        util_obj.asequal(True, actual_status, "Step 02.02 : Explode Pie slice is leaving artifacts")
        
        """
        STEP 3 : Logout using API (without saving)
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
            

        
        