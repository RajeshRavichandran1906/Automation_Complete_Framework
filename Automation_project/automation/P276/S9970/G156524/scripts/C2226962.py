'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226962
TestCase Name = Test that using BYDISPLAY has active links on each line on the highest level sort in the report.
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226962_TestClass(BaseTestCase):
    def test_C2226962(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226962"
        Test_Case_ID = Test_ID+"_"+browser_type
        #driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(15)
        
        """    2. Right click on "Store Business Region" on the report canvas. Choose Change Title. Enter 'World,Market' > OK    """
        ribbonobj.select_ribbon_item("Format", "Repeat_sort_value")
        time.sleep(4)
        
        """    3. Click Format tab > Autodrill button    """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(4)
        
        """    4. Click RUN    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04a: verify Auto Drill, drill down data set", desired_no_of_rows=15)
                
        """    5. Click on the last North America (next to Video Production) and see the Drill menu    """
        """    6. From the drill menu click on "Drill down to Store Business Sub Region"    """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",18,1,'Drill down to Store Business Sub Region', "Step 05:")
        time.sleep(15)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 06a: Verify this breadcrumb (North America) should appear above the previous one (Stereo Systems) Since this is a higher level sort .", desired_no_of_rows=15)
        time.sleep(4)
        
        """    7. Click on East next to Stereo Systems and see the Drill menu    """
        expected_tooltip_list = ['Restore Original', 'Drill up to Store Business Region', 'Drill down to Store Country']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",16,1, expected_tooltip_list, "Step 07a: Verify the Drill down menu")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(4)
        
        """    8. Click IA > Save As > Type C2226962a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID+"_a")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    9. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226962a.fex&tool=Report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID+"_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14) 
        
        """    10. Click on the Format tab. Verify that both Repeat Sort Value and Auto Drill are still selected..    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 10a: Verify Autodrill button should be active")
        disabled =self.driver.find_element_by_css_selector("#FormatRepeatSort").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 10b: Verify Repeat Sort Value button should be active")
        time.sleep(4)
        
        """    11. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    12. Click Run    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 12a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 12b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 12c: Verify the report data ')
        
        """    13. Click on the last North America (next to Video Production) and see the Drill menu    """
        """    14. From the drill menu click on "Drill down to Store Business Sub Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 13, 0, 'Drill down to Store Business Sub Region')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 14a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 14c: Verify the report data ')
        
        """    15. Click on East next to Stereo Systems and see the Drill menu.    """
        values=['Restore Original', 'Drill up to Store Business Region', 'Drill down to Store Country', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 11, 0, values, "Step 15 : Verify the Drill down menu")
        time.sleep(5)
        utillobj.switch_to_default_content(pause=3)
        time.sleep(4)
        
        """    16. Click IA > Save As > Type C2226962b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID+"_b")
        time.sleep(5)
        
        """    17. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226962b.fex&tool=Report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID+"_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    18. Click on the Format tab. Verify that both Repeat Sort Value and Auto Drill are still selected.    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 18a: Verify Autodrill button should be active")
        disabled =self.driver.find_element_by_css_selector("#FormatRepeatSort").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 18b: Verify Repeat Sort Value button should be active")
        time.sleep(4)
        time.sleep(4)
        
        """    19. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
