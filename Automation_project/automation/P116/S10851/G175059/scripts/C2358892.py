'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2358892
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, ia_resultarea, visualization_ribbon, active_miscelaneous
from common.lib import utillity

class C2358892_TestClass(BaseTestCase):

    def test_C2358892(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2358892'
        driver = self.driver
        driver.implicitly_wait(35)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """    1. Launch IA to develop a Document.
        Select 'GGSales' as master file, and change output format as Active report/APDF
        Select 'Chart' from home tab and choose Category, Product, and Unit Sales to get a chart    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10851_1', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#resultAreaResourcesSplitPane", "Category", metaobj.home_page_long_timesleep)
        
        metaobj.datatree_field_click("Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 2, expire_time=10)
        time.sleep(8)    
        metaobj.datatree_field_click("Product", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 5, expire_time=10)
        time.sleep(8)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 8, expire_time=10)
        time.sleep(8)
        
        coln_list=["Category", "Product", "Unit Sales"]
        
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 1.2a: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1 ', 2, 3, 'C2358892_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 3, 'C2358892_Ds01.xlsx', 'Step 1.2b: Verify Preview report dataset')
        
        
        """    2. Select 'Insert > New chart' and drag a area in design view to create a graph    """
        
        ribbonobj.select_ribbon_item("Insert", "Chart")
        time.sleep(5)
        
        resultobj.wait_for_property("#TableChart_2", 1, expire_time=20)
        
        ribbonobj.repositioning_document_component('5', '1')
        
        """    3. Select 'PRODUCT to Xaxis', and 'UNITSALES to Measure(Sum) to get a graph.    """
        
        metaobj.datatree_field_click("Product", 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        time.sleep(8)
        
        """    3.1. Save and close IA, and Run the report.    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        utillobj.infoassist_api_logout()
        
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", 'S10851_1', mrid='mrid', mrpass='mrpass')
        
        """    3.2. Report and JSCHART Chart should be presented without any error message.    """
        msg="Step 3"
        miscobj.verify_arChartToolbar("MAINTABLE_1",['More Options','Advanced Chart','Original Chart'],"Step 03a: Verify Chart toolbar")
        x_val_list=['Biscotti', 'Capuccino', 'Coffee Grin...', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        y_val_list=['0', '200K', '400K', '600K', '800K', '1,000K']
        resultobj.verify_riser_chart_XY_labels('MAINTABLE_1', x_val_list, y_val_list, msg + ".b")
        expected_tooltip=['Product:  Coffee Grinder', 'Unit Sales:  186534', 'Filter Chart', 'Exclude from Chart']
        miscobj.verify_active_chart_tooltip('MAINTABLE_1', 'riser!s0!g2!mbar', expected_tooltip, msg + ".c: verify the chart tooltip with fill color")
        xaxis_value="Product"
        yaxis_value="Unit Sales"
        resultobj.verify_xaxis_title("MAINTABLE_1", xaxis_value, "Step 03d(i): Verify X-Axis Title")
        resultobj.verify_yaxis_title("MAINTABLE_1", yaxis_value, "Step 03d(ii): Verify Y-Axis Title")
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g0!mbar!", "bar_blue1", "Step 03e: Verify bar color")
        
        """     Verifying the Report    """
        miscobj.verify_page_summary(0, '10of10records,Page1of1', 'Step 03e(1): Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 03f(1): Verify the column heading')
        #utillobj.create_data_set('ITableData0','I0r','C2358892_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2358892_Ds02.xlsx', 'Step 03.1f: Verify that report for between filter')
        
        
        
        
        ele=driver.find_element_by_css_selector("#MAINTABLE_1")
        utillobj.take_screenshot(ele,Test_Case_ID+'_Actual_Step03_', image_type='actual',x=0, y=20, w=-250, h=-120)
        time.sleep(1)
        
if __name__ == '__main__':
    unittest.main()