'''
Created on May 9, 2018

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/64295&group_by=cases:section_id&group_order=asc&group_id=167893
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2313569
TestCase Name = Verify multiple Currency Formats in Document Mode
'''

import unittest
import time
from common.lib import utillity
from common.pages import visualization_metadata,visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib.basetestcase import BaseTestCase

class C2313569_TestClass(BaseTestCase):

    def test_C2313569(self):
        
        Test_Case_ID = "C2313569"
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver) 
        ia_result_obj = ia_resultarea.IA_Resultarea(self.driver)
        miscelanousobj = active_miscelaneous.Active_Miscelaneous(self.driver)
        
        """
        Step 01:Launch Document Mode:
        http://machine:port/ibi_apps/ia?tool=document&master=baseapp/wf_retail_lite&item=IBFS:/WFC/Repository/S10660
        """
        utillobj.infoassist_api_login('document','baseapp/wf_retail_lite','P292/S10660_infoassist_2', 'mrid', 'mrpass')
        parent_css="#canvasFrame"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        
        """
        Step 02:Add fields 'Product,Category' and 'Cost of Goods'
        """
        metaobj.datatree_field_click("Product,Category", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Cost of Goods", 2, 1)
        time.sleep(5)
         
        """
        Verify report data at live preview
        """
        coln_list = ['ProductCategory', 'Cost of Goods']
        resobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 02:01: Verify report titles")
#         ia_result_obj.create_report_data_set('TableChart_1', 5, 2, Test_Case_ID+"_Ds01.xlsx", no_of_cells=4)
        ia_result_obj.verify_report_data_set('TableChart_1', 5, 2, Test_Case_ID+"_Ds01.xlsx", 'Step 02:02: Verify report dataset', no_of_cells=4)
        
        """
        Step 03: Click on 'Cost of Goods' in the Query Pane > Click on the "Change currency options" button in the Field Tab Ribbon
        """
        metaobj.querytree_field_click("Cost of Goods",1)
        time.sleep(5)
        parent_css="#FieldFormatCurrency div[class$='drop-down-arrow']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        ribbonobj.select_ribbon_item('Field', 'formatcurrency')

        """
        Step 04: Verify list of options
        Step 05: Select "Floating Euro symbol" 
        """
        time.sleep(5)
        list1=['Floating Currency','Non-floating Currency','Fixed Euro symbol','Floating Euro symbol','Euro symbol on the right','Fixed pound sterling sign','Floating pound sterling sign','Fixed Japanese yen symbol','Floating Japanese yen symbol','Fixed dollar sign','Floating dollar sign','Dollar sign on the right','Dollar sign on the left']
        utillobj.select_or_verify_bipop_menu('Floating Euro symbol',verify=True,expected_popup_list=list1,msg='Step 05: ')
        
        """
        Step 06: Verify selected currency symbol is displayed in the preview canvas
        """
        time.sleep(8)
        coln_list = ['ProductCategory', 'Cost of Goods']
        resobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 06:01: Verify report titles")
#         ia_result_obj.create_report_data_set('TableChart_1', 5, 2, Test_Case_ID+"_Ds02.xlsx", no_of_cells=4)
        ia_result_obj.verify_report_data_set('TableChart_1', 5, 2, Test_Case_ID+"_Ds02.xlsx", 'Step 06:02: Verify report dataset', no_of_cells=4)
        
        """
        Step 07: Select Insert Tab > Report
        """
        ribbonobj.select_ribbon_item('Insert', 'report')
        
        """  
        Step 08: Place the new Report next to the current component (side by side)
        """
        parent_css="#TableChart_2"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        ribbonobj.repositioning_document_component('5','1.5')
        time.sleep(5)
        
        """
        Step 09: Add fields "Product,Subcategory" and "Gross Profits"
        """
        metaobj.datatree_field_click("Product,Subcategory", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Gross Profit", 2, 1)
        time.sleep(5)
        
        """
        Verify the canvas,
        """
        coln_list = ['ProductSubcategory', 'Gross Profit']
        resobj.verify_report_titles_on_preview(2, 4, "TableChart_2", coln_list, "Step 09:01: Verify report titles")
#         ia_result_obj.create_report_data_set('TableChart_2', 5, 2, Test_Case_ID+"_Ds03.xlsx", no_of_cells=4)
        ia_result_obj.verify_report_data_set('TableChart_2', 5, 2, Test_Case_ID+"_Ds03.xlsx", 'Step 09:02: Verify report dataset', no_of_cells=4)
        
        """
        Step 10: Select "Gross Profits" in the Query Pane
        """
        metaobj.querytree_field_click("Gross Profit",1)
        time.sleep(5)
        
        """
        Step 11: Click on the "Decimal" dropdown box in the Field Tab Ribbon > Select "More options..."
        """
        ribbonobj.select_ribbon_item('Field', 'formattype')
        time.sleep(5)
        parent_css="div[id^='BiPopup'][style*='inherit']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        utillobj.select_or_verify_bipop_menu('More options...', custom_css="div[id^='BiComboBoxItem']")

        """        
        Step 12: Select "Fixed Euro symbol" > Click OK
        """
        parent_css="div[id='fmtDlgOk']"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 20)
        combo_btn_elem=driver.find_element_by_css_selector("#currencySymbolCBox div[class$='combo-box-arrow']")
        utillobj.default_left_click(object_locator=combo_btn_elem)
        parent_css="div[id^='BiPopup'][style*='inherit']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        utillobj.select_or_verify_bipop_menu('Fixed Euro symbol',custom_css="div[id^='BiComboBoxItem']")
        time.sleep(5)
        close_elem=driver.find_element_by_css_selector('div[id="fmtDlgOk"]')
        utillobj.default_left_click(object_locator=close_elem)
        time.sleep(5)
        
        """
        Step 13: Verify the canvas,
        """
        coln_list = ['ProductSubcategory', 'Gross Profit']
        resobj.verify_report_titles_on_preview(2, 4, "TableChart_2", coln_list, "Step 13:01: Verify report titles")
#         ia_result_obj.create_report_data_set('TableChart_2', 1, 2, Test_Case_ID+"_Ds04.xlsx", no_of_cells=4)
        ia_result_obj.verify_report_data_set('TableChart_2', 1, 2, Test_Case_ID+"_Ds04.xlsx", 'Step 13:02: Verify report dataset', no_of_cells=4)
        
        """
        Step 14: Select Insert Tab > Page
        """
        ribbonobj.select_ribbon_item('Insert', 'page')
        time.sleep(5)
        
        """
        Step 15: Add fields "Model" and "Discount"
        """
        metaobj.datatree_field_click("Model", 2, 1)
        time.sleep(5)
        metaobj.datatree_field_click("Discount", 2, 1)
        time.sleep(5)
        
        """
        Verify the canvas,
        """
        coln_list = ['Model', 'Discount']
        resobj.verify_report_titles_on_preview(2, 2, "TableChart_3", coln_list, "Step 15:01: Verify report titles")
#         ia_result_obj.create_report_data_set('TableChart_3', 5, 2, Test_Case_ID+"_Ds05.xlsx", no_of_cells=2)
        ia_result_obj.verify_report_data_set('TableChart_3', 5, 2, Test_Case_ID+"_Ds05.xlsx", 'Step 15:02: Verify report dataset', no_of_cells=2)
        
        """
        Step 16: Select "Discount" in the Query Pane > Click on the "Change currency options" button in the Field Tab ribbon
        """
        metaobj.querytree_field_click("Discount",1)
        time.sleep(5)
        parent_css="#FieldFormatCurrency div[class$='drop-down-arrow']"
        resobj.wait_for_property(parent_css, 1,expire_time=20)
        ribbonobj.select_ribbon_item('Field', 'formatcurrency')

        """
        Step 17: Select "Floating Japanese yen symbol"
        """
        time.sleep(5)
        utillobj.select_or_verify_bipop_menu('Floating Japanese yen symbol')
        
        """
        Step 18: Verify Canvas
        """
        time.sleep(8)
        coln_list = ['Model', 'Discount']
        resobj.verify_report_titles_on_preview(2, 2, "TableChart_3", coln_list, "Step 18:01: Verify report titles")
#         ia_result_obj.create_report_data_set('TableChart_3', 5, 2, Test_Case_ID+"_Ds06.xlsx")
        ia_result_obj.verify_report_data_set('TableChart_3', 5, 2, Test_Case_ID+"_Ds06.xlsx", 'Step 18:02: Verify report dataset')
        
        """ 
        Step 19: Click Run > Verify output
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        parent_css="#resultArea [id^=ReportIframe-]"
        resobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(1)
        utillobj.switch_to_frame(pause=2)
        
        parent_css="#ITableData0"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        miscelanousobj.verify_page_summary('0','7of7records,Page1of1', 'Step 19.1.a: Verify report1 Page summary')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+'_run_Ds01.xlsx', "Step 19.1.b: Verify runtime report1")
        
        time.sleep(5)
        miscelanousobj.verify_page_summary('1','21of21records,Page1of1', 'Step 19.2.a: Verify report2 Page summary')
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+'_run_Ds02.xlsx')
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+'_run_Ds02.xlsx', "Step 19.2.b: Verify runtime report2")
        
        """ 
        Step 20: Select "Page 2" > Verify output
        """
        select_css = "#IBILAYOUTDIV0TABS .arDashboardBarButton[id^='iLay']"
        self.driver.find_element_by_css_selector(select_css).click()

        parent_css="#ITableData2"
        utillobj.synchronize_with_number_of_element(parent_css, 1, 30)
        miscelanousobj.verify_page_summary('2','157of157records,Page1of3', 'Step 20.a: Verify report1 Page summary')
#         utillobj.create_data_set('ITableData2', 'I2r', Test_Case_ID+'_run_Ds03.xlsx')
        utillobj.verify_data_set('ITableData2', 'I2r', Test_Case_ID+'_run_Ds03.xlsx', "Step 20.b: Verify report1")
        
        time.sleep(2)
        utillobj.switch_to_default_content(pause=3)
        
        """ 
        Step 21: Click "Save" > Save As "C2313569" > Click Save
        """ 
        ribbonobj.select_tool_menu_item('menu_save_as')
        time.sleep(3)
        utillobj.ibfs_save_as(Test_Case_ID)
        time.sleep(3)
        
        """  
        Step 22:Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        time.sleep(2)
        
        """  
        Step 23:Restore saved Fex:
        http://machine:port/ibi_apps/iaitem=IBFS:/WFC/Repository/Public/C2313569.fex&tool=vis
        """
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', 'S10660_infoassist_2', mrid='mrid', mrpass='mrpass')
        parent_css="#TableChart_1"
        resobj.wait_for_property(parent_css, 1, expire_time=15)
        time.sleep(3)
        
        """
        Step 24: Verify the canvas,
        """
        coln_list = ['ProductCategory', 'Cost of Goods']
        resobj.verify_report_titles_on_preview(2, 4, "TableChart_1", coln_list, "Step 24:01: Verify report titles")
        ia_result_obj.verify_report_data_set('TableChart_1', 5, 2, Test_Case_ID+"_Ds02.xlsx", 'Step 24:02: Verify report dataset', no_of_cells=4)
        
        coln_list = ['ProductSubcategory', 'Gross Profit']
        resobj.verify_report_titles_on_preview(2, 4, "TableChart_2", coln_list, "Step 24:03: Verify report titles")
        ia_result_obj.verify_report_data_set('TableChart_2', 5, 2, Test_Case_ID+"_Ds04.xlsx", 'Step 24:04: Verify report dataset', no_of_cells=4)
        
        """ 
        Step 40:Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()