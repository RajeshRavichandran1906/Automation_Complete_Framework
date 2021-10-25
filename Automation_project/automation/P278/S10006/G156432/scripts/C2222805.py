'''
Created on 18-Jan-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222805
'''
import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling, ia_ribbon

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

class C2222805_TestClass(BaseTestCase):

    def test_C2222805(self):
        
        """
            VARIABLES
        """
        Test_Case_ID = "C2222805"
        
        """
            CLASS & OBJECTS
        """
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        
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
        Step02: Double click COUNTRY, CAR, DEALER_COST, RETAIL_COST       
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('RETAIL_COST', 2, 1)
        time.sleep(4)
        
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 02.01: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222562_Ds01.xlsx", 'Step 02.02: Verify report data set on peview')
        
        """
        Step03: Right click on "DEALER_COST" field from query pane
        Step04: Select More -> Traffic Light Condition
        """
        metaobj.querytree_field_click("DEALER_COST", 1, 1,'More','Traffic Light Conditions...')
        time.sleep(20)
        
        """
        Step05: Click the condition dropdown arrow and select 'Less Than'
        Step06: Click on values dropdown menu and select Type: as 'Field'
        Step07: Select "RETAIL_COST" and Click "Ok"
        """
        ia_stylingobj.traffic_light_create_new(1, relation_name='Less than', filter_type='Field',value='RETAIL_COST')
        time.sleep(10)
        
        """
        Step08: Now click on Style tab Make some changes Bold, color - Purple rgb(128,0,128), Background color - Yellow (rgb(255,255,0))
        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, text_color='purple', background_color='yellow')
        time.sleep(2)
        
        """
        Step09: click Drill Down button Now in TL window
        """
        ia_stylingobj.traffic_light_toolbar_select('DrillDown', 1)
        time.sleep(15)
        
        """
        Step10: In Drill Down window, select the "Web page" option -> Type URL - http://www.yahoo.com and Click "OK
        Step11: In TL window click Apply then OK button
        """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.yahoo.com", set_description='Yahoo', click_ok='yes')
        time.sleep(3)
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(15)
        
        """
        Step12: Verify the preview with applied TL condition
        """
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, bg_cell_no=1, bg_color='yellow', font_color='purple', bold=True, text_value='18,621', msg='Step 12.01:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=3, bg_color='yellow', font_color='purple', bold=True, text_value='4,292', msg='Step 12.02:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, bg_cell_no=5, bg_color='yellow', font_color='purple', bold=True, text_value='16,235', msg='Step 12.03:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, bg_cell_no=6, bg_color='yellow', font_color='purple', bold=True, text_value='25,000', msg='Step 12.04:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 31, bg_cell_no=8, bg_color='yellow', font_color='purple', bold=True, text_value='2,886', msg='Step 12.05:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 38, bg_cell_no=10, bg_color='yellow', font_color='purple', bold=True, text_value='49,500', msg='Step 12.06:')
         
         
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step12(i): Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222562_Ds01.xlsx", 'Step12(ii): Verify report data set on peview')
         
        """
        Step13: Click "Run"
        Step14: Click on any underlined value under DEALER_COST and Hover over the underlined values and verify the description shows "Yahoo" as tooltip info
        Step15: Verify output applied proper TL condition and Drill Down works
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222562_run_Ds01.xlsx" , 'Step 13.01: Verify report data set on run window')
         
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 3, bg_color='yellow', font_color='purple', bold=True, text_value='18,621', msg='Step 13.02:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 3, bg_color='yellow', font_color='purple', bold=True, text_value='4,292', msg='Step 13.03:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 3, bg_color='yellow', font_color='purple', bold=True, text_value='16,235', msg='Step 13.04:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 7, 3, bg_color='yellow', font_color='purple', bold=True, text_value='25,000', msg='Step 13.05:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 9, 3, bg_color='yellow', font_color='purple', bold=True, text_value='2,886', msg='Step 13.06:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 11, 3, bg_color='yellow', font_color='purple', bold=True, text_value='49,500', msg='Step 13.07:')
        ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 3, expected_drill_down_tooltip='Yahoo', underline=True, msg="Step 15.01:")       
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
        driver.maximize_window()
        time.sleep(5)
        owebpage=driver.title
        utillobj.asin("Yahoo", owebpage, "Step 15.02: Verify Yahoo page is displayed")
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        driver.maximize_window()
        time.sleep(5)
        
        """
        Step16: Click "IA" menu > "Save As" > "C2222809" > Click Save
        """
        utillobj.switch_to_default_content(pause=2)
        parent_css="#applicationMenu div[id='optionsSaveAsBtn']"
        resultobj.wait_for_property(parent_css, 1)
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
        http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222805.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("se_"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        time.sleep(15)
        
        """
        Step19: Verify Preview
        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(5)
        parent_css="#TableChart_1 [id^='ActivePreviewItem']"
        resultobj.wait_for_property(parent_css, 8)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST', 'RETAIL_COST']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 19.01: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 4, "C2222562_Ds01.xlsx", 'Step 19.02: Verify report data set on peview')
        ia_resultobj.verify_report_cell_property("TableChart_1", 7, bg_cell_no=1, bg_color='yellow', font_color='purple', bold=True, text_value='18,621', msg='Step 19.03:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=3, bg_color='yellow', font_color='purple', bold=True, text_value='4,292', msg='Step 19.04:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, bg_cell_no=5, bg_color='yellow', font_color='purple', bold=True, text_value='16,235', msg='Step 19.05:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, bg_cell_no=6, bg_color='yellow', font_color='purple', bold=True, text_value='25,000', msg='Step 19.06:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 31, bg_cell_no=8, bg_color='yellow', font_color='purple', bold=True, text_value='2,886', msg='Step 19.07:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 38, bg_cell_no=10, bg_color='yellow', font_color='purple', bold=True, text_value='49,500', msg='Step 19.08:')
                
        """
        Step20: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(2)
                
if __name__ == '__main__':
    unittest.main()