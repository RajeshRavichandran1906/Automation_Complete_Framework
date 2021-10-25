'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2334339
Test case Name =  Visualization - Basemaps configured in server
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2334339_TestClass(BaseTestCase):

    def test_C2334339(self):
    
        
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
        Test_Case_ID = "C2334339"
        

        
        """    1. Use API call to open IA in chart mode with wf_retail_lite:    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10660', 'mrid', 'mrpass')
        #time.sleep(5)
        resultobj.wait_for_property("#MAINTABLE_wbody1", 1, expire_time=60)
          
          
        """    2. Change > ESRI Choropleth    """
        ribbonobj.change_chart_type('choropleth_map')
        time.sleep(5)
        defcss="#pfjTableChart_1 div img[class^='layerTile'][src*='World_Light_Gray']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=25)
        time.sleep(9)
        lightgray_css="#pfjTableChart_1 div img[class^='layerTile'][src*='World_Light_Gray']"
        utillobj.verify_object_visible(lightgray_css, True, 'Step 2. Verify Default gray basemap displays in preview')
        
        

        """    Step 3. Click Format > Background    """
        """    Step 4. Select World Topographical Map    """
        
        ribbonobj.select_ribbon_item('Format','Background')
        chart_type_css="div[id^='BaseMapLayersPopup'][class*='bi-window active window'] img[src*='topo_map']"
        chart_elem = self.driver.find_element_by_css_selector(chart_type_css)
        elem1=(By.CSS_SELECTOR, chart_type_css)
        ribbonobj._validate_page(elem1)
        utillobj.default_left_click(object_locator=chart_elem)
        time.sleep(3)
        topomap_css="#pfjTableChart_1 div img[class^='layerTile'][src*='World_Topo_Map']"
        resultobj.wait_for_property(topomap_css, 1, expire_time=50)
        
        utillobj.verify_object_visible(topomap_css, True, 'Step 4. Verify World Topographical Map displayed in preview')
        
        
        """    Step 5. Double click Store,State,Province & Revenue    """
        """    Step 5.1. Verify preview    """
         
        metaobj.datatree_field_click('Store,State,Province', 2,1)
        time.sleep(7)
        metaobj.datatree_field_click('Revenue', 2,1)
        time.sleep(3)
        
        defcss="#MAINTABLE_wbody1 path[class^='riser!s0!g42!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        
        topomap_css="#MAINTABLE_wbody1 div img[class^='layerTile'][src*='World_Topo_Map']"
        utillobj.verify_object_visible(topomap_css, True, 'Step 5. Verify World Topographical Map displayed in preview')
        
        
        parentcss="MAINTABLE_wbody1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 5.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g42!mregion!", 'punch', 'Step 5.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g50!mregion!", 'elf_green', 'Step 5.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #MAINTABLE_wbody1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step05'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        
        """    "Step 6. Run inside IA    """
        
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        utillobj.switch_to_window(1)
        time.sleep(15)
        
        defcss="#MAINTABLE_wbody1 circle[class^='riser!s0!g42!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        topomap_css="#MAINTABLE_wbody1 div img[class^='layerTile'][src*='World_Topo_Map']"
        utillobj.verify_object_visible(topomap_css, True, 'Step 6. Verify World Topographical Map displayed in runtime')
        
        parentcss="MAINTABLE_wbody1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 6.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g42!mregion!", 'punch', 'Step 6.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g50!mregion!", 'elf_green', 'Step 6.3 Verify map color')
        
        """    Step 7. Click Save > enter name C2334339 > Save. Close window.    """
        
        utillobj.switch_to_window(0)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        """    Step 8. Restore chart in IA editor with API    """
        """    Step 9. Close IA window.   """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10660', mrid='mrid', mrpass='mrpass')
        time.sleep(3)
        
        defcss="#MAINTABLE_wbody1 circle[class^='riser!s0!g42!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        
        topomap_css="#MAINTABLE_wbody1 div img[class^='layerTile'][src*='World_Topo_Map']"
        utillobj.verify_object_visible(topomap_css, True, 'Step 8. Verify World Topographical Map displayed in preview')
        
        
        parentcss="MAINTABLE_wbody1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 8.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g42!mregion!", 'punch', 'Step 8.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g50!mregion!", 'elf_green', 'Step 8.3 Verify map color')
        

        
        
        
if __name__ == '__main__':
    unittest.main()
    
        
        
