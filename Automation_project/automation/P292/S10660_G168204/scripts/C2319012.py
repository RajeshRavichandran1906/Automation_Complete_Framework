'''
Created on Oct 7, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319012
TestCase Name = Lasso Filter using Stacked Area chart type
'''

import unittest
from selenium.webdriver import ActionChains
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2319012_TestClass(BaseTestCase):
    
    def test_C2319012(self):
        
        """
            TESTCASE VARIABLES
        """
        
        Test_Case_ID = 'C2319012'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10660_visual_1', 'mrid', 'mrpass')                        
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
                              
        """
        Step02: Click "Change" in the Home Tab > Select "Stacked Areas" chart
        """
        ribbonobj.change_chart_type('stacked_area')
        time.sleep(5)
                                 
        """
        Step03: Double-click "Cost of Goods", "Gross Profit" and "Revenue"
        Step04: Double-click "Product,Category"
        """        
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
                         
        """
        Step05: Lasso values "Stereo Systems" thru => "Video Production" in the Stacked Area chart > Select "Filter Chart"
        """   
        parent_css="#MAINTABLE_wbody1 [class*='marker!s']"
        resultobj.wait_for_property(parent_css, 21)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s2!g4!mmarker']")
        coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        sx=coord['x']-30
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g6!mmarker']")
        coord1=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        sy=coord['y']-30
        tx=coord1['x']+10
        ty=coord1['y']+70
        time.sleep(5)
        utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
        time.sleep(5)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
                        
        """
        Step06:Verify canvas
        """                  
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step06:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit','Revenue'], "Step06:a(i) Verify Y-Axis Title")
        expected_xval_list=['Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','100M','200M','300M','400M','500M','600M','700M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s2!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'start',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Stereo Systems', 'Revenue:$291,294,933.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s2!g0!mmarker",bar, msg="Step06: Verify line value",default_move=True)        
               
        """
        Step07: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)                 
                      
        """
        Step08: Verify Output
        """
        time.sleep(10)
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit','Revenue'], "Step08:a(i) Verify Y-Axis Title")
        expected_xval_list=['Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0','100M','200M','300M','400M','500M','600M','700M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')              
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s2!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        browser=utillobj.parseinitfile("browser")
        if browser == 'IE':
            time.sleep(2)
        else:
            time.sleep(1)
        bar=['Product Category:Stereo Systems', 'Revenue:$291,294,933.52', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s2!g0!mmarker",bar, msg="Step08: Verify line value",default_move=True)        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2319012_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
                
        """
        Step09: Close the output window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
              
        """
        Step10: Lasso "Televisions" and "Video Production" > Select "Filter Chart"
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s2!g1!mmarker']")
        coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        sx=coord['x']-15
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g2!mmarker']")
        coord1=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        sy=coord['y']-60
        tx=coord1['x']+10
        ty=coord1['y']+70
        time.sleep(5)
        utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
        time.sleep(5)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        """
        Step11: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit','Revenue'], "Step11:a(i) Verify Y-Axis Title")
        expected_xval_list=['Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_left')              
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable=True,mouse_duration=2.5)
        browser=utillobj.parseinitfile("browser")
        if browser == 'IE':
            time.sleep(2)
        else:
            time.sleep(1)
        bar=['Product Category:Televisions', 'Cost of Goods:$61,551,109.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker",bar, msg="Step11: Verify line value",default_move=True)        
        time.sleep(3)
               
        """
        Step12: Click "Swap" in the Home Tab ribbon
        """
        time.sleep(5)
        ribbonobj.select_ribbon_item('Home', 'Swap')
        time.sleep(3)
            
        """
        Step13:Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step13:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit','Revenue'], "Step15:a(i) Verify Y-Axis Title")
        expected_xval_list=['Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        metaobj.verify_query_pane_field('Vertical Axis',"Product,Category",1,"Step13: Verify Vertical axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Cost of Goods",1,"Step13: Verify Horizontal axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Gross Profit",2,"Step13: Verify Horizontal axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Revenue",3,"Step13: Verify Horizontal axis after swap")
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Televisions', 'Cost of Goods:$61,551,109.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker",bar, msg="Step13: Verify line value",default_move=True)        
         
        """
        Step14: Hover over blue Area for "Televisions" > Select "Filter Chart"
        """  
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'top_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=3)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1","marker!s0!g0!mmarker",'Filter Chart',default_move=True,wait_time=1)
        time.sleep(3) 
         
        """
        Step15:Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step15:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit','Revenue'], "Step15:a(i) Verify Y-Axis Title")
        expected_xval_list=['Televisions']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_right',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Televisions', 'Cost of Goods:$61,551,109.00','Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker",bar, msg="Step15: Verify line value",default_move=True)        
        time.sleep(3)
         
        """
        Step16: Click Undo
        Step17: Verify Canvas
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        time.sleep(3)
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step17:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit','Revenue'], "Step17:a(i) Verify Y-Axis Title")
        expected_xval_list=['Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step17:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        metaobj.verify_query_pane_field('Vertical Axis',"Product,Category",1,"Step17: Verify Vertical axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Cost of Goods",1,"Step17: Verify Horizontal axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Gross Profit",2,"Step17: Verify Horizontal axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Revenue",3,"Step17: Verify Horizontal axis after swap")
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Televisions', 'Cost of Goods:$61,551,109.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker",bar, msg="Step17: Verify line value",default_move=True)        
        time.sleep(3)        
                      
        """
        Step18: Click Save in the toolbar
        Step19: Save as "C2319012" > Click Save
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                       
        """
        Step20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
                   
        """
        Step21: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10660_visual_1',mrid='mrid',mrpass='mrpass')
                    
        """
        Step22: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step22:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit','Revenue'], "Step22:a(i) Verify Y-Axis Title")
        expected_xval_list=['Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step22:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        metaobj.verify_query_pane_field('Vertical Axis',"Product,Category",1,"Step22: Verify Vertical axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Cost of Goods",1,"Step22: Verify Horizontal axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Gross Profit",2,"Step22: Verify Horizontal axis after swap")
        metaobj.verify_query_pane_field('Horizontal Axis',"Revenue",3,"Step22: Verify Horizontal axis after swap")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')
        time.sleep(1)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Televisions', 'Cost of Goods:$61,551,109.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker",bar, msg="Step22: Verify line value",default_move=True)        
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()