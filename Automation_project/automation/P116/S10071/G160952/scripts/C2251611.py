'''
Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10032
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2251611
'''
import unittest
import time, keyboard
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_metadata, visualization_resultarea, visualization_ribbon, ia_resultarea, active_miscelaneous, ia_run
from common.lib import utillity

class C2251611_TestClass(BaseTestCase):

    def test_C2251611(self):
        """ TESTCASE VARIABLES """
        Test_Case_ID = 'C2251611'
        utillobj = utillity.UtillityMethods(self.driver)
        metaobj = visualization_metadata.Visualization_Metadata(self.driver)
        resultobj = visualization_resultarea.Visualization_Resultarea(self.driver)
        ribbonobj = visualization_ribbon.Visualization_Ribbon(self.driver)
        ia_resultobj=ia_resultarea.IA_Resultarea(self.driver)
        ia_runobj=ia_run.IA_Run(self.driver)
        miscobj=active_miscelaneous.Active_Miscelaneous(self.driver)
        oPrompt_right_click_menu_items=['Copy', 'Cut', 'Duplicate', 'Properties', 'Rename', 'Size and Position...', 'Delete']
        oDropdown=['[All]']
        oList=['[All]', 'C141', 'C142', 'C144', 'F101', 'F102', 'F103', 'G100', 'G104', 'G110', 'G121']
        oCheckbox=['[All]', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        oRadio_button=['[All]', 'Midwest', 'Northeast', 'Southeast', 'West']
        oPrompts=['combobox_1', 'list_2', 'checkbox_3', 'radiobutton_4', 'textinput_5']
        
        """    1. Launch IA to develop a new Document.
        Select 'GGSales' as master file, and change output format as Active report
        Select Category,Product ID, Product, Region, Unit Sales and Dollar Sales to get a report    """
        utillobj.infoassist_api_login('document','ibisamp/ggsales','P116/S10071', 'mrid', 'mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=65, string_value='Document')
        metaobj.datatree_field_click("Category", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 2, expire_time=35)    
        metaobj.datatree_field_click("Product ID", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 5, expire_time=35)
        metaobj.datatree_field_click("Product", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 8, expire_time=35)
        metaobj.datatree_field_click("Region", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 16, expire_time=35)
        metaobj.datatree_field_click("Unit Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 24, expire_time=35)  
        metaobj.datatree_field_click("Dollar Sales", 2, 1)
        resultobj.wait_for_property("#TableChart_1 div[class^='x']", 32, expire_time=35)
        ribbonobj.repositioning_document_component('0.5', '0.75')
        coln_list = ['Category', 'Product ID', 'Product', 'Region', 'Unit Sales', 'Dollar Sales']
        resultobj.verify_report_titles_on_preview(6, 6, "TableChart_1 ", coln_list, "Step 01a: Verify column titles")
        
        
        """    2. Now, select Drop down, List box, Check box, Radio button, and Text prompt from 'Insert' tab    """
        ribbonobj.select_ribbon_item("Insert", "Drop_down")
        ribbonobj.repositioning_document_component('7', '1')
        ribbonobj.select_ribbon_item("Insert", "List")
        ribbonobj.repositioning_document_component('7', '2.2')
        ribbonobj.select_ribbon_item("Insert", "Checkbox")
        ribbonobj.repositioning_document_component('9', '1')
        ribbonobj.resizing_document_component('2.5', '1.5')
        ribbonobj.select_ribbon_item("Insert", "Radio_button")
        ribbonobj.repositioning_document_component('9', '4')
        ribbonobj.resizing_document_component('1.5', '1.5')
        ribbonobj.select_ribbon_item("Insert", "Text")
        ribbonobj.repositioning_document_component('7', '4')
    
        """    3. Right click on Dropdown prompt and click Properties.
        Assign a field as Category.
        Make sure Condition is set as Equal to and Include All is checked.    """
        """    4. Click Ok.    """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties', verify='true',expected_popup_list=oPrompt_right_click_menu_items,msg='Step 03(1):')
        source_dict={'select_field':'Category', 'verify_condition':'Equal to', 'includeall':'no'}
        resultobj.customize_active_dashboard_properties(source=source_dict, msg='Step 03(ii)')
        
        """    5. Right click on List box prompt and click Properties.
        Assign a field as Product ID.
        Make sure Condition is set as Equal to and Include All is checked.    """
        """    6. Click Ok.    """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_2', 'Properties', verify='true',expected_popup_list=oPrompt_right_click_menu_items,msg='Step 05(i):')
        source_dict={'select_field':'Product ID', 'verify_condition':'Equal to', 'includeall':'no'}
        resultobj.customize_active_dashboard_properties(source=source_dict, msg='Step 05(ii)')
        
        """    7. Right click on Check box prompt and click Properties.
        Assign a field as Product.
        Make sure Condition is set as Equal to and Include All is checked.    """
        """    8. Click Ok.    """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_3', 'Properties', verify='true',expected_popup_list=oPrompt_right_click_menu_items,msg='Step 07(i):')
        source_dict={'select_field':'Product', 'verify_condition':'Equal to', 'includeall':'no'}
        resultobj.customize_active_dashboard_properties(source=source_dict, msg='Step 07(ii)')
        
        """    9. Right click on Radio button prompt and click Properties.
        Assign a field as Region.
        Make sure Condition is set as Equal to and Include All is checked.    """
        """    10. Click Ok.    """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_4', 'Properties', verify='true',expected_popup_list=oPrompt_right_click_menu_items,msg='Step 09(i):')
        source_dict={'select_field':'Region', 'verify_condition':'Equal to', 'includeall':'no'}
        resultobj.customize_active_dashboard_properties(source=source_dict, msg='Step 09(ii)')
        
        """    11. Right click on Text box prompt and click Properties.
        Assign a field as Unit Sales.
        Make sure Condition is set as Equal to and Include All is checked.    """
        """    12. Click Ok.    """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_5', 'Properties', verify='true',expected_popup_list=oPrompt_right_click_menu_items,msg='Step 11(i):')
        source_dict={'select_field':'Unit Sales', 'verify_condition':'Equal to', 'includeall':'no'}
        resultobj.customize_active_dashboard_properties(source=source_dict, msg='Step 11(ii)')
        coln_list = ['Category', 'Product ID', 'Product', 'Region', 'Unit Sales', 'Dollar Sales']
        resultobj.verify_report_titles_on_preview(6, 6, "TableChart_1 ", coln_list, "Step 11a: Verify column titles")
        #ia_resultobj.create_report_data_set('TableChart_1 ', 7, 6, 'C2251611_Ds01.xlsx')
        ia_resultobj.verify_report_data_set('TableChart_1 ', 7, 6, 'C2251611_Ds01.xlsx', 'Step 11b: Verify Preview report dataset')
        ia_resultobj.verify_active_dashboard_prompts('dropdown',"#Prompt_1", oDropdown, "step 11c: verify prompt 1 - dropdown")
        ia_resultobj.verify_active_dashboard_prompts('listbox',"#Prompt_2", oList, "step 11d: verify prompt 2 - listbox")
        ia_resultobj.verify_active_dashboard_prompts('checkbox',"#Prompt_3", oCheckbox, "step 11e: verify prompt 3 - checkbox")
        ia_resultobj.verify_active_dashboard_prompts('radiobutton',"#Prompt_4", oRadio_button, "step 11f: verify prompt 4 - radiobutton")
        
        
        """    13. Run the Document.    """
        ribbonobj.select_top_toolbar_item('toolbar_run')
        utillobj.synchronize_with_number_of_element("[id^='ReportIframe']", 1, 60) 
        utillobj.switch_to_frame()
        miscobj.verify_page_summary(0, '39of39records,Page1of1', 'Step 13a(1): Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Product', 'Region', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 13b(1): Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251611_Ds02.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251611_Ds02.xlsx', 'Step 13c(1): Verify data.')
        
        """    14. Filter Drop down with value = Food. Verify 12 of 39 records are returned.    """
        utillobj.select_dropdown('#combobox_dsPROMPT_1', 'value', 'Food')
        time.sleep(5)
        miscobj.verify_page_summary(0, '12of39records,Page1of1', 'Step 14a(1): Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Product', 'Region', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 14b(1): Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251611_Ds03.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251611_Ds03.xlsx', 'Step 14c(1): Verify data.')
        
        """    15. Select C144 under List box. Verify 3 of 39 records are returned.    """
        ia_runobj.select_active_dashboard_prompts('listbox','#PROMPT_2_cs', ['C144'])
        time.sleep(5)
        miscobj.verify_page_summary(0, '3of39records,Page1of1', 'Step 15a(1): Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Product', 'Region', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 15(1): Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251611_Ds04.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251611_Ds04.xlsx', 'Step 15c(1): Verify data.')
        
        """    16. Select Coffee Pot from Checkbox prompt. Verify 4 of 39 records are returned.    """
        ia_runobj.select_active_dashboard_prompts('checkbox', "#PROMPT_3_cs",["Coffee Pot"])
        time.sleep(5)
        miscobj.verify_page_summary(0, '4of39records,Page1of1', 'Step 16a(1): Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Product', 'Region', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 16b(1): Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251611_Ds05.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251611_Ds05.xlsx', 'Step 16c(1): Verify data.')
        
        """    17. Select Northeast from Radio button prompt. Verify 10 of 39 records are returned.    """
        ia_runobj.select_active_dashboard_prompts('radiobutton','#PROMPT_4_cs', ['Northeast'])
        time.sleep(5)
        miscobj.verify_page_summary(0, '10of39records,Page1of1', 'Step 17a(1): Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Product', 'Region', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 17(1): Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251611_Ds06.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251611_Ds06.xlsx', 'Step 17c(1): Verify data.')
        
        """    18. Enter 101154 value under Text prompt and hit enter key. Verify 1 0f 39 record is returned.    """
        textbox_obj=self.driver.find_element_by_css_selector('#PROMPT_5_cs input')
        utillobj.click_on_screen(textbox_obj, coordinate_type='middle', click_type=0)
#         keyboard.send('home')
        keyboard.press('ctrl')
        keyboard.press('home')
        time.sleep(1)
        keyboard.release('ctrl')
        keyboard.release('home')
        time.sleep(1)
        keyboard.write('101154', delay=1)
        time.sleep(1)
        keyboard.send('enter')
        time.sleep(5)
        miscobj.verify_page_summary(0, '1of39records,Page1of1', 'Step 18a(1): Verify the Report Heading')
        coln_list = ['Category', 'Product ID', 'Product', 'Region', 'Unit Sales', 'Dollar Sales']
        miscobj.verify_column_heading('ITableData0', coln_list, 'Step 18b(1): Verify the column heading')
        #utillobj.create_data_set('ITableData0', 'I0r', 'C2251611_Ds07.xlsx')
        utillobj.verify_data_set('ITableData0', 'I0r', 'C2251611_Ds07.xlsx', 'Step 18c(1): Verify data.')
        utillobj.switch_to_default_content()
        
        """    19. Save the dashboard as "Multiple prompts.fex"    """
        ribbonobj.select_tool_menu_item('menu_save')
        utillobj.ibfs_save_as(Test_Case_ID)
        utillobj.infoassist_api_logout()
        time.sleep(5)
        
        """    20. Reopen Dashboard via IA    """
        oFolder=utillobj.parseinitfile('suite_id')
        utillobj.infoassist_api_edit(Test_Case_ID, 'document', oFolder, mrid='mrid', mrpass='mrpass')
        resultobj.wait_for_property("#iaCanvasCaptionLabel", 1, expire_time=65, string_value='Document')
        
        """    21. Re-open any prompt. e.g.: Dropdown and check assigned field value    """
        resultobj.choose_right_click_menu_item_for_prompt('#Prompt_1', 'Properties')
        prompt_dict={'verify_prompts':oPrompts}
        source_dict={'select_field':'Category', 'verify_field':'Category', 'verify_condition':'Equal to', 'includeall':'no'}
        target_dict={'verify_target_name':['Report1']}
        resultobj.customize_active_dashboard_properties(prompts=prompt_dict, source=source_dict, targets=target_dict, msg='Step 21', btn_type='cancel')

        
        """    Logout: http://machine:port/ibi_apps/service/wf_security_logout.jsp    """
        
        
if __name__ == '__main__':
    unittest.main()