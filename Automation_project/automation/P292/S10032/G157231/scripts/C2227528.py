'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227528
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity
from selenium.webdriver.common.by import By

class C2227528_TestClass(BaseTestCase):

    def test_C2227528(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2227528'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        browser=utillobj.parseinitfile('browser')
        
        """ Step 01: Launch IA Report mode:- http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/EMPLOYEE&item=IBFS%3A%2FWFC%2FRepository%2FS10032 """
        utillobj.infoassist_api_login('report','ibisamp/employee','P292/S10032', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        
        """ Step 02 : Double click "EMP_ID", "LAST_NAME", "CURR_SAL", "SALARY". """
        metaobj.datatree_field_click("EMP_ID", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("LAST_NAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("CURR_SAL", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SALARY", 2, 1)
        time.sleep(4)
        
        """ Step 03 : Verify the following report is displayed in "Live Preview". """
        coln_list = ["EMP_ID", "LAST_NAME", "CURR_SAL", "SALARY"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 03a: Verify column titles")
        time.sleep(4)
        
        """ Step 04 : Click "Document" icon in "Design Grouping". """
        ribbonobj.select_ribbon_item("Home", "Document")

        """ Step 05 : Verify the report is converted to Document mode. """
        coln_list = ["EMP_ID", "LAST_NAME", "CURR_SAL", "SALARY"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 05.a: Verify column titles")
        ia_resultobj.create_report_data_set('TableChart_1', 12, 4, 'C2227528_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 12, 4, 'C2227528_Ds01.xlsx', 'Step 05.b: Verify report data set')

        """ Step 06 : Verify the Format is changed to Active Report """
        output_type=[el.text.strip() for el in driver.find_elements_by_css_selector("#HomeFormatType")]
        utillobj.asequal(['Active Report'], output_type, "Step 06: Verify the Format is changed to Active Report")

        """ Step 07 : Click Active Report dropdown > Select PDF. """
        ribbonobj.change_output_format_type("pdf")

        """ Step 08 : Click "IA" > "Save". """
        ribbonobj.select_top_toolbar_item('toolbar_save')
        time.sleep(3)

        """ Step 09 : Enter Title = "C2227528". """
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """ Step 10 : Run """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        
        """ Step 11 : Verify it generated the PDF document. """
        ele=driver.find_element_by_css_selector("#resultArea")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step11_'+browser, image_type='actual',x=50, y=20, w=-50, h=-20)
        
        """ Step 12 : Dismiss the Run window.
            Step 13 : Click "IA" > Exit.
            Step 14 : Click "No" to dismiss the prompt. """
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(5)
        ribbonobj.select_tool_menu_item('menu_close')
        time.sleep(5)
        driver.find_element_by_css_selector("#saveAllDlg #btnNo").click()
        time.sleep(5)
        
        """ Step 15 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        if browser == 'Firefox1': 
            driver.quit()
            time.sleep(3)
            from selenium import webdriver
            self.driver=webdriver.Firefox()
            driver = self.driver
            time.sleep(8)
        
        """ Step 16 : Run from Resources tree: """
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.active_run_fex_api_login(Test_Case_ID + ".fex", oFolder, 'mrid', 'mrpass')   
        time.sleep(10)
        #driver.maximize_window()
        time.sleep(2)
        
        """ Step 17: Verify that it generated the same PDF document. """
        if browser == 'IE':
            utillobj.take_monitor_screenshot(Test_Case_ID+'_Actual_Step16_'+browser, image_type='actual', left=200, top=80, right=200, bottom=50)
        elif browser == 'Chrome':
            ele=driver.find_element_by_css_selector("embed[type='application/pdf']")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step16_'+browser, image_type='actual',x=250, y=40, w=-250, h=-50)
        else:
            ele=driver.find_element_by_css_selector("#mainContainer canvas[id='page1']")
            utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step16_'+browser, image_type='actual',x=1, y=1, w=-1, h=-1)
        
        """ Step 18: Dismiss the Run window. """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ Step 19: Launch IA Report mode:- http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/EMPLOYEE&item=IBFS%3A%2FWFC%2FRepository%2FS10032 """
        utillobj.infoassist_api_login('report','ibisamp/employee','P292/S10032', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        #driver.maximize_window()
        time.sleep(5)
        
        """ Step 20 : Double click "EMP_ID", "LAST_NAME", "CURR_SAL", "SALARY". """
        metaobj.datatree_field_click("EMP_ID", 1, 1, 'Sort')
        time.sleep(4)
        metaobj.datatree_field_click("LAST_NAME", 1, 1, 'Sort')
        time.sleep(4)
        metaobj.datatree_field_click("CURR_SAL", 1, 1, 'Sum')
        time.sleep(4)
        metaobj.datatree_field_click("SALARY", 1, 1, 'Sum')
        time.sleep(4)
        coln_list = ["EMP_ID", "LAST_NAME", "CURR_SAL", "SALARY"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 20a: Verify column titles")
        time.sleep(4)
        
        """ Step 21 : Select "View" > "Document". """
        ribbonobj.select_ribbon_item("View", "Document")
        
        """ Step 22 : Verify the report is converted to Document mode. """
        coln_list = ["EMP_ID", "LAST_NAME", "CURR_SAL", "SALARY"]
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_1", coln_list, "Step 22.a: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 12, 4, 'C2227528_Ds01.xlsx', 'Step 22.b: Verify report data set')
        output_type=[el.text.strip() for el in driver.find_elements_by_css_selector("#iaCanvasCaptionLabel")]
        utillobj.asequal(['Document'], output_type, "Step 22.c: Verify the report is converted to Document mode")
        
        """ Step 23 : Click "IA" > Exit. """
        ribbonobj.select_tool_menu_item('menu_exit')
        time.sleep(5)
        
        """ Step 24 : Click "No" to dismiss the prompt. """
        driver.find_element_by_css_selector("#saveAllDlg #btnNo").click()
        time.sleep(5)
        
        """ Step 25 : Verify it prompt for "Save changes to Report1". """
        output_type=[el.text.strip() for el in driver.find_elements_by_css_selector("#saveAllDlg #saveChangesLabel")]
        utillobj.asequal(["Save Changes to 'Report1'?"], output_type, "Step 25: Verify the report is converted to Document mode")
        
        """ Step 26 : Click "No" to dismiss the Report. """
        driver.find_element_by_css_selector("#saveAllDlg #btnNo").click()
        time.sleep(5)
        
if __name__ == '__main__':
    unittest.main()