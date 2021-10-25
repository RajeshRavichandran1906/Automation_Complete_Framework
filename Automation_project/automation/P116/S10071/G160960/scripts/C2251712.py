'''
Created on Feb 06, 2018

@author: Praveen Ramkumar

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10851
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251712
TestCase Name = Create a chart using multi-page Document
'''

import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, visualization_resultarea, active_miscelaneous, ia_run
from common.lib.basetestcase import BaseTestCase

class C2251712_TestClass(BaseTestCase):

    def test_C2251712(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2251712'
        driver = self.driver
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelaneousobj = active_miscelaneous.Active_Miscelaneous(driver)
        ia_runobj = ia_run.IA_Run(self.driver)

        """
        Step 01: Create New> Document via IA tool.
        Select 'GGSales' as master file, and make sure format of the report is Active report.        
        """
        
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_4', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 65)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 01: Verify output format as Active report.")
        
        """
            Select Category, Product,Unit Sales to get a report
        """
        vis_metadata.datatree_field_click('Category', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 2, 20)
         
        vis_metadata.datatree_field_click('Product', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 5, 20)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        element_css="#TableChart_1 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 8, 20)
        
        column_list=['Category', 'Product', 'Unit Sales']
        vis_resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", column_list, "Step 01:01: Verify column titles")
        
        """
        Step 02: Select Dropdown box from 'Insert' tab,right click on dropdown box and assign "Products" in property of dropdown box
        Step 03:Click Ok. Verify [All] default value is displayed.
        """
        
        vis_ribbon.select_ribbon_item("Insert", "Drop_down")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 25)
        ia_resultobj.drag_drop_document_component('#Prompt_1', '#TableChart_1', 70, 0)
        time.sleep(2)
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1','Properties')
        
        source={'select_field':'Product'}
        vis_resultobj.customize_active_dashboard_properties(source=source, msg="Step 02:01:", btn_type='ok')
        time.sleep(3)       
        
        """
           Step 04: To add another page select Insert tab, in the Pages group click blank page. Page 2, will be inserted after the current page, and appears on the canvas
        """
        
        vis_ribbon.select_ribbon_item("Insert", "Page")
        parent_css="#iaPagesMenuBtn div[class='bi-button-label']"
        vis_resultobj.wait_for_property(parent_css, 1, 25, string_value='Page 2')
        exp_page_text = 'Page 2'
        elem_css = driver.find_element_by_css_selector("#iaPagesMenuBtn div[class='bi-button-label']")
        act_page_text = elem_css.text.strip()
        print(act_page_text)
        utillobj.asequal(act_page_text, exp_page_text,  "Step 04: Verify Page 2 appears on the canvas")
        
        """
           Step 05:Add text box from insert menu change the text content to "Create a Report Multi-page Document Page Two"
        """
        vis_ribbon.select_ribbon_item("Insert", "Text_Box")
        utillobj.synchronize_with_number_of_element("#Text_1", 1, 20)
        vis_ribbon.resizing_document_component('0.5', '3.5')
        time.sleep(3)
        ia_resultobj.enter_text_in_Textbox('Text_1', "Step 05:Create a Report Multi-page Document Page Two")
        
        """
           Step 06:Create a new report and select Product ID, Region, Dollar Sales
        """
        
        vis_ribbon.select_ribbon_item("Insert", "report")
        utillobj.synchronize_with_number_of_element("#TableChart_2", 1, 20)
        
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        element_css="#TableChart_2 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 3, 20)
         
        vis_metadata.datatree_field_click('Region', 2, 0)
        element_css="#TableChart_2 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 11, 20)
        
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        element_css="#TableChart_2 div[class^='x']"
        utillobj.synchronize_with_number_of_element(element_css, 19, 20)
        
        column_list=['Product ID', 'Region', 'Dollar Sales']
        vis_resultobj.verify_report_titles_on_preview(3, 3, "TableChart_2", column_list, "Step 06:01: Verify column titles")
        
        ia_resultobj.drag_drop_document_component('#TableChart_2', '#Text_1', 90, 0)
        
        """
           Step 07:Select List box from 'Insert' tab,right click on List box and assign Dollar Sales in property of list box
        """
        vis_ribbon.select_ribbon_item("Insert", "list")
        utillobj.synchronize_with_number_of_element("#Prompt_2", 1, 20)
        ia_resultobj.drag_drop_document_component('#Prompt_2', '#TableChart_2', 70, 0)
        
        ia_resultobj.verify_active_dashboard_prompts("listbox", "#Prompt_2", ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5'], "Step 07:01:Verify dropdown value")
        
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_2','Properties')
        source={'select_report':'Report2','select_field':'Dollar Sales'}
        vis_resultobj.customize_active_dashboard_properties(source=source, msg="Step 07:01:", btn_type='ok')
        time.sleep(3)
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 25)
        utillobj.switch_to_frame(pause=2)
        page_1_css="#IBILAYOUTDIV0 div[id='iLay$1'][class*='arDashboardBarButton']"
        utillobj.synchronize_with_number_of_element(page_1_css, 1, 45)
        
        """
           Step 08:Click Ok and run the dashboard.
            Verify that Reports with Mulit-Page document output should have the following options Layout tab, Page1 and Page2. User is able to navigate the output from Page 1 to Page 2 with out any error.
        """
        ia_runobj.select_active_document_page_layout_menu('Page 1')
        miscelaneousobj.verify_page_summary(0, '10of10records,Page1of1', "Step 08.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', Test_Case_ID + '_Ds01.xlsx', desired_no_of_rows=10)
        utillobj.verify_data_set('ITableData0', 'I0r', Test_Case_ID + '_Ds01.xlsx', " Step 08.2: Verify report at run time on page 1.", desired_no_of_rows=10)
         
        """
           Step 09:Select Latte. Verify that Page 1 report drill down report based on the drop down value.
        """
        ia_runobj.select_active_document_page_layout_menu('Page 1')
        
        utillobj.select_dropdown('#combobox_dsPROMPT_1', 'visible_text', 'Latte')
        miscelaneousobj.verify_page_summary(0, '1of10records,Page1of1', 'Step 09:01: Verify the Report Heading')
        column_list=['Category', 'Product', 'Unit Sales']
        miscelaneousobj.verify_column_heading('ITableData0', column_list, "Step 09:02: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID +'_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds02.xlsx', "Step 09:03: Verify entire Data set in Run Report on Page 1")        
        
        """
           Step 10:Go to page 2. Select "1102703" under the list box. Verify the results.
        """
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        
        ia_runobj.select_active_dashboard_prompts('listbox','#PROMPT_2_cs', ['1102703'])
        column_list=['Category', 'Product', 'UnitSales']
        miscelaneousobj.verify_column_heading('ITableData0', column_list, "Step 10:02: Verify the Run Report column heading")
#         utillobj.create_data_set('ITableData0','I0r',Test_Case_ID +'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID +'_Ds03.xlsx', "Step 10:03: Verify entire Data set in Run Report on Page 1")  
        
if __name__ == "__main__":
    unittest.main()          
