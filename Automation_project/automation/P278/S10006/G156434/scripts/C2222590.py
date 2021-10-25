'''
Created on 01-Dec-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222590
TestCase Name = Verify Reset to Quick Styles is applied
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2222590_TestClass(BaseTestCase):

    def test_C2222590(self):
        
        Test_Case_ID = "C2222590"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006    """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 2. Double click "COUNTRY","CAR","DEALER_COST","RETAIL_COST".          """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        parent_css="#TableChart_1 div[class^='x']"
        resultobj.wait_for_property(parent_css, 6)
        time.sleep(4)
        
        metaobj.datatree_field_click("CAR", 2, 1)
        parent_css="#TableChart_1 div[class^='x']"
        resultobj.wait_for_property(parent_css, 17)
        time.sleep(4)
        
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        parent_css="#TableChart_1 div[class^='x']"
        resultobj.wait_for_property(parent_css, 28)
        time.sleep(4)
        
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        parent_css="#TableChart_1 div[class^='x']"
        resultobj.wait_for_property(parent_css, 39)
        time.sleep(4)
        
        
        """ 3. Click Style in the Report section         """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        
        """ 4. Select Font > Select Comic Sans MS and Select Font Size > 11                   """
        """ 5. Click "Reset to Quick Styles"                                                  """
        time.sleep(2)
        ia_stylingobj.set_report_style(font_name='COMIC SANS MS', font_size='11', btn_reset=True, btn_cancel=True)

        
        """ 5. Verify that the currency symbol has changed for "DEALER_COST".        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 5.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 5.2: Verify report dataset After Apply Style')
           
           
        """ 6. Click Save in the toolbar > Save As C2222590 > click Save        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
           

        
        
if __name__ == '__main__':
    unittest.main()