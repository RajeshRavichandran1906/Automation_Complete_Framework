'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2230842
TestCase Name = Test that Auto Drill works with Freeze option
'''
import unittest,time,pyautogui
from common.lib import utillity 
from common.pages import ia_run
from common.wftools.report import Report
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables

class C2230842_TestClass(BaseTestCase):
    
    def test_C2230842(self):
        
        """
        Class Objects
        """
        driver = self.driver
        report_ = Report(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        
        """
        Test case variable
        """
        browser_type=Global_variables.browser_name
        Test_ID="C2230842"
        Test_Case_ID = Test_ID+"_"+browser_type
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        report_.edit_fex_using_api_url("IA-Shell", folder_name= "P276/S9970")
        utillobj.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report_.report_long_timesleep)
        
        """    2. Click Format tab > Autodrill button     """
        time.sleep(15) # adding to properly click format
        self.driver.set_page_load_timeout(report_.report_long_timesleep)
        report_.select_ia_ribbon_item("Format", "auto_drill")
        
        """    3. Select Format > Freeze    """
        report_.select_ia_ribbon_item("Format", "freeze")
        
        """    4. Click RUN     """
        report_.run_report_from_toptoolbar()
        time.sleep(5)
        utillobj.wait_for_page_loads(report_.home_page_long_timesleep)
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        iframe_width=iframe.size['width']
        iframe_height=iframe.size['height']
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        freeze_table=driver.find_element_by_css_selector("#freezeTableName1 .scrollDiv")
        fr_hight=freeze_table.size['height']
        #iarun.create_table_data_set("#freezeTableName1 .scrollDiv table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("#freezeTableName1 .scrollDiv table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04.01: Verify dataset", desired_no_of_rows=15)
        
        """    5. Drag the horizontal scroll bar to right side and verify that shows vertical scroll bar at right side    """
        pyautogui.moveTo(x_fr + (iframe_width - 50), y_fr + (iframe_height-15) + 80)
        pyautogui.click(x_fr + (iframe_width - 50), y_fr + (iframe_height-15) + 80)
        time.sleep(3)
        before_Report_header_cell_top=driver.find_element_by_css_selector("#freeze > table[summary='Summary'] > tbody > tr:nth-child(2) > td:nth-child(4) > a").location['y']
        
        """    6. Drag the vertical scroll bar to the bottom and back to the top and verify the headings are frozen so only the report body will move.    """
        pyautogui.moveTo(x_fr + (iframe_width - 10), y_fr + (fr_hight-15) + 80)
        pyautogui.click(x_fr + (iframe_width - 10), y_fr + (fr_hight-15) + 80)
        time.sleep(3)
        after_Report_header_cell_top=driver.find_element_by_css_selector("#freeze > table[summary='Summary'] > tbody > tr:nth-child(2) > td:nth-child(4) > a").location['y']
        utillobj.asequal(before_Report_header_cell_top, after_Report_header_cell_top, "Step 06.01: verify that Report header row fixed")
        pyautogui.moveTo(x_fr + (iframe_width - 10), y_fr + 115 + 80)
        pyautogui.click(x_fr + (iframe_width - 10), y_fr + 115 + 80)
        time.sleep(3)
        
        """    7. Click on North America and select "Drill down to Store Business Sub Region".     """
        pyautogui.moveTo(x_fr + 50, y_fr + (iframe_height-15) + 80)
        pyautogui.click(x_fr + 50, y_fr + (iframe_height-15) + 80)
        time.sleep(3)
#         iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",11,1,'Drill down to Store Business Sub Region', "Step 12")
        report_.select_report_autolink_tooltip_runtime("table[summary='Summary']",11,1, 'Drill down to Store Business Sub Region')
        time.sleep(8)
        #iarun.create_table_data_set("#freezeTableName1 .scrollDiv table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("#freezeTableName1 .scrollDiv table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 07.01: Verify dataset drilldown displayed", desired_no_of_rows=15)
        time.sleep(3)
        
        """    8. Drag the horizontal scroll bar to right side and verify that shows vertical scroll bar at right side    """
        pyautogui.moveTo(x_fr + (iframe_width - 50), y_fr + (iframe_height-15) + 80)
        pyautogui.click(x_fr + (iframe_width - 50), y_fr + (iframe_height-15) + 80)
        time.sleep(3)
        before_Report_header_cell_top=driver.find_element_by_css_selector("#freeze > table[summary='Summary'] > tbody > tr:nth-child(2) > td:nth-child(4) > a").location['y']
        
        """    9. Drag the vertical scroll bar to the bottom and back to the top and verify the headings are frozen so only the report body will move.    """
        pyautogui.moveTo(x_fr + (iframe_width - 10), y_fr + (fr_hight-15) + 80)
        pyautogui.click(x_fr + (iframe_width - 10), y_fr + (fr_hight-15) + 80)
        time.sleep(3)
        after_Report_header_cell_top=driver.find_element_by_css_selector("#freeze > table[summary='Summary'] > tbody > tr:nth-child(2) > td:nth-child(4) > a").location['y']
        utillobj.asequal(before_Report_header_cell_top, after_Report_header_cell_top, "Step 09.01: verify that Report header row fixed")
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(3)
        
        """    10. Click IA > Save As> Type C2230842 > click Save    """
        report_.save_as_from_application_menu_item(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    11. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2230842.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report_.report_long_timesleep)

        """    12. Click on the Format tab. Verify that Auto Drill and Freeze are still selected.   """
        time.sleep(15) # adding to properly click format
        self.driver.set_page_load_timeout(report_.report_long_timesleep)
        report_.switch_ia_ribbon_tab('Format')
        utillobj.synchronize_with_visble_text('#FormatTab', 'Features', report_.report_short_timesleep)
        report_.verify_ribbon_item_is_enabled('format_auto_drill', '12.01')
        report_.verify_ribbon_item_is_enabled('format_freeze', '12.02')
         
        """    13. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()