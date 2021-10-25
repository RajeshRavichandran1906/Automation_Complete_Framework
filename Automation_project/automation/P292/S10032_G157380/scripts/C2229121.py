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
        
        driver = self.driver
        driver.implicitly_wait(60)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        wfmapobj=wf_map.Wf_Map(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        Test_Case_ID='C2229121'
       
        """        
            Step 01:Launch Report Mode:
                    http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail','P292/S10032_leaflet_1', 'mrid', 'mrpass')
        
        """        
            Step 02 : Click "Change" dropdown > "Map" -> Select "Leaflet Choropleth"
                    
                    Select "Leaflet Choropleth" > OK (Keep default Territory "United States" selected)
        """
        ribbonobj.change_chart_type('map')
        time.sleep(5)
        ribbonobj.select_map('choropleth', teritory='United States of America',btn_click='ok') 
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css,1,expire_time=50)
        utillobj.verify_object_visible('pfjTableChart_1', False, msg='Step 2.1 : Verify the map is invisible')
        """        
            Step 03 : Double click "Store,State,Province"

                        Select "state_name" as Geographic Role > OK

                        Drag "Gross Profit" into Color bucket
        """
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        time.sleep(2)
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_object_visible("a[class='leaflet-control-layers-toggle']", True, msg='Step 3.2 : Verify leaflet control toggle')
        utillobj.verify_object_visible("button[class='data-selection-button leaflet-control']", True, msg='Step 3.3 : Verify pan button')
        expected_tooltip_list=['Store State Province:Alaska', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resobj.verify_default_tooltip_values('TableChart_1', 'riser!s0!g20!mstate!', expected_tooltip_list, msg='Step 3.4 : Verify tooltip values')
        
        time.sleep(2)
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit', 1, 'Color', 0)
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g1!mstate!', color='punch', msg='Step 3.5 : Verify punch color')
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g25!mstate!', color='elf_green', msg='Step 3.6 : Verify green color')
        expected_tooltip_list=['Store State Province:Alaska', 'Gross Profit:$1,616,022.71', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Country', 'Drill down to Store City']
        resobj.verify_default_tooltip_values('TableChart_1', 'riser!s0!g1!mstate!', expected_tooltip_list, msg='Step 3.7 : Verify tooltip values')
        expected_legend_list=['Gross Profit', '0M', '23M', '46.1M', '69.2M', '92.2M']
        ia_resultobj.verify_color_scale_esri_maps('TableChart_1', expected_legend_list, "Step 3.8 : Verify the lables and legends")
        
        """        
            Step 04 : Click "Clear" button

                        Click "OK" in the dialog

                        Verify the map is cleared
        """
        
        ribbonobj.select_ribbon_item('Home', 'clear')
        btn_click="div[class^='bi-button button button-focus ']"
        btn_ele=self.driver.find_element_by_css_selector(btn_click)
        btn_ele.send_keys(Keys.NULL)
        btn_ele.click()
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_object_visible('pfjTableChart_1', False, msg='Step 4.1 : Verify clear map')
        time.sleep(5)
        
        """        
            Step 05 : Click "undo" button

                        Verify the map is restored
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('TableChart_1', 'riser!s0!g25!mstate!', color='elf_green', msg='Step 5.1 : Verify green color')
        
        """        
            Step 06 : Click "Insert" button

                        Click "Change" dropdown > "Map"

                        Select "Leaflet Bubble" > OK (Keep default Territory "United States" selected)
        """
        ribbonobj.select_ribbon_item('Home', 'insert',opt='Chart')
        time.sleep(2)
        
        ribbonobj.change_chart_type('map')
        time.sleep(2)
        ribbonobj.select_map('bubble', teritory='United States of America',btn_click='ok')
        
        parent_css='#TableChart_2'
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_object_visible('pfjTableChart_2', False, msg='Step 6.1 : Verify the map is visible')
 
        """        
            Step 07 : Double click "Store,State,Province"

                        Select "state_name" as Geographic Role > OK

                        Drag "Revenue" into Size bucket
        """
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        parent_css="path[class='riser!s0!g20!mstate!']"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        time.sleep(2)
        utillobj.verify_chart_color('TableChart_2', 'riser!s0!g20!mstate!', color='bar_blue', msg='Step 7.1 : verify blue color')
        time.sleep(2)
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue', 1, 'Size', 0)
        parent_css="path[class='riser!s0!g25!mstate!']"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('TableChart_2', 'riser!s0!g25!mstate!', color='bar_blue', msg='Step 7.2 : verify blue color')
        utillobj.verify_object_visible("a[class='leaflet-control-layers-toggle']", True, msg='Step 7.3 : Verify leaflet control toggle')
        utillobj.verify_object_visible("button[class='data-selection-button leaflet-control']", True, msg='Step 7.4 : Verify pan button')
        
        expected_title_list=['Revenue']
        expected_label_list=['Revenue']
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_title_list, 'Step 7.5 : Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_label_list, msg='Step 7.6 : ', custom_css="text[class^='legend-labels']", same_group=True)
    
        """        
            Step 08 : Click "Clear" dropdown > "Visualization"

                        Click "OK" in the dialog

                        Verify both maps are cleared
        """
        ribbonobj.select_ribbon_item('Home', 'clear_dropdown',opt='Visualization')
        btn_click="div[class^='bi-button button button-focus ']"
        btn_ele=self.driver.find_element_by_css_selector(btn_click)
        btn_ele.send_keys(Keys.NULL)
        btn_ele.click()
        utillobj.verify_object_visible('TableChart_1', False, msg='Step 8.1 : Verify the map is cleared')
        utillobj.verify_object_visible('TableChart_2', False, msg='Step 8.2 : Verify the map is cleared')
       
        """        
            Step 09 : Click "Undo" button

                        Verify both maps are restored
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        parent_css="#TableChart_1"
        resobj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_object_visible('TableChart_1', False, msg='Step 9.1 : Verify the map is restored')
        utillobj.verify_object_visible('TableChart_2', False, msg='Step 9.2 : Verify the map is restored')
        
        expected_title_list=['Revenue']
        expected_label_list=['Revenue']
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_title_list, 'Step 9.3 : Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        resobj.verify_riser_pie_labels_and_legends('TableChart_2', expected_label_list, msg='Step 9.4 : ', custom_css="text[class^='legend-labels']", same_group=True)
        ia_resultobj.verify_color_scale_esri_maps('TableChart_1', expected_legend_list, "Step 9.5 : Verify the lables and legends")
         
        """        
            Step 10 : Click "Save" icon
              
                          Save Report fex as "C2229121"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """        
            Step 11 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout() 
        
        
        """  Step 10 : Reopen saved FEX:    
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227571.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','P292/S10032_leaflet_1', mrid='mrid', mrpass='mrpass')
   
if __name__ == '__main__':
    unittest.main()        
        
        