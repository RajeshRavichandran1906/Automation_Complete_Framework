'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227570
TestCase Name = Verify Chart with Multi Drill and Auto Drill using wf_retail_lite
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run,ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2227570_TestClass(BaseTestCase):

    def test_C2227570(self):
        
        Test_Case_ID = "C2227570"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        """ 
        Step01: http://machine:port/ibi_apps/ia?tool=report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_ia_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)  
        time.sleep(8)      
                
        """
        Step02: Double click "Country", "Sales"   
        """
        metaobj.datatree_field_click('COUNTRY', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('SALES', 2, 1)
        time.sleep(4)
        coln_list = ['COUNTRY', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02.01: Verify Column titles ")
        time.sleep(2) 
             
        """
        Step03: Click "IA" > "Save".
        Step04: Enter title= "Report003" > Click "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID+"_Report003")
        time.sleep(2)
             
        """
        Step05: Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
            
        """
        Step06: Launch IA Chart mode with wf_retail_lite.mas:
        http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032_ia_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)  
        time.sleep(8)
            
        """
        Step07: Double-click "Cost of Goods" under Sales Measures
        """
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
            
        """
        Step08: Double-click "Product,Category" under Product Dimension
        """
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(4)
            
        """
        Step09: Verify the following "Chart" in Livepreview
        """
        resultobj.verify_number_of_riser("TableChart_1", 1, 7, 'Step 09.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('TableChart_1', expected_xval_list, expected_yval_list, 'Step 09.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g1!mbar!", "bar_blue1", "Step 09.03: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step 09.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", yaxis_value, "Step 09.05: Verify Y-Axis Title")
            
        """
        Step10: Select "Format" > "Auto Drill" button (from navigation group)
        """
        ribbonobj.switch_ia_tab("Format")
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
            
        """
        Step11: Select "Cost of Goods" in Query pane
        Step12: Click "Links" > "Drill down" from "Field" tab.
        """         
        metaobj.querytree_field_click("Cost of Goods", 1, 0)
        time.sleep(2)   
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(4)
            
        """
        Step13: On "Drill Down" window, Verify "Report" is enabled by default
        """
        ia_ribbonobj.create_drilldown_report("report", verify_default_drilldown_type=True)
            
        """
        Step14: Click "Browse" > Select "Report003" > Open.
        Step15: Set "Description" = "Drilldown to Report".
        """
        ia_ribbonobj.create_drilldown_report("report", browse_file_name='C2227570_Report003',set_description="Drilldown to Report")
            
        """
        Step16: Click "Create a new drill down" icon        
        Step17: Click "Web Page" option, click URL input box.
        Step18: Type "http://www.ibi.com"
        Step19: Set "Description" = "Information builders".
        Step20: Tab out of the textfield
        Step21: Verify "Information builders" is showing on the left frame.        
        """
        ia_ribbonobj.create_drilldown_report("report",create_new_drilldown=True)
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.ibi.com",set_description="Information builders", verify_left_pane=['2','Information builders'],msg="Step 21.01: Verify description Information builders", click_ok='yes')
            
        """
        Step22: Click "Create a new drill down" icon
        Step23: Click "Web Page" option, click URL input box
        Step24: Type "http://www.google.com"
        Step25: Set "Description" = "Google".
        Step26: Tab out of the textfield
        Step27: Verify the following drilldown window
        Step28: Click "OK"
        """
        time.sleep(2)   
        ribbonobj.select_ribbon_item('Field', 'DrillDown')
        time.sleep(4)
        ia_ribbonobj.create_drilldown_report("report",create_new_drilldown=True)
        time.sleep(2)
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.google.com",set_description="Google", verify_left_pane=['3','Google'],msg="Step 27.01: Verify description Google", click_ok='yes')
         
        """
        Step29: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(4)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2227570_Actual_step29', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.switch_to_frame(pause=1)
        WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe')))
        time.sleep(3)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        utillobj.synchronize_with_number_of_element(chart_type_css, 1, 30)  
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 29.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 29.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 29.03: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 29.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 29.05: Verify Y-Axis Title")
        
        """
        Step30: Hover over on Chart riser "Accessories"
        Step31: Verify the Autodrill and Multidrill menus are displayed
        """
        expected_tooltip=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Drill down to Product Subcategory', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g0!mbar",expected_tooltip, "Step 30.01: verify the Accessories default tooltip values")
        
        """
        Step32: Select "Drill Down to Product Subcategory", Verify Chart
        """
        time.sleep(5)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g0!mbar", "Drill down to Product Subcategory",wait_time=1,x_offset_menu=20, y_offset_menu=8)
        elem = "#jschart_HOLD_0 g.chartPanel rect[class^='riser!s0']"
        utillobj.synchronize_with_number_of_element(elem, 3, 20)
#         WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        time.sleep(3)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 3, 'Step 32.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Charger', 'Headphones', 'Universal Remote Controls']
        expected_yval_list=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 32.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 32.03: Verify first bar color")
        xaxis_value="Product Subcategory"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 32.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 32.05: Verify Y-Axis Title")
        
        """
        Step33: Hover over Chart riser "Headphones", Verify menus
        """
        expected_tooltip=['Product Subcategory:Headphones', 'Cost of Goods:$51,663,564.00', 'Restore Original', 'Drill up to Product Category', 'Drill down to Model', 'Drilldown to Report', 'Information builders', 'Google']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g1!mbar",expected_tooltip, "Step 33.01: verify the Headphones default tooltip values")
        
        """
        Step34: Click "Drilldown to Report"
        """
        time.sleep(5)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g1!mbar", "Drilldown to Report",wait_time=1,x_offset_menu=20, y_offset_menu=8)
        time.sleep(8)
        utillobj.switch_to_default_content()
        time.sleep(3)
        
        """
        Step35: Verify that drilldown to "Report003" is working properly and it opens in a new window
        Step36: Close the Report window
        """
        utillobj.switch_to_window(1)
        time.sleep(10) 
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2227570_run_Ds01.xlsx" , 'Step 35.01: Verify drilldown "Report003" data set')
        time.sleep(2)
        self.driver.close()
        time.sleep(1)
        utillobj.switch_to_window(0)
        time.sleep(3)
        
        """
        Step37: Hover over Chart riser "Charger", Click "Drill down to Model"
        """
        utillobj.switch_to_frame(pause=1)
        WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe')))
        time.sleep(3)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g0!mbar", "Drill down to Model",wait_time=1,x_offset_menu=20, y_offset_menu=8)
        
        """
        Step38: Verify the following "Chart"
        """
        time.sleep(5)
        chart_type_css="rect[class*='riser!s0!g1!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 2, 'Step 38.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['B00D7MOHDO', 'BCG34HRE4KN']
        expected_yval_list=['0', '0.3M', '0.6M', '0.9M', '1.2M', '1.5M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 38.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g1!mbar!", "bar_blue1", "Step 38.03: Verify first bar color")
        xaxis_value="Model"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 38.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 38.05: Verify Y-Axis Title")
        
        """
        Step39: Hover over Chart riser "BCG34HRE4KN" , Click "Information builders"
        """
        time.sleep(3)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g1!mbar", "Information builders",wait_time=1,x_offset_menu=20, y_offset_menu=8)
        
        """
        Step40: Verify it displays a new window going to IBI site.
        Step41: Close the window
        """
        time.sleep(3)
        utillobj.switch_to_default_content(pause=2)
        utillobj.switch_to_window(1)
        time.sleep(1)
        expected_title='Data and Analytics Company | ibi'
        drill1=(expected_title in driver.title)
        utillobj.asequal(True, drill1, "Step 40.01: Verify IBI page is displayed")
        time.sleep(1)
        
        self.driver.close()
        time.sleep(1)
        utillobj.switch_to_window(0)
        time.sleep(1)
        
        """
        Step42: Hover over Chart riser "B00D7MOHDO" , Click "Restore original"
        """
        driver.switch_to.default_content()
        time.sleep(3)
        utillobj.switch_to_frame(pause=1)
        WebDriverWait(driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe')))
        time.sleep(3)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g0!mbar", "Restore Original",wait_time=1,x_offset_menu=20, y_offset_menu=8)
        """
        Step43: Verify the following Chart
        """
        time.sleep(5)
        chart_type_css="rect[class*='riser!s0!g0!mbar']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        resultobj.verify_number_of_riser("jschart_HOLD_0", 1, 7, 'Step 43.01: Verify the total number of risers displayed on Run Chart')
        expected_xval_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yval_list=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        resultobj.verify_riser_chart_XY_labels('jschart_HOLD_0', expected_xval_list, expected_yval_list, 'Step 43.02: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g0!mbar!", "bar_blue1", "Step 43.03: Verify first bar color")
        xaxis_value="Product Category"
        yaxis_value="Cost of Goods"
        resultobj.verify_xaxis_title("jschart_HOLD_0", xaxis_value, "Step 43.04: Verify X-Axis Title")
        resultobj.verify_yaxis_title("jschart_HOLD_0", yaxis_value, "Step 43.05: Verify Y-Axis Title")
        
        """
        Step44: Hover over on Chart riser "Media player" , Click "Google"
        Step45: Verify it displays a new window going to "Google" site.
        Step46: Close the window
        """
        time.sleep(3)
        ia_resultobj.select_ia_autolink_tooltip_menu("jschart_HOLD_0","riser!s0!g3!mbar", "Google",wait_time=1,x_offset_menu=20, y_offset_menu=8)        
        time.sleep(3)
        utillobj.switch_to_default_content()
        time.sleep(3)
        utillobj.switch_to_window(1)
        time.sleep(1)
        drill1=(driver.title=='Google')
        utillobj.asequal(True, drill1, "Step 45.01: Verify Gogole page is displayed")
        time.sleep(1)
        self.driver.close()
        time.sleep(1)
        utillobj.switch_to_window(0)
        time.sleep(1)
        
        """
        Step47: Click "IA" > "Save"
        Step48: Enter Title = "C2227570" > Save
        Step49: Logout
        """
        self.driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()