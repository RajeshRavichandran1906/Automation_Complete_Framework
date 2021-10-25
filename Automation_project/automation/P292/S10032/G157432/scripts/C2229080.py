'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229080
Test case Name =  Verify changing Bubble map from Lat/Long map
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon,  visualization_metadata,metadata
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase




class C2229080_TestClass(BaseTestCase):

    def test_C2229080(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        mobj=metadata.MetaData(self.driver)
        
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229080"
        Test_fex_name="C2229080"

        
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
        
        
        """    "4. Double click "Cost of Goods"    """
        """    "5. Drag "Store,Store,Latitude" into Geolocation bucket   """
        """    "6. Verify Georole dialog is prompted    """
        """    7. Select "Store,Store,Longitude" from Associated Coordinate dropdown > OK    """
        
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
        
        mobj.collapse_data_field_section('Sales->Measure Groups')
        time.sleep(5)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Store Latitude', 1, 'Layer', 0)
        
        resultobj.wait_for_property("div[id^='QbDialog']", 1, expire_time=30)
        time.sleep(4)
        """Niranjan needs to fix the action     """
        #wfmapobj.set_geo_role('Country', 'Name', btn_click='Ok')
        store_as="Store,Store Longitude"
        btn_click='Ok'
        set_assoc_obj=self.driver.find_element_by_css_selector("div[id^='QbDialog'] div[id='geoAssocCoordinateHBox'][style*='inherit'] div[id='cbAssocGeoCoordinate'] div[id^='BiButton']")
        utillobj.select_any_combobox_item(set_assoc_obj, store_as)
        time.sleep(1)
        self.driver.find_element_by_css_selector("#geoRole"+btn_click+"Btn").click()
        
      

        """    8. Verify the map is updated    """
        resultobj.wait_for_property("#pfjTableChart_1 circle[class^='riser!s0!g5!mmarker!']", 1, expire_time=90)
        
        parentcss="pfjTableChart_1"
        expected_label_list=['Cost of Goods']
        msg="Step 8.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 8.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g5!mmarker!", 'bar_blue', 'Step 8.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g16!mmarker!", 'bar_blue', 'Step 8.3b Verify map color')
        
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step08'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    "9. In the Query pane, right click "STORE_LATITUDE_STORE_LONGITUDE_POINT" > "Delete"    """
        """    10. Drag "Store,Country" into Geolocation bucket    """
        metaobj.querytree_field_click('STORE_LATITUDE_STORE_LONGITUDE_POINT', 1, 1, 'Delete')
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Country', 1, 'Layer', 0)
        time.sleep(5)

        """    11. Verify the map is updated    """
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#pfjTableChart_1 circle[class^='riser!s0!g33!mmarker!']", 1, expire_time=60)

        parentcss="pfjTableChart_1"
        expected_label_list=['Cost of Goods']
        msg="Step 11.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 11.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 11.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 11.3b Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step11'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        
        """    12. Click "Run"    """
        """    13. Verify the map is displayed correctly    """

        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_0', 1, expire_time=60)
        
        
        expected_label_list=['Cost of Goods']
        msg="Step 13.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 13.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 13.3a Verify map color at runtime')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 13.3b Verify map color at runtime')
        
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step13'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)


        
        """    14. Click "Save" icon    """
        """    15. Enter Title "C2229080"    """
        """    16. Click "Save" and dismiss IA window    """
        utillobj.switch_to_default_content(pause=3)

        ribbonobj.select_top_toolbar_item("toolbar_save")
        time.sleep(4)
        utillobj.ibfs_save_as(Test_fex_name)
        time.sleep(5)
        
        
        """    17. Reopen the fex using API code:    """
        """    18. Verify IA is launched, preserving the map    """
        """    19. Dismiss IA window    """
        """    20. Log out :    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_fex_name, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(3)
        
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, "#pfjTableChart_1 circle[class^='riser!s0!g33!mmarker!']", 1, expire_time=90)

        parentcss="pfjTableChart_1"
        expected_label_list=['Cost of Goods']
        msg="Step 11.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 11.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 11.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 11.3b Verify map color')


        
if __name__ == '__main__':
    unittest.main()
    
        