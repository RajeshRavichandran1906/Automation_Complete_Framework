'''
Created on Dec 29, 2017

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348423
TestCase Name = RCM for measure has Create Bins option in Data pane
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_ribbon
from common.lib import utillity


class C2348423_TestClass(BaseTestCase):

    def test_C2348423(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348423'
#         driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        element_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillobj.synchronize_with_number_of_element(element_css, 1, vis_ribbonobj.home_page_long_timesleep)

        """
        Step 02: Right click on "Gross Profit" in data pane
        """
        metaobj.datatree_field_click("Gross Profit",1,1)
       
        """
        Step 03: Verify menu includes "Create Bins..." option
        """
        utillobj.select_or_verify_bipop_menu(verify='true',expected_popup_list=['Sum', 'Create Bins...', 'Add To Query', 'Filter'],msg='Step 03.01: Verify menu includes "Create Bins..." option')
        """
        Step 04: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        vis_ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main()