'''
Created on May 25, 2017
@author: Kiruthika
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227603
'''
import time
import unittest
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon

class C2227603_TestClass(BaseTestCase):
    
    def test_C2227603(self):
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227603'

        """ 
        TESTCASE OBJECTS
        """
        driver = self.driver #Driver reference object created
        visual = Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is)
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_2', 'mrid', 'mrpass')                    
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
                          
        """
        Step02: Click "Change" in the Home Tab > Select "Line chart
        """
        ribbonobj.change_chart_type('line')
        time.sleep(5)
                            
        """
        Step03: Double-click "Cost of Goods" and "Gross Profit"
        Step04: Double-click "Product,Category"
        """        
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
                     
        """
        Step05: Lasso points "Accessories", "Camcorder" and "Computers" in the Line Chart > Select "Filter Chart"
        """        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(4)
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g2!mmarker']")
        visual.create_marker_lasso(source_element, target_element, source_xoffset=-10, source_yoffset=-10, target_xoffset=15, target_yoffset=15)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
                    
        """
        Step06:Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step06:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step06:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers']
        expected_yval_list=['0', '20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'start')         
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g2!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g2!mmarker",bar, msg="Step06: Verify line value",default_move=True)        
           
        """
        Step07: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)                 
                 
        """
        Step08: Hover over blue line value - 'Sony KDL46HX800' > Verify menu
        """ 
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step08:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers']
        expected_yval_list=['0', '20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g2!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g2!mmarker",bar, msg="Step08: Verify line value",default_move=True)        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227603_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
           
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
        Step10: Lasso points "Accessories" and "Camcorder" in the blue Line > Select "Filter Chart"
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 3)
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker!']")
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g1!mmarker!']")
        visual.create_marker_lasso(source_element, target_element, source_xoffset=-10, source_yoffset=-10, target_xoffset=25, target_yoffset=-5)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart') 
        
        """
        Step11: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step11:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder']
        expected_yval_list=['0', '20M','40M','60M','80M','100M','120M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Accessories', 'Gross Profit:$39,854,440.53', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s1!g0!mmarker",bar, msg="Step11: Verify line value",default_move=True)        
        time.sleep(3)
        
        """
        Step12: Click "Accessories" point in the green Line > Select "Filter Chart"
        """
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'middle')
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',0,javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(3)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
        
        """
        Step13: Verify Canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step13:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step13:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories']
        expected_yval_list=['0', '20M','40M','60M','80M','100M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step13:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(5)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker", bar, msg="Step13: Verify line value")
        
        """
        Step14: Right-click "Product,Category" Filter > Select "Delete"
        """
        time.sleep(5)
        metaobj.filter_tree_field_click('Product,Category', 1,1,'Delete')
        
        """
        Step15:Verify Canvas
        """
        time.sleep(5)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step15:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step15:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step15:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker",bar, msg="Step15: Verify line value",default_move=True)        
        time.sleep(3)  
                  
        """
        Step16: Click Save in the toolbar
        Step17: Save as "C2158150" > Click Save
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                  
        """
        Step18: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
                
        """
        Step19: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
                 
        """
        Step20: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Category', "Step20:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step20:a(i) Verify Y-Axis Title")
        expected_xval_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_yval_list=['0', '40M','80M','120M','160M','200M','240M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step20:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker']")
        utillobj.click_on_screen(parent_elem, 'start',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker",bar, msg="Step20: Verify line value",default_move=True)        
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()