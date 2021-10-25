'''
Created on DEC 26, 2017

@author: Sowmiya 

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157431
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2229121
TestCase Name = Verify clearing map components
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, wf_map
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.keys import Keys

class C2229121_TestClass(BaseTestCase):

    def test_C2229121(self):
        
        
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        wfmapobj=wf_map.Wf_Map(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        Test_Case_ID='C2229121'
       
        """        
            1. Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        """
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_leaflet_1', 'mrid', 'mrpass')
        
        """        
            Step 02 : Click "Change" dropdown > "Map" -> Select "Leaflet Choropleth"
                    
            Step 03 :Select "Leaflet Choropleth" > OK (Keep default Territory "United States" selected)
        """
        ribbonobj.change_chart_type('map')
        time.sleep(5)
        ribbonobj.select_map('choropleth', teritory='United States of America',btn_click='ok') 
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css,1,expire_time=90)
        
        """        
            Step 04 : Double click "Store,State,Province"

            Step 05 : Select "state_name" as Geographic Role > OK

            Step 06 : Drag "Gross Profit" into Color bucket
        """
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        utillobj.synchronize_with_number_of_element("div[id^='QbDialog']:not([style*='hidden'])", 1, 20, 1)
        time.sleep(2)
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        
        parent_css="#TableChart_1"
        resobj.wait_for_property(parent_css, 1, expire_time=90)
      
        time.sleep(2)
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit', 1, 'Color', 0)
        parent_css="#TableChart_1 [class*='riser!s0!g25!mstate!']"
        resobj.wait_for_property(parent_css, 1, expire_time=90)
        time.sleep(5)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g1!mstate!', color='punch', msg='Step 6.1 : Verify punch color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g25!mstate!', color='elf_green', msg='Step 6.2 : Verify green color')
        
        expected_legend_list=['Gross Profit', '0M', '23M', '46.1M', '69.2M', '92.2M']
        ia_resultobj.verify_color_scale_esri_maps('TableChart_1', expected_legend_list, "Step 6.3 : Verify the lables and legends")
        utillobj.verify_object_visible("a[class='leaflet-control-layers-toggle']", True, msg='Step 6.4 : Verify leaflet control toggle')
        utillobj.verify_object_visible("button[class='data-selection-button leaflet-control']", True, msg='Step 6.5 : Verify pan button')
        
        """        
            Step 07 : Click "Clear" button

            Step 08 : Click "OK" in the dialog

            Step 09: Verify the map is cleared
        """
        
        ribbonobj.select_ribbon_item('Home', 'clear')
        btn_click="div[class^='bi-button button button-focus ']"
        btn_ele=self.driver.find_element_by_css_selector(btn_click)
        btn_ele.send_keys(Keys.NULL)
        btn_ele.click()
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css, 1, expire_time=90)
        utillobj.verify_object_visible('pfjTableChart_1', False, msg='Step 9.1 : Verify clear map')
        time.sleep(5)
        
        """        
            Step 10 : Click "undo" button

            Step 11 : Verify the map is restored
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        
        parent_css="#TableChart_1 [class*='riser!s0!g25!mstate!']"
        resobj.wait_for_property(parent_css, 1, expire_time=90)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g25!mstate!', color='elf_green', msg='Step 10.01 : Verify green color')
        expected_legend_list=['Gross Profit', '0M', '23M', '46.1M', '69.2M', '92.2M']
        ia_resultobj.verify_color_scale_esri_maps('TableChart_1', expected_legend_list, "Step 10.02 : Verify the lables and legends")
        
        """        
            Step 12 : Click "Insert" button

            Step 13 : Click "Change" dropdown > "Map"

            Step 14 : Select "Leaflet Bubble" > OK (Keep default Territory "United States" selected)
        """
        ribbonobj.select_ribbon_item('Home', 'insert',opt='Chart')
        time.sleep(2)
        
        ribbonobj.change_chart_type('map')
        time.sleep(2)
        ribbonobj.select_map('bubble', teritory='United States of America',btn_click='ok')
        
        parent_css='#TableChart_2'
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_object_visible('pfjTableChart_2', False, msg='Step 14.01 : Verify the map is visible')
 
        """        
            Step 15:  Double click "Store,State,Province"

            Step 16: Select "state_name" as Geographic Role > OK

            Step 17:  Drag "Revenue" into Size bucket
        """
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        parent_css="#TableChart_2 [class*='riser!s0!g20!mstate!']"
        resobj.wait_for_property(parent_css, 1, expire_time=90)
        time.sleep(2)
        utillobj.verify_chart_color('TableChart_2', 'riser!s0!g20!mstate!', color='bar_blue', msg='Step 17.01 : verify blue color')
        time.sleep(2)
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue', 1, 'Size', 0)
        parent_css="#TableChart_2 [class*='riser!s0!g25!mstate!']"
        resobj.wait_for_property(parent_css, 1, expire_time=90)
        utillobj.verify_chart_color('TableChart_2', 'riser!s0!g25!mstate!', color='bar_blue', msg='Step 17.2 : verify blue color')
        utillobj.verify_object_visible("a[class='leaflet-control-layers-toggle']", True, msg='Step 17.3 : Verify leaflet control toggle')
        utillobj.verify_object_visible("button[class='data-selection-button leaflet-control']", True, msg='Step 17.4 : Verify pan button')
        
        expected_title_list=['Revenue']
        expected_label_list=['Revenue']
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_title_list, 'Step 17.5 : Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_label_list, msg='Step 17.6 : ', custom_css="text[class^='legend-labels']", same_group=True)
    
        """        
            Step 18 : Click "Clear" dropdown > "Visualization"

            Step 19 : Click "OK" in the dialog

            Step 20 : Verify both maps are cleared
        """
        ribbonobj.select_ribbon_item('Home', 'clear_dropdown',opt='Visualization')
        btn_click="div[class^='bi-button button button-focus ']"
        btn_ele=self.driver.find_element_by_css_selector(btn_click)
        btn_ele.send_keys(Keys.NULL)
        btn_ele.click()
        utillobj.verify_object_visible('TableChart_1', False, msg='Step 20.1 : Verify the map is cleared')
        utillobj.verify_object_visible('TableChart_2', False, msg='Step 20.2 : Verify the map is cleared')
       
        """        
            Step 21 : Click "Undo" button

            Step 22 : Verify both maps are restored
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        parent_css="#TableChart_1 [class*='riser!s0!g1!mstate!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90, 1)
        
        parent_css="#TableChart_2 [class*='riser!s0!g25!mstate!']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90, 1)
        
        utillobj.verify_object_visible('TableChart_1', False, msg='Step 22.1 : Verify the map is restored')
        utillobj.verify_object_visible('TableChart_2', False, msg='Step 22.2 : Verify the map is restored')
        
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g1!mstate!', color='punch', msg='Step 22.3 : Verify punch color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g25!mstate!', color='elf_green', msg='Step 22.4 : Verify green color')
        
        expected_title_list=['Revenue']
        expected_label_list=['Revenue']
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_title_list, 'Step 22.5 : Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_label_list, msg='Step 22.6 : ', custom_css="text[class^='legend-labels']", same_group=True)
        ia_resultobj.verify_color_scale_esri_maps('TableChart_1', expected_legend_list, "Step 22.7 : Verify the lables and legends")
         
        """        
            Step 23 : Click "Save" icon
            Step 24. Enter Title "C2229121"
            Step 25. Click "Save" and dismiss IA
        """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """        
            Step 26 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """   
        
if __name__ == '__main__':
    unittest.main()