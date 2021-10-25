'''
Created on Jan 10, 2019

@author: Vpriya

Testsuite =  http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=432673&group_order=asc
Testcase id=http://172.19.2.180/testrail/index.php?/cases/view/5852675
TestCase Name = Add Global filter in a Document of reports (GRMERGE=ADVANCED)..
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import report
from common.wftools import active_chart
from common.wftools import active_report
from common.wftools import document
from common.wftools import visualization
from common.lib import utillity
from common.lib import core_utility
from common.pages import webfocus_editor
import time

class C5852675_TestClass(BaseTestCase):

    def test_C5852675(self):
        
        """
            TESTCASE VARIABLES
        """
        
        Testcase_ID="C5852675"
        doc_obj=document.Document(self.driver)
        report_obj=report.Report(self.driver)
        vis_obj=visualization.Visualization(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        webfocus_editor_obj=webfocus_editor.WebfocusEditor(self.driver)
        active_report_obj=active_report.Active_Report(self.driver)
        folder_name="P116_S10670/G432673"
        report_css="#TableChart_1"
        Page2_panel_css="#singleReportPanel"
        report_css_2="#TableChart_2"
        table_css = "table[id='iLayTB$']"
        add_filter_css="[class='arFilter']"
        menu_css="#MAINTABLE_wbodyMain0"
        filter_css=".arDashboardBar .arDashboardBarGlobalButton [title='Global Filter'] img"
        
        """        
        Step1:Sign in to WebFOCUS
        http://machine:port/{alias}
        """
        """
        Step 2:Create a new Document using the ggsales file.
        Select Active Report as the Output Format
        http://machine:port/{alias}/ia?tool=document&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS10670%2F
        """
        report_obj.invoke_ia_tool_using_new_api_login("Document", "ibisamp/ggsales")
            
        """
        Step 3:From the Insert icon, add a Text Box with the text "Global Filter for Document containing Reports" .
        Expect to see the following Document canvas with the Text Box added.
        """
        vis_obj.select_ribbon_item('Insert','text_box')
        active_chart_obj.wait_for_number_of_element("#theCanvas #Text_1", 1, 35)
        doc_obj.resizing_document_component('0.25', '3.60')
        doc_obj.enter_text_in_document_Textbox('Text_1', 'Global Filter for Document containing Reports')
        time.sleep(2)
        doc_obj.verify_text_in_document_Textbox('#Text_1', 'Global Filter for Document containing Reports', "Step 01:01: Verify textbox value")
           
        """
        Step 4:Select Category, Product and Unit Sales to get a report.
        Move the Report preview underneath and centered below the Text Box.
        Expect to see the following Document canvas with the report preview panel on Page 1.
        """
        report_obj.select_ia_ribbon_item('Insert', 'report')
        utill_obj.synchronize_with_number_of_element(report_css, 1,15)
        doc_obj.drag_drop_document_component('#Text_1', '#TableChart_1', 0, 50, target_drop_point='bottom_middle')
           
        field_name_1='Category'
        field_name_2='Product'
        field_name_3='Unit Sales'
        report_obj.double_click_on_datetree_item(field_name_1, 1)
        element_css_1="#queryTreeColumn tr:nth-child(4)"
        utill_obj.synchronize_with_visble_text(element_css_1, 'Category', 25)
           
        report_obj.double_click_on_datetree_item(field_name_2, 1)
        element_css_2="#queryTreeColumn tr:nth-child(5)"
        utill_obj.synchronize_with_visble_text(element_css_2, 'Product', 25)
           
        report_obj.double_click_on_datetree_item(field_name_3,1)
        element_css_3="#queryTreeColumn tr:nth-child(3)"
        utill_obj.synchronize_with_visble_text(element_css_3, 'UnitSales', 25)
           
        coln_list = ['Category', 'Product', 'Unit Sales']
        report_obj.verify_report_titles_on_preview(3, 3, "TableChart_1", coln_list, "Step 4.1: Verify Category, Product, Unit Sales report.")
           
        """
        Step 5:Click the Page icon in the upper left to add a new Page.
        Insert a Report on Page 2 of the Document canvas.
        Expect to see Page 2 contain an empty Report preview panel.
        """
        doc_obj.select_or_verify_document_page_menu("New Page")
        utill_obj.synchronize_with_number_of_element(Page2_panel_css, 1,35)
        report_obj.select_ia_ribbon_item('Insert', 'report')
        utill_obj.verify_object_visible(report_css_2, True,"Step:2 step contain empty preview panel")
           
        """
        Step 6:Select fields Category, Product and Dollar Sales for the report on Page 2.
        Click the run button the check both reports.Expect to see the following Reports.
        """
        field_name1_1='Category'
        field_name1_2='Product'
        field_name1_3='Dollar Sales'
        report_obj.double_click_on_datetree_item(field_name1_1, 1)
        element_css_1="#queryTreeColumn tr:nth-child(4)"
        utill_obj.synchronize_with_visble_text(element_css_1, 'Category', 25)
           
        report_obj.double_click_on_datetree_item(field_name1_2, 1)
        element_css_2="#queryTreeColumn tr:nth-child(5)"
        utill_obj.synchronize_with_visble_text(element_css_2, 'Product', 25)
           
        report_obj.double_click_on_datetree_item(field_name1_3,1)
        element_css_3="#queryTreeColumn tr:nth-child(3)"
        utill_obj.synchronize_with_visble_text(element_css_3, 'Dollar Sales', 25)
           
        coln_list = ['Category', 'Product', 'Dollar Sales']
        report_obj.verify_report_titles_on_preview(3, 3, "TableChart_2", coln_list, "Step 4.1: Verify Category, Product, Unit Sales report.")
           
        report_obj.run_report_from_toptoolbar()
        utill_obj.switch_to_frame()
        time.sleep(1)
        doc_obj.verify_active_document_page_layout_menu_run_window(table_css,['Layouts','Page 1','Page 2'], "Step 4.2: Verify Multipage_dashboard")
       
        """
        Step 7:Save and run the report. Close the report
        """
        utill_obj.switch_to_default_content()
        active_chart_obj.save_as_chart_from_menubar(Testcase_ID)
        report_obj.api_logout()
           
   
        """
        Step 8:Edit the saved Fex with the Text Editor and change the Keyword/Value combination from SHOW_GLOBALFILTER=OFF to SHOW_GLOBALFILTER=ON.
        http://machine:port/alias/tools/portlets/resources/markup/sharep/SPEditorBoot.jsp?folderPath=IBFS%253A%252FWFC%252FRepository%252FP116/S10670description=C5852675&itemName=C5852675.fex&isReferenced=true&type=items
        Verify that the line containing SHOW_GLOBALFILTER has been changed.
        """
           
        webfocus_editor_obj.invoke_fex_using_text_editor(folder_name,Testcase_ID)
        webfocus_editor_obj.find_and_replace_in_text_editor("SHOW_GLOBALFILTER=OFF","SHOW_GLOBALFILTER=ON")
           
        """
        Step 9:Save the report and Close the text editor
        """
        webfocus_editor_obj.click_text_editor_ribbon_button('Save')
        report_obj.api_logout()
#          

        """
        Step 10:Execute each Document Fex.
        Verify that Global Filter icon to apply a filter to Reports is present at the top of the Document.
        Expect to see a 10 record report on Page 1, with Unit Sales.
        Expect to see a 10 record report on Page 2, with Dollar Sales.
        """
        report_obj.run_fex_using_api_url(folder_name,Testcase_ID,'mrid','mrpass',run_table_css='#ITableData0 #TCOL_0_C_0 span',wait_time=90)
        utill_obj.verify_object_visible(filter_css,True,"Step:10.1 verify active filter icon is available")
        #report_obj.create_table_data_set("#ITableData0",Testcase_ID+"_1.xlsx")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_1.xlsx",msg="Step:10.1 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:4.1 verify page summary")
        
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        
        #report_obj.create_table_data_set("#ITableData1",Testcase_ID+"_2.xlsx")
        report_obj.verify_table_data_set("#ITableData1", Testcase_ID+"_2.xlsx",msg="Step:10.2 verify table dataset for report2")
        active_report_obj.verify_page_summary(1,"10of10records,Page1of1",msg="Step:4.1 verify page summary")
        
        """
        Step 11:Tap the Global Filter icon to apply a filter to the dashboard.
        Expect to see the Global Filter menu panel appear.
        Verify that the buttons appear for: Operator:, Add Condition, Filter, Highlight and Clear functions.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        core_utill_obj.left_click(utill_obj.validate_and_get_webdriver_object(filter_css,'Filter_icon'))
        core_utill_obj.python_left_click(utill_obj.validate_and_get_webdriver_object(filter_css,'Filter_icon'))
        active_report_obj.verify_filter_buttons(['Operator: AND', 'Add Condition', 'Filter', 'Highlight', 'Clear All'], "Step 08.1: Verify Filter that the selection menu appears:")
        active_report_obj.move_active_popup('1', '350', '120')
        
        """
        Step 12:Tap the Add Condition button, then select Category as the Filter field.
        From the value drop down, select Food.
        Expect to see the following Filter selection screen.
        """
        active_report_obj.add_global_condition_field('Category','0_globalop_0')
        utill_obj.synchronize_with_number_of_element(add_filter_css,1,45)
        
        active_report_obj.create_filter(1,'Equals',value1='Food')
        active_report_obj.filter_button_click('Filter')
        time.sleep(3)
        
        """
        Step:13 Click the Filter button to apply the Global Filter to the Document.
        Expect to see the following Reports.
        """
        report_obj.create_table_data_set("#ITableData0",Testcase_ID+"_3.xlsx")
        active_report_obj.move_active_popup('1', '350', '120')
        report_obj.verify_table_data_set("#ITableData0",Testcase_ID+"_3.xlsx",msg="Step:13.1")
        active_report_obj.verify_page_summary(0,"3of10records,Page1of1",msg="Step:4.1 verify page summary")
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        time.sleep(2)
        #report_obj.create_table_data_set("#ITableData1",Testcase_ID+"_4.xlsx")
        report_obj.verify_table_data_set("#ITableData1",Testcase_ID+"_4.xlsx",msg="Step:13.2")
        active_report_obj.verify_page_summary(1,"3of10records,Page1of1",msg="Step:4.1 verify page summary")
        
        """
        Step 14:Click on Clear All button.
        Expect to see the Filters removed from the Filter menu and the report on Page 1 back to 3 Category/Product.
        """
        doc_obj.select_active_document_page_layout_menu_run_window('Page 1')
        time.sleep(2)
        active_report_obj.filter_button_click('Clear All')
        utill_obj.synchronize_with_number_of_element(menu_css,1,20)
        utill_obj.verify_object_visible("#FiltTable1 .arFilterItem", False, "Step 14:Filter menu removed from the filter dialog")
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_1.xlsx",msg="Step:14.1 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:4.1 verify page summary")
        
        """
        Step 15:Click on the Global Filter x button to close the filter menu.
        Expect to see the menu removed and the same report original report.
        """
        
        active_report_obj.close_filter_dialog()
        time.sleep(1)
        report_obj.verify_table_data_set("#ITableData0", Testcase_ID+"_1.xlsx",msg="Step:15.1 verify table dataset for report1")
        active_report_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:4.1 verify page summary")
        doc_obj.select_active_document_page_layout_menu_run_window('Page 2')
        time.sleep(2)
        report_obj.verify_table_data_set("#ITableData1", Testcase_ID+"_2.xlsx",msg="Step:10.2 verify table dataset for report2")
        active_report_obj.verify_page_summary(1,"10of10records,Page1of1",msg="Step:4.1 verify page summary")
        
        """
        Step 16:Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()