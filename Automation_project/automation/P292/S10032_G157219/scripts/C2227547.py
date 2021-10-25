'''
Created on 03-Nov-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227547
TestCase Name = Verify Chart with Auto Link and Multi Drill using wf_retail_lite
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2227547_TestClass(BaseTestCase):
    
    def test_C2227547(self):
        
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        #iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        #main_page=wf_mainpage.Wf_Mainpage(self.driver)
        
        """    1. Launch the IA API with WF_RETAIL_LITE, Chart mode:    """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
         
        """    2. Double click "Product,Category","Revenue"    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
         
        """    3. Verify the following Chart in Live Preview    """
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 03a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 03b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 03c(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 03d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 03d(ii): Verify Y-Axis Title")
         
        """    4. Select "Format" > "Enable Auto Linking".    """
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoLinkCluster").value_of_css_property("Visibility") == 'hidden':
            #driver.find_element_by_css_selector("#FormatAutoLinkCluster_altButton img").click()
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoLinkCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
         
        """    5. Click "IA" > "Save" > Enter "Title:" = "Chart_Source01", click "Save".    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("Chart_Source01")
        time.sleep(5)
         
        """    6. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """    7. Launch the IA API with WF_RETAIL_LITE, Chart mode:    """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
         
        """    8. Double click "Product,Category","Gross_Profit"    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(4)
         
        """    9. Drag and drop "Product,Category" into Filter panel    """
        metaobj.datatree_field_click("Product,Category", 1, 1,'Filter')
        time.sleep(1)
         
        """    10. Double click "<Value>", set "Type:" = "Parameter", click "OK" (2x).    """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple')
        time.sleep(10)
         
        """    11. Verify "Filter" is created    """
        metaobj.verify_filter_pane_field('Product,Category Equal to Simple Parameter (Name: PRODUCT_CATEGORY)', 1, "Step 11a")
         
        """    12. Select "Format" > "Auto Link Target".    """
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoLinkCluster").value_of_css_property("Visibility") == 'hidden':
            #driver.find_element_by_css_selector("#FormatAutoLinkCluster_altButton img").click()
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoLinkCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Link_Target")
         
        """    13. Click "IA" > "Save As" > Enter "Title:" = "Chart_Target01", click "Save"    """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("Chart_Target01")
        time.sleep(5)
         
        """    14. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """    15. Reopen fex using IA API:    """        
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit("Chart_Source01", "chart", "S7385")
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
         
        """    16. Click field "Revenue", click "Drill Down" on the Ribbon    """
        metaobj.querytree_field_click("Revenue", 1)
        time.sleep(5)
        elem1=VisualizationRibbonLocators.__dict__["field_drilldown"]
        resultobj._validate_page(elem1)
        time.sleep(5)
        drilldown_btn=driver.find_element(*VisualizationRibbonLocators.__dict__["field_drilldown"])
        utillobj.default_left_click(object_locator=drilldown_btn)
        
        time.sleep(4)
         
        """    17. Click "Web Page" radio button    """
        """    18. Click URL input box -> Type "http://www.ibi.com"    """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.ibi.com')
         
        """    19. Click "Create a new drill down" button    """
        #driver.find_element_by_css_selector("#drillDownNew img").click()
        new_btn=driver.find_element_by_css_selector("#drillDownNew img")
        utillobj.default_left_click(object_locator=new_btn)
        time.sleep(3)
         
        """    20. Click "Web Page" radio button    """
        """    21. Click URL input box -> Type "http://www.bbc.com"    """
        ia_ribbonobj.create_drilldown_report('webpage', url_value='http://www.bbc.com')
          
        """    22. Verify the following drilldown window    """
        ia_ribbonobj.create_drilldown_report('webpage', verify_left_pane=['1', 'Drill Down 1'], msg="Step 22a: Verify Drill Down 1 displayed on left side")
        ia_ribbonobj.create_drilldown_report('webpage', verify_left_pane=['2', 'Drill Down 2'], msg="Step 22b: Verify Drill Down 1 displayed on left side")
         
        """    23. Click OK    """
        ia_ribbonobj.create_drilldown_report('webpage', click_ok="yes")
         
        """    24. Click "IA" > Click Save > Click OK to message    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("Chart_Source01a")
        time.sleep(5)
        
        """    25. Click "IA" > click "Run"    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        '''iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']'''
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2227547_Actual_step25', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.switch_to_frame(pause=1)
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 25a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 25b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 25c(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 25d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 25d(ii): Verify Y-Axis Title")
        
        
        """    26. Hover over on Chart riser "Computers "    """
        """    27. Verify the Autolink and Multidrill menus are displayed    """
        expected_tooltip=['Product Category:Computers', 'Revenue:$103,316,482.12', 'Drill Down 1', 'Drill Down 2', 'Auto Links']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g2!mbar",expected_tooltip, "Step 27a: verify the default tooltip values")
        
        """    28. Hover over "Autolink" > Select "Chart_Target01"    """ #Need more debugging
        time.sleep(5)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g2!mbar", "Auto Links->Chart_Target01", wait_time=1,x_offset_menu=20, y_offset_menu=8)
        #ia_resultobj.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region',x_offset_menu=25, y_offset_menu=5, wait_time=1)
        
        """    29. Verify "Chart_Target01" is displayed in a new window    """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        driver.maximize_window()
        time.sleep(5)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 1, 'Step 29a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Computers']
        expected_yval_list=['0', '5M', '10M', '15M', '20M', '25M', '30M', '35M', '40M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 29b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 29c(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Gross Profit"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 29d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 29d(ii): Verify Y-Axis Title")
        expected_tooltip=['Product Category:Computers', 'Gross Profit:$33,508,818.12']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g0!mbar",expected_tooltip, "Step 29e: verify the default tooltip values")
        
        """    30. Close the window    """
        self.driver.close()
        time.sleep(1)
        window_before = driver.window_handles[0]  # switch back to main window
        driver.switch_to.window(window_before)
        time.sleep(1)
        
        """    31. Select "Camcorder" > Click "Drill down1"    """
        utillobj.switch_to_frame(pause=1)
        time.sleep(3)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g1!mbar", "Drill Down 1", wait_time=1,x_offset_menu=20, y_offset_menu=8)
        
        """    32. Verify it displays a new window going to IBI site    """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        drill1=('Business Intelligence' in driver.title)
        utillobj.asequal(True, drill1, "Step 32a: Verify IBI page is displayed")
        time.sleep(1)
        
        """    33. Close the IBI window    """
        self.driver.close()
        time.sleep(1)
        window_before = driver.window_handles[0]  # switch back to main window
        driver.switch_to.window(window_before)
        time.sleep(1)
        
        """    34. Select "Stereo Systems" > Click "Drill down2"    """
        utillobj.switch_to_frame(pause=1)
        time.sleep(3)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g1!mbar", "Drill Down 2", wait_time=1,x_offset_menu=20, y_offset_menu=8)
        
        """    35. Verify it displays a new window going to "BBC" site.    """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=1)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(1)
        drill2=("BBC" in driver.title)
        utillobj.asequal(True, drill2, "Step 35a: Verify BBC page is displayed")
        time.sleep(1)
        
        """    36. Close the BBC window    """
        self.driver.close()
        time.sleep(1)
        window_before = driver.window_handles[0]  # switch back to main window
        driver.switch_to.window(window_before)
        time.sleep(1)
        
        """    37. Close the "Chart" window    """
        """    38. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


