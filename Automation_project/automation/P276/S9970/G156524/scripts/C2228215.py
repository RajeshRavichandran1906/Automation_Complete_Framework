'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226956
TestCase Name = Test drilling all the way down and up a long hierarchy path - AHTML
'''
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from common.pages import visualization_resultarea, visualization_ribbon, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2228215_TestClass(BaseTestCase):
    def test_C2228215(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2228215"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        elem = "#ITableData0>tbody>tr>td>div>a"
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(15)
        
        """    2. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    3. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    4. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 04a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 04b: Verify the column heading')
        time.sleep(2)
        
        """    5. Drill down - Click on North America under Store_Business,Region column and select "Drill down to Store Business Sub Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7,0, 'Drill down to Store Business Sub Region')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 05a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 05b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', desired_no_of_rows=7)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', 'Step 05c: Verify the report data', desired_no_of_rows=7)
        time.sleep(2)
        
        """    6. Click on East and select "Drill down to Store Country"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7,0, 'Drill down to Store Country')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', 'Step 06a: Verify the Report Records')
        column_list=['Store Country', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 06b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 06c: Verify the report data')
        time.sleep(2)
        
        """    7. Click on United States and select "Drill down to Store State Province"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Drill down to Store State Province')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '21of21records,Page1of1', 'Step 07a: Verify the Report Records')
        column_list=['Store State Province', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 07b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', desired_no_of_rows=7)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 07c: Verify the report data', desired_no_of_rows=7)
        time.sleep(2)
        
        """    8. Click on New York and select "Drill down to Store City"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7,0, 'Drill down to Store City')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 4)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', 'Step 08a: Verify the Report Records')
        column_list=['Store City', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 08b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 08c: Verify the report data')
        time.sleep(2)
        
        """    9. Click on New york and select "Drill down to Store Postal Code "    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Drill down to Store Postal Code')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 5)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', 'Step 09a: Verify the Report Records')
        column_list=['Store Postal Code', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 09b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx', 'Step 09c: Verify the report data')
        time.sleep(2)
        
        """    10. Click on 10007 and select "Drilldown to Store Name"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Drill down to Store Name')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 6)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', 'Step 10a: Verify the Report Records')
        column_list=['Store Name', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 10b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds07.xlsx', 'Step 10c: Verify the report data')
        time.sleep(2)
        
        """    11. Drill up - Now Click on New York and select "Drillup to Store Postal Code"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Drill up to Store Postal Code')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 5)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', 'Step 11a: Verify the Report Records')
        column_list=['Store Postal Code', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx', 'Step 11c: Verify the report data')
        time.sleep(2)
        
        """    12. Click on 10007 and select "Drill up to Store City"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Drill up to Store City')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 4)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', 'Step 12a: Verify the Report Records')
        column_list=['Store City', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 12b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 12c: Verify the report data')
        time.sleep(2)
        
        """    13. Click on New York and select "Drill up to Store State Province"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Drill up to Store State Province')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 3)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '21of21records,Page1of1', 'Step 13a: Verify the Report Records')
        column_list=['Store State Province', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 13b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 13c: Verify the report data', desired_no_of_rows=7)
        time.sleep(2)
        
        """    14. Click on New York and select "Drill up to Store Country"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7,0, 'Drill up to Store Country')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 2)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '7of7records,Page1of1', 'Step 14a: Verify the Report Records')
        column_list=['Store Country', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 14c: Verify the report data')
        time.sleep(2)
        
        """    15. Click on United States and select "Drillup to Store Business Sub Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Drill up to Store Business Sub Region')
        time.sleep(5)
        WebDriverWait(driver, 200).until(lambda s: len(s.find_elements(By.CSS_SELECTOR, elem)) == 1)
        time.sleep(5)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 15a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 15b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds02.xlsx', 'Step 15c: Verify the report data', desired_no_of_rows=7)
        time.sleep(2)
        
        """    16. Click on East and select "Drill up to Store Business Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7,0, 'Drill up to Store Business Region')
        time.sleep(15)
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 16a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 16b: Verify the column heading')
        time.sleep(2)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(10)
        
        """    17. Click IA > Save As> Type C2228215 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    18. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2228215.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14) 
        
        """    19. Click format tab and see Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(10)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 18a: Active_Report - Verify Autodrill button is still selected")
        time.sleep(4)
        
        """    20. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
