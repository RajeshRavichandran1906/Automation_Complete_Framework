'''
Created on 19-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222808
TestCase Name = Verify Traffic Lights on a Define based on another BY field
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling,\
    ia_ribbon
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222808_TestClass(BaseTestCase):

    def test_C2222808(self):
        
        Test_Case_ID = "C2222808"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
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
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 02: Verify Column titles ")
        time.sleep(2)
        
        
        """
        Step03: Right click on "COUNTRY" field from query pane
        Step04: Select More -> Traffic Light Condition
        """
        metaobj.querytree_field_click("COUNTRY", 1, 1,'More','Traffic Light Conditions...')
        
        
        """
        Step05: Select the value dropdown arrow
        Step06: Click on Get Values drop down -> All
        Step07: Select 'ENGLAND'
        Step08: Click "OK"
        """
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='All', value='ENGLAND')
        
        """
        Step09: Now click on Style tab Make changes - Bold, BG Color - yellow, Font color -GREEN
        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, background_color='yellow', text_color='green')
        time.sleep(2)
        
        """
        Step10: Click Drill Down button Now in TL window
        """
        ia_stylingobj.traffic_light_toolbar_select('DrillDown', 1)
        time.sleep(1)
        
        """
        Step11: In Drill Down window, select the "Web page" option -> Type URL - http://www.aol.com
        Step12: And change the "Description " as "AOL" from Drill Down 1
        Step13: Click "OK"
        """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.aol.com",set_description="AOL", click_ok=True)
        
        """
        Step14: In TL window click Apply then OK button
        """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(5)
        
        """
        Step15: Click on Traffic Lights from data pane to edit the previously created TL with Drill Down
        """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(1)
        
        """
        Step16: Click on "Drill Down" in TL window
        """
        ia_stylingobj.traffic_light_toolbar_select('DrillDown', 1)
        time.sleep(1)
        
        """
        Step17: Select Target from 'New Window' to 'Same Window', Click "OK"
        """
        ia_ribbonobj.create_drilldown_report("webpage",set_target='Same Window',click_ok='yes')
        time.sleep(1)
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        
        """ Verify Styling applied in Preview"""
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, 'TableChart_1', coln_list, 'Step 17: Verify Column titles ')
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 3, 'C2222778_Ds01.xlsx', 'Step 17.1: Verify report data set on peview')
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bg_cell_no=1, bg_color='yellow', bold=True, font_color='green', text_value='ENGLAND', msg='Step 17.2: ')
        
        """
        Step18: Click "Run"
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222778_run_Ds01.xlsx" , 'Step 18: Verify report data set on run window')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, bg_color='yellow', font_color='green', bold=True, text_value='ENGLAND', msg='Step 18.1:')
        
        
        """
        Step19: Click on "ENGLAND" value under COUNTRY and Hover over the ENGLAND and verify the description shows "AOL" as tooltip info
        """
        ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 1, expected_drill_down_tooltip='AOL', msg='Step 19: ')
        time.sleep(30)
        
        
        """ 20. Verify output field applied proper TL condition and Drill Down works with Description and web page opens inside the same tool output window    """
        
        
        elem=(By.CSS_SELECTOR,"[id='m-side-nav__header'] a img")
        resultobj._validate_page(elem)
        alternate_text=driver.find_element_by_css_selector("[id='m-side-nav__header'] a img").get_attribute('alt')
        utillobj.asequal('AOL logo',alternate_text,'Step 19: Web page opens inside the same tool output window')
        time.sleep(5)
                 
         
        """ 21. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp     """
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        time.sleep(2)
        

if __name__ == '__main__':
    unittest.main()
    