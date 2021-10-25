'''
Created on Jan 28, 2019

@author: Magesh

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/7080
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231438
TestCase_Name : ADP:Object does not appear on canvas/run after restore 144546
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import document
from common.wftools import chart
from common.wftools import active_report
from common.wftools import visualization
from common.lib import utillity

class C2231438_TestClass(BaseTestCase):

    def test_C2231438(self):
        
        """
        TESTCASE VARIABLES
        """
        Testcase_ID="C2231438"
        utillobj = utillity.UtillityMethods(self.driver)
        report_obj = report.Report(self.driver)
        doc_obj = document.Document(self.driver)
        chart_obj=chart.Chart(self.driver)
        active_report_obj = active_report.Active_Report(self.driver)
        visual_obj = visualization.Visualization(self.driver)
            
        """
        COMMON VARIABLES
        """
        MEDIUM_WAIT_TIME = 60
        fex_name='dropdown'
        username='mriddev'
        password='mrpassdev'
        project = utillobj.parseinitfile('project_id')
        suite = utillobj.parseinitfile('suite_id')
        group = utillobj.parseinitfile('group_id')
        folder_path = "{0}_{1}/{2}".format(project, suite, group)
        prompt1 = {'select_prompts':'combobox_1'}
        ComboBox_1_source = {'select_field':'CAR', 'verify_condition':'Equal to', 'verify_includeall':True}
        ComboBox_1_target = {'verify_target_name':['Report1']}
        dropdown_values_1=['[All]']
        field_list=['CAR', 'SALES']
        
        """
        COMMON CSS
        """
        report_parent_css="TableChart_1"
        dropdown_css="#Prompt_1"
        run_dropdown_css="#comboboxPROMPT_1"
        report_data_css="#TableChart_1 div[class^='x']"
        source="#Prompt_1 div[id*='BiResizeHandle']"
        target="#"+report_parent_css
        
        """
        Step 01: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95/S10142
        """
        report_obj.invoke_ia_tool_using_new_api_login(tool='Document', master='ibisamp/car', mrid=username, mrpass=password)
          
        """
        Step 02: Select Format Tab, click 'Active Report' format
        Add fields CAR & SALES.
        Select Insert Tab, and add a Dropdown Box.
        Expand the Dropdown box slightly, both horizontally and vertically.
        """
        report_obj.change_output_format_type('active_report')
        for field in field_list:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text('#'+report_parent_css, field, MEDIUM_WAIT_TIME)
         
        """
        Step 02.1: Expect to see the following Preview pane with a report and a Dropdown Box.
        """  
        report_obj.wait_for_number_of_element(report_data_css, expected_number=22, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css, expected_list=field_list, msg="Step 02.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 2, Testcase_ID+'_DS01.xlsx', msg="Step 02.2: Verify report dataset") 
        
        """
        Select Insert Tab, and add a Dropdown Box.
        Expand the Dropdown box slightly, both horizontally and vertically.
        """
        doc_obj.select_ia_ribbon_item('Insert', 'Drop_Down')
        report_obj.wait_for_number_of_element(dropdown_css,  expected_number=1, time_out=MEDIUM_WAIT_TIME)
        doc_obj.drag_drop_document_component(dropdown_css, '#'+report_parent_css, x=90, y=0)
        time.sleep(3)
        source_element=utillobj.validate_and_get_webdriver_objects(source, 'Dropdown Box source object')
        target_element=utillobj.validate_and_get_webdriver_object(target, 'report target object')
        visual_obj.create_lasso(source_element[3], target_element, target_xoffset=10, target_yoffset=-40, target_element_location='middle_right')
        
        """
        Step 03: Right-click on Dropdown object on Canvas and select 'Properties'.
        Select CAR in the Field dropdown.
        Expect to see the following Properties menu for the Dropdown Box
        """
        doc_obj.choose_right_click_menu_item_for_prompt(dropdown_css, item_name='Properties')
        doc_obj.customize_active_dashboard_properties(prompts=prompt1, source=ComboBox_1_source, targets=ComboBox_1_target, msg="Step 03", btn_type='ok') 
         
        """    
        Step 04: Click OK for the Properties menu. Click the Run button.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        """    
        Step 04.1: Expect to see the following Document with the report and Dropdown Box.
        """
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_DS02.xlsx', 'Step 4.1: Verify the active report', table_css='#ITableData0')
        utillobj.verify_object_visible(run_dropdown_css, True, "Step 4.2: Verify the Dropdown Box is displayed")
        chart_obj.switch_to_default_content()
        
        """    
        Step 05: Save the Document by clicking the IA button at the top left. Name it 'dropdown'.
        Exit IA+
        """
        visual_obj.save_visualization_from_top_toolbar(file_name=fex_name)
        chart_obj.api_logout()
        
        """    
        Step 06: In IA reopen the Document just saved - 'dropdown'.
        """
        report_obj.edit_fex_using_api_url(folder_name=folder_path, tool='Document', fex_name=fex_name, mrid=username, mrpass=password)
        
        """    
        Step 06.1: Expect to see the original Preview pane with the report and the Dropdown Box.
        """
        report_obj.wait_for_number_of_element(report_data_css, expected_number=22, time_out=MEDIUM_WAIT_TIME) 
        report_obj.verify_column_title_on_preview(colnum=2, no_of_cells=2, table_id=report_parent_css, expected_list=field_list, msg="Step 06.1: Verify column titles")
        report_obj.verify_report_data_set_in_preview(report_parent_css, 10, 2, Testcase_ID+'_DS01.xlsx', msg="Step 06.2: Verify report dataset") 
        doc_obj.verify_prompts_in_preview(component=fex_name, parent_css=dropdown_css, verify_list=dropdown_values_1, msg="step 05.3: verify dropdown prompts")
        
        """    
        Step 07: Click the Run button.
        """
        chart_obj.run_chart_from_toptoolbar()
        chart_obj.switch_to_frame()
        
        """    
        Step 07.1: Expect to see the Run time Document, also with a report and a Dropdown Box.
        """
        active_report_obj.verify_active_report_dataset(Testcase_ID+'_DS02.xlsx', 'Step 7.1: Verify the active report', table_css='#ITableData0')
        utillobj.verify_object_visible(run_dropdown_css, True, "Step 7.2: Verify the Dropdown Box is displayed")
        chart_obj.switch_to_default_content()
        
        """    
        Step 08: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
         
if __name__ == "__main__":
    unittest.main()