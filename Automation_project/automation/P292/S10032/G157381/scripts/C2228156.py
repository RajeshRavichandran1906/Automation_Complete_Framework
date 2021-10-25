'''
Created on Dec 20, 2017
@author: BM13368
TestCase Name :Edit Verify Run HTML output with BAR chart within IA (82xx)
TestCase ID :http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2228156
'''
import unittest, time
from common.pages import visualization_metadata, visualization_ribbon, ia_ribbon
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2228156_TestClass(BaseTestCase):

    def test_C2228156(self):
        
        Test_Case_ID = "C2228156"
        driver = self.driver
        utillobj = utillity.UtillityMethods(driver)
        metaobj = visualization_metadata.Visualization_Metadata(driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(driver)
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(driver)
        browser=utillobj.parseinitfile('browser')
        default_chart_css="#TableChart_1 rect[class^='riser']"
        default_chart_expected_number=25
        
        """
            Step 01:Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032&tool=chart&master=ibisamp/employee
        """
        utillobj.infoassist_api_login('chart','ibisamp/employee','P292/S10032_chart_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element(default_chart_css, default_chart_expected_number, 65)
        
        """
            Step 02:Select "Home" > "Format" > "HTML".
        """
        ribbonobj.switch_ia_tab("Home")
        ia_ribbon_obj.select_or_verify_output_type(launch_point='Home', item_select_path='HTML')
         
        """ 
            Step 03:Double click "LAST_NAME", "CURR_SAL".
        """
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        time.sleep(4)
        
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
            Step 08:Click Save in the toolbar > Save as "C2228156" > Click Save.
        """
        ribbonobj.select_tool_menu_item('menu_save')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """  
            Step 09:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        
        """  
            Step 10:Run from bip
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2228156.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10032_chart_1", 'mrid', 'mrpass')
        parent_css="html body img"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 65)
      
        """  
            Step 11:Verify the following chart is displayed.
        """
        ele=driver.find_element_by_css_selector("html body img")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step11_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        
        """
            Step 12:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(4)
        
        """ 
            Step 13: Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2228156.fex
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10660_chart_1', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_number_of_element("#resultArea", 1, 65)
        
        """  
            Step 14:Verify the following chart is displayed.
        """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step13_'+browser, image_type='actual',x=20, y=20, w=-50, h=-20)
        
        """ 
            Step 15:Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()