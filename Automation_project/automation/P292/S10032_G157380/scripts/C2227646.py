'''
Created on Apr 13, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227646
Test case Name =  Date Filter with decomposed date format YYMDq
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227646_TestClass(BaseTestCase):

    def test_C2227646(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227646'
        
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
        Step 03: Expand Dimension "Sales_Related" > "Trasaction Date,Components" > Double click "Sale,Year/Quarter"
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Sale,Year/Quarter", 2, 1)
        
        """
        Step 04: Drag and drop "Sale,Year/Quarter" to the Filter pane
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 24)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.datatree_field_click("Sale,Year/Quarter", 1, 1,"Filter")
        time.sleep(2)   
        
        """
        Step 05: Verify Filter dialog
        Step 06: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'Range',"Step05.a: Verify Operator dialog")
        
        elem1=driver.find_element_by_css_selector("#avfFromDateComboBox")
        d=utillobj.get_attribute_value(elem1, 'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'2011 Q1',"Step05.b: Verify range from value")
        
        elem1=driver.find_element_by_css_selector("#avfToDateComboBox")
        d=utillobj.get_attribute_value(elem1, 'dom_visible_text')
        print(d['dom_visible_text'])
        utillobj.asequal(d['dom_visible_text'],'2017 Q1',"Step05.c: Verify range to value")  
        
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)
        
        
        """
        Step07: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','Q1 2011',msg="Step07: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','Q1 2017',msg="Step07: Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 24)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Year/Quarter',1,"Step07.a:")
        time.sleep(3)
        xaxis_value="Sale Year/Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        expected_xval_list=['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 24, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year/Quarter:2016 Q4', 'Cost of Goods:$96,808,478.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Year/Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g23!mbar", bar, "Step 07.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 08: Right click "Sale,Year/Quarter" filter in the Filter pane > Select Edit
        """
        metaobj.filter_tree_field_click('Sale,Year/Quarter',1,1,'Edit...')
        time.sleep(5)
        
        """
        Step09: Click "From" dropdown box > verify list of values
        Step10: Select "2013 Q4" > click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avfFromDateComboBox div[id^='BiButton']")
        elem = '2013 Q4'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['2011 Q1', '2011 Q2', '2011 Q3', '2011 Q4', '2012 Q1', '2012 Q2', '2012 Q3', '2012 Q4', '2013 Q1', '2013 Q2', '2013 Q3', '2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4', '2017 Q1'], msg='Step 09.a: Verify dialog')
        time.sleep(3)
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)
        
        
        """
        Step11: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','Q4 2013',msg="Step11: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','Q1 2017',msg="Step11: Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 13)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Year/Quarter',1,"Step07.a:")
        time.sleep(3)
        xaxis_value="Sale Year/Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        expected_xval_list=['2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 13, 'Step 11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year/Quarter:2016 Q4', 'Cost of Goods:$96,808,478.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Year/Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g12!mbar", bar, "Step 11.d: Verify bar value")
        time.sleep(5)
        
        """
        Step12: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
          
        """
        Step 13: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 13)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min','Q4 2013',msg="Step13:Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max','Q1 2017',msg="Step13: Verify filter prompt range max values")
        time.sleep(3)
        xaxis_value="Sale Year/Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 13:a(i) Verify X-Axis Title")
        expected_xval_list=['2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 13, 'Step 13b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year/Quarter:2016 Q4', 'Cost of Goods:$96,808,478.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Year/Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g12!mbar", bar, "Step 13.d: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227646_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 14: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
            
        """
        Step 15: Click Save in the toolbar
        Step 16: Save as "C2158206" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
            
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
            
        """
        Step 18: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
           
        """
        Step 19: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 13)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(3)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min','Q4 2013',msg="Step19:Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max','Q1 2017',msg="Step19: Verify filter prompt range max values")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Sale,Year/Quarter',1,"Step19.a:")
        time.sleep(3)
        xaxis_value="Sale Year/Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 19:a(i) Verify X-Axis Title")
        expected_xval_list=['2013 Q4', '2014 Q1', '2014 Q2', '2014 Q3', '2014 Q4', '2015 Q1', '2015 Q2', '2015 Q3', '2015 Q4', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        expected_yval_list=['0', '30M', '60M', '90M', '120M', '150M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 13, 'Step 19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 19.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year/Quarter:2016 Q4', 'Cost of Goods:$96,808,478.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Year/Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g12!mbar", bar, "Step 19.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()