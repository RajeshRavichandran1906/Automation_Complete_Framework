'''
Created on 25-NOV-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222566
TestCase Name = Verify Styling with PDF
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2222566_TestClass(BaseTestCase):

    def test_C2222566(self):
        
        Test_Case_ID = "C2222566"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006     """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#TableChart_1", 120)
        
        
        """ 2. In Report area > switch format to PDF        """
        ribbonobj.change_output_format_type('pdf')
        
        """ 3. Select "COUNTRY","CAR","DEALER_COST","RETAIL_COST".        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        
        """ 4. Click Header and Footer in the Report Section        """
        """ 5. In Report Header > type Report Header > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow    """
        time.sleep(4)
        ia_stylingobj.create_header_footer('ribbon','Report Header', 'Report Header', font_name='COMIC SANS MS', text_color='blue',background_color='yellow')
        
        
        """ 6. In Report Footer > type Report Footer > set Font to Comic Sans MS > Font color to Blue > Background color to Yellow    """
        """ 7. Click Apply > Click OK    """
        time.sleep(2)
        ia_stylingobj.create_header_footer('frame', 'Report Footer', 'Report Footer', font_name='COMIC SANS MS', text_color='blue',background_color='yellow', btn_apply=True, btn_ok=True)
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 6: Report Header, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 6.1:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=2, bg_color='yellow', msg='Step 6.2: Report Footer, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 6.3:')
        
        
        """ 8. Click Style in the Report section    """
        ribbonobj.select_ribbon_item('Home', 'style')
        
        
        """ 9. Click Font Color > Select Magenta        """
        """ 10. Click Background Color > Select Cyan    """
        """ 11. Click Apply and click ok                """
        ia_stylingobj.set_report_style(bold=True, text_color='magenta', background_color='cyan', btn_apply=True, btn_ok=True)
        utillobj.synchronize_until_element_is_visible("#TableChart_1", 120)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 11.1: Verify Canvas column titles After Apply Style")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 11.2: Verify report dataset After Apply Style')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5,bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 11.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42, bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 11.4:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 11.5: Report Header, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 11.6:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=46, bg_color='yellow', msg='Step 11.7: Report Footer, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 11.8:')
        
        
        """ 12. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(7)
        elem=(By.CSS_SELECTOR,"#resultArea")
        resultobj._validate_page(elem)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_' + browser + '_Actual_step12', image_type='actual',x=1, y=1, w=-1, h=-1)  
        


        """ 13. Click Save in the toolbar > Save As C2222566 > click Save    """
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
         
         
        """ 14. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'    """
        time.sleep(2)
        utillobj.infoassist_api_logout()
         
        """ 15. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222566.fex&tool=Report    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
 
 
        """ 16. Verify Preview        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 16.1: Verify Preview column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, Test_Case_ID+"_Ds01.xlsx", 'Step 16.2: Verify report dataset')
        ia_resultobj.verify_report_cell_property("TableChart_1", 5, bg_cell_no=5,bg_color='cyan', font_color='magenta', text_value='ENGLAND', msg='Step 16.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 37, bg_cell_no=42, bg_color='cyan', font_color='magenta', text_value='BMW', msg='Step 16.4:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, cell_no=1, bg_color='yellow', msg='Step 16.5: Report Header, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 1, font_color='blue', text_value='Report Header', font_name='Comic Sans MS', msg='Step 16.6:')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, cell_no=46, bg_color='yellow', msg='Step 16.7: Report Footer, IA-6142- Highlighted Header/Footer text background color is not applied')
        ia_resultobj.verify_report_header_footer_property('TableChart_1', 2, font_color='blue', text_value='Report Footer', font_name='Comic Sans MS', msg='Step 16.8:')
        
if __name__ == '__main__':
    unittest.main()