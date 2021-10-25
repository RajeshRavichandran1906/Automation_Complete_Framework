'''
Created on 23-NOV-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222565
TestCase Name = Verify Styling with Header & Footer
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2222565_TestClass(BaseTestCase):

    def test_C2222565(self):
        
        Test_Case_ID = "C2222565"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
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
        
        
        """ 3. Click Header and Footer in the Report Section        """
        """ 4. In Report Header > type Report Header > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow   """
        ia_stylingobj.create_header_footer('ribbon','Report Header', 'Report Header', font_name='COMIC SANS MS', text_color='blue',background_color='yellow')
        time.sleep(2)
        """ 5. In Report Footer > type Report Footer > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow """
        """ 6. Click Apply > Click OK    """
        ia_stylingobj.create_header_footer('frame', 'Report Footer', 'Report Footer', font_name='COMIC SANS MS', text_color='blue',background_color='yellow', btn_apply=True, btn_ok=True)
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 6: Report Header, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 6.1:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=2, bg_color='yellow', msg='Step 6.2: Report Footer, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 6.3:')
         
        
        """ 7. Click Style in the Report section        """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        
        """ 8. Click Font Color > Select Magenta        """
        """ 9. Click Background Color > Select Cyan     """
        """ 10. Click Apply and click ok                """
        ia_stylingobj.set_report_style(bold=True, text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        utillobj.synchronize_until_element_is_visible("#TableChart_1", 120)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 10.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 10.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5,bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 10.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37,bg_cell_no=42, bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 10.4:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 10.5: Report Header, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 10.6:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=46, bg_color='yellow', msg='Step 10.7: Report Footer, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 10.8:')
        
        
        """ 11. Click Run and verify output                 """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 11: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 3, bg_color='cyan', font_color='magenta', text_value='DEALER_COST', msg='Step 11.3:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 2, bg_color='cyan', font_color='magenta', text_value='ALFA ROMEO', msg='Step 11.4:')
        
              
        """ 12. Click Save in the toolbar > Save As C2222565 > click Save       """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
              
        """ 13. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
              
              
        """ 14. Reopen saved FEX: 
               http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222565.fex&tool=Report       """
              
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006',mrid='mrid', mrpass='mrpass')
              
              
        """ 15. Verify Preview        """
        utillobj.synchronize_until_element_is_visible("#TableChart_1", 250)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 15.1: Verify Preview column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 15.2: Verify report dataset')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,bg_cell_no=5, bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 15.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42,bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 15.4:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 15.5: Report Header, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 15.6:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=46, bg_color='yellow', msg='Step 15.7: Report Footer, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 15.8:')
         
if __name__ == '__main__':
    unittest.main()