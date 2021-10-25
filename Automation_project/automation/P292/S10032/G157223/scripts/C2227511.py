'''
Created on 17-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227511
TestCase Name = Verify Define based on a joined field 
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, define_compute
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.wftools.report import Report

class C2227511_TestClass(BaseTestCase):

    def test_C2227511(self):
        
        Test_Case_ID = "C2227511"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        defcomp=define_compute.Define_Compute(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        report = Report(self.driver)
        DATA_SET_NAME1 = Test_Case_ID + '_DataSet_01.xlsx'
        
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P137/S7385', 'mrid', 'mrpass')
        elem1="#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 60)
        
        """    2. Select "Data" > "Join".    """
        """    3. Click "Add New" > TRAINING.MAS > Open > "OK".    """
        time.sleep(8)
        ia_ribbonobj.create_join("ibisamp","training")
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 03a: Verify join link color")
        driver.find_element_by_css_selector("#dlgJoin_btnOK").click()
        time.sleep(8)
        
        """    4. Double click "LASTNAME", "COURSECODE"    """
        metaobj.datatree_field_click("Dimensions->LASTNAME", 2, 1)
        report.wait_for_visible_text("#queryTreeWindow", "LASTNAME", 60)
        metaobj.datatree_field_click("Dimensions->COURSECODE", 2, 1)
        report.wait_for_visible_text("#queryTreeWindow", "COURSECODE", 60)  
        
        """    5. verify the following report is displayed    """
        coln_list = ["LASTNAME", "COURSECODE"]
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 05a: Verify column titles")
        
        """    6. Select Data Tab > Click Define    """
        defcomp.invoke_define_compute_dialog('define')
        elem1=(By.CSS_SELECTOR, "#fname")
        resultobj._validate_page(elem1)
        
        """    7. Type ID for Field name, I9 for Format, double-click "ID Vendor"    """
        defcomp.enter_define_compute_parameter("JOINDEFEXPENSES", 'D12.2', 'Measures/Properties->EXPENSES', 1)
        
        """    8. Click OK to create define field    """
        defcomp.close_define_compute_dialog('ok')
        
        """    9. Double click "JOINDEFEXPENSES"    """
        metaobj.datatree_field_click("Measures/Properties->JOINDEFEXPENSES", 2, 1)
        time.sleep(4)
        
        """    10. verify the following report is displayed    """
        coln_list = ["LASTNAME", "COURSECODE", "JOINDEFEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 10a: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 3, "C2227511_Ds01.xlsx", "Step 10b: verify preview data")  
        
        """    11. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """    12. Verify the report is displayed.    """
        """    13. Close the output window    """
        report.switch_to_frame()
        time.sleep(20)
        #report.create_html_report_dataset(DATA_SET_NAME1)
        report.verify_html_report_dataset(DATA_SET_NAME1, "Step 12 : Verify the report is displayed.")
        report.switch_to_default_content()
        time.sleep(2)
        
        """    14. Click "IA" > "Save" > C2227511 > click Save.    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    15. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    16. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(2)
        
        """    17. Verify Canvas    """
        coln_list = ["LASTNAME", "COURSECODE", "JOINDEFEXPENSES"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 17a: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 3, "C2227511_Ds01.xlsx", "Step 17b: verify preview data") 
        
        """    18. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
        
if __name__ == '__main__':
    unittest.main()

