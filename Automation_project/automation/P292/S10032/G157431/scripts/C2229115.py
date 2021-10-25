'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229115
Test case Name =  Verify Choropleth Map with filter is working properly
'''
import unittest, time
from common.lib import utillity 
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData
from common.lib.core_utility import CoreUtillityMethods
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map

class C2229115_TestClass(BaseTestCase):

    def test_C2229115(self):
        
        '''    TESTCASE OBJECTS    '''
        wfmapobj=wf_map.Wf_Map(self.driver)
        core_metaobj = CoreMetaData(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229115"
        
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
        ok_btn_ele  = self.driver.find_element_by_css_selector("div[id='qbSelectChartTypeDlgOkBtn']")
        CoreUtillityMethods.left_click(self, ok_btn_ele)
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
        time.sleep(12)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 10.01:")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mstate!", 'sorbus_2', 'Step 10.02: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 10.03: Verify map color')
        
        '''    11. Drag "Store,Country" to the Filter pane.    '''
        core_metaobj.collapse_data_field_section('Filters and Variables')
        metaobj.drag_drop_data_tree_items_to_filter("Store,Country", 1)
        time.sleep(1)
        
        '''    12. Double click "<Value>"    '''
        '''    13. Click "Get Values" > "All"    '''
        '''    14. Double click "Argentina" , "Australia", "Canada", "China"    '''
        '''    15. Click "OK" > OK    ''' 
        ia_ribbonobj.create_constant_filter_condition('All',['Argentina','Australia','Canada','China'])
        time.sleep(8)
    
        '''  16. Verify the following map is displayed.  '''
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '12.8M', '25.6M', '38.4M', '51.1M'], "Step 16.01:")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'elf_green', 'Step 16.02: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'persian_red', 'Step 16.03: Verify map color')
        
        '''    17. Click "Run".    '''
        '''    18. Verify the following map is displayed.    '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        resultobj.wait_for_property("#jschart_HOLD_0 path[class^='riser!s0!g1!mstate!']", 1,expire_time=60)
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '12.8M', '25.6M', '38.4M', '51.1M'], "Step 18.01:")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'elf_green', 'Step 18.02: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'persian_red', 'Step 18.03: Verify map color')
        
        '''    19. Click "IA" > "Save" > "C2229115" > "Save".    '''
        '''    20. Logout:    '''
        CoreUtillityMethods.switch_to_default_content(self)
        ia_ribbonobj.select_ia_application_menu_item('save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        '''    21. Reopen fex using IA API:    '''
        '''    22. Verify the following map is displayed.'''    
        '''    23. Logout:    '''
  
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        parentcss="pfjTableChart_1"
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g1!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '12.8M', '25.6M', '38.4M', '51.1M'], "Step 22.01")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'elf_green', 'Step 22.02: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'persian_red', 'Step 22.03: Verify map color')
        
if __name__ == '__main__':
    unittest.main()