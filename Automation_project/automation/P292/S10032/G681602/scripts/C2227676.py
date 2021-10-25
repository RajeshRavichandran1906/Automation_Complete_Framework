'''
Created on Apr 18, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227676
Test case Name =  Filter Aggregation - edit values
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.wftools.visualization import Visualization

class C2227676_TestClass(BaseTestCase):

    def test_C2227676(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227676'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        visualization = Visualization(self.driver)
        
        """
        TESTCASE CSS
        """
        query_tree_css = "#queryTreeWindow"
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_1', 'mrid', 'mrpass')
        visualization.wait_for_visible_text("#pfjTableChart_1", "Drop")
     
        """
        Step 02: Double-click "Cost of Goods", located under Sales Measures.
        """
        visualization.double_click_on_datetree_item("Cost of Goods", 1)
        visualization.wait_for_visible_text(query_tree_css, "Cost of Goods")
             
        """
        Step 03: Double-click "Product,Category", located under Product Dimension
        """
        visualization.double_click_on_datetree_item("Product,Category", 1)
        visualization.wait_for_visible_text(query_tree_css, "Product,Category")
             
        """
        Step04: Drag and drop "Cost of Goods" to the Filter pane
        """
        visualization.drag_and_drop_from_data_tree_to_filter("Cost of Goods", 1)
        visualization.wait_for_visible_text("#avFilterCancelBtn", "Cancel")
         
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
        time.sleep(6)
        metaobj.verify_filter_pane_field('AVE (Cost of Goods)',1,"Step 07.00")
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        start_point="#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']"
        resultobj.wait_for_property(start_point, 2)
        time.sleep(3)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',247.26,'float',msg="Step 07.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',825.17,'float',msg="Step 07.02: Verify filter prompt range max values")
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 07.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 07.04: Verify Y-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 07.05:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 7, 'Step 07.06: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 07.07: Verify first bar color")
        time.sleep(5)
         
        """
        Step08: Drag left slider handle in the Filter Prompt to the right > "345.86".
        """
        a=self.driver.find_element_by_css_selector("span[class*='ui-slider-handle'][style='left: 0%;']")
        b=self.driver.find_element_by_css_selector("div[class*='ui-slider-range']")
        utillobj.drag_to_using_pyautogui(a, b,source_offset_x=50,source_offset_y=3,target_offset_x=4,target_offset_y=4)
        time.sleep(3)
         
        """
        Step09: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(8)
        start_point="#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']"
        resultobj.wait_for_property(start_point, 2)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',362.84,'float',msg="Step 09.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',825.17,'float',msg="Step 09.02: Verify filter prompt range max values")
        time.sleep(8)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 8)
        time.sleep(5)
        metaobj.verify_filter_pane_field('AVE (Cost of Goods)',1,"Step 09.03")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 09.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 09.05: Verify Y-Axis Title")
        expected_xval_list=['Televisions']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 09.06:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 09.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 09.08: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Televisions', 'Cost of Goods:$61,551,109.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 09.09: Verify bar value")
        time.sleep(5)
          
        """
        Step 10: Right-click "AVE(Cost of Goods)" in the Filter pane > select Edit...
        """
        metaobj.filter_tree_field_click('AVE (Cost of Goods)',1,1, 'Edit...')
        time.sleep(2)
          
        """
        Step 11: Verify dialog
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
          
        elem=self.driver.find_element_by_css_selector("#avAggregationComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'Average',"Step 11.01: Verify Aggregation in Filter dialog")
               
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(d['float_value'],"532.9","Step 11.02: Verify From in Filter dialog")
             
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "float_value")
        utillobj.asequal(d['float_value'],"825.17","Step 11.03: Verify To in Filter dialog")
          
        """
        Step 12: Change "To" value from 825.17 to 750
        Step 13: Click OK
        """
        time.sleep(2)   
        metaobj.create_visualization_filters('numeric',['From','345.86'])
        time.sleep(2)
        metaobj.filter_tree_field_click('AVE (Cost of Goods)',1,1, 'Edit...')
        time.sleep(2)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
        metaobj.create_visualization_filters('numeric',['To','750'])
        time.sleep(5)
          
        """
        Step14: Verify Canvas 
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        start_point="#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']"
        resultobj.wait_for_property(start_point, 2)
        time.sleep(5)
         
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',345.86,'float',msg="Step 14.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',750,'int',msg="Step 14.02: Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('AVE (Cost of Goods)',1,"Step 14.03:")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 14.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 14.05: Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 14.06:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 14.07: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 14.08: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 14.09: Verify bar value")
        time.sleep(5)
          
        """
        Step15: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        visualization.switch_to_new_window() 
           
        """
        Step 16: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 16.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 16.02: Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 16.03:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 16.04: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 16.05: Verify first bar color")
        time.sleep(5)        
        propertyobj.verify_slider_range_filter_prompts('#LOBJ1_cs','min',345.86,'float',msg="Step 16.06: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#LOBJ1_cs','max',750,'int',msg="Step 16.07: Verify filter prompt range max values")
          
        """
        Step17: Drag right slider handle all the way to the right
        """
        time.sleep(5)
        utillobj.drag_slider_using_pageup_or_pagedown('#LOBJ1_cs', span_index=1)
         
        #The below script is required as verify_slider_range_filter_prompts function has as_LE 
        value=self.driver.find_element_by_css_selector('#LOBJ1_cs span[id$="s_max"]').text.strip()
        if float(value) >= 750:
            status = True
        else: 
            status = False
        utillobj.asequal(True, status, 'Step 17.01 : Checking whether slider handle moved') 
        time.sleep(5)
         
        """
        Step18: Verify output 
        """
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#LOBJ1_cs','min',345.86,'float',msg="Step 18.01: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#LOBJ1_cs','max',825.18,'float',msg="Step 18.02: Verify filter prompt range max values")
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 18.03: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 18.04: Verify Y-Axis Title")
        """
        Step 19: Close output window
        """
        visualization.switch_to_previous_window()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
             
        """
        Step 20: Click Save in the toolbar
        Step 21: Save as "C2158191" > Click Save
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        visualization.wait_for_visible_text('#IbfsOpenFileDialog7_btnCancel', "Cancel")
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", visualization.home_page_short_timesleep)
             
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
        resultobj.wait_for_property(parent_css, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(3)
        metaobj.verify_filter_pane_field('AVE (Cost of Goods)',1,"Step 24.01")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step 24.02: Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", yaxis_value, "Step 24.03: Verify Y-Axis Title")
        expected_xval_list=['Media Player']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step 24.04:Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 1, 'Step 24.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step 24.06: Verify first bar color")
        time.sleep(5)
        bar=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step 24.07: Verify bar value")
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        start_point="#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']"
        resultobj.wait_for_property(start_point, 2)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',345.86,'float',msg="Step 24.08: Verify filter prompt range min values")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',750,'int',msg="Step 24.09: Verify filter prompt range max values")
        time.sleep(5)
        
        """
        Step 25: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()