'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2230984
TestCase Name = Test that Auto Drill works with ESRI Charts - AHTML
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2230984_TestClass(BaseTestCase):
    def test_C2230984(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2230984_"+browser_type
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        act_misc=active_miscelaneous.Active_Miscelaneous(self.driver)
        expected_menu=['More Options','Advanced Chart','Original Chart']
        elem = "#MAINTABLE_wbody0 span>a[href*='contentDrill']"

        """    1.  Open a new chart with wf_retail_lite using the API,    """
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P276/S9976', 'mrid', 'mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Click HTML5 and Select Active Report format from format group in Home tab    """
        ribbonobj.change_output_format_type('active_report')
        time.sleep(4)
        
        """    3. Select Format tab> ESRI Choropleth    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        time.sleep(4)
        
        """    4. Drag Revenue field to color bucket  """
        metaobj.datatree_field_click('Revenue', 1, 1, 'Add To Query', 'Color')
        time.sleep(8)
        
        """    5. Drag Store,Country in Layer  """
        metaobj.datatree_field_click('Store,Country', 1, 1, 'Add To Query', 'Layer')
        time.sleep(8)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea #pfjTableChart_1"),'C2230984_Actual_step04', image_type='actual',x=1, y=1, w=-1, h=-1)
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g5!mregion!", "persian_red", "Step 04.a(i) Verify map color")
        iaresult.verify_color_scale_esri_maps("pfjTableChart_1", ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M',], "Step 04.b")
        
        """    6. Click Format tab > Autodrill button   """
        ribbonobj.switch_ia_tab("Format")
        if driver.find_element_by_css_selector("#FormatAutoDrillCluster").value_of_css_property("Visibility") == 'hidden':
            autolink_altbtn=driver.find_element_by_css_selector("#FormatAutoDrillCluster_altButton img")
            utillobj.default_left_click(object_locator=autolink_altbtn)
            time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(8)
        
        """    7. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        frame_obj=driver.find_element_by_css_selector('[id^=ReportIframe-]')
        x_fr=frame_obj.location['x']
        y_fr=frame_obj.location['y']
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2230984_Actual_step06', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        chart_type_css="path[class*='riser!s0!g33!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        act_misc.verify_arChartToolbar("MAINTABLE_0", expected_menu, "Step 06.a: Verify Chart toolbar")
        expected_tooltip=['Store Country:China', 'Revenue:$70,110.18', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody0","riser!s0!g5!mregion",expected_tooltip, "Step 06.b: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr+15)
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g8!mregion", "persian_red", "Step 06.a: Verify region color")
        iaresult.verify_color_scale_esri_maps("MAINTABLE_wbody0", ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M',], "Step 06.c")
        time.sleep(5)
        #utillobj.switch_to_default_content(1)
        
                
        """    8. Hover over the Continental United States (Green colored area between Canada and Mexico ) until the pop up appears    """
        """    9. From the pop up select Drill down to Store State Province    """
#         iaresult.select_ia_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g33!mregion!', 'Drill down to Store State Province',wait_time=1, x_offset=x_fr-250, y_offset=y_fr+25, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10, action_x_offset=210, action_y_offset=190)
#         #resultobj.select_default_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g33!mregion!', 'Drill down to Store State Province',wait_time=1,)
#         time.sleep(5)
#         iaresult.backup_autolink_tooltip_menu(elem,'MAINTABLE_wbody0', 'riser!s0!g33!mregion!', 'Drill down to Store State Province',1, x_offset=x_fr-250, y_offset=y_fr+25, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10, action_x_offset=210, action_y_offset=190)
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g33!mregion', 'Drill down to Store State Province',wait_time=1, x_offset=210,y_offset=190, action_x_offset=210, action_y_offset=190, x_offset_menu=20, y_offset_menu=8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        act_misc.verify_arChartToolbar("MAINTABLE_0", expected_menu, "Step 09: Verify Chart toolbar")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g30!mregion", "persian_red", "Step 09.a: Verify region color")
        #expected_tooltip=['Store State Province:Texas, United States', 'Revenue:$30,157,666.34', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store Country', 'Drill down to Store City']
        expected_tooltip=['Store State Province:Texas', 'Revenue:$30,157,666.34', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody0","riser!s0!g29!mregion",expected_tooltip, "Step 09.b: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-15)
        iaresult.verify_color_scale_esri_maps("MAINTABLE_wbody0", ['Revenue', '1M', '82.7M', '164.4M', '246.1M', '327.8M'], "Step 09.c")
        time.sleep(2)
        
        """    10. Hover over California and select Drill down to Store City    """
#         iaresult.select_ia_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g4!mregion!', 'Drill down to Store City', wait_time=1, x_offset=x_fr, y_offset=y_fr-7, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
#         time.sleep(8)
#         iaresult.backup_autolink_tooltip_menu(elem,'MAINTABLE_wbody0', 'riser!s0!g4!mregion!', 'Drill down to Store City', 2, x_offset=x_fr, y_offset=y_fr-7, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g4!mregion!', 'Drill down to Store City',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(8)
        act_misc.verify_arChartToolbar("MAINTABLE_0", expected_menu, "Step 09: Verify Chart toolbar")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mregion", "persian_red", "Step 10.a: Verify region color")
        iaresult.verify_color_scale_esri_maps("MAINTABLE_wbody0", ['Revenue', '4.4M', '5M', '5.4M', '6M', '6.4M',], "Step 10.b")
        #expected_tooltip=['Store City:San Diego, California, United States', 'Revenue:$6,428,620.20', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        expected_tooltip=['Store City:San Diego', 'Revenue:$6,428,620.20', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody0","riser!s0!g1!mregion",expected_tooltip, "Step 10.c: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-15)
        utillobj.switch_to_default_content(1)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2230984_Actual_step09', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        
        """    11. Select ESRI Proportinal Symbol from chart types group under Format    """
        ribbonobj.select_ribbon_item("Format", "Proportional_symbol")
        time.sleep(4)
        
        """    12. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        frame_obj=driver.find_element_by_css_selector('[id^=ReportIframe-]')
        x_fr=frame_obj.location['x']
        y_fr=frame_obj.location['y']
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2230984_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(4)
        utillobj.switch_to_frame(1)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        chart_type_css="#MAINTABLE_wbody0 circle[class*='riser!s0!g27!mmarker']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(3)
        act_misc.verify_arChartToolbar("MAINTABLE_0", expected_menu, "Step 12: Verify Chart toolbar")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mmarker!", "bar_blue", "Step 12.a: Verify circle color")
        expected_tooltip=['Store Country:Spain', 'Revenue:$27,383,946.14', 'Filter Chart', 'Exclude from Chart', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody0","riser!s0!g27!mmarker!",expected_tooltip, "Step 12.b: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-15)
        legend_list = ['Revenue', 'Revenue', '545.8M', '273M', '0M']
        resultobj.verify_riser_legends("MAINTABLE_wbody0", legend_list, "Step 12.c: Verify legend Title")
        time.sleep(5)
        
        """    13. Hover over the Continental United States until the pop up appears. Then hover over Drill down to    """
        """    14. From the pop up select Drill down to Store State Province    """
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g33!mmarker!', 'Drill down to Store State Province',wait_time=1, x_offset_menu=20, y_offset_menu=8)
#         iaresult.select_ia_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g33!mmarker!', 'Drill down to Store State Province',wait_time=1, x_offset=x_fr, y_offset=y_fr+15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
#         time.sleep(5)
#         iaresult.backup_autolink_tooltip_menu(elem,'MAINTABLE_wbody0', 'riser!s0!g33!mmarker!', 'Drill down to Store State Province',1, x_offset=x_fr, y_offset=y_fr+15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(8)
        utillobj.switch_to_default_content(1)
        time.sleep(3)
        utillobj.take_screenshot(driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']"),'C2230984_Actual_step14', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(5)
        utillobj.switch_to_frame(1)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        act_misc.verify_arChartToolbar("MAINTABLE_0", expected_menu, "Step 14: Verify Chart toolbar")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g21!mmarker!", "bar_blue", "Step 14.a: Verify region color")
        #expected_tooltip=['Store State Province:Idaho, United States', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store Country', 'Drill down to Store City']
        expected_tooltip=['Store State Province:Idaho', 'Revenue:$327,810,680.45', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody0","riser!s0!g9!mmarker!",expected_tooltip, "Step 14.b: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-15)        
        legend_list = ['Revenue', 'Revenue', '327.8M', '164.4M', '1M']
        resultobj.verify_riser_legends("MAINTABLE_wbody0", legend_list, "Step 14.c: Verify legend Title")
        time.sleep(5)
        
        """    15. Hover over California. In the pop-up hover over Drill down to and select Drill down to Store City    """
#         iaresult.select_ia_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g4!mmarker', 'Drill down to Store City',wait_time=1, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
#         time.sleep(8)
#         iaresult.backup_autolink_tooltip_menu(elem,'MAINTABLE_wbody0', 'riser!s0!g4!mmarker', 'Drill down to Store City',2, x_offset=x_fr, y_offset=y_fr-15, x_offset_menu=x_fr-20, y_offset_menu=y_fr-10)
        iaresult.select_autolink_tooltip_menu('MAINTABLE_wbody0', 'riser!s0!g4!mmarker', 'Drill down to Store City',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(8)
        act_misc.verify_arChartToolbar("MAINTABLE_0", expected_menu, "Step 15: Verify Chart toolbar")
        utillobj.verify_chart_color("MAINTABLE_wbody0", "riser!s0!g2!mmarker", "bar_blue", "Step 15.a: Verify region color")
        legend_list = ['Revenue', 'Revenue', '6.4M', '4.4M']
        resultobj.verify_riser_legends("MAINTABLE_wbody0", legend_list, "Step 15:b Verify legend Title")
        #expected_tooltip=['Store City:San Diego, California, United States', 'Revenue:$6,428,620.20', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        expected_tooltip=['Store City:San Diego', 'Revenue:$6,428,620.20', 'Filter Chart', 'Exclude from Chart', 'Restore Original', 'Drill up to Store State Province', 'Drill down to Store Postal Code']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody0","riser!s0!g1!mmarker",expected_tooltip, "Step 15.c: verify the default tooltip values", x_offset=x_fr, y_offset=y_fr-15)
        utillobj.switch_to_default_content(1)
        time.sleep(5)
        
        """    16. Click IA > Save As > Type C2230984 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    17. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2230984.fex&tool=Chart    """
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
        utillobj.asequal(disabled, None, "Step 18a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
          
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
