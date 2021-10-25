'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229089
Test case Name =  Verify re-assigning georole using "Map As" menu 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229089_TestClass(BaseTestCase):

    def test_C2229089(self):
    
        
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
        Test_Case_ID = "C2229089"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
          
          
        """    2. Go to Format tab    """
        """    3. Click "Choropleth"    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(9)
       
        
        """    "4. Right click "Store,State,Province" > "Map As" > "State/Province..."    """
        """    "5. Verify the Georole dialog    """
        metaobj.datatree_field_click('Store,State,Province', 1,1,'Map As', 'State/Province...')
        time.sleep(3)
        georolebox="body[id=wndApp] div[id^='QbDialog']"
        resultobj.wait_for_property(georolebox, 1, expire_time=60)
        
        utillobj.verify_object_visible(georolebox, True, "Step 5. Verify Georole dialog")
        
        """    "6. Click "Geographic Role" dropdown > "US State"    """
        """    "7. Select "Stored As" = "Name" > OK    """
        wfmapobj.set_geo_role(role_name='US State', store_as='Name', btn_click='Ok')
        
        utillobj.verify_object_visible(georolebox, False, "Step 5. Wait for Georole dialog to close")
        
        time.sleep(5)
        
        """    "8. Double click "Store,State,Province", "Revenue"    """
        """    "9. Verify the map is displayed    """
        metaobj.datatree_field_click('Store,State,Province', 2,1)
        time.sleep(3)
        metaobj.datatree_field_click('Revenue', 2,1)
        time.sleep(3)
        
        parentcss="pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#pfjTableChart_1 path[class^='riser!s0!g1!mregion!']", 1,expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 9.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'punch', 'Step 9.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mregion!", 'elf_green', 'Step 9.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step09'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """    10. Click "Run"    """
        """    11. Verify the map is displayed correctly    """
        """    12. Dismiss the run window    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#jschart_HOLD_0 path[class^='riser!s0!g1!mregion!']", 1,expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 11.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'punch', 'Step 11.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mregion!", 'elf_green', 'Step 11.3 Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step11'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        
        """    12. Dismiss the run window    """
        """    13. Click "Save" icon    """
        """    14. Enter Title "C2229089"    """
        """    15. Click "Save" and dismiss IA    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        
        """    16. Reopen the fex using API code:    """
        """    17. Verify the map is restored    """
        """    18. Dismiss IA    """
        """    19. Log out :   """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        parentcss="pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#pfjTableChart_1 path[class^='riser!s0!g1!mregion!']", 1,expire_time=60)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 17.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'punch', 'Step 17.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mregion!", 'elf_green', 'Step 17.3 Verify map color')

        
if __name__ == '__main__':
    unittest.main()
    
        
        