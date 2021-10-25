'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226952
TestCase Name = Test that Auto Drill button is available when the proper Output format is chosen - HTML and Active for Report
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226951_TestClass(BaseTestCase):
    def test_C2226951(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = "C2226951_"+browser_type
        #driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)

        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
          
        """    2. Click Format tab and Verify whether Auto drill button is active or not.     """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 2a: HTML - Verify Autodrill button enabled")
        time.sleep(4)
         
        """    3. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(4)
         
        """    4. See the format tab and Verify whether Auto drill button is active or not.     """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 4a: Active_Report - Verify Autodrill button still active")
        time.sleep(4)
         
        """    5. Click IA > Save As> Type C2226951a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID+"a")
        time.sleep(5)
        
        """    6. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226951a.fex&tool=Chart    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID+"a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    7. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 7a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
         
        """    8. Click on Active Report output format in status bar and select PDF    """
        ribbonobj.change_output_format_type('pdf', 'status_bar')
        time.sleep(4)
         
        """    9. See the format tab and Verify the Auto drill button is not active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 9a: PDF - Verify Autodrill button is not active")
        time.sleep(4)
        '''
        AS per the PeterR email, we have removed the APDF option from the test case.
        """    10. Click on PDF output format in status bar and select Active PDF   """
        ribbonobj.change_output_format_type('active_pdf', 'status_bar')
        time.sleep(4)
        
        """    11. See the format tab and Verify the Auto drill button is not active.    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 11a: Active_PDF - Verify Autodrill button is not active")
        time.sleep(4)
        '''
        """    12. Click on Active PDF output format in status bar and select Excel (xlsx)    """
        ribbonobj.change_output_format_type('excel', 'status_bar')
        time.sleep(4)
        
        """    13. See the format tab and Verify the Auto drill button is not active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 13a: Excel(xlsx) - Verify Autodrill button is not active")
        time.sleep(4)
        
        """    14. Click on Excel (xlsx) output format in status bar and select Powerpoint (pptx)    """
        ribbonobj.change_output_format_type('powerpoint', 'status_bar')
        time.sleep(4)
        
        """    15. See the format tab and Verify the Auto drill button is not active.    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 15a: PowerPoint - Verify Autodrill button is not active")
        time.sleep(4)
        
        """    16. Click IA > Save As > Type C2226951b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID+"b")
        time.sleep(5)
        
         
        """    17. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226951b.fex&tool=Chart    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID+"b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(9)
        
        """    18. Click format tab and see Autodrill button should NOT be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 18a: PowerPoint - Verify Autodrill button should be active")
        time.sleep(4)
          
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
