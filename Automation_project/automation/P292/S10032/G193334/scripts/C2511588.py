'''
Created on December 20, 2017

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227781
TestCase Name = Report-Chart: Verify user can directly switch from Line to Bar to PIE to Scatter To Rollup.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run,active_chart_rollup,ia_resultarea
from common.lib import utillity
from common.wftools import active_report

class C2511588_TestClass(BaseTestCase):

    def test_C2511588(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_ON_001a.fex"
        report_dataset_name="AHTML_ON_001a"
        Test_Case_ID ="C2511588"
        
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
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """
             Step 04 : Select Unit Sales > Chart.Select Line Chart.
                Select Product column under Line Chart
        """
        
        miscelanousobj.select_menu_items("ITableData0",4, "Chart","Line","Product")
        
        """
             Expect to see the following initial Line Chart generated from the Active Report.
        """
        miscelanousobj.verify_chart_title('wall1','Unit Sales by Product','Step 04.1 : Verify line chart title')
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1000K']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 04.2: Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('wall1',11, 'Step 04.3: Verify Number of riser')
        time.sleep(2)
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 04.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 04.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 04.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
  
        """
             Step 05: From the icon bar at the top, select the second icon for Bar Chart.
        """
        rollupobj.click_chart_menu_bar_items('wall1', 1)
        
        """
             Expect to see the following initial Line Chart generated from the Active Report.
        """
       
        miscelanousobj.verify_chart_title("wall1","Unit Sales by Product", "Step 05.1 : Verify chart title ")
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1000K']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 05.2: Verify XY labels")
        resultobj.verify_number_of_riser("wall1", 1, 10, 'Step 05.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("wall1", "riser!s0!g2!mbar!", "bar_blue", "Step 05.4: Verify  riser color")
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 05.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 05.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 05.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
             Step 06: From the icon bar at the top, select the third icon for PIE Chart.
        """
        rollupobj.click_chart_menu_bar_items('wall1', 2)
        
        """
             Expect to see the Bar Chart converted into the following PIE chart.
        """
        miscelanousobj.verify_chart_title("wall1","Unit Sales by Product", "Step 06.1 : Verify chart title ")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 06.2a: Verify Color')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 06.2b: Verify Color')
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 06.3: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 06.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 06.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_riser_pie_labels_and_legends('wall1', ['Unit Sales'], "Step 06.6:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('wall1', 10, "Step 06.7: Verify number of pie")
        expected_label_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        resultobj.verify_riser_legends('wall1', expected_label_list, 'Step 06.8: Verify Legends')
        
        """
             Step 07: From the icon bar at the top, select the fifth icon for Scatter Diagram.
        """
        rollupobj.click_chart_menu_bar_items('wall1', 4)
        
        """
             Expect to see the PIE chart converted into the following Scatter diagram.
        """
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1000K']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 07.1: Verify XY labels")
        utillobj.verify_chart_color("wall1", "riser!s0!g0!mmarker!", "bar_blue", "Step 07.3: Verify  1st bar color",attribute_type='stroke')
        miscelanousobj.verify_chart_title('wall1', 'Unit Sales by Product', 'Step 07.4: Verify Chart Title')
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 07.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 07.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 07.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
             Step 08: From the icon bar at the top, select the sixth icon for Rollup Report.
        """
        rollupobj.click_chart_menu_bar_items('wall1', 5)
        
        """
            Expect to see the Scatter Diagram converted into the following Rollup Report.
        """
#         iarun.create_table_data_set('#ITableData1','C2227781_001.xlsx')
        iarun.verify_table_data_set('#ITableData1',Test_Case_ID+'_001.xlsx','Step 08.1: Verify C2227778_001.xlsx output')
        miscelanousobj.verify_page_summary('1','10of10records,Page1of1','Step 8.2 : Verify page summary')        
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 08.3: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 08.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 08.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        miscelanousobj.verify_chart_title("wall1","Unit Sales by Product", "Step 08.6 : Verify chart title ")
        
        """
             Step 09: From the icon bar at the top, select the eighth icon for Original Chart.
        """
        rollupobj.click_chart_menu_bar_items('wall1', 7)
        
        """
            Expect to see the Rollup Report converted into the Original Line Chart.
        """
        miscelanousobj.verify_chart_title('wall1','Unit Sales by Product','Step 09.1 : Verify line chart title')
        expected_xval_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_yval1_list=['0', '200K', '400K', '600K', '800K', '1000K']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 09.2: Verify XY labels")
        ia_resultobj.verify_number_of_chart_segment('wall1',11, 'Step 09.3: Verify Number of riser')
        time.sleep(2)
        utillobj.verify_chart_color("wall1", "riser!s0!g0!mline!", "bar_blue1", "Step 09.4: Verify  1st bar color",attribute_type='stroke')
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 09.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 09.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 09.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
             Step 10: Dismiss the window and logout.
                http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()   