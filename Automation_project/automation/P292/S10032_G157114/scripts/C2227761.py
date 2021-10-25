'''
Created on December 29, 2017

@author: Praveen Ramkumar/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227761
TestCase Name =Report-Other: Verify Grid Tool works in AHTML.(82xx)
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run, active_tools
from common.lib import utillity
from common.wftools import active_report

class C2227761_TestClass(BaseTestCase):

    def test_C2227761(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227761'
        driver=self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        act_tool = active_tools.Active_Tools(self.driver)
        iarun = ia_run.IA_Run(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        fex_name ="AHTML_001.fex"
        
        """
            Step 01 : Sign in to WebFOCUS as a Basic user http://machine:port/{alias}
            Step 02 : Expand folder P292_S10032_G157266 Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G157266%252FAHTML_OFF&BIP_item=Ahtml_001.fex
        """
        
        active_reportobj.run_active_report_using_api(fex_name, column_css="#ITableData0 #TCOL_0_C_0 span", synchronize_visible_element_text="COUNTRY")
        
        """
            Step 03 : Verify the report is generated
        """
        miscelanousobj.verify_page_summary('0','5of5records,Page1of1','Step 03.1 : Verify page summary')
#         utillobj.create_data_set('ITableData0','I0r','C2227761_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0','I0r','C2227761_Ds01.xlsx', 'Step 03.2:Verify the report is generated.')
        
        """
            Step 04 : Click on SALES and select Grid Tool'
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
        expected_columns1=['Column Order', 'COUNTRY', 'RETAIL_COST', 'DEALER_COST','SALES','ABC']
        act_tool.grid_tool_verify_columns('gridtoolt1', 1, expected_columns1, 'Step 04.2 : Verify that all the columns are in the same order as shown under a report')
        
        expected_columns2=['Sort Order', 'Drag Column Here', 'Group sort columns']
        act_tool.grid_tool_verify_columns('gridtoolt1', 2, expected_columns2, 'Step 4.2a : Verify Sort order columns')
        
        """
            Step 04.3 : Verify Hide icon is displayed next to each column (HIDE=OFF by default)
        """
        for item in ['COUNTRY', 'SALES', 'RETAIL_COST', 'DEALER_COST', 'ABC'] :
            act_tool.verify_grid_tool_show_hide_column('gridtoolt1', item, 1, 'Hide Column', 'Step 04.3 : Verify Hide icon is displayed next to '+item+ 'column')
        
        
        """
            Step 05:Click the calculation icon next to the columns "RETAIL_COST" and "DEALER_COST" and change the calculation to SUM for both fields.
        """
        act_tool.grid_tool_select_aggregate_function('gridtoolt1', 'RETAIL_COST', 1, 'Sum')
        act_tool.grid_tool_select_aggregate_function('gridtoolt1', 'DEALER_COST', 1, 'Sum')
        
        """
            Step 06:Left-click and drag the columns "COUNTRY" and "SALES" from the Column Order into the Sort Order section. Click Group sort columns to group the report by columns in the Sort Order section
            Select the Subtotal check box next to the column "COUNTRY" and click OK   
            Note: For different WV settings we are displaying these screenshots.
        """
        
        act_tool.grid_tool_drag_drop_items('gridtoolt1', 'COUNTRY', 1, 0)
        act_tool.grid_tool_drag_drop_items('gridtoolt1', 'SALES', 1, 1)
        act_tool.grid_tool_select_group_checkbox('gridtoolt1')
        css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) table>tbody>tr:nth-child(3) div[onclick*='changeSubCalc']"
        elem=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(elem, 'left', click_type=0)
        css="#gridtoolt1 > tbody > tr:nth-child(1) > td:nth-child(2) table>tbody>tr:nth-child(5) div[onclick*='changeSubCalc']"
        elem=driver.find_element_by_css_selector(css)
        utillobj.click_on_screen(elem, 'left', click_type=0)
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
#         iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step02.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step02.xlsx', 'Step 06.1 : Verify Product column is no longer displayed on the report.')
        
        """
            Step 07:Dismiss the window and logout.http://machine:port/ibi_apps/service/wf_security_logout.jsp       
        """
        
if __name__=='__main__' :
    unittest.main()