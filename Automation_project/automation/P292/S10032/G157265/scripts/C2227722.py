'''
Created on Jun 22, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227722
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run,\
    ia_run,wf_mainpage,ia_resultarea
from common.locators import visualization_resultarea_locators
from common.lib import utillity
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pyautogui import click


class C2227722_TestClass(BaseTestCase):

    def test_C2227722(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227722'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        wf_mainobj = wf_mainpage.Wf_Mainpage(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1) 
        time.sleep(5)
        
        """
        Step02: Verify the following chart is displayed.
        """
        
        parent_css="#TableChart_1 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 12)
        resultobj.verify_number_of_riser("TableChart_1", 3,4, 'Step01.b: Verify the total number of risers displayed on preview')
                     
        """
        Step03: Verify the "Swap" and "Clear" buttons are disabled on the Home Tab
        """
        time.sleep(3)
        self.object_visibility("#SwapVisualization>div",'true',"Step03: Verify swap disabled")
        self.object_visibility("#ClearVisualization>div",'true',"Step03: Verify clear disabled")
    
        """
        Step04: Double click "Product,Category".
        """        
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
           
        """
        Step05: Verify the following chart is displayed.
        """  
        time.sleep(5)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
                    
        xaxis_value="Product Category"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step05:d(i) Verify X-Axis Title")
        time.sleep(3)
        expected_xval_list=['Accesories','Camcorder', 'Computers','Media Player','Stereo Systems','Televisions','Video Production']
        time.sleep(2)
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step05:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step05.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step05.c: Verify first bar color")
        time.sleep(5)
        
        """
        Step06: Verify the "Swap" and "Clear" buttons are enabled
        """
        time.sleep(3)
        self.object_visibility("#SwapVisualization>div",None,"Step06: Verify swap enabled")
        self.object_visibility("#ClearVisualization>div",None,"Step06: Verify clear enabled")
        
        """
        Step07: Select Clear to remove the visualization
        """
        ribbonobj.select_ribbon_item('Home', 'Clear')
        time.sleep(2)
        utillobj.click_dialog_button("div[id^='BiDialog']", "OK")
        time.sleep(2)        
        
        """
        Step08: Double click "Revenue".
        Step09: Verify the "Swap" and "Clear" buttons are enabled on the Home Tab
        Step10: Verify the following chart is displayed.
        """
        time.sleep(4)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(3)
        self.object_visibility("#SwapVisualization>div",None,"Step09: Verify swap enabled")
        self.object_visibility("#ClearVisualization>div",None,"Step09: Verify clear enabled")
        
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
                    
        yaxis_value="Revenue"
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step10:d(i) Verify Y-Axis Title")
        time.sleep(3)
        expected_yval_list=['0','0.2B','0.4B','0.6B','0.8B','1B']
        time.sleep(2)
        expected_xval_list=[]
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 1, 'Step10.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step10.c: Verify first bar color")
        time.sleep(5)
        
        """
        Step11: Double click "Gross Profit","Product,Category".
        """
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        """
        Step12: Verify the following is displayed in the Query pane.
        """
        metaobj.verify_query_pane_field('Vertical Axis', 'Revenue', 1, "Step12: Verify Revenue in query pane")
        metaobj.verify_query_pane_field('Vertical Axis', 'Gross Profit', 2, "Step12: Verify Gross Profit in query pane")
        metaobj.verify_query_pane_field('Horizontal Axis', 'Product,Category', 1, "Step12: Verify Product Category in query pane")
        
        """
        Step13: Verify the following chart is displayed.
        """           
        xaxis_value="Product Category"
        expected_legend_list=['Revenue','Gross Profit']
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step13:d(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", expected_legend_list,"Step13:d(i) Verify Y-Axis legends")
        time.sleep(3)
        expected_xval_list=['Accesories','Camcorder', 'Computers','Media Player','Stereo Systems','Televisions','Video Production']
        time.sleep(2)
        expected_yval_list=['0','50M','100M','150M','200M','250M','300M','350M','400M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 2, 7, 'Step13.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step13.c: Verify first bar color")
        time.sleep(5)
               
        bar=['Product Category:Accessories', 'Revenue:$129,608,338.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar, "Step13: Verify bar value")
        
        """
        Step14: Drag "Customer,Business,Region" to the "Filter" pane.
        """
        time.sleep(2)
        metaobj.datatree_field_click("Customer,Business,Region",1,1,'Filter')
        time.sleep(2)
        
        """
        Step15: Verify the following "Filter" window is displayed.
        Step16: Click "OK".
        """
        item_list=['[All]','EMEA','North America','Oceania','South America']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true', Ok_button=True,msg='Step15: Verify filter window')
        
        """
        Step17: Verify "Filter Prompt" is displayed
        """
        time.sleep(2)
        parent_css="#resultArea div[id^='BoxLayoutFilterWindow']"
        resultobj.wait_for_property(parent_css, 1)
        propertyobj.select_or_verify_show_prompt_item(1, '[All]',verify=True, verify_type=True,msg="Step17: Verify Filter Prompt")
        
        """
        Step18: Verify "Customer,Business,Region" appears in the "Filter" pane.
        """
        time.sleep(2)
        metaobj.verify_filter_pane_field("Customer,Business,Region", 1, "Step18: Verify Filter Pane")
        
        """
        Step19: Select "Home" > "Visual" > "Change" (dropdown) > click "Map" button
        Step20: Select "Leaftlet Map: Choropleth"
        Step21: Select "Territory" = "World".
        Step22: Click "OK".
        Step23: Set "Geographic Role" = "iso_a2 (...)".
        Step24: Click "OK".
        """
        ribbonobj.change_chart_type('map')
        time.sleep(3)
        ribbonobj.select_map('choropleth',teritory='World',btn_click='ok')
        time.sleep(3) 
        time.sleep(5) 
        combo_btn=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #geoRoleComboBox div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn,"iso_a2 (AD, AE, AF)")
        time.sleep(2)
        btn_css="div[id*='locTypeOkBtn'] div[class=bi-button-label]"
        self.driver.find_element_by_css_selector(btn_css).click()
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
         
        """
        Step25: Double click "Customer,Country,ISO-3166,Code".
        Step26: Set "Geographic Role" = "iso_a2 (...)".
        Step27: Click "OK".
        """ 
        metaobj.datatree_field_click("Customer,Country,ISO-3166,Code", 2, 1)
        time.sleep(5) 
        combo_btn=self.driver.find_element_by_css_selector("div[id^='QbDialog'] #geoRoleComboBox div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn,"iso_a2 (AD, AE, AF)")
        time.sleep(2)
        btn_css="div[id*='locTypeOkBtn'] div[class=bi-button-label]"
        self.driver.find_element_by_css_selector(btn_css).click()
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 42)
        
        """
        Step28: Verify it displayed the following Choropleth map on the canvas.
        """
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",42, 'Step28.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mstate", "burnt_sienna", "Step28.c(i) Verify first bar color")
        legend=['Revenue','0.1M', '83.5M', '166.8M', '250.2M', '333.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step28:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Customer Country ISO-3166 Code:BR', 'Revenue:$38,995,120.68', 'Gross Profit:$11,022,235.68', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mstate",expected_tooltip, "Step28.e: verify the default tooltip values")       
        
        """
        Step29: Drag "Cost of Goods" to the Filter pane.
        Step30: Click "OK".
        """
        metaobj.datatree_field_click('Cost of Goods', 1, 1,'Filter')
        time.sleep(4)
        metaobj.create_visualization_filters('numeric')
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        
        """
        Step31: Verify both filters are displayed in the "Filter" pane.
        Step32: Verify it displayed the slider prompt.
        """   
        metaobj.verify_filter_pane_field('Customer,Business,Region',1,"Step31: Verify 'Customer business Region' appears in filter pane")        
        metaobj.verify_filter_pane_field('Cost of Goods',2,"Step31: Verify 'Cost of Goods' appears in filter pane")        
        time.sleep(2)
        
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','min','16',msg="Step32: Verify slider minimum value")
        propertyobj.verify_slider_range_filter_prompts('#ar_Prompt_2','max','13000',msg="Step32: Verify slider maximum value")
        time.sleep(2) 
        
        """
        Step33: Select "Home" > "Visual" > "Insert" (dropdown) > "Grid".
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Grid')
        
        """
        Step34: Verify the following is displayed.
        """
        time.sleep(10)
        resultobj.verify_panel_caption_label(0, 'Grid1', "Step34: Verify Grid1 is displayed")
        resultobj.verify_panel_caption_label(1, 'Choropleth Map1', "Step34: Verify Choropleth Map1 is displayed")
        
        """
        Step35: Double click "Customer,Country,ISO-3166,Code".
        Step36: Double click "Cost of Goods".
        Step37: Verify the following is displayed.
        """
        metaobj.datatree_field_click("Customer,Country,ISO-3166,Code", 2, 1)
        parent_css1="#MAINTABLE_wbody2 .rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
        time.sleep(10)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        parent_css1="#MAINTABLE_wbody2 .colHeaderScroll text"
        resultobj.wait_for_property(parent_css1, 1)
        heading = ['Customer Country ISO-3166 Code', 'Cost of Goods']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody2',heading, 'Step37: Verify column titles')
        row_val=['AR','$3,798,511.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody2',row_val,'Step37: verify grid 1st row value')
                  
        parent_css="#MAINTABLE_wbody2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 42)
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,42,"Step37: Verify Grid1 risers")
        expected_tooltip=['Customer Country ISO-3166 Code:AR', 'Cost of Goods:$3,798,511.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step37: verify the default tooltip values")
        
        """
        Step38: Add "Customer,Country,ISO-3166,Code" to Filter pane.
        Step39: Click "OK".
        """
        metaobj.datatree_field_click('Customer,Country,ISO-3166,Code', 1, 1,'Filter')
        time.sleep(4)
        metaobj.create_visualization_filters('alpha')
        time.sleep(5)
        parent_css="#resultArea div[id^='BoxLayoutFilterBox']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Customer,Business,Region',1,"Step39: Verify 'Customer business Region' appears in filter pane")        
        metaobj.verify_filter_pane_field('Cost of Goods',2,"Step39: Verify 'Cost of Goods' appears in filter pane")        
        metaobj.verify_filter_pane_field('Customer,Country,ISO-3166,Code',3,"Step39: Verify 'Customer,Country,ISO-3166,Code' appears in filter pane")        
        time.sleep(2)        
        
        """
        Step40: Vertical scroll down on the "Filter Prompt" slider.
        Step41: Verify it added to the "Filter Prompt" area.
        """
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('3', '[All]',verify=True,scroll_down=True, verify_type=True,msg="Step39: Verify [All] checked in prompt")
        
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 42)
        
        """
        Check title is wrapped and completely visible
        """
        val = self.driver.find_element_by_css_selector("#Prompt_3 table span").value_of_css_property("white-space")
        utillobj.asequal("wrap", val, "Step41.1: Verify Filter pane Customer,Country,ISO-3166,Code title in preview is completely visible(wrapped)")
        
        """
        Current scroll height & offsetheight in preview:
        379 > 379 (because scroll bar not present in preview)
        Current scroll height & offsetheight in run:
        991 > 379 (Scroll is available at runtime)
        """
        script ='obj=document.querySelector("#ar_Prompt_3");return obj.scrollHeight>obj.offsetHeight' 
        a=self.driver.execute_script(script)
        utillobj.asequal(True, a, "Step41.2: Verify Filter pane Customer,Country,ISO-3166,Code Scroll bar in preview")
        
        """
        Step42: On the "Customer,Country,ISO-3166,Code" filter, enable the checkboxes for "CN" and "CZ".
        """
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",42, 'Step41.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mstate", "burnt_sienna", "Step41.c(i) Verify first bar color")
        legend=['Revenue','0.1M', '83.5M', '166.8M', '250.2M', '333.5M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step41:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Customer Country ISO-3166 Code:BR', 'Revenue:$38,995,120.68', 'Gross Profit:$11,022,235.68', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g4!mstate",expected_tooltip, "Step41.e: verify the default tooltip values")       
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('3', 'CN',verify=False,scroll_down=True)
        time.sleep(5)
        propertyobj.select_or_verify_show_prompt_item('3', 'CZ',verify=False,scroll_down=True)
        time.sleep(5)
        
        """
        Step43: Verify the Grid has been updated to have those two countries.
        Step44: Verify the Choropleth Map has been updated to those two countries.
        """
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",2, 'Step43.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mstate", "persian_red", "Step43.c(i) Verify first bar color")
        legend=['Revenue', '0.2M', '4.2M', '8.2M', '12.2M', '16.2M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step43:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Customer Country ISO-3166 Code:CN', 'Revenue:$167,368.29', 'Gross Profit:$47,658.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mstate",expected_tooltip, "Step43.e: verify the default tooltip values")       
        time.sleep(5)
        
        parent_css1="#MAINTABLE_wbody2 .rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
          
        time.sleep(5)
        heading = ['Customer Country ISO-3166 Code', 'Cost of Goods']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody2',heading, 'Step43: Verify column titles')
        row_val=['CN', '$119,710.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody2',row_val,'Step43: verify grid 1st row value')
                  
        parent_css="#MAINTABLE_wbody2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,2,"Step43: Verify Grid1 risers")
        expected_tooltip=['Customer Country ISO-3166 Code:CN', 'Cost of Goods:$119,710.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step43: verify the default tooltip values")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,'C2227722_Actual_Step43', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step45: Click Save in the toolbar
        Save as "C2158150" > Click Save
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                      
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                 
        """
        Step46: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
            
        """
        Step47: Reopen fex using IA API:
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
            
        """
        Step48: Verify the following is displayed.
        """
        time.sleep(8)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1",2, 'Step48.a: Verify number of risers displayed', custom_css="svg g>path[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mstate", "persian_red", "Step48c(i) Verify first bar color")
        legend=['Revenue', '0.2M', '4.2M', '8.2M', '12.2M', '16.2M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step48:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Customer Country ISO-3166 Code:CN', 'Revenue:$167,368.29', 'Gross Profit:$47,658.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mstate",expected_tooltip, "Step48.e: verify the default tooltip values")       
        time.sleep(5)
        
        parent_css1="#MAINTABLE_wbody2 .rowTitle text"
        resultobj.wait_for_property(parent_css1,1)
          
        time.sleep(5)
        heading = ['Customer Country ISO-3166 Code', 'Cost of Goods']
        resultobj.verify_grid_column_heading('MAINTABLE_wbody2',heading, 'Step48: Verify column titles')
        row_val=['CN', '$119,710.00']
        resultobj.verify_grid_row_val('MAINTABLE_wbody2',row_val,'Step48: verify grid 1st row value')
                  
        parent_css="#MAINTABLE_wbody2 rect[class^='riser']"
        resultobj.wait_for_property(parent_css, 2)
        rise=len(self.driver.find_elements_by_css_selector(parent_css))
        utillobj.asequal(rise,2,"Step48: Verify Grid1 risers")
        expected_tooltip=['Customer Country ISO-3166 Code:CN', 'Cost of Goods:$119,710.00', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2","riser!s0!g0!mcellFill!r0!c0!",expected_tooltip, "Step48: verify the default tooltip values")
        time.sleep(5)
        
    def object_visibility(self,css,exp_stat,msg):
        try:
            stat=self.driver.find_element_by_css_selector(css).get_attribute('disabled')
            print(stat)
        except:
            stat=False
        utillity.UtillityMethods.asequal(self,stat,exp_stat, msg)
        

if __name__ == '__main__':
    unittest.main()