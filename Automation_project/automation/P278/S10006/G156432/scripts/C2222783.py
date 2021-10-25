'''
Created on 02-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222783
TestCase Name = Verify multiple conditions using "New" option, use styling for each condition, save and reopen
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222783_TestClass(BaseTestCase):

    def test_C2222783(self):
        
        Test_Case_ID = "C2222783"
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
        
        
        """ 3. Click on COUNTRY field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 3: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultobj.select_field_on_canvas("TableChart_1", 1)
        
        
        
        """ 4. Display tab expands -> Click on Traffic Lights        """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 5. Click on values dropdown menu                        """
        """ 6. Type value: ENGLAND -> click "OK"                    """
        ia_stylingobj.traffic_light_verify_condition_row(1, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', value_box_input='ENGLAND')
        
        
        """ 7. Click on ""Style"" -> Select Bold Font, Font Color as RED, Size 12"        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, text_color='red', font_size='12')
        time.sleep(2)
        
        
        """ 8. Click on ""New"" option from Traffic Light Condition window            """
        ia_stylingobj.traffic_light_toolbar_select('New', 2)
        time.sleep(2)
        
        
        """ 9. Click on values dropdown menu                                """
        """ 10. Type value: JAPAN -> Click" OK"                             """
        ia_stylingobj.traffic_light_verify_condition_row(2, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(2, filter_type='Constant', value_box_input='JAPAN')
        
        
        """ 11. Click on ""Style"" -> Select Bold Font, Font Color as BLUE, Size 12"        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 2, bold=True, text_color='blue', font_size='12')
        time.sleep(2)
        
        
        """ 12. Click on ""New"" option from Traffic Light Condition window        """
        ia_stylingobj.traffic_light_toolbar_select('New', 3)
        time.sleep(2)
        
        
        """ 13. Click on values dropdown menu            """
        """ 14. Type value: FRANCE -> Click "OK"         """
        ia_stylingobj.traffic_light_verify_condition_row(3, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(3, filter_type='Constant', value_box_input='FRANCE')
        
        
        
        """ 15. Click on ""Style"" -> Select Bold Font, Font Color as GREEN, Size 12"        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 3, bold=True, text_color='green', font_size='12')
        time.sleep(2)
        
        
        """ 16. Click Apply, then OK            """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 16.1: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222778_Ds01.xlsx", 'Step 16.2: Verify report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bold=True, font_size='12pt', font_color='red', text_value='ENGLAND', msg='Step 16.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, bold=True, font_size='12pt', font_color='green', text_value='FRANCE', msg='Step 16.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bold=True, font_size='12pt', font_color='blue', text_value='JAPAN', msg='Step 16.5:')
        
        
        
        """ 17. Click "Run" and Verify the traffic light condition is applied            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222778_run_Ds01.xlsx" , 'Step 17: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, bold=True, font_size='12pt', font_color='red', text_value='ENGLAND', msg='Step 17.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 1, bold=True, font_size='12pt', font_color='green', text_value='FRANCE', msg='Step 17.2:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 1, bold=True, font_size='12pt', font_color='blue', text_value='JAPAN', msg='Step 17.3:')
        
        
        
        """ 18. Click Save in the toolbar > Save As C2222783 > click Save            """
        time.sleep(2)
        driver.switch_to_default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        
        
        """ 19. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        
        """ 20. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222783.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("ia"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        
        """ 21. Verify the following report is displayed            """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 21.1: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222778_Ds01.xlsx", 'Step 21.2: Verify report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bold=True, font_size='12pt', font_color='red', text_value='ENGLAND', msg='Step 21.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, bold=True, font_size='12pt', font_color='green', text_value='FRANCE', msg='Step 21.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bold=True, font_size='12pt', font_color='blue', text_value='JAPAN', msg='Step 21.5:')
        
        
        
        """ 22. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp         """
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()
    