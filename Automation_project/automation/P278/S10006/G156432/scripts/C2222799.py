'''
Created on 17-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222799
TestCase Name = Verify TL Condition with Measure and expression 'Greater Than'
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling, ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222799_TestClass(BaseTestCase):

    def test_C2222799(self):
        
        Test_Case_ID = "C2222799"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        
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
        
        
        """ 3. Click on CAR field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )    """
        ia_resultobj.select_field_on_canvas("TableChart_1", 2)
        
        
        """ 4. Display tab expands -> Click on Traffic Lights        """
        time.sleep(3)
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(3)
        
        
        """ 5. Click on CAR drop down menu and select DEALER_COST in TL condition window            """
        """ 6. Select dropdown arrow and choose "Greater Than"                                      """
        """ 7. Select the other dropdown arrow and enter value = "7500" and click "Ok"              """
        ia_stylingobj.traffic_light_create_new(1, field_name='DEALER_COST', relation_name='Greater than', filter_type='Constant', value_box_input='7500')
        
        
        """ 8. Now click on Style tab Make changes Bold, Font size-12, Text Color - RED and Click "Ok"              """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, font_size='12', text_color='red')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        
        
        """ 9. Verify the preview applied with TL condition        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 9: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222581_Ds01.xlsx", 'Step 9.1: Verify Canvas report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, bold=True, font_size='12pt', font_color='red', text_value='JENSEN', msg='Step 9.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, font_size='9pt', font_color='gray8', text_value='TRIUMPH', msg='Step 9.3:')
        
        
        """ 10. Click "Run"            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        
        """ 11. Verify that TL condition is applied with styling            """
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222581_run_Ds01.xlsx" , 'Step 11: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 2, bold=True, font_size='12pt', font_color='red', text_value='JENSEN', msg='Step 11.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 2, font_size='9pt', font_color='gray8', text_value='TRIUMPH', msg='Step 11.2:')
        
        
        """ 12. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        self.driver.switch_to_default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        
        
if __name__ == '__main__':
    unittest.main()