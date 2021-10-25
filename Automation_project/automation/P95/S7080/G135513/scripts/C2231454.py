'''
Created on Jan 29, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7080
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2231454
TestCase_Name : ADP: delete parent object -> no report & value in object 117591
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import document
from common.wftools import chart
from common.wftools import active_report
from common.lib import utillity

class C2231454_TestClass(BaseTestCase):

    def test_C2231454(self):
        
        """
        TESTCASE VARIABLES
        """
        Testcase_ID="C2231454"
        report_obj = report.Report(self.driver)
        doc_obj = document.Document(self.driver)
        chart_obj=chart.Chart(self.driver)
        active_report_obj = active_report.Active_Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
            
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        username='mriddev'
        password='mrpassdev'
        field_list=['COUNTRY', 'CAR', 'MODEL']
        prompt1='dropdown'
        prompt2='listbox'
        dropdown_values=['Option 1']
        listbox_values=['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
        dropdown_values_1=['[All]']
        listbox_values_1=['[All]', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        ComboBox_1_source = {'select_field':'COUNTRY', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_1_target = {'verify_target_name':['Report1']}
        ComboBox_2_source = {'select_field':'CAR', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_2_target = {'verify_target_name':['Report1']}
        available_prompts = {'add_prompt':'True'}
        
        """
        COMMON CSS
        """
        report_parent_css="TableChart_1"
        run_report_parent_css="#ITableData0"
        dropdown_css="#Prompt_1"
        listbox_css="#Prompt_2"
        run_listbox_css="#PROMPT_2_cs"
        report_data_css="#TableChart_1 div[class^='x']"
        listbox="#gridAvailableADP div[class$='content'] table img[src*='listbox']"
        combobox="#gridAvailableADP div[class$='content'] table img[src*='combobox']"
        
        """
        Step 01: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95/S10142
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='Document', master='ibisamp/car', mrid=username, mrpass=password)
          
        """
        Step 02: Add fields COUNTRY, CAR & MODEL.
        """
        #report_obj.change_output_format_type('active_report')
        for field in field_list:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text('#'+report_parent_css, field, MEDIUM_WAIT_TIME)
        
        """
        Step 03: Click Insert and add Dropdown and Listbox objects.
        Reposition the Dropdown and Listbox component away from the report
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Drop_Down')
        report_obj.wait_for_number_of_element(dropdown_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(dropdown_css, '#'+report_parent_css, x=70, y=0)
        doc_obj.select_ia_ribbon_item('Insert', 'List')
        report_obj.wait_for_number_of_element(listbox_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(listbox_css, dropdown_css, x=70, y=0)
        time.sleep(3)
         
        """
        Step 03.1: Expect to see the following Document Preview pane.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=36, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=field_list, msg="Step 03.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 3, Testcase_ID+'_DS01.xlsx', msg="Step 03.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt1, parent_css=dropdown_css, verify_list=dropdown_values, msg="step 03.3: verify dropdown prompt")
        doc_obj.verify_prompts_in_preview(component=prompt2, parent_css=listbox_css, verify_list=listbox_values, msg="step 03.4: verify Listbox prompt")
        
        """    
        Step 04: Right-click in the Dropdown object, select the Properties option.
        Select COUNTRY from the Field area as parent.
        Click OK to the Properties menu.
        """
        doc_obj.choose_right_click_menu_item_for_prompt(dropdown_css, item_name='Properties')
        doc_obj.customize_active_dashboard_properties(source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 04", btn_type='ok') 
        
        """    
        Step 05: Right-click in the Dropdown object, select the Properties option.
        Select COUNTRY from the Field area as parent.
        Click OK to the Properties menu.
        """
        doc_obj.choose_right_click_menu_item_for_prompt(listbox_css, item_name='Properties')
        doc_obj.customize_active_dashboard_properties(source=ComboBox_2_source, targets=ComboBox_2_target, msg="Step 05", btn_type='ok')
        
        """
        Step 05.1: Expect to see the following Document Preview pane.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=36, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=field_list, msg="Step 05.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 3, Testcase_ID+'_DS01.xlsx', msg="Step 05.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt1, parent_css=dropdown_css, verify_list=dropdown_values_1, msg="step 05.3: verify dropdown prompts")
        doc_obj.verify_prompts_in_preview(component=prompt2, parent_css=listbox_css, verify_list=listbox_values_1, msg="step 05.4: verify Listbox prompts of CAR values")
        
        """    
        Step 06: Right-click again in the Dropdown object and click the Cascades option.
        Move both Available Prompts to the
        Selected Prompts area.
        """
        doc_obj.choose_right_click_menu_item_for_prompt(dropdown_css, item_name='Properties')
        doc_obj.add_and_verify_prompts_in_cascade()
        combobox_icon=utillobj.validate_and_get_webdriver_object(combobox, 'combobox prompt in Available Prompts')
        utillobj.default_click(combobox_icon)
        doc_obj.add_and_verify_prompts_in_cascade(available_prompts=available_prompts)
        listbox_icon=utillobj.validate_and_get_webdriver_object(listbox, 'listbox prompt in Available Prompts')
        utillobj.default_click(listbox_icon)
        doc_obj.add_and_verify_prompts_in_cascade(available_prompts=available_prompts)
        
        """    
        Step 07: Click OK to the Properties menu for the Dropdown.
        Back on the canvas, right-click the Dropdown object again.
        Select the Delete option for the Dropdown object.
        """
        doc_obj.customize_active_dashboard_properties(btn_type='ok')
        doc_obj.choose_right_click_menu_item_for_prompt(dropdown_css, item_name='Delete')
        
        """
        Step 07.1: Expect to see the following Document Preview, now with only the Listbox for CAR.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=36, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=field_list, msg="Step 07.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 3, Testcase_ID+'_DS01.xlsx', msg="Step 07.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt2, parent_css=listbox_css, verify_list=listbox_values_1, msg="step 07.3: verify Listbox prompts of CAR values")
        
        """    
        Step 08: Click the Run button.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        """    
        Step 08.1: Expect to see the following Run time Document with a report and the Listbox of CAR values.
        """
        report_obj.wait_for_number_of_element(run_listbox_css, expected_number=1, time_out=MEDIUM_WAIT_TIME)
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_DS02.xlsx', 'Step 08.1: Verify the active report', table_css=run_report_parent_css)
        doc_obj.verify_prompts(component=prompt2, parent_css=run_listbox_css, verify_list=listbox_values_1, msg="step 08.2: verify Listbox prompts of CAR values")
        chart_obj.switch_to_default_content()
        
        """    
        Step 09: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
         
if __name__ == "__main__":
    unittest.main()