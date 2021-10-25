'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2356219
Test case Name =  Verify lasso filter options on Leaflet map
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase

class C2356219_TestClass(BaseTestCase):

    def test_C2356219(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2356219"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        '''    '2. Maximize Visualization window    '''
#         utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10660', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
         
        '''    '3. Click "Change" dropdown > "Map"    '''
        '''    '4. Select "Leaflet Bubble" > OK (Keep already selected "United States" Territory)    '''
        
        ribbonobj.change_chart_type('map')
        time.sleep(5)
        ribbonobj.select_map('bubble', teritory='United States of America', btn_click='ok')
        

        '''    5. Double click "Store,State,Province"    '''
        
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        time.sleep(4)
        
        '''    6. Select "state_name" from Geographic Role dropdown > OK   '''

        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        
        '''    '7. Double click "Gross Profit"    '''
        
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(4)
        
        '''    '8. Click "Pan" in the map canvas    '''
        pan_css='#MAINTABLE_wbody1 .leaflet-top.leaflet-right button[class$="leaflet-control"]'
        
        pan_ele=self.driver.find_element_by_css_selector(pan_css)
        
        utillobj.click_on_screen(pan_ele, coordinate_type='middle', click_type=0)
        
        '''    '9. Lasso "Maine", "New York", "Massachusetts" bubbles (as shown in the screenshot)    '''
        '''    10. Verify the lasso menu    '''
        '''    11. Select "Exclude from    '''
        time.sleep(4) 
        resultobj.create_lasso('MAINTABLE_wbody1_f','path','riser!s0!g41!mstate!',target_tag='path',target_riser='riser!s0!g50!mstate!',offsetx='-45',offsety='100', ty_offset=30)
        time.sleep(5)
        
        resultobj.select_or_verify_lasso_filter(verify=['3 items selected', 'Filter Chart', 'Exclude from Chart', 'Group Store,State,Province Selection'],msg='Step 10: Verify Lasso menu')
        
        resultobj.select_or_verify_lasso_filter(select='Exclude from Chart',msg='Step 11: Select Exclude from')
        
        menu_css="div[id^='ibi'][class=tdgchart-tooltip] .tdgchart-tooltip-pad"
        utillobj.wait_for_object_not_visible(menu_css, 30, 'Step 11. Wait for Exclude menu to close')
        '''    12. Verify the map is updated    '''
        old_riser="#TableChart_1 path[class^='riser!s0!g41!mstate!']"
        utillobj.wait_for_object_not_visible(old_riser, 30, 'Step 12. Verify map is updated with old riser excluded')
        time.sleep(8)
       
                
        parentcss="TableChart_1"
        resultobj.wait_for_property("#TableChart_1 path[class^='riser!s0!g25!mstate!']", 1, expire_time=50)
        
        expected_label_list=['Gross Profit']
        msg="Step 12.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Gross Profit']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 12.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'bar_blue', 'Step 12.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mstate!", 'bar_blue', 'Step 12.3b Verify map color')
        
        
#         img1=self.driver.find_element_by_css_selector("#resultArea #TableChart_1")
#         utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step12'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        '''    13. Click "Run"    '''
        '''  14. Verify the map runs in a new window '''
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_window(1, pause=3)
        
        parentcss="MAINTABLE_wbody1"
        resultobj.wait_for_property("#MAINTABLE_wbody1 path[class^='riser!s0!g25!mstate!']", 1,expire_time=60)
        
        expected_label_list=['Gross Profit']
        msg="Step 14.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Gross Profit']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 14.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'bar_blue', 'Step 14.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g65!mstate!", 'bar_blue', 'Step 14.3b Verify map color')
        
        '''    15. Click "Pan" in the map canvas    '''
        time.sleep(2)
        pan_css='#MAINTABLE_wbody1 .leaflet-top.leaflet-right button[class$="leaflet-control"]'
        
        pan_ele=self.driver.find_element_by_css_selector(pan_css)
        
        utillobj.click_on_screen(pan_ele, coordinate_type='middle', click_type=0)
        time.sleep(3)

        '''    16. Lasso all bubbles except Alaska and Hawaii    '''
        '''    17. Select "Filter Chart"    '''
        resultobj.create_lasso("MAINTABLE_wbody1",'path','riser!s0!g69!mstate!',target_tag='path',target_riser='riser!s0!g19!mstate!',offsetx='1000',offsety='260',tx_offset=280,ty_offset=-4)
      
        
        resultobj.select_or_verify_lasso_filter(select='Filter Chart',msg='Step 17: Select Filter Chart')
        menu_css="div[id^='ibi'][class=tdgchart-tooltip] .tdgchart-tooltip-pad"
        utillobj.wait_for_object_not_visible(menu_css, 30, 'Step 17. Wait for Filter menu to close')
        
        
        '''    18. Verify the map is updated    '''
        '''    19. Dismiss the run window    '''
        
        resultobj.wait_for_property("#MAINTABLE_wbody1 path[class^='riser!s']", 31, expire_time=45)
        time.sleep(5)
        
        tot_riser=self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1 path[class^='riser!s']")
        print ('total no of riser', len(tot_riser))
        utillobj.asequal(31,len(tot_riser),'Step 18. Verify the map updated (no of risers displayed after filtering)')
        
        expected_label_list=['Gross Profit']
        msg="Step 18.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Gross Profit']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 18.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'bar_blue', 'Step 18.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'bar_blue', 'Step 18.3b Verify map color')
        
        self.driver.close()
        
        
        '''    20. Click Save in the toolbar > Save as "C2356219" > Click Save    '''
        '''    21. Logout using API    '''
        utillobj.switch_to_window(0, pause=3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
         
        
        '''    22. Restored fex using API    '''
        '''    23. Verify the map is restored    '''
        '''    24. Logout using API    '''
          
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10660', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        resultobj.wait_for_property("#TableChart_1 path[class^='riser!s0!g1!mstate!']", 1,expire_time=45)  
        
        
        expected_label_list=['Gross Profit']
        msg="Step 24.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Gross Profit']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 24.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'bar_blue', 'Step 24.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'bar_blue', 'Step 24.3b Verify map color')
        
if __name__ == '__main__':
    unittest.main()