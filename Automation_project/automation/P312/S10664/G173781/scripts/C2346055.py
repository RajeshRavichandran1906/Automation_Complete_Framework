'''
Created on Jan 8, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346055
TestCase Name = Group option uses field title 
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata
from common.lib import utillity
from common.wftools import visualization


class C2346055_TestClass(BaseTestCase):

    def test_C2346055(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346055'
        Restore_fex = 'C2346055_Base'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore the C2346055_Base.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2346055_Base.fex
        """
        utillobj.infoassist_api_edit(Restore_fex, 'idis', 'S10664_paperclipping_1',mrid='mrid',mrpass='mrpass')
#         visual.invoke_visualization_in_edit_mode_using_api(Restore_fex)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        
        """
        Step 03: Hover over "Product,Category" in query pane
        Tooltip shows Product,Category is the title of this field and PRODUCT_CATEGORY is the name
        """
        expected_list=['Segment: WF_RETAIL_PRODUCT', 'Name: PRODUCT_CATEGORY', 'Alias: PRODUCT_CATEGORY', 'Title: Product,Category', 'Description: Product Category', 'Format: A40V']
        metaobj.verify_querytree_tooltip("Product,Category", 1, expected_list, 'Step 03: Hover over "Product,Category" in query pane')
        time.sleep(4)
        
        """
        Step 04: Click on any riser (first one)
        Step 04.1: Title Product,Category is using in grouping option
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 04:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 04:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04.c: Verify first bar color")
        bar=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 04.d: Verify bar value")
        time.sleep(5)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect','riser!s0!g0!mbar!')
        time.sleep(2)
        resultobj.select_or_verify_lasso_filter(verify=['1 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection'],msg='Step 04: Verify Title Product,Category is using in grouping option')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 05: Logout using API- http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()