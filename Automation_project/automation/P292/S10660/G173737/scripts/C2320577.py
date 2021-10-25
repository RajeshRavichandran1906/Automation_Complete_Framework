'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2320577
Test case Name =  Proportional Chart - Json is created by server
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2320577_TestClass(BaseTestCase):

    def test_C2320577(self):
    
        
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
        Test_Case_ID = "C2320577"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10660', 'mrid', 'mrpass')
        #time.sleep(5)
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
          
          
        """    2. Format > Chart Type > Esri Proportional    """
        
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=25)
        time.sleep(9)

        """    Step 3. Expand 'Query Variables' in data pane > Double click 'Store,European Union'    """
        """    Step 4. Double click Store > 'Store,City' & Sales > 'Revenue'    """
        """    Step 5. Drag Sales > 'Gross Profit' to Color bucket    """

        
        
        metaobj.datatree_field_click('Filters and Variables->Store,European Union', 2,1)
        time.sleep(7)
        metaobj.datatree_field_click('Store,City', 2,1)
        time.sleep(7)
        metaobj.datatree_field_click('Revenue', 2,1)
        time.sleep(3)
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit', 1, 'Color', 0)
        
        
        
        defcss="#pfjTableChart_1 circle[class^='riser!s0!g12!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        
        
        parentcss="pfjTableChart_1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '2.3M', '4.5M', '6.7M', '9M'], "Step 5.1")
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 5.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g10!mmarker!", 'mantis1', 'Step 5.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mmarker!", 'koromiko', 'Step 5.4 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step05'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        
        """    "6. Review fex from inside IA. The GRAPH_JS_FINAL section has no URL.    """
        ribbonobj.select_top_toolbar_item('toolbar_showfex')
        
        utillobj.switch_to_frame(frame_css="iframe[id^='BiRichEdit']",pause=1)
        
        #fexeditor=self.driver.find_element_by_css_selector("div[id^='BiDialog'] iframe[id^='BiRichEdit']")
        
        
        fex_code = self.driver.find_element_by_css_selector("body>div").text
        expected_code = '"map_by_field": "WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.CITY_NAME"'
        msg = "Step 6. Verify map_by_field: WF_RETAIL_LITE.WF_RETAIL_GEOGRAPHY_STORE.CITY_NAME   is displayed inside IA"
        bol=expected_code in fex_code
        utillobj.asequal(True, bol, msg)
        utillobj.switch_to_default_content(pause=3)
        
        okbtn_ele=self.driver.find_element_by_css_selector("#showFexOKBtn")
        
        utillobj.click_on_screen(okbtn_ele, coordinate_type='middle', click_type=0)
        
        time.sleep(5)
         

        """    7. Save with name C2320577 and close.    """
        utillobj.switch_to_default_content(pause=3)
        
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    "8. Run with API call:    """
        """    9. Review the html source of the output window. Scroll to the bottom after all the data, review the "extension" section. extension" section contains URL.    """
        """  10. Close output window.    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10660_esrimap_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        utillobj.switch_to_window(wndnum=0, pause=15)
        time.sleep(3)
        parentcss="jschart_HOLD_0"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '2.3M', '4.5M', '6.7M', '9M'], "Step 8.1")
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 8.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g10!mmarker!", 'mantis1', 'Step 8.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mmarker!", 'koromiko', 'Step 8.4 Verify map color')
        
        html_code = self.driver.page_source
        expected_code = '"url": "//services.arcgis.com/P3ePLMYs2RVChkJx/ArcGIS/rest/services/World_Cities/FeatureServer/0"'
        msg = "Step 9.2 Verify the extension section in the view source page"
        bol=expected_code in html_code
        utillobj.asequal(True, bol, msg)


        
        
        
if __name__ == '__main__':
    unittest.main()
    
        
        
