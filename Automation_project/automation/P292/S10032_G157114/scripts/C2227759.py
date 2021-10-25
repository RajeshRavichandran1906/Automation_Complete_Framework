'''
Created on Jan 02, 2018

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227759
TestCase Name = Report-Grid: Verify that the Grid Tool displays and hides fields.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run, active_tools
from common.lib import utillity
from common.wftools import active_report

class C2227759_TestClass(BaseTestCase):

    def test_C2227759(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227759'
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        act_tool = active_tools.Active_Tools(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_OFF_001a.fex"
        report_dataset_name="AHTML_OFF_001a"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 : Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=AHTML_OFF_001.fex
        """
        
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 tr:nth-child(2) td:nth-child(2)", synchronize_visible_element_text="C141")
        
        """
            Step 03 : Verify the report is generated
        """
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 03.1 : Verify page summary')
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.3: verify report data")
        
        """
            Step 04 : Click State > Grid Tool
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        resultobj.wait_for_property("#wall1 .arWindowBarTitle>span",1,8,string_value='Grid Tool') 
        
        """
            Step 04.1 : Verify Grid Tool pop up opened. 
        """
        miscelanousobj.verify_popup_appears('wall1','Grid Tool', 'Step 04.1 : Verify Grid Tool pop up opened')
        miscelanousobj.move_active_popup('1', 550, 40)
        
        """
            Step 04.2 : Verify that all the columns are in the same order as shown under a report.
        """
        expected_columns1=['Column Order', 'Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        act_tool.grid_tool_verify_columns('gridtoolt1', 1, expected_columns1, 'Step 04.2 : Verify that all the columns are in the same order as shown under a report')
        expected_columns2=['Sort Order', 'Drag Column Here', 'Group sort columns']
        act_tool.grid_tool_verify_columns('gridtoolt1', 2, expected_columns2, 'Step 4.2a : Verify Sort order columns')
        
        """
            Step 04.3 : Verify Hide icon is displayed next to each column (HIDE=OFF by default)
        """
        for item in ['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales'] :
            act_tool.verify_grid_tool_show_hide_column('gridtoolt1', item, 1, 'Hide Column', 'Step 04.3 : Verify Hide icon is displayed next to '+item+ 'column')
        
        
        """
            Step 05 : Drag and drop Category and Product ID to Sort Order section.Click OK.
        """
        act_tool.grid_tool_drag_drop_items('gridtoolt1', 'Category', 1, 0)
        act_tool.grid_tool_drag_drop_items('gridtoolt1', 'Product ID', 1, 1)
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
#         iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step01.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step01.xlsx', 'Step 05.1 : Verify Product column is no longer displayed on the report.')
        
        """
            Step 06 : From the Grid Tool, check Group Sort columns checkbox. Click OK.
        """
        
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        resultobj.wait_for_property("#wall1 .arWindowBarTitle>span",1,8,string_value='Grid Tool') 
        act_tool.grid_tool_select_group_checkbox('gridtoolt1')
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
#         iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step02.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step02.xlsx', 'Step 06.1 : Verify Product column is no longer displayed on the report.')
        
        """
            Step 07 :From the Grid Tool, check both Subtotal boxes for Category and Product ID. 
            Change the Aggregation Type in Column Order section by clicking the aggregation symbol and changing both to SUM.Click OK.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        resultobj.wait_for_property("#wall1 .arWindowBarTitle>span",1,8,string_value='Grid Tool') 
        css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) table>tbody>tr:nth-child(3) div[onclick*='changeSubCalc']"
        elem=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(elem, 'left', click_type=0)
        css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) table>tbody>tr:nth-child(5) div[onclick*='changeSubCalc']"
        elem=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(elem, 'left', click_type=0)
        act_tool.grid_tool_select_aggregate_function('gridtoolt1', 'Unit Sales', 1, 'Sum')
        act_tool.grid_tool_select_aggregate_function('gridtoolt1', 'Dollar Sales', 1, 'Sum')
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
        
        """
            Expect to see the following report, now with Subtotals for both Unit Sales and Dollar Sales, at both the Product ID and Category sort breaks.
            Expect that both Unit Sales and Dollar Sales display the requested SUM operation at the top of their columns.
        """
        
#         iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step03.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step03.xlsx', 'Step 07.1 : Verify Product column is no longer displayed on the report.')
        
        """
            Step 08 :Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()
        