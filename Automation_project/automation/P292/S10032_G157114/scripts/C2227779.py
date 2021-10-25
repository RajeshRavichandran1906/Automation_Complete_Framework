'''
Created on December 19, 2017

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227779
TestCase Name =Report-Chart: Verify that user can change the contents of both X-axis and Y-axis fields on a PIE & Bar Chart.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous,active_chart_rollup,ia_resultarea
from common.lib import utillity
from common.wftools import active_report

class C2227779_TestClass(BaseTestCase):

    def test_C2227779(self):
        
        """
            TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 :Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
           
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
             Step 03 : Verify the report is generated.
            Expect to see the following Active Report
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2 verify report data")
        
        """
             Step 04 : Select Dollar_Sales > Chart > PIE > Category
                Expect to see the following PIE Chart.
        """
        miscelanousobj.select_menu_items("ITableData0",5, "Chart","Pie","Category")
        miscelanousobj.verify_chart_title("wall1","Dollar Sales BY Category", "Step 04.1 : Verify chart title ")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 04.2a: Verify Color')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 04.2b: Verify Color')
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 04.3: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 04.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 04.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_riser_pie_labels_and_legends('wall1', ['Dollar Sales'], "Step 04.6:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('wall1', 3, "Step 04.7: Verify number of pie",custom_css="path[class^='riser']")
        expected_label_list=['Coffee', 'Food', 'Gifts']
        resultobj.verify_riser_legends('wall1', expected_label_list, 'Step 04.8: Verify Legends')
        expected_tooltip_list=['Coffee', 'Dollar Sales:17.2M', '37.3% of 46.2M']
        resultobj.verify_default_tooltip_values('wall1', 'riser!s0!g0!mwedge!', expected_tooltip_list, 'Step 04.9: verify the default tooltip values')
        time.sleep(2)
        
        """
             Step 05 : From the icon list at the top, click the first icon.
            Expect to see the following graph options:
            - New
            - Group By (x)
            - Add (y)
            - Top
            - Export to (specific to IE browser)
            - Chart/Rollup Tool
            - Restore Original
        """

        expectedlist=['New','Group By (X)','Add (Y)','Top','Chart/Rollup Tool','Restore Original']
        rollupobj.create_new_item(0, 'Group By (X)',True,'wall1',expected_list=expectedlist,msg="Step 6:Verify")               
        
        """
             Step 06: Select Group By (X), then click Product ID.
                Expect to see the following PIE chart, now with Product ID add as a second sort field.
        """
        rollupobj.create_new_item(0, 'Group By (X)->Product ID',False,'wall1')
        miscelanousobj.verify_chart_title("wall1","Dollar Sales BY Category", "Step 06.1 : Verify chart title ")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 06.2a: Verify Color')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 06.2b: Verify Color')
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 06.3: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 06.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 06.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_riser_pie_labels_and_legends('wall1', ['Dollar Sales'], "Step 06.7:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('wall1', 10, "Step 06.8: Verify number of pie",custom_css="path[class^='riser']")
        expected_label_list=['Coffee/C141', 'Coffee/C142', 'Coffee/C144', 'Food/F101', 'Food/F102', 'Food/F103', 'Gifts/G100', 'Gifts/G104', 'Gifts/G110', 'Gifts/G121']
        resultobj.verify_riser_legends('wall1', expected_label_list, 'Step 06.9: Verify Legends')
        expected_tooltip_list=['Coffee/C142', 'Dollar Sales:10.9M', '23.7% of 46.2M']
        resultobj.verify_default_tooltip_values('wall1', 'riser!s1!g0!mwedge!', expected_tooltip_list, 'Step 06.10: verify the default tooltip values')
        
        
        """
             Step 07: From the icon list, click the first icon again, select Add (Y), then select Unit Sales.
                Expect to see the following PIE chart, still sorted by Category/Product ID but now using Unit Sales.
                Verify that only one Measure can show using this tool.
        """
        rollupobj.create_new_item(1, 'Add (Y)->Unit Sales',False,'wall1')
        miscelanousobj.verify_chart_title("wall1","Dollar Sales BY Category", "Step 07.1 : Verify chart title ")
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', 'bar_blue', 'Step 07.2a: Verify Color')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', 'dark_green', 'Step 07.2b: Verify Color')
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 07.3: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 07.4: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 07.5: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        resultobj.verify_riser_pie_labels_and_legends('wall1', ['Unit Sales'], "Step 07.7:",custom_css="text[class*='pieLabel']",same_group=True) 
        ia_resultobj.verify_number_of_chart_segment('wall1', 10, "Step 07.8: Verify number of pie",custom_css="path[class^='riser']")
        expected_label_list=['Coffee/C141', 'Coffee/C142', 'Coffee/C144', 'Food/F101', 'Food/F102', 'Food/F103', 'Gifts/G100', 'Gifts/G104', 'Gifts/G110', 'Gifts/G121']
        resultobj.verify_riser_legends('wall1', expected_label_list, 'Step 07.9: Verify Legends')
        expected_tooltip_list=['Coffee/C142', 'Unit Sales:878K', '23.8% of 3.7M']
        resultobj.verify_default_tooltip_values('wall1', 'riser!s1!g0!mwedge!', expected_tooltip_list, 'Step 07.10: verify the default tooltip values')
        miscelanousobj.close_popup_dialog('1')
        time.sleep(3)
        
        
        """
             Step 08: Close the PIE chart screen.Select Unit_Sales > Chart > Column > Category
            Expect to see the following vertical Column Chart, with Unit Sales By Category.
        """
        miscelanousobj.select_menu_items("ITableData0",4, "Chart","Column","Category")
        
        miscelanousobj.verify_chart_title('wall1','Unit Sales BY Category','Step 08.1 : Verify line chart title')
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval1_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 08.2: Verify XY labels")
        resultobj.verify_number_of_riser("wall1", 1, 3, 'Step 08.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("wall1", "riser!s0!g1!mbar!", "bar_blue1", "Step 08.4: Verify  1st bar color")
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 08.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 08.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 08.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        
        """
             Step 09: From the icon list, click the first icon, select Add (Y), then select Dollar_Sales.
            Expect to see the following Column Chart now with two measures for each Category sort.
        """
        rollupobj.create_new_item(1, 'Add (Y)->Dollar Sales',False,'wall1')
        miscelanousobj.verify_chart_title('wall1','Unit Sales BY Category','Step 09.1 : Verify line chart title')
        expected_xval_list=['Coffee', 'Food', 'Gifts']
        expected_yval1_list=['0', '4M', '8M', '12M', '16M', '20M']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 09.2: Verify XY labels")
        resultobj.verify_number_of_riser("wall1", 1, 6, 'Step 09.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("wall1", "riser!s0!g0!mbar!", "bar_blue1", "Step 09.4: Verify  1st bar color")
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 09.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 09.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 09.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        legend=['Unit Sales', 'Dollar Sales']
        resultobj.verify_riser_legends("wall1", legend, "Step 09.8: Verify legend")
        expected_tooltip_list=['Dollar Sales:17.2M', 'X:Coffee']
        resultobj.verify_default_tooltip_values('wall1', 'riser!s1!g0!mbar!', expected_tooltip_list, 'Step 09.9: verify the default tooltip values')
        
        """
             Step 10:From the icon list, click the first icon again, select Group By (X), then select Product ID.
                Expect to see the following Column Chart now with two Sort fields, Category & Product ID and two Measures, Unit Sales and Dollar Sales.
        """
        
        rollupobj.create_new_item(1, 'Group By (X)->Product ID',False,'wall1')
        miscelanousobj.verify_chart_title('wall1','Unit Sales BY Category','Step 10.1 : Verify line chart title')
        expected_xval_list=['Coffee/C141', 'Coffee/C142', 'Coffee/C144', 'Food/F101', 'Food/F102', 'Food/F103', 'Gifts/G100', 'Gifts/G104', 'Gifts/G110', 'Gifts/G121']
        expected_yval1_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        resultobj.verify_riser_chart_XY_labels("wall1", expected_xval_list, expected_yval1_list, "Step 10.2: Verify XY labels")
        resultobj.verify_number_of_riser("wall1", 1, 20, 'Step 10.3: Verify the total number of risers displayed on preview')
        utillobj.verify_chart_color("wall1", "riser!s0!g1!mbar!", "bar_blue1", "Step 10.4: Verify  1st bar color")
        miscelanousobj.verify_arChartToolbar('wall1', ['More Options','Column','Pie','Line','Scatter','Rollup','Advanced Chart','Original Chart'],"Step 10.5: Verify Chart toolbar")
        miscelanousobj.verify_arChartToolbar('wall1', ['Aggregation'],"Step 10.6: Verify Chart toolbar", custom_css='.arChartMenuBarContainer .tabPagingText1 td[title]')
        miscelanousobj.verify_arChartToolbar('wall1', ['Sum'],"Step 10.7: Verify Chart toolbar", custom_css=".arChartMenuBarContainer [id*='SUM']", text=True)
        legend=['Unit Sales', 'Dollar Sales']
        resultobj.verify_riser_legends("wall1", legend, "Step 10.8: Verify legend")
        expected_tooltip_list=['Dollar Sales:10.9M', 'X:Coffee/C142']
        resultobj.verify_default_tooltip_values('wall1', 'riser!s1!g1!mbar!', expected_tooltip_list, 'Step 10.9: verify the default tooltip values')
        time.sleep(4)
        """
             Step 11:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
if __name__ == '__main__':
    unittest.main()   
