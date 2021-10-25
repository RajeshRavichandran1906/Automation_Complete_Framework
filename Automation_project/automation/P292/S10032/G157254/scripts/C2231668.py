'''
Created on Dec 01, 2017

@author: PM14587
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case ID : http://172.19.2.180/testrail/index.php?/cases/view/2231668
Test Case Name : Report with Dynamic Group
'''
import unittest, time
from common.lib import utillity
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_run,ia_resultarea

class C2231668_TestClass(BaseTestCase):

    def test_C2231668(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2231668'
        
        """   
           CLASS OBJECTS     
        """
        iarun=ia_run.IA_Run(self.driver)
        core_met = CoreMetaData(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
          
        """
            Step 01 : Launch IA Report mode with wf_retail_lite: http://machine:port/ibi_apps/ia?tool=report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_5', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 'Sum',metaobj.home_page_long_timesleep)
#         resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        
        """
            Step 02 : Drag "Cost of Goods" into the "Sum" bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Cost of Goods', 1, "Sum", 0)
#         metaobj.datatree_field_click('Cost of Goods',2,1)
#         resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='Cost of Goods')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 'Cost of Goods',metaobj.home_page_long_timesleep)
        
        """
            Step 03 : Drag "Customer,Business,Region" into the "Across" bucket
        """
        core_met.collapse_data_field_section('Filters and Variables')
        metaobj.drag_drop_data_tree_items_to_query_tree('Customer,Business,Region',1,'Across',0)
#         metaobj.drag_drop_data_tree_items_to_query_tree('Customer,Business,Region',1,'Across',0,target_cord='middle')
        #resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(6)", 1,30,string_value='Customer,Business,Region')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(6)", 'Customer,Business,Region',metaobj.home_page_long_timesleep)
        
        """
            Step 04 :Drag "Customer,Country" into the "By" bucket
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Customer,Country',1,'By',0)
#         metaobj.datatree_field_click('Customer,Country',2,1)
        #resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='Customer,Country')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 'Customer,Country',metaobj.home_page_long_timesleep)
        
        """
            Step 04.1 : Verify preview 
        """
        iaresult.verify_across_report_data_set('TableChart_1',3,5, 45,5,Test_Case_ID+'_DataSet_01.xlsx','Step 04.1 : Verify preview output')
        
        """
            Step 05 : Right-click "Customer,Country" in "By" bucket > Select "Create Group..."
        """
        metaobj.querytree_field_click('Customer,Country',1,1,'Create Group...')
        
        """
            Step 06 : Multi-select values "Canada" and "United States" > Click "Group"
        """
        metaobj.create_large_ia_group('Group', ['Canada','United States'],42,close_button='ok')
        #resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='COUNTRY_NAME_1')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 'COUNTRY_NAME_1',metaobj.home_page_long_timesleep)
        
        """
            Step 07 : Click OK
            Step 08 : Verify Query pane and Preview
        """
        #iaresult.create_across_report_data_set('TableChart_1',2,5, 43,5,Test_Case_ID+'_DataSet_02.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1',2,5, 43,5,Test_Case_ID+'_DataSet_02.xlsx','Step 08.1 : Verify Preview')
        metaobj.verify_query_panel_all_field(['Report (wf_retail_lite)', 'Sum', 'Cost of Goods', 'By', 'COUNTRY_NAME_1', 'Across', 'Customer,Business,Region'],'Step 08.2 : Verify Query pane')
        
        """
            Step 09 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("table[summary]>tbody>tr:nth-child(1)>td:nth-child(2)", 1,40,string_value='EMEA')
        
        """
            Step 09.1 :  Verify output
        """       
        #iarun.create_table_data_set('table[summary]',Test_Case_ID+'_DataSet_03.xlsx')#,'Step 09.1 : Verify output')
        iarun.verify_table_data_set('table[summary]',Test_Case_ID+'_DataSet_03.xlsx','Step 09.1 : Verify output')

        """
            Step 10 : Click IA > Save As > "C2231668" > Click Save
        """
        utillobj.switch_to_default_content(3)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 11: Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
        utillobj.infoassist_api_logout()
        
        """
            Step 12 : Reopen FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10032%2FC2231668.fex&tool=report
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'report','P292/S10032_infoassist_5',mrid='mrid', mrpass='mrpass')
#         resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='COUNTRY_NAME_1')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 'COUNTRY_NAME_1',metaobj.home_page_long_timesleep)
        time.sleep(2)
        
        """
            Step 13 : Verify Query pane and Preview
        """
       
        iaresult.verify_across_report_data_set('TableChart_1',2,5, 43,5,Test_Case_ID+'_DataSet_02.xlsx','Step 13.1 : Verify Preview')
        metaobj.verify_query_panel_all_field(['Report (wf_retail_lite)', 'Sum', 'Cost of Goods', 'By', 'COUNTRY_NAME_1', 'Across', 'Customer,Business,Region'],'Step 13.2 : Verify Query pane')
        time.sleep(3)
        
        
    if __name__=='__main__' :
        unittest.main()