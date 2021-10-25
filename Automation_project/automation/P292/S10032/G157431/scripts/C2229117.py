'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229117
Test case Name =  Verify Bubble Map with Filter
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map, ia_styling
from common.lib import utillity 
import time,datetime
from common.lib.basetestcase import BaseTestCase



class C2229117_TestClass(BaseTestCase):

    def test_C2229117(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229117"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
#         utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','jsonmaps/us','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
         
        '''    2. 2. Double click "STATE_NAME","RANDOM_NUMBER"..    '''
        '''    3. Verify the following chart is displayed.    '''
        
        metaobj.datatree_field_click('STATE_NAME', 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'STATE_NAME', expire_time=30)
        metaobj.datatree_field_click('RANDOM_NUMBER', 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'RANDOM_NUMBER', expire_time=30)
        
        xaxis_value="STATE_NAME"
        yaxis_value="RANDOM_NUMBER"
        parentcss="pfjTableChart_1"
        resultobj.verify_xaxis_title(parentcss, xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title(parentcss, yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list_cr=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
        expected_xval_list_ff=['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
        expected_yval_list=['0', '200', '400', '600', '800', '1,000', '1,200']
        if browser_type=="Chrome":
            resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list_cr, expected_yval_list, "Step 02:c(iii):Verify XY labels")
        else:
            resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list_ff, expected_yval_list, "Step 02:c(iii):Verify XY labels")
        resultobj.verify_number_of_riser(parentcss, 1, 51, 'Step 02.d: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mbar", "bar_blue", "Step 02.e: Verify first bar color")
        time.sleep(5)
        
        '''    '4. Select "Format" > "Other" > "Map".    '''
        '''    5. Select "Leaflet Bubble"    '''
        '''    '6. Set "Territory" = "World" > OK    '''
        
        ribbonobj.select_ribbon_item("Format", "Other")
         
        time.sleep(4)
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_bubblemap', 1)
         
        time.sleep(3)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'United States of America')
        time.sleep(3)
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(3)
        

        
        '''    '7. Set "Geographic Role" = "Country_name">OK    '''
        '''    '8. Click "OK".    '''
        
 
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
         
        
        '''    9. Verify the following map is displayed.    '''
       
        parentcss="pfjTableChart_1"
        
        expected_label_list=['RANDOM_NUMBER']
        msg="Step 9.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['RANDOM_NUMBER']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 9.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g19!mstate!", 'bar_blue', 'Step 9.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'bar_blue', 'Step 9.3b Verify map color')
        
        
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step09'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        '''    10. Drag "STATE_NAME" to the Filter pane.    '''
        
        #metaobj.drag_drop_data_tree_items_to_query_tree('STATE_NAME', 1, 'Color', 0)
        
        metaobj.datatree_field_click('STATE_NAME', 1, 1, 'Filter')
        time.sleep(1)
        
        '''    11. Verify "Create a filtering condition" window is displayed.    '''
        '''    12. Double Click "<Value>"    '''
        '''    13. Click "Get Values" > "All"    '''
        '''    14. Double click "Alaska","Hawaii","Texas"    '''
        '''    15. Click "OK" > OK    '''
        
        ia_ribbonobj.create_constant_filter_condition('All',['Alaska','Hawaii','Texas'])
        
        time.sleep(8)
        
        '''    16. Verify the filter is displayed in the Filter pane.    '''
        '''    17. Verify the following map is displayed.    '''
        
        filtervalue="STATE_NAME Equal to Alaska or Hawaii or Texas"
        metaobj.verify_filter_pane_field(filtervalue, 1, 'Step 16. Verify filter is displayed in filter pane')
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g0!mstate!']", 1, expire_time=20)
        
        utillobj.verify_object_visible("#pfjTableChart_1 path[class^='riser!s0!g19!mstate!']", False, 'Step 17. Verify Filtered map' )
        
        expected_label_list=['RANDOM_NUMBER']
        msg="Step 17.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['RANDOM_NUMBER']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 17.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g0!mstate!", 'bar_blue', 'Step 17.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'bar_blue', 'Step 17.3b Verify map color')
        
        '''    18. Click "Run".    '''
        '''    19. Verify the following map is displayed.    '''
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        resultobj.wait_for_property("#jschart_HOLD_0 path[class^='riser!s0!g2!mstate!']", 1,expire_time=60)   
        
        expected_label_list=['RANDOM_NUMBER']
        msg="Step 19.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['RANDOM_NUMBER']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 19.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g0!mstate!", 'bar_blue', 'Step 19.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'bar_blue', 'Step 19.3b Verify map color')
             
        
        '''    20. Click "IA" > "Save" > "C2229116" > "Save".    '''
        '''    21. Logout:    '''
                
        utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        utillobj.infoassist_api_logout()
         
        
        '''    22. Reopen fex using IA API:    '''
        '''    23. Verify the following chart is displayed.    '''
        '''    24. Logout:    '''
        
        
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g2!mstate!']", 1,expire_time=60)  
        parentcss="pfjTableChart_1"
        
        expected_label_list=['RANDOM_NUMBER']
        msg="Step 23.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['RANDOM_NUMBER']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 23.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g0!mstate!", 'bar_blue', 'Step 23.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'bar_blue', 'Step 23.3b Verify map color')
        
       

if __name__ == '__main__':
    unittest.main()
    