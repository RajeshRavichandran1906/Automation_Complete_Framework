'''
Created on 28-Nov-2017

@author: Aftab/Sowmiya

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227578
TestCase Name =Change Report Margins
'''
import unittest
import time
from common.lib import utillity
from common.lib.global_variables import Global_variables
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227578_TestClass(BaseTestCase):

    def test_C2227578(self):
        
        Test_Case_ID = "C2227578"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn", 'Sum', 120)
        
        """ 2. Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        time.sleep(4)
        
        
        """ 3. Verify the following report is displayed.            """
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 3.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2227578_Ds01.xlsx", 'Step 3.2: Verify report dataset')
        
        
        """ 4. Select "Layout" > "Margins" > "Normal (1.0 inch all round)".            """
        ribbonobj.select_ribbon_item("Layout", "margins", opt="Normal (1.0 inch all round)")
        
        
        """ 5. Click "Run"            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        elem=(By.CSS_SELECTOR,"table[summary='Summary']")
        resultobj._validate_page(elem)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx", 'Step 8: Verify report dataset')
        
        """ 6. Verify the following report (with the proper margin) is displayed.            """
        table_elem="table[summary='Summary']"
#         if browser in ['Chrome']:
#             ia_runobj.verify_report_table_margin(table_elem, margin=True, expected_table_elem="96px")
#         if browser in ['Firefox', 'IE']:
#             ia_runobj.verify_report_table_margin(table_elem, margin=True, expected_table_elem="72pt")
        expected_margin = "margin-left:72pt;margin-right:72pt;margin-top:72pt;margin-bottom:72pt" if Global_variables.browser_name == 'edge' else 'margin: 72pt;'
        ia_runobj.verify_report_table_margin(table_elem, style_margin=True, expected_table_elem=expected_margin)
        
        """ 7. Click "IA" > "Save".             """
        """ 8. Enter Title = "C2227578".        """
        """ 9. Click "Save".                    """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
        """ 10. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)        
        
if __name__ == '__main__':
    unittest.main()