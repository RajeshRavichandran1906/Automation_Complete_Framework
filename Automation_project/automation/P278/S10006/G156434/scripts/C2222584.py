'''
Created on 29-NOV-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222584
TestCase Name = Verify Bold, Italic, Underline styling
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222584_TestClass(BaseTestCase):

    def test_C2222584(self):
        
        Test_Case_ID = "C2222584"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006    """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 2. Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        
        
        """ 3. Click Style in the Report section        """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        
        """ 4. Click Italic and Click Underline               """
        """ 5. Click Apply                              """
        """ 6. Click OK                                 """
        ia_stylingobj.set_report_style(italic=True, bold=True, underline=True, btn_apply=True, btn_ok=True)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 6.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 6.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, italic=True, underline=True, font_size='9pt', text_value='ENGLAND', msg='Step 6.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, italic=True, underline=True, font_size='9pt', text_value='BMW', msg='Step 6.4:')
        
        
        """ 7. Click Run and verify output                """
        time.sleep(2)
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 7: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 1, 3, italic=True, underline=True, font_size='9pt', text_value='DEALER_COST', msg='Step 7.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 2, italic=True, underline=True, font_size='9pt', text_value='ALFA ROMEO', msg='Step 7.2:')
        
        
        """ 8. Click Save in the toolbar > Save As C2222584 > click Save            """
        driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        
        """ 9. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        
        """ 10. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222584.fex&tool=Report       """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(2)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006')
        
        
        """ 11. Verify Preview                """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        resultobj.wait_for_property(parent_css, 8)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 11.1: Verify Preview column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 11.2: Verify report dataset')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, italic=True, underline=True, font_size='9pt', text_value='ENGLAND', msg='Step 11.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, italic=True, underline=True, font_size='9pt', text_value='BMW', msg='Step 11.4:')
        

if __name__ == '__main__':
    unittest.main()