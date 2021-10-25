'''
Created on 17-OCT-2016
@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227508
TestCase Name = Verify multiple Where-based Joins 
'''

from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run, metadata
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase
import unittest, time

class C2227508_TestClass(BaseTestCase):

    def test_C2227508(self):
        
        Test_Case_ID = "C2227508"
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        """    
            Step 01 : Launch the IA API with wf_retail_product, Report mode:
            http://machine:port/ibi_apps/ia?tool=report&master=baseapp/dimensions/wf_retail_product&item=IBFS%3A%2FWFC%2FRepository%2FS7385%2F
        """
        utillobj.infoassist_api_login('report','baseapp/dimensions/wf_retail_product','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeWindow table[class='bi-tree-view-table']>tbody>tr:nth-child(2)>td", 'Sum', expire_time=10)
         
        """    
            Step 02 : Select "Data" > "Join". 
            Step 03 : Click "Add New" > wf_retail_vendor.MAS.     
        """
        ia_ribbonobj.create_join("baseapp->dimensions","wf_retail_vendor")
         
        """    
            Step 04 : Link ID_VENDOR in wf_retail_product to ID_VENDOR in wf_retail_vendor.    
        """
        ia_ribbonobj.create_join_link(0, "ID_VENDOR", 1, "ID_VENDOR", source_scroll_down=5)
        ia_ribbonobj.verify_join_link_color(0, 'red', "Step 04a: verify Join link color 'red' for first join")
         
        """    
            Step 05 : Click "Filter" button in toolbar > verify default WHERE expression in dialog.
        """
        ia_ribbonobj.select_join_menu_buttons("filter")
        ia_ribbonobj.verify_join_filter_Condition("WF_RETAIL_PRODUCT.WF_RETAIL_PRODUCT.ID_VENDOR Equal to WF_RETAIL_VENDOR.WF_RETAIL_VENDOR.ID_VENDOR", "Step 07a: Verify filter condition")
         
        """    
            Step 06. Click "OK".     
        """
        ia_ribbonobj.close_filter_dialog(btn='ok')
        
        """    
            Step 07 : Click 'Add New' > select wf_retail_customer under dimensions subfolder    
        """
        ia_ribbonobj.create_join("baseapp->dimensions","wf_retail_customer", new_join=False)
         
        """
            Step 08 : Link ID_VENDOR from wf_retail_vendor to ID_CUSTOMER in wf_retail_customer
        """
        ia_ribbonobj.create_join_link(1, "ID_VENDOR", 2, "ID_CUSTOMER", source_scroll_down=2)
         
         
        utillobj.synchronize_with_number_of_element("#dlgJoin line[marker-start]", 2, expire_time=8)
        ia_ribbonobj.verify_join_link_color(0, 'blue', "Step 08a: verify Join link color 'blue' for first join")
        ia_ribbonobj.verify_join_link_color(1, 'red', "Step 08b: verify Join link color 'red' for Second join")
         
        """    
            Step 09 : Click "Filter'" in the toolbar > verify default WHERE expression in dialog   
        """
        ia_ribbonobj.select_join_menu_buttons("filter")
        ia_ribbonobj.verify_join_filter_Condition("WF_RETAIL_VENDOR.WF_RETAIL_VENDOR.ID_VENDOR Equal to WF_RETAIL_CUSTOMER.WF_RETAIL_CUSTOMER.ID_CUSTOMER", "Step 09a: Verify filter condition")
          
        """    
            Step 10 : Click OK > OK    
        """
        ia_ribbonobj.close_filter_dialog(btn='ok')
        ia_ribbonobj.select_join_menu_buttons("ok")
        utillobj.synchronize_with_visble_text("#iaMetaDataBrowser table[class='bi-tree-view-table']>tbody>tr:nth-child(12)>td", 'Vendor Name', expire_time=5)
        time.sleep(10)
         
        """    
            Step 11 : Verify Data pane   
        """
        metaobj.verify_data_pane_field('Dimensions',"Vendor Name",11,"Step 11a")
        metaobj.verify_data_pane_field('Dimensions',"Gender",15,"Step 11b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",8,"Step 11c")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Industry",15,"Step 11d")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Age",11,"Step 11e")
         
        """    
            Step 12 : Double-click fields "Product,Category", "Vendor Name", "ID Geography", "Customers" and "ID Industry"
        """
        metadataobj.collapse_data_field_section("Measures/Properties")
        time.sleep(1)
        metaobj.datatree_field_click("Dimensions->Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table[class='bi-tree-view-table']>tbody>tr:nth-child(4)>td", 'Product,Category', expire_time=4)
         
        metaobj.datatree_field_click("Dimensions->Vendor Name", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table[class='bi-tree-view-table']>tbody>tr:nth-child(5)>td", 'VendorName', expire_time=4)
        time.sleep(8)
         
        metadataobj.collapse_data_field_section('Dimensions')
        time.sleep(6)
        metaobj.datatree_field_click("Measures/Properties->ID Geography", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table[class='bi-tree-view-table']>tbody>tr:nth-child(3)>td", 'IDGeography', expire_time=4)
         
        metaobj.datatree_field_click("Measures/Properties->Customers", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table[class='bi-tree-view-table']>tbody>tr:nth-child(4)>td", 'Customers', expire_time=5)
         
        metaobj.datatree_field_click("Measures/Properties->ID Industry", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeWindow table[class='bi-tree-view-table']>tbody>tr:nth-child(5)>td", 'IDIndustry', expire_time=5)      
         
        """    
            Step 13 : verify the following report is displayed  
        """
        coln_list = ["ProductCategory", "Vendor Name", "ID Geography", "Customers", "ID Industry"]
        resultobj.verify_report_titles_on_preview(5, 10, "TableChart_1", coln_list, "Step 15a: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 30, 5, "C2227508_Ds01.xlsx", no_of_cells=10)
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 5, "C2227508_Ds01.xlsx", "Step 15b: verify preview data", no_of_cells=10)  
         
        """    
            Step 14 : Click Run > Verify output.    
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(2)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227508_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227508_Ds02.xlsx", "Step 14a: verify data set")
        utillobj.switch_to_default_content()
        #driver.switch_to.default_content()
        time.sleep(2)
        """    
            Step 15 : Close the output window  
            Step 16 : Click "IA" > "Save" > C2227508 > click Save.
        """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
         
        """    
            Step 17 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
       
        """    
            Step 18. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document 
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385', mrid='mrid', mrpass='mrpass')
        utillobj.synchronize_with_visble_text("#queryTreeWindow table[class='bi-tree-view-table']>tbody>tr:nth-child(2)>td", 'Sum', expire_time=10)
        
        """    
            Step 19 : Verify Data pane, Query pane, and Preview 
        """
        metaobj.verify_data_pane_field('Dimensions',"Vendor Name",11,"Step 19a")
        metaobj.verify_data_pane_field('Dimensions',"Gender",15,"Step 19b")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Vendor",8,"Step 19c")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Industry",15,"Step 19d")
        metaobj.verify_data_pane_field('Measures/Properties',"ID Age",11,"Step 19e") 
        metaobj.verify_query_pane_field('Sum',"ID Geography",1,"Step 19f")
        metaobj.verify_query_pane_field('Sum',"Customers",2,"Step 19g")
        metaobj.verify_query_pane_field('Sum',"ID Industry",3,"Step 19h")
        metaobj.verify_query_pane_field('By',"Product,Category",1,"Step 19i")
        metaobj.verify_query_pane_field('By',"Vendor Name",2,"Step 19j")
        coln_list = ["ProductCategory", "Vendor Name", "ID Geography", "Customers", "ID Industry"]
        resultobj.verify_report_titles_on_preview(5, 10, "TableChart_1", coln_list, "Step 19k: Verify column titles") 
        ia_resultobj.verify_report_data_set("TableChart_1", 30, 5, "C2227508_Ds01.xlsx", "Step 19l: verify preview data", no_of_cells=10)
        
        """    
            Step 20 : Click View Source button in the toolbar
            Step 21 : 21. Verify JOIN syntax
        """
        expected_syntax_list=['JOIN FILE baseapp/dimensions/wf_retail_product AT WF_RETAIL_PRODUCT.WF_RETAIL_PRODUCT.ID_VENDOR',  'TO UNIQUE FILE baseapp/dimensions/wf_retail_vendor AT WF_RETAIL_VENDOR.WF_RETAIL_VENDOR.ID_VENDOR TAG J001 AS J001', 'JOIN FILE baseapp/dimensions/wf_retail_product AT J001.WF_RETAIL_VENDOR.ID_VENDOR', 'TO UNIQUE FILE baseapp/dimensions/wf_retail_customer AT WF_RETAIL_CUSTOMER.WF_RETAIL_CUSTOMER.ID_CUSTOMER TAG J002 AS J002']
        ia_resultobj.verify_fexcode_syntax(expected_syntax_list, 'Step 21.1 : Verify J001 Join syntax in fex code')

        """    
            Step 23 : Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()
