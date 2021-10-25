'''
Created on 17-OCT-2016

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227513
TestCase Name = Verify Filter expression, retrieving Values for a Measure field
'''
import unittest, time
from selenium.webdriver.common.by import By
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run

class C2227513_TestClass(BaseTestCase):

    def test_C2227513(self):
        
        """
        Test case variable
        """
        Test_Case_ID = "C2227513"
        
        """
        Test case objects
        """
        iarun        = ia_run.IA_Run(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        utillobj     = utillity.UtillityMethods(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        core_utils   = core_utility.CoreUtillityMethods(self.driver)
        ribbonobj    = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj      = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj    = visualization_resultarea.Visualization_Resultarea(self.driver)
              
        """
        1. Launch the IA API with CAR, Report mode::
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        2. Double click "COUNTRY", "SALES" 
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4) 
        metaobj.datatree_field_click("SALES", 2, 1)
        time.sleep(4) 
        
        """
        3. Drag SALES to Filter Pane
        """  
        metaobj.drag_drop_data_tree_items_to_filter("SALES", 1)     
        time.sleep(1)

        """
        4. Double click <Value> > "Get Values" (dropdown) > "All".
        5. Double click "13000".
        6. Verify "13000" moved over to the "Multiple Values" side.
        7. Click "OK" (2x).
        """
        ia_ribbonobj.create_constant_filter_condition('All',['13000'])
        time.sleep(4)
        
        """
        8. Verify the following report is displayed.
        """
        self.driver.set_page_load_timeout(100)
        coln_list = ['COUNTRY', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 08.01: Verify column titles")
        time.sleep(4)
        ia_resultobj.verify_report_data_set('TableChart_1', 1,2,'C2227513_Ds01.xlsx',"Step 08.02: Verify report data set")
        
        """
        9. Click "Run".
        """
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """
        10. Verify report is displayed.
        """
        core_utils.switch_to_frame()
        time.sleep(3)
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227513_Ds02.xlsx", "Step 10.01: verify data set")

        """
        11. Click "IA" > "Save" > "C2227513" > click Save
        """     
        core_utils.switch_to_default_content()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """
        12. Logout
        """
        utillobj.wf_logout()
        time.sleep(3)
        
        """
        13. Reopen fex using IA API:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227513.fex&tool=report
        """
        utillobj.infoassist_api_edit('C2227513', 'document', 'S7385', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        14. Verify Preview
        """
        coln_list = ['COUNTRY', 'SALES']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 14.01: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 1,2,'C2227513_Ds01.xlsx',"Step 14.02: Verify preview data set by reopening fex")
        
        """
        15. Logout
        """  
        
if __name__ == '__main__':
    unittest.main()