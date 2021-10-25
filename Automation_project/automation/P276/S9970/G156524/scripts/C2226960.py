'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2226960
TestCase Name = Test that Auto Drill retains Data Bars option
'''
import unittest
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_ribbon, ia_run, visualization_metadata, active_miscelaneous

class C2226960_TestClass(BaseTestCase):
    
    def test_C2226960(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2226960"
        Test_Case_ID = Test_ID+"_"+browser_type
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    
            STEP 01 : Open IA_Shell for edit using the API
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FIA-Shell.fex&tool=Report    
        """
        utillobj.infoassist_api_edit("IA-Shell", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("div[id^='BiDockPanel'] div[class^='x']", 'Sale,Year', 200)
        
        """    
            STEP 02 : Right click on Store Business Region under By and select Sort > Limit > Custom. Enter 2 and click OK    
        """
        metaobj.querytree_field_click("Store,Business,Region", 1, 1, "Sort","Limit","Custom")
        utillobj.synchronize_with_visble_text("div[id^='BiDialog'] .bi-window-caption", 'Edit Limit', 10, pause_time=2)
        
        edit_title_css="div[id^='BiDialog'][tabindex='0']"
        edit_title_obj=self.driver.find_element_by_css_selector(edit_title_css)
        utillobj.set_text_field_using_actionchains(edit_title_obj.find_element_by_css_selector("input"), '2')
        utillobj.click_dialog_button(edit_title_css,"OK")
        utillobj.synchronize_with_number_of_element("div[id^='BiDockPanel'] div[class^='x']", 316, 20, pause_time=2)
        
        """    
            STEP 03 : Click Format tab > Autodrill button     
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        utillobj.synchronize_with_number_of_element("div[id='FormatAutoDrill'][class*='checked']", 1, 10, pause_time=3)
        
        """    
            STEP 4 : Click RUN     
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("iframe[id^='ReportIframe']", 1, 10, pause_time=5)
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:first-child>td:first-child", 'Sale,Year', 120)
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 04.01 : verify Auto Drill, drill down data set")
        
        """    
            STEP 05 : Click on North America and select "Drill down to Store Business Sub Region"   
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",12,1,'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("table[summary]>tbody>tr:first-child>td:first-child a", 'Home', 120)
        
        #iarun.create_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", "Step 05.01 : Verify Drill down to Sale Year/Quarter Report")
        utillobj.switch_to_default_content(1)
        
        """    
            STEP 06 : Click IA > Save As> Type C2226960 > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        
        """     
            STEP 07 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226960a.fex&tool=report    
        """
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("div[id^='BiDockPanel'] div[class^='x']", 'Sale,Year', 200) 
        
        """    
            STEP 08 : Click on the Format tab. Verify that Auto Drill is still selected.    
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("div[id='FormatAutoDrill'][class*='checked']", 1, 10, pause_time=3)
        
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 08.01 : Active_Report - Verify Autodrill button is still selected")
        
        """    
            STEP 09 : Click on HTML output format in status bar and select Active format    
        """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        utillobj.synchronize_with_visble_text("#sbpOutputFormat .bi-button-label", 'ActiveReport', 20)
        
        """    
            STEP 10 : Click Run    
        """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.synchronize_with_number_of_element("iframe[id^='ReportIframe']", 1, 10, pause_time=8)
        
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:first-child>td:first-child", 'Sale,Year', 120)
        
        miscelanousobj.verify_page_summary(0, '14of14records,Page1of1', 'Step 10.01 : Verify the Report Records')
        column_list=['Store Business Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 10.02 : Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds04.xlsx', 'Step 10.03 : Verify the report data ')
        
        """    
            STEP 11 : Click on North America and select "Drill down to Store Business Sub Region"    
        """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 7, 0, 'Drill down to Store Business Sub Region')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:first-child>td:first-child a", 'Home', 60)
        
        miscelanousobj.verify_page_summary(0, '14of14records,Page1of1', 'Step 11.01 : Verify the Report Records')
        column_list=['Store Business Sub Region', 'Product Category', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue', 'Quantity Sold', 'Revenue']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 11.02 : Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 11.03 : Verify the report data ')
        utillobj.switch_to_default_content(1)
        
        """    
            STEP 12 : Click IA > Save As > Type C2226960b > click Save    
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        
        """    
            STEP 13 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2226960b.fex&tool=Report    
        """
        utillobj.infoassist_api_logout()
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("div[id^='BiDockPanel'] div[class^='x']", 'Sale,Year', 200)
        
        """    
            STEP 14 : Click on the Format tab. Verify that Auto Drill is still selected.    
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("div[id='FormatAutoDrill'][class*='checked']", 1, 20, pause_time=3)
        
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 14.01 : Verify that Auto Drill is still selected")
        
        """    
            STEP 15 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()
    