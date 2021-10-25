'''
Created on Dec 06, 2017

@author: PM14587
Testcase Name : Verify Rank field option
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227457
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea,ia_run
from common.lib import utillity

class C2227457_TestClass(BaseTestCase):

    def test_C2227457(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2227457'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresult = ia_resultarea.IA_Resultarea(self.driver)
        iarun = ia_run.IA_Run(self.driver)
         
        """
            Step 01 : Launch IA Report mode: http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
        
        """
            Step 02 : Double click "Cost of Goods" and "Product,Category"
        """
        metaobj.datatree_field_click('Cost of Goods',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='Cost of Goods')
        
        metaobj.datatree_field_click('Product,Category',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='Product,Category')
        
        """
            Step 03 : Click on "Product,Category" in the Query pane > Select "Rank" in the Field Tab ribbon
        """
        metaobj.querytree_field_click('Product,Category',1,0)
        time.sleep(4)
        ribbonobj.select_ribbon_item('Field','rank')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(6)", 1,20,string_value='RANK')
        time.sleep(2)
        
        """
            Step 04 : Verify Rank in Query pane and Preview
        """
        #iaresult.create_across_report_data_set('TableChart_1 ',2,3, 7, 3,Test_Case_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1 ',2,3, 7, 3,Test_Case_ID+'_DataSet_01.xlsx','Step 04.1 : Verify Rank in Preview')
        expected_field=['Report (wf_retail_lite)', 'Sum', 'Cost of Goods', 'By', 'Product,Category', 'RANK', 'Across']
        metaobj.verify_query_panel_all_field(expected_field,'Step 04.2 : Verify Rank in Query pane')
        
        """
            Step 05 : Click on "Cost of Goods" in the Query pane > Select "Rank" in the Field Tab ribbon
        """
        metaobj.querytree_field_click('Cost of Goods',1,0)
        time.sleep(4)
        ribbonobj.select_ribbon_item('Field','rank')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(8)", 1,20,string_value='RANK')
        time.sleep(2)
        
        """
            Step 06 : Verify RANK Cost of Goods is displayed in the Query pane and Preview
        """
        #iaresult.create_across_report_data_set('TableChart_1 ',2,5, 7, 5,Test_Case_ID+'_DataSet_02.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1 ',2,5, 7, 5,Test_Case_ID+'_DataSet_02.xlsx','Step 06.1 : Verify RANK Cost of Goods is displayed in the Preview')
        expected_fields=['Report (wf_retail_lite)', 'Sum', 'Cost of Goods', 'By', 'Cost of Goods', 'RANK', 'Product,Category', 'RANK', 'Across']
        metaobj.verify_query_panel_all_field(expected_fields,'Step 06.2 : Verify RANK Cost of Goods is displayed in the Query')
        
        """
            Step 07 : Click "Save" > save as "C2227457" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 08 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 09 : Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227457.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'report','P292/S10032_infoassist_6',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
        
        """
            Step 10 : Verify Query pane and Preview
        """
        iaresult.verify_across_report_data_set('TableChart_1 ',2,5, 7, 5,Test_Case_ID+'_DataSet_02.xlsx','Step 10.1 : Verify Preview')
        expected_feilds=['Report (wf_retail_lite)', 'Sum', 'Cost of Goods', 'By', 'Cost of Goods', 'RANK', 'Product,Category', 'RANK', 'Across']
        metaobj.verify_query_panel_all_field(expected_feilds,'Step 10.2 : Verify Query pane')
         
        """
            Step 11 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 1,45,string_value='RANK')
        
        """
            Step 12 : Verify output > close window
        """
        #iarun.create_table_data_set('table[summary]',Test_Case_ID+'_DataSet_03.xlsx')
        iarun.verify_table_data_set('table[summary]',Test_Case_ID+'_DataSet_03.xlsx','Step 12.1 : Verify output')
        utillobj.switch_to_default_content(3)
        resultobj.select_panel_caption_btn(0,'close',custom_css='#resultAreaWindowManager')
        time.sleep(2)
        
        """
            Step 13 : Right-click "Cost of Goods" under "By" container > Delete
        """
        metaobj.querytree_field_click('Cost of Goods',2,1,'Delete')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(7)", 1,20,string_value='Across')
        
        """
            Step 14 : Verify field and associated RANK is deleted
        """
        iaresult.verify_across_report_data_set('TableChart_1 ',2,3,7,3,Test_Case_ID+'_DataSet_01.xlsx','Step 14.1 : Verify Preview')
        expected_fields=['Report (wf_retail_lite)', 'Sum', 'Cost of Goods', 'By', 'Product,Category', 'RANK', 'Across']
        metaobj.verify_query_panel_all_field(expected_fields,'Step 14.2 : Verify field and associated RANK is deleted')
        
        """
            Step 15 : Click Undo button in the toolbar 
        """
        ribbonobj.select_top_toolbar_item('toolbar_undo')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(8)", 1,20,string_value='RANK')
        time.sleep(2)
        
        """
            Step 15.1 : Verify field and associated RANK is restored
        """
        iaresult.verify_across_report_data_set('TableChart_1 ',2,5, 7, 5,Test_Case_ID+'_DataSet_02.xlsx','Step 15.1 : Verify Preview')
        expected_feilds=['Report (wf_retail_lite)', 'Sum', 'Cost of Goods', 'By', 'Cost of Goods', 'RANK', 'Product,Category', 'RANK', 'Across']
        metaobj.verify_query_panel_all_field(expected_feilds,'Step 15.2 : Verify Query pane')
        
        """
            Step 16 : Right-click "Cost of Goods" under "Sum" container > Delete
        """
        metaobj.querytree_field_click('Cost of Goods',1,1,'Delete')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,30,string_value='By')
        time.sleep(3)
        
        """
            Step 17 : Verify both "Cost of Goods" fields in Sum and By are deleted
        """
        #iaresult.create_across_report_data_set('TableChart_1 ',2,2, 7, 2,Test_Case_ID+'_DataSet_04.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1 ',2,2, 7, 2,Test_Case_ID+'_DataSet_04.xlsx','Step 17.1 : Verify preview')
        expected_fileds=['Report (wf_retail_lite)', 'Sum', 'By', 'Product,Category', 'RANK', 'Across']
        metaobj.verify_query_panel_all_field(expected_fileds,'Step 17.2 : Verify both "Cost of Goods" fields in Sum and By are deleted')
        
        """
            Step 18 : Logout and do not save changes: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__=='__main__' :
    unittest.main()