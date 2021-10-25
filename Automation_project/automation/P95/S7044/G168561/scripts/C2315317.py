'''
Created on January 16, 2019

@author: AA14564

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2315317
TestCase Name = Verify Page Information Status bar Alignment and Location.
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.active_report import Active_Report
from common.wftools.report import Report 
from common.wftools.chart import Chart

class C2315317_TestClass(BaseTestCase):

    def test_C2315317(self):
        
        """
        Test case Object's
        """
        util_obj = UtillityMethods(self.driver)
        active_rpt_obj=Active_Report(self.driver)
        report_obj=Report(self.driver)
        chart_obj=Chart(self.driver)
        
        '''
        Variables
        '''
        case_id = 'C2315317'
        tab_name = 'General'
        
        '''
        Css Variables
        '''
        page_load_css = "#TableChart_1"
        pagination_table_css = "table[id='IWindowBody0'] .arGridBar table>tbody> tr > td{0}"
        pagination_css = pagination_table_css.format("[align]")
        pagination_toggle_css = pagination_table_css.format(" span[onclick*='toggle']")
        table_css="#ITableData0"
        expected_summary_value = '18of18records,Page1of1'
        window_alignment_css = "[id^='QbDialog'] .active.window #pageInfoPropsBox #{0}"
        display_page_information_css = "[id^='QbDialog'] .active.window #generalPane #displayPageInfoCheckbox input"
        
        """       
        Step 1: Launch IA Report using below API link
                http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7044/G168561
        """
        active_rpt_obj.invoke_report_tool_using_api('ibisamp/car', mrid='mriddev', mrpass='mrpassdev')
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='Draganddropfieldsontothecanvasorintothequerypanetobeginbuildingyourreport', time_out=chart_obj.home_page_long_timesleep)
        
        """
        Step 2: Add fields COUNTRY, CAR, MODEL, SEATS.
                Select Active Report as the output option.
                Expect to see the following report Preview pane.
        """
        chart_obj.double_click_on_datetree_item('COUNTRY', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='COUNTRY', time_out=chart_obj.home_page_medium_timesleep)
        chart_obj.double_click_on_datetree_item('CAR', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='CAR', time_out=chart_obj.home_page_medium_timesleep)
        chart_obj.double_click_on_datetree_item('MODEL', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='MODEL', time_out=chart_obj.home_page_medium_timesleep)
        chart_obj.double_click_on_datetree_item('SEATS', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='SEATS', time_out=chart_obj.home_page_medium_timesleep)
        chart_obj.change_output_format_type('active_report')
        report_obj.verify_report_titles_on_preview(4, 4, page_load_css[1:], ['COUNTRY', 'CAR', 'MODEL', 'SEATS'], 'Step 2')
        report_obj.verify_report_data_set_in_preview(page_load_css[1:], 17, 4, case_id+'_Ds01.xlsx', 'Step 2: Verify data set.')
        
        """
        Step 3: Click the Run button.
                Scroll to the bottom of the report.
                Expect to see the default alignment of the Page information bar, left-justified under the report.
        """
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.verify_page_summary(0, expected_summary_value, 'Step 3: Verify page summary.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_Ds02.xlsx', 'Step 3.1: Verify data set.', table_css=table_css)
        left_align = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(pagination_css, 'Page Summary'), 'align')
        util_obj.asequal('LEFT', left_align, 'Step 3.2: Expect to see the default alignment of the Page information bar, left-justified under the report.')
        report_obj.switch_to_default_content()
        
        """
        Step 4: Click the Format tab.
                Select Active Report Options.
                In the Page Information area, click the middle alignment option.
                Expect to see the middle alignment option selected for centering.
        """
        report_obj.select_ia_ribbon_item('Format', 'active_report_options')
        active_rpt_obj.wait_for_number_of_element(window_alignment_css.format('Center'), 1, chart_obj.report_short_timesleep)
        active_rpt_obj.active_report_options(tab_name, general_alignment_center=True)
        time.sleep(2)
        util_obj.verify_object_visible(window_alignment_css.format('Center')+'.tool-bar-button-checked', True, 'Step 4: Expect to see the middle alignment option selected for centering.')
        
        """
        Step 5: Click the OK button.
                Click the Run button.
                Scroll to the bottom of the report.
                Expect to see the alignment of the Page information bar, centered, under the report.
        """
        active_rpt_obj.active_report_options(tab_name, btnOk=True)
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.verify_page_summary(0, expected_summary_value, 'Step 5: Verify page summary.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_Ds02.xlsx', 'Step 5.1: Verify data set.', table_css=table_css)
        center_align = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(pagination_css, 'Page Summary'), 'align')
        util_obj.asequal('CENTER', center_align, 'Step 5.2: Expect to see the alignment of the Page information bar, centered, under the report.')
        report_obj.switch_to_default_content()
        
        """
        Step 6: Click the Format tab.
                Select Active Report Options.
                In the Page Information area, click the right-justify alignment option.
                Expect to see the right most alignment option selected for right-justify.
        """
        report_obj.select_ia_ribbon_item('Format', 'active_report_options')
        active_rpt_obj.wait_for_number_of_element(window_alignment_css.format('Center'), 1, chart_obj.report_short_timesleep)
        active_rpt_obj.active_report_options(tab_name, general_alignment_right=True)
        time.sleep(2)
        util_obj.verify_object_visible(window_alignment_css.format('Right')+'.tool-bar-button-checked', True, 'Step 6: Expect to see the right most alignment option selected for right-justify.')
        
        """
        Step 7: Click the OK button.
                Click the Run button.
                Scroll to the bottom of the report.
                Expect to see the alignment of the Page information bar, right-justified, under the report.
        """
        active_rpt_obj.active_report_options(tab_name, btnOk=True)
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.verify_page_summary(0, expected_summary_value, 'Step 7: Verify page summary.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_Ds02.xlsx', 'Step 7.1: Verify data set.', table_css=table_css)
        center_align = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(pagination_css, 'Page Summary'), 'align')
        util_obj.asequal('RIGHT', center_align, 'Step 7.2: Expect to see the alignment of the Page information bar, right-justified, under the report.')
        report_obj.switch_to_default_content()
        
        """
        Step 8: Click the Format tab.
                Select Active Report Options.
                Below the Alignment option, change the Location to Top Row, from the default Bottom Row.
                Expect to see the following Page Location option changed to Top Row.
        """
        report_obj.select_ia_ribbon_item('Format', 'active_report_options')
        active_rpt_obj.wait_for_number_of_element(window_alignment_css.format('Center'), 1, chart_obj.report_short_timesleep)
        active_rpt_obj.active_report_options(tab_name, general_location='Top Row')
        time.sleep(2)
        location = util_obj.validate_and_get_webdriver_object(window_alignment_css.format('pageLocationCombo'), 'Location drop down').text.strip()
        util_obj.asequal('Top Row', location, 'Step 8: Expect to see the following Page Location option changed to Top Row.')
        
        """
        Step 9: Click the OK button.
                Click the Run button.
                Expect to see the Page information on the Top Row and still right-justified.
        """
        active_rpt_obj.active_report_options(tab_name, btnOk=True)
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.verify_page_summary(0, expected_summary_value, 'Step 9: Verify page summary.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_Ds02.xlsx', 'Step 9.1: Verify data set.', table_css=table_css)
        toggle_align = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(pagination_toggle_css, 'Page Summary'), 'title')
        util_obj.asequal('Move to Bottom', toggle_align, 'Step 9.2: Expect to see the Page information on the Top Row.')
        center_align = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(pagination_css, 'Page Summary'), 'align')
        util_obj.asequal('RIGHT', center_align, 'Step 9.3: Expect to see the alignment of the Page information bar, right-justified.')
        report_obj.switch_to_default_content()
        
        """
        Step 10: Click the Format tab.
                Select Active Report Options.
                In the Page Information area, uncheck the Display Page Information option.
                Expect to see the Display Page Information unchecked and the Alignment options grayed out.
        """
        report_obj.select_ia_ribbon_item('Format', 'active_report_options')
        active_rpt_obj.wait_for_number_of_element(window_alignment_css.format('Center'), 1, chart_obj.report_short_timesleep)
        active_rpt_obj.active_report_options(tab_name, general_display_page_info=True)
        time.sleep(2)
        page_status = util_obj.validate_and_get_webdriver_object(display_page_information_css, 'Display Page Information').is_selected()
        util_obj.asequal(False, page_status, 'Step 10: Expect to see the Display Page Information option is unchecked.')
        util_obj.verify_object_visible(window_alignment_css.format("Left[disabled='true']"), True, "Step 10.1: Verify the Alignment options 'Left' is grayed out")
        util_obj.verify_object_visible(window_alignment_css.format("Center[disabled='true']"), True, "Step 10.2: Verify the Alignment options 'Center' is grayed out")
        util_obj.verify_object_visible(window_alignment_css.format("Right[disabled='true']"), True, "Step 10.3: Verify the Alignment options 'Right' is grayed out")
        
        """
        Step 11: Click the OK button.
                Click the Run button.
                Expect to see the Page information removed entirely from the Active Report.
        """
        active_rpt_obj.active_report_options(tab_name, btnOk=True)
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.wait_for_visible_text(table_css, visble_element_text='ENGLAND', time_out=active_rpt_obj.home_page_medium_timesleep)
        try:
            util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(pagination_toggle_css, 'Page Summary'), 'title')
            page_status = False
        except AttributeError:
            page_status = True
        util_obj.asequal(True, page_status, 'Step 11: Expect to see the Page information removed entirely from the Active Report.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_Ds02.xlsx', 'Step 11.1: Verify data set.', table_css=table_css)
        report_obj.switch_to_default_content()
        
        """
        Step 12: Logout using the below link:
                http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()