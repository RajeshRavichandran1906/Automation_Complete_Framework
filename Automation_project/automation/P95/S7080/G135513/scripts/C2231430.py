'''
Created on January 30, 2019

@author:Kavin 

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2231430
TestCase Name = MultiPg:ADP object blank after switch multi page 145198
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import utillity
from common.wftools import report,active_report
from common.wftools import document

class C2231430_TestClass(BaseTestCase):

    def test_C2231430(self):
        """
        Test case Object's
        """
        document_obj = document.Document(self.driver)
        report_obj = report.Report(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
        
        """
        Test case variables
        """
        TestcaseID= 'C2231430'
        table_css="TableChart_1"
        dropdown_css="#Prompt_1"
        dropdown_run_css="#combobox_dsPROMPT_1"
        property_dialog_css="#adpPropertiesDlg"
        dropdown_box_1=['Option 1']
        dropdown_box_2=['[All]']
        dropdown_box_run=['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        """ 
        Step 1: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513

        """
        document_obj.invoke_ia_tool_using_api(tool='document', master='ibisamp/car',mrid='mriddev',mrpass='mrpassdev', report_css="#canvasContainer", no_of_element=1)
        
        """
        Step 2: From Home tab select 'Active Report' as output format
        Add field COUNTRY & CAR for first page
        Expect to see the following Preview pane.
        """
        chart_obj.change_output_format_type('active_report')
        chart_obj.double_click_on_datetree_item('COUNTRY', 1)
        document_obj.wait_for_visible_text("#"+table_css, 'COUNTRY', document_obj.report_medium_timesleep)
        chart_obj.double_click_on_datetree_item('CAR', 1)
        document_obj.wait_for_visible_text("#"+table_css, 'CAR', document_obj.report_medium_timesleep)
        report_obj.verify_report_data_set_in_preview(table_css, 10, 2, TestcaseID+"_DS_02.xlsx", "Step 03 : verify dataset")
        
        """
        Step 3: Click the Insert Tab.
        Select 'Drop Down' object.
        Position the object to the right of the report.
        Expand it slightly horizontally and vertically.
        Expect to see the following Preview pane, now with a Dropdown filter positioned to the right of the report.
        """
        document_obj.select_ia_ribbon_item("Insert", "drop_down")
        document_obj.drag_drop_document_component(dropdown_css, "#theCanvas", 0, 50, target_drop_point='top_middle')
        document_obj.resizing_document_component('0.30', '2.50')
        report_obj.verify_report_data_set_in_preview(table_css, 10, 2, TestcaseID+"_DS_03.xlsx", "Step 03.1 : verify dataset")
        
        document_obj.verify_prompts_in_preview('dropdown', dropdown_css, dropdown_box_1, 'Step 06.2: Verify the dropdown box')
        
        """
        Step 4: Right-click Dropdown object on Canvas and select 'Properties'
        Click on 'Field' dropdown box and select COUNTRY.
        Expect to see the following Properties menu.
        Step 5: Click OK
        Now click 'Page' on Ribbon, in the upper left to create a second page.
        Expect to see a blank Page 2.
        """
        document_obj.choose_right_click_menu_item_for_prompt(dropdown_css, 'Properties')
        document_obj.wait_for_number_of_element(property_dialog_css, 1, chart_obj.report_medium_timesleep)
        document_obj.customize_active_dashboard_properties(source={'select_field':'COUNTRY'})
        document_obj.choose_right_click_menu_item_for_prompt(dropdown_css, 'Properties')
        document_obj.wait_for_number_of_element(property_dialog_css, 1, chart_obj.report_medium_timesleep)
        document_obj.customize_active_dashboard_properties(source={"verify_field":"COUNTRY"})
        document_obj.select_ia_ribbon_item("Insert", "Page")
        document_obj.wait_for_visible_text("#iaCanvasCaptionLabel", "Document", 20)
        
        """
        Step 06 : Go back to first page by selecting it on the upper right hand side. 
        Expect to see Page 1 re-displayed with the COUNTRY & CAR report with the Dropdown next to it.
        """
        document_obj.select_or_verify_document_page_menu("Page 1",default_page_name="Page 2")
        report_obj.verify_report_data_set_in_preview(table_css, 10, 2, TestcaseID+"_DS_06.xlsx", "Step 06.1 : verify dataset")
        document_obj.verify_prompts_in_preview('dropdown', dropdown_css, dropdown_box_2, 'Step 06.2: Verify the dropdown box')
        
        """
        Step 7: Click the Run button.
        Select ENGLAND from the Dropdown.
        Expect to see the report filtered for ENGLAND.
        """
        report_obj.select_ia_toolbar_item("toolbar_run")
        document_obj.switch_to_frame()
        util_obj.select_dropdown(dropdown_run_css, 'visible_text', 'ENGLAND')
        ar_obj.verify_active_report_dataset(TestcaseID+"_DS_07.xlsx", 'Step 7.1: Verify the active report', table_css='#ITableData0')
        ar_obj.verify_page_summary(0,"3of10records,Page1of1",msg="Step:4.1 verify page summary")
        util_obj.verify_dropdown_value(dropdown_run_css, value_list=dropdown_box_run, msg="Step 7 : Verify Dropdown value")
        
        """
        Step 8: Click Page 2.
        Expect to see a blank Page, as nothing was added to it originally.
        """
        document_obj.select_active_document_page_layout_menu_run_window('Page 2')
        document_obj.wait_for_number_of_element("#IBILAYOUTDIV0TABS", 1, 20)
        
        """
        Step 9: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp

        """
        document_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()