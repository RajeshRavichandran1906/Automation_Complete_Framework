'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/9970
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2230843
TestCase Name = Test that Auto Drill works with Table of Contents option
'''
import unittest, time
from common.pages import visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous, visualization_metadata, metadata
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2197808_TestClass(BaseTestCase):
    
    def test_C2197808(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
        browser_type=utillobj.parseinitfile('browser')
        Test_ID="C2197808"
        Test_Case_ID = Test_ID+"_"+browser_type
        driver = self.driver
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        metaobj=visualization_metadata.Visualization_Metadata(self.driver)
        metadata0jb = metadata.MetaData(self.driver)
          
        """    
            Step 01 : Open a new report with baseapp/emp_data.mas   
        """
        utillobj.infoassist_api_login('report','baseapp/emp_data','P276/S9976', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn .bi-tree-view-table>tbody>tr:nth-child(2)", 'Sum', expire_time=80)
        
        """  
            Step 02 : Double click on Annual Salary and Org Department (Emp_data > ORG_D > Org Department) from data pane    
        """
        metaobj.datatree_field_click("Emp_data->Annual Salary", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn .bi-tree-view-table>tbody>tr:nth-child(3)", 'Annual Salary', expire_time=30)
        
        metadata0jb.collapse_data_field_section('Measure Groups')
        time.sleep(2)
        
        metaobj.datatree_field_click("Emp_data->ORG_D->Org Department", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn .bi-tree-view-table>tbody>tr:nth-child(5)", 'Org Department', expire_time=30)
       
        coln_list = ['Org Department', 'Annual Salary']
        resultobj.verify_report_titles_on_preview(2, 2, "TableChart_1", coln_list, "Step 02.1: Verify Canvas column titles")
        
        """    
            Step 03 :Click Format tab > Autodrill button     
        """
        ribbonobj.select_ribbon_item("Format", "Auto_Drill")
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=10)
        
        """    
            Step 04 : Click RUN     
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(1)>td:nth-child(1)", 'Org Department', expire_time=50)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 04a: Verify dataset", desired_no_of_rows=5)
        
        """    
            Step 05 : Click on the value ** "epartment of Transportation** > Select Drill down to Org Division    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",3,1,'Drill down to Org Division')
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:nth-child(1)", 'Org Division', expire_time=30)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds02.xlsx", "Step 05a: Verify Drill down to **epartment of Transportation** data set")
        
        """  
            Step 06 : Now click on the value Transit Gaithersburg Ride On > Select Restore Original    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",4,1,'Restore Original')
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(1)>td:nth-child(1)", 'Org Department', expire_time=50)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 06a: Verify Initial dataset", desired_no_of_rows=5)
               
        """ 
            Step 07 : Click on the record BB"Department of Transportation > Select Drill down to Org Division.    
        """
        cell_css="table[summary='Summary'] > tbody > tr:nth-child(59) > td:nth-child(1) > a"
        obj_cell_css=driver.find_element_by_css_selector(cell_css)
        driver.execute_script("return arguments[0].scrollIntoView();",obj_cell_css)
        time.sleep(2)
        
        obj_cell_css=driver.find_element_by_css_selector(cell_css)
        obj_cell_css.click()
        drilldown_css = "[id='my_tooltip_id'][style*='visible'] li"
        utillobj.synchronize_with_number_of_element(drilldown_css, 1, expire_time=5)
        drilldown = self.driver.find_element_by_css_selector(drilldown_css)
        drilldown.click()
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:nth-child(1)", 'Org Division', expire_time=30)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds03.xlsx", 'Step 07a: Verify Drill down to **BB"Department of Transportation** data set')
        
        """    
            Step 08 : Now click on the value Transit Gaithersburg Ride On > Select Restore Original    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",4,1,'Restore Original')
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(1)>td:nth-child(1)", 'Org Department', expire_time=30)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds01.xlsx", "Step 08a: Verify Initial dataset", desired_no_of_rows=5)
         
        """    
            Step 09 : Click on the value #epartment of Environmental Protection > Select Drill down to Org Division    
        """
        iarun.select_report_autolink_tooltip("table[summary='Summary']",4,1,'Drill down to Org Division')
        utillobj.synchronize_with_visble_text("table[summary= 'Summary']>tbody>tr:nth-child(3)>td:nth-child(1)", 'Org Division', expire_time=30)
        iarun.verify_table_data_set("table[summary= 'Summary']", Test_ID+"_Ds04.xlsx", "Step 09a: Verify Drill down to **#epartment of Environmental Protection** data set")
    
        utillobj.switch_to_default_content(1)
        
        """    
            Step 10 Click IA > Save As> Type C2197808a > click Save 
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID + "_a")
        
        """    
            Step 11 : Close the IA+ window    
        """
        utillobj.infoassist_api_logout()
        
        """    
            12. Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2197808a.fex&tool=report    
        """
        utillobj.infoassist_api_edit(Test_Case_ID + "_a", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn .bi-tree-view-table>tbody>tr:nth-child(5)", 'Org Department', expire_time=120)
         
        """    
            Step 13 : Click format tab and Verify Autodrill button is still selected   
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=10)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 13a: Verify Autodrill button should be active")
    
        """    
            Step 14 : Click on HTML output format in status bar and select Active format 
        """
        ribbonobj.change_output_format_type('active_report', 'status_bar')
        utillobj.synchronize_with_visble_text("#sbpOutputFormat", 'Active Report', expire_time=40)
        time.sleep(5)
        
        """    
            Step 15 : Click RUN    
        """
        ribbonobj.select_tool_menu_item('menu_run')
        utillobj.switch_to_frame(1)
        utillobj.switch_to_frame(pause=3,frame_css='iframe[src]')
        
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:nth-child(1)>td:nth-child(1)", 'Org Department', expire_time=30)
        miscelanousobj.verify_page_summary(0, '131of131records,Page1of3', 'Step 15a: Verify the Report Records')
        column_list=['Org Department', 'Annual Salary']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 15b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', desired_no_of_rows=5)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 15c: Verify the report data', desired_no_of_rows=5)
       
        """    
            Step 16 : Click on the value ** "epartment of Transportation** > Select Drill down to Org Divisio
        """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 1,0, 'Drill down to Org Division')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:nth-child(2)>td:nth-child(1)", 'Org Division', expire_time=30)
        
        miscelanousobj.verify_page_summary(0, '1of1records,Page1of1', 'Step 16a: Verify the Report Records')
        column_list=['Org Division', 'Annual Salary']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 16b: Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds06.xlsx', 'Step 16c: Verify the report data')
        
        """    
            Step 17 : Now click on the value Transit Gaithersburg Ride On > Select Restore Original    
        """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Restore Original')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:nth-child(1)>td:nth-child(1)", 'Org Department', expire_time=30)
        
        miscelanousobj.verify_page_summary(0, '131of131records,Page1of3', 'Step 17a: Verify the Report Records')
        column_list=['Org Department', 'Annual Salary']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 17b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 17c: Verify the report data', desired_no_of_rows=5)
        
        """    
            Step 18 : Click on the record BB"Department of Transportation > Select Drill down to Org Division.    
        """
        cell_css="#ITableData0 tr[id*='r55.'] td[id$='C0']"
        obj_cell_css=driver.find_element_by_css_selector(cell_css)
        driver.execute_script("return arguments[0].scrollIntoView();",obj_cell_css)
        time.sleep(1)
        menu_css = "div[id^='dt0_I0r55'][style*='block'] span[id^='set']"
        obj_cell_css=driver.find_element_by_css_selector(cell_css)
        obj_cell_css.click()
        utillobj.synchronize_with_number_of_element("div[id^='dt0_I0r55'][style*='block']", 1, expire_time=8)
        menu = self.driver.find_elements_by_css_selector(menu_css)[0]
        menu.click()
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:nth-child(2)>td:nth-child(1)", 'Org Division', expire_time=30)
        miscelanousobj.verify_page_summary(0, '1of1records,Page1of1', 'Step 18a: Verify the Report Records')
        column_list=['Org Division', 'Annual Salary']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 18b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds07.xlsx', 'Step 18c: Verify the report data')
        
        """    
            Step 19 : Now click on the value Transit Gaithersburg Ride On > Select Restore Original    
        """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 0,0, 'Restore Original')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:nth-child(1)>td:nth-child(1)", 'Org Department', expire_time=30)
        
        miscelanousobj.verify_page_summary(0, '131of131records,Page1of3', 'Step 19a: Verify the Report Records')
        column_list=['Org Department', 'Annual Salary']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 19b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds05.xlsx', 'Step 19c: Verify the report data', desired_no_of_rows=5)
       
        """    
            Step 20 : Click on the value #epartment of Environmental Protection > Select Drill down to Org Division.
        """
        miscelanousobj.select_field_menu_items_using_pyautogui('ITableData0', 2,0, 'Drill down to Org Division')
        utillobj.synchronize_with_visble_text("#ITableData0>tbody>tr:nth-child(2)>td:nth-child(1)", 'Org Division', expire_time=30)
        
        miscelanousobj.verify_page_summary(0, '1of1records,Page1of1', 'Step 20a: Verify the Report Records')
        column_list=['Org Division', 'Annual Salary']
        miscelanousobj.verify_column_heading('ITableData0', column_list, 'Step 20b: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_ID+'_Ds08.xlsx', 'Step 20c: Verify the report data')
       
        utillobj.switch_to_default_content(1)
        
        """    
            Step 21 : Click IA > Save As> Type C2197808b > click Save   
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID + "_b")
        
        """    
            Step 22. Close the IA+ Window    
        """
        utillobj.infoassist_api_logout()
        
        """    
            Step 23 : Open saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS9970%2FC2197808b.fex&tool=report    
        """
        utillobj.infoassist_api_edit(Test_Case_ID + "_b", 'report', 'S9970', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn .bi-tree-view-table>tbody>tr:nth-child(5)", 'Org Department', expire_time=30)
         
        """    
            Step 24 : Click format tab and see Autodrill button should be active    
        """
        ribbonobj.switch_ia_tab('Format')
        utillobj.synchronize_with_number_of_element("[id='FormatAutoDrill'][class*='checked']", 1, expire_time=10)
        disabled =self.driver.find_element_by_css_selector("#FormatAutoDrill").get_attribute('disabled')                
        utillobj.asequal(disabled, None, "Step 24a: Verify Autodrill button should be active")
        
        """    
            Step : 25. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    
        """
        
if __name__ == '__main__':
    unittest.main()
    