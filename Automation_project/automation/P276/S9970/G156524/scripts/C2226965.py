'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226965
TestCase Name = Test that existing WHERE on hierarchy field is still respected on drilldown
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_run, active_miscelaneous, ia_ribbon
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226965_TestClass(BaseTestCase):
    def test_C2226965(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID = "C2226965"
        Test_Case_ID = Test_ID+"_"+browser_type
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible("#TableChart_1", 190)
        
        """    2. Drag Store,Business,Region (Store > Store > Store,Business,Region) to the filter pane
                > Click the Get Values button & select All from the dropdown > Double click on EMEA & North America.
                Click OK twice to close the dialogues    """
        #metaobj.datatree_field_click("Store,Business,Region", 1, 1,'Filter')
        metaobj.drag_drop_data_tree_items_to_filter('Store,Business,Region', 1)
        time.sleep(5)
        browser_type = utillity.UtillityMethods.parseinitfile(self, 'browser')
        utillobj.synchronize_with_visble_text("#dlgWhere_btnOK", 'OK', 120)
        condition_elem=self.driver.find_elements_by_css_selector("#dlgWhere #dlgWhereWhereTree table tr:nth-child(2) span[class*='selected']>span>span")
        elem=condition_elem[-1]
        utillobj.default_left_click(object_locator = elem)
        time.sleep(5)
        utillobj.default_click(elem, click_option = 2)
        time.sleep(3)
        utillobj.synchronize_with_number_of_element("[id^='InlineControlValue']>div[id^='BiButton']", 1, 25)
        btn_obj = self.driver.find_element_by_css_selector("[id^='InlineControlValue']>div[id^='BiButton']")
        utillobj.default_click(btn_obj)
        utillobj.synchronize_with_visble_text("#dlgWhereValue_tbuttonGetValue", 'Get Values', 180)
        ia_ribbonobj.select_filter_values('constant', 'All', ['EMEA','North America'])
        time.sleep(3)
        elem1=self.driver.find_element_by_css_selector("#wndWhereValuePopup_btnOK img")
        utillobj.default_left_click(object_locator=elem1)
        time.sleep(3)
        ia_ribbonobj.close_filter_dialog()
        time.sleep(6)
        
        """    3. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(4)
         
        """    4. Click Run    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)              
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 06a: verify Auto Drill, drill down data set")
        time.sleep(5)
        
        """    5. Click on North America and Select "Drill down to Store Business Sub Region"     """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",12,1,'Drill down to Store Business Sub Region', "Step 07")
        time.sleep(10)
#         iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 07a: Verify that Autoprompt does not re-prompt on drill down", desired_no_of_rows=15)
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    6. Click IA > Save As> Type C2226965a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        
        """    7. Open saved fex. http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226965a.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    8. Click format tab and Verify that Auto Drill is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 8a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
        
        """    9. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(20)
        
        """    10. Click Run    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        miscelanousobj.verify_page_summary(0, '14of14records,Page1of1', 'Step 10a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 10b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 10c: Verify the report data ')
        
        """    11. Click on North America and Select "Drill down to Store Business Sub Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, 'Drill down to Store Business Sub Region')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 11a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11b: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 11c: Verify the report data ')
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    12. Click IA > Save As> Type C2226965b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    13. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226965b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_until_element_is_visible("#TableChart_1", 190)
         
        """    14. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 14a: Verify Autodrill button should be active")
        time.sleep(4)
        
        """    15. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
