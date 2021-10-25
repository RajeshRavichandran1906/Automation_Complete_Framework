'''
Created on Jan 30, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7080
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231431
TestCase_Name : MultiPage Document:Restore fex w/multi Pages and ADP returns script error 145650
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import document
from common.wftools import chart
from common.wftools import active_report
from common.wftools import visualization
from common.lib import utillity

class C2231431_TestClass(BaseTestCase):

    def test_C2231431(self):
        
        """
        TESTCASE VARIABLES
        """
        Testcase_ID="C2231431"
        report_obj = report.Report(self.driver)
        doc_obj = document.Document(self.driver)
        chart_obj=chart.Chart(self.driver)
        active_report_obj = active_report.Active_Report(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        visual_obj = visualization.Visualization(self.driver)
        project = utillobj.parseinitfile('project_id')
        suite = utillobj.parseinitfile('suite_id')
        group = utillobj.parseinitfile('group_id')
        folder_path = "{0}_{1}/{2}".format(project, suite, group)
            
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        username='mriddev'
        password='mrpassdev'
        field_list1=['CAR', 'SALES']
        field_list2=['COUNTRY', 'DEALER_COST']
        prompt1='dropdown'
        dropdown_values=['Option 1']
        dropdown_values_1=['[All]']
        ComboBox_1_source = {'select_field':'CAR', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_1_target = {'verify_target_name':['Report1']}
        ComboBox_2_source = {'select_report':'Report2', 'select_field':'COUNTRY', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_2_target = {'verify_candidate_report':['Report1'], 'verify_target_name':['Report2']}
        
        """
        COMMON CSS
        """
        report_parent_css="TableChart_1"
        report_parent_css2="TableChart_2"
        run_report_parent_css="#ITableData0"
        run_report_parent_css2="#ITableData1"
        dropdown_css="#Prompt_1"
        dropdown_css2="#Prompt_2"
        run_dropdown_css="#comboboxPROMPT_1"
        run_dropdown_css2="#comboboxPROMPT_2"
        report_data_css="#TableChart_1 div[class^='x']"
        report_data_css2="#TableChart_2 div[class^='x']"
        source="#Prompt_1 div[id*='BiResizeHandle']"
        source2="#Prompt_2 div[id*='BiResizeHandle']"
        target="#"+report_parent_css
        target2="#"+report_parent_css2
        Page2_panel_css="#singleReportPanel"
        
        """
        Step 01: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='Document', master='ibisamp/car', mrid=username, mrpass=password)
           
        """
        Step 02: From Home tab, Select Active Report as output format
        Add fields CAR & SALES.
        """
        report_obj.change_output_format_type('active_report')
        for field in field_list1:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text('#'+report_parent_css, field, MEDIUM_WAIT_TIME)
         
        """
        Step 03: Select Insert tab, click Dropdown icon in ribbon.
        Position the Dropdown to the right of the report and expand it slightly horizontally and vertically.
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Drop_Down')
        report_obj.wait_for_number_of_element(dropdown_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(dropdown_css, '#'+report_parent_css, x=70, y=0)
        time.sleep(3)
        source_element=utillobj.validate_and_get_webdriver_objects(source, 'Dropdown Box source object')
        target_element=utillobj.validate_and_get_webdriver_object(target, 'report target object')
        visual_obj.create_lasso(source_element[3], target_element, target_xoffset=10, target_yoffset=-40, target_element_location='middle_right')
          
        """
        Step 03.1: Expect to see the following Preview pane with a Dropdown list to the right of the report.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=22, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css, expected_list=field_list1, msg="Step 03.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 2, Testcase_ID+'_DS01.xlsx', msg="Step 03.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt1, parent_css=dropdown_css, verify_list=dropdown_values, msg="step 03.3: verify dropdown prompt")
         
        """    
        Step 04: Right-click dropdown object on canvas, select Properties.
        Select CAR in field dropdown.
        Click OK.
        """
        doc_obj.choose_right_click_menu_item_for_prompt(dropdown_css, item_name='Properties')
        doc_obj.customize_active_dashboard_properties(source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 04", btn_type='ok') 
         
        """
        Step 04.1: Expect to see the following Preview pane, with properties applied to the Dropdown.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=22, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css, expected_list=field_list1, msg="Step 04.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 2, Testcase_ID+'_DS01.xlsx', msg="Step 04.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt1, parent_css=dropdown_css, verify_list=dropdown_values_1, msg="step 04.3: verify dropdown prompt")
         
        """
        Step 5: Click Page on the ribbon in the upper left, to add second page
        Add fields COUNTRY & DEALER_COST.
        """
        doc_obj.select_or_verify_document_page_menu("New Page")
        utillobj.synchronize_with_number_of_element(Page2_panel_css, expected_number=1, expire_time=MEDIUM_WAIT_TIME)
        for field in field_list2:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text('#'+report_parent_css2, field, MEDIUM_WAIT_TIME)
         
        """
        Step 05.1: Expect to see following Page 2 Preview pane.
        """  
        report_obj.wait_for_number_of_element(report_data_css2, expected_number=12, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css2, expected_list=field_list2, msg="Step 05.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css2, 5, 2, Testcase_ID+'_DS02.xlsx', msg="Step 05.2: Verify report dataset") 
         
        """
        Step 06: Select Insert tab, click Dropdown icon in ribbon.
        Position the Dropdown to the right of the report and expand it slightly horizontally and vertically.
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Drop_Down')
        report_obj.wait_for_number_of_element(dropdown_css2,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(dropdown_css2, '#'+report_parent_css2, x=70, y=0)
        time.sleep(3)
        source_element2=utillobj.validate_and_get_webdriver_objects(source2, 'Dropdown Box source object')
        target_element2=utillobj.validate_and_get_webdriver_object(target2, 'report target object')
        visual_obj.create_lasso(source_element2[3], target_element2, target_xoffset=10, target_yoffset=-40, target_element_location='middle_right')
          
        """
        Step 06.1: Expect to see a Dropdown added to the Page 2 Preview pane.
        """  
        report_obj.wait_for_number_of_element(report_data_css2, expected_number=12, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css2, expected_list=field_list2, msg="Step 06.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css2, 5, 2, Testcase_ID+'_DS02.xlsx', msg="Step 06.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt1, parent_css=dropdown_css2, verify_list=dropdown_values, msg="step 06.3: verify dropdown prompt")
         
        """    
        Step 07: Select Properties for this object, select Report2 from the Report selection box.
        Select COUNTRY from the Field selection box.
        Expect to see the following Properties for the Dropdown filter for Page 2.
        """
        doc_obj.choose_right_click_menu_item_for_prompt(dropdown_css2, item_name='Properties')
        doc_obj.customize_active_dashboard_properties(source=ComboBox_2_source, targets=ComboBox_2_target, msg="Step 07", btn_type='ok')
         
        """    
        Step 08: Click OK. Save the document as C2231431.fex exit IA+.
        """
        visual_obj.save_visualization_from_top_toolbar(file_name=Testcase_ID)
        chart_obj.api_logout()
        
        """    
        Step 09: Reopen the saved doucment using below API
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP95_S7080%252FG135513%252F&BIP_item=C2231431.fex
        """
        report_obj.edit_fex_using_api_url(folder_name=folder_path, tool='Document', fex_name=Testcase_ID, mrid=username, mrpass=password) 
        
        """
        Step 09.1: Expect to see the Document in IA+ positioned on Page 1.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=22, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css, expected_list=field_list1, msg="Step 09.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 2, Testcase_ID+'_DS01.xlsx', msg="Step 09.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt1, parent_css=dropdown_css, verify_list=dropdown_values_1, msg="step 09.3: verify dropdown prompt")
        
        """
        Step 10: Select Page 2 from menu on right side. 
        """
        doc_obj.select_or_verify_document_page_menu('Page 2')
        
        """
        Step 10.1: Expect to see the Preview pane for Page 2.
        """  
        report_obj.wait_for_number_of_element(report_data_css2, expected_number=12, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css2, expected_list=field_list2, msg="Step 10.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css2, 5, 2, Testcase_ID+'_DS02.xlsx', msg="Step 10.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt1, parent_css=dropdown_css2, verify_list=dropdown_values_1, msg="step 10.3: verify dropdown prompt")
        
        """
        Step 11: Go back to Page 1.
        """
        doc_obj.select_or_verify_document_page_menu('Page 1', default_page_name='Page 2')
        
        """
        Step 11.1: Expect to see the Preview pane for Page 1.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=22, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css, expected_list=field_list1, msg="Step 11.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 2, Testcase_ID+'_DS01.xlsx', msg="Step 11.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=prompt1, parent_css=dropdown_css, verify_list=dropdown_values_1, msg="step 11.3: verify dropdown prompt")
        
        """    
        Step 12: Click the Run button.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        """
        Step 12.1: Expect to see the following Document.
        """
        report_obj.verify_table_data_set(run_report_parent_css, Testcase_ID+"_DS03.xlsx",msg="Step:12.1 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:12.2 verify page summary")
        utillobj.verify_object_visible(run_dropdown_css, True, "Step 12.3: Verify the Dropdown Box is displayed")
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        time.sleep(2)
        report_obj.verify_table_data_set(run_report_parent_css2, Testcase_ID+"_DS04.xlsx",msg="Step:12.4 verify table dataset for report2")
        active_report_obj.verify_page_summary(1,"5of5records,Page1of1",msg="Step:12.5 verify page summary")
        utillobj.verify_object_visible(run_dropdown_css2, True, "Step 12.6: Verify the Dropdown Box is displayed")
        chart_obj.switch_to_default_content()
        
        """
        Step 13: Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()