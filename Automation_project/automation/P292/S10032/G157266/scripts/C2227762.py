'''
Created on Jun 25, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227762
Testcase Name :  Report-Other: Verify correct AHTMLTAB format output for Rollup tool(82xx)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import active_miscelaneous, ia_run, active_tools
from common.lib import utillity, core_utility
from common.wftools import active_report
from common.lib.global_variables import Global_variables

class C2227762_TestClass(BaseTestCase):

    def test_C2227762(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227762'
        
        utillobj = utillity.UtillityMethods(self.driver)
        core_utillobj = core_utility.CoreUtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        act_tool = active_tools.Active_Tools(self.driver)
        iarun_obj = ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="ahtmltab.fex"
        obrowser=utillobj.parseinitfile('browser')
        
        """
            Step 01 : Sign in to WebFOCUS
            http://machine:port/{alias}
            Step 02 : Expand folder P292_S10032_G157266
            Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTMLOFF&BIP_item=ahtmltab.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="COUNTRY")
        Global_variables.current_working_area_browser_y=self.driver.execute_script('return screen.availHeight - window.innerHeight')
        
        """
            Step 03 : Verify the report is generated.
            Verify correct output displayed on run.
            All four ahtml reports appear on the same output report: 
            Multiverb Report, Simple by Report, Across Test, SubTotal Test.
        """
        miscelanousobj.verify_page_summary(0, '13of13records,Page1of1', "Step 3.1:  13of13records,Page1of1 Active Report. - page summary verification of table 1")
        miscelanousobj.verify_page_summary(1, '18of18records,Page1of1', "Step 3.2:  18of18records,Page1of1 Active Report. - page summary verification of table 2")
        miscelanousobj.verify_page_summary(2, '10of10records,Page1of1', "Step 3.3:  10of10records,Page1of1 Active Report. - page summary verification of table 3")
        miscelanousobj.verify_page_summary(3, '18of18records,Page1of1', "Step 3.4:  18of18records,Page1of1 Active Report. - page summary verification of table 4")
        table_css="#ITableData0"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds01.xlsx")
        utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds01.xlsx")
        table_css="#ITableData1"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds02.xlsx")
        table_css="#ITableData2"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds03.xlsx")
        table_css="#ITableData3"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds04.xlsx")
        utillobj.verify_table_data(table_css, Test_Case_ID+"_Ds04.xlsx")
       
        """
            Step 04 : In Multiverb Report click drop-down menu under any column heading. Eg: Country, select Chart/Rollup Tool option.
        """
        ele=self.driver.find_element_by_css_selector("#ITableData0  #popid0_0 img")
        core_utillobj.left_click(ele)
        time.sleep(1)
        if obrowser == "IE":
            expected_menu_list=['Sort Ascending', 'Sort Descending', 'Global Filter','Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Send as E-mail', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        else :    
            expected_menu_list=['Sort Ascending', 'Sort Descending', 'Global Filter', 'Filter', 'Calculate', 'Chart', 'Rollup', 'Pivot (Cross Tab)', 'Hide Column', 'Grid Tool', 'Chart/Rollup Tool', 'Pivot Tool', 'Show Records', 'Comments', 'Save Changes', 'Export', 'Print', 'Window', 'Restore Original']
        miscelanousobj.verify_menu_items('ITableData0', 0, None, expected_menu_list, msg=' Step 04:01 : Verify the menu items')
        time.sleep(1)
        
        #select_menu_items function is not working for ahtmltab fex. so given in script level to select menu
        ele=self.driver.find_element_by_css_selector("#ITableData0  #popid0_0 img")
        core_utillobj.left_click(ele)
        
        elem = self.driver.find_element_by_css_selector("#dt0_0_0[style*='block'] table tr#t0_0_0_12")
        core_utillobj.left_click(elem)
        
        """
            Verify Chart/Rollup tool is opened.
        """
        utillobj.synchronize_with_visble_text("#wall1 #wtop1 #wtitle1", "Chart/Rollup Tool", 20)
        
        menu=['Bar','Pie','Line','Scatter','Rollup']
        miscelanousobj.verify_arChartToolbar('wall1', menu, 'Step 04:02 : Verify the menu items', custom_css=".arToolMenuBar div[title]")
        
        """
            Step 05 : Under tool pop up, drag and drop COUNTRY and CAR to the Group By area, SALES(first sales field) to the Mesures area. Select Rollup from the toolbar and click OK
        """
        act_tool.chart_rollup_tool_drag_drop_items('charttool1', 'Columns', 'COUNTRY', 1, 'Group By', 0)
        act_tool.chart_rollup_tool_drag_drop_items('charttool1', 'Columns', 'CAR', 1, 'Group By', 1)
        act_tool.chart_rollup_tool_drag_drop_items('charttool1', 'Columns', 'SALES', 1, 'Measure', 0)
        time.sleep(1)
        
        """ Click on Rollup icon """
        elem=self.driver.find_element_by_css_selector("#charttool1 [title='Rollup']")
        core_utillobj.left_click(elem)
        
        btns=self.driver.find_elements_by_css_selector("#charttoolt1 .arToolButton")
        list_btn=[elem.text.strip() for elem in btns]
        btns[list_btn.index('Ok')].click()
        utillobj.synchronize_with_visble_text("#wall2 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle", "SALES by COUNTRY, CAR", 15)
        
        actual_title=self.driver.find_element_by_css_selector("#wall2 div.arWindowBar>table>tbody>tr>td.arWindowBarTitle").text
        cond=actual_title.strip()=="SALES by COUNTRY, CAR"
        utillobj.asequal(True, cond, "Step 05:01:Verify rollup report title")
         
        """
            Verify correct rollup report is returned.
        """
        table_css="#ITableData4"
#         iarun_obj.create_table_data_set(table_css, Test_Case_ID+"_Ds05.xlsx")
        iarun_obj.verify_table_data_set(table_css, Test_Case_ID+"_Ds05.xlsx", "Step 05:02::Verify rollup report data")
        
        miscelanousobj.verify_page_summary(4, '10of10records,Page1of1', "Step 5:03: 10of10records,Page1of1 Active Report. - page summary verification of rollup report table")
        
        
        """
            Step 06 : Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
    

if __name__ == "__main__":
    unittest.main()