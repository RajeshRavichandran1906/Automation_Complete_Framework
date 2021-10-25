'''
Created on Jan 23, 2019

@author: KK14897

Testsuite =  http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=432673&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/5823950
TestCase Name = Enabling Active Cache in report (i.e: Active Cache option support only for AHTML Format)
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import active_chart
from common.wftools import active_report
from common.wftools import document
from common.lib import utillity

class C5823950_TestClass(BaseTestCase):

    def test_C5823950(self):
        
        """
            TESTCASE VARIABLES
        """
        
        Testcase_ID="C5823950"
        doc_obj=document.Document(self.driver)
        report_obj=report.Report(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        util_obj=utillity.UtillityMethods(self.driver)
        Text_box="Create a Dashboard with Cache enabled via menu options"
        folder_name="P116_S10670/G432674"
        table_css="TableChart_1"
        Fex_Name="AR-AD-089-AHTML"
        
        def verify_default_active_report_options_dialog_advanced_tab(self, textbox_value, css, msg, itype=None, tbox="input_box", **kwargs): 
            if (tbox == "input_box"):
                actual_obj=util_obj.validate_and_get_webdriver_object(css, msg)
                actual_obj=util_obj.get_attribute_value(actual_obj, itype)
                util_obj.asequal(textbox_value, actual_obj[itype].strip(), msg)

            if kwargs['radio_button']==False:
                try:
                    actual_obj=util_obj.validate_and_get_webdriver_object("#advancedPane #securityDateRadioBtn input", "date button")
                    actual_obj=actual_obj.get_attribute("disabled")
                    util_obj.asequal('true', actual_obj, "Step 3.2 : Date Radio button disabled")
                except:
                    print ("Date Radio button enabled")
                try:
                    actual_obj=util_obj.validate_and_get_webdriver_object("#advancedPane #securityDaysRadioBtn input", "days button")
                    actual_obj=actual_obj.get_attribute("disabled")
                    util_obj.asequal('true', actual_obj, "Step 3.3 : Days Radio button disabled")
                except:
                    print ("Days Radio button enabled")
                    
            if 'advanced_expiration' in kwargs:
                if kwargs['advanced_expiration']==True:
                    status=self.driver.find_element_by_css_selector("#advancedPane #securityExpirationCheckBox input[class='bi-check-box-input']").is_selected()
                    util_obj.asequal(True, status, "Step 3.4 : Verify Expiration is unchecked previously.")
                if kwargs['advanced_expiration']==False:
                    status=self.driver.find_element_by_css_selector("#advancedPane #securityExpirationCheckBox input[class='bi-check-box-input']").is_selected()
                    util_obj.asequal(False, status, "Step 3.4 : Verify Expiration is checked previously.")


        """
        Step 1: Create a new Document, selecting ggsales as the file.
        Select AHTML as the output type.
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS10071%2F
        """
        report_obj.invoke_ia_tool_using_new_api_login("Document", "ibisamp/ggsales")
        
        """
        Step 2: Using the Insert button, add a text box to the Dashboard canvas.
        Add the text "Create a Dashboard with Cache enabled via menu options" to the Text Box.
        Expect to see the following Document with Text Box.
        """
        doc_obj.select_ia_ribbon_item("Insert", "text_box")
        active_chart_obj.wait_for_number_of_element("#theCanvas #Text_1", 1, 35)
        doc_obj.resizing_document_component('0.25', '4.40')
        doc_obj.enter_text_in_document_Textbox('Text_1', Text_box)
        doc_obj.verify_text_in_document_Textbox('#Text_1', Text_box, "Step 02: Verify textbox value")
        
        """
        Step 3: Using the Insert options add a Report to the canvas.
        Select Category, Product and Unit Sales for the report.
        Position the report preview pane under the Text Box and center it.
        Expect to see the following Report preview pane.
        """
        doc_obj.select_ia_ribbon_item("Insert", "report")
        util_obj.synchronize_with_number_of_element("#"+table_css, 1,15)
        report_obj.double_click_on_datetree_item("Category", 1)
        doc_obj.wait_for_visible_text("#"+table_css, "Category", 20)
        report_obj.double_click_on_datetree_item("Product", 1)
        doc_obj.wait_for_visible_text("#"+table_css, "Product", 20)
        report_obj.double_click_on_datetree_item("Unit Sales", 1)
        doc_obj.wait_for_visible_text("#"+table_css, "Unit Sales", 20)
        doc_obj.drag_drop_document_component('#Text_1', "#"+table_css, 0, 50, target_drop_point='bottom_middle')
        coln_list = ['Category', 'Product', 'Unit Sales']
#         report_obj.create_report_data_set_in_preview(table_css, 2, 3, Testcase_ID+"_1.xlsx")
        report_obj.verify_report_data_set_in_preview(table_css, 2, 3, Testcase_ID+"_1.xlsx", msg="Step 3.1 : Verify data set in preview")
        report_obj.verify_report_column_titles_on_preview(3, 3, coln_list, "#"+table_css, msg="Step 3.2 : Verify Column titles")
        
        """
        Step 4: Ensure that the Report preview is active.
        From the Format tab, click the Navigation button.
        Expect to see the Navigation options appear.
        STep 5:Click the Pages on Demand button.
        Expect to see the Pages on Demand button highlighted.
        """
        doc_obj.select_ia_ribbon_item("Format", "pages_on_demand")
        web_element=self.driver.find_element_by_css_selector("#FormatReportPod[class*='checked']")
        util_obj.verify_checked_class_property(web_element,"Step 04: verify Page on demand is highlighted")
        
        """
        Step 6: Also from the Format tab, click Features.
        Expect to see the Active Report Options icon appear.
        Step 7: Click Active Report Options, then select the Advanced tab along the left side of the Active Report Options menu. 
        Expect to see the following Active Report Options, Advanced screen.
        """
        util_obj.synchronize_with_visble_text("#FormatActiveReportStyling", "Active Report Options", 20)
        doc_obj.select_ia_ribbon_item("Format", "active_report_options")
        ar_obj.active_report_options("Advanced")
        verify_default_active_report_options_dialog_advanced_tab(self,'',"#advancedPane #advSecurityPassHBox  input", "Row_Retrieve",itype="value",radio_button=False)
        verify_default_active_report_options_dialog_advanced_tab(self,'100',"#advancedPane #rowsRetrievedCombo input[type='text']","Row_Retrieve",itype="value",advanced_expiration=False,radio_button=False)
        
        """
        Step 8: "In the Active Cache area, select value 500 from the drop down values for the Rows Retrieved option.
        Click Apply and then OK."
        Expect to see the option change from 100 to 500 rows for the Rows Retrieved option. 
        """
        ar_obj.active_report_options("Advanced",advanced_rows_retrieved="500",btnOk=True)
        verify_default_active_report_options_dialog_advanced_tab(self,'500',"#advancedPane #rowsRetrievedCombo input[type='text']", "Row_Retrieve",itype="value",radio_button=False)
        
        """
        Step 9: In the top left hand corner, click the View code button, directly above the Data icon.
        Scroll down until the block of code containing "ON TABLE SET" appears. 
        Expect to see the line: "ON TABLE SET WEBVIEWER ON".
        """
        expected_syntax_list=["ON TABLE SET WEBVIEWER ON"]
        report_obj.verify_fexcode_syntax(expected_syntax_list, "STep 09 : Verify fex code")
        
        """
        Step 10: Close the View code panel.
        Click the Run button.
        Save the Dashboard as AR-AD-089-AHTML.
        Expect to see the following Dashboard Report.
        """
        report_obj.run_report_from_toptoolbar()
        doc_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text("[id*='LOBJText']", Text_box, 20)
#         report_obj.create_table_data_set("#ITableData0",Testcase_ID+"_2.xlsx")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_2.xlsx",msg="Step 10.1 : verify table dataset for report1")
        ar_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step 10.2 : verify page summary")
        doc_obj.switch_to_previous_window()
        active_chart_obj.save_as_chart_from_menubar(Fex_Name)
        doc_obj.api_logout()
        
        """
        Step 11 : Edit the AR-AD-089-AHTML. 
        http://machine:port/alias/tools/portlets/resources/markup/sharep/SPEditorBoot.jsp?folderPath=IBFS%253A%252FWFC%252FRepository%252FP116/S10851&description=AR-AD-089-AHTML&itemName=AR-AD-089-AHTML.fex&isReferenced=true&type=items
        Scroll down until the block of code containing "ON TABLE SET" appears.
        """
        report_obj.edit_fex_using_api_url(folder_name, tool="document", fex_name=Fex_Name, mrid="mrid", mrpass="mrpass")
        report_obj.verify_fexcode_syntax(expected_syntax_list, "Step 11 : Verify fex code")
        
        
if __name__ == '__main__':
    unittest.main()