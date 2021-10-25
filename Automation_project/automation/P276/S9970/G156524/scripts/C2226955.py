'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226955
TestCase Name = Test Breadcrumbs - Have two hierarchy sorts from different dimensions.
'''
import unittest
from common.pages import visualization_ribbon, ia_run, active_miscelaneous
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from common.lib.global_variables import Global_variables
from common.wftools.report import Report
from common.wftools.visualization import Visualization

class C2226955_TestClass(BaseTestCase):
    
    def test_C2226955(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226955"
        Test_Case_ID = Test_ID+"_"+browser_type
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        report_ = Report(self.driver)
                
        """    1. Open IA_Shell for edit using the API
        http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    """
        
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report_.report_long_timesleep)

        """    2. Click Format tab > Autodrill button     """
#         ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        report_.select_ia_ribbon_item("Format", "auto_drill")
        utillobj.synchronize_with_visble_text("#FormatTab", "Features", report_.report_long_timesleep)
        
        """    3. Click RUN     """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, report_.report_long_timesleep)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 03.00: verify Auto Drill, drill down data set")
        
        """    4. Click on Stereo Systems under North America and select "Drill down to Product Subcategory "    """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",16,2,'Drill down to Product Subcategory')
        utillobj.synchronize_with_visble_text("table[summary='Summary']", "Stereo Systems", report_.report_long_timesleep)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 04.00: Verify Breadcrumb appears at the bottom of the HEADING (if one exists) with name of field you drilled down from")
          
        """    5. Click on North America and select "Drill down to Store Business Sub Region     """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",5,1,'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("table[summary='Summary']", "North America", report_.report_long_timesleep)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 05.00: Verify this breadcrumb (North America) should appear above the previous one (Stereo Systems) Since this is a higher level sort .")
        time.sleep(4)
        
        """    6. Click on Home Theater Systems under East and select "Drill down to Model"    """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",12,2,'Drill down to Model')
        utillobj.synchronize_with_visble_text("table[summary='Summary']", "Home Theater Systems", report_.report_long_timesleep)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx", "Step 06.00: Verify the breadcrumbs should keep their relative positioning (should not flip positions). 2nd breadcrumb will show additional level.")
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    7. Click IA > Save As> Type C2226955a > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.synchronize_with_number_of_element('#IbfsOpenFileDialog7_cbFileName input', 1, report_.report_long_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID+"_a")
        time.sleep(5)
        
        """    8. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226955.fex&tool=report    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID+"_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#TableChart_1", "Sale,Year", report_.report_long_timesleep)
        
        """    9. Click format tab and see Autodrill button is still selected    """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_visble_text("#FormatTab", "Features", report_.report_long_timesleep)
        report_.verify_ribbon_item_is_enabled('format_auto_drill', '09.00')
        
        """    10. Click on HTML output format in status bar and select Active format    """
        ribbonobj.change_output_format_type('active_report', 'status_bar')    
        time.sleep(10)
        
        """    11. Click Run   """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, report_.report_long_timesleep)
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')

        miscelanousobj.verify_page_summary(0, '28of28records,Page1of1', 'Step 11.01: Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11.02: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 11.03: Verify the report data ')
         
        """    12. Click on Stereo Systems under North America and select "Drill down to Product Subcategory "    """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 11, 1, 'Drill down to Product Subcategory')
        utillobj.synchronize_with_visble_text('#ITableData0', 'Stereo Systems', report_.report_long_timesleep)
        miscelanousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 12.01: Verify the Report Records')
        column_list=['Store Business Region', 'Product Subcategory', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 12.02: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx', 'Step 12.03: Verify the report data ')
        
        """    13. Click on North America and select "Drill down to Store Business Sub Region"    """
        if Global_variables.browser_name == 'firefox':
            cell_css = self.driver.find_element_by_css_selector('#ITableData0>tbody>tr:nth-child(4) > td:nth-child(1)')
            utillobj.click_type_using_pyautogui(cell_css, leftClick=True)
            time.sleep(1)
            tooltip_css="div[id^='dt0_I0r0'][style*='block'] span[id^='set']" 
            tooltips=self.driver.find_elements_by_css_selector(tooltip_css)
            utillobj.click_type_using_pyautogui(tooltips[1], leftClick=True)
        else:
            miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0, 0, 'Drill down to Store Business Sub Region')
        
        utillobj.synchronize_with_visble_text('#ITableData0', 'North America', report_.report_long_timesleep)
        miscelanousobj.verify_page_summary(0, '35of35records,Page1of1', 'Step 13.01: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Subcategory', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 13.02: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds07.xlsx', 'Step 13.03: Verify the report data ')
        
        
        """    14. Click on Home Theater Systems under East and select "Drill down to Model"    """
        if Global_variables.browser_name == 'firefox':
            cell_css = self.driver.find_element_by_css_selector('#ITableData0>tbody>tr:nth-child(12) > td:nth-child(2)')
            utillobj.click_type_using_pyautogui(cell_css, leftClick=True)
            time.sleep(1)
            tooltip_css="div[id^='dt0_I0r6'][style*='block'] span[id^='set']" 
            tooltips=self.driver.find_elements_by_css_selector(tooltip_css)
            utillobj.click_type_using_pyautogui(tooltips[2], leftClick=True)
        else:
            miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 6, 1, 'Drill down to Model')
        utillobj.synchronize_with_visble_text('#ITableData0', 'Home Theater Systems', report_.report_long_timesleep)
        miscelanousobj.verify_page_summary(0, '8of8records,Page1of1', 'Step 14.01: Verify the Report Records')
        column_list=['Store Business Sub Region', 'Model', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 14.02: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds08.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds08.xlsx', 'Step 14.03: Verify the report data ')
        time.sleep(4)
        utillobj.switch_to_default_content(1)
        time.sleep(4)
        
        """    15. Click IA > Save As> Type C2226955b > click Save    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.synchronize_with_number_of_element('#IbfsOpenFileDialog7_cbFileName input', 1, report_.report_long_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID+"_b")
        time.sleep(5)
        
        """    16. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()