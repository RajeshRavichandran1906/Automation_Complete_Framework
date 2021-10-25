'''
Created on Apr 3, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227686
Test case Name =  Change Filter Operator from Range to Equals for list with negative values
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.locators import visualization_resultarea_locators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from datetime import datetime

class C2227686_TestClass(BaseTestCase):

    def test_C2227686(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227686'
        
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double-click "Gross Profit", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Gross Profit",2,1)
         
        """
        Step 03: Double-click "Product,Subcategory", located under Product Dimension
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
         
        """
        Step 04: Drag and drop "Gross Profit" to the Filter pane
        """
        time.sleep(6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css,21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels'"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click("Gross Profit", 1, 1,"Filter")
         
        """
        Step 05: Verify Filter dialog
        Step 06: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(5)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Range'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 05.a: Verify dialog')
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "posneg_float_value")
        utillobj.asequal(float(d['posneg_float_value']),-2402.4,"Step05.b: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),3996,"Step05.c: Verify range to value")  
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric')
        time.sleep(2)
        
        """
        Step 07: Verify Canvas
        """
        time.sleep(8)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Gross Profit',1,"Step07:")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',-2402.4,'float',msg="Step07: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',3996,'int',msg="Step07: Verify filter prompt range max values")
        time.sleep(2)
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step07a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 07b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c(i) Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step 07:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1_f", yaxis_value, "Step 07:d(ii) Verify Y Axis Title") 
        expected_tooltip=['Product Subcategory:Blu Ray', 'Gross Profit:$51,771,195.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mbar",expected_tooltip, "Step 07e: verify the default tooltip values")
        time.sleep(5)
        
        """
        Step 08: Click on Prompt menu > select "Equals"
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.change_prompt_options("1","Equals")
        time.sleep(3)
        """
        Step 09: Verify Filter Prompt
        """
        time.sleep(10)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step09e: Verify [All] is checked in filter prompt")
        print(str(datetime.now()))
        """
        Step10: Select values -$2,402.40 through -$1,700.18
        """
        time.sleep(6)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '-$2,402.40')
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,801.80')
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,800.42')
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,700.18')
        print(str(datetime.now()))
        time.sleep(8)
        
        """
        Step 11: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Gross Profit',1,"Step11:")
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['-20K', '-16K', '-12K', '-8K', '-4K', '0']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Flat Panel TV', 'Gross Profit:-$15,502.10', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 11.d: Verify bar value")
        time.sleep(8)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '-$2,402.40', verify=True, verify_type=True, msg="Step11.1: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,801.80', verify=True, verify_type=True, msg="Step11.2: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,800.42', verify=True, verify_type=True, msg="Step11.3: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,700.18', verify=True, verify_type=True, msg="Step11.4: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        time.sleep(5)
        
        """
        Step 12: Right-click "Gross Profit" in the Filter pane > Edit...
        """
        metaobj.filter_tree_field_click('Gross Profit',1,1,'Edit...')
        time.sleep(5)
        
        """
        Step 13: Verify dialog
        Step 14: Click Cancel
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 06.a: Verify dialog') 
        time.sleep(2)
        item_list=['-$2,402.40','-$1,801.80','-$1,800.42','-$1,700.18' ]
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', msg = 'step13.b: Verify dialog')
        time.sleep(2)
        metaobj.create_visualization_filters('numeric', ok=False)
        
        """
        Step15: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
          
        """
        Step 16: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['-20K', '-16K', '-12K', '-8K', '-4K', '0']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Flat Panel TV', 'Gross Profit:-$15,502.10', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16.d: Verify bar value")
        time.sleep(8)
        propertyobj.select_or_verify_show_prompt_item(1, '-$2,402.40', verify=True, verify_type=True, msg="Step16.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,801.80', verify=True, verify_type=True, msg="Step16.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,800.42', verify=True, verify_type=True, msg="Step16.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,700.18', verify=True, verify_type=True, msg="Step16.4: Verify values is checked in filter prompt")
        time.sleep(8)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227686_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 17: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
          
        """
        Step 18: Click Save in the toolbar
        Step 19: Save as "C2158217" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
          
        """
        Step 20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step 21: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_ia_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
         
        """
        Step 22: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_filter_pane_field('Gross Profit',1,"Step22:")
        time.sleep(6)
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 22:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 22:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['-20K', '-16K', '-12K', '-8K', '-4K', '0']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 22:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 22.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 22.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Flat Panel TV', 'Gross Profit:-$15,502.10', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 22.d: Verify bar value")
        time.sleep(8)
        propertyobj.select_or_verify_show_prompt_item(1, '-$2,402.40', verify=True, verify_type=True, msg="Step22.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,801.80', verify=True, verify_type=True, msg="Step22.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,800.42', verify=True, verify_type=True, msg="Step22.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '-$1,700.18', verify=True, verify_type=True, msg="Step22.4: Verify values is checked in filter prompt")
        time.sleep(5)
        
        """
        Step 23: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()