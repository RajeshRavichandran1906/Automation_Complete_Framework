'''
Created on 20-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227509
TestCase Name = Verify Compute based on a joined field 
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, define_compute, metadata
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.wftools.report import Report

class C2227509_TestClass(BaseTestCase):

    def test_C2227509(self):
        
        Test_Case_ID = "C2227509"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        report = Report(self.driver)
        DATA_SET_NAME1 = Test_Case_ID + '_DataSet_01.xlsx'
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P137/S7385', 'mrid', 'mrpass')
        chart_type_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(chart_type_css, 1, 60)
        time.sleep(10)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > TRAINING.MAS > Open > "OK".    """
        ia_ribbonobj.create_join("ibisamp","training")
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 03a: Verify join link color")
        driver.find_element_by_css_selector("#dlgJoin_btnOK").click()
        time.sleep(8)
        
        """    4. Double click "LASTNAME", "COURSECODE"    """
        metaobj.datatree_field_click("Dimensions->LASTNAME", 2, 1)
        report.wait_for_visible_text("#queryTreeWindow", "LASTNAME", 60)
        metaobj.datatree_field_click("Dimensions->COURSECODE", 2, 1)
        report.wait_for_visible_text("#queryTreeWindow", "COURSECODE", 60)  
        metadataobj.collapse_data_field_section('Dimensions') 
        time.sleep(4)
        
        """    5. verify the following report is displayed    """
        coln_list = ["LASTNAME", "COURSECODE"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 05a: Verify column titles")
        
        """    6. Select Data Tab > Click Compute    """
        defcomp.invoke_define_compute_dialog('compute')
        elem1=(By.CSS_SELECTOR, "#fname")
        resultobj._validate_page(elem1)
        
        """    7. Enter Field = "NEWEXPENSES"    """
        """    8. Double click "EXPENSES" > "OK".    """
        defcomp.enter_define_compute_parameter("NEWEXPENSES", 'D12.2', 'Measures/Properties->EXPENSES', 1)
        defcomp.close_define_compute_dialog('ok')
        time.sleep(4)
        
        """    9. Verify "NEWEXPENSES" field is displayed in "Live Preview".    """
        coln_list = ["LASTNAME", "COURSECODE", "NEWEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 9a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 3, 3, "C2227509_Ds01.xlsx", "Step 9b: verify preview data")   
        
        """    10. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """    11. Verify the report is displayed.    """
        """    12. Close the output window    """
        report.switch_to_frame()
        time.sleep(20)
        #report.create_html_report_dataset(DATA_SET_NAME1)
        report.verify_html_report_dataset(DATA_SET_NAME1, "Step 12 : Verify the report is displayed.")
        report.switch_to_default_content()
        time.sleep(2)
        
        """    13. Click "IA" > "Save" > C2227509 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """    14. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    15. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    16. Verify Canvas    """
        coln_list = ["LASTNAME", "COURSECODE", "NEWEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 16a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 3, 3, "C2227509_Ds01.xlsx", "Step 16b: verify preview data") 
        
        """    17. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
       
if __name__ == '__main__':
    unittest.main()

