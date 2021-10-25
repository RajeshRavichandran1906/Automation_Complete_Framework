'''
Created on 30-NOV-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222586
TestCase Name = Verify Dollar currency symbols is applied
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2222586_TestClass(BaseTestCase):

    def test_C2222586(self):
        
        Test_Case_ID = "C2222586"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006    """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        parent_css="#TableChart_1 div[align='justify']"
        resultobj.wait_for_property(parent_css, 1)
        time.sleep(8)
        """ 2. Double click "COUNTRY","CAR","DEALER_COST","RETAIL_COST".          """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        
        """ 3. Select "DEALER_COST" in Query pane.        """
        metaobj.querytree_field_click('DEALER_COST', 1)
        
        
        """ 4. Select "Format" > "$" (dropdown) > "Floating currency".        """
        ribbonobj.select_ribbon_item('Field', 'formatcurrency', opt='Floating Currency')
        
        
        """ 5. Verify that "$" is displayed as the currency for "DEALER_COST".        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 5.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 5.2: Verify report dataset After Apply Style')
         
         
        """ 6. Click Save in the toolbar > Save As C2222586 > click Save        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
         
         
        """ 7. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'            """
        time.sleep(2)
        utillobj.infoassist_api_logout()
         
         
        """ 8. Reopen saved FEX:
               http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222586.fex&tool=Report        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
         
         
        """ 9. Verify Preview                """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 9.1: Verify Preview column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 9.2: Verify report dataset')
        
        
        
if __name__ == '__main__':
    unittest.main()