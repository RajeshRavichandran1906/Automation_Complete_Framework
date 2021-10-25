'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226981
TestCase Name = Test drilling all the way down and up a long hierarchy path - HTML5
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity  
import time, pyautogui
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226981_TestClass(BaseTestCase):
    def test_C2226981(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2226981_"+browser_type
        driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        elem = "#jschart_HOLD_0 span>a[href*='contentDrill']"
        
        """    1. Open IA_Chart for edit using the API 
        http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Chart.fex&tool=Chart    """
        utillobj.infoassist_api_edit("IA-Chart", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(45)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(35)
        
        """    2. Click Format tab > Autodrill button    """
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoDrillCluster").value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    3. Hover over the Auto Drill button and verify the tool tip appears    """
        expected_tooltip="Enable Auto Drill. This functionality requires at least one dimension sort field to be present in the request."
        pyautogui.moveTo(10,10)
        ribbon_item=driver.find_element_by_css_selector("#FormatAutoDrill img")
        x_fr=ribbon_item.location['x']
        y_fr=ribbon_item.location['y']
        w_fr=ribbon_item.size['width']
        h_fr=ribbon_item.size['height']
        pyautogui.moveTo(x_fr + (w_fr/2), y_fr + (h_fr/2) + 80)
        time.sleep(3)
        actual_tooltip=driver.find_element_by_css_selector("div[id^='BiToolTip-']").text.strip()
        utillobj.asequal(expected_tooltip, actual_tooltip, "Step 03: Verify the tooltip appears")
        print(actual_tooltip)
        time.sleep(3)
        
        """    4. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(4)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2226981_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 4a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 139, 'Step 4b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 4c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mbar!r0!c0!", "bar_green", "Step 4c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mbar!r0!c1!", "med_green", "Step 4c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g1!mbar!r0!c1!", "pale_yellow_2", "Step 4c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g1!mbar!r0!c0!", "brick_red", "Step 4c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s5!g0!mbar!r0!c1!", "light_brick", "Step 4c(6): Verify sixth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 4d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 4d(ii): Verify Y-Axis Title")
        time.sleep(8)
          
        """    5. Hover over the top bar (2016) in North America/Stereo Systems. Then hover over the Drill down to and select Store Business Sub Region.    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region')
        ##iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        a =['Store Business Sub Region:Midwest', 'Product Category:Stereo Systems', 'Revenue:$6,990,028.64', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Business Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c3!',a,"Step 05a: Verify Midwest tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 8, "Step 05b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 05c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 05d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 05e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c5!", "bar_blue1", "Step 05f: Verify bar color") 
        time.sleep(3)
        
        """    6. Hover over West and drill down to Store Country    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Store Country')
        #iaresult.select_autolink_tooltip_menu_with_offset('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Store Country')
        #iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Store Country',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Store Country',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10, action_x_offset=10, action_y_offset=200)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(8)
        a =['Store Country:United States', 'Product Category:Stereo Systems', 'Revenue:$52,755,657.68', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c0!',a,"Step 06a: Verify United States tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 1, "Step 06b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 06c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 06d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 06e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 06f: Verify bar color") 
        time.sleep(3)
        
        """    7. Hover over United States and drill down to Store State Province    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill down to->Store State Province')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill down to->Store State Province',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        time.sleep(8)
        a =['Store State Province:Idaho', 'Product Category:Stereo Systems', 'Revenue:$47,337,478.20', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Country', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c4!',a,"Step 07a: Verify Idaho tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 9, "Step 07b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 07c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 07d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 07e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c4!", "bar_blue1", "Step 07f: Verify bar color") 
        time.sleep(3)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2229681_Actual_step7', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(4)
        
        """    8. Hover over California and drill down to Store City    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c1!', 'Drill down to->Store City')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c1!', 'Drill down to->Store City',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 4)
        time.sleep(8)
        a =['Store City:Los Angeles', 'Product Category:Stereo Systems', 'Revenue:$663,518.81', 'Sale Year:2016', 'Restore Original', 'Drill up to Store State Province', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c0!',a,"Step 08a: Verify Los Angeles tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 3, "Step 08b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 08c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 08d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 08e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c1!", "bar_blue1", "Step 08f: Verify bar color") 
        time.sleep(3)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2229681_Actual_step8', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(4)
        
        """    9. Hover over San Diego and drill down to Store Postal Code    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c1!', 'Drill down to->Store Postal Code')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c1!', 'Drill down to->Store Postal Code',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 5)
        time.sleep(8)
        a =['Store Postal Code:92101', 'Product Category:Stereo Systems', 'Revenue:$810,080.63', 'Sale Year:2016', 'Restore Original', 'Drill up to Store City', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c0!',a,"Step 09a: Verify 92101 tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 1, "Step 09b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 09c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 09d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 09e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 09f: Verify bar color") 
        time.sleep(3)
        
        """    10. Hover over 92101 and drill down to Store Name    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill down to->Store Name')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill down to->Store Name',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 6)
        time.sleep(8)
        a =['Store Name:San Diego','Product Category:Stereo Systems', 'Revenue:$810,080.63', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Postal Code', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c0!',a,"Step 10a: Verify San Diego tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 1, "Step 10b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 10c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 10d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 10e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 10f: Verify bar color") 
        time.sleep(3)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2229681_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(4)
        
        """    11. Hover over San Diego and select Drill up to Store Postal Code    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store Postal Code')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store Postal Code',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 5)
        time.sleep(8)
        a =['Store Postal Code:92101', 'Product Category:Stereo Systems', 'Revenue:$810,080.63', 'Sale Year:2016', 'Restore Original', 'Drill up to Store City', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c0!',a,"Step 11a: Verify 92101 tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 1, "Step 11b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 11c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 11d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 11e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 11f: Verify bar color") 
        time.sleep(3)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2229681_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(4)
        
        """    12. Hover over 92101 and select Drill up to Store City    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store City')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store City',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 4)
        time.sleep(8)
        a =['Store City:Los Angeles', 'Product Category:Stereo Systems', 'Revenue:$663,518.81', 'Sale Year:2016', 'Restore Original', 'Drill up to Store State Province', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c0!',a,"Step 12a: Verify Los Angeles tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 3, "Step 12b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 12c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 12d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 12e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c1!", "bar_blue1", "Step 12f: Verify bar color") 
        time.sleep(3)
        
        """    13. Hover over San Diego and select Drill up to Store State Province    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c1!', 'Drill up to Store State Province')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c1!', 'Drill up to Store State Province',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        time.sleep(8)
        a =['Store State Province:Idaho', 'Product Category:Stereo Systems', 'Revenue:$47,337,478.20', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Country', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c4!',a,"Step 13a: Verify Idaho tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 9, "Step 13b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 13c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 13d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 13e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c4!", "bar_blue1", "Step 13f: Verify bar color") 
        time.sleep(3)
        
        """    14. Hover over California and select Drill up to Store Country    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c1!', 'Drill up to Store Country')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c1!', 'Drill up to Store Country',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(8)
        a =['Store Country:United States', 'Product Category:Stereo Systems', 'Revenue:$52,755,657.68', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Business Sub Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c0!',a,"Step 14a: Verify United States tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 1, "Step 14b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 14c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 14d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 14e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 14f: Verify bar color") 
        time.sleep(3)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2229681_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(4)
        
        """    15. Hover over United States and select Drill up to Store Business Sub Region    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store Business Sub Region')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c0!', 'Drill up to Store Business Sub Region',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        a =['Store Business Sub Region:Midwest', 'Product Category:Stereo Systems', 'Revenue:$6,990,028.64', 'Sale Year:2016', 'Restore Original', 'Drill up to Store Business Region', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c3!',a,"Step 15a: Verify Midwest tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 8, "Step 15b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 15c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 15d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 15e: ')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c5!", "bar_blue1", "Step 15f: Verify bar color") 
        time.sleep(3)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2229681_Actual_step15', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(4)
        
        """    16. Hover over West and select Drill up to Store Business Region    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill up to Store Business Region')
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill up to Store Business Region',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10,action_x_offset=10, action_y_offset=200)
        time.sleep(8)
        elem1 = "#jschart_HOLD_0 g.chartPanel rect[class^='riser!s']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem1)) == 139)
        time.sleep(8)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 16a:')
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 139, 'Step 16b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 16c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mbar!r0!c0!", "bar_green", "Step 16c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mbar!r0!c1!", "med_green", "Step 16c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g1!mbar!r0!c1!", "pale_yellow_2", "Step 16c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g1!mbar!r0!c0!", "brick_red", "Step 16c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s5!g0!mbar!r0!c1!", "light_brick", "Step 16c(6): Verify sixth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 16d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 16d(ii): Verify Y-Axis Title")
        time.sleep(8)
        utillobj.switch_to_default_content()
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2229681_Actual_step16', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        
        """    17. Click IA > Save As > Type C2226981 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    18. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226981.fex&tool=Chart    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    19. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 19a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
         
        """    20. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
