'''
Created on 30-Dec-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222782
TestCase Name = Verify conditional styling using LESS-THAN-OR-EQUAL-TO statement, restyle, save and reopen
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222782_TestClass(BaseTestCase):

    def test_C2222782(self):
        
        Test_Case_ID = "C2222782"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 2. Double click COUNTRY, CAR, DEALER_COST        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        
        
        """ 3. Click on DEALER_COST field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 3: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultobj.select_field_on_canvas("TableChart_1", 3)
        
        
        """ 4. Display tab expands -> Click on Traffic Lights        """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 5. Select dropdown arrow and choose LESS THAN OR EQUAL TO.        """
        """ 6. Select the other dropdown arrow and enter value = "5063" and click "Ok"        """
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(1, field_name='DEALER_COST', relation_name='Greater than', Field_Value_txt='0')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, field_name='DEALER_COST', relation_name='Less than or equal to', filter_type='Constant', value_box_input='5063')
        
        
        """ 7. Click on Style tab Make some changes Bold, Italic, Font color - GREEN, Background color - Yellow (rgb(255,255,0))        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, italic=True, text_color='green', background_color='yellow')
        time.sleep(2)
        
               
        """ 8. Cick Apply then OK        """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 8.1: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222778_Ds01.xlsx", 'Step 8.2: Verify report dataset ')
        
        
        """ 9. Verify conditional styling on field values less than or equal to 5063.        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, font_color='gray8', text_value='18,621', msg='Step 9.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, font_color='gray8', text_value='14,940', msg='Step 9.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 10, bg_cell_no=1,bg_color='yellow', font_color='green', text_value='4,292', bold=True, italic=True, msg='Step 9.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=2,bg_color='yellow', font_color='green', text_value='4,631', bold=True, italic=True, msg='Step 9.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 16, font_color='gray8', text_value='16,235', msg='Step 9.5:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, font_color='gray8', text_value='25,000', msg='Step 9.6:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, bg_cell_no=3,bg_color='yellow', font_color='green', text_value='2,626', bold=True, italic=True, msg='Step 9.7:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 23, bg_cell_no=4,bg_color='yellow', font_color='green', text_value='2,886', bold=True, italic=True, msg='Step 9.8:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 26, bg_cell_no=5,bg_color='yellow', font_color='green', text_value='5,063', bold=True, italic=True, msg='Step 9.9:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, font_color='gray8', text_value='49,500', msg='Step 9.10:')
        
        
        """ 10. Click Save in the toolbar > Save As C2222782 > click Save        """
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        
        
        """ 11. Click "Run" and Verify the traffic light condition is applied        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222778_run_Ds01.xlsx" , 'Step 10: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 3, font_color='gray8', text_value='18,621', msg='Step 10.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 3, font_color='gray8', text_value='14,940', msg='Step 10.2:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 3, bg_color='yellow', font_color='green', text_value='4,292', bold=True, italic=True, msg='Step 10.3:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 3, bg_color='yellow', font_color='green', text_value='4,631', bold=True, italic=True, msg='Step 10.4:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 3, font_color='gray8', text_value='16,235', msg='Step 10.5:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 7, 3, font_color='gray8', text_value='25,000', msg='Step 10.6:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 3, bg_color='yellow', font_color='green', text_value='2,626', bold=True, italic=True, msg='Step 10.7:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 9, 3, bg_color='yellow', font_color='green', text_value='2,886', bold=True, italic=True, msg='Step 10.8:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 10, 3, bg_color='yellow', font_color='green', text_value='5,063', bold=True, italic=True, msg='Step 10.9:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 11, 3, font_color='gray8', text_value='49,500', msg='Step 10.10:')
        
        
        """ 12. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        
        """ 13. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222782.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("ia"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        
        """ 14. Verify the following report is displayed            """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 14.1: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222778_Ds01.xlsx", 'Step 14.2: Verify report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, font_color='gray8', text_value='18,621', msg='Step 14.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, font_color='gray8', text_value='14,940', msg='Step 14.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 10, bg_cell_no=1,bg_color='yellow', font_color='green', text_value='4,292', bold=True, italic=True, msg='Step 14.5:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=2,bg_color='yellow', font_color='green', text_value='4,631', bold=True, italic=True, msg='Step 14.6:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 16, font_color='gray8', text_value='16,235', msg='Step 14.7:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, font_color='gray8', text_value='25,000', msg='Step 14.8:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, bg_cell_no=3,bg_color='yellow', font_color='green', text_value='2,626', bold=True, italic=True, msg='Step 14.9:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 23, bg_cell_no=4,bg_color='yellow', font_color='green', text_value='2,886', bold=True, italic=True, msg='Step 14.10:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 26, bg_cell_no=5,bg_color='yellow', font_color='green', text_value='5,063', bold=True, italic=True, msg='Step 14.11:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, font_color='gray8', text_value='49,500', msg='Step 14.12:')
        
        
        """ 15. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()