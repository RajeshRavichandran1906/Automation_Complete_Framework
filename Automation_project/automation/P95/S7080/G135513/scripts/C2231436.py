'''
Created on Jan 25, 2019

@author: BM13368
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231436
Testcase Name : HOLD:ADP: no table in document, but table1 in ADP properties 142902
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.wftools.document import Document
from common.lib.utillity import UtillityMethods

class C2231436_TestClass(BaseTestCase):

    def test_C2231436(self):
        """
        CLASS OBJECTS
        """
        report_obj = Report(self.driver)
        document_obj = Document(self.driver)
        utill_obj=UtillityMethods(self.driver)
        
        """
        CSS
        """
        PREVIEW_TABLE_CSS="TableChart_1"
        LISTBOX_CSS="#Prompt_1"
        DOCUMENT_LABEL_CSS="#iaCanvasCaptionLabel"
        """
        VARIABLES
        """
        Testcase_ID="C2231436"
        field_list=['COUNTRY','CAR','DEALER_COST']
        fex_name_to_save='Mytest'
        master_file='ibisamp/car'
        username='mriddev'
        password='mrpassdev'
        expected_document_label_name='Document'
        prompt={'verify_report':' '}
        
        """
        Step 1: Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Reportt&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S10142/G135513
        """
        report_obj.invoke_ia_tool_using_new_api_login(master=master_file, mrid=username, mrpass=password)
        
        """
        Step 2:Add fields COUNTRY, CAR & DEALER_COST.
        Select the File option under Chart/Report at the top left.
        Name it 'Mytest' and click Save.
        """
        for field in field_list:
            report_obj.double_click_on_datetree_item(field, 1)
            report_obj.wait_for_visible_text("#"+PREVIEW_TABLE_CSS, visble_element_text=field, time_out=report_obj.chart_short_timesleep)

        report_obj.select_ia_ribbon_item('Home','file_dropdown')
        utill_obj.select_or_verify_bipop_menu("Select a location and format...")
        report_obj.save_file_in_save_dialog(fex_name_to_save)
        utill_obj.synchronize_with_number_of_element('#createFromHoldMenuBtn', 1, report_obj.chart_long_timesleep)
            
        """
        Expect to see the following Preview pane for the saved Report - Mytest.
        """
        report_obj.verify_column_title_on_preview(3, 3, PREVIEW_TABLE_CSS, field_list, "Step 02.00 : Verify report column titles")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS, 10, 3, Testcase_ID+"_Ds01.xlsx", "Step 02.01 : Verify report data set in preview")
        
        """
        Step 3 :From status bar select document from create report
        """
        report_obj.create_hold_type('Create Document')
        
        """
        Expect to see a new Preview open for Document.
        """
        actual_document_label_name=utill_obj.validate_and_get_webdriver_object(DOCUMENT_LABEL_CSS, 'Preview document label').text.strip()
        utill_obj.asequal(expected_document_label_name,actual_document_label_name, "Step 03.00 : Expect to see a preview open for document")
        
        """
        Step 4:DO NOT INSERT ANY REPORT or CHART.
        Click on Insert-> click on List Box
        """
        document_obj.select_ia_ribbon_item('Insert', 'List')
        document_obj.wait_for_number_of_element(LISTBOX_CSS, expected_number=1, time_out=report_obj.home_page_short_timesleep)
        
        """
        Expect to see the following List Box on the Document Preview.
        """
        utill_obj.verify_object_visible(LISTBOX_CSS, True, "Step 04.00: Expect to see the following List Box on the Document Preview")
        
        """
        Step 5:Right click on List Box object. 
        Select the Properties option.
        """
        document_obj.choose_right_click_menu_item_for_prompt(LISTBOX_CSS, 'Properties')
        
        """
        Expect to see the following Properties menu with nothing appearing in the Report of Field areas.
        """
        document_obj.customize_active_dashboard_properties(prompts=prompt)
        
        """
        Step 6:Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """


if __name__ == "__main__":
    unittest.main()