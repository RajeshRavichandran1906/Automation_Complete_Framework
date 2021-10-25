'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227564
TestCase Name = Verify Auto Drill Report with Auto Link and Multi Drill, using wf_retail_lite
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_run, ia_ribbon, ia_resultarea
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.loginpage_locators import LoginPageLocators
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators

class C2227564_TestClass(BaseTestCase):

    def test_C2227564(self):
        
        Test_Case_ID = "C2227564"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)

        """    1. Reopen fex C2068414.fex using IA API:    """
        utillobj.infoassist_api_edit("C2227563", "report", "S7385")
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(5)
        
         
        """    2. Select "Format" > "Enable Auto Linking".    """
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
        
        """    3. Click "IA" > Save As > Enter "Title:" = "C2227564", click "Save"    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    4. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    5. Launch the IA API with WF_RETAIL_LITE, Report mode:    """
        utillobj.infoassist_api_login('report','new_retail/WF_RETAIL_LITE','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """    6. Double click "Product Category","Product_Subcategory","Cost of Goods"    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4) 
        
        """    7. Drag and drop "Product Category" into Filter panel    """
        metaobj.datatree_field_click("Product,Category", 1, 1, 'Filter')
        time.sleep(4)
        
        """    8. Double click "<Value>", set "Type:" = "Parameter", click "OK" (2x).    """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple')
        
        """    9. Verify "Filter" is created    """
        metaobj.verify_filter_pane_field('Product,Category Equal to Simple Parameter (Name: PRODUCT_CATEGORY)', 1, "Step 09a")
        
        """    10. Select "Format" > "Auto Link Target".    """
        ribbonobj.select_ribbon_item("Format", "Auto_Link_Target")
        
        """    11. Click "IA" > "Save" > Enter "Title:" = "Report_Target01", click "Save".    """ 
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("Report_Target01")
        time.sleep(5)
        
        """    12. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    13. Reopen fex using IA API:    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, "report", "S7385")
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """    14. Click "Run"    """
        time.sleep(2)
        driver.find_element(*VisualizationRibbonLocators.__dict__["toolbar_run"]).click()
        time.sleep(8)
        utillobj.switch_to_frame()
        #WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        
        """    15. Click "Accessories"    """
        """    16. Verify Auto drill,Multidrill and Autolink menus are displayed    """
        expected_list=['Drill down to Product Subcategory', 'Drilldown to Chart', 'MSN', 'Yahoo', 'Auto Links']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']", 2, 1, expected_list, "Step 16a: Verify menu for Multi-drill and Autolink targets")
        
        """    17. Select "Media Player" > Hover over Auto link > Select "Report_Target01"    """
        iarun.select_autolink_tooltip_menu("table[summary= 'Summary']", 5,1, "Auto Links->Report_Target01", "Step 17a: verify 'Report_Target01' fex is listed")
        
        """    18. Verify "Report_Target01" is displayed in a new window    """
        driver.switch_to.default_content()
        time.sleep(10)
        utillobj.switch_to_window(1)
        time.sleep(1)
        driver.maximize_window()
        time.sleep(5)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227564_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227564_Ds01.xlsx", "Step 18a: verify Output")
         
        """    19. Close the "Report_Source01 & Report_Target01" windows    """
        self.driver.close()
        time.sleep(1)
        utillobj.switch_to_window(0)
        time.sleep(1)
         
        """    20. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
                
if __name__ == '__main__':
    unittest.main()


        
    
