'''
Created on 23-Jan-2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251704
TestCase Name = Report and Chart with JSCHART(HTML5) ARGRAPHENGINE in a Document
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, active_miscelaneous,visualization_resultarea,ia_run
from common.lib.basetestcase import BaseTestCase

class C2251704_TestClass(BaseTestCase):

    def test_C2251704(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251704'
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_resobj=visualization_resultarea.Visualization_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        
        """ Step 1: Launch IA to develop a new Document.
            Select 'GGSales' as master file, and change output format as Active report/APDF. 
            Select Category, Product,Unit Sales to get a report
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 65)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
           
        vis_metadata.datatree_field_click('Category', 2, 1)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 2, 60)
           
        vis_metadata.datatree_field_click('Product', 2, 1)
        utillobj.synchronize_with_number_of_element(element_css, 5, 60)
           
        vis_metadata.datatree_field_click('Unit Sales', 2, 1)
        utillobj.synchronize_with_number_of_element(element_css, 8, 60)
           
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 3, 1, 2, test_case_id + '_Ds01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 3, 1, 2, Test_Case_ID + '_Ds01.xlsx', "Step 1.1: Verify Category, Product, Unit Sales report.")
           
        """ 
        Step 2: Select 'Insert > New chart' and drag a area in design view to create a graph
        """ 
        vis_ribbon.select_ribbon_item("Insert", "Chart")
        time.sleep(5)
          
        """
        Step03: Select 'PRODUCT to Horizontal axis', and 'UNITSALES to Vertical Axis to get a graph.
        """
        vis_metadata.datatree_field_click("Product", 1, 1,'Add To Query','Horizontal Axis')
        chart2_xtitle_css="#TableChart_2 [class*='xaxisOrdinal-title']"
        utillobj.synchronize_with_visble_text(chart2_xtitle_css, 'Product', 60)
        
        vis_metadata.datatree_field_click('Unit Sales', 1, 1,'Add To Query','Vertical Axis')
        chart2_ytitle_css="#TableChart_2 [class*='yaxis-title']"
        utillobj.synchronize_with_visble_text(chart2_ytitle_css, 'UnitSales', 60)
        vis_ribbon.repositioning_document_component('5.5', '2.5')
        utillobj.synchronize_with_number_of_element("#pfjTableChart_2  [class*='riser!s0']",2,60)
        
        vis_resobj.verify_number_of_riser("TableChart_2", 1, 2, 'Step 03a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Capuccino','Espresso']
        expected_yval_list=['0', '50K', '100K', '150K', '200K', '250K', '300K','350K']
        vis_resobj.verify_riser_chart_XY_labels('TableChart_2', expected_xval_list, expected_yval_list, 'Step 03b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("TableChart_2", "riser!s0!g0!mbar!", "bar_blue1", "Step 03c: Verify bar color")
        xaxis_value="Product"
        yaxis_value="Unit Sales"
        vis_resobj.verify_xaxis_title("TableChart_2", xaxis_value, "Step 03d(i): Verify X-Axis Title")
        vis_resobj.verify_yaxis_title("TableChart_2", yaxis_value, "Step 03d(ii): Verify Y-Axis Title")
          
        """
        Save and close IA, and Run the report.
        """
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        
        utillobj.active_run_fex_api_login(Test_Case_ID+str('.fex'),'S10071_4','mrid','mrpass')
        utillobj.synchronize_with_number_of_element("#ITableData0 ", 1, 10)
        
    #1st Report
        active_mis_obj.verify_page_summary(0,'10of10records,Page1of1',"Step04.1a: Verify the Report Summary of 1st Report")
        active_mis_obj.verify_column_heading('ITableData0', ['Category','Product','Unit Sales'], 'Step04.1b: Verify the column heading')
#         ia_runobj.create_table_data_set('#ITableData0', Test_Case_ID+'_DsStep04.1.xlsx')
        ia_runobj.verify_table_data_set('#ITableData0', Test_Case_ID+'_DsStep04.1.xlsx', 'Step04.1c: Verify data.')
        
    #chart
        active_mis_obj.verify_arChartToolbar("MAINTABLE_1",['More Options','Advanced Chart','Original Chart'],"Step04.1d: Verify Chart toolbar")
        vis_resobj.verify_number_of_riser("MAINTABLE_1", 1, 10, 'Step04.2a: Verify the total number of risers displayed on Preview Chart')
        expected_xval_list=['Biscotti','Capuccino','Coffee']
        expected_yval_list=['0','200K', '400K', '600K','800K','1,000K']
        vis_resobj.verify_riser_chart_XY_labels('MAINTABLE_1', expected_xval_list, expected_yval_list, 'Step04.2b: X and Y axis Scales Values has changed or NOT')
        utillobj.verify_chart_color("MAINTABLE_1", "riser!s0!g0!mbar!", "bar_blue1", "Step04.2c: Verify bar color")
        xaxis_value="Product"
        yaxis_value="Unit Sales"
        vis_resobj.verify_xaxis_title("MAINTABLE_1", xaxis_value, "Step04.2d(i): Verify X-Axis Title")
        vis_resobj.verify_yaxis_title("MAINTABLE_1", yaxis_value, "Step04.2d(ii): Verify Y-Axis Title")
        expected_tooltip=['Product:  Biscotti', 'Unit Sales:  421377', 'Filter Chart', 'Exclude from Chart']
        active_mis_obj.verify_active_chart_tooltip('MAINTABLE_1', 'riser!s0!g0!mbar', expected_tooltip, "Step04.2c: verify the chart tooltip")
        
        
        
if __name__ == '__main__':
    unittest.main()