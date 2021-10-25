'''
Created on Jan 31, 2017

@author: Magesh

Test Case =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2235511
TestCase Name = Verify Hold with Chart mode 
'''

from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon,visualization_metadata
from common.lib import utillity
import unittest,time
from selenium.common.exceptions import NoSuchElementException

class C2235511_TestClass(BaseTestCase):

    def test_C2235511(self):
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metadataobj = visualization_metadata.Visualization_Metadata(self.driver)
        
        Test_Case_ID = 'C2235511'

        """
        Step 01: Launch IA Chart mode: 
        http://machine:port/ibi_apps/ia?tool=Chart&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS10032_ia_2
        """ 
        utillobj.infoassist_api_login('chart', 'baseapp/wf_retail_lite', 'P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
          
        """
        Step 02: Double-click "Product,Category", "Cost of Goods", and "Revenue"
        """
        metadataobj.datatree_field_click('Product,Category', 2, 1)
        parent_css="#TableChart_1 svg g text[class*='mgroupLabel']"
        utillobj.synchronize_with_number_of_element(parent_css, 7, 30)
          
        metadataobj.datatree_field_click('Cost of Goods', 2, 1)
        parent_css="#TableChart_1 svg g text[class*='yaxis-title']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
          
        metadataobj.datatree_field_click('Revenue', 2, 1)
        parent_css="#TableChart_1 svg g rect[class*='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 14, 30)
          
        """
        Step 03: Verify "File" option is disabled in the Home Tab ribbon for default format HTML5"
        """
        home_file = driver.find_element_by_css_selector("[id='HomeDestFile'][disabled='true']").is_displayed()
        utillobj.asequal(True, home_file, 'Step 03.a: Verify "File" option is disabled in the Home Tab ribbon')
             
        """
        Step 04: Click the HTML5 format button > Select HTML
        """
        time.sleep(3)
        ribbonobj.change_output_format_type('charthtml')
          
        """
        Step 05: Verify "File" becomes enabled
        """
        time.sleep(3)
        try: 
            val = self.driver.find_element_by_css_selector("#HomeDestFile").is_displayed()
            utillobj.asequal(True, val, 'Step 05.a: Verify "File" becomes enabled')
        except NoSuchElementException:
            self.fail('Step 05.b: Verify "File" becomes enabled - Failed')
          
        """
        Step 06: Click "File"
        Step 07: Click "Save" in the File dialog
        """
        ribbonobj.select_ribbon_item('Home', 'File')
        time.sleep(8)
        parent_css="#dlgIbfsOpenFile7"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        pop_up_btn = self.driver.find_element_by_css_selector('#dlgIbfsOpenFile7 #IbfsOpenFileDialog7_btnOK')
        utillobj.default_left_click(object_locator=pop_up_btn)
          
        """
        Step 08: Verify Chart
        """
        time.sleep(15)
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        time.sleep(5)
        ele=self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step08', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(8)
          
        """
        Step 09: Click "Save" > Save As "C2235511" > Click "Save"
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
  
        """
        Step 10: Logout:
        """
        utillobj.infoassist_api_logout()
          
        """
        Step 11: Reopen saved FEX:
        """
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'chart', 'S10032',mrid='mrid',mrpass='mrpass')
        
        """
        Step 12: Verify successful restore
        """
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        ele=driver.find_element_by_css_selector("#TableChart_1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)
        time.sleep(2)

        """
        Step 13: Click Run > Verify message displayed
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        act_msg = driver.find_element_by_css_selector("html>body>h3").text.strip()
        print(act_msg)
        exp_msg = "Your request did not return any output to display."
        utillobj.asin(exp_msg, act_msg, "Step 13: Verify message displayed")
        utillobj.switch_to_default_content(3)
        time.sleep(15)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step13', image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """
        Step 14: Logout:
        """
        time.sleep(3)
        
if __name__ == "__main__":
    unittest.main()