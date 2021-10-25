'''
Created on Jan18, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2308069
TestCase Name = AHTML: Pagination -vertical scrollbar missing bottom arrow (ACT-562)
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,ia_run
from common.lib import utillity


class C2308069_TestClass(BaseTestCase):

    def test_C2308069(self):
        Test_Case_ID = '2308069'
        """
        Step 01: Execute attached Multipage.fex from IA.
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        active_misobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        utillobj.active_run_fex_api_login('Multipage.fex','S10071_1','mrid','mrpass')
        utillobj.synchronize_with_number_of_element("#ITableData0 ", 1, 10)
        
        """
        Step02: Verify the layout page displayed with multipages
        """
        def verify(r1,r1_sum,r1_col,step):
            #1st Report
            active_misobj.verify_page_summary(r1,r1_sum,step+'.1a: Verify the Report Heading of 1st Report')
            active_misobj.verify_column_heading('ITableData'+str(r1), r1_col, step+'.1b: Verify the column heading')
#             ia_runobj.create_table_data_set('#ITableData'+str(r1), 'C2308069_Ds'+step+'.1.xlsx')
            ia_runobj.verify_table_data_set('#ITableData'+str(r1), 'C2308069_Ds'+step+'.1.xlsx', step+'.1c: Verify data.')
        
        ia_runobj.verify_active_document_page_layout_menu("table[id='iLayTB$']", ['Layouts','Page 1','Page 2'], "Step02: Verify the layout page displayed with multipages")
        r1_col=['Category','Product','Unit Sales']
        verify(0,'10of10records,Page1of1',r1_col,"Step02")
         
        """
        Step03: Click page 2 and check Pagination -vertical scrollbar is displaying properly.
        """
        ob=self.driver.find_element_by_css_selector("form div[id='iLay$2']")
        utillobj.click_on_screen(ob, 'middle', click_type=0)
        utillobj.synchronize_with_number_of_element("#ITableData1 ", 1, 10)
        r1_col=['Category','Product','Region','Unit Sales']
        verify(1,'39of39records,Page1of1',r1_col,"Step03")
        
        page1_ele=self.driver.find_element_by_css_selector("#IWindowBody0")
        page1=utillobj.get_object_screen_coordinate(page1_ele, coordinate_type='bottom_middle')
        page2_ele=self.driver.find_element_by_css_selector("#IWindowBody1")
        page2=utillobj.get_object_screen_coordinate(page2_ele, coordinate_type='bottom_middle')
        utillobj.as_GE(int(page2['y']),int(page1['y']),"Step03.2: Verify Page2 Pagination -vertical scrollbar is displaying properly")
        
if __name__ == '__main__':
    unittest.main()


