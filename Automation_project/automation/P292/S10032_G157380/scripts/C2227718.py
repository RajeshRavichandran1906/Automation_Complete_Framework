'''
Created on Jun 12, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227718
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run,\
    ia_run
from common.locators import visualization_resultarea_locators
from common.lib import utillity
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pyautogui import click


class C2227718_TestClass(BaseTestCase):

    def test_C2227718(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227718'
        
        driver = self.driver #Driver reference object created
#         driver.implicitly_wait(35) #Intializing common implicit wait for throughout the test
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
        
        utillobj.infoassist_api_login('idis','new_retail/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
        
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Double click "Revenue","Sale,Quarter".
        """
        time.sleep(4)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Sale,Quarter", 2, 1)
        
        """
        Step03: Verify the following chart is displayed.
        """        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)  
        metaobj.verify_query_pane_field('Vertical Axis',"Revenue",1,"Step03: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Sale,Quarter",1,"Step03: Verify horizontal axis")
             
        """
        Step04: Hover over riser > verify tooltip
        """     
        time.sleep(5)        
        xaxis_value="Sale Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step04:a(i) Verify Y-Axis Title")
        expected_xval_list=['1','2','3','4']
        expected_yval_list=['0','50M','100M','150M','200M','250M','300M','350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step04.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Revenue:$255,183,348.37', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step04: Verify bar value")
        time.sleep(5)
        
        """
        Step05: Select "Home" > "Visual" > "Insert" (dropdown) > "Chart".
        Step06: Verify the following charts are displayed.
        """
        ribbonobj.select_ribbon_item('Home','Insert',opt='Chart')
        time.sleep(10)
        resultobj.verify_panel_caption_label(0, 'Bar Stacked2', "Step06: Verify Bar Stacked2 is displayed")
        resultobj.verify_panel_caption_label(1, 'Bar Stacked1', "Step06: Verify Bar Stacked1 is displayed")
        
        resultobj.verify_number_of_riser("TableChart_2", 1, 12, 'Step06: Verify the total number of risers displayed on inserted chart')
        
        """
        Step07: Double click "Cost of Goods","Sale,Quarter".
        """
        time.sleep(4)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Sale,Quarter", 2, 1)
        
        """
        Step08: Verify the following chart is displayed.
        """        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)  
        metaobj.verify_query_pane_field('Vertical Axis',"Revenue",1,"Step07: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Sale,Quarter",1,"Step07: Verify horizontal axis")
             
        """
        Step09: Hover over riser > verify tooltip
        """     
        time.sleep(5)        
        xaxis_value="Sale Quarter"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step08:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", 'Revenue', "Step08:a(i) Verify Y-Axis Title")
        expected_xval_list=['1','2','3','4']
        expected_yval_list=['0','50M','100M','150M','200M','250M','300M','350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2", expected_xval_list, expected_yval_list, "Step08:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 4, 'Step08.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step08.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Revenue:$255,183,348.37', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g0!mbar", bar,"Step09: Verify bar value")
        time.sleep(5)
        
        """
        Step10: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)                  
                 
        """
        Step11: Verify the following chart is displayed.
        Step12: Verify hover (tooltip) works on the runtime chart.
        """
        browser=utillobj.parseinitfile('browser')
        if browser != 'Firefox':
            driver.maximize_window()
            time.sleep(5) 
        parent_css="#MAINTABLE_wbody2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)
         
        xaxis_value="Sale Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody2", xaxis_value, "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody2", 'Revenue', "Step11:a(i) Verify Y-Axis Title")
        expected_xval_list=['1','2','3','4']
        expected_yval_list=['0','50M','100M','150M','200M','250M','300M','350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody2",expected_xval_list,expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody2", 1, 4, 'Step11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody2", "riser!s0!g0!mbar", "bar_blue", "Step11.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Revenue:$255,183,348.37', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody2", "riser!s0!g0!mbar", bar,"Step11: Verify bar value")
        time.sleep(5)
        
        xaxis_value="Sale Quarter"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step12:a(i) Verify Y-Axis Title")
        expected_xval_list=['1','2','3','4']
        expected_yval_list=['0','50M','100M','150M','200M','250M','300M','350M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 4, 'Step12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step12.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Revenue:$255,183,348.37', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step12: Verify bar value")
                   
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227718_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
                     
        """
        Step13: Click Save in the toolbar
        Step14: Save as "C2158150" > Click Save
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                     
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                     
        """
        Step15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
                  
        """
        Step16: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
                  
        """
        Step17: Verify canvas
        """
        parent_css="#TableChart_2 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 4)
        time.sleep(5)

        xaxis_value="Sale Quarter"
        resultobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step11:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_2", 'Revenue', "Step11:a(i) Verify Y-Axis Title")
        expected_xval_list=['1','2','3','4']
        expected_yval_list=['0','50M','100M','150M','200M','250M','300M','350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_2",expected_xval_list,expected_yval_list, "Step11:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_2", 1, 4, 'Step11.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar", "bar_blue", "Step11.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Revenue:$255,183,348.37', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        resultobj.verify_default_tooltip_values("TableChart_2", "riser!s0!g0!mbar", bar,"Step11: Verify bar value")
        time.sleep(5)
        
        xaxis_value="Sale Quarter"
        resultobj.verify_xaxis_title("TableChart_1", xaxis_value, "Step12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("TableChart_1", 'Revenue', "Step12:a(i) Verify Y-Axis Title")
        expected_xval_list=['1','2','3','4']
        expected_yval_list=['0','50M','100M','150M','200M','250M','300M','350M']
        resultobj.verify_riser_chart_XY_labels("TableChart_1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("TableChart_1", 1, 4, 'Step12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("TableChart_1", "riser!s0!g0!mbar", "bar_blue", "Step12.c: Verify first bar color")
        time.sleep(5)
        bar=['Sale Quarter:1', 'Revenue:$255,183,348.37', 'Filter Chart', 'Exclude from Chart', 'Drill up to Sale Year', 'Drill down to Sale Month']
        resultobj.verify_default_tooltip_values("TableChart_1", "riser!s0!g0!mbar", bar,"Step12: Verify bar value")
        time.sleep(5)
 

if __name__ == '__main__':
    unittest.main()



    
     
        