'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226968
TestCase Name = Test that Auto Drill works with Reporting Objects
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous, visualization_metadata
from common.wftools import report
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By
from common.lib.global_variables import Global_variables

class C2226968_TestClass(BaseTestCase):
    def test_C2226968(self):
        """
        Test case variable
        """
        Test_ID="C2226968"

        """
        Class & Objects
        """
        utillobj = utillity.UtillityMethods(self.driver)
        report_obj=report.Report(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_Case_ID = Test_ID+"_"+browser_type
        #driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(120)
        #elem1=(By.CSS_SELECTOR, "#TableChart_1")
        #resultobj._validate_page(elem1)
        #time.sleep(8)
        
        """    2. Click on Store Business Region on the canvas and Select Rank in the ribbon.    """
        metaobj.querytree_field_click("Store,Business,Region", 1)
        time.sleep(10)
        ribbonobj.select_ribbon_item('Field', 'Rank')
        
        """    3. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    4. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.wait_for_page_loads(120)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04a: Verify the Rank column added", desired_no_of_rows=15)
        
        """    5. Click on North America under Store_Business_Region column and select "Drill down to Store Business Sub Region"    """
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",12,2,'Drill down to Store Business Sub Region', "Step 05")
        browser=Global_variables.browser_name
        if browser == "firefox":
            iarun.select_autolink_tooltip_menu("table[summary='Summary']", 12, 2, 'Drill down to Store Business Sub Region', "Step 05")
        else:
            iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",12,2,'Drill down to Store Business Sub Region', "Step 05")
        utillobj.wait_for_page_loads(120)
#         iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 05a: Verify Drill down to Store Business Sub Region data set with rank", desired_no_of_rows=15)
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(10)
        
        """    6. Click IA > Save As> Type C2226968a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    7. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226968a.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(120)
        #elem1=(By.CSS_SELECTOR, "#TableChart_1")
        #resultobj._validate_page(elem1)
        #time.sleep(14)
         
        """    8. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        report_obj.wait_for_visible_text("#FormatAutoDrillCluster", 'Auto Drill', time_out=20)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 8a: Verify Autodrill button should be active")
        time.sleep(7)
         
        """    9. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    10. Click RUN    """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.wait_for_page_loads(120)
        utillobj.switch_to_frame(1)
        time.sleep(4)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 10a: Verify the Report Records')
        column_list=['RANK', 'Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 10b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 10c: Verify the report with RANK Column data', desired_no_of_rows=15)
        
        """    11. Click on North America and Select "Drill down to Store Business Sub Region"    """
        #miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 1, 'Drill down to Store Business Sub Region')
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 1, 'Drill down to Store Business Sub Region')
        utillobj.wait_for_page_loads(120)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 11a: Verify the Report Records')
        column_list=['RANK', 'Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 11c: Verify the report data ', desired_no_of_rows=15)
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    12. Click IA > Save As> Type C2226968b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(5)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(6)
        
        """    13. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226964b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.wait_for_page_loads(120)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
         
        """    14. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 14a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)

        """    15. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()