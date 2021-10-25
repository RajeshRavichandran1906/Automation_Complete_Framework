'''
Created on Mar 30, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227683
Test case Name =  Change Filter Operator from Range to Less than
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.locators import visualization_resultarea_locators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227683_TestClass(BaseTestCase):

    def test_C2227683(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227683'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step 02: Double click "Revenue,Local Currency", located under Sales Measures
        """
        time.sleep(8)
        metaobj.datatree_field_click('Revenue,Local Currency', 2, 1)
         
        """
        Step 03: Drag and drop "Revenue,Local Currency" into the Filter pane
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.drag_drop_data_tree_items_to_filter('Revenue,Local Currency', 1) 
        time.sleep(5)
         
        """
        Step 04: Click "Operator" dropdown box > Select "Less than or equal to"
        Step 05: Verify dialog
        Step 06: Click OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Less than or equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 05.a: Verify dialog') 
        time.sleep(2)
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        print(d['int_value'])
        utillobj.asequal(int(d['int_value']),5114060,"Step05.b: Verify dialog") 
        metaobj.create_visualization_filters('numeric')
         
        """
        Step 07: Double click "Product,Subcategory" from Product Dimension
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.datatree_field_click('Product,Subcategory', 2, 1)
        time.sleep(5)
         
        """
        Step 08: Drag and drop "Revenue,Local Currency" into the Size bucket
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        metaobj.datatree_field_click('Revenue,Local Currency', 1, 1,'Add To Query','Size')
        time.sleep(5)
         
        """
        Step 09: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(6)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
#         propertyobj.verify_slider_range_filter_prompts(1, [5114060], "Step 09: Verify filter prompt range values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',5114060.62,'float',msg="Step09: Verify filter prompt range max values")
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step11:")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 5)
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '0.3B', '0.6B', '0.9B', '1.2B']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Revenue Local Currency:1,123,436,666.62', 'Revenue Local Currency:1,123,436,666.62', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 09: Verify bar value")
        time.sleep(8)
        
        """
        Step 10: Edit Prompt value > Drag slider handle to the right at value 2030.82 (or approximate)
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        browser=utillobj.parseinitfile('browser')
#         propertyobj.move_slider_measure('1',date_r2='LE') #actual value as in testrail is 2030.82
        propertyobj.move_slider_measure('#ar_Prompt_1','min', 'left', 1, 'float')
        
        """
        Step11: Verify Canvas
        """
        time.sleep(5)
        if browser == 'Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',4061859.68,'float',msg="Step11: Verify filter prompt range min values")
        if browser in ['IE', 'Chrome']:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',4091250.77,'float',msg="Step11: Verify filter prompt range min values")
        time.sleep(2)
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step11:")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '0.3B', '0.6B', '0.9B', '1.2B']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Revenue Local Currency:1,123,436,666.62', 'Revenue Local Currency:1,123,436,666.62', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 11: Verify bar value")
        time.sleep(5)
        """
        Step 12: Right click "Revenue,Local Currenty" filter in the Filter pane > Edit
        Step 13: Verify dialog
        Step 14: Click Cancel
        """
        metaobj.filter_tree_field_click('Revenue,Local Currency',1,1,'Edit...')
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        print(d['float_value'])
        if browser =='Firefox':
            utillobj.asequal(float(d['float_value']),4061859.69,"Step13: Verify range from dialog")
        if browser in ['IE', 'Chrome']:
            utillobj.asequal(float(d['float_value']),4091250.77,"Step13: Verify range from dialog")
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric',ok=False)
        time.sleep(2)
           
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
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '0.3B', '0.6B', '0.9B', '1.2B']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Revenue Local Currency:1,123,436,666.62', 'Revenue Local Currency:1,123,436,666.62', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step16_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1) 
           
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
        Step 19: Save as "C2158166" > Click Save
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
        time.sleep(6)
        if browser == 'Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',4061859.68,'float',msg="Step22: Verify filter prompt range min values")
        if browser in ['IE', 'Chrome']:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',4091250.77,'float',msg="Step22: Verify filter prompt range min values")
        time.sleep(2)
        metaobj.verify_filter_pane_field('Revenue,Local Currency',1,"Step22:")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue Local Currency"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 22:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 22:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '0.3B', '0.6B', '0.9B', '1.2B']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 22:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 22.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 22.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Revenue Local Currency:1,123,436,666.62', 'Revenue Local Currency:1,123,436,666.62', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 22: Verify bar value")
        time.sleep(5)
          
        """
        Step 23: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()