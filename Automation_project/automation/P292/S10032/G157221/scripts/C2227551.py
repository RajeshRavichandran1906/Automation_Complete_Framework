'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227551
TestCase Name = Verify create, save and restore HOLD file using Document mode
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, metadata
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase

class C2227551_TestClass(BaseTestCase):

    def test_C2227551(self):
        
        Test_Case_ID = "C2227551"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        metadataobj = metadata.MetaData(self.driver)
        
        
        """ 1. Launch the IA API with WF_RETAIL_LITE, Document mode:    """
        utillobj.infoassist_api_login('document','baseapp/wf_retail_lite','P137/S7385', 'mrid', 'mrpass')
        utillobj.synchronize_until_element_is_visible("#theCanvas", metadataobj.chart_long_timesleep)
        
        """ 2. Double click "Cost of Goods", "Gross Profit". from Sales   """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        utillobj.synchronize_with_visble_text("#theCanvas", 'Cost of Goods', metadataobj.chart_long_timesleep)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        utillobj.synchronize_with_visble_text("#theCanvas", 'Gross Profit', metadataobj.chart_long_timesleep)
                
        """ 3. Double click "Sale,Year/Quarter". from Sales_Related dimension """
        metadataobj.collapse_data_field_section('Sales->Measure Groups')
        time.sleep(3)
        metadataobj.collapse_data_field_section('Filters and Variables')
        time.sleep(3)
        metaobj.datatree_field_click("Sale,Year/Quarter", 2, 1)
        utillobj.synchronize_with_visble_text("#theCanvas", 'Quarter', metadataobj.chart_long_timesleep)
        
        """ 4. Double click "Product,Category", "Product,Subcategory". from Product Dimension """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_visble_text("#theCanvas", 'Product', metadataobj.chart_long_timesleep)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        utillobj.synchronize_with_visble_text("#theCanvas", 'Subcategory', metadataobj.chart_long_timesleep)
        
        """ 5. Select Home Tab > "File" """
        ribbonobj.select_ribbon_item('Home', 'File')
        
        """ 6. Title "C2227551", Format "SQL Script (*.sql)" > click "Save"   """
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metadataobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as("C2227551", "SQL Script (*.sql)")
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_cbFileName input", metadataobj.home_page_medium_timesleep)
        
        """ 7. Verify Data and Query panes """
        metaobj.verify_data_pane_field('Dimensions', 'Sale,Year/Quarter', 1, 'Step 07.00 ')
        metaobj.verify_data_pane_field('Dimensions', 'Product,Category', 2, 'Step 07.01 ')
        metaobj.verify_data_pane_field('Dimensions', 'Product,Subcategory', 3, 'Step 07.02 ')
        metaobj.verify_data_pane_field('Measures/Properties', 'Cost of Goods', 1, 'Step 07.03 ')
        metaobj.verify_data_pane_field('Measures/Properties', 'Gross Profit', 2, 'Step 07.04 ')
        utillobj.synchronize_with_visble_text("#queryTreeColumn table", 'C2227551', metadataobj.home_page_medium_timesleep)
        metaobj.verify_query_pane_field('Files', 'C2227551 (wf_retail_lite)', 1, 'Step 07.05 ')
        
        """ 8. Double-click fields "Sale,Year/Quarter", "Product,Category" and "Gross Profit"    """
        metaobj.datatree_field_click('Dimensions->Sale,Year/Quarter', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2", 'Quarter', metadataobj.chart_long_timesleep)
        metaobj.datatree_field_click('Dimensions->Product,Category', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2", 'Category', metadataobj.chart_long_timesleep)
        metaobj.datatree_field_click('Measures/Properties->Gross Profit', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_2", 'Gross Profit', metadataobj.chart_long_timesleep)
        coln_list = ['SaleYear/Quarter', 'ProductCategory', 'Gross Profit']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_2", coln_list, "Step 08.00 : Verify Canvas column titles")
        ia_resultobj.verify_report_data_set("TableChart_2", 21, 3, Test_Case_ID+"_Ds02.xlsx", "Step 08.01: verify preview data", no_of_cells=6)
        
        """ 9. Select Insert Tab > click "Page"  """
        ribbonobj.select_ribbon_item('Insert', 'Page')
        utillobj.synchronize_with_visble_text("#theCanvas", 'Gross Profit', metadataobj.home_page_medium_timesleep,  condition_type='asnotin')
        
        """ 10. Double-click "Product,Subcategory" and "Cost of Goods"   """
        metaobj.datatree_field_click('Dimensions->Product,Subcategory', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_3", 'Subcategory', metadataobj.chart_long_timesleep)
        metaobj.datatree_field_click('Measures/Properties->Cost of Goods', 2, 1)
        utillobj.synchronize_with_visble_text("#TableChart_3", 'Goods', metadataobj.chart_long_timesleep)
        
        """ 11. Verify Canvas   """
        coln_list = ['ProductSubcategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_3", coln_list, "Step 11.01: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set("TableChart_3", 5, 2, "C2227551_Ds01.xlsx", "Step 11.02: verify preview data", no_of_cells=4)
        
        """ 12. Click "Save" > Save As "C2227551" > click Save  """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.synchronize_until_element_is_visible("#IbfsOpenFileDialog7_cbFileName input", metadataobj.home_page_medium_timesleep)
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.synchronize_until_element_disappear("#IbfsOpenFileDialog7_cbFileName input", metadataobj.home_page_medium_timesleep)
        
        """ 13. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'  """
        utillobj.infoassist_api_logout()
        
        """ 14. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227551.fex&tool=document    """
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S7385', mrid='mrid', mrpass='mrpass')
        
        """ 15. Verify Canvas   """
        utillobj.synchronize_with_visble_text("#TableChart_2", 'Gross Profit', metadataobj.chart_long_timesleep)
        coln_list = ['SaleYear/Quarter', 'ProductCategory', 'Gross Profit']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_2", coln_list, "Step 15.00: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set("TableChart_2", 21, 3, Test_Case_ID+"_Ds02.xlsx", "Step 15.01 verify preview data", no_of_cells=6)
        
        """ 16. Click Page menu in the upper right > select "Page 2"      """
        ia_resultobj.select_or_verify_document_page_menu('Page 2')
        
        """ 17. Verify Canvas   """
        utillobj.synchronize_with_visble_text("#TableChart_3", 'Cost of Goods', metadataobj.chart_long_timesleep)
        coln_list = ['ProductSubcategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_3", coln_list, "Step 17.00: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set("TableChart_3", 5, 2, Test_Case_ID+"_Ds01.xlsx", "Step 17.01: verify preview data", no_of_cells=4)

        """ 18. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()