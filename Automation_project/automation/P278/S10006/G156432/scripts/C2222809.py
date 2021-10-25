'''
Created on 18-Jan-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222809
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222809_TestClass(BaseTestCase):

    def test_C2222809(self):
        
        Test_Case_ID = "C2222809"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        """ 
        Step01: Launch IA Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
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
        Step03: Right click on Report(car) under query pane and select to Print
        """
        metaobj.querytree_field_click("Report (car)", 1, 1, "Print")
        time.sleep(20)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step03.a: Verify Canvas column titles ")
        time.sleep(5)
        #ia_resultobj.create_report_data_set('TableChart_1', 18, 3, "C2222809_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 18, 3, "C2222809_Ds01.xlsx", 'Step03.b: Verify report data set on preview')
        
        """
        Step04: Click on DEALER_COST field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )
        """
        ia_resultobj.select_field_on_canvas("TableChart_1", 3)
        time.sleep(5)
        
        """
        Step05: Display tab expands -> Click on Traffic Lights
        """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(10)
        
        """
        Step06: Select the value dropdown arrow and enter value = "2626" and click "Ok"
        """
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant',value_box_input='2626')
        time.sleep(2)
        
        """
        Step07: Now click on Style tab Make some changes Bold, color - Purple rgb(128,0,128), Background color - Yellow (rgb(255,255,0))
        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, text_color='purple', background_color='yellow')
        time.sleep(2)
        
        """
        Step08: Click apply and "OK"
        """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step08(i): Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 18, 3, "C2222809_Ds01.xlsx", 'Step08(ii): Verify report data set on peview')
        
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, bg_cell_no=1, bg_color='yellow', font_color='purple', bold=True, text_value='7,427', msg='Step08.a:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, bg_cell_no=2, bg_color='yellow', font_color='purple', bold=True, text_value='11,194', msg='Step08.b:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, bg_cell_no=4, bg_color='yellow', font_color='purple', bold=True, text_value='4,292', msg='Step08.c:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 14, bg_cell_no=5, bg_color='yellow', font_color='purple', bold=True, text_value='4,631', msg='Step08.d:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=7, bg_color='yellow', font_color='purple', bold=True, text_value='5,660', msg='Step08.e:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, bg_cell_no=9, bg_color='yellow', font_color='purple', bold=True, text_value='25,000', msg='Step08.f:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, font_color='gray8', text_value='2,626', msg='Step08.g:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 29, bg_cell_no=11, bg_color='yellow', font_color='purple', bold=True, text_value='5,063', msg='Step08.h:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=13, bg_color='yellow', font_color='purple', bold=True, text_value='6,000', msg='Step08.i:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 35, bg_cell_no=16, bg_color='yellow', font_color='purple', bold=True, text_value='8,300', msg='Step08.j:')
        
        
        """
        Step09: Click "IA" menu > "Save As" > "C2222809" > Click Save
        """
        self.driver.switch_to_default_content()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
        
        """
        Step10: Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        
        """
        Step11: Verify the output applied proper TL condition
        """
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        #ia_runobj.create_table_data_set("table[summary='Summary']", "C2222809_Ds02.xlsx")
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222809_Ds02.xlsx" , 'Step 11: Verify report data set on run window')
        
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 3, bg_color='yellow', font_color='purple', bold=True, text_value='7,427', msg='Step11.a:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 3, bg_color='yellow', font_color='purple', bold=True, text_value='11,194', msg='Step11.b:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 3, bg_color='yellow', font_color='purple', bold=True, text_value='4,292', msg='Step11.c:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 3, bg_color='yellow', font_color='purple', bold=True, text_value='4,631', msg='Step11.d:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 3, bg_color='yellow', font_color='purple', bold=True, text_value='5,660', msg='Step11.e:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 10, 3, bg_color='yellow', font_color='purple', bold=True, text_value='25,000', msg='Step11.f:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 11, 3, font_color='gray8', text_value='2,626', msg='Step11.g:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 13, 3, bg_color='yellow', font_color='purple', bold=True, text_value='5,063', msg='Step11.h:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 15, 3, bg_color='yellow', font_color='purple', bold=True, text_value='6,000', msg='Step11.i:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 18, 3, bg_color='yellow', font_color='purple', bold=True, text_value='8,300', msg='Step11.j:')      
        
        """
        Step12: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        """
        Step13: Reopen saved FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222804.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        time.sleep(15)
        
        """
        Step14: Verify Preview
        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(5)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step14(i): Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 18, 3, "C2222809_Ds01.xlsx", 'Step14(ii): Verify report data set on peview')
        
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, bg_cell_no=1, bg_color='yellow', font_color='purple', bold=True, text_value='7,427', msg='Step 14.a:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, bg_cell_no=2, bg_color='yellow', font_color='purple', bold=True, text_value='11,194', msg='Step 14.b:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, bg_cell_no=4, bg_color='yellow', font_color='purple', bold=True, text_value='4,292', msg='Step 14.c:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 14, bg_cell_no=5, bg_color='yellow', font_color='purple', bold=True, text_value='4,631', msg='Step 14.d:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=7, bg_color='yellow', font_color='purple', bold=True, text_value='5,660', msg='Step 14.e:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, bg_cell_no=9, bg_color='yellow', font_color='purple', bold=True, text_value='25,000', msg='Step 14.f:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, font_color='gray8', text_value='2,626', msg='Step 14.g:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 29, bg_cell_no=11, bg_color='yellow', font_color='purple', bold=True, text_value='5,063', msg='Step 14.h:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 32, bg_cell_no=13, bg_color='yellow', font_color='purple', bold=True, text_value='6,000', msg='Step 14.i:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 35, bg_cell_no=16, bg_color='yellow', font_color='purple', bold=True, text_value='8,300', msg='Step 14.j:')
        
        
        """
        Step15: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()