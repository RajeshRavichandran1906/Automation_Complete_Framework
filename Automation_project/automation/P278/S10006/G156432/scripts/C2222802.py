'''
Created on 5-Jan-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222802
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

class C2222802_TestClass(BaseTestCase):

    def test_C2222802(self):
        
        Test_Case_ID = "C2222802"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        def_comp = define_compute.Define_Compute(self.driver)
        define_field_path = 'Measures/Properties->Define_1'
        
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
        Step03: Click on Data Tab -> Detail (Define)
        Step04: Double click DEALER_COST and click *10 in Detail Field (Define) window
        Step05: Click "Ok" and Verify the created define field added under Measures in data pane
        """
        def_comp.invoke_define_compute_dialog('define')
        time.sleep(2)
        def_comp.enter_define_compute_parameter('Define_1', 'D12.2', 'DEALER_COST', 1)
        time.sleep(3)
        def_comp.select_calculation_btns('mult')
        def_comp.select_calculation_btns('one')
        def_comp.select_calculation_btns('zero')
        time.sleep(2)
        def_comp.close_define_compute_dialog('ok')
        time.sleep(5)
        metaobj.verify_data_pane_field('Measures/Properties', 'Define_1', 15, "Step05.1: Verify define field added under Measures in Data Pane")
        
        """
        Step06: Double click "Define_1" in Data pane
        """
        time.sleep(4)
        metaobj.datatree_field_click(define_field_path, 2, 1)        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST','Define_1']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step05.2: Verify Canvas column titles ")
        time.sleep(2)
        
        """
        Step07: Right click on "Define_1" field from query pane
        Step08: Select More -> Traffic Light Condition
        """
        metaobj.querytree_field_click('Define_1', 1, 1,'More','Traffic Light Conditions...')
        
        """
        Step09: Click the condition dropdown arrow and select 'Less Than'
        Step10: Select the value dropdown arrow and enter the Value is 50000 and click "Ok"
        """
        ia_stylingobj.traffic_light_create_new(1, relation_name='Less than',filter_type='Constant',value_box_input='50000')
        time.sleep(2)
        
        """
        Step11: Now click on Style tab Make changes - Bold, BG Color - yellow, Font color -Blue
        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, text_color='blue', background_color='yellow')
        time.sleep(2)
       
        """
        Step12: Click apply and OK
        """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        
        """
        Step13: Verify the preview with applied TL condition
        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, font_color='gray8', text_value='186,210.00', msg='Step 13.1a:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, font_color='gray8', text_value='149,400.00', msg='Step 13.1b:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 14, bg_cell_no=1,bg_color='yellow', font_color='blue', text_value='42,920.00', msg='Step 13.1c:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=2,bg_color='yellow', font_color='blue', text_value='46,310.00', msg='Step 13.1d:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 22, font_color='gray8', text_value='162,350.00', msg='Step 13.1e:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 25, font_color='gray8', text_value='250,000.00', msg='Step 13.1f:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 29, bg_cell_no=3,bg_color='yellow', font_color='blue', text_value='26,260.00', msg='Step 13.1g:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=4,bg_color='yellow', font_color='blue', text_value='28,860.00', msg='Step 13.1h:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 36, font_color='gray8', text_value='50,630.00', msg='Step 13.1i:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 39, font_color='gray8', text_value='495,000.00', msg='Step 13.1j:')
        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'Define_1']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 13.2: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222803_Ds01.xlsx", 'Step 13.3: Verify report dataset ')
        
        """
        Step14: Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        """
        Step15: Verify Define field applied proper TL condition
        """
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222803_run_Ds01.xlsx" , 'Step 15: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 4,font_color='gray8', text_value='186,210.00', msg='Step 15.1a:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 4, font_color='gray8', text_value='149,400.00', msg='Step 15.1b:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 4, bg_color='yellow', font_color='blue', text_value='42,920.00', msg='Step 15.1c:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 4, bg_color='yellow', font_color='blue', text_value='46,310.00', msg='Step 15.1d:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 4, font_color='gray8', text_value='162,350.00', msg='Step 15.1e:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 7, 4, font_color='gray8', text_value='250,000.00', msg='Step 15.1f:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 4, bg_color='yellow', font_color='blue', text_value='26,260.00', msg='Step 15.1g:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 9, 4, bg_color='yellow', font_color='blue', text_value='28,860.00', msg='Step 15.1h:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 10, 4, font_color='gray8', text_value='50,630.00', msg='Step 15.1i:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 11, 4, font_color='gray8', text_value='495,000.00', msg='Step 15.1j:')

        """
        Step16: Click "IA" menu > "Save As" > "C2222802" > Click Save
        """
        self.driver.switch_to_default_content()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        
        """
        Step17: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """
        Step18: Reopen saved FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222802.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """
        Step19: Verify Preview
        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, font_color='gray8', text_value='186,210.00', msg='Step 19.1a:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, font_color='gray8', text_value='149,400.00', msg='Step 19.1b:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 14, bg_cell_no=1,bg_color='yellow', font_color='blue', text_value='42,920.00', msg='Step 19.1c:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=2,bg_color='yellow', font_color='blue', text_value='46,310.00', msg='Step 19.1d:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 22, font_color='gray8', text_value='162,350.00', msg='Step 19.1e:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 25, font_color='gray8', text_value='250,000.00', msg='Step 19.1f:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 29, bg_cell_no=3,bg_color='yellow', font_color='blue', text_value='26,260.00', msg='Step 19.1g:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=4,bg_color='yellow', font_color='blue', text_value='28,860.00', msg='Step 19.1h:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 36, font_color='gray8', text_value='50,630.00', msg='Step 19.1i:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 39, font_color='gray8', text_value='495,000.00', msg='Step 19.1j:')
        
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST','Define_1']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 19.2: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222803_Ds01.xlsx", 'Step 19.3: Verify report dataset ')
        
        """
        Step20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()