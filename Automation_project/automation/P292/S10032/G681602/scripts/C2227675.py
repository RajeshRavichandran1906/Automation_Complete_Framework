'''
Created on Apr 6, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227675
Test case Name =  Filter Aggregation - remove aggregation
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By


class C2227675_TestClass(BaseTestCase):

    def test_C2227675(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227675'
        
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
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        time.sleep(6)
        metaobj.datatree_field_click("Cost of Goods",2,1)
            
        """
        Step 03: Double-click "Product,Subcategory", located under Product Dimension
        """
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
            
        """
        Step04: Drag and drop "Cost of Goods" to the Filter pane
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.drag_drop_data_tree_items_to_filter("Cost of Goods", 1)  
        
        """
        Step05: Click "Aggregation" dropdown menu > Select "Average"
        Step06: Click OK
        """ 
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        metaobj.create_visualization_filters('numeric',['Aggregation','Average'])
        
        """
        Step 07: Verify Canvas
        """
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        metaobj.verify_filter_pane_field('AVE (Cost of Goods)',1,"Step07:")
        parent_css= "#ar_Prompt_1 span[id$='s_min']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#ar_Prompt_1 span[id$='s_max']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',27.48,'float',msg="Step07: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',3897.56,'float',msg="Step07: Verify filter prompt range max values")
        time.sleep(3)
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Con...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 07: Verify bar value")
        time.sleep(5)
        
        """
        Step 08: Right-click "AVE(Cost of Goods)" in the Filter pane > select Edit...
        """
        metaobj.filter_tree_field_click('AVE (Cost of Goods)',1,1, 'Edit...')
        time.sleep(2)
        
        """
        Step09: Verify dialog
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'Average',"Step09.a: Verify Aggregation in Filter dialog")
             
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(d['float_value'],"27.48","Step09.b: Verify From in Filter dialog")
             
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(d['float_value'],"3897.56","Step09.c: Verify To in Filter dialog")
             
        """
        Step10: Click the "Aggregation" dropdown menu > select "None"
        Step11: Verify dialog
        Step12: Click OK
        """   
             
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox")
        combo=['(None)', 'Sum', 'Average', 'Count', 'Distinct Count', 'Maximum', 'Minimum', 'Percent', 'Median']
        utillobj.select_any_combobox_item(elem,'(None)',verify=True,expected_combobox_list=combo, msg="Step10: Verify list of aggregation functions")
        time.sleep(8)    
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'(None)',"Step11.a: Verify Aggregation in Filter dialog")
             
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"16","Step11.b: Verify From in Filter dialog")
             
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"13000","Step11.c: Verify To in Filter dialog")
             
        metaobj.create_visualization_filters('numeric')
        time.sleep(3)  
              
        """
        Step 13: Verify Filter pane is updated
        """
        time.sleep(5)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step13:")
         
        """
        Step 14: Verify Canvas
        """
        time.sleep(5)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#ar_Prompt_1 span[id$='s_min']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#ar_Prompt_1 span[id$='s_max']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',16,'int',msg="Step14: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',13000,'int',msg="Step14: Verify filter prompt range max values")
        time.sleep(3)
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 14:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 14:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Con...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 14.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 14: Verify bar value")
        time.sleep(5)
                      
        """
        Step 15: Click Run
        """
        time.sleep(8) 
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15)
  
              
        """
        Step16: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        propertyobj.verify_slider_range_filter_prompts('#PROMPT_1_cs','min',16,'int',msg="Step16: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#PROMPT_1_cs','max',13000,'int',msg="Step16: Verify filter prompt range max values")
        time.sleep(3) 
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Con...', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 16: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner']")
        utillobj.take_screenshot(ele,'C2227675_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1) 
                
        """
        Step17: Close output window
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
        Step19: Save as "C2158190" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
               
        """
        Step20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
           
        """
        Step21: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158198.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
              
        """
        Step22: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(3)
        metaobj.verify_filter_pane_field('Cost of Goods',1,"Step22:")
        parent_css= "#ar_Prompt_1 span[id$='s_min']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#ar_Prompt_1 span[id$='s_max']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',16,'int',msg="Step22: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',13000,'int',msg="Step22: Verify filter prompt range max values")
        time.sleep(5)  
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 22:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 22:a(ii) Verify Y-Axis Title")
        expected_xval_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 22:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 21, 'Step 22.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 22.c: Verify first bar color")
        time.sleep(5)
        bar=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 22: Verify bar value")
        time.sleep(5) 
        
        """
        Step23: Logout
        """     

        
if __name__ == '__main__':
    unittest.main()