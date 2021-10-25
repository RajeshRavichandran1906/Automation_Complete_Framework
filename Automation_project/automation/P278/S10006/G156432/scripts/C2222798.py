'''
Created on 17-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222798
TestCase Name = Verify TL condition on a joined field
'''
import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_styling, \
                         ia_ribbon, ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222798_TestClass(BaseTestCase):

    def test_C2222798(self):
        
        Test_Case_ID = "C2222798"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_ribbonobj = ia_ribbon.IA_Ribbon(self.driver)
        
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/empdata&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 2. Click Data tab -> Join                                                 """
        """ 3. Select "Add new" in Join window And "Training.mas" and Click "open" Verify the link between PIN from empdata to PIN from training    """
        """ 4. Click "Ok" to Join window        """
        ia_ribbonobj.create_join('ibisamp', 'training')
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 4: Verify join created successfully")
        driver.find_element_by_css_selector("#dlgJoin_btnOK img").click()
        time.sleep(5)
        
        
        """ 5. Double click LASTNAME, FIRSTNAME, EXPENSES            """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("FIRSTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('EXPENSES', 2, 1)
        time.sleep(4)
        
        
        """ 6. Click on EXPENSES field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )    """
        metaobj.querytree_field_click('EXPENSES', 1)
        time.sleep(5)
        
        
        """ 7. Display tab expands -> Click on Traffic Lights            """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
        time.sleep(3)
        
        
        """ 8. Select dropdown arrow and choose "Greater than"                            """
        """ 9. Select the other dropdown arrow and enter value = "3000" and click "Ok"    """
        ia_stylingobj.traffic_light_create_new(1, relation_name='Greater than',filter_type='Constant',value_box_input='3000')
        time.sleep(2)
        
        
        """ 10. Now click on Style tab Make changes Bold, Italic, Font size-12, Font color - Green, Justification - center, Background color - Yellow (rgb(255,255,0))    """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, italic=True, font_size='12', text_color='green', background_color='yellow')
        time.sleep(2)
        
        
        """ 11. Click Apply then OK and Verify the preview applied with TL condition        """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['LASTNAME', 'FIRSTNAME', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 11: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 41, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 11.1: Verify report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 12, bg_cell_no=3, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='green', text_value='3,100.00', msg='Step 11.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, font_size='9pt', font_color='gray8', text_value='2,600.00', msg='Step 11.3:')
         
        
        """ 12. Click "Run"            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        
        
        """ 13. Verify that TL condition applied on Joined field        """
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222801_run_Ds01.xlsx" , 'Step 13: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 3, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='green', text_value='3,100.00', msg='Step 13.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 3, font_size='9pt', font_color='gray8', text_value='2,600.00', msg='Step 13.2:')
        
        
        """ 14. Click "IA" menu > "Save As" > "C2222798" > Click Save        """
        self.driver.switch_to_default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        
        
        """ 15. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        
        """ 16. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222798.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        time.sleep(2)
        utillobj.infoassist_api_edit("ia"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        
        """ 17. Verify Preview            """
        coln_list = ['LASTNAME', 'FIRSTNAME', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 17: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 41, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 17.1: Verify report dataset ')
        ia_resultobj.verify_report_cell_property("TableChart_1", 12, bg_cell_no=3, bg_color='yellow', bold=True, italic=True, font_size='12pt', font_color='green', text_value='3,100.00', msg='Step 17.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, font_size='9pt', font_color='gray8', text_value='2,600.00', msg='Step 17.3:')
        
        
        """ 18. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp        """
        time.sleep(2)
        
if __name__ == '__main__':
    unittest.main()
    
