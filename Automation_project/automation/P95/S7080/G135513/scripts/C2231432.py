'''
Created on Jan 31, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7080
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231432
TestCase_Name : Properties dialogue displays Hold table as candidate reports 148829
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import document
from common.wftools import chart
from common.wftools import active_report
from common.lib import utillity

class C2231432_TestClass(BaseTestCase):

    def test_C2231432(self):
        
        """
        TESTCASE VARIABLES
        """
        Testcase_ID="C2231432"
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
        file_name='holdfile'
        field_list1=['CAR', 'DEALER_COST', 'RETAIL_COST']
        field_list2=['CAR', 'DEALER_COST']
        radiobutton_prompt='radiobutton'
        radiobutton_values=['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5']
        ComboBox_1_source = {'select_field':'CAR', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_1_target = {'verify_target_name':['Report1']}
        
        """
        COMMON CSS
        """
        report_parent_css="TableChart_1"
        report_parent_css2="TableChart_2"
        run_report_parent_css="#ITableData0"
        radio_button_css="#Prompt_1"
        run_radio_button_css="#PROMPT_1_cs"
        report_data_css="#TableChart_1 div[class^='x']"
        report_data_css2="#TableChart_2 div[class^='x']"
        Preview_panel_css="#canvasContainer"
        
        """
        Step 01: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='Document', master='ibisamp/car', mrid=username, mrpass=password)
           
        """
        Step 02: Select Active Report.
        Add fields CAR, DEALER_COST, & RETAIL_COST.
        """
        report_obj.change_output_format_type('active_report')
        for field in field_list1:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text('#'+report_parent_css, field, MEDIUM_WAIT_TIME)
        
        """
        Step 02.1: Expect to see the following Preview Pane. 
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=33, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=3, no_of_cells=3, table_id=report_parent_css, expected_list=field_list1, msg="Step 02.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 3, Testcase_ID+'_DS01.xlsx', msg="Step 02.2: Verify report dataset") 
            
        """
        Step 03: Click File under Report/Chart, next to the report output type(Active Report).
        Name it 'holdfile' and Save it in Foccache(temporary location)..
        """  
        report_obj.select_ia_ribbon_item(tab_name='Home', ribbon_button_name_path='File')
        chart_obj.save_file_in_save_dialog(file_name, save_folder='foccache')
        report_obj.wait_for_number_of_element(Preview_panel_css, expected_number=1, time_out=MEDIUM_WAIT_TIME)
        
        """
        Step 03.1: Expect to see the following Preview pane for the extract file: 'holdfile (car)' 
        """   
        chart_obj.verify_field_listed_under_querytree(bucket_type='Files', field_name='foccache/holdfile (car)', position=1, msg="Step 03.1: Expect to see the following extract file: 'holdfile (car) in query pane'")
        utillobj.verify_object_visible(Preview_panel_css, True, "Step 3.2: Verify the Preview is displayed")
            
        """
        Step 04: Add fields CAR, DEALER_COST from 'holdfile'.
        """ 
        report_obj.double_click_on_datetree_item('Dimensions->CAR', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css2, 'CAR', MEDIUM_WAIT_TIME)
        report_obj.double_click_on_datetree_item('Measures/Properties->DEALER_COST', 1)
        report_obj.wait_for_visible_text('#'+report_parent_css2, 'DEALER_COST', MEDIUM_WAIT_TIME)
        
        """
        Step 05: Select Insert tab, click Radio button. Position the Radio button to the right of the report.
        """  
        doc_obj.select_ia_ribbon_item('Insert', 'Radio_button')
        report_obj.wait_for_number_of_element(radio_button_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(radio_button_css, '#'+report_parent_css2, x=90, y=0)
        
        """
        Step 05.1: Expect to see the following Preview pane for the extract file: 'holdfile (car)' extract file, now containing a Radio button filter.
        """ 
        report_obj.wait_for_number_of_element(report_data_css2, expected_number=22, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css2, expected_list=field_list2, msg="Step 05.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css2, 5, 2, Testcase_ID+'_DS02.xlsx', msg="Step 05.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=radiobutton_prompt, parent_css=radio_button_css, verify_list=radiobutton_values, msg="step 05.3: verify Listbox prompt")
        
        """
        Step 06: Right-click Radio button control, select Properties. Select Field CAR from the field selection box. 
        Step 06.1: Expect to see the following Properties menu for the extract file: 'holdfile (car)' report.
        There should be only one report available and it should be Report1.
        """
        doc_obj.choose_right_click_menu_item_for_prompt(radio_button_css, item_name='Properties')
        doc_obj.customize_active_dashboard_properties(prompts=radiobutton_prompt, source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 06.1", btn_type='ok') 
        
        """
        Step 07: Click OK. Click the Run button.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        """
        Step 07.1: Expect to see the following Report with Radio button for the 'holdfile (car)' extract.
        """
        report_obj.verify_table_data_set(run_report_parent_css, Testcase_ID+"_DS03.xlsx",msg="Step:07.1 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:07.2 verify page summary")
        utillobj.verify_object_visible(run_radio_button_css, True, "Step 07.3: Verify the Dropdown Box is displayed")
        doc_obj.verify_selected_value_in_active_dashboard_prompts(component=radiobutton_prompt, parent_css=run_radio_button_css, expected_list=['[All]'], msg="step 07.4: verify Listbox prompt")
        
        """
        Step 08: Click the Radio button for AUDI.
        """
        doc_obj.select_prompt(component=radiobutton_prompt, parent_css=run_radio_button_css, select_list=['AUDI'])
        report_obj.wait_for_number_of_element('#ITableData0 tr',  expected_number=4, time_out=MEDIUM_WAIT_TIME)
        
        """
        Step 08.1: Expect to see the 'holdfile' extract filtered for AUDI.
        """
        report_obj.verify_table_data_set(run_report_parent_css, Testcase_ID+"_DS04.xlsx",msg="Step:08.1 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"1of10records,Page1of1",msg="Step:08.2 verify page summary")
        utillobj.verify_object_visible(run_radio_button_css, True, "Step 08.3: Verify the Dropdown Box is displayed")
        doc_obj.verify_selected_value_in_active_dashboard_prompts(component=radiobutton_prompt, parent_css=run_radio_button_css, expected_list=['AUDI'], msg="step 08.4: verify Listbox prompt")
        chart_obj.switch_to_default_content()
        
        """
        Step 09: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()