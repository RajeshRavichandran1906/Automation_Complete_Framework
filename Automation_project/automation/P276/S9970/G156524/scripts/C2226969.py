'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226969
TestCase Name = Test that Auto Drill works with Group created from a hierarchy field prior to setting Auto Drill
'''
import unittest, time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous, visualization_metadata
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226969_TestClass(BaseTestCase):
    
    def test_C2226969(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226969"
        Test_Case_ID = Test_ID+"_"+browser_type
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
        
        """    2. Right click on Store Business Region on the canvas and select 'Create Group...'    """
        metaobj.querytree_field_click("Store,Business,Region", 1, 1, "Create Group...")
        time.sleep(8)
        
        """    3. Change the Field name to "BUSINESS_GROUP". Multi select both North America and South America using CTRL key.
                Click on "Group" in the upper left of the dialog. Click OK to close the dialog.    """
        metaobj.create_ia_group('Group', ['North America', 'South America'], change_field_txt='BUSINESS_GROUP', close_button='ok')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table>tbody>tr:nth-child(6)", "BUSINESS_GROUP", 40)
        
        """    4. Right click on BUSINESS_GROUP on the canvas and select "Change Title". Enter "Store,Business,Group" and click OK to close.    """
        metaobj.querytree_field_click("BUSINESS_GROUP", 1, 1, "Change Title...")
        time.sleep(8)
        edit_title_css="div[id^='BiDialog'][tabindex='0']"
        edit_title_obj=self.driver.find_element_by_css_selector(edit_title_css)
        utillobj.set_text_field_using_actionchains(edit_title_obj.find_element_by_css_selector("input"), 'Store,Business,Group')
        utillobj.click_dialog_button(edit_title_css,"OK")
        time.sleep(4)
        
        """    5. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    6. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 06a: Verify the Data set", desired_no_of_rows=15)
        
        """    7. Click on Click on North America and South America Group    """
        expected_tooltip_list = ['Drill down to Store Business Region']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",12,1, expected_tooltip_list, "Step 07a: Verify the menu shows 'Drill down to Store Business Region'")
        time.sleep(5)
        
        """    8. Select "Drill down to Store Business Region"    """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",12,1,'Drill down to Store Business Region', "Step 08", cord_type='top_middle', x_offset=0, y_offset=5)
        time.sleep(15)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=15)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 08a: Verify Drill down to Store Business Sub Region data set", desired_no_of_rows=15)
        time.sleep(4)
        
        """    9. Click on North America.    """
        expected_tooltip_list = ['Restore Original', 'Drill up to Store Business Group', 'Drill down to Store Business Sub Region']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",5,1, expected_tooltip_list, "Step 09: Verify the menu shows 'Drill down to Store Business Region'")
        time.sleep(5)
        utillobj.switch_to_default_content(1)
        time.sleep(2)
        
        """    10. Click IA > Save As> Type C2226969a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    11. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226969a.fex&tool=report    """
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(35)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(14)
         
        """    12. Click format tab and Verify Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 8a: Verify Autodrill button should be active")
        time.sleep(4)
         
        """    13. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(15)
        
        """    14. Click RUN    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(1)
        time.sleep(4)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '21of21records,Page1of1', 'Step 14a: Verify the Report Records')
        column_list=['Store Business Group', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', desired_no_of_rows=15)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 14c: Verify the report dataset', desired_no_of_rows=15)
        
        """    15. Click on North America and South America Group    """
        values=['Drill down to Store Business Region', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 7, 0, values, "Step 15: Verify the menu ")
        
        """    16. Select "Drill down to Store Business Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, 'Drill down to Store Business Region')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '14of14records,Page1of1', 'Step 11a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 11c: Verify the report data')
        time.sleep(5)
        
        """    17. Click on North America.    """
        values=['Restore Original', 'Drill up to Store Business Group', 'Drill down to Store Business Sub Region', 'Comments', 'Highlight Value', 'Highlight Row', 'Unhighlight All', 'Filter Cell']
        miscelanousobj.verify_field_menu_items('ITableData0', 0, 0, values, "Step 15: Verify the menu ")
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    18. Click IA > Save As> Type C2226969b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    19. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226964b.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    20. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 14a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
        
        """    21. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
