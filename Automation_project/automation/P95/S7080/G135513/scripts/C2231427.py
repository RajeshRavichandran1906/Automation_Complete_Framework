'''
Created on January 28, 2019

@author:Kavin 

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2231427
TestCase Name = ADP:Restore fex w/ADP target from comp on Page2, get error 147146
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import chart
from common.lib import utillity
from common.wftools import report,active_report
from common.wftools import document
from common.lib import core_utility

class C2231427_TestClass(BaseTestCase):

    def test_C2231427(self):
        """
        Test case Object's
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        document_obj = document.Document(self.driver)
        report_obj = report.Report(self.driver)
        ar_obj=active_report.Active_Report(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        chart_obj=chart.Chart(self.driver)
       
        """
        Test case variables
        """
        TestcaseID= 'C2231427'
        table_css="TableChart_1"
        table_css_2="TableChart_2"
        run_table1_css="#ITableData0"
        run_table2_css="#ITableData1"
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        dropdown_css="#Prompt_1"
        dropdown_run_css="#combobox_dsPROMPT_1"
        property_dialog_css="#adpPropertiesDlg"
        dropdown_box_in_preview=['Option 1']
        dropdown_box_in_run=['[All]', 'ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        
        """ 
        Step 1: Launch IA Document using below API link
        http://machine:port/{alias}/ia?tool=Document&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7080/G135513

        """
        document_obj.invoke_ia_tool_using_api(tool='document', master='ibisamp/car',mrid='mriddev',mrpass='mrpassdev', report_css="#canvasContainer", no_of_element=1)
        
        """
        Step 2 : From Home tab select Active Report as output format  
        """
        chart_obj.change_output_format_type('active_report')
        
        
        """
        Step 3: Add fields CAR & DEALER_COST.
        Expect to see the following Preview pane.
        """
        chart_obj.double_click_on_datetree_item('CAR', 1)
        document_obj.wait_for_visible_text("#"+table_css, 'CAR', document_obj.report_medium_timesleep)
        chart_obj.double_click_on_datetree_item('DEALER_COST', 1)
        document_obj.wait_for_visible_text("#"+table_css, 'DEALER_COST', document_obj.report_medium_timesleep)
        report_obj.verify_report_data_set_in_preview(table_css, 10, 2, TestcaseID+"_DS_03.xlsx", "Step 03 : verify dataset")
        
        """
        Step 4: Select Insert tab, click PAGE to add second page.
        Add fields COUNTRY & SEATS for second page.
        Expect to see the following Preview pane for Page 2.
        """
        document_obj.select_ia_ribbon_item("Insert", "Page")
        chart_obj.double_click_on_datetree_item("COUNTRY", 1)
        document_obj.wait_for_visible_text("#"+table_css_2, 'COUNTRY', document_obj.report_medium_timesleep)
        chart_obj.double_click_on_datetree_item("SEATS", 1)
        document_obj.wait_for_visible_text("#"+table_css_2, 'SEATS', document_obj.report_medium_timesleep)
        report_obj.verify_report_data_set_in_preview(table_css_2, 5, 2, TestcaseID+"_DS_04.xlsx", "Step 03 : verify dataset")
        
        """
        Step 5: Reselect PAGE 1 from page menu on the right side.
        Select Insert tab, click 'Dropdown'. 
        Expect to see the following Preview pane for Page 1, now with a Dropdown filter.
        """
        document_obj.select_or_verify_document_page_menu("Page 1",default_page_name="Page 2")
        document_obj.select_ia_ribbon_item("Insert", "drop_down")
        document_obj.drag_drop_document_component(dropdown_css, "#theCanvas", 0, 50, target_drop_point='top_middle')
        report_obj.verify_report_data_set_in_preview(table_css, 10, 2, TestcaseID+"_DS_05.xlsx", "Step 05.1 : verify dataset")
        document_obj.verify_prompts_in_preview('dropdown', dropdown_css, dropdown_box_in_preview, 'Step 03.2: Verify the dropdown box')
        
        """
        Step 6: Right-click on the object, select Properties.
        Select 'Report2' from the Report area.
        Select COUNTRY for Field.
        Expand the Drop down Box slightly.
        Expect to see the following Properties menu.
        
        Step 7: Click OK.
        Click the Run button.
        Expect to see the following Document, still on Page 1 with the Dropdown for Country.
        """
        document_obj.choose_right_click_menu_item_for_prompt(dropdown_css, 'Properties')
        document_obj.wait_for_number_of_element(property_dialog_css, 1, chart_obj.report_medium_timesleep)
        document_obj.customize_active_dashboard_properties(source={'select_report':'Report2', 'select_field':'COUNTRY'})
        document_obj.resizing_document_component('0.25', '3.00')
        document_obj.choose_right_click_menu_item_for_prompt(dropdown_css, 'Properties')
        document_obj.wait_for_number_of_element(property_dialog_css, 1, chart_obj.report_medium_timesleep)
        document_obj.customize_active_dashboard_properties(source={"verify_report":"Report2","verify_field":"COUNTRY"})
        
        report_obj.select_ia_toolbar_item("toolbar_run")
        document_obj.switch_to_frame()
        ar_obj.verify_active_report_dataset(TestcaseID+"_DS_07.xlsx", 'Step 7.1: Verify the active report', table_css=run_table1_css)
        ar_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:4.1 verify page summary")
        util_obj.verify_dropdown_value(dropdown_run_css, value_list=dropdown_box_in_run, msg="Step 1 : Verify Dropdown value")
        
        """
        Step 8: From the Dropdown, select ITALY.
        Select Page 2 in the Document header area at the top.
        Expect to see no changes to Page 1.
        Expect to see the Dropdown value of ITALY applied to the report on Page 2.
        """
        util_obj.select_dropdown(dropdown_run_css, 'visible_text', 'ITALY')
        ar_obj.verify_active_report_dataset(TestcaseID+"_DS_08.1.xlsx", 'Step 8.1: Verify the active report', table_css=run_table1_css)
        ar_obj.verify_page_summary(0,"10of10records,Page1of1",msg="Step:4.1 verify page summary")
        document_obj.select_active_document_page_layout_menu_run_window('Page 2')
        ar_obj.verify_active_report_dataset(TestcaseID+"_DS_08.2.xlsx", 'Step 8.2: Verify the active report', table_css=run_table2_css)
        
        """
        Step 9: Save the Fex and exit IA+
        Re-open the Fex in IA+
        """
        document_obj.switch_to_default_content()
        chart_obj.save_as_chart_from_menubar(TestcaseID)
        document_obj.api_logout()
        report_obj.edit_fex_using_api_url(folder_path, tool="Document", fex_name=TestcaseID, mrid='mriddev',mrpass='mrpassdev')
        
        """
        Step 10: Click the Run button.
        Select JAPAN.
        Switch to Page 2.
        Expect to see the Document re-display, positioned on Page 1.
        Also expect to see Page 2 filtered for JAPAN.
        """
        report_obj.select_ia_toolbar_item("toolbar_run")
        document_obj.switch_to_frame()
        util_obj.select_dropdown(dropdown_run_css, 'visible_text', 'JAPAN')
        ar_obj.verify_active_report_dataset(TestcaseID+"_DS_10.1.xlsx", 'Step 10.1: Verify the active report', table_css=run_table1_css)
        document_obj.select_active_document_page_layout_menu_run_window('Page 2')
        ar_obj.verify_active_report_dataset(TestcaseID+"_DS_10.2.xlsx", 'Step 10.2: Verify the active report', table_css=run_table2_css)
        
        """
        Step 11: Logout using the below link:
        http://machine:port/{alias}/service/wf_security_logout.jsp

        """
        document_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()