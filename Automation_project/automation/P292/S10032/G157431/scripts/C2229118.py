'''
Created on DEC 18, 2017

@author: Sowmiya 

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157431
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2229112
TestCase Name = Convert Map Chart to Report
'''
import unittest,time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea,wf_map,metadata

class C2229118_TestClass(BaseTestCase):

    def test_C2229118(self):
        
        """
            TESTCASE OBJECTS
        """
        wfmapobj=wf_map.Wf_Map(self.driver)
        new_metaobj = metadata.MetaData(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)    
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
          
        """
            TESTCASE VARIABLES
        """        
        Test_Case_ID='C2229118'
        expected_title_list=['Cost of Goods']
        expected_label_list = expected_title_list
        
        """        
            Step 01:Launch Report Mode:
                    http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_leaflet_1', 'mrid', 'mrpass')
        parent_css='#TableChart_1'
        utillobj.synchronize_until_element_is_visible(parent_css, ribbonobj.home_page_long_timesleep)
        
        """        
            Step 02 : Click "Change" dropdown > "Map" -> Select "Leaflet Choropleth"
        """
        ribbonobj.change_chart_type('map')
        utillobj.synchronize_until_element_is_visible("div[id^='QbDialog']", ribbonobj.home_page_long_timesleep)
        ribbonobj.select_map('choropleth', teritory='World',btn_click='ok') 
        utillobj.synchronize_until_element_disappear("div[id^='QbDialog']", ribbonobj.home_page_long_timesleep)
        
        """        
            Step 03 : Double click "Cost of Goods", "Customer,Country" 
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        parent_css="#queryTreeWindow"
        utillobj.synchronize_with_visble_text(parent_css, "Cost of Goods", ribbonobj.home_page_long_timesleep)
        new_metaobj.collapse_data_field_section('Filters and Variables')
        time.sleep(4)
        new_metaobj.collapse_data_field_section('Sales')
        time.sleep(5)
        metaobj.datatree_field_click("Customer,Country", 2, 1)
        utillobj.synchronize_until_element_is_visible("div[id^='QbDialog'] div[id$='geoRoleComboBox'] div[id^='BiButton']", ribbonobj.home_page_long_timesleep)
        
        """        
            Step 04 : Select "country_name" from Geographic Role dropdown > OK  -> Verify the map is displayed 
        """
        wfmapobj.set_location_geo_role(role_name='country_name (Afghanistan, Aland Islands, Albania)', btn_click='Ok')
        parent_css="div[id='TableChart_1'] path[class='riser!s0!g7!mstate!']"
        utillobj.synchronize_until_element_is_visible(parent_css, ribbonobj.chart_long_timesleep)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g7!mstate!', color='persian_red', msg='Step 04.00: Verify the persian red color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g41!mstate!', color='elf_green', msg='Step 04.01: Verify the elf_green color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g4!mstate!', color='burnt_sienna', msg='Step 04.02: Verify the burnt_sienna color')
        expected_legend_list=['Cost of Goods', '0M', '60M', '119.8M', '179.6M', '239.5M']
        ia_resultobj.verify_color_scale_esri_maps('TableChart_1', expected_legend_list, "Step 04.03")
        
        """        
            Step 05 : Click "Change" dropdown > "Choropleth" 
            
            Verify the map is converted

        """
        ribbonobj.change_chart_type('choropleth_map')
        parent_css="path[path]"
        utillobj.synchronize_until_element_is_visible(parent_css, ribbonobj.chart_long_timesleep)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g7!mregion!', color='persian_red', msg='Step 05.00: Verify the persian red color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g41!mregion!', color='elf_green', msg='Step 05.01: Verify the elf_green color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g4!mregion!', color='burnt_sienna', msg='Step 05.02: Verify the burnt_sienna color')
        expected_legend_list=['Cost of Goods', '0M', '60M', '119.8M', '179.6M', '239.5M']
        ia_resultobj.verify_color_scale_esri_maps('TableChart_1', expected_legend_list, "Step 05.03")
       
        """        
            Step 06 : Click "Change" dropdown > "Map"

            Select "Leaflet Bubble" (Keep already selected "World" Territory) -> OK
            
            Select "country_name" from Geographic Role dropdown > OK
            
            Verify the map is converted to leaflet bubble
        """
        ribbonobj.change_chart_type('map')
        utillobj.synchronize_until_element_is_visible("div[id^='QbDialog']", ribbonobj.home_page_long_timesleep)
        ribbonobj.select_map('bubble', teritory='World',btn_click='ok')
        utillobj.synchronize_until_element_is_visible("div[id^='QbDialog'] div[id$='geoRoleComboBox'] div[id^='BiButton']", ribbonobj.home_page_long_timesleep)
        wfmapobj.set_location_geo_role(role_name='country_name (Afghanistan, Aland Islands, Albania)', btn_click='Ok')      
        parent_css='path[stroke-linejoin="round"]'
        utillobj.synchronize_until_element_is_visible(parent_css, ribbonobj.chart_long_timesleep)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g41!mstate!', color='bar_blue', msg='Step 06.00: Verify the bar_blue color in bubble map')
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', expected_title_list, 'Step 06.01: Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', expected_label_list, msg='Step 06.02: ', custom_css="text[class^='legend-labels']", same_group=True)
        
        """        
            Step 07 : Click "Change" dropdown > "ESRI Bubble"
            
            Verify the map is converted

        """
        ribbonobj.change_chart_type('bubble_map')
        parent_css="#TableChart_1 circle[class='riser!s0!g41!mregion!']"
        utillobj.synchronize_until_element_is_visible(parent_css, resobj.home_page_long_timesleep)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g41!mregion!', color='bar_blue', msg='Step 07.00: Verify the bar_blue color in bubble map')
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', expected_title_list, 'Step 07.01: Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', expected_label_list, msg='Step 07.02: ', custom_css="text[class^='legend-labels']", same_group=True)
        
        """        
            Step 08 : Click "Save" icon
              Save Report fex as "C2229118"
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """        
            Step 09 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout() 
        
        """  Step 10 : Reopen saved FEX:    
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227571.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','P292/S10032_leaflet_1', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1 circle[class='riser!s0!g41!mregion!']"
        utillobj.synchronize_until_element_is_visible(parent_css, ribbonobj.chart_long_timesleep)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g41!mregion!', color='bar_blue', msg='Step 10.00: Verify the bar_blue color in bubble map')
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', expected_title_list, 'Step 10.01: Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_1', expected_label_list, msg='Step 10.02: ', custom_css="text[class^='legend-labels']", same_group=True)
        
if __name__ == '__main__':
    unittest.main()             