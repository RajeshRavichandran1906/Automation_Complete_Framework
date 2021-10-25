'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229110
Test case Name =  Create a Map with Multi-Graph field
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,ia_ribbon, define_compute, ia_run, wf_map
from common.lib import utillity 
import time,pyautogui
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2229110_TestClass(BaseTestCase):

    def test_C2229110(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        '''    TESTCASE ID Variable    '''
        Test_Case_ID = "C2229110"
        
        '''    1. Launch the IA API with Chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=jsonmaps/south_america    '''
        utillobj.infoassist_api_login('chart','jsonmaps/south_america','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
        '''    2. Add fields "ISO_A2", "RANDOM_NUMBER"    '''
        metaobj.datatree_field_click('ISO_A2', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RANDOM_NUMBER', 2, 1)
        time.sleep(4)
         
        '''    3. Drag/drop "COUNTRY_NAME" in "Multi-graph" bucket    '''
         
        metaobj.drag_drop_data_tree_items_to_query_tree('COUNTRY_NAME', 1, 'Multi-graph', 0)
         
         
        '''    4. Select Format tab    '''
        '''    5. Click "Other" > "Map"  '''
        '''    6. Select "Leaflet Choropleth"    '''
        '''    7. Select 'South America' Territory > OK    '''
         
        ribbonobj.select_ribbon_item("Format", "Other")
         
        time.sleep(4)
        ia_ribbonobj.select_other_chart_type('map', 'leaflet_choropleth', 1)
         
        time.sleep(3)
        combo_btn_obj=self.driver.find_element_by_css_selector("div[id^='SelectChartTypeDlg'] div[id^='RightPane'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(combo_btn_obj, 'South America')
        time.sleep(3)
        ok_btn_css="div[id='qbSelectChartTypeDlgOkBtn']"
        self.driver.find_element_by_css_selector(ok_btn_css).click()
        time.sleep(3)
         
        '''   8. Select "iso_a2" from Geographic Role dropdown > OK    '''
        wfmapobj.set_location_geo_role(role_name='iso_a2 (AR, BO, BR)', btn_click='Ok')
         
        '''    9. Verify Preview   '''
         
        parentcss="pfjTableChart_1"
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g0!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['RANDOM_NUMBER', '540', '553.5', '567', '580.5', '594'], "Step 9.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g0!mstate!", 'persian_red', 'Step 9.2 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step09'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
                                  
        '''    10. Click "Save" icon    '''
        '''    11. Save fex as "C2229110"    '''
        '''    12. Logout:    '''
         
              
        utillobj.switch_to_window(0, pause=3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        
        '''    13. Reopen fex using IA API:    '''
        '''    14. Verify the map is restored    '''
         
         
        utillobj.infoassist_api_logout()
#         
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        parentcss="pfjTableChart_1"
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g0!mstate!']", 1, expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['RANDOM_NUMBER', '540', '553.5', '567', '580.5', '594'], "Step 14.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g0!mstate!", 'persian_red', 'Step 14.2 Verify map color')
        
        '''    15. Click Run    '''
        '''    16. Verify output displays a chart for each country    '''
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(pause=1)
        parentcss="jschart_HOLD_0"
        resultobj.wait_for_property("#jschart_HOLD_0 path[class^='riser!s0!g0!mstate!']", 1,expire_time=60)
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['RANDOM_NUMBER', '540', '553.5', '567', '580.5', '594'], "Step 16.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g0!mstate!", 'persian_red', 'Step 16.2 Verify map color')
        
        tot_charts=[]
        tot_charts=self.driver.find_elements_by_css_selector("div[id^='jschart_HOLD'][class='chart']")
        print ('Total no of charts', len(tot_charts))
        utillobj.asequal(len(tot_charts),13,'Step 16. Verify output displays a chart for each country ')
        
        
        
        utillobj.infoassist_api_logout()


if __name__ == '__main__':
    unittest.main()
    