'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226966
TestCase Name = Test that Auto Drill works with Reporting Objects
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, wf_legacymainpage , active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226966_TestClass(BaseTestCase):
    
    def test_C2226966(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226966"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        mainobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. From Resource tree, Right click on RO-Shell under S9970 folder and select New > Report    """
        node = utillobj.parseinitfile('nodeid')
        port = utillobj.parseinitfile('httpport')
        context = utillobj.parseinitfile('wfcontext')
        setup_url = 'http://' + node + ':' + port + context + '/'
        self.driver.get(setup_url)
        utillobj.login_wf('mrid','mrpass')
        time.sleep(6)
        project_id=utillobj.parseinitfile('project_id')
        folder = utillobj.parseinitfile('suite_id')
        mainobj.select_repository_menu(project_id + "->" + folder + "->RO-Shell", "New->Report")
        time.sleep(45)
        utillobj.switch_to_window(1)
        time.sleep(5)
        driver.maximize_window()
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(15)
        
        
        """    2. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    3. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        
        
        """    4. Click on North America under Store_Business,Region column and select "Drill down to Store Business Sub Region"    """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",10,1,'Drill down to Store Business Sub Region')
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",10,1,'Drill down to Store Business Sub Region', "Step 04")
        time.sleep(5)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04a: Verify Drill down to Store Business Sub Region data set", desired_no_of_rows=15)
        
        """    5. Click on Stereo Systems under East Sub Region and select "Drill down to Product Subcategory"    """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",16,2,'Drill down to Product Subcategory')
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",16,2,'Drill down to Product Subcategory', "Step 05")
        time.sleep(5)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 05a: Verify Drill down to Product Subcategory data set")
        time.sleep(3)
        
        """    6. Click on 2016 In the ACROSS titles and select "Drill down to Sale Year/Quarter"    """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,2,'Drill down to Sale Year/Quarter')
        #iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",3,2,'Drill down to Sale Year/Quarter', "Step 06")
        time.sleep(5)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 06a: Verify Drill down to Sale Year/Quarter data set")
        time.sleep(3)
        utillobj.switch_to_default_content(1)
        time.sleep(10)
        
        """    7. Click IA > Save As> Type C2226966a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        driver.close()
        time.sleep(5)
        utillobj.switch_to_window(0)
        time.sleep(5)
        
        """    8. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226966a.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(35)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14)
         
        """    9. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 9a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
         
        """    10. Click on HTML5 output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    11. Click RUN    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(1)
        time.sleep(4)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 11a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11b: Verify the column heading')
        
        """    12. Click on North America and Select "Drill down to Store Business Sub Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, 'Drill down to Store Business Sub Region')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 12a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 12b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 12c: Verify the report data ', desired_no_of_rows=15)
        time.sleep(5)
        
        """    13. Click on Stereo Systems under East Sub Region and select "Drill down to Product Subcategory"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 11, 1, 'Drill down to Product Subcategory')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 13a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Subcategory', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 13b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 13c: Verify the report data')
        time.sleep(5)
        
        """    14. Click on 2016 In the ACROSS titles and select "Drill down to Sale Year/Quarter"    """
        utillobj.asequal(True, False, "Step 14: ACT-618 has been opened for not able to drilldown from ACROSS titles")
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    15. Click IA > Save As> Type C2226966b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    16. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226964b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    17. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 17a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
        
        """    18. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
