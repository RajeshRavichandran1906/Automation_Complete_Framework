'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348655
Test case Name =  Verify defining Latitude with Longitude associated coordinate 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
import pyautogui
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2348655_TestClass(BaseTestCase):

    def test_C2348655(self):
    
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        georoledlg="body[id=wndApp] div[id^='QbDialog']"
        georolebox="div[id^='QbDialog'] div[id$='oldGeoRoleBox']"
        georolebtn="div[id^='QbDialog'] div[id$='GeoRoleBox'][style*='left'] div[id^='BiButton']"
        geoformat="div[id^='QbDialog'] div[id$='geoFormatBox']"
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2348655"
        

         
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','places/NOPLACES_XY','P292/S10660', 'mrid', 'mrpass')
        #time.sleep(5)
        defcss="#TableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=120)
           
        """    2. Go to Format tab    """
        """    3. Click "Proportinal Symbol" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=30)
        time.sleep(9)
          
        """    "4. Right click "LATITUDE" > "Map As" > "Latitude"    """
        """    "5. Verify the georole dialog is prompted, with predefined values    """
      
        metaobj.datatree_field_click('LATITUDE', 1, 1, 'Map As', 'Latitude...')
         
         
        resultobj.wait_for_property(georoledlg, 1, expire_time=60)
        utillobj.verify_object_visible(georoledlg, True, "Step 5.1 Verify Georole dialog is open")
        utillobj.verify_object_visible(georolebox, True, "Step 5.2 Verify Georolebox")
        utillobj.verify_object_visible(geoformat, True, "Step 5.3 Verify Georoleformat")
         
        """    "6. Click "Associated Coordinate" dropdown > "LONGITUDE"    """
        """    "7. Select OK    """
         
        wfmapobj.set_geo_role(assoc_cord='LONGITUDE', btn_click='Ok')
        utillobj.verify_object_visible("#geoRoleOkBtn", False, 'Step 7. Wait for Georole Dialog to close')
        time.sleep(4)
         
        """    "8. Verify both fields have GeoRole icons    """
        """    "9. Hover over "LATITUDE"    """
        """    10. Verify "Geographic Role: LATITUDE"    """
        """    11. Hover over "LONGITUDE"    """
        """    12. Verify "Geographic Role: LONGITUDE"    """
 
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, element, 'LATITUDE')
        utillobj.verify_object_visible("div[id^='QbMetaDataTree'] img[src*='chart_geo_dimension_16']", True, 'Step 8.1 Verify the icon for LATITUDE')
          
        utillity.UtillityMethods.set_text_field_using_actionchains(self, element, 'LONGITUDE')
        utillobj.verify_object_visible("div[id^='QbMetaDataTree'] img[src*='chart_geo_dimension_16']", True, 'Step 8.1 Verify the icon for LONGITUDE')
 
        expected_list=['Segment: NOPLACES_XY', 'Name: LATITUDE', 'Alias: LATITUDE', 'Title: LATITUDE', 'Description: LATITUDE', 'Format: D12.7S', 'Geographic Role: LATITUDE']
          
        metaobj.verify_datatree_tooltip('LATITUDE', 1, expected_list, 'Step 10. Verify Geographic Role for LATITUDE')
         
        expected_list=['Segment: NOPLACES_XY', 'Name: LONGITUDE', 'Alias: LONGITUDE', 'Title: LONGITUDE', 'Description: LONGITUDE', 'Format: D12.7S', 'Geographic Role: LONGITUDE']
         
        metaobj.verify_datatree_tooltip('LONGITUDE', 1, expected_list, 'Step 12. Verify Geographic Role for LONGITUDE')
        
        
        """    13. Verify a Define field is created "LATITUDE_LONGITUDE_POINT"    """
        """    14. Drag "LATITUDE" into "Layer" bucket    """
        """    15. Verify the map is updated    """
        
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        element.click()
        utillity.UtillityMethods.set_text_field_using_actionchains(self, element, '', keyboard_type=True)
        element.click()
        
        pyautogui.press('space', pause=3)
        pyautogui.press('backspace', pause=5)
        
        metaobj.verify_data_pane_field('Dimensions', 'LATITUDE_LONGITUDE_POINT', 3, 'Step 13. Verify the Define field is created LATITUDE_LONGITUDE_POINT')
        
        element = self.driver.find_element_by_id("iaMetaDataBrowser").find_element_by_id("metaDataSearchTxtFld")
        utillity.UtillityMethods.set_text_field_using_actionchains(self, element, 'LATITUDE_LONGITUDE_POINT')
        utillobj.verify_object_visible("div[id^='QbMetaDataTree'] img[src*='chart_user_dimension_edit_16']", True, 'Step 13.1 Verify the icon for LATITUDE_LONGITUDE_POINT')
        
        metaobj.drag_drop_data_tree_items_to_query_tree('LATITUDE', 1, 'Layer', 0, ty_offset=5)
        #metaobj.datatree_field_click('LATITUDE', 1, 1, 'Add To Query', 'Layer')
        
        defcss="#pfjTableChart_1 circle[class='riser!s0!g13!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
         
        parentcss="pfjTableChart_1"
         
        utillobj.verify_chart_color(parentcss, "riser!s0!g13!mmarker!", 'bar_blue', 'Step 15.1a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g447!mmarker!", 'bar_blue', 'Step 15.1b Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g188!mmarker!", 'bar_blue', 'Step 15.1b Verify map color')
         
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step15'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    16. Double click "POPULATION"    """
        """    17. Verify the map is updated    """
        
        metaobj.datatree_field_click('POPULATION', 2, 1)
        
        defcss="#pfjTableChart_1 circle[class='riser!s0!g30!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        
        parentcss="pfjTableChart_1"
        expected_label_list=['POPULATION']
        msg="Step 17.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['POPULATION']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 17.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g30!mmarker!", 'bar_blue', 'Step 17.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g213!mmarker!", 'bar_blue', 'Step 17.3b Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g277!mmarker!", 'bar_blue', 'Step 17.3b Verify map color')
        
        """    18. Click "Run"    """
        """    19. Verify the map is correct at runtime    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#jschart_HOLD_0 circle[class='riser!s0!g30!mmarker!']", 1)
        
        
        expected_label_list=['POPULATION']
        msg="Step 19.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['POPULATION']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 19.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g30!mmarker!", 'bar_blue', 'Step 19.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g213!mmarker!", 'bar_blue', 'Step 19.3b Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g277!mmarker!", 'bar_blue', 'Step 19.3b Verify map color')
        
        """    20. Click "Save" icon    """
        """    21. Enter Title "C2348655"    """
        """    22. Click "Save" and dismiss IA window    """

        utillobj.switch_to_default_content(pause=3)
 
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        """    23. Run the saved fex.    """
        """    24. Verify the map runs in a new window    """
        """    25. Dismiss the map window    """
          
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10660_esrimap_1', mrid='mrid', mrpass='mrpass')
        
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#jschart_HOLD_0 circle[class='riser!s0!g30!mmarker!']", 1)
        
        
        expected_label_list=['POPULATION']
        msg="Step 24.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['POPULATION']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 24.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g30!mmarker!", 'bar_blue', 'Step 24.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g213!mmarker!", 'bar_blue', 'Step 24.3b Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g277!mmarker!", 'bar_blue', 'Step 24.3b Verify map color')
        
        """    26. Reopen the fex using the API code:    """
        """    27. Verify IA is launched, preserving the map   """
        """    28. Dismiss IA window   """
        """    29. Log out :   """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10660', mrid='mrid', mrpass='mrpass')
        time.sleep(3)
        
        defcss="#pfjTableChart_1 circle[class='riser!s0!g30!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        
        parentcss="pfjTableChart_1"
        expected_label_list=['POPULATION']
        msg="Step 27.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['POPULATION']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 27.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g30!mmarker!", 'bar_blue', 'Step 27.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g213!mmarker!", 'bar_blue', 'Step 27.3b Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g277!mmarker!", 'bar_blue', 'Step 27.3b Verify map color')
        
        
if __name__ == '__main__':
    unittest.main()
    
        
        