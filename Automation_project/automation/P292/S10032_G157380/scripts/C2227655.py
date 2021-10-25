'''
Created on Mar 23, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227655
Test case Name =  Reposition Filter Prompts 
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class C2227655_TestClass(BaseTestCase):

    def test_C2227655(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227655'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Double click "Cost of Goods" and "Revenue" located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
        metaobj.datatree_field_click("Revenue",2,1)
        
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.datatree_field_click("Product,Category", 2, 1)
         
        """
        Step 04: Expand "Sales_Related" > "Transaction Date,Simple" > Drag and drop "Sale,Quarter" into the Columns bucket (Matrix)
        """
        time.sleep(4)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click('Sale,Quarter', 1, 1, 'Add To Query','Columns')
        
        """
        Step 05: Drag and drop "Product,Category" into the Filter pane > click OK
        """
        time.sleep(4)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 4)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        metaobj.create_visualization_filters("alpha")        
        time.sleep(6)
        
        
        """
        Step 06: Drag and drop "Sale,Year" into the Filter pane > click OK
        """
        time.sleep(4)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Filter")
        metaobj.create_visualization_filters("numeric")        
        time.sleep(6)
         
         
        """
        Step 07: Drag and drop "Revenue" into the Filter pane > click OK
        """
        time.sleep(4)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("Revenue", 1, 1,"Filter")
        metaobj.create_visualization_filters("numeric")        
        time.sleep(6)
         
        """
        Step 08: Verify canvas (scroll down to verify third Prompt is displayed)
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        try:
            if self.driver.find_element_by_css_selector("div#ar_Prompt_3 table div.arFilterButton").is_displayed():
                utillobj.asequal(True, True, 'Step 08.a: Verify third Prompt is displayed')
        except NoSuchElementException:
            utillobj.asequal(True, False, 'Step 08.a: Verify third Prompt is not displayed')
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 4)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 28, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step 08.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Product Category:Media Player', 'Cost of Goods:$46,650,488.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", bar, "Step 08: Verify bar value")
         
        
        """
        Step 09: Click "Prompts" label at the top of the Prompt panels > Drag and drop Prompt panels on top, as displayed on the screen shot, to re-position panels.
        """
        
        d1=utillobj.get_css_value(self.driver.find_element_by_css_selector("#resultArea div[id^='BoxLayoutFilterBox']"), "left", "top", "width", "height")
        print(d1)
        time.sleep(8)
#         Elem1= self.driver.find_element_by_css_selector("#resultArea div[id^='BoxLayoutMiniWindow']")
#         Elem2= self.driver.find_element_by_css_selector("#resultArea div[id^='BoxLayoutFilterBox']")
        resultobj.drag_and_drop_visualization("Prompts","Bar Stacked1","top_most", Prompts = True)
        time.sleep(5)
        
        """
        Step 10: Verify Filter Prompts are re-positioned
        """
        d2=utillobj.get_css_value(self.driver.find_element_by_css_selector("#resultArea div[id^='BoxLayoutFilterBox']"), "left", "top", "width", "height")
        print(d2)
        time.sleep(8)
        if int(d1['width']) < int(d2['width']) and int(d1['top']) == int(d2['top']) and int(d1['left']) > int(d2['left']) and int(d1['height']) > int(d2['height']):
            print("Step 10: Verify Filter Prompts are re-positioned - passed")
        else:
            print("Step 10: Verify Filter Prompts are re-positioned - Failed")
            
        """
        Step 11: Click Run
        """
        time.sleep(10) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
         
        """
        Step 12: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g3!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 4)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 28, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step 12.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Product Category:Media Player', 'Cost of Goods:$46,650,488.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", bar, "Step 12: Verify bar value")
         
        """
        Step 13: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 14: Click Save
        Step 15: Save as "C2158173" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
         
        """
        Step 16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step 17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158172.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(20)
   
        """
        Step 18: Verify canvas
        """
        
        chart_type_css="rect[class*='riser!s0!g3!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 4)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 18:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 28, 'Step 18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step 18.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Product Category:Media Player', 'Cost of Goods:$46,650,488.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", bar, "Step 18: Verify bar value")
         
        """
        Step 19: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
        
         
        """
        Step 20: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g3!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 4)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 20:a(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 20:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 28, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step 20.c: Verify first bar color")
        time.sleep(8)
        bar=['Sale Quarter:1', 'Product Category:Media Player', 'Cost of Goods:$46,650,488.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", bar, "Step 20: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$VBOX']")
        utillobj.take_screenshot(ele,'C2227655_Actual_step20', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 21: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(5)
        
        """
        Step 22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        
        
if __name__ == "__main__":
    unittest.main()        