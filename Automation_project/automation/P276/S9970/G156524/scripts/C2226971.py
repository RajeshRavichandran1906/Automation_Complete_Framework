'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226971
TestCase Name = Test that Prefix operators are retained but WITHIN is dropped with Auto Drill
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous, visualization_metadata
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226971_TestClass(BaseTestCase):
    def test_C2226971(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226971"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(40)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Right click on Sale Year from ACROSS bucket in query pane > Delete    """
        metaobj.querytree_field_click("Sale,Year", 1, 1, 'Delete')
        time.sleep(10)
        
        """    3. Select Home tab > Click on Rows Totals to deselect it.    """
        ribbonobj.select_ribbon_item("Home", "Row_totals")
        time.sleep(5)
        
        """    4. Double click on Revenue from the list of fields twice to add two more Revenue columns to the canvas    """
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("Revenue", 2, 1)
        time.sleep(8)
        
        """    5. Right click on second Revenue from the canvas > select More > Aggregation Functions > Percent    """
        metaobj.querytree_field_click("Revenue", 2, 1, 'More', 'Aggregation Functions', 'Percent')
        
        """    6. Right click of second PCT Revenue column and select Edit Format. Uncheck Floating Currency and check Percent.    """
        metaobj.querytree_field_click("PCT.Revenue", 1, 1, 'Edit Format')
        time.sleep(8)
        utillobj.select_combobox_item("currencySymbolCBox", "None")
        #driver.find_element_by_css_selector("div[id^='QbDialog-'] #floatDollarRadioBtn input").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div[id^='QbDialog-'] #percentRadioBtn input").click()
        time.sleep(3)
        ok_btn=driver.find_element_by_css_selector("div[id^='QbDialog-'] #fmtDlgOk img")
        utillobj.default_left_click(object_locator=ok_btn)
        time.sleep(8)
        
        """    7. Right click on third Revenue from the canvas > select More > Aggregation Functions > Percent    """
        metaobj.querytree_field_click("Revenue", 2, 1, 'More', 'Aggregation Functions', 'Percent')
        
        """    8. Right click of third PCT Revenue column and select Edit Format. Uncheck Floating Currency and check Percent.    """
        metaobj.querytree_field_click("PCT.Revenue", 2, 1, 'Edit Format')
        time.sleep(8)
        utillobj.select_combobox_item("currencySymbolCBox", "None")
        #driver.find_element_by_css_selector("div[id^='QbDialog-'] #floatDollarRadioBtn input").click()
        time.sleep(3)
        driver.find_element_by_css_selector("div[id^='QbDialog-'] #percentRadioBtn input").click()
        time.sleep(3)
        ok_btn=driver.find_element_by_css_selector("div[id^='QbDialog-'] #fmtDlgOk img")
        utillobj.default_left_click(object_locator=ok_btn)
        time.sleep(8)
        
        """    9. Right click on the last Revenue column only and select More > Aggregate Within > By > Store,Business,Region    """
        metaobj.querytree_field_click("PCT.Revenue", 2, 1, 'More', 'Aggregate Within', 'By', 'Store,Business,Region')
        
        """    10. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    11. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 11a: Verify dataset", desired_no_of_rows=15)
        
        """    12. Click on North America and select "Drill down to Store Business Sub Region".     """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",11,1,'Drill down to Store Business Sub Region', "Step 12")
        time.sleep(8)
        """    13. Verify the output displays as expected,
                    1.Verify that Percent prefix operator should be retained for both columns.
                    2.Verify that both percentage columns are identical now since the WITHIN is lost on drill down.
        """
#         iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 12a: Verify dataset drilldown with aggregation within displayed", desired_no_of_rows=15)
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(3)
        
        """    14. Click IA > Save As> Type C2226971a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    15. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226971a.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(35)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14)
         
        """    16. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 16a: Verify Autodrill button should be active")
        time.sleep(4)
         
        """    17. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    18. Click RUN    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(1)
        time.sleep(4)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 18a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'PCT Revenue', 'PCT Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 18b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 18c: Verify the report data', desired_no_of_rows=15)
        
        """    19. Click on North America and select "Drill down to Store Business Sub Region".    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, 'Drill down to Store Business Sub Region')
        time.sleep(6)
        
        """    20. Verify the output displays as expected,
                1) Verify that Percent prefix operator should be retained for both columns.
                2)Verify that both percentage columns are identical now since the WITHIN is lost on drill down.
        """
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 20a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'PCT Revenue', 'PCT Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 20b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 20c: Verify the report data', desired_no_of_rows=15)
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(3)
        
        """    21. Click IA > Save As> Type C2226971b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    22. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226964b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    23. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 23a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
        
        """    24. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
