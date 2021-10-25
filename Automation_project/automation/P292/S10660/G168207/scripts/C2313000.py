'''
Created on Oct 30, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2313000
TestCase Name = Paperclipping at Design Time
'''

import unittest, time
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver import ActionChains

class C2313000_TestClass(BaseTestCase):

    def test_C2313000(self):
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2313000'

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
         
        """
        Step 02: Double click Revenue and Product,Category
        """
        time.sleep(4)
        metaobj.datatree_field_click("Revenue",2,1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 180)
         
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 180)
        time.sleep(2)
         
        """
        Step 03: Right click Revenue > Sort > Descending
        """
        metaobj.querytree_field_click("Revenue", 1, 1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Sort')
        utillobj.select_or_verify_bipop_menu('Sort')
        utillobj.select_or_verify_bipop_menu('Descending')
         
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step03:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step03:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Computers', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step03:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step03.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step03.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Stereo Systems', 'Revenue:$291,294,933.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step03: Verify bar value")
        time.sleep(5)
         
        """
        Step 04: Lasso Accessories, Computers, Televisions and Video Production > Group Product,Category
        """
        time.sleep(6)
        raiser="#MAINTABLE_wbody1 [class*='riser!s0!g3!mbar!']"
        utillobj._validate_page((By.CSS_SELECTOR,raiser))
        browser = utillobj.parseinitfile('browser')
        move_riser = driver.find_element_by_css_selector(raiser)
        if browser == 'Firefox':
            utillobj.click_type_using_pyautogui(move_riser)
        else:
            action = ActionChains(driver)
            action.move_to_element(move_riser).perform()
        resultobj.create_lasso('MAINTABLE_wbody1','rect', 'riser!s0!g3!mbar', target_tag='rect', target_riser='riser!s0!g6!mbar')
        time.sleep(2)
        resultobj.select_or_verify_lasso_filter(select='Group Product,Category Selection')
         
        """
        Step 05: Review the preview and the data and query panes. 
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step05:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step05:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Computers and Televisions and 1 more', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step05:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step05.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step05.c: Verify first bar color")
        time.sleep(5)
        bar=['PRODUCT_CATEGORY_1:Accessories and Computers and Televisions and 1 more', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step05.d: Verify bar value")
        time.sleep(5)
        metaobj.verify_data_pane_field("Customer", "PRODUCT_CATEGORY_1", 1, "Step 05.e: Verify the PRODUCT_CATEGORY_1 has been added to the Data pane")
        metaobj.verify_query_pane_field("Horizontal Axis", "PRODUCT_CATEGORY_1", 2, "Step 05.f: Verify the Product,Category_1 has been added to the query pane")
        
        """
        Step 06: Review the fex. The fex contains a define.
        -*COMPONENT=Define_wf_retail_lite
        DEFINE FILE baseapp/wf_retail_lite
        PRODUCT_CATEGORY_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ( 'Accessories' 'Accessories and Computers and Televisions and 1 more' 'Computers' 'Accessories and Computers and Televisions and 1 more' 'Televisions' 'Accessories and Computers and Televisions and 1 more' 'Video Production' 'Accessories and Computers and Televisions and 1 more' ELSE 'Default');
        PRODUCT_CATEGORY_1 = IF PRODUCT_CATEGORY_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ELSE PRODUCT_CATEGORY_1;
        END
        """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        time.sleep(8)
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text.strip().split('\n')
        expected_code=['-*COMPONENT=Define_wf_retail_lite', 'DEFINE FILE baseapp/wf_retail_lite', "PRODUCT_CATEGORY_1/A100=DECODE WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ( 'Accessories' 'Accessories and Computers and Televisions and 1 more' 'Computers' 'Accessories and Computers and Televisions and 1 more' 'Televisions' 'Accessories and Computers and Televisions and 1 more' 'Video Production' 'Accessories and Computers and Televisions and 1 more' ELSE 'Default');", "PRODUCT_CATEGORY_1 = IF PRODUCT_CATEGORY_1 EQ 'Default' THEN WF_RETAIL_LITE.WF_RETAIL_PRODUCT.PRODUCT_CATEGORY ELSE PRODUCT_CATEGORY_1;", 'END']
        vp_text = 'Step 06. Review the fex. The fex contains a define'
        for label_x in expected_code:
            if label_x in fex_code:
                statex= True
            else:
                statex=False
                break
        utillity.UtillityMethods.asequal(self, statex, True, vp_text) 
        driver.switch_to_default_content()
        time.sleep(2)
        close_fexcode_btn=driver.find_element_by_css_selector("#showFexOKBtn img")
        utillobj.default_left_click(object_locator=close_fexcode_btn, action_move=True)
        time.sleep(4)
        
        """
        Step07: Click Run
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
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step07:a(ii) Verify Y-Axis Title")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 07.a(iii): Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories and Computers and Televisions and 1 more', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07.b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c(i) Verify first bar color")
        time.sleep(2)
        expected_tooltip=['PRODUCT_CATEGORY_1:Accessories and Computers and Televisions and 1 more', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 07.d: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2313000_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 08: Save visualization with name C2313000 and close.
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 09: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2313000.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10660_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'PRODUCT_CATEGORY_1', "Step09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step09:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories and Computers and Televisions and 1 more', 'Stereo Systems', 'Media Player', 'Camcorder']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step09.c: Verify first bar color")
        time.sleep(5)
        bar=['PRODUCT_CATEGORY_1:Accessories and Computers and Televisions and 1 more', 'Revenue:$369,359,230.08', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!", bar,"Step09.d: Verify bar value")
        time.sleep(5)
         
        """
        Step 10: Logout using API (without saving): http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()