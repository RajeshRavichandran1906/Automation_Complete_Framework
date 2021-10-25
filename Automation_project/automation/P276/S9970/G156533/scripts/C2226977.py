'''
Created on 13-Mar-2017
@author: Nasir
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226977
TestCase Name = Test that Auto Drill works with ESRI Charts - HTML5
'''
import unittest, time
from common.lib import utillity 
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata
  
class C2226977_TestClass(BaseTestCase):
    
    def test_C2226977(self):
        
        """
        TESTCASE OBJECTS
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        """
        TESTCASE VARIABLES
        """    
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2226977_"+browser_type
        elem = "#jschart_HOLD_0 span>a[href*='contentDrill']"
        
        """    1.  Open a new chart with wf_retail_lite using the API,    """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P276/S9976', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(20)
          
        """    2. Select Format tab> ESRI Choropleth    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        time.sleep(15)
        
        """    3. Drag Revenue field to color bucket  """
        #metaobj.datatree_field_click('Revenue', 1, 1, 'Add To Query', 'Color')
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue',1,'Color',0)
        time.sleep(8)
        
        """    4. Drag Store,Country in Layer  """
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Country',1,'Layer',0)
        #metaobj.datatree_field_click('Store,Country', 1, 1, 'Add To Query', 'Layer')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g5!mregion!", "persian_red", "Step 04.01: Verify map color")
        iaresult.verify_color_scale_esri_maps("pfjTableChart_1", ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M',], "Step 04.02")
        
        """    5. Click Format tab > Autodrill button   """
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoDrillCluster").value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(8)
        
        """    6. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        chart_type_css="path[class*='riser!s0!g33!mregion']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(5)
        frame_obj=driver.find_element_by_css_selector('[id^=ReportIframe-]')
        x_fr=frame_obj.location['x']
        y_fr=frame_obj.location['y']
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2226977_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g8!mregion", "persian_red", "Step 06.01: Verify region color")
        iaresult.verify_color_scale_esri_maps("jschart_HOLD_0", ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M',], "Step 06.02")
        expected_tooltip=['Store Country:China', 'Revenue:$70,110.18', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g5!mregion",expected_tooltip, "Step 06.03: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr+15)
                
        """    7. Hover over the Continental United States (Green colored area between Canada and Mexico ) until the pop up appears    """
        """    8. From the pop up select Drill down to Store State Province    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g33!mregion', 'Drill down to Store State Province',wait_time=1, x_offset=210,y_offset=200, action_x_offset=210, action_y_offset=200, x_offset_menu=20, y_offset_menu=8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g30!mregion", "persian_red", "Step 08.01: Verify region color")
        iaresult.verify_color_scale_esri_maps("jschart_HOLD_0", ['Revenue', '1M', '82.7M', '164.4M', '246.1M', '327.8M'], "Step 08.b")
        #expected_tooltip=['Store State Province:Texas, United States', 'Revenue:$30,157,666.35', 'Restore Original', 'Drill up to Store Country', 'Drill down to Store City']
        expected_tooltip=['Store State Province:Texas|United States', 'Revenue:$30,157,666.35', 'Restore Original', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g29!mregion",expected_tooltip, "Step 08.02: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-15)
        time.sleep(2)
        
        """    9. Hover over California and select Drill down to Store City    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g4!mregion!', 'Drill down to Store City',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(8)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mregion", "persian_red", "Step 09.01: Verify region color")
        iaresult.verify_color_scale_esri_maps("jschart_HOLD_0", ['Revenue', '4.4M', '5M', '5.4M', '6M', '6.4M',], "Step 09.02")
        #expected_tooltip=['Store City:San Diego, California, United States', 'Revenue:$6,428,620.20', 'Restore Original', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        expected_tooltip=['Store City:San Diego|California|United States', 'Revenue:$6,428,620.20', 'Restore Original', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g1!mregion",expected_tooltip, "Step 09.03: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr+5)
        utillobj.switch_to_default_content(1)
        time.sleep(5)
        
        """    10. Select ESRI Proportinal Symbol from chart types group under Format    """
        ribbonobj.select_ribbon_item("Format", "Proportional_symbol")
        time.sleep(4)
        
        """    11. Add Store,Business,Region in the Color Bucket    """
        metaobj.datatree_field_click('Store,Business,Region', 1, 1, 'Add To Query', 'Color')
        time.sleep(8)
        
        """    12. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        chart_type_css="#jschart_HOLD_0 circle[class*='riser!s0!g27!mmarker']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(10)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2226977_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s1!g2!mmarker!", "bar_green", "Step 12.01: Verify circle color")
        expected_tooltip=['Store Country:United Kingdom', 'Revenue:$51,494,193.36', 'Store Business Region:EMEA', 'Drill down to']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g27!mmarker!",expected_tooltip, "Step 12.02: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr+15)
        legend_list = ['Store Business Region','EMEA','North America','Oceania','South America', 'Revenue', '545.8M', '272.9M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend_list, "Step 12.03: Verify legend Title")
        time.sleep(5)
        
        """    13. Hover over the Continental United States until the pop up appears. Then hover over Drill down to    """
        """    14. From the pop up select Drill down to Store State Province    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s1!g2!mmarker!', 'Drill down to->Store State Province',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        utillobj.switch_to_default_content(1)
        time.sleep(3)
        utillobj.switch_to_frame(1)
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[id^="ReportIframe-"]')))
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g21!mmarker!", "bar_blue1", "Step 14.01: Verify region color")
        #expected_tooltip=['Store State Province:Idaho, United States', 'Revenue:$327,810,680.45', 'Store Business Region:North America', 'Restore Original', 'Drill up to Store Country', 'Drill down to']
        expected_tooltip=['Store State Province:Idaho|United States', 'Revenue:$327,810,680.45', 'Store Business Region:North America', 'Restore Original', 'Drill up to Store Country', 'Drill down to']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g9!mmarker!",expected_tooltip, "Step 14.02: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr+15)
        legend_list = ['Store Business Region', 'North America', 'Revenue', '327.8M', '164.4M', '1M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend_list, "Step 14.03: Verify legend Title")        
        time.sleep(3)
        
        """    15. Hover over California. In the pop-up hover over Drill down to and select Drill down to Store City    """
        iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g4!mmarker', 'Drill down to->Store City',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(28)
        utillobj.verify_chart_color("jschart_HOLD_0", "riser!s0!g2!mmarker", "bar_blue1", "Step 15.01: Verify region color")
        legend_list = ['Store Business Region', 'North America', 'Revenue', '6.4M', '4.4M']
        resultobj.verify_riser_legends("jschart_HOLD_0", legend_list, "Step 15.02: Verify legend Title")
        #expected_tooltip=['Store City:San Diego, California, United States', 'Revenue:$6,428,620.20', 'Store Business Region:North America', 'Restore Original', 'Drill up to Store State Province', 'Drill down to']
        expected_tooltip=['Store City:San Diego|California|United States', 'Revenue:$6,428,620.20', 'Store Business Region:North America', 'Restore Original', 'Drill up to Store State Province', 'Drill down to']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g1!mmarker",expected_tooltip, "Step 15.03: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr+5)
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(5)
        
        """    16. Click IA > Save As > Type C2226977 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    17. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226977.fex&tool=Chart    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    18. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 18.01: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
          
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()