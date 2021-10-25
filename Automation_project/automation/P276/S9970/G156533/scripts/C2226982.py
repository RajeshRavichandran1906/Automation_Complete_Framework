'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226982
TestCase Name = Test that Auto Drill works with Reporting Objects
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226982_TestClass(BaseTestCase):
    def test_C2226982(self):
        driver = self.driver
        #driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2226982_"+browser_type
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        """    Open IA_Chart for edit using the API 
        http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Chart.fex&tool=Chart    """
        utillobj.infoassist_api_edit("IA-Chart", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Right click on Store Business Region in Columns on the query panel and choose Change Title. Enter 'World Market' > OK    """
        metaobj.querytree_field_click("Store,Business,Region", 1, 1, "Change Title...")
        time.sleep(8)
        edit_title_css="div[id^='BiDialog'][tabindex='0']"
        edit_title_obj=self.driver.find_element_by_css_selector(edit_title_css)
        utillobj.set_text_field_using_actionchains(edit_title_obj.find_element_by_css_selector("input"), 'World Market')
        utillobj.click_dialog_button(edit_title_css,"OK")
        time.sleep(4)
        
        """    3. Right click on Sale,Year in Color By on the query panel and choose Change Title. Enter 'Fiscal Year' > Ok    """
        metaobj.querytree_field_click("Sale,Year", 1, 1, "Change Title...")
        time.sleep(8)
        edit_title_obj=self.driver.find_element_by_css_selector(edit_title_css)
        utillobj.set_text_field_using_actionchains(edit_title_obj.find_element_by_css_selector("input"), 'Fiscal Year')
        utillobj.click_dialog_button(edit_title_css,"OK")
        time.sleep(4)
        
        """    4. Click Format tab > Autodrill button    """
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoDrillCluster").value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(4)
        
        """    5. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')        
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2226982_Actual_step05', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
#         frame_obj=driver.find_element_by_css_selector('[id^=ReportIframe-]')
#         x_fr=frame_obj.location['x']
#         y_fr=frame_obj.location['y']
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]') 
        time.sleep(3)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 05a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 139, 'Step 05b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c0!", "bar_blue1", "Step 05c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g1!mbar!r0!c0!", "bar_green", "Step 05c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s2!g4!mbar!r0!c1!", "med_green", "Step 05c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g3!mbar!r0!c1!", "pale_yellow_2", "Step 05c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s4!g3!mbar!r0!c0!", "brick_red", "Step 05c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s5!g0!mbar!r0!c1!", "light_brick", "Step 05c(6): Verify sixth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 05d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 05d(ii): Verify Y-Axis Title")
        expected_label=['EMEA', 'North America', 'Oceania', 'South America']
        iaresult.verify_infoassist_row_column_header_labels("jschart_HOLD_0", "columns", "World Market", expected_label, "Step 03e:")
        expected_legend_list=['Fiscal Year','2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 03f:")
        time.sleep(8)
        
        """    6. Hover over the top bar in North America/Stereo Systems until the pop-up appears    """
        """    7. On the pop-up hover over Drill down to and select Store Business Sub Region    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region')
        #time.sleep(8)
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(8)
        elem = "#jschart_HOLD_0 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 8)
        time.sleep(8)
        a =['Store Business Sub Region:Midwest', 'Product Category:Stereo Systems', 'Revenue:$6,990,028.64', 'Fiscal Year:2016', 'Restore Original', 'Drill up to World Market', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s0!g0!mbar!r0!c3!',a,"Step 07a: Verify Midwest tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 1, 8, "Step 07b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 07c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 07d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 07e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!r0!c5!", "bar_blue1", "Step 07f: Verify bar color")
        expected_label=['Canada', 'East', 'Mexico', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        iaresult.verify_infoassist_row_column_header_labels("jschart_HOLD_0", "columns", "Store Business Sub Region", expected_label, "Step 07g:")
        expected_legend_list=['Fiscal Year','2016']
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 07h:") 
        time.sleep(3)
        
        """    8. Hover over the bar for West Sub Region, then hover over Drill down to and select Sale Year/Quarter    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter')
        #iaresult.select_autolink_tooltip_menu_with_offset('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter')
        #time.sleep(5)
        #iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10, action_x_offset=10, action_y_offset=200)
        time.sleep(5)
        elem = "#jschart_HOLD_0 g.chartPanel rect[class^='riser!s0']"
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        a =['Store Business Sub Region:West', 'Product Category:Stereo Systems', 'Revenue:$12,514,034.09', 'Sale Year/Quarter:2016 Q3', 'Restore Original', 'Drill up to', 'Drill down to']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0','riser!s2!g0!mbar!r0!c0!',a,"Step 08a: Verify Midwest tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('jschart_HOLD_0', 4, 1, "Step 08b: Verify drilldown bars")
        resultobj.verify_xaxis_title('jschart_HOLD_0', "Product Category", "Step 08c: verify X axis title")
        resultobj.verify_yaxis_title('jschart_HOLD_0', "Revenue", "Step 08d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 08e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s3!g0!mbar!r0!c0!", "pale_yellow_2", "Step 08f: Verify bar color")
        iaresult.verify_infoassist_row_column_header_labels("jschart_HOLD_0", "columns", "Store Business Sub Region", ['West'], "Step 08g:")
        expected_legend_list=['Sale Year/Quarter','2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        resultobj.verify_riser_legends("jschart_HOLD_0", expected_legend_list, "Step 08h:") 
        time.sleep(3)
        
        """    9. Hover over the top bar and then hover over Drill up to.    """
        a =['World Market', 'Fiscal Year']
        iaresult.verify_autolink_tooltip_submenu('jschart_HOLD_0','riser!s3!g0!mbar!r0!c0!', "Drill up to", a, "Step 09a: Verify the chart show entries for World Market and Fiscal Year..")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        #driver.switch_to.default_content()
        time.sleep(4)
        
        """    10. Click IA > Save As > Type C2226982a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID+"a")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    11. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226982a.fex&tool=Chart    """
        utillobj.infoassist_api_edit(Test_Case_ID+"a", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    12. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 10a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
         
        """    13. Click on HTML5 output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
         
        """    14. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]') 
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2226982_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]') 
        time.sleep(3)
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 14a: X annd Y axis Scales Values has changed or NOT')
        resultobj.verify_number_of_riser("MAINTABLE_wbody0", 1, 139, 'Step 14b: Verify the total number of risers displayed on Run Chart')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c0!", "bar_blue", "Step 14c(1): Verify first segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s1!g1!mbar!r0!c0!", "pale_green", "Step 14c(2): Verify second segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s2!g4!mbar!r0!c1!", "dark_green", "Step 14c(3): Verify third segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g3!mbar!r0!c1!", "pale_yellow", "Step 14c(4): Verify fourth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s4!g3!mbar!r0!c0!", "brick_red", "Step 14c(5): Verify fifth segment in the bar color")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s5!g0!mbar!r0!c1!", "orange", "Step 14c(6): Verify sixth segment in the bar color")
        xaxis_value="Product Category"
        yaxis_value="Revenue"
        resultobj.verify_xaxis_title("MAINTABLE_wbody0", xaxis_value, "Step 14d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody0", yaxis_value, "Step 14d(ii): Verify Y-Axis Title")
        expected_label=['EMEA', 'North America', 'Oceania', 'South America']
        iaresult.verify_infoassist_row_column_header_labels("MAINTABLE_wbody0", "columns", "World Market", expected_label, "Step 14e:")
        expected_legend_list=['Fiscal Year', '2011', '2012', '2013', '2014', '2015', '2016']
        resultobj.verify_riser_legends("MAINTABLE_wbody0", expected_legend_list, "Step 14f:")
        time.sleep(8)
        
        """    15. Hover over the top bar in North America/Stereo Systems until the pop-up appears    """
        """    16. On the pop-up hover over Drill down to and select Store Business Sub Region    """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region')
        #iaresult.select_ia_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        #time.sleep(8)
        #iaresult.select_ia_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(3)
        elem = "#MAINTABLE_wbody0 g.chartPanel rect[class^='riser!s0']"
        #iaresult.backup_autolink_tooltip_menu(elem,'MAINTABLE_wbody0', 'riser!s5!g4!mbar!r0!c1!', 'Drill down to->Store Business Sub Region',8, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 8)
        time.sleep(8)
        a =['Store Business Sub Region:Midwest', 'Product Category:Stereo Systems', 'Revenue:$6,990,028.64', 'Fiscal Year:2016', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to World Market', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s0!g0!mbar!r0!c3!',a,"Step 16a: Verify Midwest tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 1, 8, "Step 16b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 16c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 16d: verify Y axis title")
        expected_xval_list=['Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 16e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g0!mbar!r0!c5!", "bar_blue", "Step 16f: Verify bar color")
        expected_label=['Canada', 'East', 'Mexico', 'Midwest', 'Northeast', 'South', 'Southeast', 'West']
        iaresult.verify_infoassist_row_column_header_labels("MAINTABLE_wbody0", "columns", "Store Business Sub Region", expected_label, "Step 16g:")
        expected_legend_list=['Fiscal Year', '2016']
        resultobj.verify_riser_legends("MAINTABLE_wbody0", expected_legend_list, "Step 16h:") 
        time.sleep(3)
        
        """    17. Hover over the bar for West Sub Region, then hover over Drill down to and select Sale Year/Quarter    """
        #iaresult.select_ia_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter',wait_time=1, action_x_offset=10, action_y_offset=200, x_offset_menu=20, y_offset_menu=8)
        #time.sleep(5)
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter')
        #iaresult.select_autolink_tooltip_menu_with_offset('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter')
        #iaresult.select_ia_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter',wait_time=1, x_offset=x_fr,y_offset=y_fr-15, action_x_offset=10, action_y_offset=200, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        time.sleep(5)
        #iaresult.backup_autolink_tooltip_menu(elem,'MAINTABLE_wbody0', 'riser!s0!g0!mbar!r0!c7!', 'Drill down to->Sale Year/Quarter',1, x_offset=x_fr,y_offset=y_fr-15, action_x_offset=10, action_y_offset=200, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        a =['Store Business Sub Region:West', 'Product Category:Stereo Systems', 'Revenue:$12,514,034.09', 'Sale Year/Quarter:2016 Q3', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to', 'Drill down to']
        resultobj.verify_default_tooltip_values('MAINTABLE_wbody0','riser!s2!g0!mbar!r0!c0!',a,"Step 17a: Verify Midwest tooltip values")
        time.sleep(10)
        resultobj.verify_number_of_riser('MAINTABLE_wbody0', 4, 1, "Step 17b: Verify drilldown bars")
        resultobj.verify_xaxis_title('MAINTABLE_wbody0', "Product Category", "Step 17c: verify X axis title")
        resultobj.verify_yaxis_title('MAINTABLE_wbody0', "Revenue", "Step 17d: verify Y axis title")
        expected_xval_list=['Stereo Systems']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_wbody0', expected_xval_list, expected_yval_list, 'Step 17e: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s3!g0!mbar!r0!c0!", "pale_yellow", "Step 17f: Verify bar color")
        iaresult.verify_infoassist_row_column_header_labels("MAINTABLE_wbody0", "columns", "Store Business Sub Region", ['West'], "Step 17g:")
        expected_legend_list=['Sale Year/Quarter', '2016 Q1', '2016 Q2', '2016 Q3', '2016 Q4']
        resultobj.verify_riser_legends("MAINTABLE_wbody0", expected_legend_list, "Step 17h:") 
        time.sleep(3)
        
        """    18. Hover over the top bar and then hover over Drill up to.    """
        a =['World Market', 'Fiscal Year']
        iaresult.verify_autolink_tooltip_submenu('MAINTABLE_wbody0','riser!s3!g0!mbar!r0!c0!', "Drill up to", a, "Step 18a: Verify the chart show entries for World Market and Fiscal Year..")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        #driver.switch_to.default_content()
        time.sleep(4)
        
        """    19. Click IA > Save As > Type C2226982b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID+"b")
        time.sleep(5)
        
        """    20. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226982b.fex&tool=Chart   """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID+"b", 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    21. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 21a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
          
        """    22. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
