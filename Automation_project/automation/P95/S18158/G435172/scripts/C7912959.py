'''
Created on Jan 11, 2019

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/18158&group_by=cases:section_id&group_id=435172&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/7912959
TestCase Name = Allow users to enable HFREEZE for AHTML reports using the GUI
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_report import Active_Report
from common.wftools.active_chart import Active_Chart
from common.wftools.chart import Chart
from common.wftools.report import Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.lib.javascript import JavaScript

class C7912959_TestClass(BaseTestCase):

    def test_C7912959(self):
        
        """
        TESTCASE Object's
        """
        active_rpt_obj = Active_Report(self.driver)
        core_utilobj = CoreUtillityMethods(self.driver)
        utilobj = UtillityMethods(self.driver)
        chart_obj = Chart(self.driver)
        report_obj = Report(self.driver)
        j_script = JavaScript(self.driver)
        active_chart_obj = Active_Chart(self.driver)
        project_id = core_utilobj.parseinitfile('project_id')
        suite_id = core_utilobj.parseinitfile('suite_id')
        group_id = core_utilobj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        page_load_css = "#TableChart_1"
        table_id_css = '#IWindowBodyF_0_0'
        table_id_css_1 = 'IWindowBodyFTS_0_0'
        table_id_css_2 = "#IWindowBodyFTB_0_0"
        case_id = 'C7912959'
        scroll_bar_css = "#MAINTABLE_0 .vertical-scroll-indicator-wrapper"
        scroll_bar_css_1 = "#MAINTABLE_0 .vertical-virtual-scrollbar-wrapper"
        table_row_css = "#IWindowBodyFTB_0_0 tr:nth-child(57) td:nth-child(6)"
        freeze_checked_css = "#FormatTab #FormatReportFreeze.tool-bar-button-checked"
        
        '''
        local function
        '''
        def verify_page_summary(expected_title, msg):
            page_summary_css=".statusBarPagingTemplate"
            summary_object = utilobj.validate_and_get_webdriver_object(page_summary_css, 'Page summary text')
            actual_title = utilobj.get_element_attribute(summary_object, 'title').strip().replace(' ','')
            utilobj.asequal(expected_title, actual_title, msg)
        
        """
        Step 1: http://machine:port/{alias}/ia?tool=Report&master=ibisamp/ggsales&item=IBFS:/WFC/Repository/P95_S18158/G435172
        """
        active_rpt_obj.invoke_report_tool_using_api('ibisamp/ggsales')
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='Draganddropfieldsontothecanvasorintothequerypanetobeginbuildingyourreport', time_out=190)
        
        """
        Step 2: Double click the following Dimensions: Product ID, State, City, Category
        """
        chart_obj.double_click_on_datetree_item('Product ID', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='Product ID', time_out=90)
        chart_obj.double_click_on_datetree_item('State', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='State', time_out=90)
        chart_obj.double_click_on_datetree_item('City', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='City', time_out=90)
        chart_obj.double_click_on_datetree_item('Category', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='Category', time_out=90)
        
        """
        Step 3: Double click the following Measures: Dollar Sales, Budget Dollars
        """
        chart_obj.double_click_on_datetree_item('Dollar Sales', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='Dollar Sales', time_out=90)
        chart_obj.double_click_on_datetree_item('Budget Dollars', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='Budget Dollars', time_out=90)
        report_obj.verify_report_data_set_in_preview('TableChart_1', 21, 6, case_id+'_step3.xlsx', 'Step 3: Verify data set.')
        
        """
        Step 4: Select Home tab > "Active Report" format
        """
        chart_obj.change_output_format_type('active_report')
        
        """
        Step 5: Click on Home tab > "Row Totals"
        """
        report_obj.select_ia_ribbon_item('Home', 'row_totals')
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='TOTAL', time_out=90)
        
        """
        Step 6: Select Format tab > "Freeze"
        """
        report_obj.select_ia_ribbon_item('Format', 'Freeze')
        utilobj.synchronize_until_element_is_visible(freeze_checked_css, 30)
        
        """
        Step 7: Click Run button
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.wait_for_visible_text(table_id_css, visble_element_text='TOTAL', time_out=90)
        expected_heading = ['ProductID', 'State', 'City', 'Category', 'DollarSales', 'BudgetDollars', 'TOTAL']
        active_rpt_obj.verify_column_heading(table_id_css_1, expected_heading, 'Step 7: Verify heading.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_step7.xlsx', 'Step 7.1: Verify data set', table_css=table_id_css_2, desired_no_of_rows=29)
        
        """
        Step 8: Verify a thin vertical scrollbar is displayed (with data overlaying but visible)
        """
        utilobj.verify_object_visible(scroll_bar_css, True, "Step 8: Verify a thin vertical scrollbar is displayed (with data overlaying but visible)")
        
        """
        Step 9: Hover over the the "Budget Dollars" column > Verify scrollbar is fully visible
        """
        utilobj.verify_object_visible(scroll_bar_css_1, True, "Step 9: Hover over the the 'Budget Dollars' column > Verify scrollbar is fully visible")
        
        """
        Step 10: Scroll to the bottom of the current page
        """
        cell_obj = utilobj.validate_and_get_webdriver_object(table_row_css, 'Table last row cell')
        j_script.scrollIntoView(cell_obj)
        verify_page_summary('117of117records,Page1of3', 'Step 10: verify page summary.')
        report_obj.switch_to_default_content()
        
        """
        Step 11: Click on Save > Save as "C7912959_a" > Save
        """
        active_chart_obj.save_as_chart_from_menubar(case_id+'_a')
        time.sleep(3)
        
        """
        Step 12: Select Home tab > "Document"
        """
        report_obj.select_ia_ribbon_item('Home', 'Document')
        utilobj.synchronize_until_element_is_visible("#HomeTab #HomeCompose.tool-bar-button-checked", 60)
        report_obj.wait_for_number_of_element("#canvasContainer", expected_number=1, time_out=60)
        
        """
        Step 13: Click Run button
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        report_obj.wait_for_visible_text(table_id_css, visble_element_text='TOTAL', time_out=90)
        expected_heading = ['ProductID', 'State', 'City', 'Category', 'DollarSales', 'BudgetDollars', 'TOTAL']
        active_rpt_obj.verify_column_heading(table_id_css_1, expected_heading, 'Step 13: Verify heading.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_step13.xlsx', 'Step 13.1: Verify data set', table_css=table_id_css_2, desired_no_of_rows=29)
        
        """
        Step 14: Verify scrollbar is displayed
        """
        utilobj.verify_object_visible(scroll_bar_css, True, "Step 14: Verify scrollbar is displayed.")
        utilobj.verify_object_visible(scroll_bar_css_1, True, "Step 14.1: Verify scrollbar is displayed.")
        report_obj.switch_to_default_content()
        
        """
        Step 15: Click on Save > Save as "C7912959_b" > Save
        """
        active_chart_obj.save_as_chart_from_menubar(case_id+'_b')
        time.sleep(3)
        
        """
        Step 16: Logout http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        utilobj.infoassist_api_logout()
        
        """
        Step 17: Run the Document FEX
                 http://machine:port/ibi_apps/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP95_S18158/G435172&BIP_item=C7912959_b.fex
        """
        active_rpt_obj.run_active_report_using_api(case_id+'_b.fex', column_css="#IWindowBodyF_0_0", synchronize_visible_element_text='TOTAL', repository_path=folder_path)
        expected_heading = ['ProductID', 'State', 'City', 'Category', 'DollarSales', 'BudgetDollars', 'TOTAL']
        active_rpt_obj.verify_column_heading(table_id_css_1, expected_heading, 'Step 17: Verify heading.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_step13.xlsx', 'Step 17.1: Verify data set', table_css=table_id_css_2, desired_no_of_rows=29)
        
        """
        Step 18: Click arrow at the bottom of the report to select page 2
        """
        cell_obj = utilobj.validate_and_get_webdriver_object(table_row_css, 'Table last row cell')
        j_script.scrollIntoView(cell_obj)
        core_utilobj.left_click(utilobj.validate_and_get_webdriver_object(".arGridBar .statusBarPaging .statusBarPagingNext", 'Page summary next page'))
        
        """
        Step 19: Verify scrollbar is displayed > Scroll to the bottom of page 2
        """
        utilobj.verify_object_visible(scroll_bar_css, True, "Step 19: Verify scrollbar is displayed.")
        utilobj.verify_object_visible(scroll_bar_css_1, True, "Step 19.1: Verify scrollbar is displayed.")
        verify_page_summary('117of117records,Page2of3', 'Step 19.2: verify page summary.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_step19.xlsx', 'Step 19.4: Verify data set', table_css="#IWindowBodyFTB_0_1", desired_no_of_rows=29)
        utilobj.infoassist_api_logout()
        
        """
        Step 20: Reopen the saved Report FEX in IA:
                 http://machine:port/ibi_apps/ia?item=IBFS%3A%2FWFC%2FRepository%2FP95_S18158/G435172%2FC7912959_a.fex&tool=report
        """
        active_rpt_obj.invoke_report_in_edit_mode_using_api(case_id+'_a', repository_path=folder_path)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='TOTAL', time_out=190)
        
        """
        Step 21: Select Format tab > Verify "Freeze" is selected
        """
        report_obj.switch_ia_ribbon_tab('Format')
        utilobj.synchronize_until_element_is_visible(freeze_checked_css, 39)
        utilobj.verify_object_visible(freeze_checked_css, True, 'Step 21: Verify "Freeze" is selected.')
        
        """
        Step 22: Click Run > Verify Active Report output showing scrollbar
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.wait_for_visible_text(table_id_css, visble_element_text='TOTAL', time_out=90)
        expected_heading = ['ProductID', 'State', 'City', 'Category', 'DollarSales', 'BudgetDollars', 'TOTAL']
        active_rpt_obj.verify_column_heading(table_id_css_1, expected_heading, 'Step 22: Verify heading.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_step7.xlsx', 'Step 22.1: Verify data set', table_css=table_id_css_2, desired_no_of_rows=29)
        cell_obj = utilobj.validate_and_get_webdriver_object(table_row_css, 'Table last row cell')
        j_script.scrollIntoView(cell_obj)
        verify_page_summary('117of117records,Page1of3', 'Step 22.2: verify page summary.')
        utilobj.verify_object_visible(scroll_bar_css, True, "Step 22.3: Verify Active Report output showing scrollbar.")
        utilobj.verify_object_visible(scroll_bar_css_1, True, "Step 22.4: Verify Active Report output showing scrollbar.")
        report_obj.switch_to_default_content()
        
        """
        Step 23: Click on "Table" in the Format tab to deselect "Freeze"
        """
        report_obj.select_ia_ribbon_item('Format', 'Table')
        utilobj.synchronize_until_element_is_visible("#FormatTab #FormatReportTable.tool-bar-button-checked", 30)
        utilobj.verify_object_visible(freeze_checked_css, False, 'Step 23: Verify "Freeze" is not selected.')
        
        """
        Step 24: Click Run > Verify scrollbar is not displayed
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.wait_for_visible_text('#ITableData0', visble_element_text='TOTAL', time_out=90)
        active_rpt_obj.verify_active_report_dataset(case_id+'_step24.xlsx', 'Step 24.1: Verify data set', table_css="#ITableData0", desired_no_of_rows=29)
        cell_obj = utilobj.validate_and_get_webdriver_object("#ITableData0 tr:nth-child(57) td:nth-child(6)", 'Table last row cell')
        j_script.scrollIntoView(cell_obj)
        active_rpt_obj.verify_page_summary(0, '117of117records,Page1of3', 'Step 24.2: verify page summary.')
        utilobj.verify_object_visible(scroll_bar_css, False, "Step 24.3: Verify Active Report output showing scrollbar.")
        utilobj.verify_object_visible(scroll_bar_css_1, False, "Step 24.4: Verify Active Report output showing scrollbar.")
        report_obj.switch_to_default_content()
        
        """
        Step 25: Logout: Disregard changes
                 http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()