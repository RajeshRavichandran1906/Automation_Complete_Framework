'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229114
Test case Name =  Verify Choropleth Map - Tiles are cleared when unchecked
'''
import unittest, time
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map

class C2229114_TestClass(BaseTestCase):

    def test_C2229114(self):
        
        '''    TESTCASE OBJECTS    '''
        wfmapobj=wf_map.Wf_Map(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
               
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229114"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
         
        '''    2. Select "Format" tab > "Other" > "Map"    '''
        '''    3. Select "Leaflet Choropleth"    '''
        '''    4. Set "Territory" = "World".    '''
        '''    5. Click "OK"    '''
         
        ribbonobj.select_ribbon_item("Format", "Other")
         
        time.sleep(4)
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_choropleth', 1)
         
        time.sleep(3)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'World')
        time.sleep(3)
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(3)
        
        
        '''    '6. Double click "Store,Country".    '''
        metaobj.datatree_field_click('Store,Country', 2, 1)
        query_pane ='#queryTreeColumn'
        utillobj.synchronize_with_visble_text(query_pane, 'Store,Country', 30)
        
        '''    '7. Set "Geographic Role" = "Country_name"    '''
        '''    '8. Click "OK".    '''
 
        wfmapobj.set_location_geo_role(role_name='country_name (Afghanistan, Aland Islands, Albania)', btn_click='Ok')
         
        '''    '9. Double click "Revenue".    '''
        '''    10. Verify the following map is displayed.    '''
        metaobj.datatree_field_click('Revenue', 2, 1)
        utillobj.synchronize_with_visble_text(query_pane, 'Revenue', 30)
        
        parentcss="pfjTableChart_1"
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g3!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 10.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mstate!", 'sorbus_2', 'Step 10.2: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 10.3: Verify map color')
        
        '''    11. Click "Run".    '''
        '''    12. Verify the following map is displayed.    '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        resultobj.wait_for_property("#jschart_HOLD_0 path[class^='riser!s0!g3!mstate!']", 1,expire_time=60)
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 12.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mstate!", 'sorbus_2', 'Step 12.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 12.3 Verify map color')
        
        '''    13. Hover over the Tile icon (TOC)    '''
        '''    14. Uncheck "World" check box.    '''
        '''    15. Verify the following map is displayed.    '''
        
        ''' code for TOC, check /uncheck'''
        tile_css="#jschart_HOLD_0 a[class='leaflet-control-layers-toggle']"
        tile_ele=self.driver.find_element_by_css_selector(tile_css)
        
        core_utils.left_click(tile_ele)
#         utillobj.click_on_screen(tile_ele, coordinate_type='middle', click_type=3)
        
        span_css="#jschart_HOLD_0 div[class='leaflet-control-layers-overlays'] label span"
        resultobj.wait_for_property(span_css, expected_number=1, expire_time=10)
        
        span_ele=self.driver.find_element_by_css_selector(span_css)
        core_utils.left_click(span_ele)
#         utillobj.click_on_screen(span_ele, coordinate_type='middle', click_type=0)
        
        time.sleep(5)
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 15.1")
        
        ele1="#jschart_HOLD_0 path[class^='riser!s0!g3!mstate!']"
        ele2="#jschart_HOLD_0 path[class^='riser!s0!g33!mstate!']"
        utillobj.verify_object_visible(ele1, False, 'Step 15.2 Verify Map after Unchecking World checkbox from Tile')
        utillobj.verify_object_visible(ele2, False, 'Step 15.3 Verify Map after Unchecking World checkbox from Tile')
        
        
        '''    16. Click "IA" > "Save" > "C2229114" > "Save".    '''
        '''    17. Logout:    '''   
        utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
        
        '''    18. Reopen fex using IA API:    '''
        '''    19. Verify the following map is displayed.'''    
        '''    20. Logout:    '''  
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        parentcss="pfjTableChart_1"
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g3!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 12.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mstate!", 'sorbus_2', 'Step 12.2: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 12.3: Verify map color')
        
if __name__ == '__main__':
    unittest.main()