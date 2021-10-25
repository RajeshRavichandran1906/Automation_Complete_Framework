'''
Created on 29-Dec-2017

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348425
TestCase Name = RCM for date does't have option to bin
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon

class C2348425_TestClass(BaseTestCase):

    def test_C2348425(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2348425"
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        """ Step 1: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                    http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10664_binning_1', 'mrid', 'mrpass')
        text='DropMeasuresorSortsintotheQueryPane'
        resultobj.wait_for_property("#TableChart_1 svg g text.title", 0, expire_time=25, string_value=text, with_regular_exprestion=True)         
        
        """ Step 2: Right click Transaction Date, component> "Sale,Year"
        """
        metaobj.expand_field_tree('Sales_Related')
        metaobj.expand_field_tree('Transaction Date, Components')
        metaobj.expand_field_tree('Sale,Year', click_opt=1)
        
        """ Step 3: Verify menu not includes "Create Bins..." option
        """
        utillobj.select_or_verify_bipop_menu(verify=True, expected_popup_list=['Sum', 'Create Group...', 'Add To Query', 'Filter'], msg="Step 03.01: Verify menu not includes 'Create Bins...' option")
        
        """ Step 4: Logout using API (without saving)
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        vis_ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()