'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226953
TestCase Name = Test that Auto Drill button is available when the proper Output format is chosen - HTML and Active for Report
'''
import unittest
from common.pages import visualization_ribbon
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase

class C2226953_TestClass(BaseTestCase):
    
    def test_C2226953(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)

        """    
            STEP 01 : Create a new report with a MFD that does not have a dimensional hierarchy (CAR.MAS)    
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P276/S9970', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn .bi-tree-view-table>tbody>tr:first-child", 'Report(car)', 180)
        
        """    
            STEP 02 : Click Format tab and Verify whether Auto drill button is active or not.     
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_visble_text("#FormatApplicationRibbonEnable>.bi-button-label", 'InfoMini', 60)
        
        """
            STEP 02.1 : Autodrill button should NOT be active
        """
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 02.1 : Verify Autodrill button should NOT be active")
         
        """    
            STEP 03 : Click on HTML output format in status bar and select Active format    
        """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        utillobj.synchronize_with_visble_text("#sbpOutputFormat .bi-button-label", 'ActiveReport', 20)
         
        """    
            STEP 04 : See the format tab and Verify whether Auto drill button is active or not.     
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_visble_text("#FormatApplicationRibbonEnable>.bi-button-label", 'InfoMini', 60)
        
        """
            STEP 04.1 : Autodrill button should NOT be active
        """
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, 'true', "Step 04.1 : Verify Autodrill button should NOT be active")
          
        """    
            STEP 05 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()