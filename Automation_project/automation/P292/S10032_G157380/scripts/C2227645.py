'''
Created on Apr 13, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227645
Test case Name =  Date Filter with decomposed date format YYMDy
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class C2227645_TestClass(BaseTestCase):

    def test_C2227645(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227645'
        
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
        Step 02: Double-click "Cost of Goods" and "Gross Profit", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        metaobj.datatree_field_click("Gross Profit",2,1)
        
        """
        Step 03: Expand Dimension "Sales_Related" > "Trasaction Date,Components" > Double click "Sale,Year"
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Sale,Year", 2, 1)
        
        """
        Step 04: Drag and drop "Sale,Year" to the Filter pane
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.datatree_field_click("Sale,Year", 1, 1,"Filter")
        time.sleep(2)   
        
        
        """
        Step 05: Verify Filter dialog
        Step 06: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'(None)',"Step05: Verify Aggregation in Filter dialog")
        
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Range',"Step05.a: Verify Operator dialog")
        
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        print(d['int_value'])
        utillobj.asequal(d['int_value'],"2011","Step05.b: Verify range to value")
        
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        print(d['int_value'])
        utillobj.asequal(d['int_value'],"2017","Step05.c: Verify range to value")  
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)
         
         
        """
        Step07: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2011,'int',msg="Step07: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step07: Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step07.a:")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        expected_xval_list=['2011', '2012', '2013', '2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 6, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2016', 'Cost of Goods:$325,821,316.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g5!mbar", bar, "Step 07.d: Verify bar value")
        time.sleep(5)
         
        """
        Step08: Drag left slider handle to the right > change "From" value to 2014
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        action1 = ActionChains(self.driver)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser=utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_on_screen(move1, coordinate_type='right', click_type=0)
            time.sleep(5)
            utillobj.click_type_using_pyautogui(move1)
            start_point=driver.find_elements_by_css_selector("#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']")
            utillobj.click_on_screen(start_point[0], coordinate_type='middle', click_type=0)
            propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1,'int') #2172012.85
            chart_type_css="rect[class*='riser!s0!g0!mbar']"
            elem1=(By.CSS_SELECTOR, chart_type_css)
            resultobj._validate_page(elem1)
            utillobj.click_on_screen(move1, coordinate_type='right', click_type=0)
            time.sleep(5)
            utillobj.click_type_using_pyautogui(move1)
            start_point=driver.find_elements_by_css_selector("#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']")
            utillobj.click_on_screen(start_point[0], coordinate_type='middle', click_type=0)
            propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1,'int') #2172012.85
            chart_type_css="rect[class*='riser!s0!g0!mbar']"
            elem1=(By.CSS_SELECTOR, chart_type_css)
            resultobj._validate_page(elem1)
            utillobj.click_on_screen(move1, coordinate_type='right', click_type=0)
            time.sleep(5)
            utillobj.click_type_using_pyautogui(move1)
            start_point=driver.find_elements_by_css_selector("#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']")
            utillobj.click_on_screen(start_point[0], coordinate_type='middle', click_type=0)
            propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1,'int') #2172012.85
        else:
            action1.move_to_element_with_offset(move1,1,1).perform()
            time.sleep(10)
            propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 3,'int') #2172012.85
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        """
        Step09: Verify Canvas 
        """
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        browser=utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step09: Verify filter prompt range min values")
        if browser in ['IE', 'Chrome']:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step09: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step09: Verify filter prompt range max values")
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step07.a:")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        expected_xval_list=['2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2014', 'Cost of Goods:$90,376,789.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 09.d: Verify bar value")
        time.sleep(5)
         
        """
        Step10: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
           
        """
        Step 11: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        if browser == 'Firefox':
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2014,'int',msg="Step11:Verify filter prompt range min values")
        if browser in ['IE', 'Chrome']:
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2014,'int',msg="Step11: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',2017,'int',msg="Step11: Verify filter prompt range max values")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        expected_xval_list=['2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 11b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2014', 'Cost of Goods:$90,376,789.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 11.d: Verify bar value")
        time.sleep(5)
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227645_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 12: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
             
        """
        Step 13: Click Save in the toolbar
        Step 14: Save as "C2158261" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
             
        """
        Step 15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
        """
        Step 16: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
            
        """
        Step 17: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(3)
        if browser == 'Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step17:Verify filter prompt range min values")
        if browser in ['IE', 'Chrome']:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step17: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step17: Verify filter prompt range max values")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step17.a:")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 17:a(i) Verify X-Axis Title")
        expected_xval_list=['2014', '2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 17:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 17.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 017c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2014', 'Cost of Goods:$90,376,789.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 17.d: Verify bar value")
        time.sleep(5)
         
        """
        Step 18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()
        
        