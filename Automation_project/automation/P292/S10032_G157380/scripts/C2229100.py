'''
Created on Nov 17, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229100
TestCase Name = Verify Show grid and Reset chart options 
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, visualization_run, ia_run
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229100_TestClass(BaseTestCase):

    def test_C2229100(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229100'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        iarunobj = ia_run.IA_Run(self.driver)
        
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
        Step 03: Double click "Store,Country", "Revenue"
        """
        metaobj.datatree_field_click("Store,Country", 2, 1)
        time.sleep(4) 
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 41)
          
        metaobj.datatree_field_click("Revenue", 2,1)
        time.sleep(4)
        parent_css="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css, 33)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 6)
          
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step03.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 03.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step03:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step 03.e: verify the default tooltip values",default_move=True)       
        time.sleep(5)
        
        """
        Step 04: Click "Run"
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)  
        
        """
        Step 05: Verify the map in a new window
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, 33) 
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step05.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 05.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 05:d(i) Verify legend Title")
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step05.e: verify the default tooltip values",default_move=True)       
        time.sleep(5)
         
        """
        Step 06: Click the chart options menu
        Step 07: Click the "Show grid" option
        """
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"show_report")
        time.sleep(6)
         
        """
        Step 08: Verify the grid report is displayed
        """
        time.sleep(5)
#         iarunobj.create_table_data_set('#MAINTABLE_wbody2 table table', "C2229100.xlsx")
        iarunobj.verify_table_data_set('#MAINTABLE_wbody2 table table', "C2229100.xlsx", 'Step 08: Verify the grid report')
         
        """
        Step 09: Click the "Show grid" option
        """
        time.sleep(5)
        show_report_css="#MAINTABLE_menuContainer1 span[onclick*='show'] img"
        driver.find_element_by_css_selector(show_report_css).click()
        time.sleep(10)
        
        """
        Step 10: Verify the map is displayed
        """
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, 33) 
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step10.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 10.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 10:d(i) Verify legend Title")
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip= ['Store Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step10.e: verify the default tooltip values",default_move=True)       
        time.sleep(5)
        
        """
        Step 11: Hover over the United Stated > "Exlcude from Chart"
        """ 
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(2)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g19!mregion']")
        utillobj.click_on_screen(parent_elem, 'top_middle',javascript_marker_enable=True,mouse_duration=2.5,x_offset=0, y_offset=-15)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g19!mregion",'Exclude from Chart',wait_time=1,default_move=True)
        
        """
        Step 12: Verify the map is filtered
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, 32) 
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 32, 'Step12.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g5!mregion", "persian_red", "Step 12.c(i) Verify first bar color")
        legend=['Revenue', '0M', '13M', '26M', '39M', '52M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 12:d(i) Verify legend Title")
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step12.e: verify the default tooltip values",default_move=True)       
        time.sleep(5)
        
        """
        Step 13: Hover over the Australia > "Exlcude from Chart"
        """ 
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'bottom_middle')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        resultobj.select_default_tooltip_menu("MAINTABLE_wbody1", "riser!s0!g0!mregion",'Exclude from Chart',wait_time=1,default_move=True)
       
        """
        Step 14: Verify the map is filtered
        """
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, 31) 
        time.sleep(2)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 31, 'Step14.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mregion", "persian_red", "Step 14.c(i) Verify first bar color")
        legend=['Revenue', '0M', '13M', '26M', '39M', '52M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 14:d(i) Verify legend Title")
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g2!mregion']")
        utillobj.click_on_screen(parent_elem, 'bottom_middle',mouse_duration=2.5,x_offset=-10, y_offset=-70)
        time.sleep(1)
        expected_tooltip=['Store Country:Canada', 'Revenue:$51,147,788.36', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mregion",expected_tooltip, "Step14.e: verify the default tooltip values",default_move=True)       
        time.sleep(5)
        
        """
        Step 15: Click the "+" button to zoom in one level
        """
        zoom_button_css=driver.find_element_by_css_selector("div[class^='esriSimpleSliderIncrementButton'] span")
        try:
            print("Inside try")
            utillobj.click_on_screen(zoom_button_css, 'middle')
            time.sleep(1)
            utillobj.click_on_screen(zoom_button_css, 'middle', click_type=0, mouse_duration=2.5)
        except:
            print("Exception")
            utillobj.click_on_screen(zoom_button_css, 'middle')
            time.sleep(1)
            utillobj.click_on_screen(zoom_button_css, 'middle', click_type=0, mouse_duration=2.5)
        
        time.sleep(15)
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, 31) 
        
        expected_label_list = ['2000km', '1000mi']
        scale_bar_css="[class*='esriScalebarSecondNumber']"
        layer=driver.find_elements_by_css_selector(scale_bar_css)
        my_iter_x1=[i.text for i in layer]
        print(my_iter_x1)
        my_iter_x=(i.text for i in layer)
        for label_x in expected_label_list:
            if label_x in next(my_iter_x):
                statex= True
            else:
                statex=False
                break
        del my_iter_x
        utillobj.asequal(statex, True, "Step 15: Verify the scale bar line label")
        
        time.sleep(3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 31, 'Step15.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g4!mregion", "persian_red", "Step 15.c(i) Verify first bar color")
        legend=['Revenue', '0M', '13M', '26M', '39M', '52M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 15:d(i) Verify legend Title")
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g2!mregion']")
        utillobj.click_on_screen(parent_elem, 'left',mouse_duration=2.5,x_offset=50, y_offset=80)
        time.sleep(1)
        expected_tooltip=['Store Country:Canada', 'Revenue:$51,147,788.36', 'Filter Chart', 'Exclude from Chart', 'Remove Filter']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g2!mregion",expected_tooltip, "Step15.e: verify the default tooltip values",default_move=True)       
        time.sleep(5)
        
        """
        Step 16: Click the chart options menu
        Step 17: Click "reset chart" option
        """
        vis_runobj.select_run_menu_option('MAINTABLE_menuContainer1',"reset")
        time.sleep(10)
        
        """
        Step 18: Verify the original map is restored
        """
        chart_type_css="#MAINTABLE_wbody1 path[class*='riser!s0!g0!mregion!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css2="#MAINTABLE_wbody1 path[class^='riser']"
        resultobj.wait_for_property(parent_css2, 33) 
        time.sleep(4)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 33, 'Step18.a: Verify number of risers displayed', custom_css="path[class^='riser']")
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g33!mregion", "elf_green", "Step 18.c(i) Verify first bar color")
        legend=['Revenue', '0M', '136.5M', '273M', '409.4M', '545.8M']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 18:d(i) Verify legend Title")
        move1 = self.driver.find_element_by_css_selector("#MAINTABLE_wbody1")
        utillobj.click_on_screen(move1, 'start')
        time.sleep(5)
        parent_elem=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g0!mregion']")
        utillobj.click_on_screen(parent_elem, 'start',mouse_duration=2.5,x_offset=40, y_offset=30)
        time.sleep(1)
        expected_tooltip=['Store Country:Australia', 'Revenue:$1,260,307.29', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mregion",expected_tooltip, "Step18.e: verify the default tooltip values",default_move=True)       
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2229100_Actual_step18', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 19: Dismiss the run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 20: Click "Save" icon
        Step 21: Enter Title "C2229100"
        Step 22: Click "Save" and dismiss IA
        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5) 
               
if __name__ == '__main__':
    unittest.main()