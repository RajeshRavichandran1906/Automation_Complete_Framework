'''
Created on May 08, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227628
Test case Name =  Show Data via runtime menu
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run,\
    ia_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227628_TestClass(BaseTestCase):

    def test_C2227628(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227628'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
 
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
         
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
         
        """
        Step04: Drag and drop "Product,Category" to the Filter pane
        Step05: Deselect "All"
        Step06: Select "Camcorder", "Computers", "Media Player" and "Televisions"
        Step07: Click OK
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Product,Category", 1, 1,'Filter')
        time.sleep(4)
        item_list=['[All]','Camcorder','Computers','Media Player','Televisions']
        metaobj.select_or_verify_visualization_filter_values(item_list, Ok_button=True)
        time.sleep(2) 
                
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step07a: Verify filter pane has Product Category")
        time.sleep(3)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step07:a(i) Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers','Media Player','Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step07.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step07.d: Verify bar value")
        time.sleep(5)
        
        """
        Step08: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
            
        """
        Step09: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 09:a(i) Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers','Media Player','Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step 09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
        time.sleep(5)
        
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step09.d: Verify bar value")
        time.sleep(5)
        
        """
        Step10: Expand Filter menu in the lower right corner
        Step11: Click Show Data icon (first icon with grid image)
        """
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report")
        time.sleep(6)
        
        """
        Step12:Deselect "Camcorder" in the Filter prompt
        """
        propertyobj.select_or_verify_show_prompt_item('1', 'Camcorder')#selecting Computers in FF
        time.sleep(4)
        propertyobj.select_or_verify_show_prompt_item('1', 'Camcorder',verify=True,verify_type=False,msg="Step11:Verify Camcorder deselected")
                
        """
        Step13: Verify output
        """
        elem=(By.CSS_SELECTOR,'table.arPivot')
        resultobj._validate_page(elem)
        ia_runobj.verify_table_data_set("table.arPivot", "C2227628_Ds01.xlsx", "Step13: Verify Cost of Goods and product category data values")
        
        """
        Step14: Click Show Data icon to return to the Chart
        """
        time.sleep(5)
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report")
        time.sleep(5)
        
        """
        Step15: Verify output
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step 15:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step 15:a(i) Verify Y-Axis Title")
        expected_xval_list=['Computers','Media Player','Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 3, 'Step 15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 15.c: Verify first bar color")
        time.sleep(5)
        
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 15.d: Verify bar value")

        """
        Step16: Click the Undo icon in the Filter menu (icon after Grid)
        """
        time.sleep(5)
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"reset", toggle='no')
        time.sleep(5)
        
        """
        Step17: Verify output
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step17:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Cost of Goods', "Step17:a(i) Verify Y-Axis Title")
        expected_xval_list=['Camcorder','Computers','Media Player','Televisions']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step17.c: Verify first bar color")
        time.sleep(5)
        
        bar=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step17.d: Verify bar value")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227628_Actual_step17', image_type='actual',x=1, y=1, w=-1, h=-1)
           
        """
        Step18: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
               
        """
        Step18: Click Save in the toolbar
        Step18: Save as "C2158261" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
               
        """
        Step19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
#         utillobj.infoassist_api_logout()
#         time.sleep(2)        
        
if __name__ == '__main__':
    unittest.main()
        
        