'''
Created on Oct 31, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313967
TestCase Name = Rename group via tooltip
'''

import unittest, time
from common.lib import utillity,core_utility
from common.lib.basetestcase import BaseTestCase
# from common.wftools.visualization import Visualization
from common.pages import visualization_resultarea, visualization_ribbon
from selenium.webdriver.common.action_chains import ActionChains

class C2313967_TestClass(BaseTestCase):

    def test_C2313967(self):
        
        """
        TESTCASE VARIABLES
        """
        tooltip_css= ".tdgchart-tooltip span[class='tdgchart-tooltip-pad']:not([style*='hidden'])"
        Test_Case_ID_base = 'C2313967_base'
        Test_Case_ID = 'C2313967'
        
        """
        CLASS & OBJECTS
        """
        driver = self.driver
#         visual = Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        core_obj=core_utility.CoreUtillityMethods(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
           
        """
        Step 01: Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2313967_base.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID_base, 'idis', 'S10660_visual_2',mrid='mrid',mrpass='mrpass')
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, resultobj.chart_long_timesleep)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step 01.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 01.02: Verify Y-Axis Title")
        expected_xval_list=['Access, Comp, TV & Video', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 01.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 01.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 01.05: Verify first bar color")
        
        """
        Step 02: Click the group value riser "Access,Comp, TV & Video" > Rename group PRODUCT_CATEGORY_1
        """
        core_obj.python_move_to_element(self.driver.find_element_by_id('MAINTABLE_wbody1'), 'top_left')
        riser = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mbar!']")
        core_obj.python_move_to_element(riser)
        riser.click()
#         core_obj.python_left_click(riser)
#         utillobj.synchronize_until_element_is_visible(tooltip_css, 9)
#         visual.select_lasso_tooltip('Rename group PRODUCT_CATEGORY_1')

        elems=self.driver.find_elements_by_css_selector(tooltip_css)
        ActionChains(self.driver).move_to_element(elems[4]).pause(1).click(elems[5]).perform()
#         elems[5].click()
#         ActionChains(self.driver).move_to_element_with_offset(co, 0, -35).pause(1).perform()
        
        """
        Step 03: Type in the Rename Group input: "Categories" > OK
        Group name changes to "Categories" on X axis title, in query pane and in data pane.
        """
        utillobj.synchronize_until_element_is_visible("div[id^='BiDialog'] [class*='window-active']", resultobj.chart_long_timesleep)
        resultobj.rename_grouped_riser("Categories", verify_name="PRODUCT_CATEGORY_1", msg = 'Step03')
        utillobj.synchronize_until_element_disappear("div[id^='BiDialog'] [class*='window-active']", resultobj.chart_long_timesleep)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, resultobj.chart_long_timesleep)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Categories', "Step 03.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 03.02: Verify Y-Axis Title")
        expected_xval_list=['Access, Comp, TV & Video', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 03.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 03.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 03.05: Verify first bar color")
        
        """
        Step04: Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        core_obj.switch_to_new_window()
         
        """
        Verify output
        """
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 9, resultobj.chart_long_timesleep)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Categories', "Step 04.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 04.02: Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 04.03: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Access, Comp, TV & Video', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 04.04: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04.05: Verify first bar color")
     
        """
        Step 05: Close output, save and close design window.
        """
        core_obj.switch_to_previous_window()
        
        """
        Step 06: Click Save in the toolbar > Save as "C2313967" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
        Step 07: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()