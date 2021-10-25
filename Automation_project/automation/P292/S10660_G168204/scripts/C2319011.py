'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2319011
Test case Name =  Demographic layer with Silent Authentication 

'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2319011_TestClass(BaseTestCase):

    def test_C2319011(self):
    
        
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
        Test_Case_ID = "C2319011"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        #time.sleep(5)
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=60)
          
          
        """    2. Go to Format tab > "Choropleth"    """
        
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=25)
        time.sleep(9)
       
        """    "3. Click "Demographic Layers"    """
        
        
        ribbonobj.select_ribbon_item("Format", "demographiclayers")
        
        resultobj.wait_for_property("[id^='QbDemographicLayersDlg']", 1, expire_time=30)
        
        utillobj.verify_object_visible("[id^='QbDemographicLayersDlg']", True, 'Step 3. Verify Demographic Layers dialog')
        
        """    4. Check "USA Restaurant Spending 2014" > OK    """
        """    5. Verify the map is updated    """

        lifestyle_item='USA Restaurant Spending 2014'
        
        
#         wfmapobj.select_demographic_layer(lifestyle_list, population_list, btn_click='Ok')

        lifestyle_row_objs=self.driver.find_elements_by_css_selector("[id^='QbDemographicLayersDlg'] [id^='DemographicLayerGrid'] table tr")
        required_row_obj=lifestyle_row_objs[[el.text.strip() for el in lifestyle_row_objs].index(lifestyle_item)]
        utillobj.default_left_click(object_locator=required_row_obj,action_move=True)
        self.driver.find_element_by_css_selector("#demographicLayersDlgOkBtn").click()
        
        defcss="#pfjTableChart_1 text[class^='legend-labels']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        
        time.sleep(8)
        
        parentcss="pfjTableChart_1"
        expected_label_list_cr=['Series0','Series1','Series2','Series3','Series4']
        
        #utillobj.verify_picture_using_sikuli('step6.png')
        
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step05'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        msg="Step 5.1. Verify Map Legends"
         
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_cr, msg, custom_css="text[class^='legend-labels']", same_group=True)
        
        time.sleep(8)
        
        """    6. Double click "Store,Country", "Revenue"    """
        """    7. Verify the map is updated    """
        
       
        
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
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step07'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    8. Click "Run"    """
        """    9. Verify the map    """
        
   
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#jschart_HOLD_0 path[class^='riser!s0!g3!mregion!']", 1,expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 9.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mregion!", 'sorbus_2', 'Step 9.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mregion!", 'elf_green', 'Step 9.3 Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step09'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    10. Click "Layers"    """
        """    11. Verify the layers.    """
        
        utillobj.switch_to_frame(1)
        
        layer1="#jschart_HOLD_0 div[class^='TableOfContentsButton']"
         
        """Layer button verifications"""
        layerbutton=self.driver.find_element_by_css_selector(layer1)
        utillobj.verify_object_visible(layer1, True, "Step 11a. Verify Layers button visible")
        time.sleep(5)
        utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        
        time.sleep(8)
        
        nlist=[]
        layerlist=self.driver.find_elements_by_css_selector("#jschart_HOLD_0 table.esriLegendLayer  td:nth-child(2) > table > tbody > tr > td")
        nlist.extend([i.text for i in layerlist])
        print('Actual layer list', nlist)
        
        expected_layer_list=['$ 0 - 747 per year, per household', '$ 747 - 2,179 per year, per household', '$ 2,179 - 3,612 per year, per household', '$ 3,612 - 5,044 per year, per household', '$ 5,044 - 12,532 per year, per household', '$ 0 - 747 per year, per household', '$ 747 - 2,179 per year, per household', '$ 2,179 - 3,612 per year, per household', '$ 3,612 - 5,044 per year, per household', '$ 5,044 - 12,532 per year, per household', '$ 0 - 747 per year, per household', '$ 747 - 2,179 per year, per household', '$ 2,179 - 3,612 per year, per household', '$ 3,612 - 5,044 per year, per household', '$ 5,044 - 12,532 per year, per household', '$ 0 - 747 per year, per household', '$ 747 - 2,179 per year, per household', '$ 2,179 - 3,612 per year, per household', '$ 3,612 - 5,044 per year, per household', '$ 5,044 - 12,532 per year, per household', '$ 0 - 747 per year, per household', '$ 747 - 2,179 per year, per household', '$ 2,179 - 3,612 per year, per household', '$ 3,612 - 5,044 per year, per household', '$ 5,044 - 12,532 per year, per household']
        msg="Step 11b. Verify the Layers"
        
        utillobj.asequal(expected_layer_list,nlist, msg)
        
        
        """    12. Click "Save" icon    """
        """    13. Enter Title "C2319011" > Click "Save" and dismiss IA.    """
        
        utillobj.switch_to_default_content(pause=3)
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        
        """    14. Reopen the fex using API code:    """
        """    15. Verify the map is restored    """
        """    16. Dismiss IA    """
        
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        defcss="#pfjTableChart_1 path[class^='riser!s0!g3!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        
        
        parentcss="pfjTableChart_1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M'], "Step 7.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mregion!", 'sorbus_2', 'Step 7.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mregion!", 'elf_green', 'Step 7.3 Verify map color')
        
if __name__ == '__main__':
    unittest.main()
    
        
        