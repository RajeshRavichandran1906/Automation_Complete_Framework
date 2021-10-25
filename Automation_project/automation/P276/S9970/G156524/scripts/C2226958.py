'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226958
TestCase Name = Test that Auto Drill retains Data Bars option
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, visualization_metadata, ia_resultarea, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2226958_TestClass(BaseTestCase):
    def test_C2226958(self):
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226958"
        Test_Case_ID = Test_ID+"_"+browser_type
        #driver = self.driver
        #driver.implicitly_wait(60)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(15)
        
        """    2. Right click on "Sale,Year" from ACROSS in query pane and select Delete    """
        metaobj.querytree_field_click("Sale,Year", 1, 1, "Delete")
        time.sleep(15) 
        
        """    3. Click on "Quantity Sold" in the canvas    """
        metaobj.querytree_field_click("Quantity,Sold", 1)
        time.sleep(10)
        
        """    4. Select Data Bars under the display category on the Ribbon    """
        ribbonobj.select_ribbon_item('Field', 'databars')
        time.sleep(3)
        
        """    5. Right click on Revenue in the Query panel. Select More > Data Bars > On    """
        metaobj.querytree_field_click("Revenue", 1, 1, "More", "Data Bars","On")
        time.sleep(10)
        ia_resultobj.verify_live_preview_data_bars('TableChart_1', 'Step 4: Verify Data Bars Display in Live Preview', expected_number_of_bars=56, index=7, color='light_gray')
        
        """    6. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(15)
        
        """    7. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=10)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 07a: verify Auto Drill, drill down data set", desired_no_of_rows=10)
        iarun.verify_table_cell_data_bars("table[summary='Summary']", expected_number_of_bars=41, expected_color='light_gray', expected_color_index=1, msg='Step 07b:')
        
        """    8. Click on North America and select "Drill down to Store Business Sub Region"   """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",11,1,'Drill down to Store Business Sub Region', "Step 08")
        time.sleep(10)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", desired_no_of_rows=10)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 08a: Verify Drill down to Sale Year/Quarter Report", desired_no_of_rows=10)
        iarun.verify_table_cell_data_bars("table[summary='Summary']", expected_number_of_bars=88, expected_color='light_gray', expected_color_index=1, msg='Step 08b:')
        time.sleep(4)
        
        """    9. Click on Stereo Systems under West and select "drill down to Product Subcategory"    """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",16,2,'Drill down to Product Subcategory', "Step 09")
        time.sleep(10)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 09a: Verify Drill down to Sale Year/Month Report")
        iarun.verify_table_cell_data_bars("table[summary='Summary']", expected_number_of_bars=10, expected_color='light_gray', expected_color_index=1, msg='Step 08b:')
        time.sleep(8)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    10. Click IA > Save As> Type C2226958 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        time.sleep(5)
        
        """    11. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226958a.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10) 
        
        """    12. Click on the Format tab. Verify that Auto Drill is still selected.    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(10)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 12a: Active_Report - Verify Autodrill button is still selected")
        time.sleep(4)
        
        """    13. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(20)
        
        """    14. Click Run    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(1)
        time.sleep(3)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        time.sleep(3)
        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 14a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', '', 'Revenue', '', 'TOTAL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 14c: Verify the report data ')
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 2, 'light_gray', 'Step 14d: Verify Data bars for Quantity,Sold added', desired_no_of_rows=15)
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'light_gray', 'Step 14e: Verify Data bars for Revenue added', desired_no_of_rows=15) 
        
        """    15. Click on North America and select "Drill down to Store Business Sub Region"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, 'Drill down to Store Business Sub Region')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '56of56records,Page1of1', 'Step 15a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', '', 'Revenue', '', 'TOTAL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 15b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 15c: Verify the report data ')
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 2, 'light_gray', 'Step 15d: Verify Data bars for Quantity,Sold added')
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'light_gray', 'Step 15e: Verify Data bars for Revenue added') 
        
        """    16. Click on Stereo Systems under West and select "drill down to Product Subcategory"    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 18, 1, 'Drill down to Product Subcategory')
        time.sleep(10)
        miscelanousobj.verify_page_summary(0, '4of4records,Page1of1', 'Step 16a: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Subcategory', 'Quantity Sold', '', 'Revenue', '', 'TOTAL']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 16b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx', 'Step 16c: Verify the report data ')
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 2, 'light_gray', 'Step 16d: Verify Data bars for Quantity,Sold added')
        miscelanousobj.verify_visualization('ITableData0', 'I0r', 4, 'light_gray', 'Step 16e: Verify Data bars for Revenue added')
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    17. Click IA > Save As > Type C2226958b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        time.sleep(5)
        
        """    18. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226958b.fex&tool=Report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(15)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(10)
        
        """    19. Click on the Format tab. Verify that Auto Drill is still selected.    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(10)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 19a: Active_Report - Verify Autodrill button is still selected")
        time.sleep(4)
        
        """    20. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
