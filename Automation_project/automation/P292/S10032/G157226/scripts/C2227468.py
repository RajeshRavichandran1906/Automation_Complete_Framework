'''
Created on 17-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227468
TestCase Name = Verify cascading Slicers with Hierarchical data
'''
import unittest, time
from common.lib import utillity
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_ribbon, ia_resultarea, ia_run
  
class C2227468_TestClass(BaseTestCase):

    def test_C2227468(self):
        
        """
            Testcase Variable
        """
        Test_Case_ID = "C2227468"
        
        """
            Class & Objects
        """
        driver = self.driver
        iarun=ia_run.IA_Run(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
 
        """    1. Launch the IA API with CAR, Report mode::    """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P137/S7385', 'mrid', 'mrpass')
        chart_type_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(chart_type_css, 1, 30)
        
        """    2. Double click "Product,Category","Product,Subcategory", "Model"   """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_number_of_element("[id*='ActivePreviewItem']", 2, 20)
        
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        utillobj.synchronize_with_number_of_element("[id*='ActivePreviewItem']", 4, 20)
        
        metaobj.datatree_field_click("Model", 2, 1)
        utillobj.synchronize_with_number_of_element("[id*='ActivePreviewItem']", 30, 20)
        
        """    3. Select "Slicers" tab.    """
        ribbonobj.switch_ia_tab('Slicers')
        
        """    4. Drag the "Product" Dimension to "Group 1".    """
        metaobj.expand_field_tree('Product')
        time.sleep(2)
#         utillobj.drag_drop_using_Sikuli('product_group', 'slicer_group1')
        metaobj.drag_drop_data_tree_group_to_slicers('Product',2,1)
        utillobj.synchronize_with_visble_text("#SlicersCluster_1 [class^='bi-label cluster-box-title']", 'Product', 30)
        
        """    5. Verify the following slicers are displayed on the ribbon (under "Product" group)    """
        group1=['Product', 'Product,Category', 'Product,Subcategory', 'Model']
#         group1=['Group 1', 'Product,Category', '  Product,Subcategory', '  Model']
        ia_ribbonobj.verify_slicer_group(1, group1, "Step 05.01: Verify product Group has been added to Group1")
        
        """    6. Click on "Product,Category" dropdown..    """
        ia_ribbonobj.select_group_slicer_dropdown(1, 'Product,Category')      
        
        """    7. Verify the following options are available.    """
        expected_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 07.01: Verify the Product,Category options available")
        
        """    8. Select "Television" > "OK".    """
        ia_ribbonobj.select_slicer_values_from_single_list(['Televisions'])
        ia_ribbonobj.close_slicer_dialog('ok')
        
        """    9. Click on "Product,Subcategory" drop down.    """
        ia_ribbonobj.select_group_slicer_dropdown(1, 'Product,Subcategory')
        
        """    10. Verify the following options are available.    """
        expected_list=['CRT TV', 'Flat Panel TV', 'Portable TV']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 10.01: Verify the Product,Subcategory options available")
        
        """    11. Select "Flat Panel TV" > "OK".    """
        ia_ribbonobj.select_slicer_values_from_single_list(['Flat Panel TV'])
        ia_ribbonobj.close_slicer_dialog('ok')
        
        """    12. Click on "Model" dropdown.    """
        ia_ribbonobj.select_group_slicer_dropdown(1, 'Model')
        
        """    13. Verify the following options are available.    """
        expected_list=['LG 19LE5300 19', 'LG 32LE5300 32', 'Panasonic 58TV25BNDL', 'Panasonic TCP46G25', 'Sony KDL32EX400', 'Sony KDL46HX800', 'Sony KDL60EX500']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 13.01: Verify the Model options available")
        
        """    14. Click Cancel in the dialog for "Model" slicer    """
        ia_ribbonobj.close_slicer_dialog('cancel')
        
        """    15. Click "Update Preview" in the Slicers Tab    """
        ribbonobj.select_ribbon_item('Slicers', 'Update_preview')
        time.sleep(5)
        
        """    16. Verify Preview    """
        coln_list = ["ProductCategory", "ProductSubcategory", "Model"]
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 15.01: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 3, 7, "C2227468_Ds01.xlsx", no_of_cells=6)
        ia_resultobj.verify_report_data_set("TableChart_1", 3, 7, "C2227468_Ds01.xlsx", "Step 15.02: verify data set", no_of_cells=6)
        
        """    17. Click Run > Verify output    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227468_Ds02.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227468_Ds02.xlsx", "Step 17.01: verify data set")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    18. Click on "Model" dropdown in the Slicer Tab Ribbon    """
        ia_ribbonobj.select_group_slicer_dropdown(1, 'Model')
        
        """    19. Multi-select the "Sony..." models > click OK    """
        ia_ribbonobj.select_slicer_values_from_single_list(['Sony KDL32EX400', 'Sony KDL46HX800', 'Sony KDL60EX500'])
        ia_ribbonobj.close_slicer_dialog('ok')
        
        """    20. Click "Update Preview" in the Slicers Tab    """
        time.sleep(5)
        ribbonobj.select_ribbon_item('Slicers', 'Update_preview')
        
        """    21. Verify Preview and Slicers Ribbon    """
        utillobj.synchronize_with_number_of_element("[id*='ActivePreviewItem']", 6, 20)
        group1=['Product', 'Product,Category1.1', 'Televisions', 'Product,Subcategory1.2', 'Flat Panel TV', 'Model1.3', 'Multiple']
        ia_ribbonobj.verify_slicer_group(1, group1, "Step 21.01: Verify updated product slicers in Group1")
        coln_list = ["ProductCategory", "ProductSubcategory", "Model"]
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 21.02: Verify column titles")
        #ia_resultobj.create_report_data_set("TableChart_1", 3, 3, "C2227468_Ds03.xlsx", no_of_cells=6)
        ia_resultobj.verify_report_data_set("TableChart_1", 3, 3, "C2227468_Ds03.xlsx", "Step 21.03: verify data set", no_of_cells=6)
        
        """    22. Click Run > Verify output    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(8)
        WebDriverWait(self.driver, 40).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[id^=ReportIframe-]')))
        time.sleep(3)
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227468_Ds04.xlsx")
        iarun.verify_table_data_set("table[summary= 'Summary']", "C2227468_Ds04.xlsx", "Step 22.01: verify data set")
        driver.switch_to.default_content()
        time.sleep(2)
        
        """    23. Click "IA" menu > Click "Save As" > "C2227468" > Click "Save" in the save dialog    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    24. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        
        """    25. Reopen fex using IA API: - http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS7385%2FC2163511.fex&tool=document    """
        uname = 'input[id=SignonUserName]'
        utillobj.synchronize_with_number_of_element(uname, 1, 20)
        utillobj.login_wf('mrid', 'mrpass')
        time.sleep(5)
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S7385')
        chart_type_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(chart_type_css, 1, 20)
        
        """    26. Select Slicer Tab > Verify Preview and Ribbon    """
        ribbonobj.switch_ia_tab('Slicers')
        time.sleep(3)
        #group1=['Group 1', 'Product,Category1.1', 'Televisions', ' Product,Subcategory1.2', 'Flat Panel TV', ' Model1.3', 'Multiple']
        group1=['Product', 'Product,Category1.1', 'Televisions', 'Product,Subcategory1.2', 'Flat Panel TV', 'Model1.3', 'Multiple']
        ia_ribbonobj.verify_slicer_group(1, group1, "Step 26.01: Verify updated product slicers in Group1")
        coln_list = ["ProductCategory", "ProductSubcategory", "Model"]
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 26.02: Verify column titles")
        ia_resultobj.verify_report_data_set("TableChart_1", 3, 3, "C2227468_Ds03.xlsx", "Step 26.03: verify data set", no_of_cells=6)
        
        """    27. Logout:- http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
if __name__ == '__main__':
    unittest.main()