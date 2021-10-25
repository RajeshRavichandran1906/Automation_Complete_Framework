'''
Created on Jan 16, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251651
Test_Case Name : Create a simple Compound report
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous
from common.lib import utillity

class C2251651_TestClass(BaseTestCase):

    def test_C2251651(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251651'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        def verify_overloaping(table_css1, table_css2, step_num):
            table1_element=self.driver.find_element_by_css_selector(table_css1)
            table2_element=self.driver.find_element_by_css_selector(table_css2)
            table1_x=utillobj.get_object_screen_coordinate(table1_element, 'right')
            table2_x=utillobj.get_object_screen_coordinate(table2_element, 'left')
            status=True if (table1_x['x']+10)<table2_x['x'] else False
            utillobj.asequal(True, status, 'Step ' + step_num + ' : Verify Report should not over lap')
            
        """
            Step 01 : Launch IA to develop a document.Select 'GGSales' as master file, and change output format as Active report.
            Add Category Product ID,Unit Sales, to develop a report
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','S10071_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#canvasFrame svg", 1, expire_time=65)
        
        metadata.datatree_field_click('Category',2,1)
        utillobj.synchronize_with_number_of_element("div[class^='x']", 2, 15)
         
        metadata.datatree_field_click('Product ID',2,1)
        utillobj.synchronize_with_number_of_element("div[class^='x']", 5, 15)
         
        metadata.datatree_field_click('Unit Sales',2,1)
        utillobj.synchronize_with_number_of_element("div[class^='x']", 8, 15)
        
        """
            Step 02 : Click on blank area in design area, and select Product,State, Dollar Sales to get another report
        """
        container_element=self.driver.find_element_by_id('theCanvas')
        utillobj.click_on_screen(container_element, 'middle', 0)
        
        metadata.datatree_field_click('Product',2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 3, 15)
         
        metadata.datatree_field_click('State',2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 23, 15)
         
        metadata.datatree_field_click('Dollar Sales',2,1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 43, 15)
         
        """
            Step 02.1 : Report should not over lap
        """
        
        visul_ribbon.repositioning_document_component('4', '1.04')
        verify_overloaping('#TableChart_1', '#TableChart_2', '02.1')
        
        """
            Step 03 : Save and run the report
        """
        visul_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame()
        visul_result.wait_for_property("#ITableData1 #TCOL_1_C_0", 1, 30, string_value='Product')
        
        """
            Step 03.1 : Notice that both the report are presented in output .Unnecessary scroll bars should not be generated in output
        """
        #iarun.create_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_01.xlsx')
        iarun.verify_table_data_set('#ITableData0', Test_Case_ID+'_DataSet_01.xlsx', 'Step 03.1 : Verify first table data')
        #iarun.create_table_data_set('#ITableData1', Test_Case_ID+'_DataSet_02.xlsx')
        iarun.verify_table_data_set('#ITableData1', Test_Case_ID+'_DataSet_02.xlsx', 'Step 03.2 : Verify second table data')
        active.verify_page_summary('0', '10of10records,Page1of1', 'Step 03.3 : Verify first table page summary')
        active.verify_page_summary('1', '107of107records,Page1of2', 'Step 03.4 : Verify second table page summary')
        table1_scroll=self.driver.find_element_by_id('MAINTABLE_0').value_of_css_property('overflow').lower()
        table2_scroll=self.driver.find_element_by_id('MAINTABLE_1').value_of_css_property('overflow').lower()
        scroll_status=True if table1_scroll!='auto' and table2_scroll!='auto' else False
        utillobj.asequal(True, scroll_status, 'Step 03.5 : Verify Unnecessary scroll bars should not be generated in output')
        verify_overloaping('#MAINTABLE_0', '#MAINTABLE_1', '03.6')
        
if __name__ == '__main__':
    unittest.main()