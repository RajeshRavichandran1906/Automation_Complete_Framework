'''
Created on 19-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222807
TestCase Name = Verify TL condition on a BY field, add a 'Report' Drilldown to condition, add Description
'''
import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling, ia_ribbon

class C2222807_TestClass(BaseTestCase):

    def test_C2222807(self):
        
        """
            Variable
        """
        Test_Case_ID = "C2222807"
        
        """
            Class & Objects
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
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 02: Verify Column titles ")
        time.sleep(2)
        
        
        """ 3. Right click on "COUNTRY" field from query pane            """
        """ 4. Select More -> Traffic Light Condition                    """
        metaobj.querytree_field_click("COUNTRY", 1, 1,'More','Traffic Light Conditions...')
        
        
        """ 5. Select the value dropdown arrow                     """
        """ 6. Click on Get Values drop down -> All                """
        """ 7. Select 'ENGLAND'                                    """
        """ 8. Click -> OK            """
        time.sleep(3)
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='All', value='ENGLAND')
        time.sleep(3)
        
        
        """ 9. Now click on Style tab Make changes - Bold, BG Color - yellow, Font color -PURPLE    """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, background_color='yellow', text_color='purple')
        time.sleep(2)
        
        
        """ 10. Click Drill Down button Now in TL window            """
        ia_stylingobj.traffic_light_toolbar_select('DrillDown', 1)
        time.sleep(2)
        
        
        """ 11. In Drill Down window, select the "Web page" option -> Type URL - http://www.yahoo.com             """
        """ 12. And change the "Description " as "Yahoo" from Drill Down 1                                        """
        """ 13. Click "OK"                                                                                        """
        ia_ribbonobj.create_drilldown_report("webpage", url_value="http://www.yahoo.com",set_description="Yahoo", click_ok=True)
        
        
        """ 14. In TL window click Apply then OK button            """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(5)
        
        
        """ 15. Verify the preview with applied TL condition            """
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, 'TableChart_1', coln_list, 'Step 15: Verify Column titles ')
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 3, 'C2222778_Ds01.xlsx', 'Step 15.1: Verify report data set on peview')
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bg_cell_no=1, bg_color='yellow', bold=True, font_color='purple', text_value='ENGLAND', msg='Step 15.2: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, font_color='gray8', text_value='FRANCE', msg='Step 15.3: ')
        
        """ 16. Click "IA" menu > "Save As" > "C2222807" > Click Save            """
        time.sleep(2)
        self.driver.switch_to_default_content()
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        time.sleep(2)
        
        
        """ 17. Click "Run"            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(12)
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222778_run_Ds01.xlsx" , 'Step 17: Verify report data set on run window')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, bg_color='yellow', font_color='purple', bold=True, text_value='ENGLAND', msg='Step 17.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 1, font_color='gray8', text_value='FRANCE', msg='Step 17.2:')
        
        
        """ 18. Click on "ENGLAND" value under COUNTRY and Hover over the ENGLAND and verify the description shows "Yahoo" as tooltip info        """
        time.sleep(2)
        ia_runobj.select_and_verify_drilldown_report_field("table[summary='Summary']", 2, 1, expected_drill_down_tooltip='Yahoo', msg='Step 18: ')
        time.sleep(15)
        
        
        """ 19. Verify output field applied proper TL condition and Drill Down works with description        """
        time.sleep(8)
        utillobj.switch_to_window(1)
        time.sleep(8)
        driver.maximize_window()
        time.sleep(5)
        owebpage=driver.title
        utillobj.asin("Yahoo", owebpage, "Step 19: Verify Yahoo page is displayed")
        self.driver.close()
        time.sleep(8)
        utillobj.switch_to_window(0)
        time.sleep(8)
        
        
        """ 20. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        utillobj.switch_to_default_content(pause=1)
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        
        """ 21. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222807.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("ia"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        
        """ 22. Verify Preview                    """
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, 'TableChart_1', coln_list, 'Step 22: Verify Column titles ')
        ia_resultobj.verify_report_data_set("TableChart_1", 10, 3, 'C2222778_Ds01.xlsx', 'Step 22.1: Verify report data set on peview')
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, bg_cell_no=1, bg_color='yellow', bold=True, font_color='purple', text_value='ENGLAND', msg='Step 22.2: ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, font_color='gray8', text_value='FRANCE', msg='Step 22.3: ')
        
        """ 23. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp            """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()