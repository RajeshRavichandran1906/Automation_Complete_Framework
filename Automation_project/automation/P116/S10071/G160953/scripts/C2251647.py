'''
Created on 18-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251647
TestCase Name = Verify that user can insert a report in a document
'''
import unittest
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, active_miscelaneous
from common.lib.basetestcase import BaseTestCase

class C2251647_TestClass(BaseTestCase):

    def test_C2251647(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2251647'
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """ Step 1: Launch IA to develop a Document.
                    Select 'ggsales' as master file, and change output format as Active report.
                    Select Category, Product ID, Region and Unit Sales
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 65)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
        
        vis_metadata.datatree_field_click('Category', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 25)
        
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 25)
        
        vis_metadata.datatree_field_click('Region', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 13, 25)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 21, 25)
                
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 4, 0, 0, test_case_id + '_Ds01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 4, 0, 0, test_case_id + '_Ds01.xlsx', "Step 1.1: Verify Category, Product ID, Region, Unit Sales report.")
        
        """ Step 2: Click Insert tab and select Report
        """
        """ Step 3: On a canvas report box will be displayed to add a report. Drag it to the right of original report.
        """
        vis_ribbon.select_ribbon_item("Insert", "Report")
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_1', 210, 0)
        
        """ Step 4: Select Product ID, State and Unit Sales fields to get a report.
        """
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 3, 20)
        
        vis_metadata.datatree_field_click('State', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 23, 20)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 43, 20)
        
#         ia_resultobj.create_across_report_data_set('TableChart_2', 1, 3, 0, 0, test_case_id + '_Ds02.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_2', 1, 3, 0, 0, test_case_id + '_Ds02.xlsx', "Step 4: Verify Product ID, State, Unit Sales report.")
        
        """ Step 5: Run the document.
                    Notice that both the report are presented in output.
                    Unnecessary scroll bars should not be generated in output.
                    Reports should not overlap.
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']",1,45)
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'Category', 30)
        active_mis_obj.verify_page_summary(0, '39of39records,Page1of1', "Step 5: Verify page summary of Category, Product ID, Region, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds03.xlsx', " Step 5.1: Verify Category, Product, Unit Sales report.")
        active_mis_obj.verify_page_summary(1, '107of107records,Page1of2', "Step 5.2: Verify page summary of Product ID, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData1', 'I1r', test_case_id + '_Ds04.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', test_case_id + '_Ds04.xlsx', " Step 5.3: Verify Product ID, State, Dollar Sales report.")
        elem = self.driver.find_element_by_css_selector('#IWindowBody0')
        talbe1_x_plus_width = utillobj.get_object_screen_coordinate(elem, coordinate_type='top_right')
        print(talbe1_x_plus_width)
        elem1 = self.driver.find_element_by_css_selector('#IWindowBody1')
        table2_x_location = utillobj.get_object_screen_coordinate(elem1, coordinate_type='start')
        print(table2_x_location)
        table2_status = True if int(table2_x_location['x']) > int(talbe1_x_plus_width['x']) + 10 else False
        utillobj.asequal(True, table2_status, "Step 5.4: Verify reports should not overlapped")
        utillobj.switch_to_default_content(pause=1)
       
        
        
if __name__ == '__main__':
    unittest.main()