'''
Created on Jan 02, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346053
TestCase Name = Tooltip for single selection shows group option
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea
from common.lib import utillity, core_utility
from common.wftools.visualization import Visualization

class C2346053_TestClass(BaseTestCase):

    def test_C2346053(self):
        """
        TESTCASE VARIABLES
        """
        Restore_fex = 'C2346053_Base'
        

        utillobj = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        visual = Visualization(self.driver)
        
        """
        Step 01: Restore the C2346053_Base.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2346053_Base.fex
        """
        visual.edit_fex_using_api_url('P312/S10664_paperclipping_1', fex_name=Restore_fex, mrid='mrid', mrpass='mrpass')
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 7, 90)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 01.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 01.02: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 01.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 01.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 01.05: Verify first bar color")
        """
        Step 02: Click on any riser (Ex. Accessories)
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 7, 10)
        riser = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        core_utils.left_click(riser, element_location= 'bottom_middle')
        time.sleep(1)
        
        """
        Step 03: Verify the tool tip values displayed
        """
        visual.verify_lasso_tooltip(['1 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection'],msg='Step 03.01: Verify following tool tip values displayed')

        """
        Step 04: Logout using API- http://machine:port/alias/service/wf_security_logout.jsp
        """

        
if __name__ == '__main__':
    unittest.main()