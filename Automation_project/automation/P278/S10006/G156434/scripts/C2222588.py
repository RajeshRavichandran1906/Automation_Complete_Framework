'''
Created on 01-Dec-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222588
TestCase Name = Verify Japanese Yen currency symbols is applied
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon, ia_styling, ia_resultarea
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2222588_TestClass(BaseTestCase):

    def test_C2222588(self):
        
        Test_Case_ID = "C2222588"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """ 1. Reopen saved FEX in the test case C2222586:
               http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222586.fex&tool=Report    """
        utillobj.infoassist_api_edit('C2222586', 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """ Select "Home" > "Report" > "Style" > "$"          """
        """ 2. Select "Japanese Yen" as the currency.         """
        """ 3. Click "Apply" and click ok                     """
        ribbonobj.select_ribbon_item('Home', 'style')
        time.sleep(2)
        ia_stylingobj.set_report_style(currency='JPY', btn_apply=True, btn_ok=True)

        
        """ 4. Verify that the currency symbol has changed for "DEALER_COST".        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 4.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 4.2: Verify report dataset After Apply Style')
          
          
        """ 5. Click Save in the toolbar > Save As C2222588 > click Save        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
          

        
        
if __name__ == '__main__':
    unittest.main()