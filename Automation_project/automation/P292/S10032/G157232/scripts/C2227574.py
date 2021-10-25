'''
Created on Dec 7, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227574
TestCase Name : Verify report with TOC (Table of Contents)
'''
import unittest, time, pyautogui, re
from common.lib import utillity
from common.pages import visualization_resultarea, visualization_ribbon,  ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.wftools.report import Report
from common.lib import global_variables


class C2227574_TestClass(BaseTestCase):

    def test_C2227574(self):
        
        Test_Case_ID = "C2227574"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        report = Report(self.driver)
        global_var_obj = global_variables.Global_variables()
        
        """
            TESTCASE CSS
        """
        case_id = global_var_obj.current_test_case
        qwerty_tree_css = "#queryTreeWindow"
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        
        """
            Step 01:Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        """
            Step 02:Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".
        """
        report.double_click_on_datetree_item("COUNTRY", 1)
        report.wait_for_visible_text(qwerty_tree_css, "COUNTRY")
        
        report.double_click_on_datetree_item("CAR", 1)
        report.wait_for_visible_text(qwerty_tree_css, "CAR")
        
        report.double_click_on_datetree_item("DEALER_COST", 1)
        report.wait_for_visible_text(qwerty_tree_css, "DEALER_COST")
        
        report.double_click_on_datetree_item("RETAIL_COST", 1)
        report.wait_for_visible_text(qwerty_tree_css, "RETAIL_COST")
        
        """ 
            Step 03:Verify the following report is displayed.
        """
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03:01: Verify Canvas column titles")
        #report.create_report_data_set_in_preview('TableChart_1', 10, 4, DATA_SET_NAME1)
        report.verify_report_data_set_in_preview("TableChart_1", 10, 4, DATA_SET_NAME1, "Step 03:02 : Verify the following report is displayed.")
        
        """ 
            Step 04:Select "Format" > Click on "Table of Contents" button (Navigation Group).
        """
        ribbonobj.select_ribbon_item('Format', 'table_of_contents')     
        
        """ 
            Step 05:Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        iframe=driver.find_element_by_css_selector("iframe[id^='ReportIframe-']")
        x_fr=iframe.location['x']
        y_fr=iframe.location['y']
        utillobj.switch_to_frame(pause=2)
         
        """ 
            Step 06:Verify the report is displayed along with the "Table of Contents" button.
        """
        ia_runobj.verify_table_data_set("table[id='IBI_Page0'][summary= 'Summary']", Test_Case_ID+"run_Ds01.xlsx", "Step 06:02: Verify report data in runtime")
        toc_btn=driver.find_element_by_css_selector("#divtocDHTMLDummy > img").is_displayed()
        utillobj.asequal(toc_btn, True, "Step 06:03: Verify TOC is displayed at runtime")
         
        """ 
            Step 07:Double click "Table of Contents" button (top left corner).
        """
        toc_btn=driver.find_element_by_css_selector("#divtocDHTMLDummy > img")
        utillobj.click_on_screen(toc_btn, 'middle', 2)   
        
        """ 
            Step 08:Verify "Table of Contents" menu opens.
        """
        toc_items=['Table of Contents', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY', 'View Entire Report (On/Off)', 'Remove Table of Contents']
        ia_runobj.verify_toc_item(toc_items, "Step 08:01: Verify TOC list of fields")
         
        """ 
            Step 09:Re-position the "Table of Contents" menu.
        """
        toc_tree=driver.find_element_by_css_selector("#divtocDHTML #move")
        x_toc=toc_tree.location['x']
        y_toc=toc_tree.location['y']
        w_toc=toc_tree.size['width']
        pyautogui.moveTo(x_toc + x_fr + (w_toc/2), y_toc + y_fr + 75)
        time.sleep(2)
        pyautogui.dragTo(x_fr+300,y_fr+150)
        time.sleep(2)
        toc_tree_after_move_x=toc_tree.location['x']
        if toc_tree_after_move_x > 150:
            utillobj.asequal(True, True, "Step 09:01: Verify Re-position of TOC")   
         
        """ 
            Step 10:Click "IA" > "Save".
            Step 11:Enter Title = "C2227574".
            Step 12:Click "Save".
        """
        utillobj.switch_to_default_content(3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        report.wait_for_visible_text("#IbfsOpenFileDialog7_btnOK", "Save")
        
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)    
         
        """ 
            Step 13:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """ 
            Step 14:Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227574.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)        
        """ 
            Step 15:Select Format Tab > Verify "Table of Contents" remains toggled ON
        """
        #report.create_report_data_set_in_preview('TableChart_1', 10, 4, DATA_SET_NAME1)
        report.verify_report_data_set_in_preview("TableChart_1", 10, 4, DATA_SET_NAME1, "Step 15:Select Format Tab > Verify 'Table of Contents' remains toggled ON")
        ribbonobj.switch_ia_tab("Format")
        time.sleep(8)
        toc_btn=driver.find_element_by_css_selector("#FormatReportToc")
        status=True if bool(re.match('.*-checked.*', toc_btn.get_attribute("class"))) else False
        utillobj.asequal(True, status, "Step 15:02: Verify toc button is selected.")
        
        """ 
            Step 16:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__ == "__main__":
    unittest.main()