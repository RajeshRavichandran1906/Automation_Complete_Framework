'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229109
Test case Name =  Verify Map hyperlinks open in a new window at runtime
'''
import unittest,time
from common.lib import utillity ,core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon,wf_map

class C2229109_TestClass(BaseTestCase):

    def test_C2229109(self):
        
        '''    TESTCASE OBJECTS    '''
        wfmapobj=wf_map.Wf_Map(self.driver)
        core_metaobj = CoreMetaData(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229109"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 text[class*='xaxisOrdinal']", 5, 190)
        
        '''    2. Double click "Store,Country","Revenue"    '''
        core_metaobj.double_click_on_data_filed('Store,Country', field_position=1)
        query_pane ='#queryTreeColumn'
        utillobj.synchronize_with_visble_text(query_pane, 'Store,Country', 30)
        core_metaobj.double_click_on_data_filed('Revenue')
        utillobj.synchronize_with_visble_text(query_pane, 'Revenue', 30)
        
        '''    3. Select Format tab    '''
        '''    4. Select "Other" > "Map"    '''
        '''    5. Select "Leaflet Choropleth"    '''
        '''    6. Set "Territory" = "World" > OK    '''
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
        
        '''   7. Select "country_name" from Geographic Role dropdown > OK    '''
        wfmapobj.set_location_geo_role(role_name='country_name (Afghanistan, Aland Islands, Albania)', btn_click='Ok')
        
        '''    7. Verify the map is updated    '''
        parentcss="pfjTableChart_1"
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g33!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 7.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mstate!", 'sorbus_2', 'Step 7.2: Verify a color in map')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 7.3: Verify different color in map')
                                 
        '''    '8. Click "Revenue" in the Query Pane    '''
        metaobj.querytree_field_click('Revenue', 1, 0)
        time.sleep(3)
        
        '''    '9. Click "Drill Down" in the Field tab    '''
        '''    10. Select "Web Page" radio button    '''
        '''    11. Type URL http://www.google.com > OK    '''
        ribbonobj.select_ribbon_item("Field", "drilldown")
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.google.com", click_ok='yes')
        time.sleep(4)
        
        '''    12. Click Run    '''
        '''    13. Click on a country in the map    '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        resultobj.wait_for_property('#jschart_HOLD_0', 1,expire_time=60)
        
        old_windows=self.driver.window_handles
        old_set=set(old_windows)
        
        country_css="#jschart_HOLD_0 path[class^='riser!s0!g1!mstate!']"
        country_ele=self.driver.find_element_by_css_selector(country_css)
        utillobj.click_on_screen(country_ele, coordinate_type='middle', click_type=0)
        time.sleep(8)
        new_windows=self.driver.window_handles
        new_set=set(new_windows)
        
        '''    14. Verify Google page opens in a new window    '''
        '''    15. Dismiss the Google page window    '''
        
        if new_set > old_set:
            winstatus=True
            core_utilobj.switch_to_new_window()
            time.sleep(8)
            utillobj.asequal(winstatus,True, 'Step 14.1: Verify new window open')
            current_url=self.driver.current_url
            
            if 'google' in current_url:
                status=True
            else:
                status=False

            utillobj.asequal(status,True,'Step 14.2: Verify Google link is open')
            time.sleep(8)
        else:
            winstatus=False
            utillobj.asequal(winstatus,True, 'Step 14.1: Verify new window open')
        
        '''    16. Click "Save" icon    '''
        '''    17. Save as "C2229109"    '''
        '''    18. Click "Save" and dismiss IA    '''
        core_utilobj.switch_to_previous_window()
        utillobj.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        '''    19. Logout:    '''
        '''    20. Reopen fex using IA API:    '''
        '''    21. Verify IA is launched, preserving the map    '''
        '''    22. Logout:    '''
        utillobj.infoassist_api_logout()
        
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        parentcss="pfjTableChart_1"
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g33!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 21.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mstate!", 'sorbus_2', 'Step 21.2: Verify a color in map')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 21.3: Verify different color in map')
        utillobj.infoassist_api_logout()

if __name__ == '__main__':
    unittest.main()