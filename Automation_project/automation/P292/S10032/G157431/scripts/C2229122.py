'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229122
Test case Name =  Verify Show Data 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity
from common.lib import core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous


class C2229122_TestClass(BaseTestCase):

    def test_C2229122(self):
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229122"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        parent_css='#TableChart_1'
        utillobj.synchronize_until_element_is_visible(parent_css, ribbonobj.chart_long_timesleep)
         
        '''    2. Click "Change" dropdown > "Map"    '''
        '''    3. Select "Leaflet Choropleth" > OK (Keep default Territory "United States" selected)    '''
        ribbonobj.change_chart_type('map')
        utillobj.synchronize_until_element_is_visible("div[id^='QbDialog']", ribbonobj.home_page_long_timesleep)
        ribbonobj.select_map('choropleth', teritory='United States of America', btn_click='ok')
        utillobj.synchronize_until_element_disappear("div[id^='QbDialog']", ribbonobj.home_page_long_timesleep)
        
        '''    4. Double click "Store,State,Province"    '''
        
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        parent_css="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(parent_css, "Store,State,Province", ribbonobj.home_page_long_timesleep)
         
        '''    5. Select "state_name" from Geographic Role dropdown > OK   '''
        
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        
        '''    6. Double click "Gross Profit"    '''
        
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        
        '''    6.1. Verify the map is updated    '''
        
        parentcss="TableChart_1"
        utillobj.synchronize_with_number_of_element("#TableChart_1 path[class^='riser!s0!g1!mstate!']", 1, ribbonobj.chart_long_timesleep)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '23M', '46.1M', '69.2M', '92.2M'], "Step 06.01")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'punch', 'Step 06.02 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'elf_green', 'Step 06.03 Verify map color')
        
        '''    7. Click the Show data menu dropdown    '''
        '''    8. Click "Show Data"    '''
        
        resultobj.select_panel_caption_btn(0, select_type='menu')
        utillobj.synchronize_until_element_is_visible("div[id^='BiPopup'][style*='inherit']", resultobj.home_page_short_timesleep)
        utillobj.select_or_verify_bipop_menu('Show Data')
        
        '''    9. Verify an Active Report is launched in a new window    '''
        '''    10. Dismiss the report window   '''
        core_utility_obj.switch_to_new_window()
        utillobj.synchronize_with_visble_text("#ITableData0", 'Store State Province', resultobj.chart_long_timesleep)
        column_list=['Store State Province', 'Gross Profit']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 09.01: Verify active report column titles')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds01.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds01.xlsx", 'Step 09.02: Verify an Active Report is launched in a new window')
        

        '''    11. Click the Show data menu dropdown    '''
        '''    12. Click "Show Data with Related Columns"    '''
        
        core_utility_obj.switch_to_previous_window()
        resultobj.select_panel_caption_btn(0, select_type='menu')
        utillobj.synchronize_until_element_is_visible("div[id^='BiPopup'][style*='inherit']", resultobj.home_page_short_timesleep)
        utillobj.select_or_verify_bipop_menu('Show Data with Related Columns')
        
        '''    13. Verify an Active Report is launched in a new window    '''
        '''    14. Dismiss the report window    '''
        core_utility_obj.switch_to_new_window()
        utillobj.synchronize_with_visble_text("#ITableData0", 'Store Business Region', resultobj.chart_long_timesleep)
        column_list=['Store Business Region', 'Store Business Sub Region', 'Store Country', 'Store State Province', 'Store City', 'Store Postal Code', 'Store Name', 'Cost of Goods Local Currency', 'Cost of Goods', 'Discount Local Currency', 'Discount', 'Gross Profit Local Currency', 'Gross Profit', 'MSRP Local Currency', 'MSRP', 'Quantity Sold', 'Revenue Local Currency', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 13.01: Verify active report column titles')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx", 'Step 13.02: Verify an Active Report is launched in a new window')
        
        
        '''    15. Click "Save" icon    '''
        '''    16. Enter Title "C2229122"    '''
        '''    17. Click "Save" and dismiss IA    '''
        core_utility_obj.switch_to_previous_window()
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", resultobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_cbFileName input", resultobj.home_page_medium_timesleep)
        
        
        '''    18. Dismiss IA window    '''
        '''    19. Log out :    '''
     
if __name__ == '__main__':
    unittest.main()
    