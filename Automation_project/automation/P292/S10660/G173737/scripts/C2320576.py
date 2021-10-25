'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2320576
Test case Name =  Choropleth Chart - Json is created by server
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2320576_TestClass(BaseTestCase):

    def test_C2320576(self):
    
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2320576"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10660', 'mrid', 'mrpass')
        #time.sleep(5)
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=60)
          
          
        """    2. Go to Format tab > "Choropleth"    """
        
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=25)
        time.sleep(9)
       
        """    3. Double click "Store,Country", "Revenue"    """
        """    3a. Verify the map is updated    """
        
        metaobj.datatree_field_click('Store,Country', 2,1)
        time.sleep(7)
        metaobj.datatree_field_click('Revenue', 2,1)
        time.sleep(3)
        
        defcss="#pfjTableChart_1 path[class^='riser!s0!g3!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        
        
        parentcss="pfjTableChart_1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 7.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mregion!", 'sorbus_2', 'Step 7.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mregion!", 'elf_green', 'Step 7.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step03'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)


        """    "4. Review fex from inside IA. The GRAPH_JS_FINAL section has no URL.    """
        ribbonobj.select_top_toolbar_item('toolbar_showfex')
        
        utillobj.switch_to_frame(frame_css="iframe[id^='BiRichEdit']",pause=1)
        
        #fexeditor=self.driver.find_element_by_css_selector("div[id^='BiDialog'] iframe[id^='BiRichEdit']")
        
        
        fex_code = self.driver.find_element_by_css_selector("body>div").text
        expected_code = '"map_by_field": "WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.COUNTRY_NAME"'
        msg = "Step 4. Verify map_by_field: WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.COUNTRY_NAME   is displayed inside IA"
        bol=expected_code in fex_code
        utillobj.asequal(True, bol, msg)
        utillobj.switch_to_default_content(pause=3)
        
        okbtn_ele=self.driver.find_element_by_css_selector("#showFexOKBtn")
        
        utillobj.click_on_screen(okbtn_ele, coordinate_type='middle', click_type=0)
        
        time.sleep(5)
         

        """    5. Save with name C2320576 and close.    """
        utillobj.switch_to_default_content(pause=3)
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    "6. Run with API call:    """
        """    7. Review the html source of the output window. Scroll to the bottom after all the data, review the "extension" section. extension" section contains URL.    """
        """    8. Close output window.    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10660_esrimap_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        utillobj.switch_to_window(wndnum=0, pause=15)
        time.sleep(3)
        parentcss="jschart_HOLD_0"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 7.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mregion!", 'sorbus_2', 'Step 7.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mregion!", 'elf_green', 'Step 7.3 Verify map color')
        
        html_code = self.driver.page_source
        expected_code = '"url": "//services5.arcgis.com/bDCD6wpjQP5q0bHM/arcgis/rest/services/World_Reference_Mercator/FeatureServer/1"'
        msg = "Step 7.2 Verify the extension section in the view source page"
        bol=expected_code in html_code
        utillobj.asequal(True, bol, msg)
        

        
        
        
if __name__ == '__main__':
    unittest.main()
    
        
        
