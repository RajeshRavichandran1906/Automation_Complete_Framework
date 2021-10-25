'''
Created on May 9, 2018

@author: BM13368
Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_id=157266
TestCase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227745
TestCase Name : Report-Other: Verify correct AHTMLTAB format output for Rollup tool(82xx)

'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run,active_tools
from common.wftools import active_report
from common.lib import utillity, core_utility
from common.lib.global_variables import Global_variables

class C2227745_TestClass(BaseTestCase):

    def test_C2227745(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227745'
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = core_utility.CoreUtillityMethods(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        act_toolobj=active_tools.Active_Tools(self.driver)
        obrowser=utillobj.parseinitfile('browser')
        ia_runobj=ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name="AHTMLTAB_2.fex"
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="COUNTRY")
        Global_variables.current_working_area_browser_y=self.driver.execute_script('return screen.availHeight - window.innerHeight')
        
        """
            Step 03:Verify the report is generated.
            Verify correct output displayed on run.
            All four ahtml reports appear on the same output report: 
            Multiverb Report, Simple by Report, Across Test, SubTotal Test.
        """
        miscelanousobj.verify_page_summary(0, '13of13records,Page1of1', "Step 3.1:  13of13records,Page1of1 Active Report. - page summary verification of table 1")
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', "Step 3.2:  18of18records,Page1of1 Active Report. - page summary verification of table 2")
        miscelanousobj.verify_page_summary(2, '10of10records,Page1of1', "Step 3.3:  10of10records,Page1of1 Active Report. - page summary verification of table 3")
        miscelanousobj.verify_page_summary(3, '18of18records,Page1of1', "Step 3.4:  18of18records,Page1of1 Active Report. - page summary verification of table 4")
        table_css="#ITableData0"
        utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds01.xlsx")
        table_css="#ITableData1"
        ia_runobj.verify_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx", msg='Step 3.6 : Verify the table 2')
        table_css="#ITableData2"
        ia_runobj.verify_table_data_set(table_css, Test_Case_ID+"_Ds03.xlsx", msg='Step 3.7 : Verify the table 3')
        table_css="#ITableData3"
        ia_runobj.verify_table_data_set(table_css, Test_Case_ID+"_Ds04.xlsx", msg='Step 3.8 : Verify the table 4')
        
        """
            Step 04:IN the MULTI VERB AND BY TEST, in the upper left, click on the drop down arrow for Country
        """
        if obrowser == "IE":
            expected_menu_list=['Sort Ascending', 'Sort Descending', 'Global Filter','Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Send as E-mail', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        else :    
            expected_menu_list=['Sort Ascending', 'Sort Descending', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        miscelanousobj.verify_menu_items('ITableData0', 0, None, expected_menu_list, msg=' Step 3.1 : Verify the menu items')
        time.sleep(1)

        """
            Step 05:In Second report Simple By Report, click the arrow in the heading of column Country and select option Pivot Tool in drop-down menu
                        Verify Pivot tool is opened.
        """
        
        ele=self.driver.find_element_by_css_selector("#ITableData1  #popid1_0 img")
        core_utillobj.left_click(ele)
        elem = self.driver.find_element_by_css_selector("#dt1_0_0[style*='block'] table tr#t1_0_0_13")
        core_utillobj.left_click(elem)
        utillobj.synchronize_with_visble_text("#wall1 #wtop1 #wtitle1", "Pivot Tool", 25)
        
        """
        Step 06:In Pivot Tool dialog box drag and drop fields: BODYTYPE to the Group By area, CAR to the Across area and RETAIL_COST to the Measure area. 
        Click OK and expand the Pivot Table by dragging the bottom right corner to the right and down.
        """
        act_toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'BODYTYPE', 1, 'Group By', 0)
        act_toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'CAR', 1, 'Across', 0)
        act_toolobj.pivot_tool_drag_drop_items('pivottoolt1', 'Columns', 'RETAIL_COST', 1, 'Measure', 0)
        act_toolobj.pivot_tool_close('pivottoolt1', 'Ok')
        utillobj.synchronize_with_visble_text("#wall2 #wtop2 #wtitle2", "RETAIL_COST BY CAR, BODYTYPE", 25)
        utillobj.verify_pivot_data_set('piv2', Test_Case_ID+"_Ds00.xlsx",'Step 06.3: Verify Pivot table does not reflect any changes of the filter')
        
        """
            Step 07 : Close the pivot tool
            In the SIMPLE BY REPORT, click the arrow in the heading of column Country select option Chart/Rollup Tool from the drop-down menu
            Verify Chart/Rollup tool is opened.
        """
        elem=self.driver.find_element_by_css_selector("#wtop2  div[class='arWindowBar'] #WCS2 div[onclick*='closewin']")
        core_utillobj.left_click(elem)
        time.sleep(4)
        ele=self.driver.find_element_by_css_selector("#ITableData1  #popid1_0 img")
        core_utillobj.left_click(ele)
        elem = self.driver.find_element_by_css_selector("#dt1_0_0[style*='block'] table tr#t1_0_0_12")
        core_utillobj.left_click(elem)
        utillobj.synchronize_with_visble_text("#wall1 #wtop1 #wtitle1", "Chart/Rollup Tool", 25)
        menu=['Bar','Pie','Line','Scatter','Rollup']
        miscelanousobj.verify_arChartToolbar('wall1', menu, 'Step 7:01 : Verify the menu items', custom_css=".arToolMenuBar div[title]")
        time.sleep(3)
        
        """
        Step 08:Chart/Rollup Tool dialog opens with Bar chart selected by default in the top bar. 
        Drag and drop RETAIL_COST and DEALER_COST fields to the Measure box, CAR field to the Group By box. 
        Click OK button
        """
        act_toolobj.chart_rollup_tool_drag_drop_items('charttool1', 'Columns', 'CAR', 1, 'Group By', 0, mouse_speed=.75)
        act_toolobj.chart_rollup_tool_drag_drop_items('charttool1', 'Columns', 'RETAIL_COST', 1, 'Measure', 0, mouse_speed=.75)
        act_toolobj.chart_rollup_tool_drag_drop_items('charttool1', 'Columns', 'DEALER_COST', 1, 'Measure', 1, mouse_speed=.75)
        time.sleep(2)
        btns=self.driver.find_elements_by_css_selector("#charttoolt1 .arToolButton")
        list_btn=[elem.text.strip() for elem in btns]
        btns[list_btn.index('Ok')].click()
        time.sleep(7)
        
        """
        Verify Bar chart is displayed as an output.
        """
        actual_title=self.driver.find_element_by_css_selector("#wall2 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle").text
        cond=actual_title.strip()=="RETAIL_COST, DEALER_COST BY CAR"
        utillobj.asequal(True, cond, "Step 08:01:Verify chart rollup title")
        expected_toolbar_menu_list=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        miscelanousobj.verify_acitive_chart_toolbar("#wall2", expected_toolbar_menu_list, "Step 08:02:Verify active chart toolbarmenu")
        x_axis_legend1=self.driver.find_elements_by_css_selector("#wall2 .chartContainer div[title$='COST']")
        x_axis_legend=[elem.text.strip() for elem in x_axis_legend1 if elem != '']
        utillobj.asequal(x_axis_legend, ['RETAIL_COST','DEALER_COST'], "Step 08:03:Verify legends shows dealer_cost")
        act_chart_title=self.driver.find_element_by_css_selector("#wall2 .chartContainer div>div>div").text
        exp_title='RETAIL_COST, DEALER_COST BY CAR'
        utillobj.asequal(exp_title, act_chart_title, "Step 08:04:Verify chart title")
        act_labels_and_legends=self.driver.find_element_by_css_selector("#wall2 .chartContainer div").text.split('\n')
        exp_labels_legeneds=['RETAIL_COST', 'DEALER_COST', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH', '0', '20 K', '40 K', '60 K', '80 K', 'RETAIL_COST, DEALER_COST BY CAR']
        utillobj.asequal(exp_labels_legeneds, act_labels_and_legends, "Step 08:05:Verify chart legends and axis labels")
 
        """
            Step 09 : Click first image from the toolbar for More options select the stacked selection
        """ 
        click_item=self.driver.find_element_by_css_selector("#wmenu2 #cpop2")
        core_utillobj.left_click(click_item)
        select_stacked_item=self.driver.find_element_by_css_selector("span#set1_cpop2_0_3i_t")
        core_utillobj.left_click(select_stacked_item)
        utillobj.synchronize_with_number_of_element("#wall2 .chartContainer div[title$='COST']", 2, 25)
        
        """
        Verify bar chart is transformed into Stacked chart.
        """
        actual_title=self.driver.find_element_by_css_selector("#wall2 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle").text
        cond=actual_title.strip()=="RETAIL_COST, DEALER_COST BY CAR"
        utillobj.asequal(True, cond, "Step 09:01:Verify chart rollup title")
        expected_toolbar_menu_list=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Rollup', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        miscelanousobj.verify_acitive_chart_toolbar("#wall2", expected_toolbar_menu_list, "Step 09:02:Verify active chart toolbarmenu")
        x_axis_legend1=self.driver.find_elements_by_css_selector("#wall2 .chartContainer div[title$='COST']")
        x_axis_legend=[elem.text.strip() for elem in x_axis_legend1 if elem != '']
        utillobj.asequal(x_axis_legend, ['RETAIL_COST','DEALER_COST'], "Step 09:03:Verify legends shows dealer_cost")
        act_chart_title=self.driver.find_element_by_css_selector("#wall2 .chartContainer div>div>div").text
        exp_title='RETAIL_COST, DEALER_COST BY CAR'
        utillobj.asequal(exp_title, act_chart_title, "Step 09:04:Verify chart title")
        act_labels_and_legends=self.driver.find_element_by_css_selector("#wall2 .chartContainer div").text.split('\n')
        exp_labels_legeneds=['RETAIL_COST', 'DEALER_COST', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH', '0', '50 K', '100 K', '150 K', 'RETAIL_COST, DEALER_COST BY CAR']
        utillobj.asequal(exp_labels_legeneds, act_labels_and_legends, "Step 09:05:Verify chart legends and axis labels")
        
        """
        Step 10:On the SIMPLE BY REPORT screen, click the drop down button for COUNTRY and select Restore Original.
        """
        ele=self.driver.find_element_by_css_selector("#ITableData1  #popid1_0 img")
        core_utillobj.left_click(ele)
        elem = self.driver.find_element_by_css_selector("#dt1_0_0[style*='block'] table tr#t1_0_0_21")
        core_utillobj.left_click(elem)
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", "COUNTRY", 20)
        
        """
        Verify original report is restored.
        Also expect to see the Bar Chart removed.
        """
        table_css="#ITableData0"
        utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds01.xlsx")
        table_css="#ITableData1"
        ia_runobj.verify_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx", msg='Step 10.2 : Verify the table 2')
        table_css="#ITableData2"
        ia_runobj.verify_table_data_set(table_css, Test_Case_ID+"_Ds03.xlsx", msg='Step 10.3 : Verify the table 3')
        table_css="#ITableData3"
        ia_runobj.verify_table_data_set(table_css, Test_Case_ID+"_Ds04.xlsx", msg='Step 10.4 : Verify the table 4')
        actual_chart_title=self.driver.find_element_by_css_selector("#wall2").is_displayed()
        utillobj.asequal(False, actual_chart_title, "Step 10.5:Verify Bar chart removed")
        
if __name__ == '__main__':
    unittest.main()