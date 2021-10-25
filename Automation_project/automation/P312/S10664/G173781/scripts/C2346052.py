'''
Created on Jan 02, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346052
TestCase Name = Tooltip for lasso of multiple shows group option
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata
from common.lib import utillity
from common.wftools.visualization import Visualization


class C2346052_TestClass(BaseTestCase):

    def test_C2346052(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346052'
        
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        visual = Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
#         utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_paperclipping_1', 'mrid', 'mrpass')
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 1, 90)
        """
        Step 02: Double click "Revenue", "Product,Category" add fields to chart
        """
        metaobj.datatree_field_click("Revenue", 2, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 1, 30)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 7, 45)
        """
        Step 03: Verify following chart preview displayed
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 03.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 03.02: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 03.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 03.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.05: Verify first bar color")
        """
        Step 04: Lasso on first three riser
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillity.UtillityMethods.synchronize_with_number_of_element(self, parent_css, 7, 8)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g2!mbar!')
        time.sleep(2)
        """
        Step 05: Verify following tool tip values displayed
        """
        resultobj.select_or_verify_lasso_filter(verify=['3 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection'],msg='Step 05.01: Verify following tool tip values displayed')
#         time.sleep(2)
#         ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
#         utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        """
        Step 06: Click Save in the toolbar > Save as "C2346052" > Click Save
        Step 07: Logout using API- http://machine:port/alias/service/wf_security_logout.jsp
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()