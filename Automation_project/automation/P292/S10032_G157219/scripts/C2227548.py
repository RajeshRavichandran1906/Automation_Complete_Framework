'''
Created on 03-Nov-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227548
TestCase Name = Verify Chart with Auto Link, Auto Drill, and Multi Drill using wf_retail_lite 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon, wf_mainpage
from common.lib import utillity  
import time, re
from selenium.webdriver import ActionChains
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2227548_TestClass(BaseTestCase):
    
    def test_C2227548(self):
        
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        main_page=wf_mainpage.Wf_Mainpage(self.driver)
        
        """    1. Reopen fex using IA API:Chart_Source01a.fex using tool=chart    """
        utillobj.infoassist_api_edit("Chart_Source01a", "chart", "S7385")
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#TableChart_1 rect[class^='riser!s0!g0!mbar']")
        resultobj._validate_page(elem1)
        time.sleep(15)
        
        """    2. Select "Format" > "Auto Drill" (from Navigation group)    """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        
        """    3. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        time.sleep(4)
        #utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2068348_Actual_step25', image_type='actual',x=1, y=1, w=-1, h=-1)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 3a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 3b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 3c(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 3d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 3d(ii): Verify Y-Axis Title")
        
        """    4. Hover over on Chart riser "Stereo systems"    """
        """    5. Verify the Autolink,Autodrill and Multidrill menus are displayed    """
        expected_tooltip=['Product Category:Stereo Systems', 'Revenue:$291,294,933.52', 'Drill down to Product Subcategory', 'Drill Down 1', 'Drill Down 2', 'Auto Links']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g4!mbar",expected_tooltip, "Step 5a: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-15)
        
        """    6. Hover over on Chart riser "Media Player",Verify menu    """
        expected_tooltip=['Product Category:Media Player', 'Revenue:$246,073,059.36', 'Drill down to Product Subcategory', 'Drill Down 1', 'Drill Down 2', 'Auto Links']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g3!mbar",expected_tooltip, "Step 6a: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-15)
        
        """    7. Select "Drilldown to Product Subcategory"    """
        time.sleep(4)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g3!mbar", "Drill down to Product Subcategory", wait_time=1, x_offset=x_fr, y_offset=y_fr-15)
        
        """    8. Verify the following "Chart"    """
        time.sleep(1)
        driver.switch_to.default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2227548_Actual_step8', image_type='actual',x=1, y=1, w=-1, h=-1)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 4, 'Step 8a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 8b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 8c(i): Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 8d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 8d(ii): Verify Y-Axis Title")
        
        """    9. Hover over on Chart riser "Blu Ray" > Select "Drill down to Model"    """
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g0!mbar", "Drill down to Model", wait_time=2, x_offset=x_fr, y_offset=y_fr-15)
        
        """    10. Verify the following "Chart"    """
        driver.switch_to.default_content()
        time.sleep(8)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2227548_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 21, 'Step 10a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['JVC XV-BP1', 'JVC XV-BP10', 'JVC XV-BP11', 'Panasonic DMP-BD30', 'Panasonic DMP-BD60', 'Panasonic DMP-BD70V', 'Panasonic DMP-BD80', 'Pioneer BDP-120', 'Pioneer BDP-320', 'Pioneer BDP-330', 'Pioneer BDP-51', 'SAMSUNG BD-C6500', 'SHARP BD-HP70U', 'Samsung BD-C5500', 'Samsung BD-P1600', 'Samsung BD-P3600', 'Sharp BD-HP24U', 'Sony BDP-S360', 'Sony BDP-S370', 'Sony BDP-S470', 'Sony BDP-S570']
        expected_yval_list=['0', '4M', '8M', '12M', '16M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 10b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 10c(i): Verify first bar color")
        xaxis_value="Model"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 10d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 10d(ii): Verify Y-Axis Title")
        
        """    11. Hover over on Chart riser "JVCXV-BP11" > Select "Drill up to Product Subcategory"    """
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g2!mbar", "Drill up to Product Subcategory", wait_time=2, x_offset=x_fr, y_offset=y_fr-15)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 4, 'Step 11a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 11b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 11c(i): Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 11d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 11d(ii): Verify Y-Axis Title")
        
        """    12. Hover over on Chart riser "DVD Players" > Select "Restore Original"    """
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g1!mbar", "Restore Original", wait_time=2, x_offset=x_fr, y_offset=y_fr-15)
        
        """    13. Verify the "Chart" is reverted back to Original stage    """
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 13a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 13b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 13c(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 13d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 13d(ii): Verify Y-Axis Title")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    14. Click IA > "Save"    """
        """    15. Verify the message "Report Saved Successfully" > Click OK    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("Chart_Source01b")
        time.sleep(5)
        
        """    16. Click "Run"    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2227548_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        
        """    17. Verify the Chart and hover on any chart riser verify the menus    """
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 3a: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 3b: X annd Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 3c(i): Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 3d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 3d(ii): Verify Y-Axis Title")
        
        """    18. Close the Chart window    """
        """    19. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


