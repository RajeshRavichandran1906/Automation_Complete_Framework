'''
Created on 29-NOV-2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222556
TestCase Name = Verfiy Resetting Font and Background colors
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2222556_TestClass(BaseTestCase):

    def test_C2222556(self):
        
        Test_Case_ID = "C2222556"
        Test_Case_ID_dataset = "C2222583"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006     """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """ 2. Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".      """
        
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        time.sleep(5)
        
        
        
        """3. Click Style in the Report section    """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        """4. Click Font Color > Select Magenta         """
        """5. Click Background Color > Select Cyan        """
        """6. Click Apply and Click Ok                     """
        
        ia_stylingobj.set_report_style(text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 10.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID_dataset+"_Ds01.xlsx", 'Step 10.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5,bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 10.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42, bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 10.4:')
        
        
        
        """7. Again Click Style in Report Section and Click Font Color > Select Black        """
        """8. Click Background Color > Select White        """
        """9. Click Apply and click OK            """
        
        ribbonobj.select_ribbon_item('Home', 'style')
        
        ia_stylingobj.set_report_style(text_color='black', background_color='white', btn_apply=True, btn_ok=True)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 9.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID_dataset+"_Ds01.xlsx", 'Step 9.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5,bg_color='white', font_color='black', text_value='ENGLAND', msg='Step 9.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42, bg_color='white', font_color='black', text_value='BMW', msg='Step 9.4:')
        
        
              
        """ 10. Click Save in the toolbar > Save As C2222556 > click Save       """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
              
        
if __name__ == '__main__':
    unittest.main()