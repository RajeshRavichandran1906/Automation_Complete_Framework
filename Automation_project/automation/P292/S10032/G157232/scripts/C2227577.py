'''
Created on Dec 13, 2017

@author: PM14587
Testcase Name : Verify Preview and Run Time Record Limit
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2227577
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_run,ia_resultarea,ia_ribbon
from common.lib import utillity

class C2227577_TestClass(BaseTestCase):

    def test_C2227577(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2227577'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
        
        """
            Step 01 : Launch IA Report mode: http://machine:port/ibi_apps/ia?tool=Report&master=ibisamp/MOVIES&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','ibisamp/movies','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
          
        """
            Step 02 : Double click "MOVIECODE", "TITLE", "WHOLESALEPR".
        """
        metaobj.datatree_field_click('MOVIECODE',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='MOVIECODE')
              
        metaobj.datatree_field_click('TITLE',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='TITLE')
              
        metaobj.datatree_field_click('WHOLESALEPR',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='WHOLESALEPR')
        time.sleep(2)
           
        """
            Step 03 : Verify the following report is displayed.
        """
        #iaresult.create_across_report_data_set('TableChart_1',1, 3, 61, 3, Test_Case_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1',1, 3, 61, 3, Test_Case_ID+'_DataSet_01.xlsx','Step 03.1 : Verify preview report')
         
        """
            Step 04 : Select "Slicers" Tab.
            Step 05 : In Preview dropdown select "10".
        """
         
        ribbonobj.select_ribbon_item('Slicers','preview',opt='10',custom_css="div[class*='list-item']")
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 33, 20)
         
        """
            Step 06 : Verify that 10 records are shown in Live preview mode.
        """
        #iaresult.create_across_report_data_set('TableChart_1',1, 3, 10, 3, Test_Case_ID+'_DataSet_02.xlsx')
        iaresult.verify_across_report_data_set('TableChart_1',1, 3, 10, 3, Test_Case_ID+'_DataSet_02.xlsx','Step 06.1 : Verify that 10 records are shown in Live preview mode.')
         
        """
            Step 07 : In "Run Time" (Record Limit) dropdown, type "15" and press Enter key.
        """
        iaribbon.set_record_limits('RunTime','15')
        
        """
            Step 08 : Click "Run".
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 1,45,string_value='MOVIECODE')
        time.sleep(2)
        
        """
            Step 09 : Verify that 15 records are shown.
        """
        #iarun.create_table_data_set('table[summary]',Test_Case_ID+'_DataSet_03.xlsx')
        iarun.verify_table_data_set('table[summary]',Test_Case_ID+'_DataSet_03.xlsx','Step 09.1 : Verify that 15 records are shown.')
        
        """
            Step 10 : Click "IA" > "Save".
            Step 11 : Enter Title = "C2227577".
            Step 12 : Click "Save"
        """    
        utillobj.switch_to_default_content(2)
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 13 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 14 : Run saved FEX: http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2227577.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+'.fex','S10032_infoassist_3','mrid', 'mrpass')
        resultobj.wait_for_property("table[summary]>tbody>tr:nth-child(1)>td:nth-child(1)", 1,45,string_value='MOVIECODE')
        time.sleep(2)
        iarun.verify_table_data_set('table[summary]',Test_Case_ID+'_DataSet_03.xlsx','Step 14.1 : Verify report data')
        
        """
            Step 15 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 16 : Reopen saved FEX: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2227531.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID,'report','S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#TableChart_1 div[class^='x']",33,45,string_value='MOVIECODE')
        time.sleep(2)
        
        """
            Step 17 : Verify Record limit is preserved
        """
        iaresult.verify_across_report_data_set('TableChart_1',1, 3, 10, 3, Test_Case_ID+'_DataSet_02.xlsx','Step 06.1 : Verify Record limit is preserved')
        ribbonobj.switch_ia_tab('Slicers')
        time.sleep(3)
        preview_limited_value=self.driver.find_element_by_css_selector("#SlicersPreviewComboBox input").get_attribute('value')
        runtime_limited_value=self.driver.find_element_by_css_selector("#SlicersRunTimeComboBox input").get_attribute('value')
        utillobj.asequal('15',runtime_limited_value,'Step 17.1 : Verify Run Time limited value')
        utillobj.asequal('10',preview_limited_value,'Step 17.1 : Verify Preview limited value')
        
        """
            Step 18 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
if __name__=='__main__' :
    unittest.main()