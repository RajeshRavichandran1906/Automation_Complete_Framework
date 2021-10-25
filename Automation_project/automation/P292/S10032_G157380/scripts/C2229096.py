'''
Created on Nov 15, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229096
TestCase Name = Verify Map with Define and Compute in Visualization 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, wf_map
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229096_TestClass(BaseTestCase):

    def test_C2229096(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229096'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        
#         nodeid = utillobj.parseinitfile('nodeid')
#         if nodeid == "unxrh7":
        x = 102
#         else:
#             x = 106
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=baseapp/wf_retail_lite
        """
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
         
        """
        Step 02: Click "Change" dropdown > "ESRI Choropleth"
        """
        ribbonobj.change_chart_type('choropleth_map')
        time.sleep(3)        
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)   
         
        """
        Step 03: Double click "Store,State,Province", "Revenue"
        """
        metaobj.datatree_field_click("Store,State,Province", 2, 1)
        time.sleep(4) 
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 922)
         
        metaobj.datatree_field_click("Revenue", 2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, x)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
         
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", x, 'Step03.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        legend=['Revenue', '0M', '82M', '164M', '245.9M', '327.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step03:d(i) Verify legend Title")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g50!mregion", "elf_green", "Step 03.c(i) Verify first bar color")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g42!mregion']")
        utillobj.click_on_screen(parent_elem, 'middle',mouse_duration=2.5,x_offset=10, y_offset=-10)
        time.sleep(1)
        expected_tooltip=['Store State Province:Alaska', 'Revenue:$5,725,954.71', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g42!mregion",expected_tooltip, "Step03.e: verify the default tooltip values",default_move=True)       
        time.sleep(5)
         
        """
        Step 04: Click "Layers"
        """
        layer1="div[class^='TableOfContentsButton UIButton']"
        layerbutton=driver.find_element_by_css_selector(layer1)
        utillobj.verify_object_visible(layer1, True, "Step 4a. Verify Layers button visible")
        time.sleep(1)
        try:
            print("Inside try")
            utillobj.click_on_screen(layerbutton, coordinate_type='middle') 
            utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
            css="div[class='toc-opacity-container']"
            elem1=(By.CSS_SELECTOR, css)
            resultobj._validate_page(elem1)
            utillobj.verify_object_visible(css, True, 'Step 05a: Verify the Opacity slider')
        except:
            print("Exception happened")
            utillobj.click_on_screen(layerbutton, coordinate_type='middle') 
            utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
            css="div[class='toc-opacity-container']"
            elem1=(By.CSS_SELECTOR, css)
            resultobj._validate_page(elem1)
            utillobj.verify_object_visible(css, True, 'Step 05a: Verify the Opacity slider')
          
        """
        Step 05: Verify the Opacity slider
        """
        time.sleep(4)
        expected_layer_list = ['World Admin Divisions', 'Opacity']
        layer_css="#MAINTABLE_wbody1 .toc-text"
        layer=driver.find_elements_by_css_selector(layer_css)
        my_iter_x1=[i.text for i in layer]
        print(my_iter_x1)
        my_iter_x=(i.text for i in layer)
        for label_x in expected_layer_list:
            if label_x in next(my_iter_x):
                statex= True
            else:
                statex=False
                break
        del my_iter_x
        utillobj.asequal(statex, True, "Step 05b: Verify the Opacity slider")
        layerwidget="div[class='TableOfContents']"
        utillobj.verify_object_visible(layerwidget, True, "Step 5c. Verify Layers widget visible")
        
        """
        Step 06: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)  
        
        """
        Step 07: Click "Layers"
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, x) 
        time.sleep(5)
        layer1="div[class^='TableOfContentsButton UIButton']"
        layerbutton=driver.find_element_by_css_selector(layer1)
        utillobj.click_on_screen(layerbutton, coordinate_type='middle')
        try:
            print("Inside try")
            utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        except:
            print("Exception happened")
            utillobj.click_on_screen(layerbutton, coordinate_type='middle', click_type=0)
        time.sleep(3)
        
        """
        Step 08: Drag the Opacity slider to approximately half way
        """
        css=".TableOfContents .toc-slider-handle"
        elem1=(By.CSS_SELECTOR, css)
        resultobj._validate_page(elem1)
        wfmapobj.drag_layer_slider(drag_offset=-15)
        time.sleep(8)
         
        """
        Step 09: Verify the map layer is updated
        """
        elem=driver.find_element_by_css_selector("[id*='MAINTABLE_wbody1_f_com-esri-map'][id*='layerId_0_layer']")
        a=utillobj.get_css_value(elem, "opacity")
        print(a)
        utillobj.asequal(int(a['opacity']), 0, "Step 09: Verify the map layer is updated")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", x, 'Step09.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g50!mregion", "elf_green", "Step09.c(i) Verify first bar color")
        legend=['Revenue', '0M', '82M', '164M', '245.9M', '327.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step09:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Alaska', 'Revenue:$5,725,954.71', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g42!mregion",expected_tooltip, "Step09.e: verify the default tooltip values")       
        time.sleep(5)
        
        """
        Step 10: Drag the opacity slider all the way to the right 
        """
        css=".TableOfContents .toc-slider-handle"
        elem1=(By.CSS_SELECTOR, css)
        resultobj._validate_page(elem1)
        wfmapobj.drag_layer_slider(drag_offset=30)
        time.sleep(8)
         
        """
        Step 11: Verify the map layer is updated
        """
        elem=driver.find_element_by_css_selector("[id*='MAINTABLE_wbody1_f_com-esri-map'][id*='layerId_0_layer']")
        b=utillobj.get_css_value(elem, "opacity")
        print(b)
        utillobj.asequal(int(b['opacity']), 1, "Step 11: Verify the map layer is updated")
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", x, 'Step11.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g50!mregion", "elf_green", "Step 11.c(i) Verify first bar color")
        legend=['Revenue', '0M', '82M', '164M', '245.9M', '327.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 11:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['Store State Province:Alaska', 'Revenue:$5,725,954.71', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g42!mregion",expected_tooltip, "Step 11.e: verify the default tooltip values")       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2229096_Actual_step11', image_type='actual',x=1, y=1, w=-1, h=-1)
         
        """
        Step 12: Dismiss the run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 13: Click "Save" icon
        Step 14: Enter Title "C2229096"
        Step 15: Click "Save" and dismiss IA
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5) 
               
if __name__ == '__main__':
    unittest.main()
