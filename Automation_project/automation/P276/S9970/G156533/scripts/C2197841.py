'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2197841
TestCase Name = Auto Drill errors when DBA restriction is applied to a dimension field
'''
import unittest, time
from common.pages import visualization_resultarea, visualization_ribbon, ia_ribbon
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2197841_TestClass(BaseTestCase):
    def test_C2197841(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2197841"
        Test_Case_ID = Test_ID+"_"+browser_type
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbobj=ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Launch the IA Chart API with wf_retail_lite    """
        utillobj.infoassist_api_login('chart','baseapp/wf_retail_lite','P276/S9970', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)   
        time.sleep(15)
        
        """    2. Select Format Tab    """
        ribbonobj.switch_ia_tab('Format')
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 2a: Verify Autodrill button should be enabled")
        time.sleep(4)
        
        """    3. Select Format > Other in the Chart Types area of the ribbon    """
        """    4. Select Vertical Dual-Axis Cluster Bars, then click on OK    """
        ribbonobj.select_ribbon_item('Format', 'Other')
        ia_ribbobj.select_other_chart_type('threed', 'threed_bars', 1, ok_btn_click=True)
        ribbonobj.switch_ia_tab('Format')
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')  
        print(disabled)              
        utillobj.asequal(disabled, "true", "Step 4a: Verify Autodrill button should be disabled")
        time.sleep(4)
        
        """    5. Click "Save" in the toolbar > Type C2197841 > Click "Save" in the Save As dialog    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    6. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
