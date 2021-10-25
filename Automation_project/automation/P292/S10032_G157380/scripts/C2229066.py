'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229066
Test case Name =  Verify Color By in a Choropleth map
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229066_TestClass(BaseTestCase):

    def test_C2229066(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        driver.implicitly_wait(15)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229066"
#         Test_Case_ID = "a"+browser_type
        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        #time.sleep(5)
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
          
          
        """    2. Go to Format tab    """
        """    3. Click "Choropleth" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
        ribbonobj.switch_ia_tab('Format')
        ribbonobj.switch_ia_tab('Home')
#          
#          
          
        """    4. Double click "Customer,Country"    """
        metaobj.datatree_field_click('Customer,Country', 2,1)
          
          
        """    5. Drag "Customer,Continent" into Color bucket    """
        metaobj.datatree_field_click('Customer,Continent', 1, 1, 'Add To Query', 'Color')
          
          
        """    6. Verify the map is updated    """
        parentcss="pfjTableChart_1"
        expected_label_list=['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        msg="Step 6.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
#         resultobj.verify_riser_legends(parentcss, expected_label_list, msg)
        expected_title_list=['Customer Continent']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 6.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        utillobj.verify_chart_color(parentcss, "riser!s4!g0!mregion!", 'brick_red', 'Step 6.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step06'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
  
          
        """    7. Click "Run"    """
        """    8. Verify the correct map is displayed at runtime    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(16)
        utillobj.switch_to_frame(1)
         
        parentcss1="jschart_HOLD_0"
        expected_label_list=['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        msg="Step 8.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
#         resultobj.verify_riser_legends(parentcss, expected_label_list, msg)
        resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_title_list, 'Step 8.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        utillobj.verify_chart_color(parentcss1, "riser!s4!g0!mregion!", 'brick_red', 'Step 8.3 Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step08'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    9. Click "Save" icon    """
        """    10. Enter Title "CHORO_COLOR_BY"    """
        """    11. Click "Save" and dismiss IA window    """

        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    12. Run the saved fex using API code.    """
        """    13. Verify the map    """
        """    14. Dismiss the map window    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex', 'S10032_esrimap_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        utillobj.switch_to_window(wndnum=0, pause=15)
        riserele="#jschart_HOLD_0 [class^='riser!s4!g0!mregion!']"
        resultobj.wait_for_property(riserele, 1, expire_time=60)
        
        time.sleep(8)
        parentcss="jschart_HOLD_0"
        expected_label_list=['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        msg="Step 13.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
#         resultobj.verify_riser_legends(parentcss, expected_label_list, msg)
        expected_title_list=['Customer Continent']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list , 'Step 13.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        utillobj.verify_chart_color(parentcss, "riser!s4!g0!mregion!", 'brick_red', 'Step 13.3 Verify map color')
        
        
        """    15. Reopen the fex using API code:    """
        """    16. Verify IA is launched, preserving the map    """
        """    17. Log out :    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#pfjTableChart_1', 1)
        defcss="pfjTableChart_1"
        time.sleep(7)
        expected_label_list=['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        msg="Step 16.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(defcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
#         resultobj.verify_riser_legends(parentcss, expected_label_list, msg)
        resultobj.verify_riser_pie_labels_and_legends(defcss, expected_title_list, 'Step 16.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        utillobj.verify_chart_color(defcss, "riser!s4!g0!mregion!", 'brick_red', 'Step 16.3 Verify map color')
      
        
if __name__ == '__main__':
    unittest.main()
    
        