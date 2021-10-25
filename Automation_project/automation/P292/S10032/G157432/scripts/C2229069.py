'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229069
Test case Name =  Verify Color By in a Bubble map
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229069_TestClass(BaseTestCase):

    def test_C2229069(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        metadataobj=metadata.MetaData(self.driver)
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229069"
        Test_fex_name="C2229069"

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
          
          
        """    2. Go to Format tab    """
        """    3. Click "Proportional Symbol" in Chart Types group    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1"
        utillobj.synchronize_with_number_of_element(defcss, 1, 120, 1)
        
#         ribbonobj.switch_ia_tab('Format')
#         
        ribbonobj.switch_ia_tab('Home')
        time.sleep(6)
#         
        """    4. Double click "Customer,Country" "Revenue"    """
        metaobj.datatree_field_click('Customer,Country', 2,1)
        metaobj.datatree_field_click('Revenue', 2,1)
        
        metadataobj.collapse_data_field_section('Sales->Measure Groups')  
        
        metadataobj.expand_data_field_section('Customer,Country')
        time.sleep(6)  
        """    "5. Drag "Customer,Continent" into Color bucket    """
        metaobj.drag_drop_data_tree_items_to_query_tree('Customer,Continent', 1, 'Color', 0)

          
        """    6. Verify the map is updated    """
        parentcss="pfjTableChart_1"
        element_css="#pfjTableChart_1 text[class^='legend-labels']"
        utillobj.synchronize_with_number_of_element(element_css, 6, 60, 1)
        
        expected_label_list=['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        msg="Step 6.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
#         resultobj.verify_riser_legends(parentcss, expected_label_list, msg)
        expected_title_list=['Customer Continent']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 6.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        
        element_css="#pfjTableChart_1 circle[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(element_css, 42, 120, 1)
        
        utillobj.verify_chart_color(parentcss, "riser!s3!g2!mmarker!", 'pale_yellow', 'Step 6.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s2!g2!mmarker!", 'dark_green', 'Step 6.3b Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step06'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
  
          
        """    7. Click "Run"    """
        """    8. Verify the map is displayed correctly    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss1="jschart_HOLD_0"
        

        element_css="#jschart_HOLD_0 text[class^='legend-labels']"
        utillobj.synchronize_with_number_of_element(element_css, 6, 120, 1) 
        
        msg="Step 8.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
#         resultobj.verify_riser_legends(parentcss, expected_label_list, msg)
        expected_title_list=['Customer Continent']
        resultobj.verify_riser_pie_labels_and_legends(parentcss1, expected_title_list, 'Step 8.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        element_css="#jschart_HOLD_0 circle[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(element_css, 42, 120, 1)
        
        utillobj.verify_chart_color(parentcss1, "riser!s3!g2!mmarker!", 'pale_yellow', 'Step 8.3a Verify map color')
        utillobj.verify_chart_color(parentcss1, "riser!s2!g2!mmarker!", 'dark_green', 'Step 8.3b Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step08'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    9. Click "Save" icon    """
        """    10. Enter Title "C2229069"    """
        """    11. Click "Save" and dismiss IA window    """
        utillobj.switch_to_default_content(pause=3)

        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_fex_name)
        
        
        """    12. Run the saved fex.    """
        """    13. Verify the map is run in a new window    """
        """    14. Dismiss the map window    """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.active_run_fex_api_login(Test_fex_name+'.fex', 'S10032_esrimap_1', mrid='mrid', mrpass='mrpass')
        utillobj.switch_to_window(wndnum=0, pause=15)

        element_css="#jschart_HOLD_0 text[class^='legend-labels']"
        utillobj.synchronize_with_number_of_element(element_css, 6, 120, 1)
        
        parentcss="jschart_HOLD_0"
        msg="Step 13.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
#         resultobj.verify_riser_legends(parentcss, expected_label_list, msg)
        expected_title_list=['Customer Continent']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 13.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        
        element_css="#jschart_HOLD_0 circle[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(element_css, 42, 120, 1)
        
        utillobj.verify_chart_color(parentcss, "riser!s3!g2!mmarker!", 'pale_yellow', 'Step 13.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s2!g2!mmarker!", 'dark_green', 'Step 13.3b Verify map color')
        
        """    15. Reopen the fex using API code:    """
        """    16. Verify IA is launched, preserving the map    """
        """    17. Dismiss IA window    """
        """    18. Log out :    """
        utillobj.infoassist_api_logout()
        
        utillobj.infoassist_api_edit(Test_fex_name, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        element_css="#pfjTableChart_1 text[class^='legend-labels']"
        utillobj.synchronize_with_number_of_element(element_css, 6, 60, 1)
        
        parentcss="pfjTableChart_1"
        expected_label_list=['Africa', 'Asia', 'Europe', 'North America', 'Oceania', 'South America']
        msg="Step 16.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)

        expected_title_list=['Customer Continent']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 16.2. Verify Legend title', custom_css="text[class^='legend-title']", same_group=True)
        time.sleep(5)
        element_css="#pfjTableChart_1 circle[class*='riser!s']"
        utillobj.synchronize_with_number_of_element(element_css, 42, 120, 1)
        utillobj.verify_chart_color(parentcss, "riser!s3!g2!mmarker!", 'pale_yellow', 'Step 16.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s2!g2!mmarker!", 'dark_green', 'Step 16.3b Verify map color')
        
        

        
if __name__ == '__main__':
    unittest.main()
    
        