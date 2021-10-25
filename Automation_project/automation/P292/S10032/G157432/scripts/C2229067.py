'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229067
Test case Name =  Verify map with postal code
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229067_TestClass(BaseTestCase):

    def test_C2229067(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229067"
        Test_fex_name="Choro_ZIP"

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#TableChart_1", 1, 90, 1)
          
        """    2. Go to Format tab    """
        """    3. Click "Choropleth"    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        utillobj.synchronize_with_number_of_element(defcss, 1, 90, 1)
          
        ribbonobj.switch_ia_tab('Home')
        time.sleep(6)
#         
        """    4. Double click "Revenue"    """
        metaobj.datatree_field_click('Revenue', 2,1)
          
          
        """    5. Right click "Store,Postal,Code" > "Map As" > "5 Digit Zipcode    """
        metaobj.datatree_field_click('Store,Postal,Code', 1, 1, 'Map As', '5 Digit Zipcode')
          

        """    "6. Drag "Store,Postal,Code" into Location > Layer    """
        
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Postal,Code', 1, 'Layer', 0)
        
          
        """    7. Verify the map is updated    """
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 7.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g67!mregion!", 'persian_red2', 'Step 7.2 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step07'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
  
          
        """    8. Click "Run"    """
        """    9. Verify the map is displayed correctly    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss1="jschart_HOLD_0"
        utillobj.synchronize_with_number_of_element(parentcss1, 1, 90, 1)
        

        
         
        
        iaresult.verify_color_scale_esri_maps(parentcss1, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 7.1")
        time.sleep(5)
        utillobj.verify_chart_color(parentcss1, "riser!s0!g67!mregion!", 'persian_red2', 'Step 9.2 Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step09'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    9. Click "Save" icon    """
        """    11. Enter Title "Choro_ZIP"    """
        """    12. Click "Save" and dismiss IA window    """
        utillobj.switch_to_default_content(pause=3)

        ribbonobj.select_top_toolbar_item('toolbar_save')
        
        time.sleep(4)
        utillobj.ibfs_save_as(Test_fex_name)
        time.sleep(5)
        
        """    13. Run the saved fex using API code.    """
        """    14. Verify the map    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_fex_name+'.fex', 'S10032_esrimap_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        utillobj.switch_to_window(wndnum=0, pause=15)
        
        elem1="#jschart_HOLD_0 [class^='riser!s0!g67!mregion!']"
        utillobj.synchronize_with_number_of_element(elem1, 1, 90, 1)
        
        time.sleep(8)
        parentcss="jschart_HOLD_0"
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 14.1")
        time.sleep(5)
        utillobj.verify_chart_color(parentcss, "riser!s0!g67!mregion!", 'persian_red2', 'Step 14.2 Verify map color')
        
        
        """    15. Hover over a marker, Verify the tooltip is displayed correctly    """
        """    16. Dismiss the map window    """
        
        expected_tooltip=['Store Postal Code:82604', 'Revenue:$1,228,116.63']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g67!mregion",expected_tooltip, "Step 15: Verify Tooltip is displayed correctly")       
        
        """    17. Reopen the fex using API code:    """
        """    18. Verify IA is launched, preserving the map    """
        """    19. Log out :    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_fex_name, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        utillobj.synchronize_with_number_of_element('#pfjTableChart_1', 1, 120, 1)
        defcss="pfjTableChart_1"
        time.sleep(7)
        iaresult.verify_color_scale_esri_maps(defcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 18.1")
        utillobj.verify_chart_color(defcss, "riser!s0!g67!mregion!", 'persian_red2', 'Step 18.2 Verify map color')
        
        

        
if __name__ == '__main__':
    unittest.main()
    
        