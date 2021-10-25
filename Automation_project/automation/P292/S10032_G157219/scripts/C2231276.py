'''
Created on Nov 21, 2017

@author: BM13368
TestCase Name : InfoMini Report using Slicers 
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2231276
'''
import unittest, time, re
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, ia_ribbon, ia_run 
from common.lib import utillity  
from common.lib.basetestcase import BaseTestCase

class C2231276_TestClass(BaseTestCase):

    def test_C2231276(self):
        
        Test_Case_ID = "C2231276"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        ia_ribbobj = ia_ribbon.IA_Ribbon(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        """
            Step 01 : Launch IA Report mode:
            http://machine:port/ibi_apps/ia?tool=Report&master=baseapp/wf_retail_lite&item=IBFS%3A%2FWFC%2FRepository%2FS10032
        """
        utillobj.infoassist_api_login('report','new_retail/wf_retail_lite','P292/S10032_infoassist_4', 'mrid', 'mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 02 : Click Slicers Tab
        """
        ribbonobj.switch_ia_tab('Slicers')
        """
            Step 03 : Expand "Product" Dimension node > Click "Product" hierarchy
        """
        expected_list = ['Group 1', 'Drag Fields Here to Create Slicers']
        ia_ribbobj.verify_slicer_group(1, expected_list, 'Step 03:01: Group 1 slicer is available')
        
        """"
            Step 04 : Drag "Product" hierarchy into Slicers Tab > "Group 1"
        """
        metaobj.expand_field_tree('Product')
        metaobj.drag_drop_data_tree_group_to_slicers('Product',2,1)
        css_obj=self.driver.find_element_by_css_selector("#addSlicerDlg #addSlicerOkBtn")
        utillobj.click_on_screen(css_obj, 'middle', 0)
        time.sleep(2)
        
        """
            Step 05 : Verify the following slicers are displayed on the Slicers Ribbon
        """
        expected_list = ['Product', 'Product,Category', '  Product,Subcategory', '  Model']
        ia_ribbobj.verify_slicer_group(1, expected_list, 'Step 05:01: "Product" has been added to "Group 1"')
        group1=['Product', 'Product,Category', '  Product,Subcategory', '  Model']
        ia_ribbobj.verify_slicer_group(1, group1, "Step 05:02: Verify product Group has been added to Group1")
        """
            Step 06 : Click on "Product,Category" dropdown
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'Product,Category')
         
        """
            Step 07 : Verify the following options are available
        """
        expected_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 07:01: Verify the Product,Category options available")
        """
            Step 08 : Select "Televisions" > "OK"
        """
        ia_ribbobj.select_slicer_values_from_single_list(['Televisions'])
        ia_ribbobj.close_slicer_dialog('ok')
        time.sleep(2)
        """
            Step 09 : Click on "Product,Subcategory" dropdown
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'Product,Subcategory')
        time.sleep(1)
        """
            Step 10 : Verify the following options are available
        """
        expected_list=['CRT TV', 'Flat Panel TV', 'Portable TV']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 10:01: Verify the Product,Subcategory options available")
        """
            Step 11 : Select "Flat Panel TV" > "OK"
        """
        ia_ribbobj.select_slicer_values_from_single_list(['Flat Panel TV'])
        ia_ribbobj.close_slicer_dialog('ok')
        
        """
            Step 12 : Click on "Model" dropdown
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'Model')
        
        """
            Step 13 : Verify the following options are available
        """
        expected_list=['LG 19LE5300 19', 'LG 32LE5300 32', 'Panasonic 58TV25BNDL', 'Panasonic TCP46G25', 'Sony KDL32EX400', 'Sony KDL46HX800', 'Sony KDL60EX500']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 13:01: Verify the Model options available")
        """
            Step 14 : Click "Cancel"
        """
        ia_ribbobj.close_slicer_dialog('cancel')
        time.sleep(2)
        """
            Step 15 : Double-click fields "Product,Category", "Product,Subcategory" and "Model"
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(3)
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        time.sleep(3)
        metaobj.datatree_field_click("Model", 2, 1)
        time.sleep(3)
        
        """
            Step 16 : Verify Preview
        """
        coln_list = ["ProductCategory", "ProductSubcategory", "Model"]
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 16:01: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 3, 3, "C2231276_Ds01.xlsx", 'Step 17:01: Verify report dataset')
        
        """
            Step 17 : Click Run > Verify output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2231276_Ds02.xlsx" , 'Step 17:01: Verify report dataset')
        utillobj.switch_to_default_content(pause=1)
        
        """
            Step 18 : Click on "Model" dropdown in the Slicer Tab Ribbon
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'Model')
        
        """
            Step 19 : Multi-select all the Sony models > Click OK
        """
        ia_ribbobj.select_slicer_values_from_single_list(['Sony KDL32EX400', 'Sony KDL46HX800', 'Sony KDL60EX500'])
        ia_ribbobj.close_slicer_dialog('ok')
        time.sleep(1)
        """
            Step 20 : Click "Update Preview" in the Slicers Tab
        """
        update_preview=self.driver.find_element_by_css_selector("#slicersUpdatePreviewBtn img")
        utillobj.click_on_screen(update_preview, 'middle', 0)
        time.sleep(5)
        
        """
            Step 21 : Verify Preview and Slicers Ribbon
        """
        group1=['Product', 'Product,Category1.1', 'Televisions', ' Product,Subcategory1.2', 'Flat Panel TV', ' Model1.3', 'Multiple']
        ia_ribbobj.verify_slicer_group(1, group1, "Step 21:01: Verify updated product slicers in Group1")
        coln_list = ["ProductCategory", "ProductSubcategory", "Model"]
        resultobj.verify_report_titles_on_preview(3, 6, "TableChart_1", coln_list, "Step 21:02: Verify column titles")
#         ia_resultobj.create_report_data_set("TableChart_1", 3, 3, 'C2071379_Ds03.xlsx', no_of_cells=6)
        ia_resultobj.verify_report_data_set("TableChart_1", 3, 3, "C2231276_Ds03.xlsx", "Step 21:03 verify data set", no_of_cells=6)
        """
            Step 22 : Click Run > Verify output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2231276_Ds04.xlsx" , 'Step 22:01: Verify report dataset')
        
        """
            Step 23 : Select the Format Tab > Click the "InfoMini" menu > Select "Slicer Tab (Edit)" and "Resources\Field Tab"
        """
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Slicer Tab (Edit)")
        time.sleep(2)
        ribbonobj.select_ribbon_item("Format", "Infomini_arrow")
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu("Resources/Field Tab")
        time.sleep(2)
        """
            Step 24 : Click "IA" menu > Click "Save As" > "C2231276" > Click "Save"
        """
        
        ribbonobj.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(2)
        
        """
            Step 25 : Click Run
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.switch_to_window(1)
        parent_css="#interactiveModeButton"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 26 : Verify InfoMini Application is launched
        """
        css_obj=self.driver.find_element_by_css_selector("#interactiveModeButton")
        status=css_obj.is_displayed()
        utillobj.asequal(status, True, "Step 26 :01: Verify Infomini Application is launched")
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2231276_Ds05.xlsx" , 'Step 26:02: Verify report dataset')
        """
            Step 27 : Click "Edit" in the InfoMini toolbar
        """
        utillobj.switch_to_default_content(pause=1)
        ribbonobj.select_top_toolbar_item('infomini_edit')
        parent_css="#IaToolbar"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 28 : Click Slicers Tab
        """
        ribbonobj.switch_ia_tab("Slicers")
        time.sleep(10)
        """
            Step 29 : Double-click field "Cost of Goods"
        """
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(10)
        """
            Step 30 : Click "Model" slicer in the Slicer Tab > Multi-select all the Panasonic values
        """
        ia_ribbobj.select_group_slicer_dropdown(1, 'Model1.3')
        time.sleep(2)
        expected_list=['LG 19LE5300 19', 'LG 32LE5300 32', 'Panasonic 58TV25BNDL', 'Panasonic TCP46G25', 'Sony KDL32EX400', 'Sony KDL46HX800', 'Sony KDL60EX500']
        menu_items=driver.find_elements_by_css_selector("#filterValuesList table tr > td")
        actual_menu_list=[el.text.strip() for el in menu_items[:-1]]
        utillobj.asequal(expected_list, actual_menu_list, "Step 30:01: Verify the Model options available")
        ia_ribbobj.select_slicer_values_from_single_list(['Panasonic 58TV25BNDL', 'Panasonic TCP46G25'])
        
        """
            Step 31 : Click OK
        """
        ia_ribbobj.close_slicer_dialog('ok')
        time.sleep(2)
        """
            Step 32 : Click Run in the InfoMini toolbar
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        ribbonobj.switch_ia_tab("Slicers")
        
        """
            Step 33 : Verify output and Slicer ribbon
        """
        group1=['Product', 'Product,Category1.1', 'Televisions', ' Product,Subcategory1.2', 'Flat Panel TV', ' Model1.3', 'Multiple']
        ia_ribbobj.verify_slicer_group(1, group1, "Step 33:01: Verify updated product slicers in Group1")
        utillobj.switch_to_frame(pause=2)
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2231276_Ds06.xlsx" , 'Step 33:03: Verify report dataset')
        utillobj.switch_to_default_content(pause=1)
        
        """
            Step 34 : Click "Save" in the InfoMini toobar > Save As "C2231276_IM"
        """
        ribbonobj.select_top_toolbar_item('infomini_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        """
            Step 35 : Close the InfoMini application 
            Step 36 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        driver.close()
        utillobj.switch_to_window(0)
        utillobj.infoassist_api_logout()
        
        """
            Step 37 : Reopen saved FEX:
            http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FS10006%2FC2231276.fex&tool=Report
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'report', 'S10032_infosassist_4', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 38 : Verify Preview
        """
        coln_list = ["ProductCategory", "ProductSubcategory", "Model", "Cost of Goods"]
        resultobj.verify_report_titles_on_preview(4, 8, "TableChart_1", coln_list, "Step 38:01: Verify column titles")
        ia_resultobj.verify_report_data_set('TableChart_1', 3, 4, "C2231276_Ds07.xlsx", 'Step 38:02: Verify report dataset')
        
        """
            Step 39 : Select Format Tab > Verify InfoMini is enabled
        """
        ribbonobj.switch_ia_tab("Format")
        time.sleep(10)
        """IA-4076
            Request saved from InfoMini application does not show InfoMini option enabled when opened in IA(There is a ticket for this)
        """
        infomini_css=driver.find_element_by_css_selector("#FormatApplicationRibbonEnable")
        status=True if bool(re.match('.*-checked.*', infomini_css.get_attribute("class"))) else False
        utillobj.asequal(True, status, "Step 39:01: Verify infomini is selected.")
        """
            Step 40 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 41 : Run the saved InfoMini FEX:
            http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FS10032&BIP_item=C2231276_IM.fex
        """
        utillobj.active_run_fex_api_login(Test_Case_ID+".fex", "S10032_infoassist_4", 'mrid', 'mrpass')
        utillobj.switch_to_frame(pause=2)
        parent_css="table[summary= 'Summary']"
        resultobj.wait_for_property(parent_css, 1)
        
        """
            Step 42 : Verify output
        """
        ia_runobj.verify_table_data_set("table[summary='Summary']", "C2231276_Ds08.xlsx" , 'Step 42:01: Verify report dataset')
        
        """
            Step 43 : Logout:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        

if __name__ == "__main__":
    unittest.main()