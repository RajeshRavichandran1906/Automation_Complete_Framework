'''
Created on 17-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227510
TestCase Name = Verify Report with a Compute field 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, define_compute, ia_run
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227510_TestClass(BaseTestCase):

    def test_C2227510(self):
        
        Test_Case_ID = "C2227510"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','new_retail/wf_retail_lite','P292/S10032_infoassist_1', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    2.Double click "Revenue","Product,Category"    """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        coln_list = ["ProductCategory", "Revenue"]
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 02a: Verify column titles") 
        
        """    3. Select "Data" > "Summary (Compute)".    """
        defcomp.invoke_define_compute_dialog('compute')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    4. Enter "Field" = "NewRevenue".    """
        """    5. Double click "Revenue".    """
        defcomp.enter_define_compute_parameter("NewRevenue", 'D12.2', 'Revenue', 1)
        
        """    6. Enter "+ 9999" into the textbox.    """
        defcomp.select_calculation_btns(btn_series="plus->nine->nine->nine->nine")
        
        """    7. Click "OK".    """
        defcomp.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """    8. Verify the following report is displayed.    """
        coln_list = ["ProductCategory", "Revenue", "NewRevenue"]
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 08a: Verify column titles") 
#         ia_resultobj.create_report_data_set("TableChart_1", 7, 3, "C2227510_Ds01.xlsx",no_of_cells=6)
        ia_resultobj.verify_report_data_set("TableChart_1", 7, 3, "C2227510_Ds01.xlsx", "Step 8b: verify preview data", no_of_cells=6)
        
        """    9. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """    10. Verify the report is displayed.    """
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227510_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227510_Ds02.xlsx", "Step 10a: verify data set")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    11. Highlight "NewRevenue" > Right mouse click > "Edit Compute".    """
        metaobj.querytree_field_click('NewRevenue', 1,1, 'Edit Compute')
        parent_css="#fname"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        time.sleep(2)
        
        """    12. Enter "Field" = "NewRevenue_1".    """
        field_name = self.driver.find_element_by_id("fname")
        field_name.send_keys("NewRevenue_1")
        
        """    13. Click "OK".    """
        defcomp.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """    14. Verify the following report is displayed.    """
        coln_list = ["ProductCategory", "Revenue", "NewRevenue_1"]
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 14a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 7, 3, "C2227510_Ds01.xlsx", "Step 14b: verify preview data", no_of_cells=6)
        
        """    15. Click "IA" > "Save" > C2227510 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    16. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    17. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        parent_css="input[id=SignonUserName]"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_1', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        time.sleep(2)
        
        """    18. Verify Report on "Live Preview". """
        coln_list = ["ProductCategory", "Revenue", "NewRevenue_1"]
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 18a: Verify column titles") 
        ia_resultobj.verify_report_data_set("TableChart_1", 7, 3, "C2227510_Ds01.xlsx", "Step 18b: verify preview data", no_of_cells=6)
        
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()