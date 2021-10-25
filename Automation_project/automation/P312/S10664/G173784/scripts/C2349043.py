'''
Created on Feb 12, 2018

@author: Sowmiya
Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157431
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2349043
TestCase Name = Paperclipping in Leaflet Proportional map
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, wf_map
from common.lib.basetestcase import BaseTestCase
class C2349043_TestClass(BaseTestCase):

    def test_C2349043(self):
        
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj= ia_resultarea.IA_Resultarea(self.driver)      
        wfmapobj=wf_map.Wf_Map(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        Test_Case_ID='C2349043'
        
        def verify_map(parent_id, title, label_list, riser_name, tooltip_riser_name, legend_list, tooltip_list, color_name, stepno):
            resobj.verify_riser_pie_labels_and_legends(parent_id, title, 'Step '+stepno+'.1', custom_css="text[class^='sizeLegend-title']", same_group=True)
            ia_resultobj.verify_color_scale_esri_maps(parent_id, label_list, msg='Step '+stepno+'.2'+' Verify color scale')
            utillobj.verify_chart_color(parent_id, riser_name[0], color=color_name[0], msg='Step '+stepno+'.3'+' Verify color')
            utillobj.verify_chart_color(parent_id, riser_name[1], color=color_name[1], msg='Step '+stepno+'.4'+' Verify color')
            utillobj.verify_chart_color(parent_id, riser_name[2], color=color_name[2], msg='Step '+stepno+'.5'+' Verify color')
            resobj.verify_default_tooltip_values("MAINTABLE_wbody1_f", tooltip_riser_name, tooltip_list, msg='Step '+stepno+'.6'+' Verify tooltip values')       
            resobj.verify_legends(legend_list, "#MAINTABLE_wbody1_f", 10, msg='Step '+stepno+'.7'+' Verify color')
            
        """        
            Step 01:Launch Report Mode:
                    http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail','P312/S10664_Paperclipping_2', 'mrid', 'mrpass')
         
        """
        Step 02 : Click Change drop down > Map > Leaflet Proportional map (Set Territory = world)
        """
        ribbonobj.change_chart_type('map')
        
        ribbonobj.select_map('bubble', teritory='World',btn_click='ok') 
        parent_css='#TableChart_1'
        resobj.wait_for_property(parent_css,1,expire_time=60)
         
        """
        Step 03 : Double click "Store,Country" (Geo role - Country name) and "Cost of Goods"
        """
        metaobj.datatree_field_click('Store,Country', 2, 1)
        wfmapobj.set_location_geo_role(role_name='country_name (Afghanistan, Aland Islands, Albania)', btn_click='Ok')
        resobj.wait_for_property("#MAINTABLE_1 [class='riser!s0!g41!mstate!']", 1)
 
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        resobj.wait_for_property("#queryTreeColumn table tr:nth-child(9)", 1)
         
        """
        Step 04 : Drag and drop "Revenue" to Color bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue', 1, 'Color', 0)
        resobj.wait_for_property("#queryTreeColumn table tr:nth-child(11)", 1)
         
        """
        Step 05 : Verify following preview, query pane and filter pane
        """
        metaobj.verify_query_pane_field('Color', 'Revenue', 1, msg="Step 4.1 ")
        metaobj.verify_query_pane_field('Size', 'Cost of Goods', 1, msg="Step 4.2 ")
         
        parent_id='TableChart_1'
        title=['Cost of Goods']
        label_list=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        legend_list=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M', 'Cost of Goods', '392M', '196M', '0M']
        riser_name=['riser!s0!g7!mstate!','riser!s0!g33!mstate!','riser!s0!g3!mstate!']
        color_name=['Vermilion','elf_green','sorbus_2']
        tooltip_riser_name='riser!s0!g33!mstate!'
        tooltip_list=['Store Country:United States', 'Cost of Goods:$392,048,898.00', 'Revenue:$545,792,166.41', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to Store State Province']
        verify_map(parent_id, title, label_list, riser_name, tooltip_riser_name, legend_list, tooltip_list, color_name, '5')
         
        """
        Step 06 : Click Pan > Lasso on , "Canada", "Mexico","United States"
        """
        pan_css="#MAINTABLE_1 button[class^='data-s']"
        pan_elem=self.driver.find_element_by_css_selector(pan_css)
        pan_elem.click()
         
        resobj.create_lasso("MAINTABLE_wbody1", 'path', "riser!s0!g19!mstate!",target_tag='path',target_riser='riser!s0!g3!mstate!')
         
        """
        Step 07 : Select "Group Store,Country selection"
        """
        resobj.select_or_verify_lasso_filter(select='Group Store,Country Selection')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_1 path[class^='riser']", 30, 60)
         
        """
        Step 08 : Verify following preview displayed
        """
        parent_id='TableChart_1'
        title=['Cost of Goods']
        label_list=['Revenue', '0M', '152.5M', '305M', '457.4M', '610M']
        legend_list=['Revenue', '0M', '152.5M', '305M', '457.4M', '610M', 'Cost of Goods', '438M', '219M', '0M']
        riser_name=['riser!s0!g27!mstate!','riser!s0!g4!mstate!','riser!s0!g5!mstate!']
        color_name=['cinnabar','persian_red3','persian_red']
        tooltip_riser_name='riser!s0!g2!mstate!'
        tooltip_list=['COUNTRY_NAME_1:Brazil', 'Cost of Goods:$18,615,007.00', 'Revenue:$25,974,011.78', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to Store Country']
        verify_map(parent_id, title, label_list, riser_name, tooltip_riser_name, legend_list, tooltip_list, color_name, '8')
         
        """
        Step 09 : Hover Unknowns and verify "Canada" and Mexico and United States"
        """
         
        elem="#MAINTABLE_1 div[class='leaflet-bar leaflet-control leaflet-control-unmatched-data']"
        elem1=self.driver.find_element_by_css_selector(elem)
        utillobj.get_element_attribute(elem1, 'title')
         
        """
        Step 10 : Right click "COUNTRY_NAME_1" > Edit group
        """
        metaobj.querytree_field_click('COUNTRY_NAME_1', 1, 1,'Edit Group...')
         
        """
        Step 11 : Rename group value name to "United States" > Hit enter
        """
        element_list=['Canada and Mexico and United States']
        metaobj.create_ia_group('Rename', element_list, rename_field='United States')
        time.sleep(3)
         
        """
        Step 12 : Click OK to dismiss edit group dialog
        """
        metaobj.close_ia_group_dialog(close_button='ok')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_1 path[class^='riser']", 31, 60)
         
        """
        Step 13 : Hover on 'United states' and Verify tooltip values
        """
        parent_id='TableChart_1'
        title=['Cost of Goods']
        label_list=['Revenue', '0M', '152.5M', '305M', '457.4M', '610M']
        legend_list=['Revenue', '0M', '152.5M', '305M', '457.4M', '610M', 'Cost of Goods', '438M', '219M', '0M']
        riser_name=['riser!s0!g31!mstate!','riser!s0!g0!mstate!','riser!s0!g7!mstate!']
        color_name=['elf_green','persian_red3','persian_red']
        tooltip_riser_name='riser!s0!g31!mstate!'
        tooltip_list=['COUNTRY_NAME_1:United States', 'Cost of Goods:$437,951,635.00', 'Revenue:$609,916,853.67', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to Store Country']
        verify_map(parent_id, title, label_list, riser_name, tooltip_riser_name, legend_list, tooltip_list, color_name, '13')
         
        """
        Step 14 : Click Save in the toolbar > Save as "C2349043" > Click Save
        """
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """
        Step 15 : Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step 16 : Run fex from Resource tree using API
                    http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10664&BIP_item=C2349043.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10664_paperclipping_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_1 path[class^='riser']", 31, 60)
        """
        Step 17 : Hover on map and verify tooltip values
        """
        parent_id='MAINTABLE_1'
        title=['Cost of Goods']
        label_list=['Revenue', '0M', '152.5M', '305M', '457.4M', '610M']
        legend_list=['Revenue', '0M', '152.5M', '305M', '457.4M', '610M', 'Cost of Goods', '438M', '219M', '0M']
        riser_name=['riser!s0!g31!mstate!','riser!s0!g0!mstate!','riser!s0!g7!mstate!']
        color_name=['elf_green','persian_red3','persian_red']
        tooltip_riser_name='riser!s0!g31!mstate!'
        tooltip_list=['COUNTRY_NAME_1:United States', 'Cost of Goods:$437,951,635.00', 'Revenue:$609,916,853.67', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to Store Country']
        verify_map(parent_id, title, label_list, riser_name, tooltip_riser_name, legend_list, tooltip_list, color_name, '17')
        
        """
        Step 18 : Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
        Step 19 : Restore saved fex using API
                    http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349043.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis','P312/S10664_paperclipping_2', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#MAINTABLE_1 path[class^='riser']", 31, 60)
        
        parent_id='TableChart_1'
        title=['Cost of Goods']
        label_list=['Revenue', '0M', '152.5M', '305M', '457.4M', '610M']
        legend_list=['Revenue', '0M', '152.5M', '305M', '457.4M', '610M', 'Cost of Goods', '438M', '219M', '0M']
        riser_name=['riser!s0!g31!mstate!','riser!s0!g0!mstate!','riser!s0!g7!mstate!']
        color_name=['elf_green','persian_red3','persian_red']
        tooltip_riser_name='riser!s0!g31!mstate!'
        tooltip_list=['COUNTRY_NAME_1:United States', 'Cost of Goods:$437,951,635.00', 'Revenue:$609,916,853.67', 'Filter Chart', 'Exclude from Chart', 'Drill up to Store Business Sub Region', 'Drill down to Store Country']
        verify_map(parent_id, title, label_list, riser_name, tooltip_riser_name, legend_list, tooltip_list, color_name, '19')
        
if __name__ == '__main__':
    unittest.main()        