'''
Created on 17-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227507
TestCase Name = Verify Define-based Join 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, define_compute, ia_run
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227507_TestClass(BaseTestCase):

    def test_C2227507(self):
        
        Test_Case_ID = "C2227507"
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
        elem1=(By.CSS_SELECTOR, chart_type_css)
        resultobj._validate_page(elem1)
        
        """    2. Select Data Tab > Click Define    """
        defcomp.invoke_define_compute_dialog('define')
        elem1=(By.CSS_SELECTOR, "#fname")
        resultobj._validate_page(elem1)
        
        """    3. Type ID for Field name, I9 for Format, double-click "ID Vendor"    """
        defcomp.enter_define_compute_parameter("ID", 'I9', 'ID Vendor', 1)
        
        """    4. Click OK to create define field    """
        defcomp.close_define_compute_dialog('ok')
        time.sleep(8)
        
        """    5. Verify Data pane   """
        metaobj.verify_data_pane_field('Dimensions',"Product Name",8,"Step 05a")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Product",1,"Step 05b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",2,"Step 05c")
        metaobj.verify_data_pane_field('Measures/Properties',"Accessories",9,"Step 05d")
        metaobj.verify_data_pane_field('Measures/Properties',"ID",11,"Step 05e") 
        
        """    6. Select "Data" > "Join".    """
        """    7. Click "Add New" > select wf_retail_vendor under Dimensions subfolder    """
        ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_vendor")
        time.sleep(5)
        
        """    8. Link ID_VENDOR in wf_retail_product to ID_VENDOR in wf_retail_vendor.    """
        ia_ribbonobj.create_additional_join_link(0, "ID", 1, "ID_VENDOR")
        #ia_ribbonobj.create_join_link(0, "ID", 1, "ID_VENDOR")
        
        """    9. Verify dialog    """
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 09a: verify Join link created successfully")
        
        """    10. Click "Filter" in the toolbar > Verify dialog.    """
        ia_ribbonobj.select_join_menu_buttons("filter")
        time.sleep(2)
        ia_ribbonobj.verify_join_filter_Condition("Double-click or press F2 to edit!", "Step 10a: Verify filter condition")
        
        """    11. Click Cancel in the filter dialog    """
        driver.find_element_by_css_selector("#dlgWhere  #dlgWhere_btnCancel img").click()
        time.sleep(4)
        
        """    12. Click OK to create join     """
        ia_ribbonobj.select_join_menu_buttons("ok")
        time.sleep(8)
        
        """    13. Verify Data pane    """
        metaobj.verify_data_pane_field('Dimensions',"Vendor Name",11,"Step 13a")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Product",1,"Step 13b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",8,"Step 13c")
        metaobj.verify_data_pane_field('Measures/Properties',"Accessories",11,"Step 13d")
        metaobj.verify_data_pane_field('Measures/Properties',"ID",13,"Step 13e") 
        
        """    14. Double-click fields "Product,Category", "Vendor Name", "ID" and "ID Geography".    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("Vendor Name", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("ID", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("ID Geography", 2, 1)
        time.sleep(8)       
        
        """    15. verify the following report is displayed    """
        coln_list = ["ProductCategory", "Vendor Name", "ID", "ID Geography"]
        resultobj.verify_report_titles_on_preview(4, 8, "TableChart_1", coln_list, "Step 15a: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 4, "C2227507_Ds01.xlsx", no_of_cells=8)
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 4, "C2227507_Ds01.xlsx", "Step 15b: verify preview data", no_of_cells=8)  
        
        """    16. Click Run > Verify output.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227507_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227507_Ds02.xlsx", "Step 16a: verify data set")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    17. Close the output window    """
        """    18. Click "IA" > "Save" > C2227507 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    20. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    21. Verify Data pane, Query pane, and Preview    """
        metaobj.verify_data_pane_field('Dimensions',"Vendor Name",11,"Step 21a")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Product",1,"Step 21b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",8,"Step 21c")
        metaobj.verify_data_pane_field('Measures/Properties',"Accessories",11,"Step 21d")
        metaobj.verify_data_pane_field('Measures/Properties',"ID",13,"Step 21e") 
        metaobj.verify_query_pane_field('Sum',"ID",1,"Step 21f")
        metaobj.verify_query_pane_field('Sum',"ID Geography",2,"Step 21g")
        metaobj.verify_query_pane_field('By',"Product,Category",1,"Step 21h")
        metaobj.verify_query_pane_field('By',"Vendor Name",2,"Step 21i")
        coln_list = ["ProductCategory", "Vendor Name", "ID", "ID Geography"]
        resultobj.verify_report_titles_on_preview(4, 8, "TableChart_1", coln_list, "Step 21j: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 4, "C2227507_Ds01.xlsx", "Step 21k: verify preview data", no_of_cells=8)  
        
        """    22. Click View Source button in the toolbar    """
        ribbonobj.select_top_toolbar_item("toolbar_showfex")
        '''fexcode=driver.find_element_by_css_selector("#showFexButton img")
        ActionChains(driver).move_to_element(fexcode).click(fexcode).perform()'''
        time.sleep(8)
        
        """    23. Verify JOIN syntax    """
        e = driver.find_element_by_xpath("//iframe[starts-with(@id,'BiRich')]")
        time.sleep(3)
        driver.switch_to.frame(e)
        time.sleep(2)
        fex_code = driver.find_element_by_css_selector("body > div").text
        expected_code = 'JOIN ID WITH WF_RETAIL_PRODUCT.WF_RETAIL_PRODUCT.BRAND IN NEW_RETAIL/DIMENSIONS/WF_RETAIL_PRODUCT\nTO UNIQUE WF_RETAIL_VENDOR.WF_RETAIL_VENDOR.ID_VENDOR IN new_retail/dimensions/wf_retail_vendor TAG J001 AS J001'
        vp_text = "Step 23a: Verify Join syntax in fex code"
        bol=expected_code in fex_code
        utillity.UtillityMethods.asequal(self,True, bol, vp_text)
        driver.switch_to.default_content() 
        
        """    24. Close the View Source window    """
        driver.find_element_by_css_selector("#showFexOKBtn img").click()
        time.sleep(4)
        
        """    25. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
