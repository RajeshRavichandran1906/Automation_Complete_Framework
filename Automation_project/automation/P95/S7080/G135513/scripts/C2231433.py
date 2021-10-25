'''
Created on Jan 31, 2019

@author: Kavin
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231433
Testcase Name : Script error after add ADP object & click Format shortcut 147729
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.wftools import chart
from common.wftools.document import Document
from common.lib.utillity import UtillityMethods


class C2231433_TestClass(BaseTestCase):

    def test_C2231433(self):
        """
        CLASS OBJECTS
        """
        report_obj = Report(self.driver)
        document_obj = Document(self.driver)
        utill_obj=UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        CSS
        """
        PREVIEW_TABLE_CSS="TableChart_1"
        CHECK_BOX_CSS="#Prompt_1"
        
        """
        VARIABLES
        """
        Testcase_ID="C2231433"
        field_name=['CAR']
        master_file='ibisamp/car'
        username='mriddev'
        password='mrpassdev'
        
        """
        Step 1: Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Reportt&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        document_obj.invoke_ia_tool_using_api(master=master_file, mrid=username, mrpass=password)
        
        """
        Step 2:Add field CAR.
        Select Insert tab, click Checkbox.
        Position the Checkbox to the right of the report.
        Click 'Active Report' format shortcut in the
        IA status bar.
        Expect to see the following Preview pane.
        """
        
        chart_obj.double_click_on_datetree_item('CAR', 1)
        document_obj.wait_for_visible_text("#"+PREVIEW_TABLE_CSS, 'CAR', document_obj.report_medium_timesleep)
        document_obj.select_ia_ribbon_item('Insert', 'Checkbox')
        document_obj.drag_drop_document_component(CHECK_BOX_CSS, "#theCanvas", 0, 50, target_drop_point='top_middle')
        document_obj.wait_for_number_of_element(CHECK_BOX_CSS, expected_number=1, time_out=report_obj.home_page_short_timesleep)
        document_obj.drag_drop_document_component(CHECK_BOX_CSS, CHECK_BOX_CSS, 40, 0)
        report_obj.verify_column_title_on_preview(1, 1, PREVIEW_TABLE_CSS, field_name, "Step 2.1: Verify report column titles")
#         report_obj.create_report_data_set_in_preview(PREVIEW_TABLE_CSS, 10, 1, Testcase_ID+"_Ds01.xlsx")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS, 10, 1, Testcase_ID+"_Ds01.xlsx","Step 2:2: Verify report data set")
        utill_obj.verify_object_visible(CHECK_BOX_CSS,True,"Step 2.3 verify checkbox is visible")
        
        """
        Step 3:Click 'Active Report' format shortcut in the
        IA status bar at the bottom right.
        From the menu, change the output to Active PDF.
        Click the Home tab at the top left.
        Expect to see the following Preview pane, with Active PDF as the output format.
        """
        
        report_obj.change_output_format_type('active_pdf', location='')
        report_obj.switch_ia_ribbon_tab('Home')
        document_obj.verify_output_format("Active PDF", step="Step 3")
        
        
        """
        Step 4:Click 'Active PDF' format shortcut again in the
        IA status bar at the bottom right.
        From the menu, change the output to Active Report.
        Expect to see the following Preview pane, with Active Report as the output format.
        """
        
        report_obj.change_output_format_type('active_report', location='')
        report_obj.switch_ia_ribbon_tab('Home')
        document_obj.verify_output_format("Active Report", step="Step 4")
        
        """
        Step 5:Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        document_obj.api_logout()

if __name__ == "__main__":
    unittest.main()