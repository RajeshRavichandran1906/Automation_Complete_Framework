'''
Created on Jan 29, 2019

@author: BM13368
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231423
Testcase Name : ADP:Action Failed error after create ADP and run request (145547)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.wftools.document import Document
from common.wftools.active_report import Active_Report

class C2231423_TestClass(BaseTestCase):

    def test_C2231423(self):
        """
        CLASS OBJECTS
        """
        report_obj = Report(self.driver)
        document_obj = Document(self.driver)
        active_report_obj=Active_Report(self.driver)
        
        """
        CSS
        """
        PREVIEW_TABLE_CSS="TableChart_1"
        LISTBOX_CSS="#Prompt_1"
        RUNTABLE_CSS="ITableData0"
        RUNTIME_LIST_CSS="#list_dPROMPT_1"
        RUNTABLE_DATA_CSS="#"+RUNTABLE_CSS+" tr:nth-child{0} td:nth-child{1}"
        
        """
        VARIABLES
        """
        Testcase_ID="C2231423"
        field_list=['CAR','SALES']
        master_file='ibisamp/car'
        username='mriddev'
        password='mrpassdev'
        source={'select_field':'CAR'}
        expected_page_summary='{0}of{1}records,Page1of1'
        expected_value_list=['[All]', 'ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        
        """
        Step 1:Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        document_obj.invoke_ia_tool_using_api(master=master_file, mrid=username, mrpass=password)
       
        """
        Step 2:From home tab change output format as Active Reports
        """
        #This step cannot be done as the document defalut format is Active Report. 
        """
        Step 3:Double click "CAR", "SALES"
        """
        for field in field_list:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text("#"+PREVIEW_TABLE_CSS, visble_element_text=field, time_out=report_obj.add_field_timesleep)
            
        report_obj.verify_column_title_on_preview(2, 2, PREVIEW_TABLE_CSS, field_list, "Step 3.1 Verify report column titles")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS, 10, 2, Testcase_ID+"_Ds01.xlsx", "Step 3.2 Verify report data in preview")
        
        """
        Step 4:Select Insert tab
        Step 5:Click "List"
        """
        document_obj.select_ia_ribbon_item('Insert', 'List')
        document_obj.wait_for_number_of_element(LISTBOX_CSS, expected_number=1, time_out=report_obj.document_component_timesleep)
        
        """
        Step 6:Reposition the List component away from the report
        """
        document_obj.drag_drop_document_component(LISTBOX_CSS, "#"+PREVIEW_TABLE_CSS, 70, 0)
         
        """
        Step 7:Right-click on ADP object on canvas > "Properties"
        """
        document_obj.choose_right_click_menu_item_for_prompt(LISTBOX_CSS, 'Properties')
        
        """
        Step 8:Click "Field" dropdown > "CAR"
        Step 9:Click OK
        """
        document_obj.customize_active_dashboard_properties(source=source)
                
        """
        Step 10:Click "Run"
        """
        report_obj.run_report_from_toptoolbar()
         
        """
        Step 11:Verify the report is run
        """
        report_obj.switch_to_frame()
        report_obj.wait_for_visible_text(RUNTABLE_DATA_CSS.format('2','1'), 'ALFA ROMEO', time_out=report_obj.report_short_timesleep)
        active_report_obj.verify_page_summary(0, expected_page_summary.format('9','107'), 'Step 11.1 Verify expected page summary is shown as' +expected_page_summary)
        document_obj.verify_prompts('listbox', RUNTIME_LIST_CSS, expected_value_list, "Step 11.2 Verify list box values at runtime")
        active_report_obj.verify_active_report_dataset(Testcase_ID+"_Ds02.xlsx", "Step 11.3 Verify report data at runtime", table_css="#"+RUNTABLE_CSS)
        document_obj.verify_default_selected_listbox_value('[All]', 'gray8', msg="Step 11.4")
        
        """
        Step 12:Click "ALFA ROMEO", "AUDI", "BMW"
        """
        report_obj.wait_for_visible_text("#"+RUNTABLE_CSS, 'CAR', time_out=report_obj.report_short_timesleep)
        document_obj.select_prompt('listbox', RUNTIME_LIST_CSS, ['ALFA ROMEO','AUDI','BMW'])
        
        """
        Step 13:Verify the report displays the selected values
        """
        active_report_obj.verify_active_report_dataset(Testcase_ID+"_Ds03.xlsx", "Step 13.1 Verify report data at runtime", table_css="#"+RUNTABLE_CSS)
        document_obj.verify_default_selected_listbox_value('ALFA ROMEO', 'gray8', msg="Step 13.2")
        document_obj.verify_default_selected_listbox_value('AUDI', 'gray8', msg="Step 13.3")
        document_obj.verify_default_selected_listbox_value('BMW', 'gray8', msg="Step 13.4")
        active_report_obj.verify_page_summary(0, expected_page_summary.format('3','10'), 'Step 13.5 Verify expected page summary is shown as' +expected_page_summary)
               
        """
        Step 14:Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()