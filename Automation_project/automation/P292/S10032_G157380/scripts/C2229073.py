'''
Created on Mar 22, 2017

@author: Robert

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229073
Test case Name =  Verify multiple Demographic Layers 

'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_metadata, wf_map
from common.lib import utillity 
import time
from common.lib.basetestcase import BaseTestCase



class C2229073_TestClass(BaseTestCase):

    def test_C2229073(self):
    
        
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
        Test_Case_ID = "C2229073"
        

        
        """    1. Launch the IA API with Chart in edit mode    """
#         utillobj.infoassist_api_edit('a', 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        utillobj.infoassist_api_login('chart','new_retail/wf_retail_lite','P292/S10032', 'mrid', 'mrpass')
        resultobj.wait_for_property("#TableChart_1", 1, expire_time=90)
          
          
        """    2. Go to Format tab > "Choropleth"    """
        
        ribbonobj.select_ribbon_item("Format", "Choropleth")
        defcss="#pfjTableChart_1"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=25)
        time.sleep(9)
       
        """    "3. Click "Demographic Layers"    """
        """    "4. Verify the dialog appear correctly    """
        
        ribbonobj.select_ribbon_item("Format", "demographiclayers")
        
        resultobj.wait_for_property("[id^='QbDemographicLayersDlg']", 1, expire_time=30)
        
        utillobj.verify_object_visible("[id^='QbDemographicLayersDlg']", True, 'Step 4. Verify Demographic Layers dialog')
        
        """    "5. Check "USA Population Density 2014", "USA Tapestry Segmentation 2012" > OK    """
        """    "6. Verify the map is updated    """

        lifestyle_list=[('USA Tapestry Segmentation 2012',0)]
        population_list=[('USA Population Density 2014',4)]
        
        wfmapobj.select_demographic_layer(lifestyle_list, population_list, btn_click='Ok')
        
        defcss="#pfjTableChart_1 text[class^='legend-labels']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        
        parentcss="pfjTableChart_1"
        expected_label_list_cr=['Series0','Series1','Series2','Series3','Series4']
        
        #utillobj.verify_picture_using_sikuli('step6.png')
        
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step06'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        msg="Step 17.1. Verify Map Legends"
         
        resultobj.verify_riser_pie_labels_and_legends(parentcss, expected_label_list_cr, msg, custom_css="text[class^='legend-labels']", same_group=True)
        
        time.sleep(8)
        
        """    "7. Right click "Store,State,Province" > "Map As" > "US State (Name)"    """
        """    "8. Double click "Store,State,Province", "Revenue"    """
        """    "9. Verify the map is updated    """
        
        metaobj.datatree_field_click('Store,State,Province', 1,1,'Map As', 'US State (Name)')
        
        time.sleep(3)
        
        metaobj.datatree_field_click('Store,State,Province', 2,1)
        time.sleep(3)
        metaobj.datatree_field_click('Revenue', 2,1)
        time.sleep(3)
        
        defcss="#pfjTableChart_1 path[class^='riser!s0!g1!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1,expire_time=25)
        
        
        parentcss="pfjTableChart_1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 9.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'punch', 'Step 9.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mregion!", 'elf_green', 'Step 9.3 Verify map color')
        img1=self.driver.find_element_by_css_selector("#resultArea #pfjTableChart_1")
        utillobj.take_screenshot(img1,Test_Case_ID+'_Actual_step09'+'_'+browser_type, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """    10. Click "Run"    """
        """    11. Verify the map    """
        
   
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
        
        
        """    12. Click "Layers"    """
        """    13. Uncheck "US States Generalized"    """
        """    14. Uncheck "USA Tapestry Segmentation 2012"    """
        utillobj.switch_to_frame(1)
        
        layer1="#jschart_HOLD_0 div[class^='TableOfContentsButton']"
         
        """Layer button verifications"""
        layerbutton=self.driver.find_element_by_css_selector(layer1)
        utillobj.verify_object_visible(layer1, True, "Step 12a. Verify Layers button visible")
        time.sleep(5)
        utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        
        op1="#jschart_HOLD_0 div[class='toc-container'] div[title='USA Tapestry Segmentation 2012']"
        op2="#jschart_HOLD_0 div[class='toc-container'] div[title='USA_States_Generalized']"
        
        op1_ele=self.driver.find_element_by_css_selector(op1)
        op1_ele.click()
        
        op2_ele=self.driver.find_element_by_css_selector(op2)
        op2_ele.click()
           
        tocheadercss="#jschart_HOLD_0 div[class='toc-header']"
        tocvisible=self.driver.find_element_by_css_selector(tocheadercss).is_displayed()
        
        if tocvisible==True:
            tocheader=self.driver.find_element_by_css_selector(tocheadercss)
            utillobj.click_on_screen(tocheader, coordinate_type='middle', click_type=2)
            time.sleep(4)
        
        """    15. Click "Save" icon    """
        """    16. Enter Title "C2229073"    """
        """    17. Click "Save" and dismiss IA """
        utillobj.switch_to_default_content(pause=3)
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        
        
        """    18. Reopen the fex using API code:    """
        """    19. Verify the map is restored    """
        """    20. Dismiss IA    """
        """    21. Log out :   """
        
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'P292/S10032', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        defcss="#pfjTableChart_1 path[class^='riser!s0!g1!mregion!']"
        visualization_resultarea.Visualization_Resultarea.wait_for_property(self, defcss, 1, expire_time=50)
        
        
        parentcss="pfjTableChart_1"
        
        iaresult.verify_color_scale_esri_maps(parentcss, ['Revenue', '0M', '82M', '164M', '245.9M', '327.8M'], "Step 19.1")
        utillobj.verify_chart_color(parentcss, "riser!s0!g1!mregion!", 'punch', 'Step 19.2 Verify map color')
        utillobj.verify_chart_color(parentcss, "riser!s0!g25!mregion!", 'elf_green', 'Step 19.3 Verify map color')
        
if __name__ == '__main__':
    unittest.main()
    
        
        