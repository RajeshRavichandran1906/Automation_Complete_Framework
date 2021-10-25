'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227506
TestCase Name = Verify Blend Join 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_ribbon
from common.lib import utillity  
import time
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class C2227506_TestClass(BaseTestCase):

    def test_C2227506(self):
        
        Test_Case_ID = "C2227506"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbonobj= ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','new_retail/dimensions/wf_retail_product','P137/S7385', 'mrid', 'mrpass')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > select wf_retail_vendor under Dimensions subfolder    """
        ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_vendor")
        
        """    4. Link ID_VENDOR in wf_retail_product to ID_VENDOR in wf_retail_vendor.    """
        ia_ribbonobj.create_join_link(0, "ID_VENDOR", 1, "ID_VENDOR", source_scroll_down=5)
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 04a: verify Join link created successfully")
        
        """    5. Click "Blend'" in the toolbar > verify "Filter" is disabled    """
        ia_ribbonobj.select_join_menu_buttons("blend")
        booln="tool-bar-button-disabled" in driver.find_element_by_css_selector("#dlgJoin_btnEditWhere").get_attribute("class")
        utillobj.asequal(True, booln, "Step 5a: Verify 'Filter' icon has been disabled")
        
        """    6. Click OK    """
        ia_ribbonobj.select_join_menu_buttons("ok")
        time.sleep(4)
        
        """    7. Verify Data pane   """
        metaobj.verify_data_pane_field('Dimensions',"Vendor Name",11,"Step 07a")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Product",1,"Step 07b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",8,"Step 07c")
        metaobj.verify_data_pane_field('Measures/Properties',"Accessories",11,"Step 07d")        
         
        """    8. Double-click fields "Vendor Name", "ID Product" and "ID Geography".    """
        metaobj.datatree_field_click("Vendor Name", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("ID Product", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("ID Geography", 2, 1)
        time.sleep(8)       
        
        """    9 . verify the following report is displayed    """
        coln_list = ["Vendor Name", "ID Product", "ID Geography"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 09: Verify column titles")
        time.sleep(4)
        
        """    10. Click Run > Verify output    """
        ribbonobj.select_top_toolbar_item("toolbar_run")
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227506_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227506_Ds01.xlsx", "Step 10a: verify data set")
        
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    11. Close the output window    """
        """    12. Click "Save" > Save as "C2227506" > Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    13. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    14. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        time.sleep(40)
        
        """    15. Verify Data pane, Query pane, and Preview    """
        metaobj.verify_data_pane_field('Dimensions',"Product Name",8,"Step 15a")
        metaobj.verify_data_pane_field('Measures/Properties',"Product,Cost",6,"Step 15b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",8,"Step 15c")
        metaobj.verify_data_pane_field('Measures/Properties',"Accessories",11,"Step 15d")
        metaobj.verify_query_pane_field('Sum',"ID Product",1,"Step 15e")
        metaobj.verify_query_pane_field('Sum',"ID Geography",2,"Step 15f")
        metaobj.verify_query_pane_field('By',"Vendor Name",1,"Step 15g")
        coln_list = ["Vendor Name", "ID Product", "ID Geography"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 15h: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 3, "C2068466_Ds02.xlsx")
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 3, "C2227506_Ds02.xlsx", "Step 15i: verify data set")
        
        """    16. Click View Source button in the toolbar    """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        '''fexcode=driver.find_element_by_css_selector("#showFexButton img")
        ActionChains(driver).move_to_element(fexcode).click(fexcode).perform()'''
        time.sleep(8)
        
        """    17. Verify JOIN syntax    """
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text
        expected_code = 'JOIN AS_ROOT WF_RETAIL_PRODUCT.WF_RETAIL_PRODUCT.ID_VENDOR IN NEW_RETAIL/DIMENSIONS/WF_RETAIL_PRODUCT\nTO UNIQUE WF_RETAIL_VENDOR.WF_RETAIL_VENDOR.ID_VENDOR IN NEW_RETAIL/DIMENSIONS/WF_RETAIL_VENDOR TAG J001 AS J001'
        vp_text = "Step 17a: Verify Join syntax in fex code"
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        driver.switch_to.default_content() 
        
        """    18. Close the View Source window    """
        driver.find_element_by_css_selector("#showFexOKBtn img").click()
        time.sleep(4)
        
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()

