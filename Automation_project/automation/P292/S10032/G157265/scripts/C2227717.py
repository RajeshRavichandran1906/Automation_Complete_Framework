'''
Created on Jun 12, 2017
@author: Kiruthika

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227717
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_properties, visualization_resultarea, visualization_ribbon,visualization_run,ia_run, metadata
from common.locators import visualization_resultarea_locators
from common.lib import utillity
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pyautogui import click


class C2227717_TestClass(BaseTestCase):

    def test_C2227717(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227717'
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        propertyobj = visualization_properties.Visualization_Properties(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_runobj = visualization_run.Visualization_Run(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        new_metaobj = metadata.MetaData(self.driver)
        
        """
        Step 01: Launch the IA API with wf_retail_lite, Visualization mode:
        http://machine:port/ibi_apps/ia?tool=idis&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS8979%2F
        """
       
        utillobj.infoassist_api_login('idis','baseapp/wf_retail_lite','P292/S10032_visual_3', 'mrid', 'mrpass')
       
        elem1=visualization_resultarea_locators.VisualizationResultareaLocators.__dict__['default_riser']
        resultobj._validate_page(elem1)
        
        """
        Step02: Double click "Revenue","Gender".
        """
        time.sleep(4)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        new_metaobj.collapse_data_field_section('Sales->Measure Groups')
        time.sleep(5)
        metaobj.datatree_field_click("Gender", 2, 1)
        
        """
        Step03: Verify Query pane displays as follow.
        """        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)  
        metaobj.verify_query_pane_field('Vertical Axis',"Revenue",1,"Step03: Verify vertical axis")
        metaobj.verify_query_pane_field('Horizontal Axis',"Gender",1,"Step03: Verify horizontal axis")
             
        """
        Step04: Verify the following chart is displayed.
        Step05: Verify hover (tooltip) works.
        """     
        time.sleep(5)        
        xaxis_value="Gender"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step04:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step04:a(i) Verify Y-Axis Title")
        expected_xval_list=['F','M']
        expected_yval_list=['0','100M','200M','300M','400M','500M','600M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step06:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step04.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step04.c: Verify first bar color")
        time.sleep(5)
        bar=['Gender:F', 'Revenue:$526,361,785.28', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step05: Verify bar value")
        time.sleep(5)
        
        """
        Step06: Click Run
        """
        time.sleep(8)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(20)
        utillobj.switch_to_window(1)
        time.sleep(15)                  
                
        """
        Step07: Verify the following chart is displayed.
        """
        browser=utillobj.parseinitfile('browser')
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        
        xaxis_value="Gender"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step07:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step07:a(i) Verify Y-Axis Title")
        expected_xval_list=['F','M']
        expected_yval_list=['0','100M','200M','300M','400M','500M','600M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step07:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step07.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step07.c: Verify first bar color")
        time.sleep(5)
        bar=['Gender:F', 'Revenue:$526,361,785.28', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step07: Verify bar value")
        time.sleep(5)
                  
        time.sleep(20)
        ele=driver.find_element_by_css_selector("div[id*='ibi$container$inner$HBOX_1']")
        utillobj.take_screenshot(ele,'C2227717_Actual_step07', image_type='actual',x=1, y=1, w=-1, h=-1)
                    
        """
        Step08: Click Save in the toolbar
        Step09: Save as "C2158150" > Click Save
        """
        time.sleep(5)
        self.driver.close()
        time.sleep(10)
        utillobj.switch_to_window(0)
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
                    
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
                    
        """
        Step10: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2) 
                 
        """
        Step11: Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS8979%2FC2158150.fex&tool=idis
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'idis','S10032_visual_3',mrid='mrid',mrpass='mrpass')
                 
        """
        Step12: Verify canvas
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        resultobj.wait_for_property(parent_css, 2)
        time.sleep(5)
        
        xaxis_value="Gender"
        resultobj.verify_xaxis_title("MAINTABLE_wbody1", xaxis_value, "Step12:a(i) Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_wbody1", 'Revenue', "Step12:a(i) Verify Y-Axis Title")
        expected_xval_list=['F','M']
        expected_yval_list=['0','100M','200M','300M','400M','500M','600M']
        resultobj.verify_riser_chart_XY_labels("MAINTABLE_wbody1", expected_xval_list, expected_yval_list, "Step12:a(iii):Verify XY labels")
        resultobj.verify_number_of_riser("MAINTABLE_wbody1", 1, 2, 'Step12.b: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("MAINTABLE_wbody1", "riser!s0!g0!mbar", "bar_blue", "Step12.c: Verify first bar color")
        time.sleep(5)
        bar=['Gender:F', 'Revenue:$526,361,785.28', 'Filter Chart', 'Exclude from Chart']
        resultobj.verify_default_tooltip_values("MAINTABLE_wbody1", "riser!s0!g0!mbar", bar,"Step12: Verify bar value")
        time.sleep(5)
 

if __name__ == '__main__':
    unittest.main()



    
     
        