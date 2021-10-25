'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229079
Test case Name =  Verify Bubble map with AutoDrill
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon,  visualization_metadata,ia_resultarea
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229079_TestClass(BaseTestCase):

    def test_C2229079(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229079"
        Test_fex_name="C2229079"

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
#         time.sleep(10)
        
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
            
            
        """    2. Go to Format tab    """
        """    3. Click "Proportional Symbol" esri map from Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
#         ribbonobj.switch_ia_tab('Format')
#         
        ribbonobj.switch_ia_tab('Home')
        time.sleep(6)
          
        """    "4. Drag "Store,Country" to Geolocation    """
        """    "5. Drag "Revenue" to Size    """
        """    "6. Click "Auto Drill"    """
          
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Country', 1, 'Layer', 0)
          
        time.sleep(4)
          
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue', 1, 'Size', 0)
          
          
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#pfjTableChart_1 circle[class^='riser!s0!g33!mmarker!']", 1, expire_time=60)
  
        parentcss="pfjTableChart_1"
          
        expected_label_list=['Revenue']
        msg="Step 5.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 5.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
          
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 5.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 5.3b Verify map color')
  
    
        time.sleep(4)
          
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
          
        """    7. Click "Run"    """
        """    8. Verify the map is displayed correctly at runtime    """

        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(pause=3)
        time.sleep(3)
#         WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
#         time.sleep(3)
        utillobj.switch_to_frame(frame_css='iframe[src]', frame_height_value=0)
        time.sleep(3)
        defcss="#jschart_HOLD_0 circle[class^='riser!s0!g33!mmarker!']"
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=30)
        expected_label_list=['Revenue']
        msg="Step 8.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Revenue']
         
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 8.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 8.3a Verify map color at runtime')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 8.3b Verify map color at runtime')
         
        utillobj.switch_to_default_content(pause=3)
        
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step8'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
         
        
        """    "9. Hover over US bubble    """
        """    10. Verify the tooltip and Auto Drill menu    """
        frame_height=utillobj.get_frame_height()
        frame_height_def=frame_height['ia_frame_height']
        utillobj.switch_to_frame(pause=3)
        time.sleep(3)
#         WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        utillobj.switch_to_frame(frame_css="iframe[src*='contentDrill']", frame_height_value=frame_height_def)
        time.sleep(10)
#         circle1=driver.find_element_by_css_selector("#jschart_HOLD_0 circle[class^='riser!s0!g33!mmarker!']")
#         utillobj.click_on_screen(circle1, coordinate_type='top_middle')
        expected_tooltip=['Store Country:United States', 'Revenue:$545,792,166.40', 'Drill down to Store State Province']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g33!mmarker!",expected_tooltip, "Step 10.: Verify Tooltip is displayed correctly")
        
        """    11. Select "Drill down to Store,State,Province"    """
        """    12. Verify the map drills down correctly    """
        
        #iaresult.select_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g33!mmarker!', 'Drill down to Store State Province',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g33!mmarker!', 'Drill down to Store State Province',wait_time=1)
        time.sleep(3)
        #utillobj.switch_to_frame(frame_css='iframe[src]', frame_height_value=0)
        time.sleep(4)
        
        resultobj.wait_for_property("#jschart_HOLD_0 circle[class^='riser!s0!g9!mmarker!']", 1, expire_time=60)
        time.sleep(9)
        parentcss="jschart_HOLD_0"
        expected_label_list=['Revenue']
        msg="Step 12.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 12.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g9!mmarker!", 'bar_blue', 'Step 12.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g21!mmarker!", 'bar_blue', 'Step 12.3b Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step12'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        """    13. Hover over New York bubble    """
        """    14. Verify the tooltip and Auto Drill menu    """
        utillobj.switch_to_frame(pause=3)
        time.sleep(3)
#         WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        utillobj.switch_to_frame(frame_css='iframe[src]', frame_height_value=frame_height_def)
        time.sleep(3)
#         circle1=driver.find_element_by_css_selector("#jschart_HOLD_0 circle[class^='riser!s0!g21!mmarker!']")
#         utillobj.click_on_screen(circle1, coordinate_type='top_middle')
#         time.sleep(3)
        expected_tooltip=['Store State Province:New York|United States', 'Revenue:$25,902,385.29', 'Restore Original', 'Drill up to Store Country', 'Drill down to Store City']
        resultobj.verify_default_tooltip_values("jschart_HOLD_0","riser!s0!g21!mmarker!",expected_tooltip, "Step 14.: Verify Tooltip is displayed correctly")
        """    15. Select "Restore Original"    """
        """    16. Verify the map is reset    """
        iaresult.select_ia_autolink_tooltip_menu('jschart_HOLD_0', 'riser!s0!g21!mmarker!', 'Restore Original',wait_time=1, x_offset_menu=20, y_offset_menu=8)
        time.sleep(4)
        resultobj.wait_for_property("#jschart_HOLD_0 circle[class^='riser!s0!g33!mmarker!']", 1, expire_time=60)
        #parentcss="pfjTableChart_1"
        
        expected_label_list=['Revenue']
        msg="Step 16.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 16.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 16.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 16.3b Verify map color')

        time.sleep(4)
        """    17. Click "Save" icon    """
        """    18. Enter Title "C2229079"    """
        """    19. Click "Save" and dismiss IA    """
        utillobj.switch_to_default_content(pause=3)

        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_fex_name)
        time.sleep(5)
        
        
        """    20. Reopen the fex using API code:    """
        """    21. Verify IA is launched, preserving the map    """
        """    22. Dismiss IA window    """
        """    23. Log out :    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_fex_name, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(3)
        
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#pfjTableChart_1 circle[class^='riser!s0!g33!mmarker!']", 1, expire_time=60)

        parentcss="pfjTableChart_1"
        
        expected_label_list=['Revenue']
        msg="Step 21.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 21.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 21.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 21.3b Verify map color')


        
if __name__ == '__main__':
    unittest.main()
    
        