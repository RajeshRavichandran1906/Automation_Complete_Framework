'''
Created on 5-Jan-2017

@author: Kiruthika

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222801
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling,\
    define_compute, ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222801_TestClass(BaseTestCase):

    def test_C2222801(self):
        
        Test_Case_ID = "C2222801"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        def_comp = define_compute.Define_Compute(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        
        """ 
        Step01: Launch IA Report mode:
        http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/empdata&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 
        Step02: Click Data tab -> Join  
        Step03: Select "Add new" in Join window And "Training.mas" and Click "open"
        Verify the link between PIN from empdata to PIN from training     
        """
        ia_ribbonobj.create_join('ibisamp', 'training')
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 03a: Verify join created successfully")
        driver.find_element_by_css_selector("#dlgJoin_btnOK img").click()
        time.sleep(5)
        
        """
        Step05: Double click LASTNAME, FIRSTNAME, EXPENSES
        """ 
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("FIRSTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('EXPENSES', 2, 1)
        time.sleep(4)
        
        """
        Step06: Click on EXPENSES field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )
        Step07: Display tab expands -> Click on Traffic Lights
        """
        metaobj.querytree_field_click('EXPENSES', 1)
        time.sleep(5)
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        """
        Step08: Select dropdown arrow and choose 'Greater than or equal to'
        Step09: Select the other dropdown arrow and enter value = "1900" and click "Ok"
        """
        ia_stylingobj.traffic_light_create_new(1, relation_name='Greater than or equal to',filter_type='Constant',value_box_input='1900')
        time.sleep(2)
        
        """
        Step10: Now click on Style tab Make changes Bold, BG color - Yellow, Font color - RED"
        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, text_color='red', background_color='yellow')
        time.sleep(2)
       
        """
        Step11: Click Apply then OK to Traffic Light window
        """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        
        """
        Step12: Verify the preview with applied TL conditions
        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, bg_cell_no=1,bg_color='yellow',font_color='red', text_value='3,400.00', msg='Step 12.1a:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, bg_cell_no=2,bg_color='yellow',font_color='red', text_value='3,300.00', msg='Step 12.1b:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 12, bg_cell_no=3,bg_color='yellow', font_color='red', text_value='3,100.00', msg='Step 12.1c:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 15, font_color='gray8', text_value='.', msg='Step 12.1d:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=4,bg_color='yellow', font_color='red', text_value='2,600.00', msg='Step 12.1e:')
         
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['LASTNAME', 'FIRSTNAME', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 12.2: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 41, 3, "C2222801_Ds01.xlsx", 'Step 12.3: Verify report dataset ')
         
        """
        Step13: Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
         
        """
        Step14: Verify Define field applied proper TL condition
        """
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222801_run_Ds01.xlsx" , 'Step 14: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 3,bg_color='yellow', font_color='red', text_value='3,400.00', msg='Step 14.1a:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 3,bg_color='yellow', font_color='red', text_value='3,300.00', msg='Step 14.1b:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 3, bg_color='yellow', font_color='red', text_value='3,100.00', msg='Step 14.1c:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 3, font_color='gray8', text_value='.', msg='Step 14.1d:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 3,bg_color='yellow', font_color='red', text_value='2,600.00', msg='Step 14.1e:')
        
        """
        Step15: Click "IA" menu > "Save As" > "C2222801" > Click Save
        """
        self.driver.switch_to_default_content()
        elem1=(By.CSS_SELECTOR, "#applicationButton img")
        resultobj._validate_page(elem1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("se_"+Test_Case_ID)
         
        """
        Step16: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
         
        """
        Step17: Reopen saved FEX:
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222801.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
         
        """
        Step18: Verify Preview
        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, bg_cell_no=1,bg_color='yellow',font_color='red', text_value='3,400.00', msg='Step 18.1a:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 9, bg_cell_no=2,bg_color='yellow',font_color='red', text_value='3,300.00', msg='Step 18.1b:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 12, bg_cell_no=3,bg_color='yellow', font_color='red', text_value='3,100.00', msg='Step 18.1c:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 15, font_color='gray8', text_value='.', msg='Step 18.1d:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=4,bg_color='yellow', font_color='red', text_value='2,600.00', msg='Step 18.1e:')
         
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['LASTNAME', 'FIRSTNAME', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 18.2: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 41, 3, "C2222801_Ds01.xlsx", 'Step 18.3: Verify report dataset ')
         
        """
        Step19: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
        
        
if __name__ == '__main__':
    unittest.main()