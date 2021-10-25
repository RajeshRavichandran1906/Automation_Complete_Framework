'''
Created on Apr 19, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227678
Test case Name =  Filter Aggregation with List of Values - Equal To
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By
from datetime import datetime


class C2227678_TestClass(BaseTestCase):

    def test_C2227678(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227678'
        
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
        Step 02: Double-click "Gross Profit", located under Sales Measures
        """
        time.sleep(6)
        metaobj.datatree_field_click("Gross Profit",2,1)
            
        """
        Step 03: Double-click "Product,Subcategory", located under Product Dimension
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
            
        """
        Step04: Drag and drop "Gross Profit" to the Filter pane
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        metaobj.drag_drop_data_tree_items_to_filter("Gross Profit", 1)
        
        """
        Step05: Click "Aggregation" dropdown menu > Select "Average"
        Step06: Click "Operator" dropdown menu > Select "Equal to"
        Step07: Verify Filter dialog
        Step08: Click OK
        """ 
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox")
        combo=['(None)', 'Sum', 'Average', 'Count', 'Distinct Count', 'Maximum', 'Minimum', 'Percent', 'Median']
        utillobj.select_any_combobox_item(elem,'Average',verify=True,expected_combobox_list=combo, msg="Step05: Verify list of aggregation functions")
        time.sleep(8)   
        operator_combo_elem=driver.find_element_by_css_selector("#numericAndDateFieldPanel #avOperatorComboBox div[id^='BiButton']")
        elem = 'Equal to'
        utillobj.select_any_combobox_item(operator_combo_elem, elem, verify =True, expected_combobox_list =['Equal to', 'Not equal to', 'Greater than or equal to', 'Less than or equal to', 'Range'], msg='Step 06.a: Verify dialog')
        time.sleep(3)
        item_list=['[All]']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', msg = 'step07.a: Verify dialog') 
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'Average',"Step07.b: Verify Aggregation in Filter dialog")
        metaobj.create_visualization_filters('numeric')
        time.sleep(3)  
        
        """
        Step 09: Verify Canvas
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('AVE (Gross Profit)',1,"Step09:")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 09.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Gross Profit:$51,771,195.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 09: Verify bar value")
        time.sleep(5)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '[All]', verify=True, verify_type=True, msg="Step09.e: Verify [All] is checked in filter prompt")
        print(str(datetime.now()))
        
        """
        Step10: Scroll down in the Filter Prompt > Select values $149.41 through $977.81.
        """
        time.sleep(6)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$149.41', scroll_down = True)
        time.sleep(2)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$151.44', scroll_down = True)
        time.sleep(2)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$155.04', scroll_down = True)
        time.sleep(8)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$170.00', scroll_down = True)
        time.sleep(5)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$184.34', scroll_down = True)
        time.sleep(2)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$242.05', scroll_down = True)
        time.sleep(2)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$977.81', scroll_down = True)
        time.sleep(2)
        print(str(datetime.now()))
        
        
        """
        Step 11: Verify Canvas
        """
        time.sleep(15)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        time.sleep(5)
        metaobj.verify_filter_pane_field('AVE (Gross Profit)',1,"Step11:")
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 11:a(ii) Verify Y-Axis Title")
        time.sleep(5)
        expected_xval_list=['CRT TV', 'Flat Panel TV', 'Headphones', 'Professional', 'Receivers', 'Speaker Kits', 'Tablet']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M', '24M', '28M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 11.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Headphones', 'Gross Profit:$24,523,023.97', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 11.d: Verify bar value")
        time.sleep(5)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$149.41', verify=True, verify_type=True, scroll_down = True, msg="Step11.1: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$151.44', verify=True, verify_type=True, scroll_down = True, msg="Step11.2: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$155.04', verify=True, verify_type=True, scroll_down = True, msg="Step11.3: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$170.00', verify=True, verify_type=True, scroll_down = True, msg="Step11.4: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$184.34', verify=True, verify_type=True, scroll_down = True, msg="Step11.5: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$242.05', verify=True, verify_type=True, scroll_down = True, msg="Step11.6: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$977.81', verify=True, verify_type=True, scroll_down = True, msg="Step11.7: Verify values is checked in filter prompt")
        print(str(datetime.now()))
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
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 13:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 13:a(ii) Verify Y-Axis Title")
        expected_xval_list=['CRT TV', 'Flat Panel TV', 'Headphones', 'Professional', 'Receivers', 'Speaker Kits', 'Tablet']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M', '24M', '28M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 13.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Headphones', 'Gross Profit:$24,523,023.97', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 13.d: Verify bar value")
        time.sleep(5)
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$149.41', verify=True, verify_type=True, scroll_down = True, msg="Step13.1: Verify values is checked in filter prompt")
        print(str(datetime.now()))
        propertyobj.select_or_verify_show_prompt_item(1, '$151.44', verify=True, verify_type=True, scroll_down = True, msg="Step13.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$155.04', verify=True, verify_type=True, scroll_down = True, msg="Step13.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$170.00', verify=True, verify_type=True, scroll_down = True, msg="Step13.4: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$184.34', verify=True, verify_type=True, scroll_down = True, msg="Step13.5: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$242.05', verify=True, verify_type=True, scroll_down = True, msg="Step13.6: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$977.81', verify=True, verify_type=True, scroll_down = True, msg="Step13.7: Verify values is checked in filter prompt")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227678_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1) 
        
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
        Step 16: Save as "C2158192" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
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
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        metaobj.verify_filter_pane_field('AVE (Gross Profit)',1,"Step19:")
        time.sleep(6)
        xaxis_value="Product Subcategory"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 19:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 19:a(ii) Verify Y-Axis Title")
        expected_xval_list=['CRT TV', 'Flat Panel TV', 'Headphones', 'Professional', 'Receivers', 'Speaker Kits', 'Tablet']
        expected_yval_list=['0', '4M', '8M', '12M', '16M', '20M', '24M', '28M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 19:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 19.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 19.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Headphones', 'Gross Profit:$24,523,023.97', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g2!mbar", bar, "Step 19.d: Verify bar value")
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item(1, '$149.41', verify=True, verify_type=True, scroll_down = True, msg="Step19.1: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$151.44', verify=True, verify_type=True, scroll_down = True, msg="Step19.2: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$155.04', verify=True, verify_type=True, scroll_down = True, msg="Step19.3: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$170.00', verify=True, verify_type=True, scroll_down = True, msg="Step19.4: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$184.34', verify=True, verify_type=True, scroll_down = True, msg="Step19.5: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$242.05', verify=True, verify_type=True, scroll_down = True, msg="Step19.6: Verify values is checked in filter prompt")
        propertyobj.select_or_verify_show_prompt_item(1, '$977.81', verify=True, verify_type=True, scroll_down = True, msg="Step19.7: Verify values is checked in filter prompt")
        time.sleep(5)
        
        """
        Step 20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()