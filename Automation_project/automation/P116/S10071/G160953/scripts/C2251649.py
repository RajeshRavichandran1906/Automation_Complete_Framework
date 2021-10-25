'''
Created on 19-Jan-2018

@author: AAkhan

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251649
TestCase Name = Insert a Document report with filter controls
'''
import unittest, time
from common.lib import utillity
from common.pages import visualization_metadata, ia_resultarea, visualization_ribbon, active_miscelaneous, visualization_resultarea, ia_run
from common.lib.basetestcase import BaseTestCase
import keyboard

class C2251649_TestClass(BaseTestCase):

    def test_C2251649(self):
        """
        TESTCASE VARIABLES
        """
        test_case_id = 'C2251649'
        utillobj = utillity.UtillityMethods(self.driver)
        vis_metadata = visualization_metadata.Visualization_Metadata(self.driver)
        ia_resultobj = ia_resultarea.IA_Resultarea(self.driver)
        vis_ribbon = visualization_ribbon.Visualization_Ribbon(self.driver)
        active_mis_obj = active_miscelaneous.Active_Miscelaneous(self.driver)
        vis_resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ia_runobj = ia_run.IA_Run(self.driver)
        
        
        """ Step 1: Launch IA to develop a document.
                    Select 'GGSales' as master file, and change output format as Active report
                    Select Category, Product, Region, State and Unit Sales to get a report. Run the dashboard.
        """
        utillobj.infoassist_api_login('document', 'ibisamp/ggsales', 'S10071_2', 'mrid', 'mrpass')
        utillobj.synchronize_with_number_of_element("#canvasFrame", 1, 60)
        vis_ribbon.switch_ia_tab('Home')
        output_type = self.driver.find_element_by_css_selector("#HomeFormatType").text.strip()
        utillobj.asequal('Active Report', output_type, "Step 1: Verify output format as Active report.")
          
        vis_metadata.datatree_field_click('Category', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 2, 30)
          
        vis_metadata.datatree_field_click('Product', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 5, 30)
        
        vis_metadata.datatree_field_click('Region', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 13, 30)
        
          
        vis_metadata.datatree_field_click('State', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 33, 30)
          
        vis_metadata.datatree_field_click('Unit Sales', 2, 0)
        utillobj.synchronize_with_number_of_element("#TableChart_1 div[class^='x']", 53, 30)
        
#         ia_resultobj.create_across_report_data_set('TableChart_1', 2, 5, 0, 0, test_case_id + '_Ds01.xlsx')
        ia_resultobj.verify_across_report_data_set('TableChart_1', 2, 5, 0, 0, test_case_id + '_Ds01.xlsx', "Step 1.1: Verify Category, Product, Region, State, Unit Sales report generated in Live preview.")
          
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        path_css="[id^='ReportIframe']"
        utillobj.synchronize_with_number_of_element(path_css, 1, 60)
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'Category', 65)
        
        active_mis_obj.verify_page_summary(0, '107of107records,Page1of2', "Step 1.2: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds02.xlsx', " Step 1.3: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
        utillobj.switch_to_default_content(pause=1)
          
        """ Step 2: Now close the dashboard and on preview pane insert Drop down, List, Checkbox, Radio button and Text prompts.
        """
        vis_resultobj.select_panel_caption_btn(0, select_type='close', custom_css="[class*='active'] [class*='caption'][class*='window']")
         
        ''' Insert Drop down '''
        vis_ribbon.select_ribbon_item("Insert", "Drop_down")
        utillobj.synchronize_with_number_of_element("#Prompt_1", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_1', '#TableChart_1', 70, 0)
          
        ''' Insert List '''
        vis_ribbon.select_ribbon_item("Insert", "List")
        utillobj.synchronize_with_number_of_element("#Prompt_2", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_2', '#Prompt_1', 70, 0)
          
        ''' Insert Checkbox '''
        vis_ribbon.select_ribbon_item("Insert", "Checkbox")
        utillobj.synchronize_with_number_of_element("#Prompt_3", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_3', '#Prompt_2', 70, 0)
          
        ''' Insert Radio button '''
        vis_ribbon.select_ribbon_item("Insert", "Radio_Button")
        utillobj.synchronize_with_number_of_element("#Prompt_4", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_4', '#Prompt_2', 0, 70, target_drop_point='bottom_middle')
          
        ''' Insert Text '''
        vis_ribbon.select_ribbon_item("Insert", "Text")
        utillobj.synchronize_with_number_of_element("#Prompt_5", 1, 35)
        ia_resultobj.drag_drop_document_component('#Prompt_5', '#Prompt_4', 70, 0)
        
        """ Step 3: Right click drop down prompt, select Properties and verify Active Dashboard Properties opens up. Select Category field.
        """
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        ComboBox_1_source = {'select_field':'Category', 'verify_condition':'Equal to', 'verify_sort':'Ascending', 'verify_includeall':True}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 3.")
         
        """ Step 4: Click OK.
                    Verify drop down prompt shows default value as "All".
        """
        ia_resultobj.verify_active_dashboard_prompts('dropdown', '#Prompt_1', ['[All]'], "Step 4: Verify drop down prompt shows default value as 'All'.")
         
        """ Step 5: Right click List prompt, select Properties and verify Active Dashboard Properties opens up. Select Category field.
        """
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_2', 'Properties')
        ComboBox_1_source = {'select_field':'Category', 'verify_condition':'Equal to', 'verify_sort':'Ascending', 'verify_includeall':True}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 5.")
         
        """ Step 6: Click OK.
                    Verify List prompt shows these values as "All", "Coffee", "Food", "Gifts"
        """
        ia_resultobj.verify_active_dashboard_prompts('listbox', '#Prompt_2', ['[All]', 'Coffee', 'Food', 'Gifts'], 'Step 6: Verify drop down prompt shows default value as "All", "Coffee", "Food", "Gifts".')
         
        """ Step 7: Right click Checkbox prompt, select Properties and verify Active Dashboard Properties opens up. Select Region field.
        """
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_3', 'Properties')
        ComboBox_1_source = {'select_field':'Region', 'verify_condition':'Equal to', 'verify_sort':'Ascending', 'verify_includeall':True}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 7.")
         
        """ Step 8: Click OK.
                    Verify Checkbox prompt shows these values as "All", "Midwest", "Northwest", "Southwest", ""West".
        """
        checkbox_list = ['[All]', 'Midwest', 'Northeast', 'Southeast', 'West']
        ia_resultobj.verify_active_dashboard_prompts('checkbox', '#Prompt_3', checkbox_list, 'Step 8: Verify drop down prompt shows default value as "All", "Midwest", "Northwest", "Southwest", ""West".')
         
        """ Step 9: Right click Radio buttons prompt, select Properties and verify Active Dashboard Properties opens up. Select State field.
        """
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_4', 'Properties')
        ComboBox_1_source = {'select_field':'State', 'verify_condition':'Equal to', 'verify_sort':'Ascending', 'verify_includeall':True}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 9.")
         
        """ Step 10: Click OK.
                     Verify Radio button prompt shows State names with ALL as default.
        """ 
        radiobutton_list = ['[All]', 'CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA']
        ia_resultobj.verify_active_dashboard_prompts('radiobutton', '#Prompt_4', radiobutton_list, "Step 10: Verify drop down prompt shows default value as 'All'.")
         
        """ Step 11: Right click Text prompt, select Properties and verify Active Dashboard Properties opens up. Select Unit Sales field.
        """
        vis_resultobj.choose_right_click_menu_item_for_prompt('#Prompt_5', 'Properties')
        
        ComboBox_1_source = {'select_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_sort':'Ascending', 'verify_includeall':True}
        vis_resultobj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 11.")
         
        """ Step 12: Click OK.
                     Text input box will have textbox
        """
        ia_resultobj.verify_active_dashboard_prompts('text', '#Prompt_5', [''], "Step 12: Verify drop down prompt shows default value as 'All'.")
        
        """ Step 13: Click Run.
        """
        vis_ribbon.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']",1,120)
        utillobj.switch_to_frame(pause=3)
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'Category', 65)
        active_mis_obj.verify_page_summary(0, '107of107records,Page1of2', "Step 13: Verify page summary of Category, Product, Region, State, Unit Sales report.")

#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds03.xlsx', " Step 13.1: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
         
        """ Step 14: Select Coffee from the drop down prompt
                     Verify the output. It should show 30 records of Coffee.
        """
        utillobj.select_dropdown("#combobox_dsPROMPT_1", 'value', 'Coffee')
        utillobj.verify_dropdown_value("#combobox_dsPROMPT_1", expected_default_selected_value='Coffee', default_selection_msg='Step 14: Verify Coffee selected now in drop down.')
         
        ''' Verify report output '''
        
        utillobj.synchronize_with_visble_text("#ITableData0 #TCOL_0_C_0", 'Category', 65)
        active_mis_obj.verify_page_summary(0, '30of107records,Page1of1', "Step 14.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds04.xlsx', " Step 14.2: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
         
        """ Step 15: Select Food from the List prompt
                     Verify the output. It should show 33 records of Food.
        """
        ia_runobj.select_active_dashboard_prompts('listbox', '#PROMPT_2_cs', ['Food'])
        ia_runobj.verify_active_dashboard_prompts('listbox', '#PROMPT_2_cs', ['[All]', 'Coffee', 'Food', 'Gifts'], "Step 15: Verify Food selected in list box.")
         
        ''' Verify report output '''
        active_mis_obj.verify_page_summary(0, '33of107records,Page1of1', "Step 15.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds05.xlsx', " Step 15.2: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
         
        """ Step 16: Select Northeast from the checkbox prompt
                     Verify the output. It should show 30 records for Northeast.
        """
        ia_runobj.select_active_dashboard_prompts('checkbox', '#PROMPT_3_cs', ['Northeast'])
        ia_runobj.verify_active_dashboard_prompts('checkbox', '#PROMPT_3_cs', ['[All]', 'Midwest', 'Northeast', 'Southeast', 'West'], "Step 16: Verify Northeast selected in checkbox box.")
         
        ''' Verify report output '''
        active_mis_obj.verify_page_summary(0, '30of107records,Page1of1', "Step 16.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds06.xlsx', " Step 16.2: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
         
        """ Step 17: Select CT from the radio button prompt
                     Verify the output. It should show 10 records for CT.
        """
        ia_runobj.select_active_dashboard_prompts('radio button', '#PROMPT_4_cs', ['CT'])
        ia_runobj.verify_active_dashboard_prompts('radio button', '#PROMPT_4_cs', ['[All]', 'CA', 'CT', 'FL', 'GA', 'IL', 'MA', 'MO', 'NY', 'TN', 'TX', 'WA'], "Step 17: Verify Northeast selected in radio button.")
         
        ''' Verify report output '''
        active_mis_obj.verify_page_summary(0, '10of107records,Page1of1', "Step 17.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds07.xlsx', " Step 17.2: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
         
        """ Step 18: Enter "12386" and hit enter in the text box
                     Verify the output is only for that record.
        """
#         ia_runobj.select_active_dashboard_prompts('text', "#PROMPT_5_cs", ['12386'])
        
        element=self.driver.find_element_by_css_selector('#PROMPT_5_cs input')
        exec("element.clear()")
        exec("element.send_keys('12386')")
        keyboard.send('enter')
        time.sleep(5) 
        ia_runobj.verify_active_dashboard_prompts('text', '#PROMPT_5_cs', ['12386'], "Step 18: Verify Northeast selected in radio button.")
         
        ''' Verify report output '''
        active_mis_obj.verify_page_summary(0, '1of107records,Page1of1', "Step 18.1: Verify page summary of Category, Product, Region, State, Unit Sales report.")
#         utillobj.create_data_set('ITableData0', 'I0r', test_case_id + '_Ds08.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', test_case_id + '_Ds08.xlsx', " Step 18.2: Verify Category, Product, Region, State, Unit Sales report generated at run time.")
         
        utillobj.switch_to_default_content(pause=1)
        vis_ribbon.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(test_case_id)
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()