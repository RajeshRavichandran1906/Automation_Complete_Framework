'''
Created on Dec 20, 2017

@author: Sowmiya/Updated by : Bhagavathi

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157310
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2227777
TestCase Name : Report-Chart: Verify Chart window toolbar is available and user is able to use each option
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous,active_chart_rollup,ia_run
from common.lib import utillity
from common.wftools import active_report

class C2227777_TestClass(BaseTestCase):

    def test_C2227777(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227777'
        utillobj = utillity.UtillityMethods(self.driver)
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        rollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """        
            Step 01:Sign in to WebFOCUS as a Basic user
                    http://machine:port/{alias} Sign on screen will display
            Step 02:Expand folder P292_S10032_G157266
                    Execute the following URL:
                    http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03: Verify the AHTML formatted report is generated.

        """
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 03.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """
            Step 04: Select Unit Sales > Chart 
            Select Pie chart type. Select Category column under Pie chart type.
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Chart','Pie','Category')
        utillobj.synchronize_with_number_of_element('#wall1', 1, 15)
        
        expected_title='Unit Sales by Category'
        miscelanousobj.verify_chart_title('wall1', expected_title, msg='Step 05: Verify chart title')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', color='dark_green', msg='Step 05 : Verify the pie chart color Green')
        utillobj.verify_chart_color('wall1', 'riser!s1!g0!mwedge!', color='bar_green', msg='Step 05 : Verify the pie chart color Bar green')
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', color='bar_blue', msg='Step 05 : Verify the pie chart color bar_blue')
        parent_css='div[id="wall1"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        risers = self.driver.find_elements_by_css_selector('#wall1 [class*="riser!"]')
#         result_obj.verify_number_of_pie_segments('wall1', 1, 3, msg='Step 05 : Verify number of pie segments displayed')
        utillobj.asequal(3, len(risers), 'Step 05 : Verify number of pie segments displayed')
        expected_legend_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_legends('wall1', expected_legend_list, msg='Step 05 : ')
        expected_label_list=['Unit Sales']
        result_obj.verify_riser_pie_labels_and_legends('wall1', expected_label_list, msg='Step 05 : ')
        rollupobj.verify_arChartMenu('wall1', msg='Step 05 : Verify menu items')
        
        """
            Step 05 : Click each menu option under Active Chart menu
            Eg: Click First dropdown button
            Verify user is able to use each option 
            Verify dropdown menu shows:
            - New
            - Group By (X)
            - Add (Y)
            - Top
            - Chart/Rollup 
            Tool
            - Restore Original
            Step 06 : Click First dropdown button > New
        """
        
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', color='dark_green', msg='Step 06 : Verify the pie chart color Green')
        utillobj.verify_chart_color('wall1', 'riser!s1!g0!mwedge!', color='bar_green', msg='Step 06 : Verify the pie chart color Bar green')
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', color='bar_blue', msg='Step 06 : Verify the pie chart color bar_blue')
        
        rollupobj.create_new_item(0, 'New', False)
        parent_css='div[id="wall2"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        
        """
            Step 07 : From the New window, click Bar.
        """
        rollupobj.click_chart_menu_bar_items('wall2', 1)
        parent_css='div[id="wall2"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        
        utillobj.verify_chart_color('wall2','riser!s0!g0!mbar!', color='bar_blue', msg='Step 07 : Verify the bar color')
        result_obj.verify_number_of_riser('wall2', 1, 3, msg='Step 07 : Verify number of risers displayed')
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        expected_xval_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_chart_XY_labels('wall2', expected_xval_list, expected_yval_list, msg='Step 07 : Labels ')
        """
            Step 08 : From the New window, click Pie.
        """
        rollupobj.click_chart_menu_bar_items('wall2', 2)
        parent_css='div[id="wall2"]'
        utillobj.synchronize_with_number_of_element(parent_css+" [class='riser!s2!g0!mwedge!']", 1, 15)
        
        utillobj.verify_chart_color('wall2', 'riser!s2!g0!mwedge!', color='dark_green', msg='Step 08 : Verify the pie chart color Green')
        utillobj.verify_chart_color('wall2', 'riser!s1!g0!mwedge!', color='bar_green', msg='Step 08 : Verify the pie chart color Bar green')
        utillobj.verify_chart_color('wall2', 'riser!s0!g0!mwedge!', color='bar_blue', msg='Step 08 : Verify the pie chart color bar_blue')
#         result_obj.verify_number_of_pie_segments('wall2', 1, 3, msg='Step 08 : Verify number of pie segments displayed')
        risers = self.driver.find_elements_by_css_selector('#wall1 [class*="riser!"]')
        utillobj.asequal(3, len(risers), 'Step 08 : Verify number of pie segments displayed')
        expected_legend_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_legends('wall1', expected_legend_list, msg='Step 08 : ')
        expected_label_list=['Unit Sales']
        result_obj.verify_riser_pie_labels_and_legends('wall1', expected_label_list, msg='Step 08 : ')
        """
            Step 09 : From the New window, click Line.

        """
        rollupobj.click_chart_menu_bar_items('wall2', 3)
        
        parent_css='div[id="wall2"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 15)
        
        utillobj.verify_chart_color('wall2','riser!s0!g0!mline!', color='bar_blue', attribute_type='stroke', msg='Step 09 : Verify the line color')
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        expected_xval_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_chart_XY_labels('wall2', expected_xval_list, expected_yval_list, msg='Step 09 : Labels ')
        """
            Step 10 : From the New window, click Scatter.

        """
        rollupobj.click_chart_menu_bar_items('wall2', 4)
        parent_css='div[id="wall2"]'
        utillobj.synchronize_with_number_of_element(parent_css+" [class='riser!s0!g0!mmarker!']", 1, 15)
        
        utillobj.verify_chart_color('wall2','riser!s0!g0!mmarker!', color='bar_blue', attribute_type='stroke', msg='Step 10 : Verify the Scatter color')
        utillobj.verify_chart_color('wall2','riser!s0!g1!mmarker!', color='bar_blue', attribute_type='stroke', msg='Step 10 : Verify the Scatter color')
        utillobj.verify_chart_color('wall2','riser!s0!g2!mmarker!', color='bar_blue', attribute_type='stroke', msg='Step 10 : Verify the Scatter color')

        result_obj.verify_number_of_circle('wall2', 3, 4, msg='Step 10 : Verify the number of circles')
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        expected_xval_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_chart_XY_labels('wall2', expected_xval_list, expected_yval_list, msg='Step 10 : Labels ')
        
        """
            Step 11 : Close the New Window and return to the original PIE window.

                Click Rollup icon at the top as output type.

        """
        popup_index='2'
        miscelanousobj.close_popup_dialog(popup_index)
        time.sleep(3)
        parent_css='div[id="wall1"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        
        rollupobj.click_chart_menu_bar_items('wall1', 5)
        parent_css='div[id="wall1"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        
#         ia_runobj.create_table_data_set('#ITableData1',Test_Case_ID+'_001.xlsx')
        ia_runobj.verify_table_data_set('#ITableData1',Test_Case_ID+'_001.xlsx','Step 11: Verify C2227777_001.xlsx output')
        miscelanousobj.verify_page_summary(1,'3of3records,Page1of1','Step 11 : Verify page summary')
         
        """
            Step 12 : Click Advance Chart/Rollup icon at the top(7th option)
            Opens up Advance Chart pop up.

        """
        rollupobj.click_chart_menu_bar_items('wall1', 6)
        time.sleep(3)
        rollupobj.verify_arChartMenu('wall1', msg='Step 12 : Verify the menu items')
        
        """
            Step 13 : Cancel Advance Chart pop up.
            Click Original chart icon.
            
        """
        popup_index='2'
        miscelanousobj.close_popup_dialog(popup_index)
        time.sleep(3)
        
        rollupobj.click_chart_menu_bar_items('wall1', 7)
        parent_css='div[id="wall1"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', color='dark_green', msg='Step 13 : Verify the pie chart color Green')
        utillobj.verify_chart_color('wall1', 'riser!s1!g0!mwedge!', color='bar_green', msg='Step 13 : Verify the pie chart color Bar green')
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', color='bar_blue', msg='Step 13 : Verify the pie chart color bar_blue')
        
        """
            Step 14 : Click Rollup icon on the output type and click Freeze icon.

        """
        rollupobj.click_chart_menu_bar_items('wall1', 5)
        
        parent_css='div[id="wall1"]'
        utillobj.synchronize_with_number_of_element(parent_css, 1, 10)
        
        """Verify Freeze option from unlock turns to lock state."""
        
        """
            Step 15 : Click Aggregation icon.
            By default aggregation is SUM for Unit Sales.
            On clicking aggregation icon, it shows these options:
            - Sum
            - Avg
            - Min
            - Max
            - Count
            - Disctinct
            
            Step 16 : Click Avg to change the aggregation type to Average Unit Sales.
            Expect to see the lock symbol change to unlock and Averages displayed for each Category.
        """
        rollupobj.click_chart_menu_bar_items('wall1', 8)
        parent_css='div[id="wall1"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        
        rollupobj.select_aggregate_function('wall1', 1, 'Avg', elem_index=9, verify=True,msg=' Step 15 : Verify the aggregate function')
        ia_runobj.verify_table_data_set('#ITableData1', Test_Case_ID+'_002.xlsx', msg='Verify the average table data set')
        
        """
            Step 17:Dismiss the window and logout.
                http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """   
                
if __name__ == '__main__':
    unittest.main()