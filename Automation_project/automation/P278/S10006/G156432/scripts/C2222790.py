'''
Created on 03-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222790
TestCase Name = Verify conditional styling on a column based on another field in Traffic Light dialog - use a Measure
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222790_TestClass(BaseTestCase):

    def test_C2222790(self):
        
        Test_Case_ID = "C2222790"
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
        
        
        """ 2. Double click COUNTRY, CAR, DEALER_COST            """
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
        
        
        """ 4. Display tab expands -> Click on Traffic Lights            """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 5. Click on COUNTRY drop down menu and select DEALER_COST         """
        """ 6. Select dropdown arrow and choose "Greater than"                """
        """ 7. Select the other dropdown arrow and enter value = "7427" and click "Ok"        """
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(1, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, field_name='DEALER_COST', relation_name='Greater than', filter_type='Constant', value_box_input='7427')
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(1, field_name='DEALER_COST', relation_name='Greater than', Field_Value_txt='7427')
        
        
        """ 8. Now click on Style tab Make changes Bold, Font size-12, Color-RED            """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, font_size='12', text_color='red')
        time.sleep(2)
        
        
        """ 9. Cick Apply then OK            """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 9: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222778_Ds01.xlsx", 'Step 9.1: Verify report dataset ')
        
        
        
        """ 10. Notice that field values "Greater than" to 7427, field values are applied with conditional styling        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bold=True, font_size='12pt', font_color='red', text_value='ENGLAND', msg='Step 10.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, font_size='9pt', font_color='gray8', text_value='FRANCE', msg='Step 10.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 14, bold=True, font_size='12pt', font_color='red', text_value='ITALY', msg='Step 10.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, font_size='9pt', font_color='gray8', text_value='JAPAN', msg='Step 10.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, font_size='9pt', font_color='gray8', text_value='W GERMANY', msg='Step 10.5:')
        
        
        """ 11. Click "Run"                """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222778_run_Ds01.xlsx" , 'Step 11: Verify report dataset')
        
        
        """ 12. Verify the condition styling is applied                             """
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, bold=True, font_size='12pt', font_color='red', text_value='ENGLAND', msg='Step 12.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 1, font_size='9pt', font_color='gray8', text_value='FRANCE', msg='Step 12.2:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 1, bold=True, font_size='12pt', font_color='red', text_value='ITALY', msg='Step 12.3:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 1, font_size='9pt', font_color='gray8', text_value='JAPAN', msg='Step 12.4:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 10, 1, font_size='9pt', font_color='gray8', text_value='W GERMANY', msg='Step 12.5:')
        
        
        
        """ 13. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp             """
        time.sleep(2)
        driver.switch_to_default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        time.sleep(2)

if __name__ == '__main__':
    unittest.main()