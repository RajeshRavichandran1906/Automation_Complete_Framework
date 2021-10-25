'''
Created on Apr 24, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227597
Test case Name =  Design time 'Filter Chart'
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227597_TestClass(BaseTestCase):

    def test_C2227597(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227597'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
#         port_no = utillobj.parseinitfile('httpport')
#         if port_no == '8080':
#             utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
#         else:
#             utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','S10032_visual_1', 'mrid01', 'mrpass01')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Double-click "Cost of Goods"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
        
        """
        Step 03: Double-click "Product,Category"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        
        """
        Step 04: Hover over "Media Player" riser (bar) > Select "Filter Chart"
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","riser!s0!g3!mbar", 'Filter Chart')
        time.sleep(2) 
          
        """
        Step05: Verify Canvas 
        """        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step05a: Verify filter pane has Product Category")
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 05:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 05:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 05:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 05.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 05.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 05.d: Verify bar value")
        time.sleep(5)
        
        """
        Step06: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
            
        """
        Step07: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10) 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 07:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 7.d: Verify bar value")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227645_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step08: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
              
        """
        Step09: Click Save in the toolbar
        Step10: Save as "C2158261" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
              
        """
        Step11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step12: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step13: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step13a: Verify filter pane has Product Category")
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step13:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step13:a(i) Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step13.d: Verify bar value")
        time.sleep(5)
          
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()
        
        