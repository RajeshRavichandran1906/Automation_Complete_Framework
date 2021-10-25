'''
Created on December 15, 2017

@author: PM14587
Testcase Name : Verify hold JSON format in Report mode
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2313584
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_resultarea,ia_ribbon
from common.lib import utillity

class C2313584_TestClass(BaseTestCase):

    def test_C2313584(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2313584'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        
        """
            Step 01 : http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('Report','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
         
        """
            Step 02 : Add fields "Product,Category", "Product,Subcategory", "Model" and "Quantity,Sold"
        """
        metaobj.datatree_field_click('Product,Category',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='Product,Category')
         
        metaobj.datatree_field_click('Product,Subcategory',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='Product,Subcategory')
         
        metaobj.datatree_field_click('Model',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(6)", 1,20,string_value='Model')
         
        metaobj.datatree_field_click('Quantity,Sold',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,20,string_value='Quantity,Sold')
         
        """
            Step 03 : Click "File" in the Home Tab ribbon
            Step 04 : Click the hold formats dropdown menu > Select JSON format
            Step 05 : Click "Save" in the hold file dialog
        """
        iaribbon.create_hold_file('File1','JSON (*.json)')
        resultobj.wait_for_property("#createFromHoldButton >div[id^='BiLabel']", 1,40,string_value='Create Report')
         
        """
            Step 06 : Verify "Create Report" menu is displayed
        """
        utillobj.verify_element_text("#createFromHoldButton >div[id^='BiLabel']",'Create Report','Step 06.1 : Verify "Create Report" menu is displayed')
         
        """
            Step 07 : Click "Save" in the toolbar
            Step 08 : Save As "C2313584" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
         
        """
            Step 09 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
         
        """
            Step 10 : Reopen the saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2313584.fex&tool=report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#createFromHoldButton >div[id^='BiLabel']", 1,40,string_value='Create Report')
        time.sleep(8)
        
        """
            Step 11 : Click on the "Create Report" menu arrow > Select "Create Report"
        """
        iaribbon.select_hold_format_type('Create Report')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='Sum')
        time.sleep(8)
        expected_data_fields=['Dimensions', 'Product,Category', 'Product,Subcategory', 'Model', 'Measures/Properties', 'Quantity,Sold']
        metaobj.verify_all_data_panel_fields(expected_data_fields,'Step 11.1 : Verify Data Pane')
        
        """
            Step 12 : Add fields "Product,Category" and "Quantity,Sold"
        """
        metaobj.datatree_field_click('Product,Category',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(6)", 1,20,string_value='Product,Category')
        metaobj.datatree_field_click('Quantity,Sold',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='Quantity,Sold')
        time.sleep(3)
        
        """
            Step 13 : Verify Data Pane, Query Pane and Live Preview
        """
        expected_query_fields=['Files', 'File1 (wf_retail_lite)', 'Report (File1)', 'Sum', 'Quantity,Sold', 'By', 'Product,Category', 'Across'] 
        #iaresult.create_across_report_data_set('TableChart_2 ',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_2 ',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx','Step 13.1 : Verify Live Preview')
        metaobj.verify_query_panel_all_field(expected_query_fields,'Step 13.2 : Verify Query Pane')
        
        """
            Step 14 : Click "Save" > Click OK
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 15 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 16 : Reopen the saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2313584.fex&tool=report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,20,string_value='Sum')
        time.sleep(3)
        
        """
            Step 17 : Verify Data Pane, Query Pane and Live Preview
        """
        metaobj.verify_query_panel_all_field(expected_query_fields,'Step 17.1 : Verify Query Pane')
        metaobj.verify_all_data_panel_fields(expected_data_fields,'Step 17.2 : Verify Data Pane')
        iaresult.verify_across_report_data_set('TableChart_2 ',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx','Step 17.3 : Verify Live Preview')
        
        """
            Step 18 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__=='__main__' :
    unittest.main()