'''
Created on May 24, 2018

@author: BM13368
Test_Case ID : http://172.19.2.180/testrail/index.php?/cases/view/2510986&group_by=cases:section_id&group_id=175061&group_order=asc
Test_Name : Create a Document with multiple pages and Global Filtering.
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, visualization_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase


class C2510986_TestClass(BaseTestCase):

    def test_C2510986(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2510986'
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        """
        Step 01: Create a new Document using the GGSALES file.
        From the Insert icon, add a Text Box to the canvas.
        Change the text content to "Create a Report Multi-page Dashboard Page one"
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10851_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_visble_text("#iaCanvasCaptionLabel", 'Document', 65)
        vis_ribbon.select_ribbon_item('Insert', 'text_box')
        utillobj.synchronize_with_number_of_element("#theCanvas #Text_1", 1, 15)
          
        vis_ribbon.resizing_document_component('0.25', '4.60')
        ia_resultobj.enter_text_in_Textbox('Text_1', "Create a Report Multi-page Dashboard Page one")
        
        """    
        Step 02 :Select Category, Product,Unit Sales to get a report
        Expect to see the following report with text box
        """
        vis_ribbon.select_ribbon_item('Insert', 'report')
        time.sleep(5)
        ia_resultobj.drag_drop_document_component('#Text_1', '#TableChart_1', 0, 15, target_drop_point='bottom_middle')
        vis_metadata.datatree_field_click('Category', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, expire_time=10)
          
        vis_metadata.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, expire_time=10)
        
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 8, expire_time=10)
          
        coln_list = ['Category', 'Product','Unit Sales']
        vis_resultobj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 02:01: Verify Category, Product, Unit Sales report.")
        
#         ia_resultobj.create_report_data_set('TableChart_1 ', 2, 3, Test_Case_ID+'_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1', 2, 3, Test_Case_ID+'_Ds01.xlsx', 'Step 02:02 Verify Preview report dataset')      
    
        """
            Step 03:Select Dropdown box from 'Insert' tab,right click on dropdown box and assign "Products" in property of dropdown box
            Expect to see the following report with dropdown filter control and text box
        """ 
        vis_ribbon.select_ribbon_item('Insert', 'drop_down')
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 20)
        ia_resultobj.drag_drop_document_component('#Prompt_1', '#Text_1', 0, 45, target_drop_point='top_right')
        vis_resultobj.choose_right_click_menu_item_for_prompt("#Prompt_1", "Properties")
        source_dict={'select_field':'Product'}
        vis_resultobj.customize_active_dashboard_properties(source=source_dict,btn_type='ok')   
        
        """ 
            Step 04:To add another page select Insert tab, in the Pages group Page 2, is inserted after the current page, and appears on the canvas
            Expected to see the following canvas of page2 which is displayed in right top corner
        """
        ia_resultobj.select_or_verify_document_page_menu("New Page")
        time.sleep(5)
        page_elem=self.driver.find_element_by_css_selector("#iaPagesMenuBtn").text
        utillobj.asequal('Page 2', page_elem, "Step 04:01: Verify page2 is added in the canvas")
        
        """ 
            Step 05:Add text box from insert menu change the text content to "Create a Report Multi-page Dashboard Page Two"
        """
        vis_ribbon.select_ribbon_item('Insert', 'text_box')
        utillobj.synchronize_with_number_of_element("#theCanvas #Text_2", 1, 15)
        vis_ribbon.resizing_document_component('0.25', '5.60')
        ia_resultobj.enter_text_in_Textbox('Text_2', "Create a Report Multi-page Dashboard Page Two")
        
        """
            Step 06:Create a new report and select Product ID,Region,Dollar Sales
        """
        
        vis_ribbon.select_ribbon_item('Insert', 'report')
        time.sleep(5)
        ia_resultobj.drag_drop_document_component('#Text_2', '#TableChart_2', 20, 15, target_drop_point='bottom_middle')
        time.sleep(3)
        vis_metadata.datatree_field_click('Product ID', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 3, expire_time=10)
          
        vis_metadata.datatree_field_click('Region', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 11, expire_time=10)
        
        vis_metadata.datatree_field_click('Dollar Sales', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_2 div[class^='x']", 19, expire_time=10)
        
        """
            Step 07:Select List box from 'Insert' tab,right click on List box and 
            assign Dollar Sales field of report 2.
            Verify that Reports with Mulit-Page Dashboard output should have the following options Layout tab,Page1 and Page2 option and able to navigate the output from Page 1 to Page 2 with out any error
        """
        vis_ribbon.select_ribbon_item('Insert', 'list')
        time.sleep(5)
        ia_resultobj.drag_drop_document_component('#Prompt_2', '#Text_2', 0, 45, target_drop_point='top_right')
        
        vis_resultobj.choose_right_click_menu_item_for_prompt("#Prompt_2", "Properties")
        source_dict={'select_report':'Report2','select_field':'Dollar Sales'}
        vis_resultobj.customize_active_dashboard_properties(source=source_dict, btn_type='ok')
        ia_resultobj.verify_active_dashboard_prompts('listbox', "#Prompt_2", ['[All]','748','799','813','824','879','884','893'], "step 5: verify prompts")
        
        """ 
            Step 08:Execute the report.
            Verify that Page 1 report drop down report based on the drop down value and Page 2 report list box report based on the selected values.
            Page 1
            Page 2
            Step 09 :Save as AR_AD_01a and Close.
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 45)
        utillobj.switch_to_frame(pause=2)
        
        """
        Verify page 1 report 
        """
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value='[All]', default_selection_msg="Step 09:01:Verify the default selection value")
        utillobj.verify_data_set('ITableData0','I0r',Test_Case_ID+'_Ds02.xlsx', 'Step 09:02: Verify that report for between filter')
        
        """
        Verify page 2
        """
        ia_runobj.select_active_document_page_layout_menu('Page 2')
        utillobj.synchronize_with_visble_text("#ITableData1 tr:nth-child(2) td:nth-child(2)", "Midwest", 20)
        ia_runobj.verify_active_dashboard_prompts('listbox', "#PROMPT_2_cs", ['509200','542095','571368'], "Step 09:04:Verify list of values")
#         utillobj.create_data_set('ITableData1','I1r',Test_Case_ID+'_Ds03.xlsx')
        utillobj.verify_data_set('ITableData1','I1r',Test_Case_ID+'_Ds03.xlsx', 'Step 09:03: Verify that report for between filter')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()