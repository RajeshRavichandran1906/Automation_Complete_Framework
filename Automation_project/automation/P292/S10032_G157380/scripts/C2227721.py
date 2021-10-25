'''
Created on Jun 22, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227721
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run,\
    ia_run,wf_mainpage
from common.locators import visualization_resultarea_locators
from common.lib import utillity
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pyautogui import click


class C2227721_TestClass(BaseTestCase):

    def test_C2227721(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227721'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        port_no = utillobj.parseinitfile('httpport')

        utillobj.infoassist_api_edit('C2227720','idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
         
        time.sleep(5)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css="#resultArea div[id^='BoxLayoutFilterWindow']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=False,msg="Step01: Verify All unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Store Front',verify=True, verify_type=True,msg="Step01: Verify Store Front checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Web',verify=True, verify_type=True,msg="Step01: Verify Web checked in prompt")
         
        propertyobj.select_or_verify_show_prompt_item('2', 'Camcorder',scroll_down=True,verify=True, verify_type=True,msg="Step01: Verify Camcorder checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('2', 'Computers',scroll_down=True,verify=True, verify_type=True,msg="Step01: Verify Computers checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('2', 'Video Production',scroll_down=True,verify=True, verify_type=True,msg="Step01: Verify Video Production checked in prompt")
          
        time.sleep(3)
        expected_xval_list=['Camcorder','Computers','Video Production']
        time.sleep(2)
        expected_yval_list=['0','5M','10M','15M','20M','25M','30M','35M','40M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step01:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1,6, 'Step01.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step01.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step01: Verify Column header")
             
        bar=['Store Type:Store Front', 'Product Category:Camcorder', 'Gross Profit:$34,471,375.27', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step01: Verify bar value")
        time.sleep(5)
             
        """
        Step02: Select Insert > Chart (2x).
        Step03: Verify 3 components are displayed on the canvas.
        """
        time.sleep(3)
        ribbonobj.select_ribbon_item('Home', 'Insert',opt='Chart')
        time.sleep(3)
        ribbonobj.select_ribbon_item('Home', 'Insert',opt='Chart')
        time.sleep(10)
        resultobj.verify_panel_caption_label(0, 'Bar Stacked3', "Step03: Verify Bar Stacked3 is displayed")
        resultobj.verify_panel_caption_label(1, 'Bar Stacked2', "Step03: Verify Bar Stacked2 is displayed")
        resultobj.verify_panel_caption_label(2, 'Bar Stacked1', "Step03: Verify Bar Stacked1 is displayed")
         
        """
        Step04: Click "Bar Stacked2" on the canvas.
        Step05: Verify that "Bar Stacked2" on Query pane expanded.
        """
        metaobj.verify_query_pane_field('Bar Stacked2','Bar Stacked3', 1, "Step04: Verify Bar Stacked2")
        time.sleep(4)
        self.driver.find_element_by_css_selector("#TableChart_2").click()
        time.sleep(2)
        metaobj.verify_query_pane_field('Bar Stacked2','Matrix', 1, "Step05: Verify Bar Stacked2 expanded")
         
        """
        Step06: Double click "Gross Profit", "Product,Category".
        """        
        metaobj.datatree_field_click("Gross Profit", 2, 1)       
        parent_css="#TableChart_2 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
          
        """
        Step07: Verify the following chart is displayed.
        Step08: Verify hover (tooltip) works and display appropriate information.
        """  
        time.sleep(5)
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
                   
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step07:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Gross Profit", "Step07:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Camcorder', 'Computers','Video Production']
        time.sleep(2)
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 3, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step07.c: Verify first bar color")
        time.sleep(5)
              
        bar=['Product Category:Camcorder', 'Gross Profit:$49,598,845.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g0!mbar", bar, "Step08: Verify bar value")
          
        """
        Step09: Click "Bar Stacked3" on the canvas.
        Step10: Verify that "Bar Stacked3" on Query pane expanded.
        Step11: Click Change (dropdown) > Pie.
        Step12: Verify Query pane refreshed with "Pie1".
        """
        time.sleep(4)
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#TableChart_3"
        resultobj.wait_for_property(parent_css, 1)
        self.driver.find_element_by_css_selector("#TableChart_3").click()
        time.sleep(2)
        metaobj.verify_query_pane_field('Bar Stacked3','Matrix', 1, "Step09: Verify Bar Stacked3 expanded")
         
        time.sleep(2)
        ribbonobj.change_chart_type('pie')
        time.sleep(4)
         
        metaobj.verify_query_pane_field('Bar Stacked2','Pie1', 1, "Step12: Verify pie expanded")
        time.sleep(2)
         
        """
        Step13: Double click "Gross Profit", "Product,Category".
        """        
        metaobj.datatree_field_click("Gross Profit", 2, 1)       
        parent_css="#TableChart_3 text[class='pieLabel!g0!mpieLabel!']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(15)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(6)
#         utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        parent_css= "#TableChart_3 .legend text"
        resultobj.wait_for_property(parent_css, 4)
           
        elem=self.driver.find_element_by_css_selector("#TableChart_3 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step13.b: Verify X-axis label")
           
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',2,"Step13.c: Verify filter pane")
        resultobj.verify_number_of_pie_segments("TableChart_3", 1, 3, 'Step13.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("TableChart_3", "riser!s0!g0!mwedge", "bar_blue", "Step13.d(i) Verify first bar color")
        legend=['Product Ca', 'Camcorder', 'Computers', 'Video Production']
        resultobj.verify_riser_legends("TableChart_3", legend, "Step13:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Product Category:Camcorder', 'Gross Profit:$49,598,845.24  (49.08%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("TableChart_3","riser!s0!g0!mwedge",expected_tooltip, "Step13e: verify the default tooltip values")       
        
        """
        Step15: Click Run
        Step16: Verify output at Runtime matches outputs on canvas.
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10)
        
        time.sleep(6)
        parent_css= "#MAINTABLE_wbody3 .legend text"
        resultobj.wait_for_property(parent_css, 4)
           
        elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody3 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step16.b: Verify X-axis label")
           
        time.sleep(5)
        resultobj.verify_number_of_pie_segments("MAINTABLE_wbody3", 1, 3, 'Step16.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody3", "riser!s0!g0!mwedge", "bar_blue", "Step16.d(i) Verify first bar color")
        legend=['Product Category', 'Camcorder', 'Computers', 'Video Production']
        resultobj.verify_riser_legends("MAINTABLE_wbody3", legend, "Step16:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Product Category:Camcorder', 'Gross Profit:$49,598,845.24  (49.08%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody3","riser!s0!g0!mwedge",expected_tooltip, "Step13e: verify the default tooltip values")       
        
        time.sleep(5)
        parent_css="#MAINTABLE_wbody2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
                   
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step16:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", "Gross Profit", "Step16:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Camcorder', 'Computers','Video Production']
        time.sleep(2)
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2", expected_xval_list, expected_yval_list, "Step16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 3, 'Step16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step16.c: Verify first bar color")
        time.sleep(5)
              
        bar=['Product Category:Camcorder', 'Gross Profit:$49,598,845.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2", "riser!s0!g0!mbar", bar, "Step16: Verify bar value")
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css="#resultArea div[id^='BoxLayoutFilterWindow']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        
        expected_xval_list=['Camcorder','Computers','Video Production']
        time.sleep(2)
        expected_yval_list=['0','5M','10M','15M','20M','25M','30M','35M','40M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step16:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1,6, 'Step16.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step16.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody1", 'Columns','Store Type', expected,"Step16: Verify Column header")
             
        bar=['Store Type:Store Front', 'Product Category:Camcorder', 'Gross Profit:$34,471,375.27', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar!r0!c0", bar, "Step16: Verify bar value")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227721_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
                     
        """
        Step17: Close
        Step18: Click Save in the toolbar
        Save as "C2158150" > Click Save
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                     
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                
        """
        Step19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
           
        """
        Step20: Reopen fex using IA API:
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
           
        """
        Step21: Verify the following is displayed.
        """
        time.sleep(4)
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_css="#TableChart_3"
        resultobj.wait_for_property(parent_css, 1)
        
        time.sleep(6)
        parent_css= "#TableChart_3 .legend text"
        resultobj.wait_for_property(parent_css, 4)
           
        elem=self.driver.find_element_by_css_selector("#TableChart_3 text[class^='pieLabel!g0!mpieLabel!']")
        d=utillobj.get_attribute_value(elem,'dom_visible_text')
        utillobj.asequal(d['dom_visible_text'],'Gross Profit',"Step21.b: Verify X-axis label")
           
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',2,"Step21.c: Verify filter pane")
        resultobj.verify_number_of_pie_segments("TableChart_3", 1, 3, 'Step21.c(i): Verify the total number of pie segments displayed on pie Chart')
        utillobj.verify_chart_color("TableChart_3", "riser!s0!g0!mwedge", "bar_blue", "Step21.d(i) Verify first bar color")
        legend=['Product Ca', 'Camcorder', 'Computers', 'Video Production']
        resultobj.verify_riser_legends("TableChart_3", legend, "Step21:e(ii) Verify Legends Title")
        time.sleep(2)
        expected_tooltip=['Product Category:Camcorder', 'Gross Profit:$49,598,845.24  (49.08%)', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("TableChart_3","riser!s0!g0!mwedge",expected_tooltip, "Step21e: verify the default tooltip values")       
        
        time.sleep(5)
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
                   
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step21:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Gross Profit", "Step21:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Camcorder', 'Computers','Video Production']
        time.sleep(2)
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 3, 'Step21: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step21.c: Verify first bar color")
        time.sleep(5)
              
        bar=['Product Category:Camcorder', 'Gross Profit:$49,598,845.24', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g0!mbar", bar, "Step21: Verify bar value")
        
        time.sleep(3)
        expected_xval_list=['Camcorder','Computers','Video Production']
        time.sleep(2)
        expected_yval_list=['0','5M','10M','15M','20M','25M','30M','35M','40M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody3", expected_xval_list, expected_yval_list, "Step21:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody3", 1,6, 'Step21.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody3", "riser!s0!g0!mbar!r0!c0", "bar_blue", "Step21.c: Verify first bar color")
        time.sleep(5)
        expected=['Store Front','Web']
        resultobj.verify_visualization_row_column_header_labels("MAINTABLE_wbody3", 'Columns','Store Type', expected,"Step21: Verify Column header")
             
        bar=['Store Type:Store Front', 'Product Category:Camcorder', 'Gross Profit:$34,471,375.27', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody3", "riser!s0!g0!mbar!r0!c0", bar, "Step21: Verify bar value")
        time.sleep(5)
         

if __name__ == '__main__':
    unittest.main()



    
     
        