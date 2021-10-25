'''
Created on 06-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227550
TestCase Name = Verify HOLD with Joined files 
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea,active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.locators.loginpage_locators import LoginPageLocators

class C2227550_TestClass(BaseTestCase):

    def test_C2227550(self):        
        Test_Case_ID = "C2227550"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)

        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P137/S7385', 'mrid', 'mrpass')
        time.sleep(10)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    2. Click Data tab --> Join    """
        """    3. Click 'Add New' > select Training file > click 'Open'    """
        ia_ribbonobj.create_join("training")
        time.sleep(10)
        
        '''
        Workaround: Open dialog was not able to open using pyautogui for the second time, hence added the below workaround 
        '''
        ia_ribbonobj.select_join_menu_buttons("ok")
        time.sleep(6)
        '''ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as("temp")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit("temp", 'report', 'S7385', mrid='mrid', mrpass='mrpass')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)'''
        
        """    4. Click 'Add New' > select Locator file > click 'Open'    """
        ia_ribbonobj.create_join("locator")
        #ia_ribbonobj.create_join("locator", new_join=False)
        time.sleep(10)
        
        """    5. Click 'Remove' > OK to delete default link    """
        ia_ribbonobj.select_join_menu_buttons("remove")
        time.sleep(8)
        '''
        driver.find_element_by_css_selector("#dlgJoin_btnDeleteJoin img").click()
        time.sleep(4)
        btn_css="div[id^='BiDialog'] div[id^='BiOptionPane'] div[id^='BiButton']"
        elem=[el for el in self.driver.find_elements_by_css_selector(btn_css) if el.text.strip()=="OK"]
        elem[0].click()'''
        
        """    6. Drag and drop PIN field from Training table to PIN field in Locator table    """
        ia_ribbonobj.create_join_link(1, "PIN", 2, "PIN")
        ia_ribbonobj.verify_join_link_color(0, 'blue', "Step 06a: verify Join link color 'blue' for first join")
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 06b: verify Join link color 'red' for second join")
        
        """    7. Click OK to create Join    """
        ia_ribbonobj.select_join_menu_buttons("ok")
        #driver.find_element_by_css_selector("#dlgJoin_btnOK").click()
        time.sleep(8)
        
        """    8. Verify Data pane    """
        metaobj.verify_data_pane_field("Dimensions", "GRADE", 13, "Step 8a: ")
        metaobj.verify_data_pane_field("Dimensions", "FLOOR", 17, "Step 8b: ")
        metaobj.verify_data_pane_field("Dimensions", "AREA", 20, "Step 8c: ")
        metaobj.verify_data_pane_field("Measures/Properties", "SALARY", 1, "Step 8d: ")
        metaobj.verify_data_pane_field("Measures/Properties", "EXPENSES", 2, "Step 8e: ")
        
        """    9. Double-click fields DEPT, SITE, LASTNAME, COURSECODE, EXPENSES.    """
        metaobj.datatree_field_click("DEPT", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SITE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("COURSECODE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("EXPENSES", 2, 1)
        time.sleep(4)
        coln_list = ['DEPT', 'SITE', 'LASTNAME', 'COURSECODE', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 09: Verify column titles")
        time.sleep(4)
        
        """    10. Select "Home" > "File" button    """        
        """    11. Save with Default file name "File1"    """
        """    12. File type as Binary(*.ftm)    """
        """    13. Click Save    """
        ia_ribbonobj.create_hold_file("C2227550", "Binary (*.ftm)")
        
        
        """    14. Notice "Create Report" button at the bottom of report    """
        btn_css='#createFromHoldButton #createFromHoldMenuBtn'
        bol=driver.find_element_by_css_selector(btn_css).is_displayed()
        utillobj.asequal(True, bol, "Step 14: Verify 'Create Report' button at the bottom of report ")
        
        """    15. Click on the "Create Report" menu > select "Create Document"    """
        ia_resultobj.create_hold_type("Create Document")
        time.sleep(15)
        
        """    16. Verify Query and Data pane    """
        metaobj.verify_data_pane_field('Dimensions', 'DEPT', 1, "Step 15a: ")
        metaobj.verify_data_pane_field('Dimensions', 'SITE', 2, "Step 15b: ")
        metaobj.verify_data_pane_field('Dimensions', 'LASTNAME', 3, "Step 15c: ")
        metaobj.verify_data_pane_field('Dimensions', 'COURSECODE', 4, "Step 15d: ")
        metaobj.verify_data_pane_field('Measures/Properties', 'EXPENSES', 1, "Step 15e: ")
        metaobj.verify_query_pane_field('Files', 'C2227550 (empdata)', 1, "Step 15f: ")
        
        """    17. Double-click fields LASTNAME, SITE, COURSECODE, EXPENSES.    """
        metaobj.datatree_field_click("LASTNAME", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("SITE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("COURSECODE", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("EXPENSES", 2, 1)
        time.sleep(4)
        
        """    18. Verify the Query pane and the following report is displayed.    """
        metaobj.verify_query_pane_field("Sum", "EXPENSES", 1, "Step 18a: ")
        metaobj.verify_query_pane_field("By", "LASTNAME", 1, "Step 18b: ")
        metaobj.verify_query_pane_field("By", "SITE", 2, "Step 18c: ")
        metaobj.verify_query_pane_field("By", "COURSECODE", 3, "Step 18d: ")
        
        coln_list = ['LASTNAME', 'SITE', 'COURSECODE', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_2", coln_list, "Step 18e: Verify column titles")
        time.sleep(4)
        
        """    19. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        
        """    20. Verify the report is displayed.    """
        active_misobj.verify_page_summary('0','41of41records,Page1of1', 'Step 20a: Verify Page summary')
        column_list=['LASTNAME', 'SITE', 'COURSECODE', 'EXPENSES']
        active_misobj.verify_column_heading('ITableData0', column_list, 'Step 20b: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','C2227550_Ds01.xlsx',"Step 20c: Verify the data set")
        #utillobj.create_data_set('ITableData0','I0r','C2227550_Ds01.xlsx')
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    21. Close the output window    """
        """    22. Click "IA" > "Save".    """
        """    23. Enter Title = "C2227550".    """
        """    24. Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    25. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    26. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S7385')
        time.sleep(20)
        elem1=(By.CSS_SELECTOR, "#TableChart_2")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    27. Verify Document    """
        metaobj.verify_query_pane_field('Files', 'C2227550 (EMPDATA)', 1, "Step 22a: ")
        coln_list = ['LASTNAME', 'SITE', 'COURSECODE', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_2", coln_list, "Step 27a: Verify column titles")
        time.sleep(4)
        
        """    28. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()


        
        
        
        
        
        
        
        
        
