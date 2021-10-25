'''
Created on Dec 20, 2017
@author: BM13368
TestCase Name :Edit Verify Run HTML output with BAR chart within IA (82xx)
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2228156
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2228156_TestClass(BaseTestCase):

    def test_C2228156(self):
        
        Test_Case_ID = "C2228156"
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
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10660_chart_1', 'mrid', 'mrpass')
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        """
            Step 02:Select "Home" > "Format" > "HTML".
        """
        ribbonobj.switch_ia_tab("Home")
        ia_ribbon_obj.select_or_verify_output_type(launch_point='Home', item_select_path='HTML')
         
        """ 
            Step 03:Double click "LAST_NAME", "CURR_SAL".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(4) td"
        resultobj.wait_for_property(parent_css, 1)
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1)
        
        """  
            Step 04:Verify the following chart is displayed.
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step04_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        """ 
            Step 05:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        
        """  
            Step 06:Verify the following chart is displayed.
            Step 07:Dismiss the "Run" output window.
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step06_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        
        """  
            Step 08:Click "IA" > "Save" > "C2021016" > "Save".
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        """  
            Step 09:Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()
        """  
            Step 10:Highlight "C2021016" > Right mouse click > "Run".
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="html body img"
        resultobj.wait_for_property(parent_css,1)
        """  
            Step 11:Verify the following chart is displayed.
        """
        ele=driver.find_element_by_css_selector("html body img")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step11_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        utillobj.infoassist_api_logout()
        
        """ 
            Step 12:Highlight "C2021016" > Right mouse click > "Edit".
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        
        """  
            Step 13:Verify the following chart is displayed.
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step13_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        """ 
            Step 14:Dismiss the tool window.
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()