'''
Created on Jan 31, 2019

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/2231425
Testcase Name : ADP:Error when create prompt if there is a -include 145100
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.wftools.document import Document
from common.lib.core_utility import CoreUtillityMethods

class C2231425_TestClass(BaseTestCase):

    def test_C2231425(self):
        
        """
        CLASS OBJECTS
        """
        report_obj = Report(self.driver)
        document_obj = Document(self.driver)
        core_utillobj=CoreUtillityMethods(self.driver)
        
        """
        CSS
        """
        PREVIEW_TABLE_CSS1="TableChart_1"
        EXISTING_REPORT_CSS="IncludeTable_1"
        DROPDOWN_CSS="#Prompt_1"
        CANVAS_CSS="#theCanvas"
        
        """
        VARIABLES
        """
        Testcase_ID="C2231425"
        field_list1=['CAR','SALES']
        field_list2=['LASTNAME','SALARY']
        master_file1='ibisamp/car'
        master_file2='ibisamp/empdata'
        username='mriddev'
        password='mrpassdev'
        source={'select_report':'Report1','select_field':'LASTNAME'}
        
        suite_id=core_utillobj.parseinitfile('suite_id')
        project_id=core_utillobj.parseinitfile('project_id')
        group_id=core_utillobj.parseinitfile('group_id')
        folder_path=project_id+'_'+suite_id+'->'+group_id
       
        """
        Step 1:Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        report_obj.invoke_ia_tool_using_new_api_login(master=master_file1, mrid=username, mrpass=password)
         
        """
        Step 2:Add CAR, SALES to query
        """
        for field in field_list1:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text("#"+PREVIEW_TABLE_CSS1, visble_element_text=field, time_out=report_obj.add_field_timesleep)
            
        report_obj.verify_column_title_on_preview(2, 2, PREVIEW_TABLE_CSS1, field_list1, "Step 2.1 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS1, 10, 2, Testcase_ID+"_Ds01.xlsx", "Step 2.2 Verify report data in preview")
        
        """
        Step 3:save this report as "Car"
        """
        report_obj.save_report_from_toptoolbar()
        report_obj.save_file_in_save_dialog('car')
        report_obj.api_logout()
         
        """
        Step 4:Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/empdata&item=IBFS:/WFC/Repository/P95/S10142
        """
        document_obj.invoke_ia_tool_using_api(master=master_file2, mrid=username, mrpass=password)
         
        """
        Step 5:Select Insert tab
        """
        document_obj.select_ia_ribbon_item('Insert', 'existing_report')
        
        """
        Step 6:Click "Existing Report"
        Select "Car" > Open
        """
        report_obj.select_masterfile_in_open_dialog(folder_path, 'car')
        
        """
        Step 7:Click on canvas to deselect the report
        Double click LASTNAME, SALARY
        Reposition the new report away from the inserted report
        """ 
        report_obj.wait_for_visible_text("#"+EXISTING_REPORT_CSS, visble_element_text=field, time_out=report_obj.add_field_timesleep)
        report_obj.click_preview_canvas(CANVAS_CSS, element_location='middle')
        report_obj.verify_column_title_on_preview(2, 2, EXISTING_REPORT_CSS, field_list1, "Step 7.1 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(EXISTING_REPORT_CSS, 10, 2, Testcase_ID+"_Ds02.xlsx", "Step 7.2 Verify existing report data in preview")
        
        
        for field in field_list2:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text("#"+PREVIEW_TABLE_CSS1, visble_element_text=field, time_out=report_obj.add_field_timesleep)
            
        report_obj.verify_column_title_on_preview(2, 2, PREVIEW_TABLE_CSS1, field_list2, "Step 7.3 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS1, 10, 2, Testcase_ID+"_Ds03.xlsx", "Step 7.4 Verify newly added document report data in preview")
        document_obj.drag_drop_document_component("#"+PREVIEW_TABLE_CSS1, "#"+EXISTING_REPORT_CSS, 130, 0)
        
        """
        Step 8:Select "Drop down" in Insert tab
        Right click the drop down component > "Properties"
        Click "Report" dropdown > "Report1"
        Click "Field" dropdown > LASTNAME
        Step 9:Click OK
        """
        document_obj.select_ia_ribbon_item('Insert','drop_down')
        document_obj.wait_for_number_of_element(DROPDOWN_CSS, 1, time_out=report_obj.document_component_timesleep)
        document_obj.drag_drop_document_component(DROPDOWN_CSS, "#"+PREVIEW_TABLE_CSS1,130, 0)
        document_obj.choose_right_click_menu_item_for_prompt(DROPDOWN_CSS, 'Properties')
        document_obj.customize_active_dashboard_properties(source=source)
       
        """
        Step : Expect to see the following Document canvas with Reports and Drop down.
        """
        report_obj.verify_column_title_on_preview(2, 2, EXISTING_REPORT_CSS, field_list1, "Step 9.1 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(EXISTING_REPORT_CSS, 10, 2, Testcase_ID+"_Ds04.xlsx", "Step 9.2 Verify existing report data in preview")
        
        report_obj.verify_column_title_on_preview(2, 2, PREVIEW_TABLE_CSS1, field_list2, "Step 9.3 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS1, 10, 2, Testcase_ID+"_Ds05.xlsx", "Step 9.4 Verify newly added document report data in preview")
        
        document_obj.verify_prompts_in_preview('dropdown', "#Prompt_1",['[All]'], "Step 9.5 Verify dropdown values")
        
        """
        Step 10:Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()