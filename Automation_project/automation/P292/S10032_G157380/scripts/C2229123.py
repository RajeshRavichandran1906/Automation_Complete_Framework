'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229123
Test case Name =  Verify Export data
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map, ia_styling
from common.lib import utillity 
import time,datetime
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By



class C2229123_TestClass(BaseTestCase):

    def test_C2229123(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229123"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        
#         utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
         
        '''    2. Click "Change" dropdown > "Map"    '''
        '''    3. Select "Leaflet Bubble" > OK (Keep default Territory "United States" selected)    '''
        
        ribbonobj.change_chart_type('map')
        
        time.sleep(5)
        
        ribbonobj.select_map('bubble', teritory='United States of America', btn_click='ok')
        

        '''    4. drag "Store,State,Province" into Geolocation bucket    '''
        
        #metaobj.datatree_field_click('Store,State,Province', 2, 1)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,State,Province', 1, 'Layer', 0)
        time.sleep(4)
        
                

        
        '''    5. Select "state_name" from Geographic Role dropdown > OK   '''
        
        
 
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        
        '''    6. Right click "Revenue" > "Add To Query" > "Size"    '''
        
        metaobj.datatree_field_click('Revenue', 1, 1, 'Add To Query', 'Size')
        time.sleep(4)
        
        '''    7. Verify the map is updated    '''
        
        parentcss="TableChart_1"
        resultobj.wait_for_property("#TableChart_1 path[class^='riser!s0!g25!mstate!']", 1, expire_time=50)
        
        expected_label_list=['Revenue']
        msg="Step 7.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 7.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'bar_blue', 'Step 7.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mstate!", 'bar_blue', 'Step 7.3b Verify map color')
        
        
        img1=self.driver.find_element_by_css_selector("#resultArea #TableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step07'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        '''    '8. Click the Show Data menu dropdown    '''
        '''    '9. Select "Export Data" > "Summary"    '''
        
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Export Data')
        utillobj.select_or_verify_bipop_menu('Summary')
        
        time.sleep(6)
        
        
        '''    10. Download and Open the Excel file    '''
        '''    11. Verify the excel spreadsheet contains the data from the fields    '''
        '''    12. Dismiss Excel    '''
        
        utillobj.save_file_from_browser('C2229123_Ds01_actual.xlsx')
        
        time.sleep(10)
        utillobj.verify_excel_files('C2229123_Ds01.xlsx', 'Sheet1', 'C2229123_Ds01_actual.xlsx', 'Sheet1', 78, 2, 'Step 11. Verify excel sheet after export', tool='openpyxl')
        

        '''    13. Click "Save" icon    '''
        '''    14. Enter Title "C2229123"    '''
        '''    15. Click "Save" and dismiss IA    '''
        utillobj.switch_to_window(0, pause=3)
             
        #utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        utillobj.infoassist_api_logout()
         
       
        

if __name__ == '__main__':
    unittest.main()
    