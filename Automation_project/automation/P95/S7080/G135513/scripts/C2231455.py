'''
Created on Jan 29, 2019

@author: BM13368
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231455
Testcase Name : ADP: delete target with no source fld->error message 117337
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.wftools.document import Document
from common.wftools.active_report import Active_Report
from common.lib.utillity import UtillityMethods

class C2231455_TestClass(BaseTestCase):

    def test_C2231455(self):
        """
        CLASS OBJECTS
        """
        report_obj = Report(self.driver)
        document_obj = Document(self.driver)
        active_report_obj=Active_Report(self.driver)
        utillobj=UtillityMethods(self.driver)
        
        """
        CSS
        """
        PREVIEW_TABLE_CSS1="TableChart_1"
        PREVIEW_TABLE_CSS2="TableChart_2"
        LISTBOX_CSS="#Prompt_1"
        RUNTABLE_CSS1="ITableData0"
        RUNTABLE_CSS2="ITableData1"
        RUNTIME_LIST_CSS="#list_dPROMPT_1"
        
        """
        VARIABLES
        """
        Testcase_ID="C2231455"
        field_list1=['COUNTRY','CAR']
        field_list2=['MODEL','BODYTYPE']
        master_file='ibisamp/car'
        username='mriddev'
        password='mrpassdev'
        source1={'select_report':'Report1','select_field':'COUNTRY','verify_condition':'Equal to','verify_sort':'Ascending','verify_includeall':True}
        source2={'select_field':'MODEL'}
        targets={'select_candidate_report':'Report2','add_to_target':True,'verify_target_name':['Report1', 'Report2']}
        expected_page_summary='{0}of{1}records,Page1of1'
        verify_list1=['[All]','ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        verify_list2=['[All]', '100 LS 2 DOOR AUTO', '2000 4 DOOR BERLINA', '2000 GT VELOCE', '2000 SPIDER VELOCE']
        
        """
        Step 1 : Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        document_obj.invoke_ia_tool_using_api(master=master_file, mrid=username, mrpass=password)
         
        """
        Step 2:Change output format to Active Reports from Home tab
        """
        #default output for document id active report hence no need to change outout format 
        """
        Step 3:Add fields COUNTRY & CAR.
        Click Insert and add another report.
        Add fields MODEL & BODYTYPE to the second report.
        """
        for field in field_list1:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text("#"+PREVIEW_TABLE_CSS1, visble_element_text=field, time_out=report_obj.add_field_timesleep)
            
        document_obj.select_ia_ribbon_item('Insert', 'report')
        document_obj.wait_for_number_of_element("#"+PREVIEW_TABLE_CSS2,1,time_out=20)
            
        for field in field_list2:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text("#"+PREVIEW_TABLE_CSS2, visble_element_text=field, time_out=report_obj.add_field_timesleep)
            
        document_obj.drag_drop_document_component("#"+PREVIEW_TABLE_CSS2, "#"+PREVIEW_TABLE_CSS1, 120, 0)
            
        """
        Expect to see the following Document Preview containing two report objects.
        """
        report_obj.verify_column_title_on_preview(2, 2, PREVIEW_TABLE_CSS1, field_list1, "Step 3.1 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS1, 10, 2, Testcase_ID+"_Ds01.xlsx", "Step 3.2 Verify report data in preview")
        
        report_obj.verify_column_title_on_preview(2, 2, PREVIEW_TABLE_CSS2, field_list2, "Step 3.3 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS2, 10, 2, Testcase_ID+"_Ds02.xlsx", "Step 3.4 Verify report data in preview")
        
        """
        Step 4:Click the Insert tab and select Listbox.
        Expect to see the following Document Preview containing two report objects and a Listbox.
        """
        document_obj.select_ia_ribbon_item('Insert', 'List')
        document_obj.wait_for_number_of_element(LISTBOX_CSS, expected_number=1, time_out=report_obj.document_component_timesleep)
        utillobj.verify_object_visible(LISTBOX_CSS, True,"Step 4. Verify listbox is visible in the document page")
        
        """
        Step 5:Right-click in the Listbox and select Properties.
        Select Report1.
        Select COUNTRY from the Field area.
        Click Report2 in the Candidate area and move it to the Targets area.
        Expect to see the following Properties menu for the Listbox object.
        """
        
        document_obj.drag_drop_document_component(LISTBOX_CSS, "#"+PREVIEW_TABLE_CSS2, 70, 0)
        document_obj.choose_right_click_menu_item_for_prompt(LISTBOX_CSS, 'Properties')
        document_obj.customize_active_dashboard_properties(source=source1, targets=targets,msg="Step 5.1")
        document_obj.verify_prompts_in_preview('listbox', LISTBOX_CSS, verify_list1, "Step 5.2 Verify list box values in document preview")
       
        """
        Step 6:Click OK to the Properties menu.
        Click the first reporting object with COUNTRY & CAR and delete it from the canvas.
        """
        document_obj.choose_right_click_menu_item_for_prompt("#"+PREVIEW_TABLE_CSS1,'Delete')
        
        """
        Expect to see the Preview pane now with only the second report and the Listbox.
        """
        utillobj.verify_object_visible("#"+PREVIEW_TABLE_CSS1, False, 'Step 6. Verify rpeort1 is not available in the document preview')
        
        """
        Step 7:Click the Run button.
        Expect to see the Run time Document with only the second report and no Listbox.
        This is due to the deletion of the first report], which removed the print objects from the Properties.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        utillobj.verify_object_visible("#"+RUNTABLE_CSS2, False, 'Step 7.1 Verify rpeort1 is not available in the document preview')
        active_report_obj.verify_page_summary(0, expected_page_summary.format('18','18'), 'Step 7.2 Verify expected page summary is shown as' +expected_page_summary)
        active_report_obj.verify_active_report_dataset(Testcase_ID+"_Ds03.xlsx", "Step 7.3 Verify report data at runtime", table_css="#"+RUNTABLE_CSS1)
        utillobj.verify_object_visible(RUNTIME_LIST_CSS, False, 'Step 7.4 Verify rpeort1 is not available in the document preview')
        
        """
        Step 8:Back fin the Preview pane, right-click in the Listbox and select Properties.
        Select MODEL from the Field area.
        Click OK to the Properties menu.
        """
        report_obj.switch_to_default_content()
        document_obj.select_result_area_panel_caption_button('close')
        document_obj.choose_right_click_menu_item_for_prompt(LISTBOX_CSS, 'Properties')
        document_obj.customize_active_dashboard_properties(source=source2)
        
        """
        Expect to see the Preview pane now with only the second report and the Listbox.
        """
        report_obj.verify_column_title_on_preview(2, 2, PREVIEW_TABLE_CSS2, field_list2, "Step 8.1 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS2, 10, 2, Testcase_ID+"_Ds04.xlsx", "Step 8.2 Verify report data in preview")
        document_obj.verify_prompts_in_preview('listbox', LISTBOX_CSS, verify_list2, "Step 8.3 Verify listbox values in document preivew")
        
        """
        Step 9:Click the Run button.
        Expect to see the Run time Document with only the second report and the Listbox, which displays MODELs.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_report_obj.verify_page_summary(0, expected_page_summary.format('18','18'), 'Step 9.1 Verify expected page summary is shown as' +expected_page_summary)
        active_report_obj.verify_active_report_dataset(Testcase_ID+"_Ds05.xlsx", "Step 9.2 Verify report data at runtime", table_css="#"+RUNTABLE_CSS1)
        document_obj.verify_prompts('listbox', RUNTIME_LIST_CSS, verify_list2, "Step 9.3 Verify listbox value at document runtime")
        document_obj.verify_default_selected_listbox_value('[All]', 'gray8', msg="Step 9.4")
        
        """
        Step 10:Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
 


if __name__ == "__main__":
    unittest.main()