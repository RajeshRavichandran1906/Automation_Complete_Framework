'''
Created on Jan 18, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251653
Test_Case Name : Create a simple Compound report
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_run, active_miscelaneous, ia_resultarea, ia_styling
from common.lib import utillity

class C2251653_TestClass(BaseTestCase):

    def test_C2251653(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2251653'
        utillobj = utillity.UtillityMethods(self.driver)
        metadata = visualization_metadata.Visualization_Metadata(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        active=active_miscelaneous.Active_Miscelaneous(self.driver)
        iastyling=ia_styling.IA_Style(self.driver)
        
        """
            Step 01 : Launch IA to develop a document.Select 'GGSales' as master file, and change output format as Active report.
            Select Category, Product,Unit Sales to get a report
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','S10071_2', 'mrid', 'mrpass')
        visul_result.wait_for_property("#canvasFrame svg", 1, 40)
        time.sleep(3)
        
        metadata.datatree_field_click('Category',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(4)>td", 1, 15, string_value='Category')
         
        metadata.datatree_field_click('Product',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(5)>td", 1, 15, string_value='Product')
         
        metadata.datatree_field_click('Unit Sales',2,1)
        visul_result.wait_for_property("#queryTreeColumn table>tbody>tr:nth-child(3)>td", 1, 15, string_value='Unit Sales') 
        
        """
            Step 02 : Now select 'Report' > Style' from 'Home' tab
        """
        visul_ribbon.select_ribbon_item('Home', 'style')
        
        """
            Step 03 : Select font type as "COMIC SANS MS", and font size as '14', and select "OK"
        """
        iastyling.set_report_style(font_name='COMIC SANS MS', font_size='14', btn_ok=True)
        time.sleep(5)
        for cell_no in range(1,9) :
            iaresult.verify_report_cell_property('TableChart_1', cell_no, font_name='Comic Sans MS', font_size='14pt', bold=True, font_color='gray8', msg='Step 03.1 : Cell['+str(cell_no)+']')
            
        """
            Step 04 : Save and run the report
        """
        visul_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame()
        visul_result.wait_for_property("#ITableData0 #TCOL_0_C_0 span", 1, 25, string_value='Category')
        
        """
            Step 04.1 : Note that font size and type is respected in output.
        """
        #iarun.create_table_data_set("#ITableData0",Test_Case_ID+'_Dataset_01.xlsx')
        iarun.verify_table_data_set("#ITableData0",Test_Case_ID+'_Dataset_01.xlsx', 'Step 04.1 : Verify report data')
        active.verify_page_summary('0', '10of10records,Page1of1', 'Step 04.2 : Verify data report')
        for row in range(2, 11) :
            for cell in range(1, 4) :
                iarun.verify_table_cell_property('#ITableData0', row, cell, font_name='Comic Sans MS', font_size='14pt', bold=True, font_color='gray8', msg='Step 04.3 : Row['+str(row)+'], Cell['+str(cell)+']')
        
if __name__ == '__main__':
    unittest.main()