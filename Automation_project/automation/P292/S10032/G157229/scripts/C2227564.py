'''
Created on 05-OCT-2016

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7385
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227564
TestCase Name = Verify Auto Drill Report with Auto Link and Multi Drill, using wf_retail_lite
'''

import unittest
from common.pages import visualization_metadata, visualization_ribbon, ia_run, ia_ribbon
from common.lib import utillity  
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2227564_TestClass(BaseTestCase):

    def test_C2227564(self):
        
        Test_Case_ID = "C2227564"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        iarun=ia_run.IA_Run(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        visualiz_obj = visualization.Visualization(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_ribbonobj=ia_ribbon.IA_Ribbon(self.driver)

        """    1. Reopen fex C2068414.fex using IA API:    """
        utillobj.infoassist_api_edit("C2227563", "report", "S7385", mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        time.sleep(5)
        
         
        """    2. Select "Format" > "Enable Auto Linking".    """
        ribbonobj.select_ribbon_item("Format", "Enable_Auto_Linking")
        
        """    3. Click "IA" > Save As > Enter "Title:" = "C2227564", click "Save"    """
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(5)
        
        """    4. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
        
        """    5. Launch the IA API with WF_RETAIL_LITE, Report mode:    """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P137/S7385', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """    6. Double click "Product Category","Product_Subcategory","Cost of Goods"    """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 9, 190)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 32, 190)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 55, 190)
        
        """    7. Drag and drop "Product Category" into Filter panel    """
        metaobj.drag_drop_data_tree_items_to_filter("Product,Category", 1)
        time.sleep(4)
        
        """    8. Double click "<Value>", set "Type:" = "Parameter", click "OK" (2x).    """
        ia_ribbonobj.create_parameter_filter_condition('Simple', 'Simple')
        utillobj.synchronize_with_visble_text('#qbFilterBox', 'Equal', 30)
        
        """    9. Verify "Filter" is created    """
        metaobj.verify_filter_pane_field('Product,Category Equal to Simple Parameter (Name: PRODUCT_CATEGORY)', 1, "Step 09a")
        
        """    10. Select "Format" > "Auto Link Target".    """
        ribbonobj.select_ribbon_item("Format", "Auto_Link_Target")
        
        """    11. Click "IA" > "Save" > Enter "Title:" = "Report_Target01", click "Save".    """ 
        ribbonobj.select_top_toolbar_item('toolbar_save')
        utillobj.ibfs_save_as("Report_Target01")
        time.sleep(5)
        
        """    12. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(1)
        
        """    13. Reopen fex using IA API:    """
        utillobj.infoassist_api_edit(Test_Case_ID, "report", "S7385", mrid='mrid', mrpass='mrpass')
        elem1= "#TableChart_1"
        utillobj.synchronize_with_number_of_element(elem1, 1, 30)
        
        """    14. Click "Run"    """
        visualiz_obj.run_visualization_from_toptoolbar()
        utillobj.synchronize_until_element_is_visible("iframe[id^='Report']", 60, pause_time=5)
        utillobj.switch_to_frame()
        utillobj.synchronize_until_element_is_visible("iframe[src*='Drill']", 20, pause_time=5)
        utillobj.switch_to_frame(frame_css="iframe[src*='Drill']")
        utillobj.synchronize_with_visble_text("table[summary]", 'Televisions', 100)
        
        """    15. Click "Accessories"    """
        """    16. Verify Auto drill,Multidrill and Autolink menus are displayed    """
        expected_list=['Drill down to Product Subcategory', 'Drilldown to Chart', 'MSN', 'Yahoo', 'Auto Links']
        iarun.verify_autolink_tooltip_values("table[summary='Summary']", 2, 1, expected_list, "Step 16a: Verify menu for Multi-drill and Autolink targets")
        
        """    17. Select "Media Player" > Hover over Auto link > Select "Report_Target01"    """
        iarun.select_report_autolink_tooltip("table[summary= 'Summary']", 5,1, "Auto Links->Report_Target01")
        
        """    18. Verify "Report_Target01" is displayed in a new window    """
        count=1
        while True:
            if count==90:
                break
            total_window=len(self.driver.window_handles)
            if total_window>0:
                break
            else:
                count+=1
                continue
            time.sleep(1)
        driver.switch_to.default_content()
        utillobj.switch_to_window(1)
        table_css="table[summary= 'Summary']"
        utillobj.synchronize_with_number_of_element(table_css, 1, 190)
        
        #iarun.create_table_data_set("table[summary= 'Summary']", "C2227564_Ds01.xlsx")
        iarun.verify_table_data_set(table_css, "C2227564_Ds01.xlsx", "Step 18a: verify Output")
         
        """    19. Close the "Report_Source01 & Report_Target01" windows    """
        self.driver.close()
        time.sleep(1)
        utillobj.switch_to_window(0)
        time.sleep(1)
         
        """    20. Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        utillobj.infoassist_api_logout()
        time.sleep(3)
         
                
if __name__ == '__main__':
    unittest.main()