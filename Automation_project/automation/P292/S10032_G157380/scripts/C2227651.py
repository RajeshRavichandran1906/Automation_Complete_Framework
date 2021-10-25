'''
Created on Apr 19, 2017

@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227651
Test case Name =  Filter with Integer field 'Month'
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon, visualization_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227651_TestClass(BaseTestCase):

    def test_C2227651(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227651'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        runobj = visualization_run.Visualization_Run(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        metaobj.datatree_field_click("Gross Profit",2,1)
                
        """
        Step03: Expand Product Dimension > Double click "Product,Category"
        Step04: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > Drag and drop "Sale,Month" into the Rows bucket in the Query pane
        """
        time.sleep(5)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.datatree_field_click("Sale,Month", 1, 1,"Add To Query", 'Rows')
                
        """
        Step05: Drag and drop "Sale,Month" into the Filter pane
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 72)
        metaobj.datatree_field_click("Sale,Month", 1, 1,"Filter")        
        time.sleep(6)
                
        """
        Step06: Verify Filter dialog
        Step07: Click "Operators" dropdown box > select "Equal to"
        Step08: Uncheck values 1 through 6
        Step09: Click OK
        """  
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
                      
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"1","Step06: Verify From in Filter dialog")
                
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"12","Step06: Verify To in Filter dialog")
 
        l=['1','2','3','4','5','6']               
        metaobj.create_visualization_filters('numeric',['Operator','Equal to'],['GridItems',l])
        time.sleep(3)
                  
        """
        Step10: Verify Canvas
        """
         
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', '7',verify=True, verify_type=True,msg="Step10: Verify 7 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '8',verify=True, verify_type=True,msg="Step10: Verify 8 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '9',verify=True, verify_type=True,msg="Step10: Verify 9 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '10',verify=True, verify_type=True,msg="Step10: Verify 10 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '11',verify=True, verify_type=True,msg="Step10: Verify 11 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '12',verify=True, verify_type=True,msg="Step10: Verify 12 checked in prompt")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 48)
        time.sleep(2) 
        metaobj.verify_filter_pane_field('Sale,Month',1,"Step08: Verify 'Sale,Month' appears in filter pane")        
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step10:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step10:d(ii) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        browser=utillobj.parseinitfile('browser')
        time.sleep(2)
#         parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels!m1!']"
#         resultobj.wait_for_property(parent_css, 6, string_value='5M', with_regular_exprestion=True)
        if browser in['Chrome','IE']:
            expected_yval_list=['0', '5M','10M','15M','20M','25M','30M','35M']
        else:
            expected_yval_list=['0', '7M', '14M', '21M', '28M', '35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 84, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step10.c: Verify first bar color")
        time.sleep(5)
        expected=['7', '8', '9', '10', '11', '12']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step10: Verify Row header")
           
        bar=['Sale Month:7', 'Product Category:Stereo Systems', 'Cost of Goods:$16,142,228.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Quarter', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", bar, "Step10: Verify bar value")
                  
        """
        Step11: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)    
                  
        """
        Step12: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        propertyobj.select_or_verify_show_prompt_item('1', '7',verify=True, verify_type=True,msg="Step12: Verify 7 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '8',verify=True, verify_type=True,msg="Step12: Verify 8 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '9',verify=True, verify_type=True,msg="Step12: Verify 9 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '10',verify=True, verify_type=True,msg="Step12: Verify 10 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '11',verify=True, verify_type=True,msg="Step12: Verify 11 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '12',verify=True, verify_type=True,msg="Step12: Verify 12 checked in prompt")
        time.sleep(5)  
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step12:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step12:d(ii) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M','30M','35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 84, 'Step12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step12.c: Verify first bar color")
        time.sleep(5)
        expected=['7', '8', '9', '10', '11', '12']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step12: Verify Row header")
            
        bar=['Sale Month:7', 'Product Category:Stereo Systems', 'Cost of Goods:$16,142,228.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Quarter', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", bar, "Step12: Verify bar value")
                            
        """
        Step13: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
       
        """
        Step14: Click Save
        Step15: Click Save as "C2158200" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                   
        """
        Step16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
                 
        """
        Step18: Verify Canvas
        """
        elem1=(By.CSS_SELECTOR, "[class*='riser!s']")
        resultobj._validate_page(elem1)
        time.sleep(15)
        metaobj.verify_filter_pane_field('Sale,Month',1,"Step18: Verify 'Sale,Month' appears in filter pane")
        propertyobj.select_or_verify_show_prompt_item('1', '7',verify=True, verify_type=True,msg="Step18: Verify 7 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '8',verify=True, verify_type=True,msg="Step18: Verify 8 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '9',verify=True, verify_type=True,msg="Step18: Verify 9 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '10',verify=True, verify_type=True,msg="Step18: Verify 10 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '11',verify=True, verify_type=True,msg="Step18: Verify 11 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '12',verify=True, verify_type=True,msg="Step18: Verify 12 checked in prompt")
        time.sleep(5) 
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g4!mbar!r0!c0']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True)
        time.sleep(3) 
#         parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels!m1!']"
#         resultobj.wait_for_property(parent_css, 6, string_value='5M', with_regular_exprestion=True)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step18:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step18:d(ii) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        browser=utillobj.parseinitfile('browser')
        time.sleep(2)
#         parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-labels!m1!']"
#         resultobj.wait_for_property(parent_css, 6, string_value='5M', with_regular_exprestion=True)
        if browser in['Chrome','IE']:
            expected_yval_list=['0', '5M','10M','15M','20M','25M','30M','35M']
        else:
            expected_yval_list=['0', '7M', '14M', '21M', '28M', '35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 84, 'Step18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step18.c: Verify first bar color")
        time.sleep(5)
        expected=['7', '8', '9', '10', '11', '12']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step18: Verify Row header")
            
        bar=['Sale Month:7', 'Product Category:Stereo Systems', 'Cost of Goods:$16,142,228.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Quarter', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", bar, "Step18: Verify bar value")
             
        """
        Step19: Check off values 3, 4 and 5 in the Filter Prompt
        Step20: Verify Canvas
        """
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', '3')
        propertyobj.select_or_verify_show_prompt_item('1', '4')
        propertyobj.select_or_verify_show_prompt_item('1', '5')
          
        time.sleep(2)
        propertyobj.select_or_verify_show_prompt_item('1', '3',verify=True, verify_type=True,msg="Step19: Verify 3 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '4',verify=True, verify_type=True,msg="Step19: Verify 4 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '5',verify=True, verify_type=True,msg="Step19: Verify 5 checked in prompt")
        resultobj.wait_for_property("#MAINTABLE_wbody1 svg g.risers>g>rect[class^='riser']", 126)
        time.sleep(5)
        expected=['3','4','5','7', '8', '9', '10']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step20: Verify Row header")
          
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 126, 'Step20: Verify the total number of risers displayed on preview')
          
        """
        Step21: Click "Save"
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(2)
         
        """
        Step22: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15) 
         
        """
        Step23: Verify output
        """
        elem1=(By.CSS_SELECTOR, "rect[class*='riser!s']")
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        xaxis_value="Product Category"
        legend=["Cost of Goods", 'Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step23:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step23:d(ii) Verify Y-Axis Title")
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 54)
        time.sleep(2)
        expected_xval_list=['Accessories','Camcorder', 'Computers','Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M', '0', '7M', '14M', '21M', '28M', '35M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step23:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 126, 'Step23.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", "bar_blue", "Step23.c: Verify first bar color")
        time.sleep(5)
        expected=['3','4','5','7', '8', '9', '10', '11', '12']
        runobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Month', expected,"Step23: Verify Row header")
        time.sleep(5)
        bar=['Sale Month:3', 'Product Category:Stereo Systems', 'Cost of Goods:$17,012,927.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Quarter', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g4!mbar!r0!c0", bar, "Step23: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227651_Actual_Step23', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', '3',verify=True, verify_type=True,msg="Step23: Verify 3 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '4',verify=True, verify_type=True,msg="Step23: Verify 4 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '5',verify=True, verify_type=True,msg="Step23: Verify 5 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '7',verify=True, verify_type=True,msg="Step23: Verify 7 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '8',verify=True, verify_type=True,msg="Step23: Verify 8 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '9',verify=True, verify_type=True,msg="Step23: Verify 9 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '10',verify=True, verify_type=True,msg="Step23: Verify 10 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '11',verify=True, verify_type=True,msg="Step23: Verify 11 checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', '12',verify=True, verify_type=True,msg="Step23: Verify 12 checked in prompt")
         
        """
        Step24: Close the output window
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
        Step25: Logout
        """
if __name__ == '__main__':
    unittest.main()