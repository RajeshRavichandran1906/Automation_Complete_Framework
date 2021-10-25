'''
Created on Jan 16, 2018

@author: BM13368
TestSuite Name:AR14 - Active Document 
TestSuite ID: http://172.19.2.180/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc&group_id=160952
TestCase ID:http://172.19.2.180/testrail/index.php?/cases/view/2251613
TestCase Name :Verify that user should be able change the Source field under prompts and yield expected results
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous
from common.lib import utillity


class C2251613_TestClass(BaseTestCase):

    def test_C2251613(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251613'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        """
            Step 01:Launch IA to develop a new Document.
            Select 'GGSales' as master file, and change output format as Active report.
            Create a report with these fields: Category, Product ID, Product, State, Unit Sales and Dollar Sales.
        """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=65, string_value='Document')
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn", "Category", 190)    
        metaobj.datatree_field_click("Product ID", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn", "Product ID", 190)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn", "Product", 190)    
        metaobj.datatree_field_click("State", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn", "State", 190)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn", "Unit Sales", 190)
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_visble_text("#queryTreeColumn", "Dollar Sales", 190)
        
        coln_list = ["Category", "Product ID", "Product", "State", "Unit Sales", "Dollar Sales"]
        resultobj.verify_report_titles_on_preview(6, 6, "TableChart_1 ", coln_list, "Step 05:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 18, 6, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 18, 6, Test_Case_ID+"_Ds01.xlsx", 'Step 01:02: Verify Preview report dataset')
        """    
            Step 02:Click Drop down prompt from Insert menu
        """
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        ribbonobj.repositioning_document_component('6.50', '1.5')
        """ 
            Step 03:Right click on 'Drop down' box and select 'Properties' from canvas.
        """
        combo_box=driver.find_element_by_id("Prompt_1")
        utillobj.default_click(combo_box, click_option=1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Properties')
        time.sleep(1)
        
        """     
            Step 04:Select Field = Unit Sales.
            Verify the Condition is set to Equal to and Include All is checked.
        """
        properties_dlg="#adpPropertiesDlg [class*='caption']"
        resultobj.wait_for_property(properties_dlg, 1, expire_time=15)
        utillobj.select_combobox_item('comboSourceFields', 'Unit Sales')
        time.sleep(1)
        menu_item=driver.find_element_by_css_selector("#checkShowAll input").get_attribute("checked")
        expected_val='true'
        utillobj.asequal(menu_item, expected_val, "Step 04:01: Verify Include all checkbox is selected")
        condition_combo_value=driver.find_elements_by_css_selector("#comboConditions")
        cond_val=[el.text.strip() for el in condition_combo_value]
        expected_val=['Equal to']
        utillobj.asequal(cond_val, expected_val, "Step 04:02: Verify condition value is set to Equal to")
        """ 
            Step 05:Click 'OK' and run.
            Verify by default unit sales is set to "All" value in drop down prompt.
        """
        ok_Btn=driver.find_element_by_css_selector('#btnADPOK img')
        utillobj.default_left_click(object_locator=ok_Btn)
        time.sleep(5)
        
        ribbonobj.select_top_toolbar_item('toolbar_run')
        time.sleep(15)
        utillobj.switch_to_frame(pause=1)
        
        miscobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 05:01: Verify the Report Heading')
        column_list=["Category", "Product ID", "Product", "State","Unit Sales", "Dollar Sales"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 05:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds02.xlsx", 'Step 05:03: Verify data.')
        option_css=driver.find_element_by_css_selector("#combobox_dsPROMPT_1").get_attribute('value')
        print(option_css)
        expected_val='[All]'
        utillobj.asequal(option_css, expected_val, "Step 05:04: Verify drop down combobox is selected ALL")
        utillobj.switch_to_default_content(pause=1)
        
        """ 
            Step 06:Close the window and user will be in preview mode.
        """
        resultobj.select_panel_caption_btn(0, 'close', custom_css="[class*='window-caption']")
        time.sleep(10)
        """ 
            Step 07:Right click on 'Drop down' box and select 'Properties' from canvas
        """
        combo_box=driver.find_element_by_id("Prompt_1")
        utillobj.default_click(combo_box, click_option=1)
        time.sleep(1)
        utillobj.select_or_verify_bipop_menu('Properties')
        time.sleep(1)
        """ 
            Step 08:Change the field value from Unit Saels to Product ID.
            Active Dashboard Properties pop up will show message as "Changing the source field for control Prompt_1 will remove Prompt_1 and any children controls from the existing cascades"
        """
        properties_dlg="#adpPropertiesDlg [class*='active'] [class*='window'][class*='caption']"
        resultobj.wait_for_property(properties_dlg, 1, expire_time=15)
        utillobj.select_combobox_item('comboSourceFields', 'Product ID')
        time.sleep(1)
        prompt_css="#promptDlg"
        resultobj.wait_for_property(prompt_css, 1, expire_time=15)
        err_dlg="#msgBox #errLabel"
        elem1=driver.find_element_by_css_selector(err_dlg).get_attribute('text')
        expected_val="Changing the source field for control combobox_1 will remove combobox_1and any children controls from the existing cascades.Click OK to continue.Click Cancel to keep the original source field."
        utillobj.asequal(elem1, expected_val, "Step 08:01: Verify error message")
        
        """ 
            Step 09:Select 'OK'
            Field value will be displayed as "Product ID"
        """
#         css="#promptDlg #btnOK"
        prompt_dlg=driver.find_element_by_css_selector("#promptDlg #btnOK")
        utillobj.default_left_click(object_locator=prompt_dlg)
#         utillobj.synchronize_until_element_disappear(css, 15)
        field_css=driver.find_element_by_css_selector("#comboSourceFields")
        field_val=field_css.get_attribute('text').strip()
        expected_val='Product ID'
        utillobj.asequal(field_val, expected_val, "Step 09:01:Verify field value is selected as Product ID")
        
        """ 
            Step 10:Click OK and run the Document.
        """
        ok_Btn=driver.find_element_by_css_selector('#btnADPOK img')
        utillobj.default_left_click(object_locator=ok_Btn)
        time.sleep(5)

if __name__ == "__main__":
    unittest.main()