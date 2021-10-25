'''
Created on December 19, 2017

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227778
TestCase Name = Report-Chart: Verify user can switch from Pie chart to a Rollup and use Active Controls in Rollup
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run,active_chart_rollup
from common.lib import utillity
from common.wftools import active_report

class C2227778_TestClass(BaseTestCase):

    def test_C2227778(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266
                Execute the following URL:http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
             Step 03 : Verify the report is generated.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
        
        """
             Step 04 : Select Unit Sales > Chart Select Column and Select Product under Column.
        """
        miscelanousobj.select_menu_items("ITableData0",4, "Chart","Column","Product")
        miscelanousobj.verify_chart_title("wall1","Unit Sales by Product", "Step 04.1 : Verify chart title ")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1000K']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        resultobj.verify_number_of_riser("wall1", 1, 10, 'Step 04.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("wall1", "riser!s0!g0!mbar!", "bar_blue", "Step 04.4: Verify  riser color")
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 04.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 04.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 04.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Unit Sales:421K', 'X:Biscotti']
        resultobj.verify_default_tooltip_values("wall1", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 04.8: Verify bar value")
        
        """
             Step 05 : Click the sixth icon from the left for Rollup option from the Chart toolbar menu.
                Expect to see the Column converted to a Rollup Report.
        """
        
        rollupobj.click_chart_menu_bar_items('wall1', 5)        
#         iarun.create_table_data_set('#ITableData1','C2227778_001.xlsx')
        iarun.verify_table_data_set('#ITableData1','C2227778_001.xlsx','Step 05.1: Verify C2227778_001.xlsx output')
        miscelanousobj.verify_page_summary('1','10of10records,Page1of1','Step 05.2 : Verify page summary')        
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 05.3: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 05.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 05.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscelanousobj.verify_chart_title("wall1","Unit Sales by Product", "Step 05.6 : Verify chart title ")
        
        """
             Step 06: From the Rollup report click the dropdown arrow for Product and select Descending sort order.
            Expect to see the Rollup report reflect descending order of Products.
        """
        miscelanousobj.select_menu_items("wall1",0,"Sort Descending")
#         iarun.create_table_data_set('#ITableData1','C2227778_002.xlsx')
        iarun.verify_table_data_set('#ITableData1','C2227778_002.xlsx','Step 06.1: Verify C2227778_002.xlsx output')
        miscelanousobj.verify_page_summary('1','10of10records,Page1of1','Step 06.2 : Verify page summary') 
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 06.3: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 06.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 06.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscelanousobj.verify_chart_title("wall1","Unit Sales by Product", "Step 06.6 : Verify chart title ")
        
        """
             Step 07: From the Rollup report, click the icon to the left of the Lock, to restore the original Column Chart.
                Expect to see the original vertical Column Chart.
        """
        
        rollupobj.click_chart_menu_bar_items('wall1',7)
        miscelanousobj.verify_chart_title("wall1","Unit Sales by Product", "Step 07.1 : Verify chart title ")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K','400K', '600K', '800K', '1000K']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 07.2: Verify XY labels")
        resultobj.verify_number_of_riser("wall1", 1, 10, 'Step 07.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("wall1", "riser!s0!g0!mbar!", "bar_blue", "Step 07.4: Verify  riser color")
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 07.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 07.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 07.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        expected_tooltip_list=['Unit Sales:421K', 'X:Biscotti']
        resultobj.verify_default_tooltip_values("wall1", "riser!s0!g0!mbar!", expected_tooltip_list, "Step 07.8: Verify bar value")
        
        """
             Step 08:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
if __name__ == '__main__':
    unittest.main()