'''
Created on Oct 31, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313967
TestCase Name = Rename group via tooltip
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata
from common.lib import utillity

class C2313967_TestClass(BaseTestCase):

    def test_C2313967(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID_1 = 'C2313001'
        Test_Case_ID = 'C2313967'

        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        
        """
        Step 01: Open existing visualization (created in previous test case) in design mode "Continue from previous testcase: C2313001"
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2313001.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID_1, 'idis', 'S10660_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step01:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step01:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Access, Comp, TV & Video', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step01:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step01.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step01.c: Verify first bar color")
        time.sleep(5)
        expected_tooltip=['PRODUCT_CATEGORY_1:Access, Comp, TV & Video', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", expected_tooltip,"Step01.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 02: Click the group value riser "Access,Comp, TV & Video" > Rename group PRODUCT_CATEGORY_1
        """
        move1 = driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(3)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g0!mbar!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        move_riser = driver.find_element_by_css_selector(raiser)
        utillobj.click_on_screen(move_riser, 'middle', click_type=0)
        time.sleep(3)
        resultobj.select_or_verify_lasso_filter(verify=['1 point', 'Filter Chart', 'Exclude from Chart', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Rename Access, Comp, TV & Video...', 'Ungroup Access, Comp, TV & Video...', 'Ungroup All'],msg='Step 02: Expect to see the options appear in the tooltip')
        time.sleep(1)
        resultobj.select_or_verify_lasso_filter(select='Rename group PRODUCT_CATEGORY_1')
        time.sleep(3)
        
        """
        Step 03: Type in the Rename Group input: "Categories" > OK
        Group name changes to "Categories" on X axis title, in query pane and in data pane.
        """
        resultobj.rename_grouped_riser("Categories", verify_name="PRODUCT_CATEGORY_1", msg = 'Step03')
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Categories', "Step03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Access, Comp, TV & Video', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step03:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step03.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step03.c: Verify first bar color")
        time.sleep(5)
        expected_tooltip=['Categories:Access, Comp, TV & Video', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", expected_tooltip,"Step03.d: Verify bar value")
        metaobj.verify_query_pane_field("Horizontal Axis", "Categories", 2, "Step 05.f: Verify the Categories has been added to the query pane")
        
        """
        Step04: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
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
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Categories', "Step04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step04:a(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 04.a(iii): Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Access, Comp, TV & Video', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 04.b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 04.c(i) Verify first bar color")
        time.sleep(2)
        expected_tooltip=['Categories:Access, Comp, TV & Video', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 04.d: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2313001_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 05: Close output, save and close design window.
        """
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
        Step 06: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()