'''
Created on Jan 16, 2018
TestSuite : AR14 - Active Document
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10071&group_by=cases:section_id&group_order=asc&group_id=160952
TestCase ID: http://172.19.2.180/testrail/index.php?/cases/view/2251614
TestSuite Name : Verify Dashboard with 2 reports and 2 prompts (a dropdown and a radio button) works as expected
@author: BM13368
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251614_TestClass(BaseTestCase):

    def test_C2251614(self):
        
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251614'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
   
        """
            Step 01:Launch IA to develop a new Document.
            Select 'GGSales' as master file, and change output format as Active report.
            Select fields as Category, Product, Product ID, State, Unit Sales and Dollar Sales.
        """ 
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 65)
        metaobj.datatree_field_click("Category", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 30)
        metaobj.datatree_field_click("Product ID", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 30)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, 30)    
        metaobj.datatree_field_click("State", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 28, 30)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 48, 30)
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 68, 30)
            
        ribbonobj.repositioning_document_component('0.35', '1.04')
            
        coln_list = ["Category", "Product ID", "Product", "State", "Unit Sales", "Dollar Sales"]
        resultobj.verify_report_titles_on_preview(6, 6, "TableChart_1 ", coln_list, "Step 01:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_1', 18, 6, Test_Case_ID+"_Ds01.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_1', 18, 6, Test_Case_ID+"_Ds01.xlsx", 'Step 01:02: Verify Preview report dataset')
        time.sleep(5)
        
                 
        """ 
            Step 02:Select Radio button from 'Insert' tab
        """
        ribbonobj.select_ribbon_item("Insert", "Radio_Button")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 35)
        ribbonobj.repositioning_document_component('5.40', '.25')
        
        """ 
            Step 03:Right click on radio button.
            In Properties window assign Field value as Product ID. Make sure Condition is set as Equal to and Include All is checked.
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        source_item= {'select_field':'Product ID', 'verify_condition':'Equal to', 'verify_includeall':True}
        resultobj.customize_active_dashboard_properties(source=source_item, msg="Step 03.")
          
        """ 
            Step 04:Click on blank area in design area, and select Product, State and Unit Sales to get another report. Drag report to the right side.
        """
        canvas_css=driver.find_element_by_css_selector("#theCanvas")
        utillobj.click_on_screen(canvas_css, "top_middle", click_type=0)
        time.sleep(5)
        metaobj.datatree_field_click("Product", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 3, 30)
        metaobj.datatree_field_click("State", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 23, 30)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 43, 30)
        ribbonobj.repositioning_document_component('6.85', '1.04')
          
        coln_list = ["Product", "State", "Unit Sales"]
        resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2 ", coln_list, "Step 04:01: Verify column titles")
#         ia_resultobj.create_report_data_set('TableChart_2', 18, 3, Test_Case_ID+"_Ds02.xlsx")
        ia_resultobj.verify_report_data_set('TableChart_2', 18, 3, Test_Case_ID+"_Ds02.xlsx", 'Step 04:02: Verify Preview report dataset')
        
        """ 
            Step 05:Now, select drop down box from 'Insert' tab
        """
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        utillobj.synchronize_with_number_of_element("#Prompt_2", 1, 35)
        ribbonobj.repositioning_document_component('1.04', '0.35')
        
        """ 
            Step 06:Right click on Drop down button.
            Select Report as Report 2. In Properties window assign Field value as State. Make sure Condition is set as Equal to and Include All is checked.
            Step 07:Click OK button.
        """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_2','Properties')
        source_items={'select_report':'Report2','select_field':'State','verify_condition':'Equal to','verify_field':'State','verify_includeall':True}
        resultobj.customize_active_dashboard_properties(source=source_items, msg='Step 06:01:Verify dashboard prompts')
        time.sleep(8)
          
        """ 
            Verify that Radio button prompt shows Product IS values and Drop down button shows States.
        """
        val1=['[All]', 'C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        ia_resultobj.verify_active_dashboard_prompts('radiobutton', '#Prompt_1', val1, "Step 07:01:Verify radio button values")

        exp_val=['[All]', 'CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        elem=self.driver.find_element_by_css_selector("#Prompt_2 [id^='BiComboBox']")
        utillobj.verify_combo_box_item(exp_val, elem, combobox_dropdown_css=None, msg='Step 07:02:Verify dropdown values')
        
        canvas_css=driver.find_element_by_css_selector("#theCanvas")
        utillobj.click_on_screen(canvas_css, "top_middle", click_type=0)
        time.sleep(2)
        
        """ 
            Step 08:Click run.
        """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 65)
        utillobj.switch_to_frame(pause=1)
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 45)
        
        miscobj.verify_page_summary(0, '107of107records,Page1of2', 'Step 08:01: Verify the Report Heading')
        column_list=["Category", "Product ID", "Product", "State","Unit Sales", "Dollar Sales"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 08:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds03.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds03.xlsx", 'Step 08:03: Verify data.')
        
        radio_val1=['[All]', 'C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        ia_runobj.verify_active_dashboard_prompts('radiobutton', "div[id^='PROMPT_1']", radio_val1, "Step 08:04: Verify list of values in the added radio button", default_selected_check='[All]')
   
        exp_val=['[All]', 'CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA'] 
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_2", value_list=exp_val, msg="Step 08:05:Verify list of prompt2 dropdown values", expected_default_selected_value='[All]', default_selection_msg="Step 08:06 Verify selected value is All")
    
        miscobj.verify_page_summary(1, '107of107records,Page1of2', 'Step 08:06: Verify the Report Heading')
        column_list=["Product", "State","Unit Sales"]
        miscobj.verify_column_heading('ITableData1', column_list, 'Step 08:07: Verify the column heading')
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+"_Ds04.xlsx")
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+"_Ds04.xlsx", 'Step 08:08: Verify second report table data.')
        
        """ 
            Step 09:Select C142 product ID from radio prompt and select GA state from drop down prompt.
            Verify radio prompt filters the first report and return 11 records. Verify drop down prompt filters second report and return 10 records.
        """
        ia_runobj.select_active_dashboard_prompts('radiobutton', "div[id^='PROMPT_1']", ['C142'])
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0 span", 'Category', 45)
        
        miscobj.verify_page_summary(0, '11of107records,Page1of1', 'Step 09:01: Verify the Report Heading')
        column_list=["Category", "Product ID", "Product", "State","Unit Sales", "Dollar Sales"]
        miscobj.verify_column_heading('ITableData0', column_list, 'Step 09:02: Verify the column heading')
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds05.xlsx")
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID+"_Ds05.xlsx", 'Step 09:03: Verify first report table data.')

        utillobj.select_dropdown("#combobox_dsPROMPT_2", "visible_text", "GA")
        utillobj.synchronize_with_visble_text("#ITableData1 #TCOL_1_C_0 span", 'Product', 45)
        exp_val=['[All]', 'CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_2", value_list=exp_val, msg="Step 09:04:01:Verify dropdown values", expected_default_selected_value='GA', default_selection_msg="Step 09:04:02: Verify dropdown value is GA selected")
        
        miscobj.verify_page_summary(1, '10of107records,Page1of1', 'Step 09:05: Verify the Report Heading')
        column_list=["Product", "State","Unit Sales"]
        miscobj.verify_column_heading('ITableData1', column_list, 'Step 09:06: Verify the column heading')
#         utillobj.create_data_set('ITableData1', 'I1r', Test_Case_ID+"_Ds06.xlsx")
        utillobj.verify_data_set('ITableData1', 'I1r', Test_Case_ID+"_Ds06.xlsx", 'Step 09:06: Verify second report table data.')
        utillobj.switch_to_default_content(pause=1)
        

if __name__ == "__main__":
    unittest.main()