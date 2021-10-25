'''
Created on 23-NOV-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222564
TestCase Name = Verify Theme applied then Styling Report
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222564_TestClass(BaseTestCase):

    def test_C2222564(self):
        
        Test_Case_ID = "C2222564"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006      """
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
        
        
        """ 3. Select Theme > Legacy Templates > Select EnBlack_DarkComp.sty        """
        """ 4. Click OK                                                             """
        ribbonobj.select_theme('Legacy Templates', 'ENBlack_DarkComp.sty')
        time.sleep(4)
        ia_resultobj.verify_report_cell_property("TableChart_1", 1,bg_cell_no=1, bg_color='dark_gray', font_color='white', text_value='COUNTRY', msg='Step 4.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,bg_cell_no=5, bg_color='gray25', font_color='white', text_value='ENGLAND', msg='Step 4.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37,bg_cell_no=42, bg_color='gray45', font_color='white', text_value='BMW', msg='Step 4.3:')
        
        
        """ 5. Click Style in the Report section                                    """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        
        """ 6. Click Font Color > Select Magenta        """
        """ 7. Click Background Color > Select Cyan    """
        """ 8. Click Apply and click ok                """
        ia_stylingobj.set_report_style(bold=True, text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 8.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 8.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,bg_cell_no=5, bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 8.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42,bg_color='gray45', font_color='magenta', text_value='BMW', msg='Step 8.4:')
        
        
        """ 9. Click Run and verify output            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 9: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 1, 3, bg_color='cyan', font_color='magenta', text_value='DEALER_COST', msg='Step 9.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 7, 2, bg_color='gray45', font_color='magenta', text_value='MASERATI', msg='Step 9.2:')
      
              
        """ 10. Click Save in the toolbar > Save As C2222564 > click Save       """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
              
        """ 11. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
              
              
        """ 12. Reopen saved FEX: 
               http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222564.fex&tool=Report       """
              
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
              
              
        """ 13. Verify Preview        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        resultobj.wait_for_property(parent_css, 8)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 13.1: Verify Preview column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 13.2: Verify report dataset')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5,bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 13.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37,bg_cell_no=42, bg_color='gray45', font_color='magenta', text_value='BMW', msg='Step 13.4:')
         
        
if __name__ == '__main__':
    unittest.main()