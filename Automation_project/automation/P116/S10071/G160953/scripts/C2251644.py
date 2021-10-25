'''
Created on 16-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251644
TestCase Name = Verify that active Dashboard reports does not overlap each other
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, active_miscelaneous
from common.lib.basetestcase import BaseTestCase

class C2251644_TestClass(BaseTestCase):

    def test_C2251644(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2251644'
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """ Step 1: Launch IA to develop an Active document.
                    Select 'GGSales' as master file, and change output format as Active report.
                    Select Category, Product, Unit Sales to get a report.
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 65)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'Category', 25)
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(5)"
        utillobj.synchronize_with_visble_text(element_css, 'Product', 25)
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#TableChart_1"
        utillobj.synchronize_with_visble_text(element_css, 'CategoryProductUnitSalesCoffeeCapuccino189217Espresso293544', 25)
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 3, 0, 0, test_case_id + '_Ds01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 3, 0, 0, test_case_id + '_Ds01.xlsx', "Step 1.1: Verify Category, Product, Unit Sales report.")
          
        """ Step 2: Click on blank area in design area, and select Product ID, State, Dollar Sales to get another report. Drag another report next to the first one.
        """
        parent_elem = self.driver.find_element_by_css_selector("#TableChart_1")
        utillobj.click_on_screen(parent_elem, 'right', click_type=0, x_offset=90)
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(5)"
        utillobj.synchronize_with_visble_text(element_css, 'ProductID', 25)
        vis_metadata.datatree_field_click('State', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(6)"
        utillobj.synchronize_with_visble_text(element_css, 'State', 25)
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        element_css="#queryTreeColumn tr:nth-child(4)"
        utillobj.synchronize_with_visble_text(element_css, 'DollarSales', 2)
#         ia_resultobj.create_across_report_data_set('TableChart_2', 2, 3, 0, 0, test_case_id + '_Ds02.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_2', 2, 3, 0, 0, test_case_id + '_Ds02.xlsx', "Step 2: Verify Product ID, State, Dollar Sales  report.")
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#TableChart_1', 250, 0)
        time.sleep(2)
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        
        """ Step 3: Run the dashboard and verify that both the report are presented in output.
                    Make sure unnecessary scroll bars should not be generated in output.
                    Reports should not be overlapped.
        """
        utillobj.switch_to_frame(pause=3)
        active_mis_obj.verify_page_summary(0, '10of10records,Page1of1', "Step 3: Verify page summary of Category, Product, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds03.xlsx', " Step 3.1: Verify Category, Product, Unit Sales report.")
        active_mis_obj.verify_page_summary(1, '107of107records,Page1of2', "Step 3.2: Verify page summary of Product ID, State, Dollar Sales report.")
#         utillobj.create_data_set('ITableData1', 'I1r', test_case_id + '_Ds04.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', test_case_id + '_Ds04.xlsx', " Step 3.3: Verify Product ID, State, Dollar Sales report.")
        elem = self.driver.find_element_by_css_selector('#IWindowBody0')
        talbe1_x_plus_width = utillobj.get_object_screen_coordinate(elem, coordinate_type='top_right')
        elem1 = self.driver.find_element_by_css_selector('#IWindowBody1')
        table2_x_location = utillobj.get_object_screen_coordinate(elem1, coordinate_type='start')
        table2_status = True if int(table2_x_location['x']) > int(talbe1_x_plus_width['x']) + 10 else False
        utillobj.asequal(True, table2_status, "Step 3.4: Verify reports should not overlapped")
        utillobj.switch_to_default_content(pause=1)
        elem = self.driver.find_element_by_css_selector("#theCanvas")
        utillobj.take_screenshot(elem, test_case_id+"_Actual_Step_3.5")
        time.sleep(5)
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(test_case_id)
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()