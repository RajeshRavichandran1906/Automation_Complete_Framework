'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229075
Test case Name =  Verify converting between map types
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229075_TestClass(BaseTestCase):

    def test_C2229075(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj=metadata.MetaData(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229075"
#         Test_Case_ID = "a"+browser_type
        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('C2229075', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        #time.sleep(5)
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
        
        
        """    2. Go to Format tab    """
        """    3. Click "Choropleth" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
         
        """    4. Double click "Store,Country", "Cost of Goods"    """
        """    5. Drag "Store,Business,Region" into "Multi-graph" bucket    """
        """    6. Verify the map is updated    """
        metaobj.datatree_field_click('Store,Country', 2, 1)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        
        metadataobj.collapse_data_field_section('Sales->Measure Groups')  
        
        metadataobj.expand_data_field_section('Dimensions->Store->Store')
        time.sleep(6)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Business,Region', 1, 'Multi-graph', 0)
        
        parentcss="pfjTableChart_1"
        resultobj.wait_for_property("#TableChart_1 path[class^='riser!s0!g1!mregion!']", 1, expire_time=90)
        time.sleep(8)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '9.3M', '18.6M', '27.9M', '37.2M'], "Step 6.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g5!mregion!", 'crusta2', 'Step 6.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'persian_red', 'Step 6.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g27!mregion!", 'sea_green1', 'Step 6.4 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step06'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """    7. Multi-select "Gross Profit", "Revenue"    """
        """    8. Drag the fields into "Tooltip" bucket    """
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit', 1, 'Tooltip', 0)
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue', 1, 'Gross Profit', 0)
        defcss="#TableChart_1 path[class^='riser!s0!g27!mregion!']"
        utillobj.synchronize_with_number_of_element(defcss, 1, 120, 1)
        
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '9.3M', '18.6M', '27.9M', '37.2M'], "Step 8.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g5!mregion!", 'crusta2', 'Step 8.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'persian_red', 'Step 8.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g27!mregion!", 'sea_green1', 'Step 8.4 Verify map color')

        """    9. Click "Run"    """
        """    10. Verify the maps    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_3', 1,expire_time=60)
        utillobj.verify_object_visible('#jschart_HOLD_0', True, 'Step 09a. Verify Chart1')
        utillobj.verify_object_visible('#jschart_HOLD_1', True, 'Step 09a. Verify Chart2')
        utillobj.verify_object_visible('#jschart_HOLD_2', True, 'Step 09a. Verify Chart3')
        utillobj.verify_object_visible('#jschart_HOLD_3', True, 'Step 09a. Verify Chart4')
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '9.3M', '18.6M', '27.9M', '37.2M'], "Step 10.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g5!mregion!", 'crusta2', 'Step 10.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'persian_red', 'Step 10.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g27!mregion!", 'sea_green1', 'Step 10.4 Verify map color')
        time.sleep(10)
        
        """    11. Hover over a country    """
        """    12. Verify the tooltips displays all fields    """
        expected_tooltip=['Store Business Region:EMEA', 'Store Country:China', 'Cost of Goods:$50,702.00', 'Gross Profit:$19,408.18', 'Revenue:$70,110.18']
        resultobj.verify_default_tooltip_values('jschart_HOLD_0',"riser!s0!g1!mregion!",expected_tooltip, "Step 12: Verify Tooltip is displayed correctly")

        """    13. Click "Save" icon    """
        """    14. Enter Title "C2229075"    """
        """    15. Click "Save" and dismiss IA    """
        utillobj.switch_to_default_content(pause=3)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        
        """    16. Reopen the fex using API code:    """
        """    17. Verify IA is launched, preserving the map    """
        """    18. Dismiss IA window    """
        """    19. Log out :    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        defcss="#TableChart_1 path[class^='riser!s0!g27!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '9.3M', '18.6M', '27.9M', '37.2M'], "Step 10.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g5!mregion!", 'crusta2', 'Step 10.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'persian_red', 'Step 10.3 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g27!mregion!", 'sea_green1', 'Step 10.4 Verify map color')
        
        
        
if __name__ == '__main__':
    unittest.main()
    
    
        
        