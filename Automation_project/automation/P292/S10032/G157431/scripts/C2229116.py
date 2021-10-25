'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229116
Test case Name =  Verify Bubble Map can be created 
'''
import unittest,time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map,core_metadata
from common.lib.core_utility import CoreUtillityMethods

class C2229116_TestClass(BaseTestCase):

    def test_C2229116(self):
        
        core_mta = core_metadata.CoreMetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229116"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032_leaflet_1', 'mrid', 'mrpass')
        parent_css='#TableChart_1'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 90, 1)
         
         
        '''    2. Double click "Store,Country","Cost of Goods".    '''
        '''    3. Verify the following chart is displayed.    '''
        
        core_mta.double_click_on_data_filed('Store,Country', 1)
        time.sleep(4)
        core_mta.double_click_on_data_filed('Cost of Goods', 1)
        time.sleep(4)
        
        element_css="#pfjTableChart_1 [class^='riser!s0!g2!mbar']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 90)
        
        xaxis_value="Store Country"
        yaxis_value="Cost of Goods"
        parentcss="pfjTableChart_1"
        resultobj.verify_xaxis_title(parentcss, xaxis_value, "Step 02.01: Verify X-Axis Title")
        resultobj.verify_yaxis_title(parentcss, yaxis_value, "Step 02.02: Verify Y-Axis Title")
        expected_xval_list_cr=['Australia', 'Belgium', 'Brazil']
#         expected_xval_list_ff=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Korea, Republic of', 'Luxembourg', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        resultobj.verify_data_labels("pfjTableChart_1", expected_xval_list_cr, "Step 02.03: Verify X labels", data_label_length=3,custom_css="svg > g text[class^='xaxis'][class*='labels']")
        resultobj.verify_data_labels("pfjTableChart_1", expected_yval_list, "Step 02.04: Verify Y labels", custom_css="svg > g text[class^='yaxis'][class*='labels']")
        resultobj.verify_number_of_riser(parentcss, 1, 34, 'Step 02.05: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mbar", "bar_blue", "Step 02.06: Verify first bar color")
        time.sleep(5)
        
        '''    '4. Select "Format" > "Other" > "Map".    '''
        '''    5. Select "Leaflet Bubble"    '''
        '''    '6. Set "Territory" = "World" > OK    '''
        
        ribbonobj.select_ribbon_item("Format", "Other")
         
        time.sleep(4)
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_bubblemap', 1)
         
        time.sleep(3)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'World')
        time.sleep(3)
        ok_btn_ele = self.driver.find_element_by_css_selector("div[id='qbSelectChartTypeDlgOkBtn']")
        CoreUtillityMethods.python_left_click(self, ok_btn_ele)
        time.sleep(3)
        
        '''    '7. Set "Geographic Role" = "Country_name">OK    '''
        wfmapobj.set_location_geo_role(role_name='country_name (Afghanistan, Aland Islands, Albania)', btn_click='Ok')
         
        '''    8. Verify the following map is displayed.    '''
       
        parentcss="pfjTableChart_1"
        
        element_css="#pfjTableChart_1 [class^='riser!s0!g33!mstate!']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 90)
        
        expected_label_list=['Cost of Goods']
        msg="Step 08.01: Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 08.02: Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'bar_blue', 'Step 08.03: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'bar_blue', 'Step 08.04: Verify different map color again')
        
        '''    9. Drag "Revenue" to Color bucket    '''
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue', 1, 'Color', 0)
        time.sleep(1)
        element_css="#pfjTableChart_1 g text[class*='colorScaleLegend-title']"
        utillobj.synchronize_with_visble_text(element_css, 'Revenue', 90, 1)
        
        time.sleep(10)
        
        '''    10. Verify the following chart is displayed.    '''
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 10.01")
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 10.02: Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 10.03: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'Vermilion', 'Step 10.04: Verify different map color again')
        
        '''    11. Click "IA" > "Save" > "C2229116" > "Save".    '''
        '''    12. Logout:    '''
                
        CoreUtillityMethods.switch_to_default_content(self)
        ia_ribbonobj.select_ia_application_menu_item('save')
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        
        '''    13. Run saved fex from BIP using IA API:    '''
        '''    14. Verify the following chart is displayed.    '''
        '''    15. Logout:    '''
        
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_leaflet_1', mrid='mrid', mrpass='mrpass')
#         utillobj.switch_to_window(wndnum=0, pause=15)
        element_css="#jschart_HOLD_0 [class^='riser!s0!g33!mstate!']"
        utillobj.synchronize_with_number_of_element(element_css, 1, 90, 1)
        
        parentcss="jschart_HOLD_0"

        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 14.01")
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 14.02: Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 14.03: Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'Vermilion', 'Step 14.04: Verify different map color again')   
        
if __name__ == '__main__':
    unittest.main()