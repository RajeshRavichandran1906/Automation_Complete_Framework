'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229074
Test case Name =  Verify map with multiple Reference Layers 

'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229074_TestClass(BaseTestCase):

    def test_C2229074(self):
    
        
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
        Test_Case_ID = "C2229074"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        element_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(element_css, 1, 90, 1)
          
          
        """    2. Go to Format tab > "Choropleth"    """
        """    3. Select "Chorpleth"    """
        
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        utillobj.synchronize_with_number_of_element(defcss, 1, 90, 1)
        time.sleep(9)
        
        
        """    4. Double click "Store,State,Province", "Cost of Goods"    """
        metaobj.datatree_field_click('Store,State,Province', 2,1)
        
        resultobj.wait_for_property("#pfjTableChart_1 path[class^='riser!s0!g92!mregion!']", 1, expire_time=40)
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2,1)
        time.sleep(5)
        
       
        """    "5. Click "Reference Layers" in the Format tab    """
        """    "6. Verify the Reference Layers dialog    """

        ribbonobj.switch_ia_tab('Format')
        #ribbonobj.select_ribbon_item("Format", "referencelayers")
        
        utillobj.synchronize_with_number_of_element('#FormatReferenceLayers img', 1, 20, 1)
        time.sleep(3)
        parent_elem=self.driver.find_element_by_css_selector('#FormatReferenceLayers img')
        
        utillobj.click_on_screen(parent_elem, 'middle', 0)
#         ele=self.driver.find_element_by_css_selector('#FormatReferenceLayers img')
#         ele.click()
        
        resultobj.wait_for_property("[id^='QbReferenceLayersDlg']", 1, expire_time=30)
        
        utillobj.verify_object_visible("[id^='QbReferenceLayersDlg']", True, 'Step 6. Verify Reference Layers dialog')
        
        """    7. Check "World Countries", "USA_States_Generalized" > OK    """
        """    8. Verify the Reference Layers are drawn    """

        layer_list=[('World Countries',0), ('USA States Generalized',0)]
        
        
        wfmapobj.select_reference_layer(layer_list, btn_click='Ok')
        
        defcss="#pfjTableChart_1 path[class^='riser!s0!g50!mregion']"
        
        resultobj.wait_for_property(defcss, 1, expire_time=30)
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '59M', '117.8M', '176.7M', '235.6M'], "Step 8.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g42!mregion!", 'punch', 'Step 8.2a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g50!mregion!", 'elf_green', 'Step 8.2b Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step08'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        time.sleep(6)
                                 
        """    "9. Click "Run"    """
        """    10. Verify the map is displayed correctly    """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#jschart_HOLD_0 path[class^='riser!s0!g50!mregion!']", 1,expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '59M', '117.8M', '176.7M', '235.6M'], "Step 10.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g42!mregion!", 'punch', 'Step 10.2a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g50!mregion!", 'elf_green', 'Step 10.2b Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step10'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
         
        """    11. Click "Save" icon    """
        """    12. Enter Title "C2229074"    """
        """    13. Click "Save" and dismiss IA """
        
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        
        """    14. Reopen the fex using API code:    """
        """    15. Verify the map is restored    """
        """    16. Dismiss IA    """
        """    17. Log out :   """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        defcss="#pfjTableChart_1 path[class^='riser!s0!g50!mregion!']"
        
        utillobj.synchronize_with_number_of_element(defcss, 1, 90, 1)
        
        parentcss="pfjTableChart_1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '59M', '117.8M', '176.7M', '235.6M'], "Step 15.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g42!mregion!", 'punch', 'Step 15.2a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g50!mregion!", 'elf_green', 'Step 15.2b Verify map color')
        
if __name__ == '__main__':
    unittest.main()
    
        
        