'''
Created on Jan 18, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10071
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5751535
TestCase_Name : Verify that reopening Document does not affect "Include ALL" option
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import document
from common.lib import utillity
from common.pages import wf_legacymainpage

class C5751535_TestClass(BaseTestCase):

    def test_C5751535(self):
        
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
        prompt_css="#Prompt_1"
        fex_name="AR-AD-09a"
        folder_name='P116->S10071_1'
        text_search="ARFILTER_SHOWALL='ON'"
        
        """
        Step 01: Execute the following URL:
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS10071_1%2F
        """
        report_obj.invoke_ia_tool_using_api_login(tool='document', master='ibisamp/ggsales', report_css='#resultArea', no_of_element=1, wait_time=MEDIUM_WAIT_TIME)
         
        """
        Step 02: Add Category, Product,Unit Sales to get a report
        """
        report_obj.double_click_on_datetree_item('Category', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'Category', MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item('Product', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'Product', MEDIUM_WAIT_TIME)
         
        report_obj.double_click_on_datetree_item('Unit Sales', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css, 'Unit Sales', MEDIUM_WAIT_TIME)
         
        report_obj.wait_for_number_of_element("#TableChart_1 div[class^='x']", 8, time_out=MEDIUM_WAIT_TIME) 
        
        coln_list=['Category', 'Product', 'Unit Sales']
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=coln_list, msg="Step 02: Verify column titles")
         
        """
        Step 03: Now, select Drop down button from 'Insert' tab
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Drop_Down')
        report_obj.wait_for_number_of_element(prompt_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component('#Prompt_1', '#TableChart_1', 70, 0)
         
        """    
        Step 04: Right click on Drop down button select properties    
        """
        doc_obj.choose_right_click_menu_item_for_prompt(prompt_css, item_name='Properties')
         
        """    
        Step 05. In Active Dashboard Properties assign UNIT SALES in 'Field'. Make sure Include All is checked already and Condition is Equal to. 
        Step 06. Click Ok.  
        """
        ComboBox_1_source = {'select_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_1_target = {'verify_target_name':['Report1']}
        doc_obj.customize_active_dashboard_properties(source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 05.", btn_type='ok') 
         
        """    
        Step 07. Save and close the report as AHTML as AR-AD-09a.fex.   
        """
        report_obj.save_report_from_toptoolbar()
        report_obj.save_file_in_save_dialog(fex_name)
        doc_obj.api_logout()
        
        """    
        Step 08. Now open the report again in IA (Edit), and right click on dropdown, and select properties.    
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        wf_legacymainpageobj.select_repository_folder_item_menu(folder_path=folder_name, item_name=fex_name, menu_item_path='Edit With...->InfoAssist+')
        doc_obj.switch_to_new_window()
        report_obj.wait_for_number_of_element("#TableChart_1 div[class^='x']", 8, time_out=MEDIUM_WAIT_TIME)
        coln_list=['Category', 'Product', 'Unit Sales']
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=coln_list, msg="Step 08: Verify column titles")
        report_obj.wait_for_number_of_element(prompt_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.choose_right_click_menu_item_for_prompt(prompt_css, item_name='Properties')
        
        """    
        Step 09. "Include All" should be checked on reopening the saved report
        """
        ComboBox_1_source = {'verify_field':'Unit Sales', 'verify_condition':'Equal to', 'verify_includeall':True}
        doc_obj.customize_active_dashboard_properties(source=ComboBox_1_source, msg="Step 09.", btn_type='ok') 
        doc_obj.switch_to_previous_window()
        doc_obj.api_logout()
        
        """    
        Step 10. Verify Include All gets generated in the syntax (ARFILTER_SHOWALL=ON)
        """
        utillobj.invoke_webfocu('mrid', 'mrpass')
        wf_legacymainpageobj.select_repository_folder_item_menu(folder_path=folder_name, item_name=fex_name, menu_item_path='Edit With...->Text Editor')
        text_editor_css="#bipEditorArea"
        report_obj.wait_for_number_of_element(text_editor_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        text_editor_css=utillobj.validate_and_get_webdriver_object(text_editor_css, 'Text area in Text Editor')
        text_value=text_editor_css.get_attribute('value').strip()
        utillobj.asin(text_search,text_value,"Step 10: Verify Include All gets generated in the syntax (ARFILTER_SHOWALL=ON)")

if __name__ == "__main__":
    unittest.main()