'''
Created on Jan 3, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346061
TestCase Name = Group option not available for Date dimension
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata
from common.wftools import visualization
from common.lib import utillity


class C2346061_TestClass(BaseTestCase):

    def test_C2346061(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346061'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P312/S10664_paperclipping_1', 'mrid', 'mrpass')
#         visual.invoke_visualization_tool_using_api('new_retail/wf_retail_lite')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1, expire_time=30)

        """
        Step 02: Double click "Revenue", "Sale, Year (YYMDy)"(Sales_Related\Transaction Date, Component) add fields to chart
        """
#         visual.add_field_using_double_click('Revenue', 1)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        
#         visual.add_field_using_double_click('Sale,Year', 1)
        metaobj.datatree_field_click("Sale,Year", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 6)
        
        """
        Step 03: Verify following chart preview displayed
        """
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Sale Year', "Step 03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 03:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 6, 'Step 03.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2011', 'Revenue:$48,965,069.21', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 03.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 04: Lasso on last two risers
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 6)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g4!mbar!', target_tag='rect', target_riser='riser!s0!g5!mbar!')
        time.sleep(2)
        
        """
        Step 05: Verify Tooltip does not have option to group.
        """
        resultobj.select_or_verify_lasso_filter(verify=['2 item selected', 'Filter Chart', 'Exclude from Chart'],msg='Step 05: Verify following tool tip values displayed')
        time.sleep(8)
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele, Test_Case_ID+'_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 06: Logout using API- http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()
