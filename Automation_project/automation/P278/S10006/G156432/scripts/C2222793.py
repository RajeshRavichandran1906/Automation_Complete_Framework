'''
Created on 05-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222793
TestCase Name = Verify Traffic Light condition with various formats
'''
import unittest
import time
import os
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, active_miscelaneous, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class C2222793_TestClass(BaseTestCase):

    def test_C2222793(self):
        
        Test_Case_ID = "C2222793"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        act_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        ia_stylingobj = ia_styling.IA_Style(self.driver)
        browser=utillobj.parseinitfile('browser')
        
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
         
         
        """ 3. Click on COUNTRY field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 3: Verify Canvas column titles ")
        time.sleep(2)
        ia_resultobj.select_field_on_canvas("TableChart_1", 1)
          
          
        """ 4. Display tab expands -> Click on Traffic Lights        """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
          
          
        """ 5. Select dropdown arrow and choose "Equal to"                                        """
        """ 6. Select the other dropdown arrow and enter value = "ENGLAND" and click "Ok"         """
        time.sleep(2)
        ia_stylingobj.traffic_light_verify_condition_row(1, field_name='COUNTRY', relation_name='Equal to', Field_Value_txt=' ')
        time.sleep(2)
        ia_stylingobj.traffic_light_create_new(1, relation_name='Equal to', filter_type='Constant', value_box_input='ENGLAND')
          
          
        """ 7. Now click on Style tab Make changes Bold, Font size-12, Italics, Underline, Justification - center, Text Color - BLUE , BG Color - YELLOW    """
        time.sleep(2)
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, font_size='12', italic=True, underline=True, center_justify=True, text_color='blue', background_color='yellow')
        time.sleep(2)
          
          
        """ 8. Cick Apply then OK            """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        time.sleep(2)
        ia_stylingobj.traffic_light_close_dialog('Ok')
        time.sleep(2)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 8: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222778_Ds01.xlsx", 'Step 8.1: Verify report dataset ')
          
          
        """ 9. Click on Home tab and Change the report format to HTML       """
        ribbonobj.change_output_format_type('html')
          
          
        """ 10. Click "Run" and Verify the output in the mentioned formats For HTML, Verify that COUNTRY is having styling      """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222778_run_Ds01.xlsx" , 'Step 10: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 1, bg_color='yellow', bold=True, font_size='12pt', italic=True, underline=True, text_align='center', font_color='blue', text_value='ENGLAND', msg='Step 10:')
        driver.switch_to.default_content()
        time.sleep(2)
          
        """ 11. Click on Home tab and Change the report format to Active Report        """
        ribbonobj.change_output_format_type('active_report')
          
        """ 12. Click "Run" and Verify the output in the mentioned formats For Active Report, Verify that COUNTRY is having styling        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[id='ITableData0']", Test_Case_ID+"_run_Ds01.xlsx" , 'Step 12: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[id='ITableData0']", 2, 1, bg_color='yellow', bold=True, font_size='12pt', italic=True, underline=True, text_align='center', font_color='blue', text_value='ENGLAND', msg='Step 12.1:')
        act_misobj.verify_page_summary(0,'10of10records,Page1of1', 'Step 12.2: Verify Title')
        time.sleep(2)
        driver.switch_to.default_content()
          
          
        """ 13. Click on Home tab and Change the report format to PDF        """
        ribbonobj.change_output_format_type('pdf')
          
          
        """ 14. Click "Run" and Verify the output in the mentioned formats For PDF, Verify that COUNTRY is having styling       """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        elem1=(By.CSS_SELECTOR, "#resultArea")
        resultobj._validate_page(elem1)
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_step14'+'_'+ browser, image_type='actual',x=1, y=1, w=-1, h=-1)  
        
        
        """ 15. Click on Home tab and Change the report format to Excel formats        """
        ribbonobj.change_output_format_type('excel')
        
        """ 16. Click "Run" and Verify the output in the mentioned formats For Excel formats, Verify that COUNTRY is having styling        
                for Excel open the downloaded excel file and see the output        
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(7)
        os.system(os.getcwd()+"\\common\\lib\\Open_file.exe "+browser)
        time.sleep(15)
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_step16', image_type='actual', left=245, top=160, right=70, bottom=110)  
        time.sleep(2)
        utillobj.kill_process('excel')
        time.sleep(5)
        utillobj.switch_to_main_window()
        time.sleep(7)
        
        """ 17. Click on Home tab and Change the report format to PowerPoint       """
        time.sleep(2)
        driver.switch_to_default_content()
        time.sleep(3)
        ribbonobj.change_output_format_type('powerpoint')
        
        
        """ 18. Click "Run" and Verify the output in the mentioned formats For PowerPoint, Verify that COUNTRY is having styling        
                for PowerPoint, open the downloaded PowerPoint file and see the output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(7)
        os.system(os.getcwd()+"\\common\\lib\\Open_file.exe "+browser)
        time.sleep(15)
        utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_step18', image_type='actual', left=265, top=150, right=70, bottom=130)  
        time.sleep(2)
        utillobj.kill_process('POWERPNT')
        time.sleep(5)
        utillobj.switch_to_main_window()
        time.sleep(7)
        
        """ 19. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp     """
        time.sleep(2)
        driver.switch_to_default_content()
        time.sleep(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
        time.sleep(2)
         

if __name__ == '__main__':
    unittest.main()


