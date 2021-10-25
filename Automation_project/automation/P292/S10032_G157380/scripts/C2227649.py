'''
Created on Apr 20, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227649
Test case Name =  Filter with Integer field 'Year'
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227649_TestClass(BaseTestCase):

    def test_C2227649(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227649'
        
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
        Step 03: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > Double click "Sale,Year"
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
        Step 06: Change "From" value to 2014
        Step 07: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'Range',"Step05.a: Verify Operator dialog")
        
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        print(d['int_value'])
        utillobj.asequal(d['int_value'],"2011","Step05.b: Verify range to value")
        
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        print(d['int_value'])
        utillobj.asequal(d['int_value'],"2017","Step05.c: Verify range to value")   
        
        metaobj.create_visualization_filters('numeric',['From','2014'])
        time.sleep(5)
        
        """
        Step08: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step08: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step08: Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step08.a:")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 08:a(i) Verify X-Axis Title")
        expected_xval_list=['2014','2015','2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 08.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2016', 'Cost of Goods:$325,821,316.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 08.d: Verify bar value")
        time.sleep(5)
        
        """
        Step09: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
          
        """
        Step 10: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)  
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2014,'int',msg="Step10:Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',2017,'int',msg="Step10: Verify filter prompt range max values")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        expected_xval_list=['2014','2015','2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 10b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2016', 'Cost of Goods:$325,821,316.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 10.d: Verify bar value")
        time.sleep(5)
        
        """
        Step11: Drag left slider to the right > change value to 2015
        """
        time.sleep(5)
        propertyobj.move_slider_measure('#sliderPROMPT_1','min', 'right', 1,'int') #2172012.85
        
        """
        Step 12: Verify output window
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        driver.maximize_window()
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',2015,'int',msg="Step12:Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',2017,'int',msg="Step12: Verify filter prompt range max values")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        expected_xval_list=['2015', '2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 2, 'Step 12b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2016', 'Cost of Goods:$325,821,316.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 12.d: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227649_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        
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
        Step 14: Click Save in the toolbar
        Step 15: Save as "C2158175" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
            
        """
        Step 16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
            
        """
        Step 17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158175.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
        
        """
        Step 18: Verify Canvas
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
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',2014,'int',msg="Step18:Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',2017,'int',msg="Step18: Verify filter prompt range max values")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Sale,Year',1,"Step18.a:")
        time.sleep(3)
        xaxis_value="Sale Year"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 18:a(i) Verify X-Axis Title")
        expected_xval_list=['2014','2015','2016']
        expected_yval_list=['0', '100M', '200M', '300M', '400M', '500M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 3, 'Step 18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 18.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Year:2016', 'Cost of Goods:$325,821,316.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Sale Quarter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 18.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()