'''
Created on January 17, 2019

@author: AA14564

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2315318
TestCase Name = Verify HTML5 is no longer available in the Active Report Options menu.
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.active_report import Active_Report
from common.wftools.report import Report
from common.wftools.chart import Chart

class C2315318_TestClass(BaseTestCase):

    def test_C2315318(self):
        
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
        case_id = 'C2315318'
        tab_name = 'General'
        
        '''
        Css Variables
        '''
        page_load_css = "#TableChart_1"
        table_css="#ITableData0"
        expected_summary_value = '10of10records,Page1of1'
        window_alignment_css = "[id^='QbDialog'] .active.window #pageInfoPropsBox #{0}"
        chart_type_css = "[id^='QbDialog'] .active.window #generalPane #dpChartOptions"
        
        """       
        Step 1: Launch IA Report using below API link
                http://machine:port/{alias}/ia?tool=Report&master=ibisamp/car&item=IBFS:/WFC/Repository/P95_S7044/G168561
        """
        active_rpt_obj.invoke_report_tool_using_api('ibisamp/car', mrid='mriddev', mrpass='mrpassdev')
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='Draganddropfieldsontothecanvasorintothequerypanetobeginbuildingyourreport', time_out=chart_obj.home_page_long_timesleep)
        
        """
        Step 2: Add fields CAR & DEALER_COST.
                Select Active Report as the output option.
                Expect to see the following report Preview pane.
        """
        chart_obj.double_click_on_datetree_item('CAR', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='CAR', time_out=chart_obj.home_page_medium_timesleep)
        chart_obj.double_click_on_datetree_item('DEALER_COST', 1)
        active_rpt_obj.wait_for_visible_text(page_load_css, visble_element_text='DEALER_COST', time_out=chart_obj.home_page_medium_timesleep)
        chart_obj.change_output_format_type('active_report')
        report_obj.verify_report_titles_on_preview(2, 2, page_load_css[1:], ['CAR', 'DEALER_COST'], 'Step 2')
        report_obj.verify_report_data_set_in_preview(page_load_css[1:], 10, 2, case_id+'_Ds01.xlsx', 'Step 2: Verify data set.')
        
        """
        Step 3: Click the Format tab, then select Active Report options.
                Verify that there is no option for Chart types.
                The option is no longer available in 82xx.
        """
        report_obj.select_ia_ribbon_item('Format', 'active_report_options')
        active_rpt_obj.wait_for_number_of_element(window_alignment_css.format('Center'), 1, chart_obj.report_short_timesleep)
        chart_type_status = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(chart_type_css, 'Chart type'), 'visibility')
        util_obj.asequal('hidden', chart_type_status, 'Step 3: Verify that there is no option for Chart types.')
        
        """
        Step 4: Click the OK button.
                Click the Run button.
                Expect to see the following Active Report.
        """
        active_rpt_obj.active_report_options(tab_name, btnOk=True)
        report_obj.run_report_from_toptoolbar()
        report_obj.switch_to_frame()
        active_rpt_obj.verify_page_summary(0, expected_summary_value, 'Step 4: Verify page summary.')
        active_rpt_obj.verify_active_report_dataset(case_id+'_Ds02.xlsx', 'Step 4.1: Verify data set.', table_css=table_css)
        report_obj.switch_to_default_content()
        
        """
        Step 5: Click the View Code tab at the top.
                Scroll to the bottom of the code.
                Verify that the default chart engine is JSCHART by the presence of the statement:
                ARGRAPHENGINE=JSCHART
        """
        report_obj.verify_fexcode_syntax('ARGRAPHENGINE=JSCHART', "Step 5: Verify that the default chart engine is JSCHART by the presence of the statement: 'ARGRAPHENGINE=JSCHART'.")
        
        """
        Step 6: Logout using the below link:
                http://machine:port/{alias}/service/wf_security_logout.jsp 
        """
        time.sleep(3)
        
if __name__ == '__main__':
    unittest.main()