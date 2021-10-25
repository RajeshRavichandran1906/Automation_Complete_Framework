'''
Created on Nov 14, 2017

@author: BM13368
Testcase_Name : Verify hiding visibility (NOPRINT) on Dimension and Measure
Testcase_ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2235386
'''
import unittest,time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea,ia_run
from common.lib.basetestcase import BaseTestCase
from selenium.webdriver.common.by import By

class C2235386_TestClass(BaseTestCase):

    def test_C2235386(self):
        
        Test_Case_ID = "C2235386"
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_resultarea_obj=ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon_obj=visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_run_obj=ia_run.IA_Run(self.driver)
        
        """
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','baseapp/wf_retail_lite','P292/S10032_infoassist_3', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        """
            Step 02 : Add "Cost of Goods" and "Gross Profit" to the Sum container
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(4)
        """
            Step 03 : Add "Product,Category" and "Product,Subcategory" to the By container    
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(4)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        time.sleep(4)
        """
            Step 04 : Drag "Sale,Year" (from Sales_Related) to the "Across" container 
        """
        metaobj.drag_drop_data_tree_items_to_query_tree("Sale,Year",1, 'Across', 0)
#         metaobj.datatree_field_click("Sale,Year",1,0,'Across')
        time.sleep(3)
#         ia_resultarea_obj.create_across_report_data_set('TableChart_1', 3, 8, 4, 8, "C2235386_Ds01.xlsx")
        ia_resultarea_obj.compare_across_report_data_set('TableChart_1', 3, 8, 4, 8, "C2235386_Ds01.xlsx")
        """
            Step 05 : Select "Sale,Year" in "Across" container > Click "Hide Field" button in the Field Tab
        """
        metaobj.querytree_field_click("Sale,Year",1,0)
        time.sleep(2)
        
#         vis_ribbon_obj.select_visualization_ribbon_item('Field', 'Display')
        vis_ribbon_obj.select_visualization_ribbon_item('Field', 'Hide_Field')
        time.sleep(8)
        
        """
            Step 06 : Verify field is hidden in the Preview 
        """
#         ia_resultarea_obj.create_across_report_data_set('TableChart_1', 3, 8, 4, 8, "C2235386_Ds02.xlsx")
        ia_resultarea_obj.compare_across_report_data_set('TableChart_1', 3, 8, 4, 8, "C2235386_Ds02.xlsx")
        """
            Step 07 : Select "Product,Category" in "By" container > Click "Hide Field" button in the Field Tab
        """
        metaobj.querytree_field_click("Product,Category",1,0)
        time.sleep(2)
#         vis_ribbon_obj.select_visualization_ribbon_item('Field', 'Display')
        vis_ribbon_obj.select_visualization_ribbon_item('Field', 'Hide_Field')
#         vis_ribbon_obj.select_ribbon_item('Field', 'Hide_Field')
        time.sleep(8)
        
        """
            Step 08 : Verify field is hidden in the Preview
        """
#         ia_resultarea_obj.create_across_report_data_set('TableChart_1', 2, 13, 4, 13, "C2235386_Ds03.xlsx")
        ia_resultarea_obj.compare_across_report_data_set('TableChart_1', 2, 13, 4, 13, "C2235386_Ds03.xlsx")
        
        """
            Step 09 : Select "Cost of Goods" in "Sum" container > Click "Hide Field" button in the Field Tab
        """
        metaobj.querytree_field_click("Cost of Goods",1,0)
        time.sleep(2)
#         vis_ribbon_obj.select_visualization_ribbon_item('Field', 'Display')
        vis_ribbon_obj.select_visualization_ribbon_item('Field', 'Hide_Field')
#         vis_ribbon_obj.select_ribbon_item('Field', 'Hide_Field')
        time.sleep(8)
        """
            Step 10 : Verify field is hidden in the Preview
        """
#         ia_resultarea_obj.create_across_report_data_set('TableChart_1', 2, 7, 4, 7, "C2235386_Ds04.xlsx")
        ia_resultarea_obj.compare_across_report_data_set('TableChart_1', 2, 7, 4, 7, "C2235386_Ds04.xlsx")
        
        """
            Step 11 : Click Run
        """
        vis_ribbon_obj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        time.sleep(5)
        """
            Step 12 : Verify outputVerify output
        """
#         ia_run_obj.create_table_data_set("html table", "C2235386_Ds05.xlsx", desired_no_of_rows=5)
        ia_run_obj.verify_table_data_set("html table", "C2235386_Ds05.xlsx", "Step 12.01: verify preview data")
        
        """
            Step 13 : Click "Save" > "C2235386" > Click "Save"
        """
        utillobj.switch_to_default_content(pause=1)
        vis_ribbon_obj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        """
            Step 14 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        """
            Step 15 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2235386.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infoassist_3',mrid='mrid', mrpass='mrpass')
        elem1=(By.CSS_SELECTOR, "#TableChart_1")
        resultobj._validate_page(elem1)
        """
            Step 16 : Verify Query pane and Preview
        """
        metaobj.verify_query_pane_field('By', 'Product,Category', 1, "Step 16.01: Verify Product, Category is visible underneath By", expected_color='Trolley_Grey', font_style='italic')
        metaobj.verify_query_pane_field('Sum', 'Cost of Goods', 1, "Step 16.02: Verify Cost of Goods is visible underneath Sum", expected_color='Trolley_Grey', font_style='italic')
        """
            Step 17 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        

if __name__ == "__main__":
    unittest.main()