'''
Created on 23-NOV-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222563
TestCase Name = Verify Styling Report then Theme
'''
import unittest, time 
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling

class C2222563_TestClass(BaseTestCase):

    def test_C2222563(self):
        
        '''
        Testcase Varibales
        '''
        Test_Case_ID = "C2222563"
        
        '''
        Class & Objects
        '''
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
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'COUNTRY', 30)
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'CAR', 30)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        utillobj.synchronize_with_visble_text('#queryTreeColumn', 'DEALER_COST', 30)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        
        """ 3. Click Style in the Report section        """
        ribbonobj.select_ribbon_item('Home', 'style')
         
        """ 4. Verify the Bold is selected by default               """
        """ 5. Click Font Color > Select Magenta                    """
        """ 6. Click Background Color > Select Cyan                 """
        """ 7. Click Apply and Click OK                             """
        ia_stylingobj.set_report_style(bold=True, text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,bg_cell_no=5, bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 06.01:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37,bg_cell_no=42, bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 06.02:')
        
        """ 8. Select Theme > Select EnBlack_DarkComp    """
        """ 9. Click Open                                  """
        ribbonobj.select_theme('Legacy Templates', 'ENBlack_DarkComp.sty')
        utillobj.synchronize_with_number_of_element("#TableChart_1  div[class^='x'][class*='title']", 4, resultobj.home_page_long_timesleep)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 08.01: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 08.02: Verify report dataset', no_of_cells=4)
        ia_resultobj.verify_report_cell_property("TableChart_1", 2, bg_cell_no=2, bg_color='dark_gray', font_color='white', text_value='CAR', msg='Step 08.03: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5, bg_color='gray25', font_color='white', text_value='ENGLAND', msg='Step 08.04: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 16, bg_cell_no=18, bg_color='gray45', font_color='white', text_value='PEUGEOT', msg='Step 08.05: ')
            
        """ 9. Click Run and verify output       """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 09.01: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 1, 2, bg_color='dark_gray', font_color='white', text_value='CAR', msg='Step 09.02: ')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, bg_color='gray25', font_color='white', text_value='ENGLAND', msg='Step 09.03: ')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 2, bg_color='gray45', font_color='white', text_value='PEUGEOT', msg='Step 09.04: ')
            
        """ 10. Click Save in the toolbar > Save As C2222563 > click Save       """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
            
        """ 11. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
                  
        """ 12. Reopen saved FEX: 
               http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222563.fex&tool=Report        """
        time.sleep(2)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10006',mrid='mrid', mrpass='mrpass')       
            
        """ 13. Verify Preview        """
        utillobj.synchronize_with_number_of_element("#TableChart_1  div[class^='x'][class*='title']", 4, resultobj.home_page_long_timesleep)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 13.01: Verify Preview column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 13.02: Verify report dataset', no_of_cells=4)
        ia_resultobj.verify_report_cell_property("TableChart_1", 2, bg_cell_no=2, bg_color='dark_gray', font_color='white', text_value='CAR', msg='Step 13.03: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5, bg_color='gray25', font_color='white', text_value='ENGLAND', msg='Step 13.04: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 16, bg_cell_no=18, bg_color='gray45', font_color='white', text_value='PEUGEOT', msg='Step 13.05: ')
          
if __name__ == '__main__':
    unittest.main()