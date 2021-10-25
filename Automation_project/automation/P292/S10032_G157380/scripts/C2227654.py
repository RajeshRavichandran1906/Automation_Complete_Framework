'''
Created on Apr 21, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227654
Test case Name =  Range with Attributes field Sale,Year Month
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon
from common.locators import visualization_resultarea_locators
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class C2227654_TestClass(BaseTestCase):

    def test_C2227654(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227654'
        
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
        Step 02: Double-click "Cost of Goods"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(4)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
                 
        """
        Step03: Expand Product Dimension > Double click "Product,Category"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
         
        """
        Step04: Expand Dimension "Sales_Related" > "Trasaction Date,Simple" > "Sale,Day" > "Attributes" > Drag and drop "Sale, Year Month" into the Rows bucket in the Query pane
        """
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Year Month", 1, 1,"Add To Query", 'Rows')
                 
        """
        Step05: Drag and drop "Sale,Year Month" into the Filter pane
        """
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 432)
        metaobj.datatree_field_click("Sale,Year Month", 1, 1,"Filter")        
        time.sleep(6)
         
        """
        Step06: Verify Filter dialog
        Step07: Click OK
        """      
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        resultobj._validate_page(elem)
         
        elem=self.driver.find_element_by_css_selector("#avOperatorComboBox div")
        d=utillobj.get_attribute_value(elem,'text')
        utillobj.asequal(d['text'],'Range',"Step06.a: Verify Operator dialog")
                  
        elem1=driver.find_element_by_css_selector("#avfFromValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"201101","Step06.b: Verify From in Filter dialog")
                 
        elem1=driver.find_element_by_css_selector("#avfToValue input")
        d=utillobj.get_attribute_value(elem1, "int_value")
        utillobj.asequal(d['int_value'],"201703","Step06.c: Verify To in Filter dialog")
         
        time.sleep(2)
        metaobj.create_visualization_filters('numeric')
        time.sleep(3)
         
        """
        Step08: Verify Canvas
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201101,'int',msg="Step08: Verify filter prompt range values- min")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step08: Verify filter prompt range values- max")
        time.sleep(2)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 432)
        time.sleep(2)
        metaobj.verify_filter_pane_field('Sale,Year Month',1,"Step08: Verify 'Sale,Day' appears in filter pane")
        time.sleep(2)  
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step08:d(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 504, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step08.c: Verify first bar color")
        time.sleep(5)
        expected=['201101','201102','201103','201104','201105','201106','201107']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year Month', expected,"Step08: Verify Row header")
        bar=['Sale Year Month:201101', 'Product Category:Media Player', 'Cost of Goods:$820,371.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", bar, "Step08: Verify bar value")
        time.sleep(5) 
         
        """
        Step09: Drag the left slider handle in the Filter Prompt to the right > change value to 201505
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        action1 = ActionChains(self.driver)
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        browser=utillobj.parseinitfile('browser')
        if browser == 'Firefox':
            utillobj.click_on_screen(move1, coordinate_type='bottom_middle', click_type=0)
            time.sleep(8)
            utillobj.click_type_using_pyautogui(move1)
            start_point=driver.find_elements_by_css_selector("#ar_Prompt_1 div[id^='slider_'] [class^='ui-slider-handle']")
            utillobj.click_on_screen(start_point[0], coordinate_type='middle', click_type=0)
        else:
            action1.move_to_element_with_offset(move1,1,1).perform()
        time.sleep(8)
        propertyobj.move_slider_measure('#ar_Prompt_1','min', 'right', 1, 'str') 
        time.sleep(5)
          
        """
        Step10: Verify Canvas
        """
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201221,'int',msg="Step10: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step10: Verify filter prompt range values- max")
        else:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201221,'int',msg="Step10: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step10: Verify filter prompt range values- max")         
        time.sleep(2)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        time.sleep(2)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 288)
        time.sleep(2)
        metaobj.verify_filter_pane_field('Sale,Year Month',1,"Step10: Verify 'Sale,Day' appears in filter pane")
        time.sleep(5)  
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step10:d(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 336, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step10.c: Verify first bar color")
        time.sleep(5)
        expected=['201301','201301','201303','201304','201305','201306','201307']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year Month', expected,"Step10: Verify Row header")
        bar=['Sale Year Month:201301', 'Product Category:Media Player', 'Cost of Goods:$1,389,176.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", bar, "Step10: Verify bar value") 
        time.sleep(5)
         
        """
        Step11: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(15)    
                 
        """
        Step12: Verify output
        """
        chart_type_css="rect[class*='riser!s0!g3!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 288)
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',201221,'int',msg="Step12: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',201703,'int',msg="Step12: Verify filter prompt range values- max")
        else:
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','min',201221,'int',msg="Step12: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#sliderPROMPT_1','max',201703,'int',msg="Step12: Verify filter prompt range values- max")         
        time.sleep(2)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step12:d(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 336, 'Step12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step12.c: Verify first bar color")
        time.sleep(5)
        expected=['201301','201301','201303','201304','201305','201306','201307']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year Month', expected,"Step12: Verify Row header")
        time.sleep(2)
        bar=['Sale Year Month:201301', 'Product Category:Media Player', 'Cost of Goods:$1,389,176.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", bar, "Step12: Verify bar value")
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step12_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
                           
        """
        Step13: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1) 
      
        """
        Step14: Click Save
        Step15: Click Save as "C2158180" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
                  
        """
        Step16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158180.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_1',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
                 
        """
        Step18: Verify Canvas
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!s0!g3!mbar!r0!c0']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(2)        
        browser=utillobj.parseinitfile('browser')
        if browser=='Firefox':
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201221,'int',msg="Step18: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step18: Verify filter prompt range values- max")
        else:
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','min',201221,'int',msg="Step18: Verify filter prompt range values- min")
            propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_1','max',201703,'int',msg="Step18: Verify filter prompt range values- max")         
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 288)
        time.sleep(3)
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1_f", xaxis_value, "Step18:d(i) Verify X-Axis Title")
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '2M', '4M', '6M', '8M', '10M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step18:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 336, 'Step18.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", "bar_blue", "Step18.c: Verify first bar color")
        time.sleep(5)
        expected=['201301','201301','201303','201304','201305','201306','201307']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Rows','Sale Year Month', expected,"Step18: Verify Row header")
        time.sleep(2)
        bar=['Sale Year Month:201301', 'Product Category:Media Player', 'Cost of Goods:$1,389,176.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g3!mbar!r0!c0", bar, "Step18: Verify bar value")
        time.sleep(5)
         
        """
        Step19: Logout
        """
        
if __name__ == '__main__':
    unittest.main()