'''
Created on 04-Jan-2017

@author: Aftab

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2222788
TestCase Name = Veirfy conditional styling with option From File - Flat file
'''
import unittest
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run, ia_styling
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from common.lib.uiauto import FileDialog
import uiautomation as automation
import time, pyautogui
from common.lib.core_utility import CoreUtillityMethods
from common.lib.global_variables import Global_variables

class C2222788_TestClass(BaseTestCase):

    def test_C2222788(self):
        
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
        
        """
            Variables 
        """
        Test_Case_ID = "C2222788"
        canvas_css = "#TableChart_1"
        trafficLights_css = "[id*='trafficLightsDlg']"
        text_file = os.path.join(os.getcwd(), "data", "Flat_file.txt")
        text_file_path = os.getcwd() + "\data\\" + "Flat_file.txt"
        
        
        """ 1. Launch IA Report mode:
               http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10006
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P278/S10006', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, canvas_css)
        resultobj._validate_page(elem1)
        utillobj.wait_for_page_loads(50)
        
        """ 2. Double click COUNTRY, CAR, DEALER_COST            """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        utillobj.synchronize_with_visble_text(canvas_css, 'COUNTRY', metaobj.home_page_medium_timesleep)
        metaobj.datatree_field_click("CAR", 2, 1)
        utillobj.synchronize_with_visble_text(canvas_css, 'CAR', metaobj.home_page_medium_timesleep)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        utillobj.synchronize_with_visble_text(canvas_css, 'DEALER_COST', metaobj.home_page_medium_timesleep)
        
        
        """ 3. Click on DEALER_COST field in Canvas, then Display button from Field tab (If display group not expanded in Field tab )        """
        elem1=(By.CSS_SELECTOR, canvas_css)
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 3: Verify Canvas column titles ")
        ia_resultobj.select_field_on_canvas("TableChart_1", 3)
                
        """ 4. Display tab expands -> Click on Traffic Lights            """
        ribbonobj.select_ribbon_item('Field', 'trafficlights')
                
        """ 5. Click on the dropdown menu to add values                                                    """
        """ 6. Now click on the ""Get Values"" menu And Select ""From File"" from the dropdown menu        """
        """ 7. Opens the "Select From File..." window                                                      """
        """ 8. Select File Format : "" Flat file or csv ""            """
        """ 9. Browse for Flat file (attached Flat file.txt), Click "Ok" and Values displays and select the value "4444"    """
        utillobj.synchronize_with_visble_text(trafficLights_css, 'DEALER_COST', metaobj.home_page_medium_timesleep)
        ia_stylingobj.traffic_light_verify_condition_row(1, field_name='DEALER_COST', relation_name='Greater than', Field_Value_txt='0')
        ia_stylingobj.traffic_light_create_new(1, filter_type='Constant', getvalue_params='From File', flat_file=text_file)
        if Global_variables.browser_name == 'chrome':
            uploadWindow = automation.WindowControl(RegexName="File Upload.*")
            uploadWindow.SetFocus()
            time.sleep(2)
            uploadWindow.EditControl(RegexName="File name.*").Click()
            time.sleep(2)
            pyautogui.hotkey('ctrl','a')
            time.sleep(2)
            pyautogui.hotkey('del')
            time.sleep(2)
    #             automation.EditControl(RegexName="File name.*").SendKeys(os.getcwd() + "\data\\" + filename)
             
            pyautogui.typewrite(text_file_path)
            time.sleep(2)
            uploadWindow.ButtonControl(Name="Open").Click()

        else:
            FileDialog().open_file()
        #         automation.ButtonControl(Name="Open").Click(10, 10, False, 10)

        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "[id^='IBIDialog'] iframe[class*='iframe-focus']")))
        self.driver.find_element_by_css_selector("form table tr td input[id='okBtn']").click()              
        self.driver.switch_to_default_content()
        input_val = self.driver.find_element_by_css_selector("#id_wv_text_value")
        input_val.clear()
        time.sleep(3)
        input_val.send_keys('4444')
        ok_button = self.driver.find_element_by_css_selector("div#wndWhereValuePopup div#wndWhereValuePopup_btnOK")
        CoreUtillityMethods.python_left_click('self', ok_button)
        
        
        """ 10. Now click on Style tab Make some changes Bold, Italic, Font color - Purple rgb(128,0,128), Background color - Yellow (rgb(255,255,0))        """
        ia_stylingobj.traffic_light_toolbar_select('Style', 1, bold=True, italic=True, text_color='purple', background_color='yellow')
        
                
        """ 11. Click Apply then OK            """
        ia_stylingobj.traffic_light_close_dialog('Apply')
        ia_stylingobj.traffic_light_close_dialog('Ok')
        utillobj.synchronize_until_element_disappear(trafficLights_css, metaobj.home_page_medium_timesleep)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 11: Verify Canvas column titles ")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, "C2222778_Ds01.xlsx", 'Step 11.1: Verify report dataset ')
        
        
        """ 12. Notice that conditional styling is applied            """
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, bg_cell_no=1, bg_color='yellow', font_color='purple', text_value='18,621', bold=True, italic=True, msg='Step 12.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, bg_cell_no=2, bg_color='yellow', font_color='purple', text_value='14,940', bold=True, italic=True, msg='Step 12.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 10, font_color='gray8', text_value='4,292', msg='Step 12.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=3, bg_color='yellow', font_color='purple', text_value='4,631', bold=True, italic=True, msg='Step 12.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 16, bg_cell_no=4, bg_color='yellow', font_color='purple', text_value='16,235', bold=True, italic=True, msg='Step 12.5:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=5, bg_color='yellow', font_color='purple', text_value='25,000', bold=True, italic=True, msg='Step 12.6:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, font_color='gray8', text_value='2,626', msg='Step 12.7:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 23, font_color='gray8', text_value='2,886', msg='Step 12.8:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 26, bg_cell_no=6, bg_color='yellow', font_color='purple', text_value='5,063', bold=True, italic=True, msg='Step 12.9:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=7, bg_color='yellow', font_color='purple', text_value='49,500', bold=True, italic=True, msg='Step 12.10:')
        
        
        """ 13. Click "IA" > "Save" > Save As "C2222788" > Click Save            """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("ia"+Test_Case_ID)
                
        """ 14. Click "Run" and Verify the traffic light condition is applied            """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        WebDriverWait(self.driver, 50).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2222778_run_Ds01.xlsx" , 'Step 14: Verify report dataset')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 2, 3, bg_color='yellow', font_color='purple', text_value='18,621', bold=True, italic=True, msg='Step 14.1:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 3, 3, bg_color='yellow', font_color='purple', text_value='14,940', bold=True, italic=True, msg='Step 14.2:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 4, 3, font_color='gray8', text_value='4,292', msg='Step 14.3:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 5, 3, bg_color='yellow', font_color='purple', text_value='4,631', bold=True, italic=True, msg='Step 14.4:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 6, 3, bg_color='yellow', font_color='purple', text_value='16,235', bold=True, italic=True, msg='Step 14.5:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 7, 3, bg_color='yellow', font_color='purple', text_value='25,000', bold=True, italic=True, msg='Step 14.6:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 8, 3, font_color='gray8', text_value='2,626', msg='Step 14.7:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 9, 3, font_color='gray8', text_value='2,886', msg='Step 14.8:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 10, 3, bg_color='yellow', font_color='purple', text_value='5,063', bold=True, italic=True, msg='Step 14.9:')
        ia_runobj.verify_table_cell_property("table[summary='Summary']", 11, 3, bg_color='yellow', font_color='purple', text_value='49,500', bold=True, italic=True, msg='Step 14.10:')
        
        
        """ 15. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp            """
        driver.switch_to.default_content()
        utillobj.infoassist_api_logout()
        
        
        """ 16. Reopen saved FEX:
                http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2222788.fex&tool=Report
        """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.infoassist_api_edit("ia"+Test_Case_ID, 'report', 'S10006', mrid='mrid', mrpass='mrpass')
        
        """ 17. Verify the following report is displayed                        """
        elem1=(By.CSS_SELECTOR, canvas_css)
        resultobj._validate_page(elem1)
        ia_resultobj.verify_report_cell_property("TableChart_1", 6, bg_cell_no=1, bg_color='yellow', font_color='purple', text_value='18,621', bold=True, italic=True, msg='Step 17.1:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 8, bg_cell_no=2, bg_color='yellow', font_color='purple', text_value='14,940', bold=True, italic=True, msg='Step 17.2:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 10, font_color='gray8', text_value='4,292', msg='Step 17.3:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 13, bg_cell_no=3, bg_color='yellow', font_color='purple', text_value='4,631', bold=True, italic=True, msg='Step 17.4:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 16, bg_cell_no=4, bg_color='yellow', font_color='purple', text_value='16,235', bold=True, italic=True, msg='Step 17.5:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 18, bg_cell_no=5, bg_color='yellow', font_color='purple', text_value='25,000', bold=True, italic=True, msg='Step 17.6:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 21, font_color='gray8', text_value='2,626', msg='Step 17.7:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 23, font_color='gray8', text_value='2,886', msg='Step 17.8:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 26, bg_cell_no=6, bg_color='yellow', font_color='purple', text_value='5,063', bold=True, italic=True, msg='Step 17.9:')
        ia_resultobj.verify_report_cell_property("TableChart_1", 28, bg_cell_no=7, bg_color='yellow', font_color='purple', text_value='49,500', bold=True, italic=True, msg='Step 17.10:')

        """ 18. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp             """

if __name__ == '__main__':
    unittest.main()