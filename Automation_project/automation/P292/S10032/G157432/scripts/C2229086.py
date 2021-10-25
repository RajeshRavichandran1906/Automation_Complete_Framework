'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229086
Test case Name =  Verify Map using Joined files 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata,ia_ribbon
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase




class C2229086_TestClass(BaseTestCase):

    def test_C2229086(self):
    
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229086"
        Test_fex_name="C2229086"

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/dimensions/wf_retail_geography','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
        #time.sleep(6)
          
        """    2. Go to Data tab > "Join"    """
        """    "3. Verify the Join dialog    """
        """    "4. Click "Add New"    """
        """    "5. Select new_retail/dimensions/wf_retail_store > "Open"    """
        ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_store")
        time.sleep(8)
         
           
        if browser_type=="Firefox":
             
            ia_ribbonobj.create_join_link(0, "ID_GEOGRAPHY", 1, "ID_GEOGRAPHY", source_scroll_down=9, target_scroll_down=2)
        else:
            ia_ribbonobj.create_join_link(0, "ID_GEOGRAPHY", 1, "ID_GEOGRAPHY", source_scroll_down=13, target_scroll_down=2)
             
                       
        """    "6. Drag "ID_GEOGRAPHY" from the first pane to "ID_GEOGRAPHY" in the second pane    """
        time.sleep(8)
        ia_ribbonobj.select_join_menu_buttons("ok")
        
        """    "7. Click "Add New"    """
        """    "8. Select new_retail/facts/wf_retail_sales > "Open"    """
        """    "9. Drag "ID_STORE" from the second pane to "ID_STORE" in the third pane    """
        """    10. Click OK    """
         
        time.sleep(8)
#         ia_ribbonobj.select_join_menu_buttons("ok")
#         time.sleep(10)
        ia_ribbonobj.create_join("new_retail->facts->wf_retail_sales")
        if browser_type=="Firefox":
            ia_ribbonobj.create_join_link(1, "ID_STORE", 2, "ID_STORE", source_scroll_down=2)
        else:
            ia_ribbonobj.create_join_link(1, "ID_STORE", 2, "ID_STORE", source_scroll_down=3)
         
        time.sleep(5)
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 09a: Verify the Link color is Red for 2nd Join")
        ia_ribbonobj.verify_join_link_color(0, 'blue', "Step 09a: Verify the Link color is Blue for 1st Join")
        ia_ribbonobj.select_join_menu_buttons("ok")
        time.sleep(4)
        """    11. Go to Format tab > "Proportional Symbol"    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
        ribbonobj.switch_ia_tab('Home')
        time.sleep(10)
           
        """    12. Double click "Country", "Revenue"    """
        """    13. Drag "Business,Sub Region" into Color bucket    """
        metaobj.datatree_field_click("Country", 2, 1)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(6) 
        metaobj.datatree_field_click('Business,Sub Region', 1, 0, 'Add To Query', 'Color')
        
        resultobj.wait_for_property("#pfjTableChart_1 circle[class^='riser!s13!g0!mmarker!']", 1, expire_time=60) 
        
        time.sleep(6) 
         
        """    14. Verify the map is displayed correctly    """
        parentcss="pfjTableChart_1"
         
        utillobj.verify_chart_color(parentcss, "riser!s13!g0!mmarker!", 'tea_green', 'Step 14.1a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s9!g0!mmarker!", 'kournikova', 'Step 14.1b Verify map color')
        expected_label_list=['Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico', 'Midwest', 'Northeast', 'SA-Port', 'SA-Span', 'South', 'Southeast', 'West']
        msg="Step 14.2. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Business Sub Region']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 14.3. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 14.4. Verify Size Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step14'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
         
         
        """    15. Click "Run"    """
        """    16. Verify the map is displayed correctly    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_0', 1)
         
         
        utillobj.verify_chart_color(parentcss, "riser!s13!g0!mmarker!", 'tea_green', 'Step 16.1a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s9!g0!mmarker!", 'kournikova', 'Step 16.1b Verify map color')
        expected_label_list=['Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico', 'Midwest', 'Northeast', 'SA-Port', 'SA-Span', 'South', 'Southeast', 'West']
        msg="Step 16.2. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Business Sub Region']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 16.3. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 16.4. Verify Size Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step16'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)

 
         
        """    17. Click "Save" icon    """
        """    18. Enter Title "C2229086"    """
        """    19. Click "Save" and dismiss IA window    """
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
         
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#pfjTableChart_1', 1)
        time.sleep(10)
        parentcss="pfjTableChart_1"
        utillobj.verify_chart_color(parentcss, "riser!s13!g0!mmarker!", 'tea_green', 'Step 21.1a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s9!g0!mmarker!", 'kournikova', 'Step 21.1b Verify map color')
        expected_label_list=['Africa', 'Asia', 'Australia-New Zealand', 'Canada', 'East', 'Europe', 'Mexico', 'Midwest', 'Northeast', 'SA-Port', 'SA-Span', 'South', 'Southeast', 'West']
        msg="Step 21.2. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Business Sub Region']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 21.3. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        expected_title_list=['Revenue']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 21.4. Verify Size Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)        
         

        
if __name__ == '__main__':
    unittest.main()
    
        