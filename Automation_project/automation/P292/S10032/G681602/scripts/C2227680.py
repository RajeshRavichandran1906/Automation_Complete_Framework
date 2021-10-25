'''
Created on Apr 7, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227680
Test case Name =  Hide Filter Prompt from dialog
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


class C2227680_TestClass(BaseTestCase):

    def test_C2227680(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227680'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)

        """
        Step 02: Double-click "Cost of Goods, Local Currency", located under Sales Measures
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods,Local Currency",2,1)
        
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
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        time.sleep(2)   
        metaobj.create_visualization_filters('alpha')
        time.sleep(2)
        
        """
        Step 06: Drag and drop "Cost of Goods, Local Currency" to the Filter pane
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_filter('Cost of Goods,Local Currency', 1)
        time.sleep(5)
        
        """
        Step 07: Verify Filter dialog
        Step 08: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(5)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Range'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 07.a: Verify dialog')
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        print(d['float_value'])
        utillobj.asequal(float(d['float_value']),10.12,"Step07.b: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        print(d['float_value'])
        utillobj.asequal(float(d['float_value']),3620014.67,"Step07.c: Verify range to value")  
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)
        
        """
        Step09: Edit "Cost of Goods, Local Currency" filter on canvas > Drag left slider handle to the right at value > 2830300.3
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        action1 = ActionChains(self.driver)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser=utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_on_screen(move1, coordinate_type='bottom_middle', click_type=0)
            time.sleep(5)
            utillobj.click_type_using_pyautogui(move1)
            start_point=driver.find_elements_by_css_selector("#ar_Prompt_2 div[id^='slider_'] [class^='ui-slider-handle']")
            utillobj.click_on_screen(start_point[0], coordinate_type='middle', click_type=0)
        else:
            action1.move_to_element_with_offset(move1,1,1).perform()
        time.sleep(15)
        propertyobj.move_slider_measure('#ar_Prompt_2','min', 'right', 3, 'float') #2195070.2
         
        """
        Step10: Verify Canvas 
        """
        time.sleep(10)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(5)
#         if browser == 'Firefox':
#             propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min',2195070.2,'float',msg="Step10: Verify filter prompt range min values")
#         if browser in ['IE', 'Chrome']:
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min',2172012.85,'float',msg="Step10: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','max',3620014.67,'float',msg="Step10: Verify filter prompt range max values")
        time.sleep(6)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step10.a:")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step10.b:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 10:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 10:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 10.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods Local Currency:14,342,627.70', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 10.d: Verify bar value")
        time.sleep(5)
          
        """
        Step 11: Right click "Product,Category" filter in the Filter pane > Select "Hide Prompt"
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.change_prompt_options("1","Hide Prompt")
        time.sleep(8)
          
        """
        Step12: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
#         if browser == 'Firefox':
#             propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min',2195070.2,'float',msg="Step12: Verify filter prompt range min values")
#         if browser in ['IE', 'Chrome']:
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min',2172012.85,'float',msg="Step12: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','max',3620014.67,'float',msg="Step12: Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step12.a:")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step12.b:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 12:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 12.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods Local Currency:14,342,627.70', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 12.d: Verify bar value")
        time.sleep(5)
           
        """
        Step 13: Right click "Cost of Goods, Local Currency" filter in the Filter pane > Select "Edit"
        """
        metaobj.filter_tree_field_click('Cost of Goods,Local Currency',1,1, 'Edit...')
        time.sleep(2)
          
        """
        Step 14: Verify Filter dialog
        Step 15: Uncheck "Show Prompt" > click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(5)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Range'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 14.a: Verify dialog')
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        print(d['float_value'])
#         if browser == 'Firefox':
#             utillobj.asequal(float(d['float_value']),2195070.2,"Step14.b: Verify range from value")
#         if browser in ['IE', 'Chrome']:
        utillobj.asequal(float(d['float_value']),2172012.85,"Step14.b: Verify range from value")
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        print(d['float_value'])
        utillobj.asequal(float(d['float_value']),3620014.67,"Step14.c: Verify range to value")  
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric',['ShowPrompt'])
        time.sleep(5)
          
        """
        Step16: Verify Canvas 
        """
        try:
            if self.driver.find_element_by_css_selector("div[id^='BoxLayoutFilterBox']").is_displayed():
                utillity.UtillityMethods.asequal(self, 'a', 'b', "Step 16: Verify Filter Prompts not removed from canvas")
        except NoSuchElementException:
            utillity.UtillityMethods.asequal(self, 'a', 'a', "Step 16: Verify Filter Prompts are removed from canvas")
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step16.a:")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step16.b:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods Local Currency:14,342,627.70', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16.d: Verify bar value")
        time.sleep(5)
          
        """
        Step17: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
          
        """
        Step 18: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods Local Currency:14,342,627.70', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16.d: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227680_Actual_step18', image_type='actual',x=1, y=1, w=-1, h=-1)
          
        """
        Step 19: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
            
        """
        Step 20: Click Save in the toolbar
        Step 21: Save as "C2158167" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
            
        """
        Step 22: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
            
        """
        Step 23: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_ia_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
           
        """
        Step 24: Verify Canvas and Filter pane
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step24.a:")
        time.sleep(3)
        metaobj.verify_filter_pane_field('Cost of Goods,Local Currency',2,"Step24.b:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 24:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 24:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Camcorder', 'Televisions']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 24:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 24.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 24.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Camcorder', 'Cost of Goods Local Currency:14,342,627.70', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 24.d: Verify bar value")
        time.sleep(5)
        
        """
        Step 25: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()