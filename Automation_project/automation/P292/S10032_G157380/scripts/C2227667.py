'''
Created on Mar 31, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227667
Test case Name =  Sort Descending and Ascending
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227667_TestClass(BaseTestCase):

    def test_C2227667(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227667'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
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
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        
        """
        Step 04: Drag and drop "Product,Category" to the Filter pane
        Step 05: Click OK
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Product,Category", 1, 1,"Filter")
        metaobj.create_visualization_filters("alpha")        
        time.sleep(6)
        
        """
        Step 06: Select values in the Filter Prompt: "Media Player" and "Stereo Systems"
        Step 07: Verify Canvas
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player') 
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', 'Stereo Systems')  
        
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 07: Verify bar value")
             
        """
        Step08: Right-click "Product,Category" in the Filter pane > Select Edit...
        Step09: Check off value: "Video Production" > Click OK
        Step10: Verify Canvas
        """
        metaobj.filter_tree_field_click('Product,Category', 1, 1, 'Edit...')
        metaobj.create_visualization_filters('alpha',['GridItems',['Video Production']])
        
        time.sleep(6)        
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player', verify=True,verify_type=True,msg="Step10: Verify Media Player checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Stereo Systems', verify=True,verify_type=True,msg="Step10: Verify Stereo Systems checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Video Production', verify=True,verify_type=True,msg="Step10: Verify Video Production checked")
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems','Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g2!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Video Production', 'Cost of Goods:$40,105,657.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 10: Verify bar value")
        
        """
        Step11: Click Save
        Step12: Click Save as "C2158200" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
           
        """
        Step13: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step14: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_ia_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
           
        """
        Step15: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 15:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 15:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Media Player', 'Stereo Systems', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 15: Verify bar value")
         
        time.sleep(6)        
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player', verify=True,verify_type=True,msg="Step15: Verify Media Player checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Stereo Systems', verify=True,verify_type=True,msg="Step15: Verify Stereo Systems checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Video Production', verify=True,verify_type=True,msg="Step15: Verify Video Production checked")
         
        """
        Step 16: Check off value "Computers" in the Filter Prompt
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item('1', 'Computers')
        time.sleep(5)      
                 
        """
        Step 17: Verify Canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step17:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step17:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Computers', 'Media Player', 'Stereo Systems', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step17.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step17: Verify bar value")
         
        propertyobj.select_or_verify_show_prompt_item('1', 'Computers', verify=True,verify_type=True,msg="Step17: Verify Computers checked")
        time.sleep(5) 
       
        """
        Step 18: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
           
        """
        Step 19: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 19:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 19:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Computers', 'Media Player', 'Stereo Systems', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 19.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 19: Verify bar value")
        
        time.sleep(6)        
        propertyobj.select_or_verify_show_prompt_item('1', 'Media Player', verify=True,verify_type=True,msg="Step19: Verify Media Player checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Stereo Systems', verify=True,verify_type=True,msg="Step19: Verify Stereo Systems checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Video Production', verify=True,verify_type=True,msg="Step19: Verify Video Production checked")
        propertyobj.select_or_verify_show_prompt_item('1', 'Computers', verify=True,verify_type=True,msg="Step19: Verify Computers checked")
                 
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227667_Actual_step19', image_type='actual',x=1, y=1, w=-1, h=-1) 
            
        """
        Step20: Close the output window
        Step21: Logou
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)          
                 

        
if __name__ == '__main__':
    unittest.main()
        