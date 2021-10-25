'''
Created on Nov 20, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2229106
TestCase Name = Verify Bubble map with single point zooms correctly
'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, wf_map, visualization_properties
from common.locators.visualization_resultarea_locators import VisualizationResultareaLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2229106_TestClass(BaseTestCase):

    def test_C2229106(self):
        driver = self.driver #Driver reference object created
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2229106'
        
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        wfmapobj=wf_map.Wf_Map(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=idis&master=ibisamp/car
        """
        utillobj.infoassist_api_login('idis','ibisamp/car','P292/S10032_esrimap_2', 'mrid', 'mrpass')
        parent_css="#pfjTableChart_1>svg>g.chartPanel rect[class*='riser!s0!g0!mbar!']"
        resultobj.wait_for_property(parent_css,1)
        
        """
        Step 02: Click "Change" dropdown > "Proportional Symbol"
        """
        ribbonobj.change_chart_type("bubble_map")
        time.sleep(5)
        parent_css="[class*='esriScalebarSecondNumber']"
        resultobj.wait_for_property(parent_css,2)
        
        """
        Step 03: Drag "COUNTRY" into Filter pane
        """
        time.sleep(4)
        metaobj.drag_drop_data_tree_items_to_filter("COUNTRY", 1)        
        time.sleep(6)
                
        """
        Step 04: Uncheck "[All]"
        Step 05: Check "ITALY" > OK
        """
        elem=(By.CSS_SELECTOR,'#avFilterOkBtn')
        metaobj._validate_page(elem)            
        item_list=['[All]','ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        metaobj.select_or_verify_visualization_filter_values(item_list, verify='true')
        time.sleep(2)
        l=['[All]', 'ITALY']               
        metaobj.create_visualization_filters('alpha',['Operator','Equal to'],['GridItems',l])
        time.sleep(3)
        
        """
        Step 06: Double click "SALES"
        """ 
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4)
        
        """
        Step 07: Double click "COUNTRY"
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        
        """ 
        Step 08. Set "Geographic Role" = Country
        Step 09. Set "Stored As" = "Name"
        Step 10. Click OK
        """
        time.sleep(3)
        elem=(By.CSS_SELECTOR,'#geoRoleCancelBtn')
        resultobj._validate_page(elem)
        wfmapobj.set_geo_role(role_name='Country', store_as='Name', btn_click='Ok')
        time.sleep(3)
        
        """
        Step 11: Verify the map is zoomed correctly
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 1, 'Step 11.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 11.c(i) Verify first bar color")
        legend=['SALES', 'SALES', '30,200']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step11:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['COUNTRY:ITALY', 'SALES:30200']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 11.e: verify the default tooltip values")       
        time.sleep(5)
        metaobj.verify_filter_pane_field('COUNTRY',1,"Step 11: Verify 'COUNTRY' appears in filter pane")
        propertyobj.select_or_verify_show_prompt_item('1', 'ITALY',verify=True, verify_type=True, msg="Step11:Verify prompt 'ITALY' is checked")
        time.sleep(5)
        
        expected_label_list = ['200km', '100mi']
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
        utillobj.asequal(statex, True, "Step 11: Verify the map is zoomed correctly")
        
        """
        Step 12: Click Run
        """
        time.sleep(10)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(15) 
        
        """
        Step 13: Verify the map is zoomed correctly
        """
        chart_type_css="#MAINTABLE_wbody1 circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 1, 'Step 13.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 13.c(i) Verify first bar color")
        legend=['SALES', 'SALES', '30,200']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step13:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['COUNTRY:ITALY', 'SALES:30200']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 13.e: verify the default tooltip values")       
        propertyobj.select_or_verify_show_prompt_item('1', 'ITALY',verify=True, verify_type=True, msg="Step13:Verify prompt 'ITALY' is checked")
        
        expected_label_list = ['200km', '100mi']
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
        utillobj.asequal(statex, True, "Step 13: Verify the map is zoomed correctly")
        
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2229106_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 14: Dismiss the map run window
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
         
        """
        Step 15: Click "Save" icon
        Step 16: Enter Title "C2229106"
        Step 17: Click "Save" and dismiss IA
        """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(10)
        utillobj.infoassist_api_logout()
        time.sleep(2)
         
        """
        Step 18: Right click the saved fex > "Run"
        """ 
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex','S10032_esrimap_2','mrid','mrpass')
        time.sleep(10)
        
        """
        Step 19: Verify the map is zoomed correctly
        """
        chart_type_css="#MAINTABLE_wbody1 circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 1, 'Step 19.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 19.c(i) Verify first bar color")
        legend=['SALES', 'SALES', '30,200']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 19:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['COUNTRY:ITALY', 'SALES:30200']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 19.e: verify the default tooltip values")       
        propertyobj.select_or_verify_show_prompt_item('1', 'ITALY',verify=True, verify_type=True, msg="Step 19:Verify prompt 'ITALY' is checked")
        expected_label_list = ['200km', '100mi']
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
        utillobj.asequal(statex, True, "Step 19: Verify the map is zoomed correctly")
        time.sleep(5)
        
        """
        Step 20: Dismiss the map run window
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
              
        """
        Step 21: Right click the saved fex > "Edit"
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'idis', 'S10032_esrimap_2',mrid='mrid',mrpass='mrpass')
        time.sleep(10)
             
        """
        Step 22: Verify IA is launched, preserving the map
        """
        elem=(By.CSS_SELECTOR,'#MAINTABLE_wbody1')
        resultobj._validate_page(elem)
        chart_type_css="circle[class*='riser!s0!g0!mmarker!']"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        parent_css="#MAINTABLE_wbody1 circle[class^='riser']"
        resultobj.wait_for_property(parent_css, 1)
        parent_css="#MAINTABLE_wbody1 .legend text"
        resultobj.wait_for_property(parent_css, 3)
        iaresultobj.verify_number_of_chart_segment("MAINTABLE_wbody1", 1, 'Step 22.b: Verify number of bubble displayed', custom_css="svg g>circle[class^='riser!s']")
        time.sleep(2)
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mmarker!", "bar_blue", "Step 22.c(i) Verify first bar color")
        legend=['SALES', 'SALES', '30,200']
        resultobj.verify_riser_legends("MAINTABLE_wbody1", legend, "Step 22:d(i) Verify legend Title")
        time.sleep(5)
        expected_tooltip=['COUNTRY:ITALY', 'SALES:30200']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1","riser!s0!g0!mmarker!",expected_tooltip, "Step 22.e: verify the default tooltip values")       
        time.sleep(5)
        metaobj.verify_filter_pane_field('COUNTRY',1,"Step 22: Verify 'COUNTRY' appears in filter pane")
        propertyobj.select_or_verify_show_prompt_item('1', 'ITALY',verify=True, verify_type=True, msg="Step 22:Verify prompt 'ITALY' is checked")
        expected_label_list = ['200km', '100mi']
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
        utillobj.asequal(statex, True, "Step 22: Verify the map is zoomed correctly")
        time.sleep(5)
        
        """
        Step 23: Dismiss IA window
        """
                
if __name__ == '__main__':
    unittest.main()