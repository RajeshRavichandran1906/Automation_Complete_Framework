'''
Created on 07-Nov-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227563
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227563_TestClass(BaseTestCase):

    def test_C2227563(self):
        
        Test_Case_ID = "C2227563"
        driver = self.driver
        driver.implicitly_wait(20)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
                
        """
        1. Launch the IA API with CAR, Chart mode:
        http://machine:port/ibi_apps/ia?tool=chart&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F
        """
        utillobj.infoassist_api_login('chart','ibisamp/CAR','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        
        """
        2. Double click "Country", "Dealer_cost"
        """
        time.sleep(4) 
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        
        """
        3. Verify the following Chart in Live preview
        """
        resultobj.verify_number_of_riser("TableChart_1", 1, 5, 'Step 03a: Verify 5 risers displayed on Run Chart')
        expected_xval_list=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        expected_yval_list=['0', '10K', '20K','30K','40K','50K','60K']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03b: X annd Y axis Scale Values')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 03c(i): Verify first bar color")
        xaxis_value="COUNTRY"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03d(i): Verify X-Axis Title COUNTRY")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03d(ii): Verify Y-Axis Title DEALER_COST") 
        
        """
        4. Click "IA" > "Save" > Enter title= "Chart002" > Click "Save".
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("C2227563_Chart002")
        time.sleep(5)
        
        """
        5. Logout:
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        6. Launch the IA API with WF_RETAIL_LITE, Report mode:
        http://machine:port/ibi_apps/ia?tool=report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F
        """
        utillobj.infoassist_api_login('report','new_retail/WF_RETAIL_LITE','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        7. Double-click "Revenue" under Sales Measures
        """
        time.sleep(4) 
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4) 
        
        """
        8: Double-click "Product,Category" under Product Dimension.
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4) 
        
        """
        9. Verify the following "Report" in Livepreview
        """
        ia_resultobj.verify_report_data_set('TableChart_1', 5,2, 'C2227563_Preview.xlsx',"Step 09: Verify report data set",no_of_cells=4)  
        
        """
        10: Select "Format" > "Auto Drill" button (from navigation group)
        """
        ribbonobj.select_ribbon_item('Format', 'Auto_Drill') 
        
        """
        11. Select "Product,Category" in Query pane
        12. Click "Links" > "Drill down" from "Field" tab.
        """
        metaobj.querytree_field_click("Product,Category", 1, 1,"Drill Down")
        time.sleep(5)
        
        """
        13. On "Drill Down" window, Verify "Report" is enabled by default
        14. Click "Browse" > Select "Chart002" > Open.
        """
        default=self.driver.find_element_by_css_selector("#rBtnProc input").get_attribute("checked")
        utillobj.asequal(default,"true","Step 13: Verify Report is enabled by default")
        time.sleep(2)
        ia_ribbonobj.create_drilldown_report('report',browse_file_name='C2227563_Chart002')
        time.sleep(2)
        
        """
        15. Set "Description" = "Drilldown to Chart".
        16. Tab out of the textfield
        """
        ia_ribbonobj.create_drilldown_report('report',set_description='Drilldown to Chart')
        time.sleep(2)
        
        """
        16. Tab out of the textfield
        ""
        action=ActionChains(self.driver)
        action.send_keys(keys.Keys.TAB).perform()
        del action
        time.sleep(2)"""
        
        """
        17. Verify "Drilldown to Chart" is showing on the left frame
        """
        ia_ribbonobj.create_drilldown_report('report', verify_left_pane=['1','Drilldown to Chart'], msg="Step 17: Verify Drilldown to Chart displayed on left side")
        time.sleep(2)
        
        """
        18. Click "Create a new drill down" icon
        """
        #driver.find_element_by_css_selector("#drillDownNew img").click()
        new_btn=driver.find_element_by_css_selector("#drillDownNew img")
        utillobj.default_left_click(object_locator=new_btn)
        time.sleep(3)
        
        """
        19. Click "Web Page" option, click URL input box
        20. Type "http://www.msn.com"
        """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.msn.com')
        
        """
        21. Set "Description" = "MSN". 
        21. Tab out of the textfield       
        """
        ia_ribbonobj.create_drilldown_report('webpage',set_description='MSN')
        time.sleep(2)
        
        """
        22. Tab out of the textfield
        ""
        action=ActionChains(self.driver)
        action.send_keys(keys.Keys.TAB).perform()
        del action
        time.sleep(2)"""
        
        """
        23. Verify "MSN" is showing on the left frame.
        """
        ia_ribbonobj.create_drilldown_report('webpage', verify_left_pane=['2','MSN'], msg="Step 23: Verify MSN displayed on left side")
        time.sleep(2)
        
        """
        24: Click "Create a new drill down" icon
        """
        new_btn=driver.find_element_by_css_selector("#drillDownNew img")
        utillobj.default_left_click(object_locator=new_btn)
        #driver.find_element_by_css_selector("#drillDownNew img").click()
        time.sleep(3)
        
        """
        25. Click "Web Page" option, click URL input box
        26. Type "http://www.yahoo.com"
        """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.yahoo.com')
        
        """
        27. Set "Description" = "Yahoo".
        28. Tab out of the textfield
        """
        ia_ribbonobj.create_drilldown_report('webpage',set_description='Yahoo')
        time.sleep(2)
        
        
        """
        28. Tab out of the textfield
        ""
        action=ActionChains(self.driver)
        action.send_keys(keys.Keys.TAB).perform()
        del action
        time.sleep(2)"""
        
        """
        29. Verify the following drilldown window
        """
        ia_ribbonobj.create_drilldown_report('webpage', verify_left_pane=['3','Yahoo'], msg="Step 29: Verify Yahoo displayed on left side")
        time.sleep(2)
        
        """
        30. Click "OK"
        """
        ia_ribbonobj.create_drilldown_report('webpage', click_ok="yes")
        time.sleep(5)
        
        """
        31. Verify Report preview with hyperlinks
        """
        ia_resultobj.verify_autolink("TableChart_1","Accessories",7,"Step 31: Verify Auto Drill applied in Accessories") 
        
        """
        32: Click Run"
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        '''iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']'''
        
        """
        33: Click value "Computers", Verify the Autodrill and Multidrill menus are displayed
        """
        utillobj.switch_to_frame()
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe"]')))
        time.sleep(3)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        a=['Drill down to Product Subcategory', 'Drilldown to Chart', 'MSN', 'Yahoo']
        #iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,1,a, "Step 33: Verify the Auto Drill menu for Computers",browser_height=80, x_offset=x_fr, y_offset=y_fr+5)
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,1,a, "Step 33: Verify the Auto Drill menu for Computers")
        time.sleep(5) 
        
        """
        34: Select "Drill Down to Product Subcategory", Verify Report
        """        
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drill down to Product Subcategory', "Step 34.1: Select the Auto Drill menu, Drill down to Product Subcategory", browser_height=80, x_offset=x_fr, y_offset=y_fr+5)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drill down to Product Subcategory', "Step 34.1: Select the Auto Drill menu, Drill down to Product Subcategory")
        time.sleep(3)
        iarun.verify_autolink("table[summary='Summary']","Smartphone",4,1,3,"Step 34.2: Verify Auto Drill applied in value Smartphone")
        time.sleep(2)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227563_Ds01.xlsx", "Step 34.3: verify Auto Drill, drill down to Product Subcategory data set")
        
        """
        35: Click "Smartphone" , Verify menus
        """        
        time.sleep(2)
        a=['Restore Original', 'Drill up to Product Category', 'Drill down to Model', 'Drilldown to Chart', 'MSN', 'Yahoo']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,1,a, "Step 35: Verify the Auto Drill menu for Smartphone")
        #iarun.verify_autolink_tooltip_values("table[summary='Summary']",4,1,a, "Step 35: Verify the Auto Drill menu for Smartphone", browser_height=80, x_offset=x_fr, y_offset=y_fr+5)
        time.sleep(5)
        
        """
        36: Click "Drilldown to Chart"
        37: Verify drilldown to chart is working properly and it opens in a new window
        """
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drilldown to Chart', "Step 36.1: Select the Auto Drill menu, Drilldown to Chart")
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Drilldown to Chart', "Step 36.1: Select the Auto Drill menu, Drilldown to Chart", browser_height=80, x_offset=x_fr, y_offset=y_fr+5)
        time.sleep(8)
        utillobj.switch_to_default_content(pause=2)
        utillobj.switch_to_window(1) #to switch to run window
        time.sleep(8)
        driver.maximize_window()
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#jschart_HOLD_0")
        resultobj._validate_page(elem1)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#jschart_HOLD_0"),'C2227563_Base_step37', image_type='base',x=1, y=1, w=-1, h=-1)
        
        time.sleep(5)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 5, 'Step 37.1: Verify 5 risers displayed on Run Chart')
        time.sleep(1)
        expected_xval_list=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        expected_yval_list=['0', '10K', '20K','30K','40K','50K','60K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 37.2: X annd Y axis Scale Values')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar", "bar_blue1", "Step 03c(i): Verify first bar color")
        xaxis_value="COUNTRY"
        yaxis_value="DEALER_COST"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 37.3(i): Verify X-Axis Title COUNTRY")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 37.3(ii): Verify Y-Axis Title DEALER_COST")
        
        """
        38. Close the Chart window
        """
        self.driver.close()
        utillobj.switch_to_window(0) # switch back to main window
        
        """
        39: Click "Tablet" > Select "drill down to Model"
        """
        utillobj.switch_to_frame()
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        time.sleep(3)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(5)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",5,1,'Drill down to Model', "Step 36.1: Select the Auto Drill menu, Drill down to Model")
        time.sleep(5)
        
        """
        40. Verify the Report , Click "GLXYT70" > Click MSN
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227563_Ds02.xlsx", "Step 40.1: verify Auto Drill, Drill down to Model data set")
        time.sleep(2)
        iarun.verify_autolink("table[summary='Summary']","GLXYT70",8,1,12,"Step 40.2: Verify Auto Drill applied in value GLXYT70")
        time.sleep(5)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",8,1,'MSN', "Step 40.3: Select the Auto Drill menu, MSN")
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",8,1,'MSN', "Step 40.3: Select the Auto Drill menu, MSN", browser_height=80, x_offset=x_fr, y_offset=y_fr+5)
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        
        """
        41. Verify it displays a new window going to MSN site.
        42. Close the MSN window
        """
        time.sleep(10)
        utillobj.switch_to_window(1) #to switch to run window
        time.sleep(5)
        drill2=(driver.title=='MSN.com - Hotmail, Outlook, Skype, Bing, Latest News, Photos & Videos')
        utillobj.asequal(True, drill2, "Step 42: Verify MSN page is displayed")
        self.driver.close()
        utillobj.switch_to_window(0) # switch back to main window
        
        """
        43. Click "SGPT122US/S" > Click "Drill up to Product Subcategory"
        """
        utillobj.switch_to_frame()
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        time.sleep(3)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(5)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",12,1,'Drill up to Product Subcategory', "Step 43: Select the Auto Drill menu, Drill up to Product Subcategory")
        time.sleep(5)
        
        """
        44: Verify Report, Click Smartphone > Select "Restore Original"
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227563_Ds01.xlsx", "Step 44.1: verify Auto Drill, Drill up to Product Subcategory data set")
        time.sleep(2)
        iarun.verify_autolink("table[summary='Summary']","Smartphone",4,1,3,"Step 44.2: Verify Auto Drill applied in value Smartphone")
        time.sleep(3)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Restore Original', "Step 40.3: Select the Auto Drill menu, Restore Original")
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",4,1,'Restore Original', "Step 40.3: Select the Auto Drill menu, Restore Original", browser_height=80, x_offset=x_fr, y_offset=y_fr+5)
        time.sleep(5)
        
        """
        45. Verify the Report > Click "Televisions" > Click "Yahoo"
        """
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227563_Ds04.xlsx", "Step 45.1: verify Auto Drill, Restore Original data set")
        time.sleep(3)
        iarun.verify_autolink("table[summary='Summary']","Televisions",7,1,7,"Step 45.2: Verify Auto Drill applied in value Televisions")
        time.sleep(3)
        iarun.select_autolink_tooltip_menu("table[summary='Summary']",7,1,'Yahoo', "Step 45.3: Select the Auto Drill menu, Yahoo")
        #iarun.select_autolink_tooltip_menu("table[summary='Summary']",7,1,'Yahoo', "Step 45.3: Select the Auto Drill menu, Yahoo", browser_height=80, x_offset=x_fr, y_offset=y_fr+5)
        time.sleep(5)
        #driver.switch_to.default_content()
        utillobj.switch_to_default_content(pause=2)
        time.sleep(2)
        """
        46. Verify it displays a new window going to Yahoo site.
        47. Close the window
        """
        time.sleep(10)
        utillobj.switch_to_window(1) #to switch to run window
        time.sleep(5)
        drill2=("Yahoo" in driver.title)
        utillobj.asequal(True, drill2, "Step 46: Verify Yahoo page is displayed")
        self.driver.close()
        utillobj.switch_to_window(0) # switch back to main window
        
        """
        48. Click "IA" > "Save" > Enter Title = "C2227563" > Save
        """
        driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)        
        
        """
        49: Logout:
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """
        50. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227563.fex&tool=report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        51. Verify Preview
        """
        ia_resultobj.verify_report_data_set('TableChart_1', 5,2, 'C2227563_Preview.xlsx',"Step 51: Verify report data set",no_of_cells=4) 
        
        """
        52. Logout:
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        

if __name__ == "__main__":
    unittest.main()
        
        
        
        
                  
    