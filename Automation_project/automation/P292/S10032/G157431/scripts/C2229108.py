'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229108
Test case Name =  Verify Map hyperlinks open in a new window at runtime
'''
import unittest, time
from common.lib import utillity, core_utility 
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map

class C2229108_TestClass(BaseTestCase):

    def test_C2229108(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        utillobj.infoassist_api_login('chart','jsonmaps/statepop','P292/S10032', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1 text[class*='xaxisOrdinal']", 5, 190)
        
        '''    2. Add fields STATE, POPULATION    '''
        metaobj.datatree_field_click('STATE', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('POPULATION', 2, 1)
        time.sleep(4)
        
        ribbonobj.select_ribbon_item("Format", "Other")
        time.sleep(4)
        
        
        '''    3. Select Format tab    '''
        '''    4. Select "Other" > "Map"    '''
        '''    5. Select "Leaflet Choropleth" > OK (Keep default "United States" Territory)    '''
        
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_choropleth', 1)
        
        time.sleep(3)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'United States of America')
        time.sleep(3)
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(3)
        
        '''    6. Select "State name" from Geographic Role dropdown > OK    '''
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        
        '''    7. Verify the map is updated    '''
        
        parentcss="pfjTableChart_1"
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g1!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['POPULATION', '2.5M', '39.9M', '77.2M', '114.6M', '152M'], "Step 7.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'persian_red', 'Step 7.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g4!mstate!", 'elf_green', 'Step 7.2 Verify map color')
                              
        '''    8. Click "Run"    '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        resultobj.wait_for_property('#jschart_HOLD_0', 1,expire_time=60)
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['POPULATION', '3.2M', '49.7M', '96.2M', '142.7M', '189.2M'], "Step 8.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'persian_red', 'Step 8.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g4!mstate!", 'elf_green', 'Step 8.2 Verify map color')
        utillobj.switch_to_default_content(pause=3) 
        
        '''    9. Click each hyperlink at the bottom of the Map - "Leaflet", "Information Builders"    '''
        '''    10. Verify each hyperlink open in a new window at runtime, when using defaut Single tab output location    '''
        '''    11. Close output windows    '''
        old_windows=self.driver.window_handles
        old_set=set(old_windows)
        utillobj.switch_to_frame(1)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#jschart_HOLD_0 a[href*='leafletjs']").click()
        time.sleep(6)
        utillobj.switch_to_default_content(pause=3)
        new_windows=self.driver.window_handles
        new_set=set(new_windows)
        if new_set > old_set:
            winstatus=True
            core_utilobj.switch_to_new_window()
            time.sleep(8)
            utillobj.asequal(winstatus,True, 'Step 9.2. Verify new window open')
            current_url=self.driver.current_url
            if 'leafletjs' in current_url:
                status=True
            else:
                status=False

            utillobj.asequal(status,True,'Step 9.3. Leafletjs link is open')
            time.sleep(8)
        else:
            winstatus=False
            utillobj.asequal(winstatus,True, 'Step 9.4. Verify new window open')
        
        '''ibi link test '''
        core_utilobj.switch_to_previous_window()
        old_windows=self.driver.window_handles
        old_set=set(old_windows)
        utillobj.switch_to_frame(1)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#jschart_HOLD_0 a[href*='tibco']").click()
        time.sleep(6)
        utillobj.switch_to_default_content(pause=3)
        new_windows=self.driver.window_handles
        new_set=set(new_windows)
        if new_set > old_set:
            winstatus=True
            core_utilobj.switch_to_new_window()
            time.sleep(8)
            utillobj.asequal(winstatus,True, 'Step 9.5. Verify new window open')
            current_url=self.driver.current_url
            
            if 'tibco' in current_url:
                status=True
            else:
                status=False

            utillobj.asequal(status,True,'Step 9.6. tibco link is open')
            time.sleep(8)
        else:
            winstatus=False
            utillobj.asequal(winstatus,True, 'Step 9.7. Verify new window open')
        core_utilobj.switch_to_previous_window()
        time.sleep(8)
        
        '''    12. Select output location 'Single Window' from output shortcut in status bar    '''  
        ia_ribbonobj.select_report_output_window('Single Window')
        time.sleep(5)
        old_windows=self.driver.window_handles
        old_set=set(old_windows) 
        
        '''    13. Click Run    '''
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        new_windows=self.driver.window_handles
        new_set=set(new_windows)
        
        '''    14. Verify Map opens in a new window    '''
        if new_set > old_set:
            winstatus=True
            core_utilobj.switch_to_new_window()
            time.sleep(8)
            
        else:
            winstatus=False
        utillobj.asequal(winstatus,True, 'Step 14.1. Verify new window open')
        
        '''    15. Click each hyperlink at the bottom of the Map - Leaflet and IBI    '''        
        '''    16. Verify each hyperlink is opened a new window, not in the Map window    '''
        '''    17. Dismiss the output windows    '''
        
        old_windows=self.driver.window_handles
        old_set=set(old_windows)
        time.sleep(2)
        self.driver.find_element_by_css_selector("#jschart_HOLD_0 a[href*='leafletjs']").click()
        time.sleep(6)
        
        new_windows=self.driver.window_handles
        new_set=set(new_windows)
        if new_set > old_set:
            core_utilobj.switch_to_new_window()
            time.sleep(8)
            current_url=self.driver.current_url
            
            if 'leafletjs' in current_url:
                status=True
            else:
                status=False

            utillobj.asequal(status,True,'Step 16.1. Leafletjs link is open')
            time.sleep(8)
        else:
            winstatus=False
            utillobj.asequal(winstatus,True, 'Step 16.2. Verify new window open')
        
        '''ibi link test '''
        core_utilobj.switch_to_previous_window()
        old_windows=self.driver.window_handles
        old_set=set(old_windows)
        
        self.driver.find_element_by_css_selector("#jschart_HOLD_0 a[href*='tibco']").click()
        time.sleep(6)
        
        new_windows=self.driver.window_handles
        new_set=set(new_windows)
        if new_set > old_set:
            winstatus=True
            core_utilobj.switch_to_new_window()
            time.sleep(8)
            utillobj.asequal(winstatus,True, 'Step 16.3: Verify new window open')
            current_url=self.driver.current_url
            
            if 'tibco' in current_url:
                status=True
            else:
                status=False
            time.sleep(8)
        else:
            winstatus=False
            utillobj.asequal(winstatus,True, 'Step 16.4: Verify new window open')
        core_utilobj.switch_to_previous_window()
        time.sleep(8)
        core_utilobj.switch_to_previous_window()
        utillobj.switch_to_default_content()
        
        '''    18. Dismiss the map window    '''
        '''    19. Logout:    '''
      
if __name__ == '__main__':
    unittest.main()