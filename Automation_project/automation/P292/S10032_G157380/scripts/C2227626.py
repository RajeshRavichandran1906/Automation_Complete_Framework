'''
Created on May 22, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227626
TestCase Name = Drill down with Treemap chart type 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227626_TestClass(BaseTestCase):

    def test_C2227626(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2227626'
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
         
        """
        Step 02: Click "Change" in the Home Tab > Select "Treemap" chart
        """
        ribbonobj.change_chart_type("treemap")
        
        """
        Step 03: Double-click "Cost of Goods"
        """
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        
        """
        Step 04: Double-click "Product,Category"
        """
        time.sleep(4)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 svg g>rect[class^='group-header!']"
        resultobj.wait_for_property(parent_css, 7)
        
        """
        Step 05: Drag and drop "Gross Profit" into the Color bucket
        """
        time.sleep(4)
        metaobj.datatree_field_click('Gross Profit',1, 1, 'Add To Query', 'Color')
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 svg g>rect[class^='group-header!']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        
        """
        Step 06: Verify canvas
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 svg g>rect[class^='group-header!']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 7, 'Step 06a: Verify number of Circle displayed', custom_css="svg g>rect[class^='riser!s']")
        expected_xval_list=['Stereo Systems', 'Media Player', 'Camcorder', 'Accessories', 'Computers', 'Televisions', 'Video Production']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 06.b: X and Y axis Scales Values has changed or NOT', x_custom_css="text[text-anchor='middle']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!sStereo Systems!g0!mnode", "elf_green", "Step 06.c(i) Verify first bar color")
        legend=['Gross Profit', '16.8M', '34.2M', '51.5M', '68.8M', '86.2M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step06:d(ii) Verify legend Title")
        time.sleep(2)
        expected_tooltip=['Product Category:Stereo Systems', 'Cost of Goods:$205,113,863.00', 'Gross Profit:$86,181,070.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!sStereo Systems!g0!mnode",expected_tooltip, "Step 06.e: verify the default tooltip values")       
        
        """
        Step 07:  Hover over "Stereo Systems" (green area) > Select "Drill down to Product Subcategory"
        """
        time.sleep(5)
        raiser="[id^='MAINTABLE_1'] [class*='riser!sStereo Systems!g0!mnode']"
        elem1=(By.CSS_SELECTOR, raiser)
        resultobj._validate_page(elem1) 
        time.sleep(3)        
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!sStereo Systems!g0!mnode", "Drill down to Product Subcategory", wait_time=1)
        time.sleep(5)
        
        """
        Step 08: Verify Preview
        """
        time.sleep(6)
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody1 svg g>rect[class^='group-header!']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step08.a:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 5, 'Step 08.a: Verify number of Circle displayed', custom_css="svg g>rect[class^='riser!s']")
        expected_xval_list=['Speaker Kits', 'Home Theater Systems', 'Receivers', 'iPod Docking Station']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 08.b: X and Y axis Scales Values has changed or NOT', x_custom_css="text[text-anchor='middle']")
        
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!sHome Theater Systems!g0!mnode", "elf_green", "Step 08.c(i) Verify first bar color")
        legend=['Gross Profit', '0.5M', '7.4M', '14.2M', '21M', '28M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step08:d(i) Verify Y-Axis Title")
        time.sleep(2)
        expected_tooltip=['Product Subcategory:Speaker Kits', 'Cost of Goods:$81,396,140.00', 'Gross Profit:$25,819,241.69', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!sSpeaker Kits!g0!mnode",expected_tooltip, "Step 08.e: verify the default tooltip values")       
        
        """
        Step 09: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 10: Hover over "Receivers" > "Drill down to Model"
        """
        chart_type_css="rect[class*='riser!sSpeaker Kits!g0!mnode']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody1 svg g>rect[class^='group-header!']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        resultobj.select_default_tooltip_menu('MAINTABLE_wbody1', "riser!sReceivers!g0!mnode", "Drill down to Model", wait_time=1)
        time.sleep(5)
        
        """
        Step 11: Verify output
        """
        chart_type_css="rect[class*='riser!sOnkyo TXSR876B!g0!mnode']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(8)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css="#MAINTABLE_wbody1 svg g>rect[class^='group-header!']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 6, 'Step 11.a: Verify number of Circle displayed', custom_css="svg g>rect[class^='riser!s']")
        expected_xval_list=['Onkyo TXSR876B', 'Yamaha RXV465', 'Sony STRDA1500', 'Yamaha RXV3900', 'Sony STRDH810', 'Yamaha RXV2065']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 11.b: X and Y axis Scales Values has changed or NOT', x_custom_css="text[text-anchor='middle']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!sYamaha RXV465!g0!mnode", "elf_green", "Step 11.c(i) Verify first bar color")
        legend=['Gross Profit', '1.9M', '2.3M', '2.8M', '3.2M', '3.6M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:d(ii) Verify Y-Axis Title")
        time.sleep(2)
        expected_tooltip=['Model:Onkyo TXSR876B', 'Cost of Goods:$7,810,644.00', 'Gross Profit:$2,897,512.77', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!sOnkyo TXSR876B!g0!mnode",expected_tooltip, "Step 11.e: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227626_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 12: Close output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 13: Click "Save" > Save as "C2167769" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        
        """
        Step 14: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
             
        """
        Step 15: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
            
        """
        Step 16: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="rect[class*='riser!sSpeaker Kits!g0!mnode']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser!s']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody1 svg g>rect[class^='group-header!']"
        resultobj.wait_for_property(parent_css, 5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='colorScaleLegend-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step16.a:")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 5, 'Step 16.a: Verify number of Circle displayed', custom_css="svg g>rect[class^='riser!s']")
        expected_xval_list=['Speaker Kits', 'Home Theater Systems', 'Receivers', 'iPod Docking Station']
        expected_yval_list=[]
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody1', expected_xval_list, expected_yval_list, 'Step 16.b: X and Y axis Scales Values has changed or NOT', x_custom_css="text[text-anchor='middle']")
        time.sleep(5)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!sHome Theater Systems!g0!mnode", "elf_green", "Step 16.c(i) Verify first bar color")
        legend=['Gross Profit', '0.5M', '7.4M', '14.2M', '21M', '28M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step16:d(i) Verify Y-Axis Title")
        time.sleep(2)
        expected_tooltip=['Product Subcategory:Speaker Kits', 'Cost of Goods:$81,396,140.00', 'Gross Profit:$25,819,241.69', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!sSpeaker Kits!g0!mnode",expected_tooltip, "Step 16.e: verify the default tooltip values")       
        time.sleep(5)
        
        """
        Step 17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()