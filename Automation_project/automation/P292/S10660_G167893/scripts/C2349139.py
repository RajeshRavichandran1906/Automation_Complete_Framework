'''
Created on Nov 30, 2017
@author: Praveen Ramkumar
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10006_infoassist_2
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2349139
TestCase Name = Verify Report with a Compute field

'''

import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea,define_compute,ia_run
from common.lib.basetestcase import BaseTestCase

class C2349139_TestClass(BaseTestCase):

    def test_C2349139(self):
        driver = self.driver #Driver reference object created
        driver.implicitly_wait(15) #Intializing common implicit wait for throughout the test
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2349139'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaresultobj = ia_resultarea.IA_Resultarea(self.driver)
        calculate_obj=define_compute.Define_Compute(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        
        """
        Step 01: Launch the IA API with WF_RETAIL_LITE, Report mode:
            http://machine:port/ibi_apps/ia?tool=report&master=baseapp/WF_RETAIL_LITE&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F
        """ 
         
        utillobj.infoassist_api_login('Report','baseapp/wf_retail_lite','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="div[align='justify']"
        resultobj.wait_for_property(parent_css, 1,expire_time=20)
      
        """
        Step 02: Double click "Revenue","Product,Category".
        """ 
         
        metaobj.datatree_field_click('Revenue', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(3) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=10,string_value='Revenue', with_regular_exprestion=True)
        metaobj.verify_query_pane_field('Sum','Revenue',1,"Step 02.1: Verify query pane")
         
        metaobj.datatree_field_click('Product,Category', 2, 0)
        parent_css="#queryTreeWindow table tr:nth-child(5) td"
        resultobj.wait_for_property(parent_css, 1,expire_time=15,string_value='Product,Category', with_regular_exprestion=True)
        metaobj.verify_query_pane_field('By','Product,Category',1,"Step 02.2: Verify query pane")
 
        """
        Step 03: Select "Data" > "Summary (Compute)".
        """
         
        ribbonobj.select_ribbon_item('Data','summary_compute')
        time.sleep(5)
         
        """
        Step 04:Enter "Field" = "NewRevenue".
        Step 05:Double click "Revenue".
         
        """
        calculate_obj.enter_define_compute_parameter("NewRevenue", "D12.2", "Revenue", 1)
        time.sleep(5)
         
        """
        Step 06:Enter "+ 9999" into the textbox.
        Step 07:Click "OK".
        """
         
        calculate_obj.select_calculation_btns("plus")
        calculate_obj.select_calculation_btns("nine")
        calculate_obj.select_calculation_btns("nine")
        calculate_obj.select_calculation_btns("nine")
        calculate_obj.select_calculation_btns("nine")
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
         
         
        """
        Step 08:Verify the following report is displayed.
         
 
        """
#          iaresultobj.create_across_report_data_set('TableChart_1', 2, 3, 7, 3,Test_Case_ID+'_DataSet_01.xlsx')
        iaresultobj.verify_across_report_data_set('TableChart_1',2,3,7,3,Test_Case_ID+'_DataSet_01.xlsx','Step 08: Verify report')
               
        """Step 09:Click "Run".
        """
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(5)
        parent_css="#resultArea [id^=ReportIframe-]"
        resultobj.wait_for_property(parent_css, 1)
        utillobj.switch_to_frame(pause=2)
        time.sleep(3)
        
        """        Step 10:Verify the following report is displayed."""
        
#         iarun.create_table_data_set("table[summary='Summary']",Test_Case_ID+'_Ds02.xlsx') 
        iarun.verify_table_data_set("table[summary='Summary']",Test_Case_ID+"_Ds02.xlsx", 'Step 10: Verify HTML format report After Run')
       
        """
        Step 11:Highlight "NewRevenue" > Right mouse click > "Edit Compute".
        Step 12:Enter "Field" = "NewRevenue_1".
        """
        
        utillobj.switch_to_default_content(pause=3)
        time.sleep(8)
        metaobj.querytree_field_click("NewRevenue",1,1,"Edit Compute")
        time.sleep(8)
        field_name = self.driver.find_element_by_id("fname")
        field_name.clear() 
        time.sleep(1)                                                    
        field_name.send_keys("NewRevenue_1")
        time.sleep(1) 
        calculate_obj.close_define_compute_dialog("ok")
        time.sleep(5)
        
        """
        Step 13:Click "OK".
        Step 14:Verify the following report is displayed.        
        """
        
#         iaresultobj.create_across_report_data_set('TableChart_1', 2, 3, 7, 3,Test_Case_ID+'_DataSet_03.xlsx')
        iaresultobj.verify_across_report_data_set('TableChart_1',2,3,7,3,Test_Case_ID+'_DataSet_03.xlsx','Step 13 : Verify report')
        
        
        """
        Step 15:Click "IA" > "Save" > "C2349139" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(8)
        
        """
        Step 16:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp        
        """
        
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """
        Step 17:Reopen fex using IA API:http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2349139.fex&tool=report      
        """
        
        utillobj.infoassist_api_edit(Test_Case_ID,'Report', 'P292/S10032_infoassist_3',mrid='mrid',mrpass='mrpass')
        time.sleep(8)
        
        """
        Step 18:Verify Report on "Live Preview".
        """
        
#         iaresultobj.create_across_report_data_set('TableChart_1', 2, 3, 7, 3,Test_Case_ID+'_DataSet_04.xlsx')
        iaresultobj.verify_across_report_data_set('TableChart_1',2,3,7,3,Test_Case_ID+'_DataSet_04.xlsx','Step 18: Verify report')
        
        """
        Step 19:Logout:http://machine:port/ibi_apps/service/wf_security_logout.jsp        
        """
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()  