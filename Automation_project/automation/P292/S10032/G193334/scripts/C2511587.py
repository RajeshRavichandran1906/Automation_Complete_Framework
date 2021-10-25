'''
Created on December 20, 2017

@author: Prabhakaran/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227780
TestCase Name = Report-Chart: Verify Chart/Rollup tool can generate Bar and PIE charts.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, ia_resultarea, active_miscelaneous, active_tools,active_chart_rollup
from common.lib import utillity
from common.wftools import active_report

class C2511587_TestClass(BaseTestCase):

    def test_C2511587(self):
        
        """
            TESTCASE VARIABLES
        """
#         Test_Case_ID = 'C2511587'
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        act_tool = active_tools.Active_Tools(self.driver)
        act_chartroll=active_chart_rollup.Active_Chart_Rollup(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 : Expand folder P292_S10032_G193334
            Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G193334%252FAHTMLON&BIP_item=AHTML_ON_001a.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03.0 : Verify the report is generated. And select the Chart/Rollup Tool option from the Category field drop down control.
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
         
        """
            Step 03.1 : select the Chart/Rollup Tool option from the Category field drop down control.
        """ 
        miscelanousobj.select_menu_items('ITableData0', 0, 'Chart/Rollup Tool')
        utillobj.synchronize_with_visble_text("#wall1 .arWindowBarTitle>span", 'Chart/Rollup Tool', 10)
        
        """
            Step 03.2 : Expect to see the following Active Report with the Chart/Rollup Tool activated.
        """ 
        miscelanousobj.verify_popup_appears('wall1','Chart/Rollup Tool', 'Step 03.2 : Verify Active Report with the Chart/Rollup Tool activated')
        miscelanousobj.move_active_popup('1', 800, 300)
        
        """
            Step 04 : From the Chart/Rollup Tool, drag the Category field under the Columns list to the Group By area and then Unit Sales to the Measure area.
        """
        act_tool.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Category', 1, 'Group By', 0)
        time.sleep(5)
        act_tool.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Unit Sales', 1, 'Measure', 0)  
        time.sleep(3) 
         
        """
            Step 05 : Click the Charts button at the top and select the first Bar Chart in the upper left, for horizontal Bar Chart.Click OK to generate the Bar Chart.
        """
        act_chartroll.select_advance_chart('wall1', 'bar')
        top=self.driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", top)
        time.sleep(3)
        utillobj.synchronize_with_visble_text("#wbody2_ft div", 'Unit Sales by Category', 10)

        """
            Step 05.1 : Expect to see the following Horizontal Bar chart.
        """  
        expected_axis_label=['Coffee', 'Food', 'Gifts']
        expected_yaxis_label=['0','0.4M','0.8M','1.2M','1.6M']
        miscelanousobj.verify_popup_title('wall2', 'Unit Sales by Category', 'Step 05.1 : Verify popup title')
        miscelanousobj.verify_chart_title('wbody2_ft', 'Unit Sales by Category', 'Step 05.2 : Verify chart title')
        resultobj.verify_riser_chart_XY_labels('wbody2_f', expected_axis_label, expected_yaxis_label, 'Step 05.3 :', 10) 
        resultobj.verify_number_of_riser('wbody2_f',1, 3, 'Step 05.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody2_f', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 05.5 : Verify chart riser color')
        
        act_chartroll.verify_arChartMenu('wall2','Step 05.7 : Verify Chart toolbar')
        miscelanousobj.verify_arChartToolbar('wall2', ['Aggregation'],"Step 05.8 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall2', ['Sum'],"Step 05.7 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
            Step 6 : Now add a second Measure by clicking the first icon at the top, selecting Add (Y) and adding Dollar Sales.
        """
        time.sleep(2)
        act_chartroll.create_new_item(0, 'Add (Y)->Dollar Sales',False,'wall2')
        utillobj.synchronize_with_visble_text("#wbody2_ft div", 'Unit Sales, Dollar Sales by Category', 10)
        
        """
            Step 06.1 : Expect to see the following horizontal Bar chart, now with two Measures, stacked on top of each other for each Category.
        """
        expected_axis_label=['Coffee', 'Food', 'Gifts']
        expected_yaxis_label=['0','4M','8M','12M','16M','20M']
        miscelanousobj.verify_popup_title('wall2', 'Unit Sales by Category', 'Step 06.1 : Verify popup title')
        miscelanousobj.verify_chart_title('wbody2_ft', 'Unit Sales, Dollar Sales by Category', 'Step 06.2 : Verify chart title')
        resultobj.verify_riser_chart_XY_labels('wbody2_f', expected_axis_label, expected_yaxis_label, 'Step 06.3 :', 10) 
        resultobj.verify_number_of_riser('wbody2_f',1, 6, 'Step 06.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody2_f', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 06.5 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s1!g1!mbar!', 'pale_green', 'Step 06.6 : Verify chart riser color')
        resultobj.verify_riser_legends('wbody2_f', ['Unit Sales', 'Dollar Sales'], 'Step 06.7 : Verify char legend labels')
        
        act_chartroll.verify_arChartMenu('wall2','Step 06.9 : Verify Chart toolbar')
        miscelanousobj.verify_arChartToolbar('wall2', ['Aggregation'],"Step 6.10 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall2', ['Sum'],"Step 6.11 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
        """
            Step 07 : Now add a second Dimension by clicking the first icon at the top, selecting Group By (X) and adding Product ID.
        """
        act_chartroll.create_new_item(1, 'Group By (X)->Product ID',False,'wall2')
        utillobj.synchronize_with_visble_text("#wbody2_ft div", 'Unit Sales, Dollar Sales by Category, Product ID', 10)
        
        """
            Step 07.1 : Expect to see the following horizontal Bar chart, now with two Measures, stacked on top of each other for each Category/Product ID combination.
        """
        expected_axis_label=['Coffee/C141', 'Coffee/C142', 'Coffee/C144','Food/F101','Food/F102','Food/F103','Gifts/G100','Gifts/G104','Gifts/G110','Gifts/G121']
        expected_yaxis_label=['0','2M','4M','6M','8M','10M','12M']
        miscelanousobj.verify_popup_title('wall2', 'Unit Sales by Category', 'Step 07.1 : Verify popup title')
        miscelanousobj.verify_chart_title('wbody2_ft', 'Unit Sales, Dollar Sales by Category, Product ID', 'Step 07.2 : Verify chart title')
        resultobj.verify_riser_chart_XY_labels('wbody2_f', expected_axis_label, expected_yaxis_label, 'Step 07.3 :', 10) 
        resultobj.verify_number_of_riser('wbody2_f',1, 20, 'Step 07.4 : Verify number of chart risers')
        utillobj.verify_chart_color('wbody2_f', 'riser!s0!g1!mbar!', 'bar_blue', 'Step 07.5 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s1!g1!mbar!', 'pale_green', 'Step 07.6 : Verify chart riser color')
        resultobj.verify_riser_legends('wbody2_f', ['Unit Sales', 'Dollar Sales'], 'Step 07.7 : Verify char legend labels')
        
        act_chartroll.verify_arChartMenu('wall2','Step 07.9 : Verify Chart toolbar')
        miscelanousobj.verify_arChartToolbar('wall2', ['Aggregation'],"Step 7.10 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall2', ['Sum'],"Step 7.11 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
        """
            Step 08 : Close the Bar Chart graph and again select the Chart/Rollup Tool from the original 107 line report. Add Dollar Sales to Measure and Category to Dimension.
        """
        miscelanousobj.close_popup_dialog('2')
        time.sleep(3)
        miscelanousobj.select_menu_items('ITableData0', 0, 'Chart/Rollup Tool')
        utillobj.synchronize_with_visble_text("#wall1 .arWindowBarTitle>span", 'Chart/Rollup Tool', 10)
        miscelanousobj.verify_popup_appears('wall1','Chart/Rollup Tool', 'Step 08.1 : Verify Active Report with the Chart/Rollup Tool activated')
        
        """
            Step 08.1 : Expect to see the Chart/Rollup Tool again, this time with Dollar Sales and Category.
        """
        act_tool.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Category', 1, 'Group By', 0)
        time.sleep(3)
        act_tool.chart_rollup_tool_drag_drop_items('charttoolt1', 'Columns', 'Dollar Sales', 1, 'Measure', 0)  
        time.sleep(3)
        
        """
            Step 09 : Click the Charts button at the top, scroll down until the selection of PIE charts appears. Select the first PIE Chart option. Click OK to generate the PIE Chart.
        """
        act_chartroll.select_advance_chart('wall1', 'piebevel')
        top=self.driver.find_element_by_css_selector("#ITableData0 .arGridColumnHeading")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", top)
        time.sleep(3)
        utillobj.synchronize_with_visble_text("#wbody2_ft div", 'Dollar Sales by Category', 10)
        
        """
            Step 09.1 : Expect to see the following PIE Chart with one Dollar Sales slice for each Category. 
        """
        miscelanousobj.verify_popup_title('wall2', 'Dollar Sales by Category','Step 09.1 : Verify popup title')
        miscelanousobj.verify_chart_title('wbody2_ft', 'Dollar Sales by Category', 'Step 09.2 : Verify chart title')
        resultobj.verify_riser_legends('wbody2_f', ['Coffee', 'Food', 'Gifts'], 'Step 09.3 : Verify char legend labels')
#         resultobj.verify_number_of_pie_segments('wbody2_f', 1, 3, 'Step 09.4 : Verify number of pie chart segments')
        ia_resultobj.verify_number_of_chart_segment('wbody2_f', 3, "Step 09.4: Verify number of pie")
        resultobj.verify_riser_pie_labels_and_legends('wbody2_f', ['Dollar Sales'], 'Step 09.5 : Verify pie chart label')
        utillobj.verify_chart_color('wbody2_f', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 09.6 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s1!g0!mwedge!', 'pale_green', 'Step 09.7 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 09.8 : Verify chart riser color')
        
        act_chartroll.verify_arChartMenu('wall2','Step 9.10 : Verify Chart toolbar')
        miscelanousobj.verify_arChartToolbar('wall2', ['Aggregation'],"Step 9.11 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall2', ['Sum'],"Step 9.12 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
        """
            Step 10 : Now add a second Dimension by clicking the first icon at the top, selecting Group By (X) and adding Product.
        """
        act_chartroll.create_new_item(1, 'Group By (X)->Product',False,'wall2')
        utillobj.synchronize_with_visble_text("#wbody2_ft div", 'Dollar Sales by Category, Product', 10)
        
        """
            Step 10.1 : Expect to see the PIE chart, now with one Dollar Sales slice for each Category/Product combination.
        """
        expected_legend=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        miscelanousobj.verify_popup_title('wall2', 'Dollar Sales by Category','Step 10.1 : Verify popup title')
        miscelanousobj.verify_chart_title('wbody2_ft', 'Dollar Sales by Category, Product', 'Step 10.2 : Verify chart title')
        resultobj.verify_riser_legends('wbody2_f', expected_legend, 'Step 10.3 : Verify char legend labels')
#         resultobj.verify_number_of_pie_segments('wbody2_f', 1, 10, 'Step 10.4 : Verify number of pie chart segments')
        ia_resultobj.verify_number_of_chart_segment('wbody2_f', 10, "Step 10.4: Verify number of pie")
        resultobj.verify_riser_pie_labels_and_legends('wbody2_f', ['Dollar Sales'], 'Step 10.5 : Verify pie chart label')
        utillobj.verify_chart_color('wbody2_f', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 10.6 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s1!g0!mwedge!', 'pale_green', 'Step 10.7 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 10.8 : Verify chart riser color')
        
        act_chartroll.verify_arChartMenu('wall2','Step 10.10 : Verify Chart toolbar')
        miscelanousobj.verify_arChartToolbar('wall2', ['Aggregation'],"Step 10.11 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall2', ['Sum'],"Step 10.12 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(3)
        
        """
            Step 11 : Now try to add a second Measure by clicking the first icon at the top, selecting Add (Y) and adding Unit Sales.
        """
        act_chartroll.create_new_item(1, 'Add (Y)->Unit Sales',False,'wall2')
        utillobj.synchronize_with_visble_text("#wbody2_ft div", 'Dollar Sales, Unit Sales by Category, Product', 10)
        
        """
            Step 11.1 : Expect to see the following two PIE charts, the first is Dollar Sales by Category/Product and the second is Unit Sales by Category/Product.
        """
        expected_legend=['Coffee/Capuccino', 'Coffee/Espresso', 'Coffee/Latte', 'Food/Biscotti', 'Food/Croissant', 'Food/Scone', 'Gifts/Coffee Grinder', 'Gifts/Coffee Pot', 'Gifts/Mug', 'Gifts/Thermos']
        miscelanousobj.verify_popup_title('wall2', 'Dollar Sales by Category','Step 11.1 : Verify popup title')
        miscelanousobj.verify_chart_title('wbody2_ft', 'Dollar Sales, Unit Sales by Category, Product', 'Step 11.2 : Verify chart title')
        resultobj.verify_riser_legends('wbody2_f', expected_legend, 'Step 11.3 : Verify char legend labels')
        ia_resultobj.verify_number_of_chart_segment('wbody2_f', 20, "Step 11.4: Verify number of riser in two pie chart")
#         resultobj.verify_number_of_pie_segments('wbody2_f', 2, 10, 'Step 11.4 : Verify number of pie chart segments')
        resultobj.verify_riser_pie_labels_and_legends('wbody2_f', ['Dollar Sales', 'Unit Sales'], 'Step 11.5 : Verify pie chart label')
        utillobj.verify_chart_color('wbody2_f', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 11.6 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s1!g0!mwedge!', 'pale_green', 'Step 11.7 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 11.8 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s0!g1!mwedge!', 'bar_blue', 'Step 11.9 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s1!g1!mwedge!', 'pale_green', 'Step 11.10 : Verify chart riser color')
        utillobj.verify_chart_color('wbody2_f', 'riser!s2!g1!mwedge!', 'dark_green', 'Step 11.11 : Verify chart riser color')
        
        act_chartroll.verify_arChartMenu('wall2','Step 11.14 : Verify Chart toolbar')
        miscelanousobj.verify_arChartToolbar('wall2', ['Aggregation'],"Step 11.15 : Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall2', ['Sum'],"Step 11.16 : Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        time.sleep(2)
        
        """
            Step 12 : Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        miscelanousobj.close_popup_dialog('2')
        time.sleep(2)
        
        
if __name__=='__main__' :
    unittest.main()