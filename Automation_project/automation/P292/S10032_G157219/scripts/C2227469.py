'''
Created on 20-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227469
TestCase Name = Verify create Slicer from field context menu in the Data pane
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_run
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227469_TestClass(BaseTestCase):

    def test_C2227469(self):
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        chart_type_css="#TableChart_1"
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """    2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"    """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("DEALER_COST", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("RETAIL_COST", 2, 1)
        time.sleep(4)   
        
        """    3. Verify the following report is displayed.    """
        coln_list = ["COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03a: Verify column titles")
        
        """    4. Select Slicers Tab    """
        ribbonobj.switch_ia_tab('Slicers')
        
        """    5. Under "Options" group > Click "New Group".    """
        ribbonobj.select_ribbon_item('Slicers', 'New_group')
        #driver.find_element_by_css_selector("#createSlicerGroupBtn img").click()
        time.sleep(5)
        
        """    6. Verify a new slicer group (Group 2) is added.    """
        bol=driver.find_element_by_css_selector("#SlicersTab #SlicersCluster_1 div[class*='cluster-box-title']").text=='Group 1'
        utillobj.asequal(True, bol, "Step 06a: Verify 'Group 1'")
        bol=driver.find_element_by_css_selector("#SlicersTab #SlicersCluster_2 div[class*='cluster-box-title']").text=='Group 2'
        utillobj.asequal(True, bol, "Step 06b: Verify 'Group 2'")
        
        """    7. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """    8. Verify the report is displayed.    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2068433_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227469_Ds01.xlsx", "Step 8a: verify data set")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    9. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


