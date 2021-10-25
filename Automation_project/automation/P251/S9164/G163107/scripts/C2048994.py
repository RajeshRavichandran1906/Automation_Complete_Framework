'''
Created date 19.12.2016 

@author: Nasir

http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2048994
Suite : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7086
'''

import unittest,time, pyautogui
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2048994_TestClass(BaseTestCase):
    
    def test_C2048994(self):
        
        Test_Case_ID = "C2048994"
        driver = self.driver
        driver.implicitly_wait(35)#Default sticky timeout for driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        browser=utillobj.parseinitfile('browser') 
        
        """Step 01: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S7086', mrid='mrid', mrpass='mrpass')#application will login with fex
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 02: Verify the following chart is displayed."""
        time.sleep(5)     
        ele=driver.find_element_by_css_selector("#resultArea")
        #utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step02', image_type='actual')  
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step2_"+ browser +".png","step2:verification")
        time.sleep(3)
        
        """Step 03: Drag Gross Profit to Open bucket."""
        metaobj.drag_drop_data_tree_items_to_query_tree("Gross Profit", 1, "Open", 0)
        time.sleep(4)
        
        """Step 04: Drag MSRP to High bucket."""
        if browser == 'IE':
            element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
            element.clear()
            time.sleep(3)
            element.click()
            time.sleep(5)
            pyautogui.typewrite("MSRP", interval=0.2)
            #element.send_keys('CO')
            time.sleep(3)
            utillobj.drag_drop_using_Sikuli('MSRP_IE', 'High_IE')
        else:
            metaobj.drag_drop_data_tree_items_to_query_tree("MSRP", 1, "High", 0)
        time.sleep(4)
        
        """Step 05: Drag Discount to Low bucket."""
        metaobj.drag_drop_data_tree_items_to_query_tree("Discount", 1, "Low", 0)
        time.sleep(4)
        
        """Step 06: Drag Cost of Goods to Close bucket."""
        metaobj.drag_drop_data_tree_items_to_query_tree("Cost of Goods", 1, "Close", 0)
        time.sleep(4)
        
        """Step 07: Drag Sale,Month to X Axis bucket."""
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Month", 1, "X Axis", 0)
        time.sleep(4)
        
        """Step 08: Verify the following chart is displayed."""        
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        #utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step08', image_type='actual',x=1, y=1, w=-1, h=-1)  
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step8_"+ browser +".png","step8:verification")
        time.sleep(3)
        
        """Step 09: Click "Run"."""
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        
        """Step 10: Verify the following chart is displayed."""     
        ele=driver.find_element_by_css_selector("#resultArea")
        #utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step10_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)#browser variation snapshot
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step10_"+ browser +".png","step10:verification") 
        
        """Step 11: Click "IA" > "Save"."""
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID + "_" + browser)
        time.sleep(5)
        
        """Step 12: Close the IA window.""" 
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """Step 13: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS6940Chart_Type_PDF_Charts_Part_1_Test_Suite_%2FC2048426.fex&tool=chart"""
        utillobj.infoassist_api_edit(Test_Case_ID + "_" + browser, 'chart', 'S7086', mrid='mrid', mrpass='mrpass')#application will login with fex
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """Step 14: Verify the following chart is displayed."""
        """Step 15: Close IA."""
        time.sleep(3)     
        ele=driver.find_element_by_css_selector("[id^='LayoutChartObjectDrawLayer']")
        #utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step14', image_type='actual',x=1, y=1, w=-1, h=-1)  
        utillobj.verify_picture_using_sikuli(Test_Case_ID + "_step14_"+ browser +".png","step14:verification")
        time.sleep(3)
        
if __name__=='__main__':
    unittest.main()
        
        
        
        