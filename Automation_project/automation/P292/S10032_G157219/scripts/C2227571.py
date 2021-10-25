'''

Edited by Niranjan on 06-Nov-2017.

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227571
TestCase Name = Verify Theme from Legacy Templates
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227571_TestClass(BaseTestCase):

    def test_C2227571(self):
        
        Test_Case_ID = "C2227571"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """ 2. Double click "COUNTRY", "CAR", "DEALER_COST".            """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(6)
        """ 3. Verify the following report is displayed.            """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 3.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 3.2: Verify report dataset', no_of_cells=4)
        
        """ 4. Select "Home" > Click "Theme" icon.                            """
        """ 5. Select "Legacy Templates" under Libraries (left panel)         """
        """ 6. Select Theme = "ENInformationBuilders_Medium1.sty"             """
        """ 7. Click "Open".                                                  """
        ribbonobj.select_theme('Legacy Templates', 'ENInformationBuilders_Medium1.sty')
        
        
        """ 8. Verify the selected theme has been applied to the report.        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 8.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 8.2: Verify report dataset after applying styling.', no_of_cells=4)
        ia_resultobj.verify_report_cell_property("TableChart_1", 2, bg_cell_no=2, bg_color='havelock_blue', font_color='white', text_value='CAR', msg='Step 8.3: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bg_cell_no=4, bg_color='light_steel_blue', font_color='black', text_value='ENGLAND', msg='Step 8.4: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 12 ,bg_cell_no=14, bg_color='hawkes_blue', font_color='black', text_value='PEUGEOT', msg='Step 8.5: ')

        """ 9. Click "Run".                """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_Ds02.xlsx", 'Step 9: Verify report dataset After Run')

        """ 10. Verify the report is displayed.            """
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 1, 2, bg_color='havelock_blue', font_color='white', text_value='CAR', msg='Step 10.1: ')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, bg_color='light_steel_blue', font_color='black', text_value='ENGLAND', msg='Step 10.2: ')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 2, bg_color='hawkes_blue', font_color='black', text_value='PEUGEOT', msg='Step 10.3: ')
        
        """ 11. Click "IA" > "Save".                     """
        """ 12. Enter Title = "C2227571".                """
        """ 13. Click "Save".                            """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """ 14. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp            """
        utillobj.infoassist_api_logout()
        
        """ 15. Reopen saved FEX:    
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227571.fex&tool=Report
        """
        uname=(By.CSS_SELECTOR, "input[id='SignonUserName']")
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        
        """ 16. Verify Theme                            """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 16.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 16.2: Verify report dataset after reopening the fex.', no_of_cells=4)
        ia_resultobj.verify_report_cell_property("TableChart_1", 2, bg_cell_no=2, bg_color='havelock_blue', font_color='white', text_value='CAR', msg='Step 16.3: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bg_cell_no=4, bg_color='light_steel_blue', font_color='black', text_value='ENGLAND', msg='Step 16.4: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 12 ,bg_cell_no=14, bg_color='hawkes_blue', font_color='black', text_value='PEUGEOT', msg='Step 16.5: ')

        """ 17. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp         """
        time.sleep(2)

if __name__ == '__main__':
    unittest.main() 