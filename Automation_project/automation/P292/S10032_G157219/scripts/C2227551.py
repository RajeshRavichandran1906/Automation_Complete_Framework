'''
Created on 08-NOV-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227551
TestCase Name = Verify create, save and restore HOLD file using Document mode
'''
import unittest
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2227551_TestClass(BaseTestCase):

    def test_C2227551(self):
        
        Test_Case_ID = "C2227551"
        driver = self.driver
        driver.implicitly_wait(60)
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        
        
        """ 1. Launch the IA API with WF_RETAIL_LITE, Document mode:    """
        utillobj.infoassist_api_login('document','new_retail/wf_retail_lite','P137/S7385', 'mrid', 'mrpass')
        elem1=(By.CSS_SELECTOR, "#theCanvas")
        resultobj._validate_page(elem1)
        
        """ 2. Double click "Cost of Goods", "Gross Profit". from Sales   """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
                
        """ 3. Double click "Sale,Year/Quarter". from Sales_Related dimension """
        time.sleep(5)
        metaobj.datatree_field_click("Sale,Year/Quarter", 2, 1)
        
        """ 4. Double click "Product,Category", "Product,Subcategory". from Product Dimension """
        time.sleep(5)
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        
        """ 5. Select Home Tab > "File" """
        ribbonobj.select_ribbon_item('Home', 'File')
        
        """ 6. Title "C2227551", Format "SQL Script (*.sql)" > click "Save"   """
        time.sleep(5)
        utillobj.ibfs_save_as("C2227551", "SQL Script (*.sql)")
        
        """ 7. Verify Data and Query panes """
        metaobj.verify_data_pane_field('Dimensions', 'Sale,Year/Quarter', 1, 'Step:7.a.1')
        metaobj.verify_data_pane_field('Dimensions', 'Product,Category', 2, 'Step:7.a.2')
        metaobj.verify_data_pane_field('Dimensions', 'Product,Subcategory', 3, 'Step:7.a.3')
        metaobj.verify_data_pane_field('Measures/Properties', 'Cost of Goods', 1, 'Step:7.b.1')
        metaobj.verify_data_pane_field('Measures/Properties', 'Gross Profit', 2, 'Step:7.b.1')
        time.sleep(5)
        metaobj.verify_query_pane_field('Files', 'C2227551 (wf_retail_lite)', 1, 'Step:7.c')
        
        """ 8. Double-click fields "Sale,Year/Quarter", "Product,Category" and "Gross Profit"    """
        time.sleep(5)
        metaobj.datatree_field_click('Sale,Year/Quarter', 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click('Product,Category', 2, 1)
        time.sleep(8)
        metaobj.datatree_field_click('Gross Profit', 2, 1)
        time.sleep(12)
        coln_list = ['SaleYear/Quarter', 'ProductCategory', 'Gross Profit']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_2", coln_list, "Step 8.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set("TableChart_2", 21, 3, Test_Case_ID+"_Ds02.xlsx", "Step 8.2: verify preview data", no_of_cells=6)
        
        
        """ 9. Select Insert Tab > click "Page"  """
        ribbonobj.select_ribbon_item('Insert', 'Page')
        elem1=(By.CSS_SELECTOR, "#theCanvas")
        resultobj._validate_page(elem1)
        
        """ 10. Double-click "Product,Subcategory" and "Cost of Goods"   """
        time.sleep(5)
        metaobj.datatree_field_click('Product,Subcategory', 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click('Cost of Goods', 2, 1)
        
        """ 11. Verify Canvas   """
        time.sleep(3)
        coln_list = ['ProductSubcategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_3", coln_list, "Step 11.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set("TableChart_3", 5, 2, "C2227551_Ds01.xlsx", "Step 11.2: verify preview data", no_of_cells=4)
        time.sleep(2)
        driver.switch_to.default_content()
        
        """ 12. Click "Save" > Save As "C2227551" > click Save  """
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(2)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """ 13. Logout: 'http://machine:port/ibi_apps/service/wf_security_logout.jsp'  """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """ 14. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2227551.fex&tool=document    """
        uname = (By.CSS_SELECTOR,'input[id=SignonUserName]')
        resultobj._validate_page(uname)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(3)
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S7385')
        
        """ 15. Verify Canvas   """
        elem1=(By.CSS_SELECTOR, "#theCanvas")
        resultobj._validate_page(elem1)
        time.sleep(15)
        coln_list = ['SaleYear/Quarter', 'ProductCategory', 'Gross Profit']
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_2", coln_list, "Step 15.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set("TableChart_2", 21, 3, Test_Case_ID+"_Ds02.xlsx", "Step 15.2: verify preview data", no_of_cells=6)
        
        
        """ 16. Click Page menu in the upper right > select "Page 2"      """
        ia_resultobj.select_or_verify_document_page_menu('Page 2')
        
        """ 17. Verify Canvas   """
        elem1=(By.CSS_SELECTOR, "#theCanvas")
        resultobj._validate_page(elem1)
        time.sleep(15)
        coln_list = ['ProductSubcategory', 'Cost of Goods']
        resultobj.verify_report_titles_on_preview(2, 4, "TableChart_3", coln_list, "Step 17.1: Verify Canvas column titles")
        ia_resultobj.verify_report_data_set("TableChart_3", 5, 2, Test_Case_ID+"_Ds01.xlsx", "Step 17.2: verify preview data", no_of_cells=4)

        """ 18. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()