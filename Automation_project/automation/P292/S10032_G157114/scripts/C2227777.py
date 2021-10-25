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
            Step 03:Verify the AHTML formatted report is generated.

        """
        expected_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        miscelanousobj.verify_column_heading('ITableData0', expected_list,'Step 03.1: Verify column heading')
        miscelanousobj.verify_page_summary(0, '107of107records,Page1of2', "Step 03.2:  107of107records,Page1of2 Active Report. - page summary verification")
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """
            Step 04:Click dropdown next to Unit Sales column heading.
                Verify all the report menu options are present on a report.
        """
        expected_menu_list=['Sort Ascending', 'Sort Descending', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Visualize','Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Export', 'Print', 'Window', 'Restore Original']
        miscelanousobj.verify_menu_items("ITableData0",4, None,expected_menu_list, 'Step 04:  Verify all the report menu options are present on a rep')
        
        """
            Step 05 : Select Unit Sales > Chart 
                Select Pie chart type. Select Category column under Pie chart type. 
                Click each menu option under Active Chart menu
        """
        miscelanousobj.select_menu_items('ITableData0', 4, 'Chart','Pie','Category')
        time.sleep(5)
        expected_title='Unit Sales BY Category'
        miscelanousobj.verify_chart_title('wall1', expected_title, msg='Step 05 : ')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', color='dark_green', msg='Step 05 : Verify the pie chart color Green')
        utillobj.verify_chart_color('wall1', 'riser!s1!g0!mwedge!', color='bar_green', msg='Step 05 : Verify the pie chart color Bar green')
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', color='bar_blue', msg='Step 05 : Verify the pie chart color bar_blue')
        parent_css='div[id="wall1"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        expected_tooltip_list=[['Coffee', 'Unit Sales:1.4M', '37.3% of 3.7M'],['Food', 'Unit Sales:1.4M', '37.5% of 3.7M'],['Gifts', 'Unit Sales:928K', '25.2% of 3.7M']]
        result_obj.verify_default_tooltip_values("wall1", "riser!s0!g0!mwedge!", expected_tooltip_list[0], "Step 05: Verify pie tool tip value")
        result_obj.verify_default_tooltip_values("wall1", "riser!s1!g0!mwedge!", expected_tooltip_list[1], "Step 05: Verify pie tool tip value")
        result_obj.verify_default_tooltip_values("wall1", "riser!s2!g0!mwedge!", expected_tooltip_list[2], "Step 05: Verify pie tool tip value")
        result_obj.verify_number_of_pie_segments('wall1', 1, 3, msg='Step 05 : Verify number of pie segments displayed')
        expected_legend_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_legends('wall1', expected_legend_list, msg='Step 05 : ')
        expected_label_list=['Unit Sales']
        result_obj.verify_riser_pie_labels_and_legends('wall1', expected_label_list, msg='Step 05 : ')
        rollupobj.verify_arChartMenu('wall1', msg='Step 05 : Verify menu items')
        
        """
            Step 06 : Click First dropdown button > New
        """
        rollupobj.create_new_item(0, 'New', False, 'wall1')
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', color='dark_green', msg='Step 06 : Verify the pie chart color Green')
        utillobj.verify_chart_color('wall1', 'riser!s1!g0!mwedge!', color='bar_green', msg='Step 06 : Verify the pie chart color Bar green')
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', color='bar_blue', msg='Step 06 : Verify the pie chart color bar_blue')
        parent_css='div[id="wall2"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        expected_tooltip_list=[['Coffee', 'Unit Sales:1.4M', '37.3% of 3.7M'],['Food', 'Unit Sales:1.4M', '37.5% of 3.7M'],['Gifts', 'Unit Sales:928K', '25.2% of 3.7M']]
        result_obj.verify_default_tooltip_values("wall2", "riser!s0!g0!mwedge!", expected_tooltip_list[0], "Step 06: Verify pie tool tip value")
        result_obj.verify_default_tooltip_values("wall2", "riser!s1!g0!mwedge!", expected_tooltip_list[1], "Step 06: Verify pie tool tip value")
        result_obj.verify_default_tooltip_values("wall2", "riser!s2!g0!mwedge!", expected_tooltip_list[2], "Step 06: Verify pie tool tip value")
        
        """
            Step 07 : From the New window, click Bar.
        """
        rollupobj.click_chart_menu_bar_items('wall2', 1)
        time.sleep(3)
        parent_css='div[id="wall2"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('wall2','riser!s0!g0!mbar!', color='bar_blue', msg='Step 07 : Verify the bar color')
        expected_tooltip_list=[['Unit Sales:1.4M', 'X:Coffee'],['Unit Sales:1.4M', 'X:Food'],['Unit Sales:928K', 'X:Gifts']]
        result_obj.verify_default_tooltip_values("wall2", "riser!s0!g0!mbar!", expected_tooltip_list[0], "Step 07: Verify bar tool tip value")
        result_obj.verify_default_tooltip_values("wall2", "riser!s0!g1!mbar!", expected_tooltip_list[1], "Step 07: Verify bar tool tip value")
        result_obj.verify_default_tooltip_values("wall2", "riser!s0!g2!mbar!", expected_tooltip_list[2], "Step 07: Verify bar tool tip value")
        result_obj.verify_number_of_riser('wall2', 1, 3, msg='Step 07 : Verify number of risers displayed')
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        expected_xval_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_chart_XY_labels('wall2', expected_xval_list, expected_yval_list, msg='Step 07 : Labels ')
        """
            Step 08 : From the New window, click Pie.

        """
        rollupobj.click_chart_menu_bar_items('wall2', 2)
        time.sleep(3)
        parent_css='div[id="wall2"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('wall2', 'riser!s2!g0!mwedge!', color='dark_green', msg='Step 08 : Verify the pie chart color Green')
        utillobj.verify_chart_color('wall2', 'riser!s1!g0!mwedge!', color='bar_green', msg='Step 08 : Verify the pie chart color Bar green')
        utillobj.verify_chart_color('wall2', 'riser!s0!g0!mwedge!', color='bar_blue', msg='Step 08 : Verify the pie chart color bar_blue')
        expected_tooltip_list=[['Coffee', 'Unit Sales:1.4M', '37.3% of 3.7M'],['Food', 'Unit Sales:1.4M', '37.5% of 3.7M'],['Gifts', 'Unit Sales:928K', '25.2% of 3.7M']]
        result_obj.verify_default_tooltip_values("wall2", "riser!s0!g0!mwedge!", expected_tooltip_list[0], "Step 08: Verify pie tool tip value")
        result_obj.verify_default_tooltip_values("wall2", "riser!s1!g0!mwedge!", expected_tooltip_list[1], "Step 08: Verify pie tool tip value")
        result_obj.verify_default_tooltip_values("wall2", "riser!s2!g0!mwedge!", expected_tooltip_list[2], "Step 08: Verify pie tool tip value")
        result_obj.verify_number_of_pie_segments('wall2', 1, 3, msg='Step 08 : Verify number of pie segments displayed')
        expected_legend_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_legends('wall1', expected_legend_list, msg='Step 08 : ')
        expected_label_list=['Unit Sales']
        result_obj.verify_riser_pie_labels_and_legends('wall1', expected_label_list, msg='Step 08 : ')
        """
            Step 09 : From the New window, click Line.

        """
        rollupobj.click_chart_menu_bar_items('wall2', 3)
        time.sleep(3)
        parent_css='div[id="wall2"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('wall2','riser!s0!g0!mline!', color='bar_blue', attribute_type='stroke', msg='Step 09 : Verify the line color')
        expected_yval_list=['0', '0.4M', '0.8M', '1.2M', '1.6M']
        expected_xval_list=['Coffee','Food','Gifts']
        result_obj.verify_riser_chart_XY_labels('wall2', expected_xval_list, expected_yval_list, msg='Step 09 : Labels ')
        """
            Step 10 : From the New window, click Scatter.

        """
        rollupobj.click_chart_menu_bar_items('wall2', 4)
        time.sleep(3)
        parent_css='div[id="wall2"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('wall2','riser!s0!g0!mmarker!', color='bar_blue', attribute_type='stroke', msg='Step 10 : Verify the Scatter color')
        utillobj.verify_chart_color('wall2','riser!s0!g1!mmarker!', color='bar_blue', attribute_type='stroke', msg='Step 10 : Verify the Scatter color')
        utillobj.verify_chart_color('wall2','riser!s0!g2!mmarker!', color='bar_blue', attribute_type='stroke', msg='Step 10 : Verify the Scatter color')
        
        expected_tooltip_list=[['Unit Sales', 'X:Coffee', 'Y:1.4M'],['Unit Sales', 'X:Food', 'Y:1.4M'],['Unit Sales', 'X:Gifts', 'Y:928K']]
        result_obj.verify_default_tooltip_values("wall2", "riser!s0!g0!mmarker!", expected_tooltip_list[0], "Step 10: Verify scatter tool tip value")
        result_obj.verify_default_tooltip_values("wall2", "riser!s0!g1!mmarker!", expected_tooltip_list[1], "Step 10: Verify scatter tool tip value")
        result_obj.verify_default_tooltip_values("wall2", "riser!s0!g2!mmarker!", expected_tooltip_list[2], "Step 10: Verify scatter tool tip value")

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
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        rollupobj.click_chart_menu_bar_items('wall1', 5)
        time.sleep(3)
        parent_css='div[id="wall1"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        ia_runobj.create_table_data_set('#ITableData1',Test_Case_ID+'_001.xlsx')
        ia_runobj.verify_table_data_set('#ITableData1',Test_Case_ID+'_001.xlsx','Step 11: Verify C2227777_001.xlsx output')
        miscelanousobj.verify_page_summary(1,'3of3records,Page1of1','Step 11 : Verify page summary') 
        """
            Step 12 : Click Advance Chart/Rollup icon at the top(7th option)
            
            Cancel Advance Chart pop up. 

        """
        rollupobj.click_chart_menu_bar_items('wall1', 6)
        time.sleep(3)
        rollupobj.verify_arChartMenu('wall1', msg='Step 12 : Verify the menu items')
        popup_index='2'
        miscelanousobj.close_popup_dialog(popup_index)
        time.sleep(3)
        """
            Step 13 : Click Original chart icon. 
            
        """
        rollupobj.click_chart_menu_bar_items('wall1', 7)
        time.sleep(3)
        parent_css='div[id="wall1"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        utillobj.verify_chart_color('wall1', 'riser!s2!g0!mwedge!', color='dark_green', msg='Step 13 : Verify the pie chart color Green')
        utillobj.verify_chart_color('wall1', 'riser!s1!g0!mwedge!', color='bar_green', msg='Step 13 : Verify the pie chart color Bar green')
        utillobj.verify_chart_color('wall1', 'riser!s0!g0!mwedge!', color='bar_blue', msg='Step 13 : Verify the pie chart color bar_blue')
        expected_tooltip_list=[['Coffee', 'Unit Sales:1.4M', '37.3% of 3.7M'],['Food', 'Unit Sales:1.4M', '37.5% of 3.7M'],['Gifts', 'Unit Sales:928K', '25.2% of 3.7M']]
        result_obj.verify_default_tooltip_values("wall1", "riser!s0!g0!mwedge!", expected_tooltip_list[0], "Step 13: Verify pie tool tip value")
        result_obj.verify_default_tooltip_values("wall1", "riser!s1!g0!mwedge!", expected_tooltip_list[1], "Step 13: Verify pie tool tip value")
        result_obj.verify_default_tooltip_values("wall1", "riser!s2!g0!mwedge!", expected_tooltip_list[2], "Step 13: Verify pie tool tip value")
        """
            Step 14 : Click Rollup icon on the output type and click Freeze icon.

        """
        rollupobj.click_chart_menu_bar_items('wall1', 5)
        time.sleep(3)
        parent_css='div[id="wall1"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        """
            Step 15 : Click Aggregation icon.
            
            Click Avg to change the aggregation type to Average Unit Sales.

        """
        rollupobj.click_chart_menu_bar_items('wall1', 8)
        time.sleep(5)
        parent_css='div[id="wall1"]'
        result_obj.wait_for_property(parent_css, 1, expire_time=10)
        rollupobj.select_aggregate_function('wall1', 1, 'Avg', elem_index=9, verify=True,msg=' Step 15 : Verify the aggregate function')
        ia_runobj.verify_table_data_set('#ITableData1', Test_Case_ID+'_002.xlsx', msg='Verify the average table data set')
        
        """
            Step 16:Dismiss the window and logout.
                http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """   
        time.sleep(5)
        
                
if __name__ == '__main__':
    unittest.main()