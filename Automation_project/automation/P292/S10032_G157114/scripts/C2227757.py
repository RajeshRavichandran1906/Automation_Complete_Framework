'''
Created on December 29, 2017

@author: Prabhakaran/Updated by : Bhagavathi

Test Suite =http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227757
TestCase Name = Report-Grid: Verify that the Grid Tool displays and hides fields.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea, active_miscelaneous, ia_run, active_tools
from common.lib import utillity
from common.wftools import active_report

class C2227757_TestClass(BaseTestCase):

    def test_C2227757(self):
        
        """
            TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2227757'
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
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 03.2: verify report data")
        
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
            Step 05 : Click Hide icon for Product on Grid Tool and click OK
        """
        act_tool.grid_tool_show_hide_column('gridtoolt1', 'Product', 1, 'Hide Column')
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
        
        """
            Step 05.1 : Verify Product column is no longer displayed on the report.
        """
        #iarun.create_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step05.xlsx')
        iarun.verify_table_data_set('#ITableData0',Test_Case_ID+'_DataSet_Step05.xlsx', 'Step 05.1 : Verify Product column is no longer displayed on the report.')
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 05.2 : Verify page summary')
        
        """
            Step 06 : Click dropdown menu from State column and open Grid Tool
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        resultobj.wait_for_property("#wall1 .arWindowBarTitle>span",1,8,string_value='Grid Tool')
        
        """
            Step 06.1 : Verify Product column shows HIDE=ON on hide/Show icon.
        """
        act_tool.verify_grid_tool_show_hide_column('gridtoolt1', 'Product', 1, 'Show Column', 'Step 06.1 : Verify Product column shows HIDE=ON on hide/Show icon.')
        
        """
            Step 07 : Click Hide/Show icon again on Grid Tool and click OK
        """
        act_tool.grid_tool_show_hide_column('gridtoolt1', 'Product', 1, 'Show Column')
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
        
        """
            Step 07.1 : Verify HIDE=OFF and Product column is displayed on the report.
        """
        utillobj.verify_data_set('ITableData0', 'I0r', report_dataset_name+".xlsx", "Step 07.1: verify report data shows 107 records")
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 07.2 : Verify page summary')
        
        """
            Step 08 : From any column drop-down menu open Grid Tool, drag the Category field under the Product field, then click OK.
        """
        miscelanousobj.select_menu_items('ITableData0', 1, 'Grid Tool')
        resultobj.wait_for_property("#wall1 .arWindowBarTitle>span",1,8,string_value='Grid Tool')
        act_tool.drag_drop_grid_tool_column('gridtoolt1', 'Category', 'Product')
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
        
        """
            Step 08.1 : Expect to see the report, with new column order of Product ID, Product, then Category, State, Unit Sales & Dollar Sales.
            Also verify that the order of the report is still in Category sequence, that is Coffee, then Food and lastly Gifts
        """
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_DataSet_Step08.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_DataSet_Step08.xlsx', "Step 08.1: Verify expect to see the report, with new column order of Product ID, Product, then Category, State, Unit Sales & Dollar Sales")
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 08.2 : Verify page summary')
        
        """
            Step 09 : From any column dropdown menu open Grid Tooll, drag the State field under Sort Order and click OK.
        """
        miscelanousobj.select_menu_items('ITableData0', 2, 'Grid Tool')
        resultobj.wait_for_property("#wall1 .arWindowBarTitle>span",1,8,string_value='Grid Tool')
        act_tool.grid_tool_drag_drop_items('gridtoolt1', 'State', 1, 0)
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
        
        """
            Step 09.1 : Expect to see the report now in State order, even though the columns are Product ID, Product, State...
        """
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_DataSet_Step09.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_DataSet_Step09.xlsx', "Step 09.1: Verify expect to see the report now in State order, even though the columns are Product ID, Product, State..")
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 09.2 : Verify page summary')
        
        """
            Step 10 : From any column dropdown menu open Grid Tool, check the box for Group Sort Columns. Click OK.
        """
        miscelanousobj.select_menu_items('ITableData0', 3, 'Grid Tool')
        resultobj.wait_for_property("#wall1 .arWindowBarTitle>span",1,8,string_value='Grid Tool')
        act_tool.grid_tool_select_group_checkbox('gridtoolt1')
        expected_columns1=['Column Order', 'State', 'Product ID', 'Product', 'Category', 'Unit Sales', 'Dollar Sales']
        act_tool.grid_tool_verify_columns('gridtoolt1', 1, expected_columns1, 'Step 10.1 : Verify grid columns')
        act_tool.grid_tool_close('gridtoolt1', 'Ok')
        time.sleep(3)
        
        """
            Step 10.1 : Expect to see the report now with State displayed first, as a true sort column, with duplicate values suppressed.
        """
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_DataSet_Step10.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_DataSet_Step10.xlsx', "Step 09.1: 'Step 10.1 : Verify expect to see the report now with State displayed first, as a true sort column, with duplicate values suppressed.")
        miscelanousobj.verify_page_summary('0','107of107records,Page1of2','Step 10.2 : Verify page summary')
        
        """
            Step 11 : Dismiss the window and logout http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__=='__main__' :
    unittest.main()