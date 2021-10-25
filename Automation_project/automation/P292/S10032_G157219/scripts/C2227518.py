'''
Created on 27-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227518
TestCase Name = Verify Static Filter based on user Defined field
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

class C2227518_TestClass(BaseTestCase):

    def test_C2227518(self):
        
        Test_Case_ID = "C2227518"
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
        time.sleep(5)
        ia_ribbonobj.create_join("new_retail->dimensions->wf_retail_vendor")
        time.sleep(2)     
        
        """
        4. Link ID_VENDOR in wf_retail_product to ID_VENDOR in wf_retail_vendor
        """
        ia_ribbonobj.create_join_link(0, "ID_VENDOR", 1, "ID_VENDOR", source_scroll_down=5)
        time.sleep(4)        
        
        """
        5. Click OK
        """
        driver.find_element_by_css_selector("#dlgJoin_btnOK").click()
        time.sleep(8)        
        
        """
        6. Select Data Tab > Define
        """
        defcomp.invoke_define_compute_dialog('define')
        
        """
        7. Enter Field name "Vendor", Format A30V, double-click field "Vendor Name"
        """
        defcomp.enter_define_compute_parameter("Vendor", 'A30V', 'Vendor Name', 1)
        
        """
        8. Click OK
        """
        defcomp.close_define_compute_dialog('ok')
        
        """
        9. Verify Data pane
        """
        metaobj.verify_data_pane_field('Dimensions',"Vendor",12,"Step 09: Verify Define field Vendor is displayed in Data pane ")
        
        """
        10. Double-click fields "Product,Category", "Vendor", "ID Geography" and "Product Cost"
        """
        time.sleep(2) 
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Vendor", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("ID Geography", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("Product,Cost", 2, 1)
        time.sleep(4)
        
        """
        11. Verify Report
        """        
        coln_list = ['ProductCategory', 'Vendor', 'ID Geography', 'ProductCost']
        resultobj.verify_report_titles_on_preview(4, 8, "TableChart_1", coln_list, "Step 11: Verify column titles")
        time.sleep(2)
        ia_resultobj.create_report_data_set('TableChart_1', 30,4, 'C2227518_Ds01.xlsx', no_of_cells=8)
        ia_resultobj.verify_report_data_set('TableChart_1', 30,4, 'C2227518_Ds01.xlsx',"Step 11: Verify report data set",no_of_cells=8)        
        
        """
        12. Drag and drop field "Vendor" from the Data pane to the Filter pane
        """        
        metaobj.datatree_field_click("Vendor", 1, 1,'Filter')
        time.sleep(1)

        """
        13. Click <Value> and select Type:Parameter
        14. Verify "Dynamic" option is disabled
        15. Click "Static" radio button > click
        16. Click "Get Values" > All
        17. Select values displayed screen shot
        18. Click OK > OK
        """
        sel_list=['Audio Technica','Canon','LG','Panasonic','Samsung','Sharp','Sony','Toshiba']
        ia_ribbonobj.create_parameter_filter_condition('Static',sel_list,verify_radiobtn="true",getvalue_params='All')
        time.sleep(2)
        
        """
        19. Verify Filter in the filter pane
        """        
        metaobj.verify_filter_pane_field('Vendor Equal to Static Parameter (Name: Vendor, Values: Audio Technica, Canon, LG, ...)', 1, "Step 17: Verify the filter pane")
        time.sleep(2)
        ia_resultobj.create_report_data_set('TableChart_1', 30,4, 'C2227518_Ds02.xlsx', no_of_cells=8)
        ia_resultobj.verify_report_data_set('TableChart_1', 30,4, 'C2227518_Ds02.xlsx',"Step 19: Verify report data set",no_of_cells=8)        
        
        """
        20. Click Run
        """ 
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        
        """
        21. Click dropdown menu > Verify list of values from Static Filter
        22. Select value "Samsung" > click Run button
        """
        small_list=['Audio Technica', 'Canon', 'LG', 'Panasonic', 'Samsung', 'Sharp', 'Sony', 'Toshiba']
        iarun.select_amper_value('Vendor', ['Samsung'],False,verify_small_value_list=small_list)      
        time.sleep(4)
        iarun.select_amper_menu('Run')
        
        """
        23. Verify output
        """        
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        time.sleep(2)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227518_Ds03.xlsx", "Step 23: verify data set")
        
        """
        24. Click "Save" > Save as "C2227518" > Save
        """
        driver.switch_to.default_content()
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
         
        """
        25. Logout
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """
        26. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163549.fex&tool=report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit('C2227518', 'report', 'S7385')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        27. Verify Data pane, Query pane, and Preview
        """      
        metaobj.verify_data_pane_field('Dimensions','Vendor',12,"Step 27.1: Verify Vendor in Data Pane")
        time.sleep(2)
        metaobj.verify_query_pane_field('Sum', 'ID Geography', 1, "Step 27.2.1: Verify ID Geography in Sum")
        metaobj.verify_query_pane_field('Sum', 'Product,Cost', 2, "Step 27.2.2: Verify Product,Cost in Sum")
        time.sleep(2)
        metaobj.verify_query_pane_field('By', 'Product,Category', 1, "Step 27.2.3: Verify Product,Category in By")
        metaobj.verify_query_pane_field('By', 'Vendor', 2, "Step 27.2.4: Verify Vendor in By")
        
        ia_resultobj.verify_report_data_set('TableChart_1', 30,4, 'C2227518_Ds02.xlsx',"Step 19: Verify report data set",no_of_cells=8) 
                 
        """
        28. Logout:
        """
        utillobj.infoassist_api_logout()
         
if __name__ == '__main__':
    unittest.main()