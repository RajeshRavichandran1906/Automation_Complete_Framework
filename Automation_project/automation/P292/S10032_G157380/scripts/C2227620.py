'''
Created on May 19, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227620
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227620_TestClass(BaseTestCase):
    def test_C2227620(self):
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227620'

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
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        elem1=VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
                          
        """
        Step02: Click "Change" in the Home Tab > Select "Line chart
        """
        ribbonobj.change_chart_type('line')
        time.sleep(5)
                            
        """
        Step03: Double-click "Cost of Goods" and "Gross Profit"
        Step04: Double-click "Product,Subcategory"
        """        
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        time.sleep(5)
                     
        """
        Step05: Lasso values from "DVD Players - Portable" to "Portable TV"
        """        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 21)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g5!mmarker']")
        coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        sx=coord['x']-10
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g6!mmarker']")
        coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        sy=coord['y']-40
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g10!mmarker']")
        coord=utillobj.enable_marker_using_javascript(parent_elem, 'middle')
        tx=coord['x']+10
        ty=coord['y']+40
        time.sleep(2)
        utillobj.drag_drop_on_screen(sx_offset=sx,sy_offset=sy,tx_offset=tx,ty_offset=ty)
#         utillobj.drag_drop_on_screen(sx_offset=par_cord['x']+329,sy_offset=par_cord['y']+362,tx_offset=par_cord['x']+683,ty_offset=par_cord['y']+572)
        time.sleep(3)
                         
        """
        Step06:Select "Filter Chart" (12 points)
        """
        time.sleep(2)
        resultobj.select_or_verify_lasso_filter(select='Filter Chart')
                    
        """
        Step07:Verify Preview
        Step08:Hover over blue line (for 'Cost of Goods') - value 'Flat Panel TV' > Verify menu
        """
#         utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
               
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 6)
                  
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step07:a(i) Verify Y-Axis Title")
        expected_xval_list=['DVD Players - Portable','Flat Panel TV','Handheld','Headphones','Home Theater Systems','Portable TV']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
                  
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g1!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Product Subcategory:Flat Panel TV', 'Cost of Goods:$59,077,345.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g1!mmarker",bar, msg="Step08: Verify line value",default_move=True)        
            
        """
        Step09: Select "Drill down to Model" > Verify Preview
        """
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s1!g1!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "marker!s1!g1!mmarker",'Drill down to Model',wait_time=1,default_move=True)
        
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
                    
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Model', "Step09:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step09:a(i) Verify Y-Axis Title")
        expected_xval_list=['LG 19LE5300 19','LG 32LE5300 32','Panasonic 58TV25BNDL','Panasonic TCP46G25','Sony KDL32EX400','Sony KDL46HX800','Sony KDL60EX800']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step09:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g5!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Model:Sony KDL46HX800', 'Cost of Goods:$11,445,420.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g5!mmarker", bar, msg="Step09: Verify line value",default_move=True)
#         utillobj.infoassist_api_edit('cv20','idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')  
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
        """
        Step10: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        #time.sleep(15)                  
                
        """
        Step11: Hover over blue line value - 'Sony KDL46HX800' > Verify menu
        """
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(5)
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)
                  
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Model', "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step11:a(i) Verify Y-Axis Title")
        expected_xval_list=['LG 19LE5300 19', 'LG 32LE5300 32', 'Panasonic 58TV25BNDL', 'Panasonic TCP46G25', 'Sony KDL32EX400', 'Sony KDL46HX800', 'Sony KDL60EX500']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step11:a(iii):Verify XY labels",x_custom_css="text[class*='xaxisOrdinal-labels']")
        time.sleep(5)   
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'middle')
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g5!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5,x_offset=10,y_offset=20)
        time.sleep(1)
        bar=['Model:Sony KDL46HX800', 'Cost of Goods:$11,445,420.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g5!mmarker", bar, msg="Step11: Verify line value",default_move=True)
             
        """
        Step12: Select "Drill up to Product Subcategory"
        Step13: Verify output and pop up menu
        """ 
        time.sleep(5)   
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(parent_elem, 'middle')
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g5!mmarker']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "marker!s0!g5!mmarker",'Drill up to Product Subcategory',default_move=True)
              
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 1)
                  
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Product Subcategory', "Step12:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step12:a(i) Verify Y-Axis Title")
        expected_xval_list=['Flat Panel TV']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M','60M','70M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("[class*='eventPanel']")
        utillobj.click_on_screen(parent_elem, 'middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g0!mmarker!']")
        utillobj.click_on_screen(parent_elem, 'middle',javascript_marker_enable = True,mouse_duration=2.5)    
        bar=['Product Subcategory:Flat Panel TV', 'Cost of Goods:$59,077,345.00', 'Drill up to Product Category', 'Drill down to Model']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g0!mmarker!", bar, msg="Step13: Verify line value",default_move=True)
              
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227620_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
                    
        """
        Step14: Click Save in the toolbar
        Step15: Save as "C2158150" > Click Save
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
        Step16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
                 
        """
        Step17: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
                 
        """
        Step18: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 7)    
        time.sleep(5)
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", 'Model', "Step18:a(i) Verify X-Axis Title")
        resultobj.verify_riser_legends("MAINTABLE_wbody1", ['Cost of Goods','Gross Profit'], "Step18:a(i) Verify Y-Axis Title")
        expected_xval_list=['LG 19LE5300 19','LG 32LE5300 32','Panasonic 58TV25BNDL','Panasonic TCP46G25','Sony KDL32EX400','Sony KDL46HX800','Sony KDL60EX800']
        expected_yval_list=['0', '3M', '6M', '9M', '12M', '15M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step18:a(iii):Verify XY labels",x_custom_css="text[class^='xaxisOrdinal-labels']")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='marker!s0!g5!mmarker']")
        utillobj.click_on_screen(parent_elem, 'start',javascript_marker_enable=True,mouse_duration=2.5)
        time.sleep(1)
        bar=['Model:Sony KDL46HX800', 'Cost of Goods:$11,445,420.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Subcategory']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "marker!s0!g5!mmarker", bar, msg="Step18: Verify line value",default_move=True)
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()