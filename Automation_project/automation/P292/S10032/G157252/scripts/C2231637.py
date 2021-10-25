'''
Created on Nov 22, 2017

@author: PM14587
Testcase Name : Verify InfoMini request with Chart mode 
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2231637
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon,ia_run,ia_resultarea, metadata
from common.lib import utillity
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class C2231637_TestClass(BaseTestCase):

    def test_C2231637(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID = 'C2231637'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        iaresult=ia_resultarea.IA_Resultarea(self.driver)
        metadataobj = metadata.MetaData(self.driver)
         
        """
            Step 01 : Launch IA Report mode with wf_retail_lite: http://machine:port/ibi_apps/ia?tool=report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
        
        """
            Step 02 : Right-click "Sum" in the Query pane > New Parameter
        """
        metaobj.querytree_field_click('Sum',1,1,'New Parameter')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(3)", 1,40,string_value='Parameter1')
          
        """
            Step 03 : Drag and drop "Revenue", "Cost of Goods", and "Gross Profit" under Parameter1
        """
        metadataobj.collapse_data_field_section("Filters and Variables")
        time.sleep(3)
        metaobj.drag_drop_data_tree_items_to_query_tree('Gross Profit',1,'Parameter1',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,40,string_value='Gross Profit')
        metaobj.drag_drop_data_tree_items_to_query_tree('Cost of Goods',1,'Parameter1',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,40,string_value='Cost of Goods')
        metaobj.drag_drop_data_tree_items_to_query_tree('Revenue',1,'Parameter1',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(4)", 1,40,string_value='Revenue')
        time.sleep(2)
          
        """
            Step 04 : Right-click "By" in the Query pane > New Parameter
        """
        metaobj.querytree_field_click('By',1,1,'New Parameter')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(8)", 1,40,string_value='Parameter2')
          
        """
            Step 05 : Drag and drop "Product,Category" and "Product,Subcategory" under Parameter2
        """
        metadataobj.collapse_data_field_section("Sales")
        time.sleep(3)
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Subcategory',1,'Parameter2',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(9)", 1,40,string_value='Product,Subcategory')
        metaobj.drag_drop_data_tree_items_to_query_tree('Product,Category',1,'Parameter2',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(9)", 1,40,string_value='Product,Category')
        time.sleep(2)
          
        """
            Step 06 : Drag "Store,Business,Region" into Across bucket in the Query pane
        """
        metaobj.drag_drop_data_tree_items_to_query_tree('Store,Business,Region',1,'Across',0,target_cord='middle')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(12)", 1,40,string_value='Store,Business,Region')
        time.sleep(2)
         
        """
            Step 07 : Click "Save" > save as "C2231637" > Click Save
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """
            Step 08 : Run
            Step 09 : Verify output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(3)
        utillobj.switch_to_frame(pause=2)
        resultobj.wait_for_property("#promptPanel label[class='autop-title']",1,20,string_value='Filter Values')
        
        actual_field1=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter1'] span").text.strip()
        actual_field2=self.driver.find_element_by_css_selector("div[class='autop-amper-ctrl-container'] div[class^='autop-amper'][title='Parameter2'] span").text.strip()
        
        expected_paramter1="Revenue"
        expected_paramter2="Product Category"
        
        utillobj.asequal(actual_field1,expected_paramter1,'Step 09.1 : Verify default amper value for Paramater1')
        utillobj.asequal(actual_field2,expected_paramter2,'Step 09.2 : Verify default amper value for Paramater2')
        
        
        """
            Step 10 : Click on the "Revenue" dropdown > Select "Cost of Goods"
        """
        iarun.select_amper_value('Parameter1',['Cost of Goods'],False,verify_small_value_list=['Revenue', 'Cost of Goods', 'Gross Profit'])
         
        """
            Step 11 : Click on the "Product,Category" dropdown > Select "Product,Subcategory"
        """
        iarun.select_amper_value('Parameter2',['Product Subcategory'],False,verify_small_value_list=['Product Category', 'Product Subcategory'])
         
        """
            Step 12 : Click the Submit button
            Step 13 : Verify output
        """
        iarun.select_amper_menu('Run')
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe[name="wfOutput"]')))
        resultobj.wait_for_property("table[summary= 'Summary']>tbody>tr:nth-child(1)>td",1,20,string_value='Store,Business,Region')
        iarun.verify_table_data_set("table[summary= 'Summary']",Test_Case_ID+'_DataSet_01.xlsx','Step 13.1 : Verify output report')
         
        """
            Step 14 : Logout
        """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
        """
            Step 15 : Reopen FEX:
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_4',mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#queryTreeColumn table[class='bi-tree-view-table']>tbody>tr:nth-child(2)", 1,60,string_value='Sum')
        time.sleep(3)
         
        """
            Step 16 : Verify Query pane and Preview
        """
        
        expected_fields=['Parameter1', 'Revenue', 'Cost of Goods', 'Gross Profit', 'By', 'Parameter2', 'Product,Category', 'Product,Subcategory', 'Across', 'Store,Business,Region']
        position=1
        for field in expected_fields :
            metaobj.verify_query_pane_field('Sum',field,position,'Step 16.'+str(position))
            position+=1
        iaresult.verify_across_report_data_set('TableChart_1',3,5,7,5,Test_Case_ID+'_DataSet_02.xlsx','Step 16.11 : Verify preview report')
        
    if __name__ == "__main__":
        unittest.main()