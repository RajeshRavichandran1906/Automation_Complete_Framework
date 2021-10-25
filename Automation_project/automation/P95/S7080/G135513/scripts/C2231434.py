'''
Created on Jan 31, 2019

@author: Kavin
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2231434
Testcase Name : ADP:Existing source Report displays string code as title 150328
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.report import Report
from common.wftools import chart
from common.wftools.document import Document
from common.lib.utillity import UtillityMethods
from common.pages import ia_ribbon


class C2231434_TestClass(BaseTestCase):

    def test_C2231434(self):
        """
        CLASS OBJECTS
        """
        ia_ribbon_obj=ia_ribbon.IA_Ribbon(self.driver)
        report_obj = Report(self.driver)
        document_obj = Document(self.driver)
        utill_obj=UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        CSS
        """
        PREVIEW_TABLE_CSS="TableChart_1"
        RADIO_BUTTON_CSS="#Prompt_1"
        
        """
        VARIABLES
        """
        Testcase_ID="C2231434"
        master_file='ibisamp/car'
        username='mriddev'
        password='mrpassdev'
        
        """
        Step 1 : Launch IA Report using below API link
        http://machine:port/{alias}/ia?tool=Reportt&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        document_obj.invoke_ia_tool_using_api(master=master_file, mrid=username, mrpass=password)
        
        """
        Step 2 : Add fields CAR, MODEL & SALES.
        Expect to see the following Preview pane.
        """
        fields_list=['CAR','MODEL','SALES']
        for field in fields_list:
            chart_obj.double_click_on_datetree_item(field, 1)
            document_obj.wait_for_visible_text("#"+PREVIEW_TABLE_CSS, field, document_obj.report_medium_timesleep)
#         report_obj.create_report_data_set_in_preview(PREVIEW_TABLE_CSS, 18, 3, Testcase_ID+"_DS_02.xlsx")
        report_obj.verify_report_data_set_in_preview(PREVIEW_TABLE_CSS, 18, 3, Testcase_ID+"_DS_02.xlsx", "Step 02 : verify dataset")   
        
        """
        Step 3 : Exit report and save as Report1.
        """
        
        ia_ribbon_obj.select_ia_application_menu_item("exit")
        report_obj.ia_exit_save("Yes")
        report_obj.save_file_in_save_dialog(Testcase_ID)
        
        """
        Step 4 : Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513
        """
        document_obj.api_logout()
        document_obj.invoke_ia_tool_using_api(master=master_file, mrid=username, mrpass=password)
        
        """
        Step 5 : Select Insert tab, click Radio Button.
        Expect to see the following Preview pane, containing only the Radio button.
        """
        document_obj.select_ia_ribbon_item('Insert', 'Radio_Button')
        utill_obj.verify_object_visible(RADIO_BUTTON_CSS,True,"Step 5 :  verify checkbox is visible")
        
        """
        Step 6 : Right-click in the Radio button and select the Properties option.
        Expect to see the following Properties menu.
        Also expect to see nothing for Report, as the Document only contains a Radio button.
        Step 7 : Click the drop down controls for the Report and Field boxes
        Nothing should display for Report or Field.
        """
        document_obj.choose_right_click_menu_item_for_prompt(RADIO_BUTTON_CSS, 'Properties')
        document_obj.wait_for_number_of_element("#adpPropertiesDlg", 1, chart_obj.report_medium_timesleep)
        document_obj.customize_active_dashboard_properties(source={"verify_report":" ","verify_field":" "})
        
        """
        Step 8 : Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        document_obj.api_logout()

if __name__ == "__main__":
    unittest.main()