'''
Created on December 15, 2017

@author: PM14587
Testcase Name : Veify hold JSON format in Document mode
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2321231
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_ribbon,ia_resultarea
from common.lib import utillity

class C2321231_TestClass(BaseTestCase):
      
    def test_C2321231(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2321231'
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
            Step 05 : Select "foccache" folder on the left pane
            Step 06 : Click "Save" in the hold file dialog
        """
        iaribbon.create_hold_file('File1','JSON (*.json)',save_folder='foccache')
        resultobj.wait_for_property("#createFromHoldButton >div[id^='BiLabel']", 1,40,string_value='Create Report')
         
        """
            Step 07 : Verify "Create Report" menu is displayed
        """
        utillobj.verify_element_text("#createFromHoldButton >div[id^='BiLabel']",'Create Report','Step 07.1 : Verify "Create Report" menu is displayed')
         
        """
            Step 08 : Select "Create Document"
        """
        iaribbon.select_hold_format_type('Create Document')
        resultobj.wait_for_property("#iaMetaDataBrowser div[id^='QbMetaDataTree-'] table[class^='bi-tree-view-table']>tbody>tr:nth-child(1)", 1,40,string_value='Dimensions')
        time.sleep(5)
        
        """
            Step 09 : Verify Data Pane and Query Pane
        """
        expected_data_fields=['Dimensions', 'Product,Category', 'Product,Subcategory', 'Model', 'Measures/Properties', 'Quantity,Sold']
        expected_query_fields=['Files', 'foccache/File1 (wf_retail_lite)']
        metaobj.verify_all_data_panel_fields(expected_data_fields,'Step 09.1 : Verify Data Pane')
        metaobj.verify_query_panel_all_field(expected_query_fields,'Step 09.2 : Verify Query Pane')
        
        """
            Step 10 : Add fields "Product,Category" and "Quantity,Sold"
        """
        metaobj.datatree_field_click('Product,Category',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(6)", 1,20,string_value='Product,Category')
        metaobj.datatree_field_click('Quantity,Sold',2,1)
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(5)", 1,20,string_value='Quantity,Sold')
        time.sleep(3)
        expected_query_fields=['Files', 'foccache/File1 (wf_retail_lite)', 'Report1 (File1)', 'Sum', 'Quantity,Sold', 'By', 'Product,Category', 'Across', 'Coordinated']
        metaobj.verify_query_panel_all_field(expected_query_fields,'Step 10.1 : Verify Query Pane')
        
        """
            Step 10.1 : Verify the canvas
        """
        #iaresult.create_across_report_data_set('TableChart_2 ',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx')
        iaresult.verify_across_report_data_set('TableChart_2 ',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx','Step 10.1 : Verify the canvas')
        
        """
            Step 11 : lick "Save" in the toolbar > Save As "C2321231" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 12 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 13 : Reopen the saved fex: http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC2313586.fex&tool=chart
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10660_infoassist_2',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1,40,string_value='Document')
        time.sleep(3)
        
        """
            Step 14 : Verify Data Pane, Query Pane and Live Preview
        """
        expected_query_fields=['Files', 'foccache/File1 (wf_retail_lite)']
        expected_data_fields=['Dimensions', 'Product,Category', 'Product,Subcategory', 'Model', 'Measures/Properties', 'Quantity,Sold']
        metaobj.verify_query_panel_all_field(expected_query_fields,'Step 14.1 : Verify Query Pane')
        metaobj.verify_all_data_panel_fields(expected_data_fields,'Step 14.2 : Verify Data Pane')
        iaresult.verify_across_report_data_set('TableChart_2 ',2,2,7,2,Test_Case_ID+'_DataSet_01.xlsx','Step 14.3 : Verify tLive Preview')
        screenshot_elelemnt=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_elelemnt,Test_Case_ID+'_Actual_Step_14','actual')
        
        """
            Step 15 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__=='__main__' :
    unittest.main()