'''
Created on Dec 20, 2016

@author: Magesh

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2047936
Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/6940
Verify Bubble Chart is working properly
'''

from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from selenium.webdriver import ActionChains
import unittest, time
from selenium import webdriver
from common.lib.utillity import UtillityMethods
from common.lib import utillity
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import pyautogui
from pynput.mouse import Button, Controller

class C2047936_TestClass(BaseTestCase):
    
    def test_C2047936(self):
        
        Test_Case_ID = "C2047936"
        
        driver = self.driver
        driver.implicitly_wait(40)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_styobj = ia_styling.IA_Style(self.driver)
        
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2047936.fex&tool=chart"""
        
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')#application will login with fex
        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step02: Select "Format" > "Chart Types" > "Other".
        Step03: Select "X Y Plots" > "Bubble Chart" > "OK".
        """
        time.sleep(5)  
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('x_y_plots', 'x_y_plots_bubble', 3, ok_btn_click=True)
        
        
        """Step 04: Double click "Revenue". """
        
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
       
        
        """Step 05: Drag and drop "Cost of Goods" over "Measure (Sum)"."""
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Cost of Goods', 1, 'Measure (Sum)',0)
        time.sleep(4)
        
        
        """step 06: Drag and drop "Sale,Month" over "Size"."""
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Sale,Month', 1, 'Size',0)
        time.sleep(4)
        
        """step 07: Right click "Product,Category" under "Legend" > Delete."""
        
        time.sleep(4)
        metaobj.querytree_field_click("Product,Category",1,1,"Delete")
        
        """Step 08: Verify the following chart is displayed."""
        
        time.sleep(10)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step08', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
        """Step 09: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        
        """Step 10: Verify the following chart is displayed."""
        
        browser=utillobj.parseinitfile('browser')  
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step10_"+ browser +".png" , "Step10 verification")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step10_'+browser+'', image_type='actual',x=1, y=1, w=-1, h=-1)#browser variation snapshot  
        
        
        """Step 11: Click "IA" > "Save"."""

        """Step 12: Close the IA window.""" 
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID+"_"+browser)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """Step 13: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2047936.fex&tool=chart"""
        
        
        utillobj.infoassist_api_edit(Test_Case_ID+"_"+browser, 'chart', 'S6940', mrid='mrid', mrpass='mrpass')#application will login with fex
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 14: Verify the following chart is displayed."""
        
        time.sleep(3)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step14', image_type='actual',x=1, y=1, w=-1, h=-1)  
        time.sleep(3)
        
        """ Step15: Close IA."""
#         utillobj.infoassist_api_logout()
#         time.sleep(1)
        
if __name__=='__main__':
    unittest.main()