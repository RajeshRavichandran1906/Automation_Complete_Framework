'''
Created on Dec 29, 2017

@author: Sowmiya

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348424
TestCase Name = RCM for numeric dimension has Create Bin option in Data pane
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.lib import utillity


class C2348424_TestClass(BaseTestCase):

    def test_C2348424(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID='C2348424'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                 http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1 rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=10)

        """
        Step 02: Right click on "Sale,Year" in data pane
        """
        time.sleep(4)
        metaobj.datatree_field_click("Sale,Year",1,1)
        time.sleep(2)
        
        """
        Step 03: Verify menu includes "Create Bins..." option
        """
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Sum', 'Create Bins...', 'Add To Query', 'Filter'],msg='Step 03.01: Verify menu includes "Create Bins..." option')
        
        """
        Step 04: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        vis_ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()