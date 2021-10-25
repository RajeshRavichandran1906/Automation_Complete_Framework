'''
Created on 27-Dec-2016

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222778
TestCase Name = Verify conditional styling using EQUAL-TO statement save and reopen
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222778_TestClass(BaseTestCase):

    def test_C2222778(self):
        
        Test_Case_ID = "C2222778"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        
        
        """ 1.Launch IA Report mode: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006  """
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
#         
        
        """ 3. Click on COUNTRY field > Display button from Field tab (If display group not expanded in Field tab )        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        ia_resultobj.select_field_on_canvas("TableChart_1", 1)
        
        
        """ 4. Display tab expands -> Click on Traffic Lights -> change condition to NOT EQUAL TO            """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        
        
        """ 5. Click on drop down button next to Not Equal to drop down > Type in the Value: ENGLAND        """
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, relation_name='Not equal to', filter_type='Constant', value_box_input='ENGLAND')
        
        
        """ 6. Click on Style tab Make some changes Bold, Italic, Font color - RED, Background color - Yellow (rgb(255,255,0))        """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, italic=True, text_color='red', background_color='yellow')
        time.sleep(2)
        
        
        """ 7. Cick Apply then OK                    """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 7.1: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 7.2: Verify report dataset ')
        
        
        """ 8. Verify conditional styling on all Country values except ENGLAND            """
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, font_color='gray8', text_value='ENGLAND', msg='Step 8:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, bg_cell_no=1,bg_color='yellow', font_color='red', text_value='FRANCE', bold=True, italic=True, msg='Step 8.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 14, bg_cell_no=2,bg_color='yellow', font_color='red', text_value='ITALY', bold=True, italic=True, msg='Step 8.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bg_cell_no=4,bg_color='yellow', font_color='red', text_value='JAPAN', bold=True, italic=True, msg='Step 8.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, bg_cell_no=6,bg_color='yellow', font_color='red', text_value='W GERMANY', bold=True, italic=True, msg='Step 8.4:')
        
        
        """ 9. Click "Run" and Verify the traffic light condition is applied        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 9: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, font_color='gray8', text_value='ENGLAND', msg='Step 9.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 1, bg_color='yellow', font_color='red', text_value='FRANCE', bold=True, italic=True, msg='Step 9.2:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 1, bg_color='yellow', font_color='red', text_value='ITALY', bold=True, italic=True, msg='Step 9.3:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 1, bg_color='yellow', font_color='red', text_value='JAPAN',bold=True, italic=True,  msg='Step 9.4:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 10, 1, bg_color='yellow', font_color='red', text_value='W GERMANY', bold=True, italic=True, msg='Step 9.5:')
        
        
        """ 10. Click Save in the toolbar > Save As C2222778 > click Save        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        
        
        """ 11. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp            """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        
        
        """ 12. Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222778.fex&tool=Report    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        
        """ 13. Verify the following report is displayed        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 13: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 13.1: Verify report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 4, font_color='gray8', text_value='ENGLAND', msg='Step 13.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 11, bg_cell_no=1,bg_color='yellow', font_color='red', text_value='FRANCE', bold=True, italic=True, msg='Step 13.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 14, bg_cell_no=2,bg_color='yellow', font_color='red', text_value='ITALY', bold=True, italic=True, msg='Step 13.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 19, bg_cell_no=4,bg_color='yellow', font_color='red', text_value='JAPAN', bold=True, italic=True, msg='Step 13.5:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 24, bg_cell_no=6,bg_color='yellow', font_color='red', text_value='W GERMANY', bold=True, italic=True, msg='Step 13.6:')
        
        
        """ 14. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)  


if __name__ == '__main__':
    unittest.main()