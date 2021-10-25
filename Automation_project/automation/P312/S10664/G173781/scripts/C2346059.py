'''
Created on Jan 3, 2018

@author: Magesh

TestSuite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2346059
TestCase Name = Group option not available at run time for lasso selection
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon
from common.lib import utillity,core_utility
from common.wftools import visualization
from selenium.webdriver.common.by import By


class C2346059_TestClass(BaseTestCase):

    def test_C2346059(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2346059'
        Restore_fex = 'C2346059_Base'
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        Step 01: Restore the C2346059_Base.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2346059_Base.fex
        """
        utillobj.infoassist_api_edit(Restore_fex, 'idis', 'S10664_paperclipping_1',mrid='mrid',mrpass='mrpass')
#         visual.invoke_visualization_in_edit_mode_using_api(Restore_fex)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 7, 150)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 01:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 01:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 01.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 01.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 01.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 02: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        core_util_obj.switch_to_new_window()
                 
        """
        Step 03: Lasso several risers at run time (Ex..first three risers)
        """
        time.sleep(5) 
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g0!mbar!', target_tag='rect', target_riser='riser!s0!g2!mbar!')
        time.sleep(2)
        
        """
        Step 04: Verify tool tip doesn't show option to group
        """
        resultobj.select_or_verify_lasso_filter(verify=['1 item selected', 'Filter Chart', 'Exclude from Chart'],msg='Step 04: Verify tool tip doesnt show option to group')
        time.sleep(4)
        
        """
        Step 05: Close run window
        """
#         visual.switch_to_previous_window()
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step 06: Logout using API: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 07: Run C2346052.fex from resource tree: http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2346052.fex
        """
        utillobj.active_run_fex_api_login(Restore_fex+'.fex','S10664_paperclipping_1','mrid','mrpass')
        time.sleep(10) 
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step 07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        ele=driver.find_element_by_css_selector("#orgdiv0")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 08: Click any one of the riser
        """
        resultobj.create_lasso("MAINTABLE_wbody1",'rect', 'riser!s0!g4!mbar!')
        time.sleep(2)
        
        """
        Step 09: Verify tool tip doesn't show option to group
        """
        resultobj.select_or_verify_lasso_filter(verify=['1 point', 'Filter Chart', 'Exclude from Chart'],msg='Step 09: Verify tool tip doesnt show option to group')
        time.sleep(4)                                 
        
        """
        Step 10: Logout using API- http://machine:port/alias/service/wf_security_logout.jsp
        """
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()