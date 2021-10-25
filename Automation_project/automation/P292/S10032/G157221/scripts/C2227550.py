'''
Created on 06-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227550
TestCase Name = Verify HOLD with Joined files 
'''
import unittest, time
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea,active_miscelaneous
from common.lib import utillity, core_utility
from common.lib.basetestcase import BaseTestCase

class C2227550_TestClass(BaseTestCase):

    def test_C2227550(self):        
        Test_Case_ID = "C2227550"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        core_utilobj = core_utility.CoreUtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        active_misobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)

        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','ibisamp/empdata','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#TableChart_1", ia_ribbonobj.chart_long_timesleep)
        
        """    2. Click Data tab --> Join    """
        """    3. Click 'Add New' > select Training file > click 'Open'    """
        ia_ribbonobj.create_join("ibisamp","training")
        utillobj.synchronize_with_visble_text("#dlgJoinLinkManager", 'training', ia_ribbonobj.home_page_medium_timesleep)
        
        '''
        Workaround: Open dialog was not able to open using pyautogui for the second time, hence added the below workaround 
        '''
        ia_ribbonobj.select_join_menu_buttons("ok")
        utillobj.synchronize_until_element_disappear("#dlgJoin [class*='active']", ia_ribbonobj.home_page_long_timesleep)
        
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
        ia_ribbonobj.create_join("ibisamp","locator")
        utillobj.synchronize_with_visble_text("#dlgJoinLinkManager", 'locator', ia_ribbonobj.home_page_medium_timesleep)
        
        """    5. Click 'Remove' > OK to delete default link    """
        ia_ribbonobj.select_join_menu_buttons("remove")
        utillobj.synchronize_until_element_disappear("marker path[fill='red']", ia_ribbonobj.home_page_medium_timesleep)
        
        '''
        driver.find_element_by_css_selector("#dlgJoin_btnDeleteJoin img").click()
        time.sleep(4)
        btn_css="div[id^='BiDialog'] div[id^='BiOptionPane'] div[id^='BiButton']"
        elem=[el for el in self.driver.find_elements_by_css_selector(btn_css) if el.text.strip()=="OK"]
        elem[0].click()'''
        
        """    6. Drag and drop PIN field from Training table to PIN field in Locator table    """
        ia_ribbonobj.create_join_link(1, "PIN", 2, "PIN")
        utillobj.synchronize_until_element_is_visible("marker path[fill='red']", ia_ribbonobj.home_page_medium_timesleep)
        ia_ribbonobj.verify_join_link_color(0, 'blue', "Step 06.00: verify Join link color 'blue' for first join")
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 06.01: verify Join link color 'red' for second join")
        
        """    7. Click OK to create Join    """
        ia_ribbonobj.select_join_menu_buttons("ok")
        utillobj.synchronize_with_visble_text("[id^=QbMetaDataTree] table", 'GRADE', ia_ribbonobj.chart_long_timesleep)
        
        """    8. Verify Data pane    """
        metaobj.verify_data_pane_field("Dimensions", "GRADE", 13, "Step 08.00: ")
        metaobj.verify_data_pane_field("Dimensions", "FLOOR", 17, "Step 08.01: ")
        metaobj.verify_data_pane_field("Dimensions", "AREA", 20, "Step 08.02: ")
        metaobj.verify_data_pane_field("Measures/Properties", "SALARY", 1, "Step 08.03: ")
        metaobj.verify_data_pane_field("Measures/Properties", "EXPENSES", 2, "Step 08.04: ")
        
        """    9. Double-click fields DEPT, SITE, LASTNAME, COURSECODE, EXPENSES.    """
        metaobj.datatree_field_click("Dimensions->DEPT", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'DEPT', ia_ribbonobj.chart_long_timesleep)
        metaobj.datatree_field_click("Dimensions->SITE", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'SITE', ia_ribbonobj.chart_long_timesleep)
        metaobj.datatree_field_click("Dimensions->LASTNAME", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'LASTNAME', ia_ribbonobj.chart_long_timesleep)
        metaobj.datatree_field_click("Dimensions->COURSECODE", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'COURSECODE', ia_ribbonobj.chart_long_timesleep)
        metaobj.datatree_field_click("Measures/Properties->EXPENSES", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_1", 'EXPENSES', ia_ribbonobj.chart_long_timesleep)
        coln_list = ['DEPT', 'SITE', 'LASTNAME', 'COURSECODE', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(5, 5, "TableChart_1", coln_list, "Step 09.00: Verify column titles.")
        
        """    10. Select "Home" > "File" button    """        
        """    11. Save with Default file name "File1"    """
        """    12. File type as Binary(*.ftm)    """
        """    13. Click Save    """
        ia_ribbonobj.create_hold_file("C2227550", "Binary (*.ftm)")
        
        
        """    14. Notice "Create Report" button at the bottom of report    """
        btn_css='#createFromHoldButton #createFromHoldMenuBtn'
        utillobj.synchronize_until_element_is_visible(btn_css, ia_ribbonobj.home_page_medium_timesleep)
        bol=driver.find_element_by_css_selector(btn_css).is_displayed()
        utillobj.asequal(True, bol, "Step 14.00: Verify 'Create Report' button at the bottom of report ")
        
        """    15. Click on the "Create Report" menu > select "Create Document"    """
        ia_resultobj.create_hold_type("Create Document")
        utillobj.synchronize_with_visble_text("[id^=QbMetaDataTree] table", 'DEPT', ia_ribbonobj.chart_long_timesleep) 
        
        """    16. Verify Query and Data pane    """
        metaobj.verify_data_pane_field('Dimensions', 'DEPT', 1, "Step 15.00: ")
        metaobj.verify_data_pane_field('Dimensions', 'SITE', 2, "Step 15.01: ")
        metaobj.verify_data_pane_field('Dimensions', 'LASTNAME', 3, "Step 15.02: ")
        metaobj.verify_data_pane_field('Dimensions', 'COURSECODE', 4, "Step 15.03: ")
        metaobj.verify_data_pane_field('Measures/Properties', 'EXPENSES', 1, "Step 15.04: ")
        metaobj.verify_query_pane_field('Files', 'C2227550 (empdata)', 1, "Step 15.05: ")
        
        """    17. Double-click fields LASTNAME, SITE, COURSECODE, EXPENSES.    """
        metaobj.datatree_field_click("Dimensions->LASTNAME", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2", 'LASTNAME', ia_ribbonobj.chart_long_timesleep)
        metaobj.datatree_field_click("Dimensions->SITE", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2", 'SITE', ia_ribbonobj.chart_long_timesleep)
        metaobj.datatree_field_click("Dimensions->COURSECODE", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2", 'COURSECODE', ia_ribbonobj.chart_long_timesleep)
        metaobj.datatree_field_click("Measures/Properties->EXPENSES", 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2", 'EXPENSES', ia_ribbonobj.chart_long_timesleep)
        
        """    18. Verify the Query pane and the following report is displayed.    """
        metaobj.verify_query_pane_field("Sum", "EXPENSES", 1, "Step 18.00: ")
        metaobj.verify_query_pane_field("By", "LASTNAME", 1, "Step 18.01: ")
        metaobj.verify_query_pane_field("By", "SITE", 2, "Step 18.02: ")
        metaobj.verify_query_pane_field("By", "COURSECODE", 3, "Step 18.03: ")
        
        coln_list = ['LASTNAME', 'SITE', 'COURSECODE', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_2", coln_list, "Step 18.04: Verify column titles")
        
        """    19. Click "Run".    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_until_element_is_visible("[id^=ReportIframe]", ia_ribbonobj.chart_long_timesleep)
        core_utilobj.switch_to_frame()
        utillobj.synchronize_with_visble_text("#MAINTABLE_0", 'LASTNAME', ia_ribbonobj.chart_long_timesleep)
        
        """    20. Verify the report is displayed.    """
        active_misobj.verify_page_summary('0','41of41records,Page1of1', 'Step 20.00: Verify Page summary')
        column_list=['LASTNAME', 'SITE', 'COURSECODE', 'EXPENSES']
        active_misobj.verify_column_heading('MAINTABLE_0', column_list, 'Step 20.01: Verify the column heading')
        utillobj.verify_data_set('ITableData0','I0r','C2227550_Ds01.xlsx',"Step 20.02: Verify the data set")
        #utillobj.create_data_set('ITableData0','I0r','C2227550_Ds01.xlsx')
        core_utilobj.switch_to_default_content()
        
        """    21. Close the output window    """
        """    22. Click "IA" > "Save".    """
        """    23. Enter Title = "C2227550".    """
        """    24. Click "Save".    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", ia_ribbonobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    25. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    26. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S7385', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_2", 'LASTNAME', ia_ribbonobj.chart_long_timesleep)
        
        """    27. Verify Document    """
        metaobj.verify_query_pane_field('Files', 'C2227550 (EMPDATA)', 1, "Step 22a: ")
        coln_list = ['LASTNAME', 'SITE', 'COURSECODE', 'EXPENSES']
        resultobj.verify_report_titles_on_preview(4, 4, "TableChart_2", coln_list, "Step 27.00: Verify column titles.")
        
        """    28. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()
