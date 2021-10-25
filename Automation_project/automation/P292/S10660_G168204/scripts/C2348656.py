'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348656
Test case Name =  Verify Basemaps
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By



class C2348656_TestClass(BaseTestCase):

    def test_C2348656(self):
    
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2348656"
        

        
        """    1. Use API call to open IA in chart mode with wf_retail_lite:    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10660', 'mrid', 'mrpass')
        #time.sleep(5)
        resultobj.wait_for_property("#pfjTableChart_1", 1, expire_time=60)
          
        """    "2. Go to Format tab    """
        """    "3. Click "Choropleth"    """

        ribbonobj.select_ribbon_item("Format", "Choropleth")
        lightgray_css="#pfjTableChart_1 div img[class^='layerTile'][src*='World_Light_Gray']"
        resultobj.wait_for_property(lightgray_css, 1, expire_time=25)
        
        """    4. Double click "Revenue", "Store,Country"    """
        
        
        metaobj.datatree_field_click('Revenue', 2,1)
        time.sleep(7)
        metaobj.datatree_field_click('Store,Country', 2,1)
        time.sleep(3)
        
        """    "5. Click "Background" dropdown > "World street map    """
        """    "6. Verify the map is updated    """
        
        ribbonobj.select_ribbon_item('Format','Background')
        chart_type_css="div[id^='BaseMapLayersPopup'][class*='bi-window active window'] img[src*='streets_map']"
        chart_elem = self.driver.find_element_by_css_selector(chart_type_css)
        elem1=(By.CSS_SELECTOR, chart_type_css)
        ribbonobj._validate_page(elem1)
        utillobj.default_left_click(object_locator=chart_elem)
        time.sleep(3)
        streetmap_css="#pfjTableChart_1 div img[class^='layerTile'][src*='World_Street_Map']"
        resultobj.wait_for_property(streetmap_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(streetmap_css, True, 'Step 6. Verify World Street Map displayed in preview')
        parentcss="pfjTableChart_1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 6.1")
        
        utillobj.verify_chart_color('pfjTableChart_1' ,'riser!s0!g33!mregion!', 'elf_green', 'Step 6.2: Verify green color') 
        utillobj.verify_chart_color('pfjTableChart_1' ,'riser!s0!g3!mregion!', 'sorbus_2', 'Step 6.3: Verify red color')
        
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step06'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    "7. Click "Run" and verify the map    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        
        streetmap_css="#jschart_HOLD_0 div img[class^='layerTile'][src*='World_Street_Map']"
        resultobj.wait_for_property(streetmap_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(streetmap_css, True, 'Step 7. Verify World Street Map displayed in preview')
        parentcss="jschart_HOLD_0"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 7.1")
        
        utillobj.verify_chart_color('jschart_HOLD_0' ,'riser!s0!g33!mregion!', 'elf_green', 'Step 7.2: Verify green color') 
        utillobj.verify_chart_color('jschart_HOLD_0' ,'riser!s0!g3!mregion!', 'sorbus_2', 'Step 7.3: Verify red color')
        
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step07'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    "8. Click "Live Preview" button to return to Live Preview    """
        """    "9. Click "Background" dropdown > "World Imagery"    """
        """    10. Verify the map is updated    """
        utillobj.switch_to_default_content(pause=2)
        
        live_elem=self.driver.find_element_by_css_selector("div[id^='showCu']")
        utillobj.default_left_click(object_locator=live_elem)
        
        ribbonobj.select_ribbon_item('Format','Background')
        
        
        chart_type_css="div[id^='BaseMapLayersPopup'][class*='bi-window active window'] img[src*='imagery_map']"
        chart_elem = self.driver.find_element_by_css_selector(chart_type_css)
        elem1=(By.CSS_SELECTOR, chart_type_css)
        ribbonobj._validate_page(elem1)
        utillobj.default_left_click(object_locator=chart_elem)
        time.sleep(3)
        map_css="#pfjTableChart_1 div img[class^='layerTile'][src*='World_Imagery']"
        resultobj.wait_for_property(map_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(map_css, True, 'Step 10. Verify World Imagery Map displayed in preview')
        parentcss="pfjTableChart_1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 10.1")
        utillobj.verify_chart_color(parentcss ,'riser!s0!g33!mregion!', 'elf_green', 'Step 10: Verify green color') 
        utillobj.verify_chart_color(parentcss ,'riser!s0!g3!mregion!', 'sorbus_2', 'Step 10: Verify red color')
        
        
        """    11. Click "Run" and verify the map    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        
        map_css="#jschart_HOLD_0 div img[class^='layerTile'][src*='World_Imagery']"
        resultobj.wait_for_property(map_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(map_css, True, 'Step 11. Verify World Street Map displayed in preview')
        parentcss="jschart_HOLD_0"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 11.1")
        
        utillobj.verify_chart_color(parentcss ,'riser!s0!g33!mregion!', 'elf_green', 'Step 11.2: Verify green color') 
        utillobj.verify_chart_color(parentcss ,'riser!s0!g3!mregion!', 'sorbus_2', 'Step 11.3: Verify red color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step11'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    12. Click "Live Preview" button to return to Live Preview    """
        """    13. Click "Proportional Symbol" in Chart Types group    """
        """    14. Click "Background" dropdown > "Open Street map"    """
        """    15. Verify the map is updated    """
        #utillobj.switch_to_default_content(pause=2)
        
        live_elem=self.driver.find_element_by_css_selector("div[id^='showCu']")
        utillobj.default_left_click(object_locator=live_elem)
        
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        
        defcss="#pfjTableChart_1 circle[class^='riser!s0!g33!mmarker!']"
        resultobj.wait_for_property(defcss, 1, expire_time=60)
        
        parentcss="pfjTableChart_1"
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 13.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 13.4 Verify map color')
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 13.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        
        ribbonobj.select_ribbon_item('Format','Background')
        chart_type_css="div[id^='BaseMapLayersPopup'][class*='bi-window active window'] img[src*='open_street_map']"
        chart_elem = self.driver.find_element_by_css_selector(chart_type_css)
        elem1=(By.CSS_SELECTOR, chart_type_css)
        ribbonobj._validate_page(elem1)
        utillobj.default_left_click(object_locator=chart_elem)
        time.sleep(3)
        map_css="#pfjTableChart_1 div img[class^='layerTile'][src*='openstreetmap']"
        resultobj.wait_for_property(map_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(map_css, True, 'Step 15. Verify World Open Street Map displayed in preview')
        parentcss="pfjTableChart_1"
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 15.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 15.4 Verify map color')
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 15.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        """    16. click "Run" and verify the map    """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        
        map_css="#jschart_HOLD_0 div img[class^='layerTile'][src*='openstreetmap']"
        resultobj.wait_for_property(map_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(map_css, True, 'Step 16. Verify World Open Street Map displayed in preview')
        parentcss="jschart_HOLD_0"
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 16.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 16.4 Verify map color')
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 16.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step16'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    17. Click "Live Preview" button to return to Live Preview   """
        """    18. Click "Background" dropdown > "National Geographic World Map"   """
        """    19. Verify the map is updated   """
        #utillobj.switch_to_default_content(pause=2)
        live_elem=self.driver.find_element_by_css_selector("div[id^='showCu']")
        utillobj.default_left_click(object_locator=live_elem)
         
        ribbonobj.select_ribbon_item('Format','Background')
        chart_type_css="div[id^='BaseMapLayersPopup'][class*='bi-window active window'] img[src*='national_geographic_map']"
        chart_elem = self.driver.find_element_by_css_selector(chart_type_css)
        elem1=(By.CSS_SELECTOR, chart_type_css)
        ribbonobj._validate_page(elem1)
        utillobj.default_left_click(object_locator=chart_elem)
        time.sleep(3)
        map_css="#pfjTableChart_1 div img[class^='layerTile'][src*='NatGeo_World_Map']"
        resultobj.wait_for_property(map_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(map_css, True, 'Step 19. Verify National Geographic World Map displayed in preview')
        parentcss="pfjTableChart_1"
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 19.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 19.4 Verify map color')
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 19.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        """    20. Click "Run" and verify the map    """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        
        map_css="#jschart_HOLD_0 div img[class^='layerTile'][src*='NatGeo_World_Map']"
        resultobj.wait_for_property(map_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(map_css, True, 'Step 20. Verify World Open Street Map displayed in preview')
        parentcss="jschart_HOLD_0"
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 20.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 20.4 Verify map color')
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 20.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step20'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    21. Click "Save" icon    """
        """    22. Enter Title "C2348656"    """
        """    23. Click "Save" and logout using API."""
        
        utillobj.switch_to_default_content(pause=2)
        
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """    24. Reopen the saved fex with API:    """
        """    25. Verify IA is launched, preserving the map    """
        """    26. Dismiss IA"""
        """    27. Log out :    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10660', mrid='mrid', mrpass='mrpass')
        time.sleep(3)
        map_css="#pfjTableChart_1 div img[class^='layerTile'][src*='NatGeo_World_Map']"
        resultobj.wait_for_property(map_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(map_css, True, 'Step 25. Verify National Geographic World Map displayed in preview')
        parentcss="pfjTableChart_1"
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 25.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 25.4 Verify map color')
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 25.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        
        
if __name__ == '__main__':
    unittest.main()
    
        
        
