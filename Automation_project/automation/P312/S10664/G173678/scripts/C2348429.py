'''
Created on Jan 05, 2018

@author: Nasir
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_metadata, visualization_ribbon
from common.lib.basetestcase import BaseTestCase

class C2348429_TestClass(BaseTestCase):


    def test_C2348429(self):
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """    1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is): http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite    """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P312/S10664_binning_1', 'mrid', 'mrpass')
        time.sleep(4)
        parent_css= "#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css, 1,expire_time=100)
        
        """    2. Right click "Revenue" > Create Bin    """
        metaobj.datatree_field_click("Revenue",1,1, "Create Bins...")
        time.sleep(2)
        parent_css= "div[id^='QbDialog'] div[class*='active window']"
        resultobj.wait_for_property(parent_css, 1)
        
        """    3. Bin width = 1000 Format D15.2CM    """
        """    4. Click "OK"    """
        metaobj.create_bin("REVENUE_US_BIN_1", bin_format_btn=True, check_box_list=['Use Comma (C)'],ok_btn=True, bin_width='1000')
        
        """    5. Add bin to Horizontal axis    """
        metaobj.datatree_field_click('Dimensions->REVENUE_US_BIN_1', 2, 1)
        metaobj.verify_query_pane_field('Horizontal Axis', 'REVENUE_US_BIN_1', 1, "Step 05a: Verify REVENUE_US_BIN_1 is visible underneath Horizontal Axis")
        
        """    6. Double click "Revenue"    """
        metaobj.datatree_field_click("Revenue", 2, 1)
        
        """    7. Verify horizontal axis labels are showing with decimal and comma.    """
        riser_css="#TableChart_1 svg g.risers >g>rect[class^='riser']"
        resultobj.wait_for_property(riser_css, 16, expire_time=25)
        resultobj.verify_yaxis_title("TableChart_1", 'Revenue', "Step 07a: Verify y-Axis Title")
        resultobj.verify_xaxis_title("TableChart_1", 'REVENUE_US_BIN_1', "Step 07b: Verify x-Axis Title")
        resultobj.verify_number_of_riser("TableChart_1", 1, 16, 'Step 07c: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '200M', '400M', '600M', '800M', '1,000M']
        expected_xval_list=['$.00', '$1,000.00', '$2,000.00', '$3,000.00', '$4,000.00', '$5,000.00', '$6,000.00', '$7,000.00', '$8,000.00', '$9,000.00', '$10,000.00', '$11,000.00', '$12,000.00', '$13,000.00', '$14,000.00', '$15,000.00']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, 'Step 07d: X and Y axis labels')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step 07e: Verify first bar color")
        
        """    8. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        parent_css="#MAINTABLE_wbody1 svg>g rect[class^='riser!']"
        resultobj.wait_for_property(parent_css, 16, expire_time=30)
        
        """    9. Hover on run time chart and Verify tool tip value    """
        resultobj.verify_yaxis_title("MAINTABLE_1", 'Revenue', "Step 09a: Verify y-Axis Title")
        resultobj.verify_xaxis_title("MAINTABLE_1", 'REVENUE_US_BIN_1', "Step 09b: Verify x-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_1", 1, 16, 'Step 09c: Verify the total number of risers displayed on livepreview Chart')
        expected_yval_list=['0', '200M', '400M', '600M', '800M', '1,000M']
        expected_xval_list=['$.00', '$1,000.00', '$2,000.00', '$3,000.00', '$4,000.00', '$5,000.00', '$6,000.00', '$7,000.00', '$8,000.00', '$9,000.00', '$10,000.00', '$11,000.00', '$12,000.00', '$13,000.00', '$14,000.00', '$15,000.00']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_1", expected_xval_list, expected_yval_list, 'Step 09d: X and Y axis labels')
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g3!mbar!", "bar_blue", "Step 09e: Verify first bar color")
        
        ele=driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.take_screenshot(ele,'C2348429_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    10. Dismiss run window    """
        driver.close()
        time.sleep(2)
        utillobj.switch_to_window(0)
        
        """    11. Logout using API - http://machine:port/alias/service/wf_security_logout.jsp    """
        
if __name__ == "__main__":
    unittest.main()