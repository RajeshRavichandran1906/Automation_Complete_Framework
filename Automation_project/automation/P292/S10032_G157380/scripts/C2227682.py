'''
Created on Mar 29, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227682
Test case Name =  Change Filter Operator from Range to Greater than 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, visualization_properties
from common.locators import visualization_resultarea_locators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class C2227682_TestClass(BaseTestCase):

    def test_C2227682(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227682'
        
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
        Step 02: Drag and drop "Cost of Goods" into the Filter pane
        """
        time.sleep(6)
        metaobj.datatree_field_click('Cost of Goods', 1, 1, 'Filter')
        time.sleep(5)
         
        """
        Step 03: Click "Operator" dropdown box > Verify list of operators
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(3)
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Greater than or equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 03: Click "Operator" dropdown box > Verify list of operators') 
         
        """
        Step 04: Select "Greater than or equal to"
        Step 05: Change "From" value to 8000
        """
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric',['From',8000])
        time.sleep(2)
         
        """
        Step 06: Verify dialog
        Step 07: Click OK
        """
        metaobj.filter_tree_field_click('Cost of Goods',1,1,'Edit...')
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        time.sleep(5)
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(int(d['int_value']),8000,"Step06: Verify range from value")
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric')
        time.sleep(2)
          
        """
        Step 08: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step08:")
        try:
            if self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 svg g.risers").is_displayed():
                utillity.UtillityMethods.asequal(self, 'a', 'b', "Step 08: Verify preview with risers")
        except NoSuchElementException:
            utillity.UtillityMethods.asequal(self, 'a', 'a', "Step 08: Verify preview with no risers")
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
#         propertyobj.verify_slider_range_filter_prompts(1, [8000], "Step 08: Verify filter prompt range values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',8000,'int',msg="Step08: Verify filter prompt range min values")
        time.sleep(2)
         
        """
        Step 09: Double click "Cost of Goods"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(5)
         
        """
        Step 10: Double click "Product,Subcategory" from Product Dimension
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.datatree_field_click('Product,Subcategory', 2, 1)
        time.sleep(5)
         
        """
        Step 11: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(6)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',8000,'int',msg="Step11: Verify filter prompt range min values")
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step11:")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M','3M','3.5M','4M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Professional', 'Cost of Goods:$3,532,404.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 11: Verify bar value")
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
        propertyobj.verify_slider_range_filter_prompts('#PROMPT_1_cs','min',8000,'int',msg="Step13: Verify filter prompt range min values")
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 13:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 13:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M','3M','3.5M','4M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Professional', 'Cost of Goods:$3,532,404.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 13: Verify bar value")
        time.sleep(5)
         
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
        Step 16: Save as "C2158166" > Click Save
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
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_ia_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
         
        """
        Step 19: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(6)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',8000,'int',msg="Step19: Verify filter prompt range min values")
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step 19:")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 19:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 19:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M','3M','3.5M','4M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 19.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Professional', 'Cost of Goods:$3,532,404.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 19: Verify bar value")
        time.sleep(5)
        
        """
        Step 20: Select Insert > Grid in the Home Tab
        """
        time.sleep(3)
        ribbonobj.select_ribbon_item('Home', 'Insert', opt='Grid')
        
        """
        Step 21: Double click "Cost of Goods"
        """
        time.sleep(6)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(6)
        
        """
        Step 22: Double click "Product,Subcategory"
        """
        metaobj.datatree_field_click('Product,Subcategory', 2, 1)
        time.sleep(5)
        
        """
        Step 23: Verify canvas 
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem)
        time.sleep(8)
        list_val=['Product Subcategory', 'Cost of Goods']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody2',list_val, 'Step 23.1: Verify field titles')
        time.sleep(20)
        row1=['Flat Panel TV', '$958,750.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody2',row1,'Step 23.2: verify grid 1st row value')
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(6)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',8000,'int',msg="Step23: Verify filter prompt range min values")
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step 23:")
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 23:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 23:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M','3M','3.5M','4M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 23:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 23.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 23.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Professional', 'Cost of Goods:$3,532,404.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 23: Verify bar value")
        time.sleep(5)
        
        """
        Step 24: Click Run > Verify output
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody2')
        resultobj._validate_page(elem)
        time.sleep(8)
        list_val=['Product Subcategory', 'Cost of Goods']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody2',list_val, 'Step 24.1: Verify field titles')
        time.sleep(20)
        row1=['Flat Panel TV', '$958,750.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody2',row1,'Step 24.2: verify grid 1st row value')
        time.sleep(3)
        propertyobj.verify_slider_range_filter_prompts('#PROMPT_1_cs','min',8000,'int',msg="Step24: Verify filter prompt range min values")
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 24:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 24:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV', 'Professional']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M','3M','3.5M','4M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 24:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step 24.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 24.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Professional', 'Cost of Goods:$3,532,404.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g1!mbar", bar, "Step 24: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227682_Actual_step24', image_type='actual',x=1, y=1, w=-1, h=-1) 
        
        """
        Step 25: Close the output window
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
        Step 26: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()