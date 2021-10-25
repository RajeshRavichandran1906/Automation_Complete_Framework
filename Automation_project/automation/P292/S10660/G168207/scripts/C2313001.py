'''
Created on Oct 30, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313001
TestCase Name = Rename value group via tooltip
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon
from common.lib import utillity, core_utility

class C2313001_TestClass(BaseTestCase):

    def test_C2313001(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID_1 = 'C2313001_base'
        Test_Case_ID = 'C2313001'

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        core_obj = core_utility.CoreUtillityMethods(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        
        """
        Step 01: Open existing visualization (created in previous test case) in design mode
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292%2FS10664_visual_2%2FC2313001_base.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID_1, 'idis', 'S10660_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step01:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Computers and Televisions and 1 more', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step01:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step01.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step01.c: Verify first bar color")
        time.sleep(5)
        bar=['PRODUCT_CATEGORY_1:Accessories and Computers and Televisions and 1 more', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step01.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 02: Click on first riser from left - Accessories and Computers...
        The following options appear in the tooltip (in addition the filter options):
        Edit group PRODUCT_CATEGORY_1
        Rename group PRODUCT_CATEGORY_1
        Rename Accessories and Computers...
        Ungroup Accessories and Computers...
        Ungroup All
        """
        move1 = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(3)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g0!mbar!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        move_riser = driver.find_element_by_css_selector(raiser)
        utillobj.click_on_screen(move_riser, 'middle', click_type=0)
        time.sleep(3)
        resultobj.select_or_verify_lasso_filter(verify=['1 item selected','Filter Chart','Exclude from Chart','Edit group PRODUCT_CATEGORY_1','Rename group PRODUCT_CATEGORY_1','Rename Accessories and Computers...','Ungroup Accessories and Computers...','Ungroup All'],msg='Step 02: Expect to see the options appear in the tooltip (in addition the filter options):')
        
        """
        Step 03: Select Rename Accessories and Computers...
                 Text box "Rename Value" opens. Input field shows current name: Accessories and Computers and Televisions and 1 more.
        Step 04: Type in input box "Access, Comp, TV & Video" > OK
        """
        time.sleep(1)
        resultobj.select_or_verify_lasso_filter(select='Rename Accessories and Computers...')
        time.sleep(3)
        resultobj.rename_grouped_riser("Access, Comp, TV & Video", verify_name="Accessories and Computers and Televisions and 1 more", msg = 'Step03')
        time.sleep(10) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step04:a(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 04.a(iii): Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Access, Comp, TV & Video', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 04.b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04.c(i) Verify first bar color")
        time.sleep(2)
        expected_tooltip=['PRODUCT_CATEGORY_1:Access, Comp, TV & Video', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 04.d: verify the default tooltip values")       
        
        """
        Step05: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        core_obj.switch_to_new_window()
        time.sleep(15)
         
        """
        Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step05:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step05:a(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 05.a(iii): Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Access, Comp, TV & Video', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 05.b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 05.c(i) Verify first bar color")
        time.sleep(2)
        expected_tooltip=['PRODUCT_CATEGORY_1:Access, Comp, TV & Video', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 05.d: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2313001_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 06: Dismiss run window
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 07: Click Save in the toolbar > Save as "C2313001" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        Step 08: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()