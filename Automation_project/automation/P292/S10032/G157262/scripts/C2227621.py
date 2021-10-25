'''
Created on May 24, 2017

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227621
TestCase Name = Drill down with Area chart type 
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227621_TestClass(BaseTestCase):
    
    def test_C2227621(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227621'

        """
        Step01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
                  
        """
        Step02: Click "Change" in the Home Tab > Select "Area" chart
        """
        ribbonobj.change_chart_type('area')
                    
        """
        Step03: Double-click "Cost of Goods" and "Gross Profit"
        Step04: Double-click "Product,Category"
        """  
        time.sleep(5)      
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-title']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 2)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
         
        """
        Step 05:  Hover over value for "Cost of Goods" and "Computers" > Select "Drill down to Product Subcategory"
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 7)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g2!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle', javascript_marker_enable = True,mouse_duration=3)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g2!mmarker",bar, msg="Step05: Verify line value",default_move=True)        
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'middle')
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g2!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable = True,mouse_duration=3)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "marker!s0!g2!mmarker",'Drill down to Product Subcategory',default_move=True)
         
        """
        Step06:Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step06.a:")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step06:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step06:a(i) Verify Y-Axis Title")
        expected_xval_list=['Smartphone','Tablet']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'top_middle')
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable = True,mouse_duration=3)
        bar=['Product Subcategory:Smartphone', 'Cost of Goods:$44,035,774.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker", bar, msg="Step06: Verify line value",default_move=True)
         
        """
        Step07:Hover over value for "Cost of Goods" and "Smartphone" > Verify Menu > Select "Drill down to Model" 
        """
#         time.sleep(5)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
#         utillobj.click_on_screen(parent_elem, 'top_middle')
#         time.sleep(3)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
#         utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable = True,mouse_duration=2.5)
#         bar=['Product Subcategory:Smartphone', 'Cost of Goods:$44,035,774.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker",bar, msg="Step07: Verify line value",default_move=True)        
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'middle')
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable = True,mouse_duration=3)
#         utillobj.synchronize_with_number_of_element(parent_elem, 1, 25)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "marker!s0!g0!mmarker",'Drill down to Model',default_move=True)
         
        """
        Step08:Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 10)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        time.sleep(5)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step08.a:")
        metaobj.verify_filter_pane_field('Product,Subcategory',2,"Step08.b:")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Model', "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step08:a(i) Verify Y-Axis Title")
        expected_xval_list=['C6506B','C6506S','C6506W','GS4B','GS4S','GS4W','LT22i-SLB','LT22i-SLW','i897B','i898W']
        expected_yval_list=['0', '1M', '2M', '3M', '4M', '5M', '6M', '7M', '8M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'top_middle')
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable = True,mouse_duration=3)
        bar=['Model:C6506B', 'Cost of Goods:$7,199,829.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker", bar, msg="Step08: Verify line value",default_move=True)
         
        """
        Step09: Click Undo button in the toolbar
        """
        time.sleep(5)
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        time.sleep(5)
         
        """
        Step10: Verify Preview
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(2)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step10.a:")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step10:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step10:a(i) Verify Y-Axis Title")
        expected_xval_list=['Smartphone','Tablet']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step10:a(iii):Verify XY labels")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'top_middle')
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable = True,mouse_duration=3)
        bar=['Product Subcategory:Smartphone', 'Cost of Goods:$44,035,774.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker", bar, msg="Step10: Verify line value",default_move=True)
        
        """
        Step 11: Click Run
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_window(1)
        time.sleep(2) 
        
        """
        Step 12: Hover over value for 'Gross Profit' and 'Tablet' > Verify menu > Select "Drill down to Model"
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!marea!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step12:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step12:a(i) Verify Y-Axis Title")
        expected_xval_list=['Smartphone','Tablet']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        time.sleep(5)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
#         utillobj.click_on_screen(parent_elem, 'bottom_middle')
#         time.sleep(5)
#         parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g1!mmarker']")
#         utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable = True,mouse_duration=2.5)
#         bar=['Product Subcategory:Tablet', 'Gross Profit:$17,674,115.97', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
#         resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s1!g1!mmarker", bar, msg="Step12: Verify line value",default_move=True)
        
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(1)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g1!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable = True,mouse_duration=2.5)
#         utillobj.synchronize_with_number_of_element(parent_elem, 1, 25)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "marker!s1!g1!mmarker",'Drill down to Model',wait_time=0,default_move=True)
        
        """
        Step 13: Verify output and hover over pop up menu
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 10)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 9)
        time.sleep(2)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Model', "Step13:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step13:a(i) Verify Y-Axis Title")
        expected_xval_list=['GLXYT10716','GLXYT10732','GLXYT3B','GLXYT3W','GLXYT70','SGP311U1/B','SGP312U1/B']
        expected_yval_list=['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(1)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'top_middle', javascript_marker_enable = True, mouse_duration=3)
        bar=['Model:GLXYT10716', 'Cost of Goods:$3,618,906.00', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker", bar, msg="Step13: Verify line value",default_move=True)
        time.sleep(8)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227621_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 14: Close output window
        """
        time.sleep(1)
        self.driver.close()
        time.sleep(1)
        utillobj.switch_to_window(0)
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        
        """
        Step 15: Click "Save" > Save as "C2167744" > Click Save
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(1)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(1)
         
        """
        Step 16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 17: Reopen fex using IA API: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158195.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_visual_3',mrid='mrid',mrpass='mrpass')
             
        """
        Step 18: Verify Preview
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        parent_css= "#MAINTABLE_wbody1 svg g text[class*='yaxis-labels']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(1)
        metaobj.verify_filter_pane_field('Product,Category',1,"Step18.a:")
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step18:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step18:a(i) Verify Y-Axis Title")
        expected_xval_list=['Smartphone','Tablet']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step18:a(iii):Verify XY labels")
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'bottom_middle')
        time.sleep(1)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',javascript_marker_enable = True,mouse_duration=2.5)
        bar=['Product Subcategory:Smartphone', 'Cost of Goods:$44,035,774.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker", bar, msg="Step18: Verify line value",default_move=True)
        time.sleep(2)
        
        """
        Step 19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
                
if __name__ == '__main__':
    unittest.main()