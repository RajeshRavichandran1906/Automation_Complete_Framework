'''
Created on 13-Mar-2017

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226952
TestCase Name = Test that a non-hierarchy field used as a sorting field will not be active for Drill down
'''
import unittest
from common.pages import visualization_resultarea, visualization_ribbon, visualization_metadata, ia_run, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2223211_TestClass(BaseTestCase):
    
    def test_C2223211(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2223211"
        Test_Case_ID = Test_ID+"_"+browser_type
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
        
        """    2. Double click Brand (Product > Product > Model > Attributes > Brand)    """
        metaobj.datatree_field_click("Brand", 1, 1, 'Sort')
        time.sleep(8)
        
        """    3. Click Format tab > Autodrill button     """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        time.sleep(4)
         
        """    4. Click Run and verify Brand should not have drilldown links    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
#         time.sleep(3)
#         WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[src]')))
#         time.sleep(3)
#         iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", desired_no_of_rows=5)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04a: verify Auto Drill, drill down data set", desired_no_of_rows=5)
        iarun.verify_table_cell_property("table[summary= 'Summary']", 4, 3, text='Denon', font_color = 'gray8', msg='Step 04b ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 11, 3, text='Sony', font_color = 'gray8', msg='Step 04c ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 21, 3, text='LG', font_color = 'gray8', msg='Step 04d ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 28, 3, text='Samsung', font_color = 'gray8', msg='Step 04e ')
        time.sleep(8)
        
        """    5. Click on Accessories under EMEA and select Drill down to Product Subcategory. Verify Brand still does not have drilldown links     """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",3,2,'Drill down to Product Subcategory', "Step 05:")
        time.sleep(10)
#         iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 05a: verify drilldown to Product Subcategory data set")
        iarun.verify_table_cell_property("table[summary= 'Summary']", 5, 3, text='Samsung', font_color = 'gray8', msg='Step 05b ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 9, 3, text='Grado', font_color = 'gray8', msg='Step 05c ')
        iarun.verify_table_cell_property("table[summary= 'Summary']", 13, 3, text='Logitech', font_color = 'gray8', msg='Step 05d ')
        time.sleep(2)
        
        """    6. Click on EMEA and see that Restore Original is in the list of options    """
        expected_tooltip_list = ['Reset', 'Drill down to Store Business Sub Region']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']",5,1, expected_tooltip_list, "Step 06: Restore Original is in the list of options")
        time.sleep(5)
        
        """    7. Click on 2016 and select Restore Original    """
        iarun.select_autolink_tooltip_menu_using_pyautogui("table[summary='Summary']",3,2,'Reset', "Step 07:")
        time.sleep(10)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 07: verify Auto Drill, drill down data set", desired_no_of_rows=5)
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    8. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        time.sleep(20)
        
        """    9. Click Run and verify Brand should not have drilldown links    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        miscelanousobj.verify_page_summary(0, '201of201records,Page1of4', 'Step 09a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Brand', 'Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 09b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 09c: Verify the report data ')
        miscelanousobj.verify_cell_property('ITableData0', 3, 2, 'Logitech', "Step 09d: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 9, 2, 'Canon', "Step 09e: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 17, 2, 'JVC', "Step 09f: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 26, 2, 'Sharp', "Step 09g: ", text_color='gray8')
        time.sleep(4)
        utillobj.switch_to_default_content(pause=2)
        time.sleep(4)
        
        """    10. Click IA > Save As> Type C2223211 > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(4)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    11. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2223211.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        time.sleep(8)
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        time.sleep(8)
         
        """    12. Click format tab and see Autodrill button should be active    """
        ribbonobj.switch_ia_tab('Format')
        time.sleep(4)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 12a: Active_Report - Verify Autodrill button should be active")
        time.sleep(4)
         
        """    13. Click Run    """
        ribbonobj.select_tool_menu_item('menu_run')
        time.sleep(10)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        miscelanousobj.verify_page_summary(0, '201of201records,Page1of4', 'Step 13a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Brand', 'Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 13b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 13c: Verify the report data ')
        miscelanousobj.verify_cell_property('ITableData0', 3, 2, 'Logitech', "Step 13d: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 9, 2, 'Canon', "Step 13e: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 17, 2, 'JVC', "Step 13f: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 26, 2, 'Sharp', "Step 13g: ", text_color='gray8')
        utillobj.switch_to_default_content(pause=2)
        time.sleep(4)
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    14. Run from BIP using API
        http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS9970&BIP_item=C2223211.fex    """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S9970", 'mrid', 'mrpass')
        time.sleep(25)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        miscelanousobj.verify_page_summary(0, '201of201records,Page1of4', 'Step 14a: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Brand', 'Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue','Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds03.xlsx', 'Step 14c: Verify the report data ') 
        miscelanousobj.verify_cell_property('ITableData0', 3, 2, 'Logitech', "Step 14d: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 9, 2, 'Canon', "Step 14e: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 17, 2, 'JVC', "Step 14f: ", text_color='gray8')
        miscelanousobj.verify_cell_property('ITableData0', 26, 2, 'Sharp', "Step 14g: ", text_color='gray8') 
        utillobj.switch_to_default_content(pause=2)
        time.sleep(4)
        
        """    15. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()
    
