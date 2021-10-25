'''
Created on Dec 7, 2017

@author: BM13368
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227574
TestCase Name : Verify report with TOC (Table of Contents)
'''
import unittest, time, pyautogui, re
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By


class C2227574_TestClass(BaseTestCase):

    def test_C2227574(self):
        
        Test_Case_ID = "C2227574"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
            Step 01:Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/CAR&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/car','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        """
            Step 02:Double click "COUNTRY", "CAR", "DEALER_COST", "RETAIL_COST".
        """
        metaobj.datatree_field_click("COUNTRY", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CAR", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click('DEALER_COST', 2, 1)
        time.sleep(4)
        """ 
            Step 03:Verify the following report is displayed.
        """
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        coln_list = ['COUNTRY', 'CAR', 'DEALER_COST']
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 03:01: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step 03:02: Verify report dataset in live preview', no_of_cells=4)
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
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)    
         
        """ 
            Step 13:Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
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
        ia_resultobj.verify_report_data_set('TableChart_1', 10, 3, Test_Case_ID+"_Ds01.xlsx", 'Step15:01: Verify report dataset in live preview', no_of_cells=4)
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