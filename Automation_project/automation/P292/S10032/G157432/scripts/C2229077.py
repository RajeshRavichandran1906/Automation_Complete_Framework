'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229077
Test case Name =  Verify ESRI TOC is displayed 
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata,wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229077_TestClass(BaseTestCase):

    def test_C2229077(self):
    
        
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        browser=utillobj.parseinitfile('browser')
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = "C2229077"
#         Test_Case_ID = "a"+browser_type
        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
         
        """    2. Go to Format tab    """
        """    3. Click "Choropleth"    """
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        utillobj.synchronize_with_number_of_element(defcss, 1, 90, 1)
        
        time.sleep(10)
         
        """    4. Double click "Store,Country", "Cost of Goods"    """
        metaobj.datatree_field_click('Store,Country', 2,1)
        metaobj.datatree_field_click('Cost of Goods', 2,1)
         
        """    "5. Click "Layers" and verify the "Layers" displayed correctly    """
        """layers code to come here"""
        layer1="div[class^='TableOfContentsButton']"
         
         
        layerwidget="div[class='TableOfContents']"
        layertitle="div[class='toc-text'][title='World Countries']"
        layeropacity="div[class='toc-opacity-container']"
         
        """Layer button verifications"""
        layerbutton=self.driver.find_element_by_css_selector(layer1)
        utillobj.verify_object_visible(layer1, True, "Step 5a. Verify Layers button visible")
         
        utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        time.sleep(4)
        utillobj.verify_object_visible(layerwidget, True, "Step 5b. Verify Layers widget visible")
        utillobj.verify_object_visible(layertitle, True, "Step 5c. Verify Layers title visible")
        utillobj.verify_object_visible(layeropacity, True, "Step 5d. Verify Layers opacity slider visible")
         
         
         
        defcss="#pfjTableChart_1 path[class^='riser!s0!g3!mregion!']"
        utillobj.synchronize_with_number_of_element(defcss, 1, 90, 1)
        
        time.sleep(8)
         
        parentcss="pfjTableChart_1"
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '98M', '196M', '294M', '392M'], "Step 5.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mregion!", 'sorbus_2', 'Step 5.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mregion!", 'elf_green', 'Step 5.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step05'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """    "6. Click "Run"    """
        """    "7. Click "Layers"    """
        """    "8. Verify the "Layers" is displayed correctly    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        #visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_0', 1, expire_time=60)
         
         
         
        defcss="#jschart_HOLD_0 path[class^='riser!s0!g3!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(8)
         
        """Layer button verifications"""
        layerbutton=self.driver.find_element_by_css_selector(layer1)
        utillobj.verify_object_visible(layer1, True, "Step 8a. Verify Layers button visible")
         
        utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        time.sleep(4)
        utillobj.verify_object_visible(layerwidget, True, "Step 8b. Verify Layers widget visible")
        utillobj.verify_object_visible(layertitle, True, "Step 8c. Verify Layers title visible")
        utillobj.verify_object_visible(layeropacity, True, "Step 8d. Verify Layers opacity slider visible")
 
         
         
        iaresult.verify_color_scale_esri_maps(parentcss, ['Cost of Goods', '0M', '98M', '196M', '294M', '392M'], "Step 5.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g3!mregion!", 'sorbus_2', 'Step 5.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mregion!", 'elf_green', 'Step 5.3 Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
         
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step08'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """    "9. Click "Propotional Symbol" in the Format tab    """
        """    10. Click "Layers"    """
        """    11. Verify the "Layers" is displayed correctly    """
        ribbonobj.select_ribbon_item("Format", "proportional_symbol")
        defcss="#pfjTableChart_1 circle[class^='riser!s0!g2!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(5)
        tocheadercss="#pfjTableChart_1 div[class='toc-header']"
        tocvisible=self.driver.find_element_by_css_selector(tocheadercss).is_displayed()
        
        if tocvisible==True:
            tocheader=self.driver.find_element_by_css_selector(tocheadercss)
            utillobj.click_on_screen(tocheader, coordinate_type='middle', click_type=2)
            time.sleep(4)
            
        layerbutton=self.driver.find_element_by_css_selector("#pfjTableChart_1 div[class^='TableOfContentsButton UIButton']")
            
#         utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
#         time.sleep(4)
#          
        """Layer button verifications"""
        
        utillobj.verify_object_visible("#pfjTableChart_1 div[class^='TableOfContentsButton UIButton']", True, "Step 11a. Verify Layers button visible")
         
        utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        time.sleep(4)
        utillobj.verify_object_visible(layerwidget, True, "Step 11b. Verify Layers widget visible")
        utillobj.verify_object_visible(layertitle, True, "Step 11c. Verify Layers title visible")
        utillobj.verify_object_visible(layeropacity, True, "Step 11d. Verify Layers opacity slider visible")
 
         
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
        """    13. Click "Layers"    """
        """    14. Verify the "Layers" is displayed correctly    """
        """    15. Dismiss IA window (Do not save changes)    """
        """    16. Log out :    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(6)
        utillobj.switch_to_frame(1)
        parentcss="jschart_HOLD_0"
        #visualization_resultarea.Visualization_Resultarea.wait_for_property(self, '#jschart_HOLD_0', 1, expire_time=60)
        defcss="#jschart_HOLD_0 circle[class^='riser!s0!g33!mmarker!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1)
        time.sleep(8)
         
        """Layer button verifications"""
        layerbutton=self.driver.find_element_by_css_selector(layer1)
        utillobj.verify_object_visible(layer1, True, "Step 14a. Verify Layers button visible")
         
        utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        time.sleep(4)
        utillobj.verify_object_visible(layerwidget, True, "Step 14b. Verify Layers widget visible")
        utillobj.verify_object_visible(layertitle, True, "Step 14c. Verify Layers title visible")
        utillobj.verify_object_visible(layeropacity, True, "Step 14d. Verify Layers opacity slider visible")
 
         
        expected_label_list=['Cost of Goods']
        msg="Step 14.1. Verify Map Legends"
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list, msg, custom_css="text[class^='legend-labels']", same_group=True)
        expected_title_list=['Cost of Goods']
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_title_list, 'Step 14.2. Verify Legend title', custom_css="text[class^='sizeLegend-title']", same_group=True)
        utillobj.verify_chart_color(parentcss, "riser!s0!g33!mmarker!", 'bar_blue', 'Step 14.3a Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g2!mmarker!", 'bar_blue', 'Step 14.3b Verify map color')
        utillobj.switch_to_default_content(pause=3)
        img1=self.driver.find_element_by_css_selector("#resultArea div[class$='window-content-pane']")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step14'+'_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
       
if __name__ == '__main__':
    unittest.main()
    
        
