'''
Created on Jan 28, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7080
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231437
TestCase_Name : ADP:Duplicate Report1 displayed after switching from Cascade 149322
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import document
from common.lib import utillity

class C2231437_TestClass(BaseTestCase):

    def test_C2231437(self):
        
        """
        TESTCASE VARIABLES
        """
        Testcase_ID="C2231437"
        utillobj = utillity.UtillityMethods(self.driver)
        report_obj = report.Report(self.driver)
        doc_obj = document.Document(self.driver)
            
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        username='mriddev'
        password='mrpassdev'
        dropdown_prompt='dropdown'
        list_prompt='listbox'
        dropdown_values=['Option 1']
        listbox_values=['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
        cascades = {'verify_cascades':['Cascade1']}
        prompt1 = {'verify_prompts':['combobox_1','list_2']}
        field_list=['COUNTRY', 'DEALER_COST']
        
        """
        COMMON CSS
        """
        report_parent_css="TableChart_1"
        dropdown_css="#Prompt_1"
        list_css="#Prompt_2"
        report_data_css="#TableChart_1 div[class^='x']"
        dropdown_btn_css="div[id*='comboSourceReports'] div[id^='BiButton']"
        source_target_css="#btnTargetsOpt img"
        
        """
        Step 01: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95/S10142
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='Document', master='ibisamp/car', mrid=username, mrpass=password)
          
        """
        Step 02: Change format to Active Report and Add fields COUNTRY(BY) and DEALER_COST(SUM)
        """
        report_obj.change_output_format_type('active_report')
        for field in field_list:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text('#'+report_parent_css, field, MEDIUM_WAIT_TIME)
         
        """
        Step 02.1: Expect to see the following Preview pane for the report component.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=12, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css, expected_list=field_list, msg="Step 02.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 5, 2, Testcase_ID+'_DS01.xlsx', msg="Step 02.2: Verify report dataset") 
        
        """
        Step 03: Insert "Drop Down" and "List" Active Dashboard Prompts(ADP) and place them next to the report on the canvas.
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Drop_Down')
        report_obj.wait_for_number_of_element(dropdown_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(dropdown_css, '#'+report_parent_css, x=70, y=0)
        doc_obj.select_ia_ribbon_item('Insert', 'List')
        report_obj.wait_for_number_of_element(list_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(list_css, dropdown_css, x=70, y=0)
        time.sleep(3)
        
        """
        Step 03.1: Expect to see the following Prompts added to the Preview pane.
        """
        doc_obj.verify_prompts_in_preview(component=dropdown_prompt, parent_css=dropdown_css, verify_list=dropdown_values, msg="step 03.3: verify dropdown prompt")
        doc_obj.verify_prompts_in_preview(component=list_prompt, parent_css=list_css, verify_list=listbox_values, msg="step 03.4: verify Listbox prompt")
         
        """    
        Step 04: Right-click on the Drop Down box object and select Properties.
        Click on the arrow at Report and verify that there is ONLY ONE option, "Report1"
        Step 04.1: Expect to see only one candidate report - Report1 available for selection, from the Report area.
        """
        doc_obj.choose_right_click_menu_item_for_prompt(dropdown_css, item_name='Properties')
        dropdown_btn_obj=utillobj.validate_and_get_webdriver_object(dropdown_btn_css, 'SourceReports combobox Dropdown button')
        utillobj.select_any_combobox_item(dropdown_btn_obj, combo_item='Report1', verify=True, expected_combobox_list=['Report1'], msg='Step 04.1: Expect to see only one candidate report - Report1 available for selection, from the Report area.')
        
        """    
        Step 05: Click on "Cascades" tab at the top of the Properties menu.
        Click on "Prompt Source & Targets" tab at the top of the Properties menu.
        Step 05.1: Expect to see the following Propertied menu
        """
        doc_obj.add_and_verify_prompts_in_cascade(cascades=cascades, msg='Step 05.1:')
        source_target_tab=utillobj.validate_and_get_webdriver_object(source_target_css, 'source_target_tab button')
        utillobj.default_click(source_target_tab)
        doc_obj.customize_active_dashboard_properties(prompts=prompt1, msg="Step 05.2", btn_type='Apply') 
        
        """    
        Step 06: Click the dropdown control for Report in the Properties menu.
        Step 06.1: Expect to see Report1 appear only once in the dropdown list for Reports.
        """
        dropdown_btn_obj=utillobj.validate_and_get_webdriver_object(dropdown_btn_css, 'SourceReports combobox Dropdown button')
        utillobj.select_any_combobox_item(dropdown_btn_obj, combo_item='Report1', verify=True, expected_combobox_list=['Report1'], msg='Step 06.1: Expect to see Report1 appear only once in the dropdown list for Reports.')
        doc_obj.customize_active_dashboard_properties(btn_type='ok')
        
        """    
        Step 07: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
         
if __name__ == "__main__":
    unittest.main()