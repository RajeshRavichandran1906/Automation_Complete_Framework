'''
Created on 17-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227508
TestCase Name = Verify multiple Where-based Joins 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, define_compute, ia_run
from common.lib import utillity  
import time, pyautogui
from common.locators.loginpage_locators import LoginPageLocators
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.visualization_ribbon_locators import VisualizationRibbonLocators
from selenium.webdriver.common.action_chains import ActionChains

class C2227508_TestClass(BaseTestCase):

    def test_C2227508(self):
        
        Test_Case_ID = "C2227508"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','new_retail/dimensions/wf_retail_product','P137/S7385', 'mrid', 'mrpass')
        chart_type_css="#TableChart_1"
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > wf_retail_vendor.MAS.    """
        ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_vendor")
        
        """    4. Link ID_VENDOR in wf_retail_product to ID_VENDOR in wf_retail_vendor.    """
        ia_ribbonobj.create_join_link(0, "ID_VENDOR", 1, "ID_VENDOR", source_scroll_down=5)
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 04a: verify Join link color 'red' for first join")
        
        """    5. Click "Filter" button in toolbar > verify default WHERE expression in dialog.    """
        ia_ribbonobj.select_join_menu_buttons("filter")
        ia_ribbonobj.verify_join_filter_Condition("WF_RETAIL_PRODUCT.WF_RETAIL_PRODUCT.ID_VENDOR Equal to WF_RETAIL_VENDOR.WF_RETAIL_VENDOR.ID_VENDOR", "Step 07a: Verify filter condition")
        
        """    6. Click "OK".     """
        ia_ribbonobj.close_filter_dialog(btn='ok')
        '''    Workaround::: clicking add file not working, Hence closing the join dialog and reopening it '''
        ia_ribbonobj.select_join_menu_buttons("ok")
        time.sleep(5)
#         ribbonobj.select_tool_menu_item('menu_save_as')
#         utillobj.ibfs_save_as("temp")
#         time.sleep(5)
#         utillobj.infoassist_api_logout()
#         time.sleep(3)
#         utillobj.infoassist_api_edit("temp", 'report', 'S7385', mrid='mrid', mrpass='mrpass')
#         time.sleep(20)
#         elem1=(By.CSS_SELECTOR, "#TableChart_1")
#         resultobj._validate_page(elem1)
#         time.sleep(10)
        """    7. Click 'Add New' > select wf_retail_customer under dimensions subfolder    """
        ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_customer")
        #ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_customer", new_join=False)
        #ia_ribbonobj.add_more_join("new_retail->dimensions->wf_retail_customer")
        
        """    8. Link ID_VENDOR from wf_retail_vendor to ID_CUSTOMER in wf_retail_customer    """
        """    ++++++++++++++++++++++++++++++++++++Workaround+++++++++++++++++++++++++++++++++++++++++    """
        """    #ia_ribbonobj.create_additional_join_link(1, "ID_VENDOR", 2, "ID_CUSTOMER")    """
        table_css="#dlgJoin #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        source_tds=tables[1].find_elements_by_css_selector("td")
        source_list=[el.text for el in source_tds]
        if "ID_VENDOR" in source_list:
            src_elem=source_tds[source_list.index("ID_VENDOR")].find_element_by_css_selector("img[src*='column']")
            utillobj.click_on_screen(src_elem, coordinate_type='middle',click_type=1)
        time.sleep(2)
        utillobj.select_or_verify_bipop_menu("New Join")
        utillobj.select_or_verify_bipop_menu("JOIN new_retail/dimensions/wf_retail_vendor TO new_retail/dimensions/wf_retail_customer")
        time.sleep(2)
        driver.find_element_by_css_selector("#dlgJProp #id_description").click()
        driver.find_element_by_css_selector("#dlgJProp #id_description").send_keys("J002")
        time.sleep(2)
        host=driver.find_element_by_css_selector("#dlgJProp #dlgJProp_addHostField img")
        utillobj.click_on_screen(host, coordinate_type='middle',click_type=1)
        index_hz=driver.find_element_by_css_selector("div[class='bi-glass-pane']").value_of_css_property("z-index")
        table_css="#dlgMetaDataBrowser[style*='"+index_hz+"'] #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        host_tds=tables[0].find_elements_by_css_selector("td")
        host_list=[el.text for el in host_tds]
        if "ID_VENDOR" in host_list:
            host_elem=host_tds[host_list.index("ID_VENDOR")].find_element_by_css_selector("img[src*='column']")
            utillobj.click_on_screen(host_elem, coordinate_type='middle',click_type=1)
        time.sleep(4)
        driver.find_element_by_css_selector("#dlgMetaDataBrowser[style*='"+index_hz+"'] div[class$='window-content-pane'] div[id^='BiButton']").click()
        time.sleep(4)
        target=driver.find_element_by_css_selector("#dlgJProp #dlgJProp_addTargetField img")
        utillobj.click_on_screen(target, coordinate_type='middle',click_type=1)
        index_tz=driver.find_element_by_css_selector("div[class='bi-glass-pane']").value_of_css_property("z-index")
        table_css="#dlgMetaDataBrowser[style*='"+index_tz+"'] #metaDataBrowser"
        tables=self.driver.find_elements_by_css_selector(table_css)
        target_tds=tables[0].find_elements_by_css_selector("td")
        target_list=[el.text for el in target_tds]
        if "ID_CUSTOMER" in target_list:
            target_elem=target_tds[target_list.index("ID_CUSTOMER")].find_element_by_css_selector("img[src*='column']")
            utillobj.click_on_screen(target_elem, coordinate_type='middle',click_type=1)
        time.sleep(4)
        pyautogui.hotkey('enter')
        '''dialog_btns=driver.find_elements_by_css_selector("#dlgMetaDataBrowser[style*='"+index_tz+"'] div[class$='window-content-pane'] div[id^='BiButton']")
        btn_text_list=[el.text.strip() for el in dialog_btns]
        dialog_btns[btn_text_list.index('OK')].click()'''
        time.sleep(4)
        host=driver.find_element_by_css_selector("#dlgJProp #dlgJProp_btnOK img")
        utillobj.click_on_screen(host, coordinate_type='middle',click_type=1)
        """    +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    """
        time.sleep(8)
        ia_ribbonobj.verify_join_link_color(0, 'blue', "Step 08a: verify Join link color 'blue' for first join")
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 08b: verify Join link color 'red' for Second join")
        
        """    9. Click "Filter'" in the toolbar > verify default WHERE expression in dialog    """
        ia_ribbonobj.select_join_menu_buttons("filter")
        ia_ribbonobj.verify_join_filter_Condition("WF_RETAIL_VENDOR.WF_RETAIL_VENDOR.ID_VENDOR Equal to WF_RETAIL_CUSTOMER.WF_RETAIL_CUSTOMER.ID_CUSTOMER", "Step 09a: Verify filter condition")
         
        """    10. Click OK > OK    """
        ia_ribbonobj.close_filter_dialog(btn='ok')
        ia_ribbonobj.select_join_menu_buttons("ok")
        
        """    11. Verify Data pane   """
        metaobj.verify_data_pane_field('Dimensions',"Vendor Name",11,"Step 11a")
        metaobj.verify_data_pane_field('Dimensions',"Gender",15,"Step 11b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",8,"Step 11c")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Industry",15,"Step 11d")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Age",11,"Step 11e")
        
        """    12. Double-click fields "Product,Category", "Vendor Name", "ID Geography", "Customers" and "ID Industry".    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Vendor Name", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("ID Geography", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Customers", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("ID Industry", 2, 1)
        time.sleep(4)      
        
        """    13. verify the following report is displayed    """
        coln_list = ["ProductCategory", "Vendor Name", "ID Geography", "Customers", "ID Industry"]
        resultobj.verify_report_titles_on_preview(5, 10, "TableChart_1", coln_list, "Step 15a: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 5, "C2227508_Ds01.xlsx", no_of_cells=10)
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 5, "C2227508_Ds01.xlsx", "Step 15b: verify preview data", no_of_cells=10)  
        
        """    14. Click Run > Verify output.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        iarun.create_table_data_set("table[summary= 'Summary']", "C2227508_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227508_Ds02.xlsx", "Step 14a: verify data set")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    15. Close the output window    """
        """    16. Click "IA" > "Save" > C2227508 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    17. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    18. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    19. Verify Data pane, Query pane, and Preview    """
        metaobj.verify_data_pane_field('Dimensions',"Vendor Name",11,"Step 19a")
        metaobj.verify_data_pane_field('Dimensions',"Gender",15,"Step 19b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",8,"Step 19c")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Industry",15,"Step 19d")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Age",11,"Step 19e") 
        metaobj.verify_query_pane_field('Sum',"ID Geography",1,"Step 19f")
        metaobj.verify_query_pane_field('Sum',"Customers",2,"Step 19g")
        metaobj.verify_query_pane_field('Sum',"ID Industry",3,"Step 19h")
        metaobj.verify_query_pane_field('By',"Product,Category",1,"Step 19i")
        metaobj.verify_query_pane_field('By',"Vendor Name",2,"Step 19j")
        coln_list = ["ProductCategory", "Vendor Name", "ID Geography", "Customers", "ID Industry"]
        resultobj.verify_report_titles_on_preview(5, 10, "TableChart_1", coln_list, "Step 19k: Verify column titles") 
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 5, "C2227508_Ds01.xlsx", "Step 19l: verify preview data", no_of_cells=10)
        
        """    20. Click View Source button in the toolbar    """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        '''fexcode=driver.find_element_by_css_selector("#showFexButton img")
        ActionChains(driver).move_to_element(fexcode).click(fexcode).perform()'''
        time.sleep(8)
        
        """    21. Verify JOIN syntax    """
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text
        expected_code = 'JOIN FILE new_retail/dimensions/wf_retail_product AT WF_RETAIL_PRODUCT.WF_RETAIL_PRODUCT.ID_VENDOR\nTO UNIQUE FILE new_retail/dimensions/wf_retail_vendor AT WF_RETAIL_VENDOR.WF_RETAIL_VENDOR.ID_VENDOR TAG J001 AS J001'
        vp_text = "Step 21a: Verify J001 Join syntax in fex code"
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        expected_code = 'JOIN FILE new_retail/dimensions/wf_retail_product AT J001.WF_RETAIL_VENDOR.ID_VENDOR\nTO UNIQUE FILE new_retail/dimensions/wf_retail_customer AT WF_RETAIL_CUSTOMER.WF_RETAIL_CUSTOMER.ID_CUSTOMER TAG J002 AS J002'
        vp_text = "Step 21b: Verify J002 Join syntax in fex code"
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        driver.switch_to.default_content() 
        
        """    22. Close the View Source window    """
        driver.find_element_by_css_selector("#showFexOKBtn img").click()
        time.sleep(4)
        
        """    23. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
