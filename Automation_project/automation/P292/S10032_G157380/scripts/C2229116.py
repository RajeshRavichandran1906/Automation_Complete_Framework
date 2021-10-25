'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229116
Test case Name =  Verify Bubble Map can be created 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map, ia_styling
from common.lib import utillity 
import time,datetime
from common.lib.basetestcase import BaseTestCase



class C2229116_TestClass(BaseTestCase):

    def test_C2229116(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229116"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
         
        '''    2. Double click "Store,Country","Cost of Goods".    '''
        '''    3. Verify the following chart is displayed.    '''
        
        metaobj.datatree_field_click('Store,Country', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        time.sleep(4)
        
        xaxis_value="Store Country"
        yaxis_value="Cost of Goods"
        parentcss="pfjTableChart_1"
        resultobj.verify_xaxis_title(parentcss, xaxis_value, "Step 02:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title(parentcss, yaxis_value, "Step 02:a(ii) Verify Y-Axis Title")
        expected_xval_list_cr=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Korea, Republic of', 'Luxembourg', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States']
        expected_xval_list_ff=['Australia', 'Belgium', 'Brazil', 'Canada', 'Chile', 'China', 'Czech Republic', 'Denmark', 'Egypt', 'France', 'Germany', 'Greece', 'Hungary', 'India', 'Ireland', 'Israel', 'Italy', 'Japan', 'Korea, Republic of', 'Luxembourg', 'Mexico', 'Netherlands', 'Norway', 'Philippines', 'Poland', 'Portugal', 'Singapore', 'Spain', 'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'United Kingdom', 'United States']
        expected_yval_list=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M', '400M', '450M']
        if browser_type=="Chrome":
            resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list_cr, expected_yval_list, "Step 02:c(iii):Verify XY labels")
        else:
            resultobj.verify_riser_chart_XY_labels(parentcss, expected_xval_list_ff, expected_yval_list, "Step 02:c(iii):Verify XY labels")
        resultobj.verify_number_of_riser(parentcss, 1, 34, 'Step 02.d: Verify the total number of risers displayed on preview')
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
        utillobj.select_any_combobox_item(combo_btn_obj, 'World')
        time.sleep(3)
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(3)
        

        
        '''    '7. Set "Geographic Role" = "Country_name">OK    '''
        
 
        wfmapobj.set_location_geo_role(role_name='country_name (Afghanistan, Aland Islands, Albania)', btn_click='Ok')
         
        
        '''    8. Verify the following map is displayed.    '''
       
        parentcss="pfjTableChart_1"
        
        expected_label_list=['Cost of Goods']
        msg="Step 8.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 8.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'bar_blue', 'Step 8.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'bar_blue', 'Step 8.3b Verify map color')
        
        
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step08'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        '''    9. Drag "Revenue" to Color bucket    '''
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue', 1, 'Color', 0)
        time.sleep(1)
        
        resultobj.wait_for_property("#pfjTableChart_1 g text[class*='colorScaleLegend-title']", 1, expire_time=60, string_value='Revenue')
        
        time.sleep(6)
        
        '''    10. Verify the following chart is displayed.    '''
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 10.1")
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 10.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 10.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'Vermilion', 'Step 10.3b Verify map color')
        
        
        
        '''    11. Click "IA" > "Save" > "C2229116" > "Save".    '''
        '''    12. Logout:    '''
                
        utillobj.switch_to_window(0, pause=3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        utillobj.infoassist_api_logout()
         
        
        '''    13. Run saved fex from BIP using IA API:    '''
        '''    14. Verify the following chart is displayed.    '''
        '''    15. Logout:    '''
        
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_leaflet_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        utillobj.switch_to_window(wndnum=0, pause=15)
        
        
        resultobj.wait_for_property("#jschart_HOLD_0 [class^='riser!s0!g33!mstate!']", 1, expire_time=90)
        
        
        parentcss="jschart_HOLD_0"

        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 14.1")
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 14.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mstate!", 'elf_green', 'Step 14.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mstate!", 'Vermilion', 'Step 14.3b Verify map color')   
        utillobj.infoassist_api_logout()


if __name__ == '__main__':
    unittest.main()
    