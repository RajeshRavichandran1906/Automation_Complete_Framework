'''
Created on 30-NOV-2016

@author: Gobizen

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222570
TestCase Name = Verify Styling with Data Bars present
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222570_TestClass(BaseTestCase):

    def test_C2222570(self):
        
        Test_Case_ID = "C2222570"
        Test_Case_ID_Dataset = "C2222569"
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
        
        
        """ 2. Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".            """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        time.sleep(8)
        
        """ 3. Select DEALER_COST in the Query window        """
        metaobj.querytree_field_click('DEALER_COST', 1)
        
        
        """ 4. Click Data Bars in the Display section         """
        time.sleep(6)
        ribbonobj.select_ribbon_item('Field', 'databars')
        time.sleep(3)
        ia_resultobj.verify_live_preview_data_bars('TableChart_1', 'Step 4: Verify Data Bars Display in Live Preview', expected_number_of_bars=10, index=3, color='light_gray')
        
        
        """5. Select RETAIL_COST in the Query window        """
        metaobj.querytree_field_click('RETAIL_COST', 1)
       
        
        """6. Click Data Bars in the Display section        """
        time.sleep(6)
        ribbonobj.select_ribbon_item('Field', 'databars')
        time.sleep(3)
        ia_resultobj.verify_live_preview_data_bars('TableChart_1', 'Step 4: Verify Data Bars Display in Live Preview', expected_number_of_bars=20, index=7, color='light_gray')
        
        
        """7. Click Header and Footer in the Report Section        """
        """8. In Report Header > type Report Header > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow        """
        ia_stylingobj.create_header_footer('ribbon','Report Header', 'Report Header', font_name='COMIC SANS MS', text_color='blue',background_color='yellow')
        
        """9. In Report Footer > type Report Footer > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow"""
        """10.  Click Apply > Click OK      """
        time.sleep(2)
        ia_stylingobj.create_header_footer('frame', 'Report Footer', 'Report Footer', font_name='COMIC SANS MS', text_color='blue', background_color='yellow', btn_apply=True, btn_ok=True)
        
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 10: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 10.1:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=22, bg_color='yellow', msg='Step 10.2: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 10.3:')
        time.sleep(3)
        
        
    
        
        """ 11. Click Style in the Report section        """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        """ 12. Click Font Color > Select Magenta        """
        """ 13. Click Background Color > Select Cyan    """
        """ 14. Click Apply and click ok                """
        
        ia_stylingobj.set_report_style(text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        time.sleep(3)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 14.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID_Dataset+"_Ds01.xlsx", 'Step 14.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=6,bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 14.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=61,bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 14.4:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 14.5: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 14.6:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=66, bg_color='yellow', msg='Step 14.7: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 14.8:')
        ia_resultobj.verify_live_preview_data_bars('TableChart_1', 'Step 14.9: Verify Data Bars Display in Live Preview', expected_number_of_bars=20, index=7, color='light_gray')
        
       
        """ 15. Click Run and verify output                """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 15.1: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 3, bg_color='cyan', font_color='magenta', text_value='DEALER_COST', msg='Step 15.2:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 2, bg_color='cyan', font_color='magenta', text_value='ALFA ROMEO', msg='Step 15.3:')
        ia_runobj.verify_header_footer_stying(1, bg_color='yellow', font_color='blue', text_value='Report Header', font_name='comic sans ms', font_size='14pt', 
                                             msg='Step 15.4: ')
        ia_runobj.verify_header_footer_stying(2, bg_color='yellow', font_color='blue', text_value='Report Footer', font_name='comic sans ms', font_size='10pt', 
                                             msg='Step 15.5: ')
        ia_runobj.verify_table_cell_data_bars("table[summary='Summary']", expected_number_of_bars=20, expected_color='light_gray', expected_color_index=1, msg='Step 15.6:')
        
        
        """ 16. Click Save in the toolbar > Save As C2222570 > click Save        """
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(2)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
       
        
        """ 17. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'        """
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ 18. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222570.fex&tool=Report    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(2)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006')
        
        
        """ 19. Verify Preview                """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(3)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 19.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID_Dataset+"_Ds01.xlsx", 'Step 19.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5,bg_cell_no=6, bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 19.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37,bg_cell_no=61, bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 19.4:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 19.5: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 19.6:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=66, bg_color='yellow', msg='Step 19.7: ')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 19.8:')
        ia_resultobj.verify_live_preview_data_bars('TableChart_1', 'Step 19.9: Verify Data Bars Display in Live Preview', expected_number_of_bars=20, index=7, color='light_gray')
        
                
        
        
if __name__ == '__main__':
    unittest.main()