'''
Created on Jul 6, 2017

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7074
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2204941
TestCase Name = Verify Default riser color for chart from report is displayed as blue
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous,visualization_resultarea

class C2204941_TestClass(BaseTestCase):

    def test_C2204941(self):
        
        """
        Test case objects
        """
        utillobj = utillity.UtillityMethods(self.driver)
#         miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        

        """
        1. Run C46049.fex
        """
        utillobj.active_run_fex_api_login("C46049.fex", "S7074", 'mrid', 'mrpass')
        miscelaneousobj.verify_page_summary(0, '5of5records,Page1of1', 'Step 01.1: Execute the c46049.fex')
        column_list=['COUNTRY','SALES']
        miscelaneousobj.verify_column_heading('ITableData0', column_list, 'Step 01.2: Verify the column heading')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C46049.xlsx','Step 01.3: Expect to see the  Active Report')
#         utillobj.create_data_set('ITableData0', 'I0r', 'C46049.xlsx')
        
        """
        Step 02: From the Active drop down control for SALES, select Chart, then Column.
        """
        values=['Group By (X)', 'COUNTRY', 'SALES']
        miscelaneousobj.verify_menu_items('ITableData0', 1, 'Chart->Column', values, 'Step 02: Verify Group By (Columns) list are displayed', all_items='yes')
        
        """
        Step 03: Click COUNTRY as the Group by field. 
        """
        miscelaneousobj.select_menu_items("ITableData0", "1", "Chart", "Column", "COUNTRY")
        time.sleep(4)
        self.driver.set_page_load_timeout(100)
        parent_css="#wall1 g.bevels rect[class^='riser']"
        utillobj.synchronize_with_number_of_element(parent_css, 4, 20)
        expected_xval_list=['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        expected_yval_list=['0', '20K', '40K', '60K', '80K', '100K']
        result_obj.verify_riser_chart_XY_labels('wall1', expected_xval_list, expected_yval_list, 'Step 03.1: Verify XY labels')
        result_obj.verify_number_of_riser('wall1', 1, 5, 'Step 03.2: Verify number of risers')
        utillobj.verify_chart_color("wall1", "riser!s0!g3!mbar!", "cerulean_blue", "Step 03.3: Verify bar color")
        time.sleep(5)
        expected_legend_list=['SALES']
        result_obj.verify_riser_legends('wall1', expected_legend_list, 'Step 03.4: Verify Legend Title')
        miscelaneousobj.verify_chart_title('wall1', 'SALES by COUNTRY', 'Step 03.5: Verify Chart Title')
        miscelaneousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 03.6: Verify Chart toolbar")
        miscelaneousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 03.7: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelaneousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 03.8: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        

if __name__ == '__main__':
    unittest.main()