'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226978
TestCase Name = Test that a non-hierarchy field used as a sorting field will not be active for Drill down
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226978_TestClass(BaseTestCase):
    def test_C2226978(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2226978_"+browser_type
        driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        #browser=utillobj.parseinitfile("browser")

        """    1. Open IA_Chart for edit using the API 
        http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Chart.fex&tool=Chart    """
        utillobj.infoassist_api_edit("IA-Chart", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Drag Brand Type (Product > Product > Model > Attributes > Brand Type) and place over the Product,Category in Horizontal axis bucket    """
        metaobj.querytree_field_click('Product,Category', 1, 1, "Delete")
        time.sleep(2)
        metaobj.drag_drop_data_tree_items_to_query_tree('Brand Type',1,'Horizontal Axis',0)
        #metaobj.datatree_field_click('Brand Type', 2, 1)
        time.sleep(8)
        """    Workaround for replace the field on query tree
        metaobj.replace_query_tree_item_with_data_tree_item('Brand Type', 1, 'Product,Category',0) """
        
        """    3. Click Format tab > Autodrill button    """
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoDrillCluster").value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(10)
         
        """    4. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        utillobj.switch_to_default_content(1)        
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2226978_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        expected_xval_list=['Major Brand', 'Specialty Brand', 'Major Brand', 'Specialty Brand', 'Major Brand', 'Specialty Brand','Major Brand', 'Specialty Brand']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M', '500M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 4a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 40, 'Step 4b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 4c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mbar!r0!c0!", "bar_green", "Step 4c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g0!mbar!r0!c1!", "med_green", "Step 4c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g1!mbar!r0!c1!", "pale_yellow_2", "Step 4c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g1!mbar!r0!c0!", "brick_red", "Step 4c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s5!g0!mbar!r0!c1!", "light_brick", "Step 4c(6): Verify sixth segment in the bar color")
        xaxis_value="Brand Type"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 4d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 4d(ii): Verify Y-Axis Title")
        time.sleep(8)
        
                
        """    5. HHover over any bar and then on "Drill down to".    """
        a =['Store Business Sub Region', 'Sale Year/Quarter']
        iaresult.verify_autolink_tooltip_submenu('jschart_HOLD_0','riser!s5!g0!mbar!r0!c0!', "Drill down to", a, "Step 05a: Verify the drill menu shows for only Region and Year.", x_offset_menu1=20, y_offset_menu1=8)
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        #driver.switch_to.default_content()
        time.sleep(4)
        
        """    6. Click IA > Save As > Type C2226978a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID+"a")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    7. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226978a.fex&tool=Chart    """
        utillobj.infoassist_api_edit(Test_Case_ID+"a", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    8. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 08a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
         
        """    9. Click on HTML5 output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
         
        """    10. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2226978_Actual_step10', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        expected_xval_list=['Major Brand', 'Specialty Brand', 'Major Brand', 'Specialty Brand', 'Major Brand', 'Specialty Brand','Major Brand', 'Specialty Brand']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M', '500M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 10a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 40, 'Step 10b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 10c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g1!mbar!r0!c0!", "pale_green", "Step 10c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g0!mbar!r0!c1!", "dark_green", "Step 10c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g1!mbar!r0!c1!", "pale_yellow", "Step 10c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s4!g1!mbar!r0!c0!", "brick_red", "Step 10c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s5!g0!mbar!r0!c1!", "orange", "Step 10c(6): Verify sixth segment in the bar color")
        xaxis_value="Brand Type"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 10d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 10d(ii): Verify Y-Axis Title")
        
        """    11. Hover over the highest bar under North America/Stereo Systems. Then hover over Drill down to and select Store Business Sub Region    """
        a =['Store Business Sub Region', 'Sale Year/Quarter']
        iaresult.verify_autolink_tooltip_submenu('MAINTABLE_wbody0','riser!s5!g0!mbar!r0!c0!', "Drill down to", a, "Step 05a: Verify the drill menu shows for only Region and Year.")
        time.sleep(5) 
        utillobj.switch_to_default_content(1)
        #driver.switch_to.default_content()
        time.sleep(4)
        
        """    12. Click IA > Save As > Type C2226978b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID+"b")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    13. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226978b.fex&tool=Chart    """
        utillobj.infoassist_api_edit(Test_Case_ID+"b", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    14. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 14a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
          
        """    15. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
