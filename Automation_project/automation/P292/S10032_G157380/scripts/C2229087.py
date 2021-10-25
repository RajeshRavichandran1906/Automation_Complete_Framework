'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229087
Test case Name =  Verify map with InfoMini 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,define_compute,wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229087_TestClass(BaseTestCase):

    def test_C2229087(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        
        driver.implicitly_wait(15)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229087"
        Test_fex_name="C2229087"

         
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
           
           
        """    2. Go to Format tab    """
        """    3. Click "Proportional Symbol" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
#         ribbonobj.switch_ia_tab('Format')
#         
        ribbonobj.switch_ia_tab('Home')
        time.sleep(6)
         
        """    "4. Double click "Store,Country", "Cost of Goods"    """
        """    "5. Drag "Gross Profit" to Color bucket    """
        """    "6. Click "InfoMini" in the ribbon    """
 
         
        metaobj.datatree_field_click("Store,Country", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit', 1, 'Color', 0)
        time.sleep(5)
         
        ribbonobj.select_ribbon_item("Format", "infomini")
         
        """    "7. Click "Run"    """
        """    "8. Verify InfoMini is run in a new window, displaying the map    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_window(1)
        time.sleep(2)
        utillobj.switch_to_frame(pause=2)
         
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_0', 1)
         
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 8.1. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
         
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '38.4M', '76.9M', '115.3M', '153.7M'], "Step 8.2")
         
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'elf_green', 'Step 8.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mmarker!", 'flame_pea1', 'Step 8.3b Verify map color')
         
        """    9. Click "Format" tab    """
        """    10. Select "Active Report"    """
        """    11. Click "Run"    """
        """    12. Verify the map is run    """
 
        utillobj.switch_to_window(1)
        #ribbonobj.select_ribbon_item("Format", "active_report")
        f_tab="#FormatTab_tabButton"
        f_active="#FormatReportActive img"
         
        f_tab_ele=self.driver.find_element_by_css_selector(f_tab)
         
        utillobj.click_on_screen(f_tab_ele, coordinate_type='middle', click_type=0)
         
        time.sleep(5)
         
        f_active_ele=self.driver.find_element_by_css_selector(f_active)
         
        utillobj.click_on_screen(f_active_ele, coordinate_type='middle', click_type=0)
         
        time.sleep(5)
         
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(10)
         
        parentcss="MAINTABLE_wbody0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#MAINTABLE_wbody0', 1)
         
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 12.1. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
         
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '38.4M', '76.9M', '115.3M', '153.7M'], "Step 12.2")
         
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'elf_green', 'Step 12.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mmarker!", 'flame_pea1', 'Step 12.3b Verify map color')
         
         
        """    13. Click "Save" icon    """
        """    14. Enter Title "C2229087"    """
        """    15. Click "Save" and dismiss InfoMini and IA windows    """
         
        utillobj.switch_to_default_content(pause=1)
 
        ribbonobj.select_top_toolbar_item('infomini_save')
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """    16. Run the fex with the following API from the resource tree:    """
        """    17. Verify the InfoMini map is run    """
        """    18. Dismiss the map window     """
         
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        utillobj.active_run_fex_api_login(Test_fex_name+'.fex', 'S10032_esrimap_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        utillobj.switch_to_window(wndnum=1, pause=15)
        
        time.sleep(3)
        
        
        utillobj.switch_to_frame(pause=2)
        defcss="#MAINTABLE_wbody0 circle[class^='riser!s0!g33!mmarker!']"
        parentcss="MAINTABLE_wbody0"
        resultobj.wait_for_property(defcss, 1)
        time.sleep(10)
        
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 17.1. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '38.4M', '76.9M', '115.3M', '153.7M'], "Step 17.2")
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'elf_green', 'Step 17.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mmarker!", 'flame_pea1', 'Step 17.3b Verify map color')
        
        """    19. Reopen the fex using API code:    """
        """    20. Verify IA is launched, preserving the map    """
        """    21. Dismiss IA window    """
        """    22. Log out :    """
        
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_fex_name, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(3)
        
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#pfjTableChart_1', 1)
        time.sleep(10)
        parentcss="pfjTableChart_1"
        
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 20.1. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        iaresult.verify_color_scale_esri_maps(parentcss, ['Gross Profit', '0M', '38.4M', '76.9M', '115.3M', '153.7M'], "Step 17.2")
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'elf_green', 'Step 20.2a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mmarker!", 'flame_pea1', 'Step 20.2b Verify map color')        
        

        
if __name__ == '__main__':
    unittest.main()
    
        