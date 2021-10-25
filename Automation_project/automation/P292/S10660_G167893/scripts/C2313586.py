'''
Created on December 15, 2017

@author: PM14587
Testcase Name : Verify hold JSON with Chart conversion
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2313586
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_ribbon
from common.lib import utillity

class C2313586_TestClass(BaseTestCase):

    def test_C2313586(self):
        
        """   
                TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2313586'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iaribbon=ia_ribbon.IA_Ribbon(self.driver)
        
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
            Step 08 : Select "Create Chart"
        """
        iaribbon.select_hold_format_type('Create Chart')
        resultobj.wait_for_property("#TableChart_2 text[class='legend-labels!s0!']", 1,40,string_value='Series0')
        time.sleep(3)
        
        """
            Step 09 : Verify Data Pane and Query Pane Veriy "File" button is disabled in Chart mode
        """
        expected_data_fields=['Dimensions', 'Product,Category', 'Product,Subcategory', 'Model', 'Measures/Properties', 'Quantity,Sold']
        expected_query_fields=['Files', 'foccache/File1 (wf_retail_lite)', 'Chart (File1)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Horizontal Axis', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        metaobj.verify_all_data_panel_fields(expected_data_fields,'Step 09.1 : Verify Data Pane')
        metaobj.verify_query_panel_all_field(expected_query_fields,'Step 09.2 : Verify Query Pane')
        disabled_status=self.driver.find_element_by_id("HomeDestFile").get_attribute('disabled').lower()
        utillobj.asequal('true',disabled_status,'Step 09.3 : Verify "File" button is disabled in Chart mode')
        
        """
            Step 10 : Add fields "Product,Category" and "Quantity,Sold"
        """
        metaobj.datatree_field_click('Product,Category',2,1)
        resultobj.wait_for_property("#TableChart_2 text[class='xaxisOrdinal-title']", 1,20,string_value='Product Category')
        metaobj.datatree_field_click('Quantity,Sold',2,1)
        resultobj.wait_for_property("#TableChart_2 text[class='yaxis-title']", 1,20,string_value='Quantity Sold')
        time.sleep(3)
        
        """
            Step 10.1 : Verify chart output in preview
        """
        expected_xlabel_list=['Accessories','Camcorder','Computers','Media Player','Stereo Systems','Televisions','Video Production']
        expected_ylabel_list=['0','0.3M','0.6M','0.9M','1.2M']
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xlabel_list, expected_ylabel_list,'Step 10.1 : ')
        resultobj.verify_xaxis_title('TableChart_2','Product Category','Step 10.2 : Verify X-Axis title')
        resultobj.verify_yaxis_title('TableChart_2','Quantity Sold','Step 10.3 : Verify Y-Axis title')
        resultobj.verify_number_of_riser('TableChart_2',1,7,'Step 10.4 : Verify number of chart risers')
        screenshot_elelemnt=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_elelemnt,Test_Case_ID+'_Actual_Step_10','actual')
        
        """
            Step 11 : Click "Save" in the toolbar > Save As "C2313586" > Click Save
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
        resultobj.wait_for_property("#TableChart_2 text[class='xaxisOrdinal-title']", 1,40,string_value='Product Category')
        time.sleep(3)
        
        """
            Step 14 : Verify Data Pane, Query Pane and Live Preview Verify "File" button remains disabled
        """
        expected_query_fields1=['Files', 'foccache/File1 (wf_retail_lite)', 'Chart (File1)', 'Matrix', 'Rows', 'Columns', 'Axis', 'Vertical Axis', 'Quantity,Sold', 'Horizontal Axis', 'Product,Category', 'Marker', 'Color', 'Size', 'Tooltip', 'Multi-graph', 'Animate']
        expected_data_fields1=['Dimensions', 'Product,Category', 'Product,Subcategory', 'Model', 'Measures/Properties', 'Quantity,Sold']
        metaobj.verify_query_panel_all_field(expected_query_fields1,'Step 14.1 : Verify Query Pane')
        metaobj.verify_all_data_panel_fields(expected_data_fields1,'Step 14.2 : Verify Data Pane')
        disabled_status=self.driver.find_element_by_id("HomeDestFile").get_attribute('disabled').lower()
        utillobj.asequal('true',disabled_status,'Step 14.3 : Verify "File" button remains disabled')
        resultobj.verify_riser_chart_XY_labels('TableChart_2', expected_xlabel_list, expected_ylabel_list,'Step 14.4 : ')
        resultobj.verify_xaxis_title('TableChart_2','Product Category','Step 14.5 : Verify X-Axis title')
        resultobj.verify_yaxis_title('TableChart_2','Quantity Sold','Step 14.6 : Verify Y-Axis title')
        resultobj.verify_number_of_riser('TableChart_2',1,7,'Step 14.7 : Verify number of chart risers')
        screenshot_elelemnt=self.driver.find_element_by_id('resultArea')
        utillobj.take_screenshot(screenshot_elelemnt,Test_Case_ID+'_Actual_Step_14','actual')
        
        """
            Step 15 : Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()

if __name__=='__main__' :
    unittest.main()