'''
Created on 4-Jan-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222804
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling,\
    define_compute
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222804_TestClass(BaseTestCase):

    def test_C2222804(self):
        
        Test_Case_ID = "C2222804"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        def_comp = define_compute.Define_Compute(self.driver)
        
        
        """ 
        Step01: Launch IA Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 
        Step02: Double click COUNTRY, CAR, DEALER_COST        
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        
        """
        Step03: Click on Data Tab -> Summary (Compute)
        Step04: Double click DEALER_COST and click *10 in Summary Field (Compute) window
        Step05: Click "Ok" and Verify the created compute field added under Sum in query pane
        """
        def_comp.invoke_define_compute_dialog('compute')
        time.sleep(2)
        def_comp.enter_define_compute_parameter('Compute_1', 'D12.2', 'DEALER_COST', 1)
        time.sleep(3)
        def_comp.select_calculation_btns('mult')
        def_comp.select_calculation_btns('one')
        def_comp.select_calculation_btns('zero')
        time.sleep(2)
        def_comp.close_define_compute_dialog('ok')
        time.sleep(2)
        metaobj.verify_query_pane_field('Sum', 'Compute_1', 2, "Step05.1: Verify compute field added under Sum in query pane")
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST','Compute_1']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step05.2: Verify Canvas column titles ")
        time.sleep(2)
        
        """
        Step06: Right click on "DEALER_COST" field from query pane
        """
        metaobj.querytree_field_click('DEALER_COST', 1, 1,'More','Traffic Light Conditions...')
        
        """
        Step07: Click the field dropdown and select field 'Compute_1'
        Step08: Click the Condition dropdown and select 'Less Than'
        Step09: Click the Value dropdown and enter the value '45000', Click "OK"
        """
        ia_stylingobj.traffic_light_create_new(1, field_name='Compute_1',relation_name='Less than', filter_type='Constant',value_box_input='45000')
        time.sleep(2)
        
        """
        Step10: Now click on Style tab Make changes Bold, Text Color - RED , BG Color - YELLOW and Click "Ok"
        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, text_color='red', background_color='yellow')
        time.sleep(2)
        
        """
        Step11: Now click on 'New' button in TL window   
        Step12: Click the field dropdown and select field 'Compute_1'
        Step13: Click the Condition dropdown and select 'Equal to'
        Step14: Click the Value dropdown and enter the value '46310', Click "OK"     
        """
        ia_stylingobj.traffic_light_toolbar_select('New', 2)
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(2, field_name='Compute_1',relation_name='Equal to', filter_type='Constant',value_box_input='46310')
        time.sleep(2)
        
        """
        Step15: Now click on Style tab Make changes - Bold, BG Color - yellow, Font color -Blue
        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 2, bold=True, text_color='blue', background_color='yellow')
        time.sleep(2)
        
        """
        Step16: Click apply and "OK"
        """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        
        """
        Step17: Verify the preview with applied TL condition
        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, font_color='gray8', text_value='18,621', msg='Step 17.1a:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 10, font_color='gray8', text_value='14,940', msg='Step 17.1b:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=1,bg_color='yellow', font_color='red', text_value='4,292', msg='Step 17.1c:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 17, bg_cell_no=2,bg_color='yellow', font_color='blue', text_value='4,631', msg='Step 17.1d:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, font_color='gray8', text_value='16,235', msg='Step 17.1e:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, font_color='gray8', text_value='25,000', msg='Step 17.1f:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=3,bg_color='yellow', font_color='red', text_value='2,626', msg='Step 17.1g:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 31, bg_cell_no=4,bg_color='yellow', font_color='red', text_value='2,886', msg='Step 17.1h:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 35, font_color='gray8', text_value='5,063', msg='Step 17.1i:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 38, font_color='gray8', text_value='49,500', msg='Step 17.1j:')
        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'Compute_1']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 17.2: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222804_Ds01.xlsx", 'Step 17.3: Verify report dataset ')
        
        """
        Step18: Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """
        Step19: Verify the output applied proper TL condition
        """
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222804_run_Ds01.xlsx" , 'Step 19: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 3, font_color='gray8', text_value='18,621', msg='Step 19.1a:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 3, font_color='gray8', text_value='14,940', msg='Step 19.1b:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 3, bg_color='yellow', font_color='red', text_value='4,292', msg='Step 19.1c:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 3, bg_color='yellow', font_color='blue', text_value='4,631', msg='Step 19.1d:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 3, font_color='gray8', text_value='16,235', msg='Step 19.1e:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 7, 3, font_color='gray8', text_value='25,000', msg='Step 19.1f:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 3, bg_color='yellow', font_color='red', text_value='2,626', msg='Step 19.1g:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 9, 3, bg_color='yellow', font_color='red', text_value='2,886', msg='Step 19.1h:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 10, 3, font_color='gray8', text_value='5,063', msg='Step 19.1i:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 11, 3, font_color='gray8', text_value='49,500', msg='Step 19.1j:')

        """
        Step20: Click "IA" menu > "Save As" > "C2222804" > Click Save
        """
        self.driver.switch_to_default_content()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        
        """
        Step21: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """
        Step22: Reopen saved FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222804.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        """
        Step23: Verify Preview
        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, font_color='gray8', text_value='18,621', msg='Step 23.1a:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 10, font_color='gray8', text_value='14,940', msg='Step 23.1b:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=1,bg_color='yellow', font_color='red', text_value='4,292', msg='Step 23.1c:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 17, bg_cell_no=2,bg_color='yellow', font_color='blue', text_value='4,631', msg='Step 23.1d:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, font_color='gray8', text_value='16,235', msg='Step 23.1e:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, font_color='gray8', text_value='25,000', msg='Step 17.1f:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=3,bg_color='yellow', font_color='red', text_value='2,626', msg='Step 23.1g:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 31, bg_cell_no=4,bg_color='yellow', font_color='red', text_value='2,886', msg='Step 23.1h:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 35, font_color='gray8', text_value='5,063', msg='Step 23.1i:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 38, font_color='gray8', text_value='49,500', msg='Step 23.1j:')
        
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST','Compute_1']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 23.2: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222804_Ds01.xlsx", 'Step 23.3: Verify report dataset ')
        
        """
        Step24: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()