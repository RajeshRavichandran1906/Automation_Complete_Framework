'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229122
Test case Name =  Verify Show Data 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, wf_map, ia_styling
from common.lib import utillity 
import time,datetime
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from common.pages import active_miscelaneous



class C2229122_TestClass(BaseTestCase):

    def test_C2229122(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229122"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):    '''
        
#         utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
         
        '''    2. Click "Change" dropdown > "Map"    '''
        '''    3. Select "Leaflet Choropleth" > OK (Keep default Territory "United States" selected)    '''
        
        ribbonobj.change_chart_type('map')
        
        time.sleep(5)
        
        ribbonobj.select_map('choropleth', teritory='United States of America', btn_click='ok')
        

        '''    4. Double click "Store,State,Province"    '''
        
        metaobj.datatree_field_click('Store,State,Province', 2, 1)
        
        time.sleep(4)
        
                

        
        '''    5. Select "state_name" from Geographic Role dropdown > OK   '''
        
        
 
        wfmapobj.set_location_geo_role(role_name='state_name (Alabama, Alaska, Arizona)', btn_click='Ok')
        
        '''    6. Double click "Gross Profit"    '''
        
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(4)
        
        '''    6.1. Verify the map is updated    '''
        
        parentcss="TableChart_1"
        resultobj.wait_for_property("#TableChart_1 path[class^='riser!s0!g1!mstate!']", 1, expire_time=50)
        
        
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '23M', '46.1M', '69.2M', '92.2M'], "Step 6.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mstate!", 'punch', 'Step 6.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mstate!", 'elf_green', 'Step 6.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #TableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step06'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)

        
        '''    7. Click the Show data menu dropdown    '''
        '''    8. Click "Show Data"    '''
        
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Show Data')

        time.sleep(6)
        
        '''    9. Verify an Active Report is launched in a new window    '''
        '''    10. Dismiss the report window   '''
        utillobj.switch_to_window(1, pause=3)

        column_list=['Store State Province', 'Gross Profit']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 9.1: Verify active report column titles')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds01.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds01.xlsx", 'Step 09.2: Verify an Active Report is launched in a new window')
        
        self.driver.close()

        '''    11. Click the Show data menu dropdown    '''
        '''    12. Click "Show Data with Related Columns"    '''
        utillobj.switch_to_window(0, pause=3)
        
        resultobj.select_panel_caption_btn(0, select_type='menu')
        time.sleep(3)
        utillobj.select_or_verify_bipop_menu('Show Data with Related Columns')
        time.sleep(5)
        
        
        
        '''    13. Verify an Active Report is launched in a new window    '''
        '''    14. Dismiss the report window    '''
        utillobj.switch_to_window(1, pause=3)
        column_list=['Store Business Region', 'Store Business Sub Region', 'Store Country', 'Store State Province', 'Store City', 'Store Postal Code', 'Store Name', 'Cost of Goods Local Currency', 'Cost of Goods', 'Discount Local Currency', 'Discount', 'Gross Profit Local Currency', 'Gross Profit', 'MSRP Local Currency', 'MSRP', 'Quantity Sold', 'Revenue Local Currency', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 13.1: Verify active report column titles')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx", 'Step 13.2: Verify an Active Report is launched in a new window')
        
        self.driver.close()
        

        
        '''    15. Click "Save" icon    '''
        '''    16. Enter Title "C2229122"    '''
        '''    17. Click "Save" and dismiss IA    '''
        utillobj.switch_to_window(0, pause=3)
             
        #utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        '''    18. Dismiss IA window    '''
        '''    19. Log out :    '''
        utillobj.infoassist_api_logout()
       
        

if __name__ == '__main__':
    unittest.main()
    