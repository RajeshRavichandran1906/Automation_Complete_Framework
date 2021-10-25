'''
Created on Jan 22, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5751536
TestCase_Name : Verify that same syntax available in report and text editor
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import document
from common.lib import utillity
from common.pages import wf_legacymainpage

class C5751536_TestClass(BaseTestCase):

    def test_C5751536(self):
        
        """
        TESTCASE VARIABLES
        """
        utillobj = utillity.UtillityMethods(self.driver)
        report_obj = report.Report(self.driver)
        doc_obj=document.Document(self.driver)
        wf_legacymainpageobj = wf_legacymainpage.Wf_Legacymainpage(self.driver)
        
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        report_parent_css="TableChart_1"
        dropdown_css="#Prompt_1"
        list_css="#Prompt_2"
        checkbox_css="#Prompt_3"
        text_editor_css="#bipEditorArea"
        fex_name="DB-with-prompts"
        folder_name='P116->S10071_2'
        combobox_text_search="OBJECT=combobox, NAME=Prompt_1, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='CATEGORY', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='OFF', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING'"
        list_text_search="OBJECT=list, NAME=Prompt_2, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='PCD', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='ON', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING'"
        checkbox_text_search="OBJECT=checkbox, NAME=Prompt_3, ARDATA_REPORT='TableChart_1', ARDATA_COLUMN='PRODUCT', ARFILTER_TARGET='TableChart_1,', ARFILTER_CONDITION='EQ', ARFILTER_MULTIPLE='ON', ARFILTER_SHOWALL='ON', ARFILTER_VALUEASIS='OFF', ARFILTER_SORT='ASCENDING'"
        
        """
        Step 01: Execute following URL to launch document
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS10071_1%2F
        """
        report_obj.invoke_ia_tool_using_api_login(tool='document', master='ibisamp/ggsales', report_css='#resultArea', no_of_element=1, wait_time=MEDIUM_WAIT_TIME)
         
        """
        Step 02: Add following fields:
        Category, Product ID, Product, State, Unit Sales and Dollar Sales to get a report
        """
        report_obj.double_click_on_datetree_item('Category', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'Category', MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item('Product ID', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'Product ID', MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item('Product', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'Product', MEDIUM_WAIT_TIME)
        
        report_obj.double_click_on_datetree_item('State', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'State', MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item('Unit Sales', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'Unit Sales', MEDIUM_WAIT_TIME)
        
        report_obj.double_click_on_datetree_item('Dollar Sales', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'Dollar Sales', MEDIUM_WAIT_TIME)
         
        report_obj.wait_for_number_of_element("#TableChart_1 div[class^='x']", 68, time_out=MEDIUM_WAIT_TIME) 
        
        coln_list=['Category', 'Product ID', 'Product', 'State', 'Unit Sales', 'Dollar Sales']
        report_obj.verify_column_title_on_preview(colnum=6, no_of_cells=6, table_id=report_parent_css, expected_list=coln_list, msg="Step 02: Verify column titles")
        
        """
        Step 03: Now, select Drop down prompt from 'Insert' tab and drag to the right of report.
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Drop_Down')
        report_obj.wait_for_number_of_element(dropdown_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(dropdown_css, '#'+report_parent_css, x=70, y=0)
        
        """
        Step 04: Now, select List prompt from 'Insert' tab and drag to the right of drop down prompt.
        """
        doc_obj.select_ia_ribbon_item('Insert', 'List')
        report_obj.wait_for_number_of_element(list_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(list_css, dropdown_css, x=70, y=0)
        time.sleep(3)
        
        """
        Step 05: Now, select Check box prompt from 'Insert' tab and drag to the right of List prompt.
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Checkbox')
        report_obj.wait_for_number_of_element(checkbox_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(checkbox_css, list_css, x=70, y=0)
        time.sleep(3)
        
        """    
        Step 06: Right click on Dropdown prompt and assign a field as follows:
        Click ComboBox_1 --> from Field select Category
        Click List_2 --> from Field select Product ID
        Click CheckBox_3 --> from Field select Product
        Make sure Condition = Equal to and Include All is checked.
        Step 07: Select Ok.
        """
        doc_obj.choose_right_click_menu_item_for_prompt(dropdown_css, item_name='Properties')
        prompt1 = {'select_prompts':'combobox_1'}
        ComboBox_1_source = {'select_field':'Category', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_1_target = {'verify_target_name':['Report1']}
        doc_obj.customize_active_dashboard_properties(prompts=prompt1, source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 06.1", btn_type='Apply') 
        prompt2 = {'select_prompts':'list_2'}
        ComboBox_2_source = {'select_field':'Product ID', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_2_target = {'verify_target_name':['Report1']}
        doc_obj.customize_active_dashboard_properties(prompts=prompt2, source=ComboBox_2_source, targets=ComboBox_2_target, msg="Step 06.2", btn_type='Apply')
        prompt3 = {'select_prompts':'checkbox_3'}
        ComboBox_3_source = {'select_field':'Product', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_3_target = {'verify_target_name':['Report1']}
        doc_obj.customize_active_dashboard_properties(prompts=prompt3, source=ComboBox_3_source, targets=ComboBox_3_target, msg="Step 06.3", btn_type='ok')
        
        """    
        Step 08. Save Document as DB with prompts.fex   
        """
        report_obj.save_report_from_toptoolbar()
        report_obj.save_file_in_save_dialog(fex_name)
        report_obj.api_logout()
        
        """    
        Step 09. Edit fex with Text Editor to check the code
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        wf_legacymainpageobj.select_repository_folder_item_menu(folder_path=folder_name, item_name=fex_name, menu_item_path='Edit With...->Text Editor')
        
        """    
        Step 09.1: Check code in Text editor.
        """
        report_obj.wait_for_number_of_element(text_editor_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        text_editor_css=utillobj.validate_and_get_webdriver_object(text_editor_css, 'Text area in Text Editor')
        text_value=text_editor_css.get_attribute('value').strip()
        utillobj.asin(combobox_text_search,text_value,"Step 09.1: Check code in Text editor for combobox")
        utillobj.asin(list_text_search,text_value,"Step 09.2: Check code in Text editor for list")
        utillobj.asin(checkbox_text_search,text_value,"Step 09.3: Check code in Text editor for checkbox")
        doc_obj.api_logout()
        
        """    
        Step 10. Edit Document in IA and click View source.    
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        wf_legacymainpageobj.select_repository_folder_item_menu(folder_path=folder_name, item_name=fex_name, menu_item_path='Edit With...->InfoAssist+')
        doc_obj.switch_to_new_window()
        report_obj.wait_for_number_of_element("#TableChart_1 div[class^='x']", 68, time_out=MEDIUM_WAIT_TIME)
        
        """    
        Step 10.1: Verify Same syntax should be in Text editor.
        """
        expected_syntax_list=["OBJECT=combobox", "NAME=Prompt_1", "ARDATA_REPORT='TableChart_1'", "ARDATA_COLUMN='CATEGORY'", "ARFILTER_TARGET='TableChart_1,'", "ARFILTER_CONDITION='EQ'", "ARFILTER_MULTIPLE='OFF'", "ARFILTER_SHOWALL='ON'", "ARFILTER_VALUEASIS='OFF'", "ARFILTER_SORT='ASCENDING'",
        "OBJECT=list", "NAME=Prompt_2", "ARDATA_REPORT='TableChart_1'", "ARDATA_COLUMN='PCD'", "ARFILTER_TARGET='TableChart_1,'", "ARFILTER_CONDITION='EQ'", "ARFILTER_MULTIPLE='ON'", "ARFILTER_SHOWALL='ON'", "ARFILTER_VALUEASIS='OFF'", "ARFILTER_SORT='ASCENDING'",
        "OBJECT=checkbox", "NAME=Prompt_3", "ARDATA_REPORT='TableChart_1'", "ARDATA_COLUMN='PRODUCT'", "ARFILTER_TARGET='TableChart_1,'", "ARFILTER_CONDITION='EQ'", "ARFILTER_MULTIPLE='ON'", "ARFILTER_SHOWALL='ON'", "ARFILTER_VALUEASIS='OFF'", "ARFILTER_SORT='ASCENDING'"]
        report_obj.verify_fexcode_syntax(expected_syntax_list, msg="Step 10.1: Verify Same syntax should be in Text editor.")
        
if __name__ == "__main__":
    unittest.main()