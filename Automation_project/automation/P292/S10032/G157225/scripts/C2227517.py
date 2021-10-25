'''
Created on 25-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227517
TestCase Name = Verify Dynamic Filter based on Joined field
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, define_compute, ia_run
from common.lib import utillity  
import time
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common import keys

class C2227517_TestClass(BaseTestCase):

    def test_C2227517(self):
        
        Test_Case_ID = "C2227517"
        driver = self.driver
        driver.implicitly_wait(20)
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
                
        """
        1. Launch the IA API with wf_retail_product, Report mode:
        http://machine:port/ibi_apps/ia?tool=report&master=baseapp/dimensions/wf_retail_product&item=IBFS%3A%2FWFC%2FRepository%2FP137/S7385
        """
        utillobj.infoassist_api_login('report','new_retail/dimensions/wf_retail_product','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        2. Select Data Tab > Click Join
        3. Click 'Add New' > select wf_retail_vendor under Dimensions subfolder
        """
        time.sleep(2)
        ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_vendor")
        time.sleep(2)     
        
        """
        4. Link ID_VENDOR in wf_retail_product to ID_VENDOR in wf_retail_vendor
        """
        ia_ribbonobj.create_additional_join_link(0, "ID_VENDOR", 1, "ID_VENDOR")
        time.sleep(4) 
        
        """
        5. Click OK
        """
        driver.find_element_by_css_selector("#dlgJoin_btnOK").click()
        time.sleep(8)        
        
        """
        6. Double-click fields "Vendor Name", "Product,Category", "ID Geography" and "Product Cost"
        """
        time.sleep(2)
        metaobj.datatree_field_click("Vendor Name", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("ID Geography", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("Product,Cost", 2, 1)
        time.sleep(4)
        coln_list = ['Vendor NameID Geography', 'ProductProductCategoryCost']
        resultobj.verify_report_titles_on_preview(2, 8, "TableChart_1", coln_list, "Step 06: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 5,4,'C2227517_Ds01.xlsx',"Step 06: Verify report data set",no_of_cells=8)        
        
        """
        7. Right-click "Vendor Name" in the Data pane > select "Filter"
        """        
        metaobj.datatree_field_click("Vendor Name", 1, 1,'Filter')
        time.sleep(2)

        """
        8. Click <Value>, select Type:Parameter
        9. Click "Dynamic" radio button > Check off "Select multiple values at runtime"
        10. Click OK > OK
        """
        ia_ribbonobj.create_parameter_filter_condition('Dynamic', ['Vendor Name'],ParamMultiple=True)
        time.sleep(2)
        metaobj.verify_filter_pane_field('Vendor Name Equal to Multiselect Dynamic Parameter (Name: VENDOR_NAME, Field: VENDOR_NAME in J001)', 1, "Step 10: Verify the filter pane")
        ia_resultobj.verify_report_data_set('TableChart_1',5,4,'C2227517_Ds02.xlsx',"Step 10: Verify report data set",no_of_cells=8)        
        
        """
        11. Click "Run".
        """ 
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        
        """
        12. Click "All Values" dropdown menu > Verify default selection "All Values"
        """
        iarun.verify_default_amper_value('Vendor Name','All Values',"Step 12: Verify Default amper value All Values in run window")
        """
        13. Click "Select Values" button > Click "All" button
        """
        iarun.select_amper_value('Vendor Name', ['All'],All=True)
        
        """
        14. Click Run button
        """        
        time.sleep(4)
        iarun.select_amper_menu('Run')
        
        """
        15. Verify output
        """        
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227517_Ds03.xlsx", "Step 15: verify data set")
        
        """
        16. Click "Save" > Save as "C2227517" > Save
        """
        driver.switch_to.default_content()
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """
        17. Logout
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """
        18. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227517.fex&tool=report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit('C2227517', 'report', 'S7385', mrid='mrid', mrpass='mrpass')
        time.sleep(15)
        
        """
        19. Click Run in the IA toolbar
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        
        """
        20. Click "All Values" dropdown menu > Click "Select Values" button
        21. Select values: Audiovox, BOSE, Canon
        """
        iarun.select_amper_value('Vendor Name', ['Audiovox','BOSE','Canon'],Search=True)
        
        """
        22. Click Run button
        """        
        time.sleep(4)
        iarun.select_amper_menu('Run')
        
        """
        23. Verify output
        """        
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        time.sleep(4)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227517_Ds04.xlsx", "Step 23: verify data set")
                  
        """
        24. Logout:
        """
        utillobj.infoassist_api_logout()
         
if __name__ == '__main__':
    unittest.main()