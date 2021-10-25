''''
Created on Dec 18, 2017
@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2228155
TestCase Name : Test Vertical Axis Minimum and Maximum manual scale, Set Horizontal Axis Label position with Stagger Labels
'''

import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2228155_TestClass(BaseTestCase):

    def test_C2228155(self):
        
        Test_Case_ID = "C2228155"
        Test_Case_ID1="IA-VAL-CHART-010"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(driver)
        browser=utillobj.parseinitfile('browser')
        """
            Step 01:Launch WF, New > Chart with EMPLOYEE.MAS.
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02:Double click "LAST_NAME", "CURR_SAL".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        """ 
            Step 03:Select "HTML" from Output Types group under Home tab.
        """
        ia_ribbon_obj.select_or_verify_output_type(launch_point='Home', item_select_path='HTML')
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step03_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        """ 
            Step 04:Click on "Format" tab.
            Step 05:Expand "Labels" group if not expanded.
        """
        
        ribbonobj.select_ribbon_item("Format", "Axes")
       
        """ 
            Step 07:Go to "Vertical Axis" > "More Vertical Axis Options".
        """
        utillobj.select_or_verify_bipop_menu("Vertical Axis")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("More Vertical Axis Options")
        time.sleep(2)
        parent_css="div[id^='QbDialog'] [class*='active'] [class*='caption']"
        resultobj.wait_for_property(parent_css, 1)
        
        """     
            Step 08:Uncheck "Automatic Minimum".
            Step 09:Enter "5000" in Value text field below "Automatic Minimum".
        """
        ia_ribbon_obj.set_format_vertical_axis_scale('checkbox','automatic_minimum', 'check')
        ia_ribbon_obj.set_format_vertical_axis_scale('textbox','minimum_value', '5000')
        """ 
            Step 10:Uncheck "Automatic Maximum".
            Step 11:Enter "30000" in Value text field below "Automatic Maximum".
        """
        ia_ribbon_obj.set_format_vertical_axis_scale('checkbox','automatic_maximum', 'check')
        ia_ribbon_obj.set_format_vertical_axis_scale('textbox','maximum_value', '30000')
        time.sleep(0.5)
       
        """ 
            Step 12:Click "OK".
        """
        ok_btn_elem=driver.find_element_by_css_selector("#axesOkBtn")
        utillobj.click_on_screen(ok_btn_elem, "middle", click_type=0, pause=1)
        """ 
            Step 13:Verify the chart in Live Preview updates vertical axis minimum and maximum values.
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step13_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        """ 
            Step 14:Click "Axes" (dropdown).
            Step 15:Go to "Horizontal Axis" > "More Horizontal Axis Options".
        """
#         ribbonobj.select_ribbon_item("Format", "labels")
        ribbonobj.select_ribbon_item("Format", "Axes")
        utillobj.select_or_verify_bipop_menu("Horizontal Axis")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("More Horizontal Axis Options")
        time.sleep(2)
        
        """ 
            Step 16:Click on "Labels" tab.
            Step 18:Check "Stagger Labels" checkbox.
        """ 
        ia_ribbon_obj.set_format_horizontal_axis_labels("checkbox", "stagger_labels", "Top")       
        
        """ 
            Step 19:Click "OK".
        """ 
        ok_btn_elem=driver.find_element_by_css_selector("#axesOkBtn")
        utillobj.click_on_screen(ok_btn_elem, "middle", 0)   
        """ 
            Step 20:Verify the horizontal axis labels change take effect in "Live Preview".
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step20_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        """ 
            Step 21:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
            
        """    
            Step 22:Verify the chart at runtime is the same displayed at "Live Preivew".
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step20_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        """ 
            Step 23:Click "IA" > "Save".
            Step 24:Enter Title = "IA-VAL-CHART-010".
            Step 25:Click "Save" and dismiss IA.
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID1)
        time.sleep(5)
        utillobj.infoassist_api_logout()     
        
        """ 
            Step 26:Locate the saved fex > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_ID1+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="html body img"
        resultobj.wait_for_property(parent_css,1)
        """ 
            Step 27:Verify the correct chart is displayed.
        """
        ele=driver.find_element_by_css_selector("html body img")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step11_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        
        """ 
            Step 28:Dismiss the chart run window.
        """
        utillobj.infoassist_api_logout()       
        """ 
            Step 29:Locate the saved fex > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID1, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        """ 
            Step 30:Verify IA is launched with correct chart displayed in "Live Preview".
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step13_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        """ 
            Step 31:Click "IA" > "Exit".
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()