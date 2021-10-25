'''
Created on Jun 19, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227714
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


class C2227714_TestClass(BaseTestCase):

    def test_C2227714(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227714'
        
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
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
            
        """
        Step02: Select Change > Grid in the Home Tab ribbon
        Step03: Verify Preview
        """
        time.sleep(3)
        ribbonobj.change_chart_type('grid')
        time.sleep(10)
        resultobj.verify_panel_caption_label(0, 'Grid1', "Step02: Verify Grid1 is displayed")
         
        """
        Step04: Add fields "Store,Country", "Product,Category", and "Revenue"
        """    
        time.sleep(4)
        metaobj.datatree_field_click("Store,Country", 2, 1)       
        parent_css1="#TableChart_1 .rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        parent_css1="#TableChart_1 .rowTitle text"
        resultobj.wait_for_property(parent_css1,2)
        metaobj.datatree_field_click("Revenue",2,1)
       
        parent_css1="#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
         
        """
        Step05: Drag and drop "Store,Country" into the Filter pane
        """
        time.sleep(4)
        metaobj.datatree_field_click("Store,Country", 1, 1,'Filter') 
         
        """
        Step06: De-select [All] to de-select all values
        Step07: Check off values: Brazil, Canada, China, United States > click OK        
        """
        time.sleep(3)
        browser = utillobj.parseinitfile("browser")
        if browser == 'Chrome':
            l=['[All]','Brazil','Canada']
            self.select_or_verify_visualization_filter_values(l)
            time.sleep(4)
            l=['United States']
            self.select_or_verify_visualization_filter_values(l,scroll_down=True)
            time.sleep(2)
            metaobj.create_visualization_filters('alpha')
        else:
            l=['[All]','Brazil','Canada','United States']
            metaobj.create_visualization_filters('alpha',['GridItems',l])
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', 'China')
        
        """
        Step08: Verify Preview
        """
        time.sleep(5)
        metaobj.verify_query_pane_field('Grid1',"Rows",1,"Step08: Verify Grid1")
        metaobj.verify_query_pane_field('Store,Country',"Product,Category",1,"Step08: Verify Rows")
        metaobj.verify_query_pane_field('Measure',"Revenue",1,"Step08: Verify Revenue in measure")
           
        time.sleep(4)
        parent_css1="#TableChart_1 .rowTitle text"
        resultobj.wait_for_property(parent_css1,2)
        parent_css1="#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('1', '[All]',verify=True, verify_type=False,msg="Step08: Verify All unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Brazil',verify=True, verify_type=True,msg="Step08: Verify Brazil checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'Canada',verify=True, verify_type=True,msg="Step08: Verify Canada checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('1', 'China',verify=True, verify_type=True,msg="Step08: Verify China checked in prompt")
           
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 28)
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,28,"Step08: Verify Grid1 risers")
         
        """
        Step09: Select Insert > Chart in the Home Tab
        Step10: Add fields "Store,Country", "Product,Category", and "Cost of Goods"
        """
        time.sleep(3)
        ribbonobj.select_ribbon_item('Home', 'Insert',opt='Chart')
        time.sleep(10)
        resultobj.verify_panel_caption_label(0, 'Bar Stacked1', "Step10: Verify Bar Stacked1 is displayed")
        resultobj.verify_panel_caption_label(1, 'Grid1', "Step10: Verify Grid1 is displayed")
         
        time.sleep(4)
        metaobj.datatree_field_click("Store,Country", 2, 1)       
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
         
        """
        Step11: Verify Preview
        """  
        time.sleep(5)
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 28)
                  
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step11:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step11:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Brazil: Accessories','Brazil: Camcorder', 'Brazil: Computers']
        time.sleep(2)
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 28, 'Step11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step11.c: Verify first bar color")
        time.sleep(5)
             
        bar=['Store Country:Brazil', 'Product Category:Accessories', 'Cost of Goods:$2,197,681.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g0!mbar", bar, "Step11: Verify bar value")
                
        time.sleep(5)
        heading = ['Store C...', 'Product C...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step11: Verify column titles')
        row_val=['Brazil','Accessories', '$3,174,057.03']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step11: verify grid 1st row value')
        expected_tooltip=['Store Country:Brazil', 'Product Category:Accessories', 'Revenue:$3,174,057.03', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_1","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step11: verify the default tooltip values")
         
        """
        Step12: Drag and drop "Product,Category" into the Filter pane
        Step13: De-select [All] to de-select all values
        Step14: Check off values: Computers, Media Player, and Televisions > click OK
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 1, 1,'Filter') 
         
        time.sleep(3)
        l=['[All]','Computers', 'Media Player','Televisions']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        time.sleep(2)
         
        """
        Step15: Verify Preview
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('2', '[All]',verify=True, verify_type=False,msg="Step15: Verify All unchecked in prompt")
        propertyobj.select_or_verify_show_prompt_item('2', 'Computers',verify=True, scroll_down=True,verify_type=True,msg="Step15: Verify Computers checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('2', 'Media Player',verify=True,scroll_down=True, verify_type=True,msg="Step15: Verify Media Player checked in prompt")
        propertyobj.select_or_verify_show_prompt_item('2', 'Televisions',verify=True,scroll_down=True, verify_type=True,msg="Step15: Verify Televisions checked in prompt")
#         utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(5)
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 12)
         
        parent_css= "#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step15:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step15:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        time.sleep(2)
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step15.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar", "bar_blue", "Step15.c: Verify first bar color")
        time.sleep(5)
            
        bar=['Store Country:Brazil', 'Product Category:Media Player', 'Cost of Goods:$4,798,755.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g1!mbar", bar, "Step15: Verify bar value")
               
        time.sleep(5)
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step15: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step15: verify grid 1st row value')
        expected_tooltip=['Store Country:Brazil', 'Product Category:Computers', 'Revenue:$2,081,329.04', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_1","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step15: verify the default tooltip values")
        
        """
        Step16: Click "New" in the toolbar > select "Build a Visualization" > select wf_retail_lite
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_new')
        time.sleep(2)
        ribbonobj.select_item_in_splash_options('Build a Visualization')
        time.sleep(6)
#         utillobj.ibfs_save_as('wf_retail_lite.mas')
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step17: Add fields "Cost of Goods" and "Product,Subcategory"
        """
        time.sleep(4)
        metaobj.datatree_field_click("Cost of Goods",2,1)
        time.sleep(6)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)

        """
        Step18: Drag and drop "Product,Category" into the Filter pane
        """
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 1, 1,'Filter') 
         
        """
        Step19: De-select [All] to de-select all values
        Step20: Check off values: Computers and Televisions > click OK        
        """
        time.sleep(3)
        l=['[All]','Computers','Televisions']
        metaobj.create_visualization_filters('alpha',['GridItems',l])
        time.sleep(2)
 
        """
        Step21: Verify Preview
        """  
        time.sleep(5)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 5)
                  
        xaxis_value="Product Subcategory"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step21:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", "Cost of Goods", "Step21:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['CRT TV','Flat Panel TV','Portable TV','Smartphone','Tablet']
        time.sleep(2)
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step21.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar", "bar_blue", "Step21.c: Verify first bar color")
        time.sleep(5)
             
        bar=['Product Subcategory:Flat Panel TV', 'Cost of Goods:$59,077,345.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("TableChart_1", "riser!s0!g1!mbar", bar, "Step21: Verify bar value")

        """
        Step22: Click the switch "Reports" shortcut in the lower right corner
        Step23: Select "Visual1" > Verify Preview
        """        
        time.sleep(2)
        self.driver.find_element_by_css_selector("#sbpSwitchReport div[id^='BiComponent']").click()
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Visual1')
        time.sleep(2)
        
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 12)
         
        parent_css= "#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step23:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step23:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        time.sleep(2)
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step23:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step23.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar", "bar_blue", "Step23.c: Verify first bar color")
        time.sleep(5)
            
        bar=['Store Country:Brazil', 'Product Category:Media Player', 'Cost of Goods:$4,798,755.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g1!mbar", bar, "Step23: Verify bar value")
               
        time.sleep(5)
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step23: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step23: verify grid 1st row value')
        expected_tooltip=['Store Country:Brazil', 'Product Category:Computers', 'Revenue:$2,081,329.04', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_1","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step23: verify the default tooltip values")
        
        """
        Step24: Click the switch "Reports" shortcut in the lower right corner > Select "Visual2" > Verify Preview
        """
        time.sleep(2)
        self.driver.find_element_by_css_selector("#sbpSwitchReport div[id^='BiComponent']").click()
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Visual2')
        time.sleep(2)
        
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 5)
                  
        xaxis_value="Product Subcategory"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step24:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", "Cost of Goods", "Step24:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['CRT TV','Flat Panel TV','Portable TV','Smartphone','Tablet']
        time.sleep(2)
        expected_yval_list=['0','10M','20M','30M','40M','50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step24:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step24.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar", "bar_blue", "Step24.c: Verify first bar color")
        time.sleep(5)
             
        bar=['Product Subcategory:Flat Panel TV', 'Cost of Goods:$59,077,345.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("TableChart_1", "riser!s0!g1!mbar", bar, "Step24: Verify bar value")

        """
        Step25: Click the switch "Reports" shortcut in the lower right corner > Select "Visual1" > Verify Preview
        """
        time.sleep(2)
        self.driver.find_element_by_css_selector("#sbpSwitchReport div[id^='BiComponent']").click()
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu('Visual1')
        time.sleep(2)
        
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 12)
         
        parent_css= "#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step25:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step25:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        time.sleep(2)
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step26:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step25.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar", "bar_blue", "Step25.c: Verify first bar color")
        time.sleep(5)
            
        bar=['Store Country:Brazil', 'Product Category:Media Player', 'Cost of Goods:$4,798,755.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g1!mbar", bar, "Step25: Verify bar value")
               
        time.sleep(5)
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step25: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step25: verify grid 1st row value')
        expected_tooltip=['Store Country:Brazil', 'Product Category:Computers', 'Revenue:$2,081,329.04', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_1","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step25: verify the default tooltip values")
        
        """
        Step26: Click Run > Verify output
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(10) 
        
        time.sleep(2)        
        parent_css="#MAINTABLE_wbody2_f svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 12)
         
        parent_css= "#MAINTABLE_wbody1_f .colHeaderScroll text"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2_f", xaxis_value, "Step26:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2_f", "Cost of Goods", "Step26:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        time.sleep(2)
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2_f", expected_xval_list, expected_yval_list, "Step26:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2_f", 1, 12, 'Step26.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody2_f", "riser!s0!g1!mbar", "bar_blue", "Step26.c: Verify first bar color")
        time.sleep(5)
            
        bar=['Store Country:Brazil', 'Product Category:Media Player', 'Cost of Goods:$4,798,755.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2_f", "riser!s0!g1!mbar", bar, "Step26: Verify bar value")
               
        time.sleep(5)
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody1_f',heading, 'Step26: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('MAINTABLE_wbody1_f',row_val,'Step26: verify grid 1st row value')
        expected_tooltip=['Store Country:Brazil', 'Product Category:Computers', 'Revenue:$2,081,329.04', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1_f","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step26: verify the default tooltip values")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227714_Actual_step26', image_type='actual',x=1, y=1, w=-1, h=-1)
                    
        """
        Step27: Close
        Step08: Click Save in the toolbar
        Step09: Save as "C2158150" > Click Save
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
        Step29: Click "IA" > "Close"
        """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(2)
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#TableChart_1 svg g text[class*='yaxis-labels!']"
        resultobj.wait_for_property(parent_css, 8)
        parent_css="#TableChart_1 svg g text[class*='xaxisOrdinal-title']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#TableChart_1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
           
        """
        Step30: Click "Save" > "C2158288_Visual2" > click Save
        """        
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                         
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID+'_Visual2')
        time.sleep(5)
                         
        """
        Step31: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
          
        """
        Step32: Reopen fex using IA API:
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
          
        """
        Step33: Verify the following is displayed.
        """
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 12)
         
        parent_css= "#TableChart_1 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
         
        xaxis_value="Store Country : Product Category"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step33:d(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", "Cost of Goods", "Step33:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_xval_list=['Brazil: Computers','Brazil: Media Player', 'Brazil: Televisions']
        time.sleep(2)
        expected_yval_list=['0','20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step33:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step33.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g1!mbar", "bar_blue", "Step33.c: Verify first bar color")
        time.sleep(5)
            
        bar=['Store Country:Brazil', 'Product Category:Media Player', 'Cost of Goods:$4,798,755.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g1!mbar", bar, "Step33: Verify bar value")
               
        time.sleep(5)
        heading = ['Store C...', 'Product Ca...', 'Revenue']
        resultobj.verify_grid_column_heading('TableChart_1',heading, 'Step33: Verify column titles')
        row_val=['Brazil', 'Computers', '$2,081,329.04']
        resultobj.verify_grid_row_val('TableChart_1',row_val,'Step33: verify grid 1st row value')
        expected_tooltip=['Store Country:Brazil', 'Product Category:Computers', 'Revenue:$2,081,329.04', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("TableChart_1","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step33: verify the default tooltip values")
        time.sleep(3)



    def select_or_verify_visualization_filter_values(self, item_list, **kwargs):
        utillobj = utillity.UtillityMethods(self.driver)
        if 'msg' in kwargs:
            kwargs['msg'] =  kwargs['msg']
        else:
            kwargs['msg'] = 'Step X:'
        for item in item_list:
            flag = 0
            checkbox_item_css="div[id$='ValuesBox']  div[id^='CheckBoxItem']"
            while flag < 200:
                elem=self.driver.find_elements_by_css_selector(checkbox_item_css)
                elem_list=[el.text.strip() for el in elem]
                if item in elem_list:
                    if 'verify' in kwargs: 
                        status=elem[elem_list.index(item)].find_element_by_css_selector("input").get_attribute("checked")
                        if status == 'true':
                            utillobj.asequal(self, status, kwargs['verify'], kwargs['msg']+" verify " + item + " is checked in filter box.")
                        else:
                            utillobj.asequal(self, status, kwargs['verify'], kwargs['msg']+" verify " + item + " is Unchecked in filter box.")
                    else:
                        val_obj=elem[elem_list.index(item)].find_element_by_css_selector("input")
                        if 'scroll_down' in kwargs:
                            self.driver.execute_script("arguments[0].scrollIntoView(true);", val_obj)
                        time.sleep(4)
                        utillobj.default_left_click(self,object_locator=val_obj,action_move=True, **kwargs)
                    flag = 200
                else:
                    for i in range(8):
                        self.driver.find_element_by_css_selector("div[id$='ValuesBox'] [class*='scroll-bar-vertical'] [class*='scroll-bar-inc-button']").click()
                    flag = flag + 8
                    time.sleep(1)
            try:
                if flag > 200:
                    raise ValueError(item + "does not exist in filter grid")
            except ValueError as err:
                print(err.args)
        
        if 'Ok_button' in kwargs:
            self.driver.find_element_by_id("avFilterOkBtn").click()
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()