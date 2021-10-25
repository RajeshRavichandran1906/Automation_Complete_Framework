'''
Created on January 8, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2104971
TestCase Name = AHTML:Multi-Drill Down with Active Report and Chart shows duplicate options in the menu (ACT-593).
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools.active_report import Active_Report
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.wftools.chart import Chart
from common.lib import base

class C2104971_TestClass(BaseTestCase):

    def test_C2104971(self):
        
        """
        TESTCASE Object's
        """
        chart_obj = Chart(self.driver)
        active_chart_obj = Active_Chart(self.driver)
        active_report_obj = Active_Report(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        util_obj = UtillityMethods(self.driver)
        base_obj = base.BasePage(self.driver)
        
        """
        Test case CSS
        """
        PARENT_CSS = "#MAINTABLE_wbody0_fmg g.chartPanel"
        page_load_css= PARENT_CSS + " text[class*='xaxisOrdinal-labels!g2!mgroupLabel']"
        W_GERMANY_CSS = PARENT_CSS + " rect[class*='riser!s0!g0!mbar']"
        expected_url='https://www.ibi.com/'
        
        """
        Test case variables
        """
        expected_google_title = 'Google'
        expected_infobuild_title = 'DataandAnalyticsCompany|ibi'
        england_tooltip = ['COUNTRY:  ENGLAND', 'DEALER_COST:  37,853', 'Filter Chart', 'Exclude from Chart', 'IBI', 'Google']
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        
        """
        Step 1: Sign in to WebFOCUS as a basic user
        http://machine:port/{alias}
        Step 2: Run the existing fex using the below API link
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P95_S7063/G135480&BIP_item=act-593.fex
        """
        active_report_obj.run_active_report_using_api('act-593.fex', column_css=page_load_css, synchronize_visible_element_text='ITALY', repository_path=folder_path)
        active_chart_obj.verify_x_axis_title_in_run_window(['COUNTRY'], msg='Step 2')
        active_chart_obj.verify_y_axis_title_in_run_window(['DEALER_COST'], msg='Step 2.1')
        active_chart_obj.verify_chart_title('DEALER_COST by COUNTRY', msg='Step 2.2', parent_css='#MAINTABLE_wbody0_fmg')
        active_chart_obj.verify_x_axis_label_in_run_window(['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY'], msg='Step 2.3')
        active_chart_obj.verify_y_axis_label_in_run_window(['0', '10K', '20K', '30K', '40K', '50K', '60K'], msg='Step 2.4')
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 2.5')
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window(W_GERMANY_CSS, 'cerulean_blue', msg='Step 2.6')
        
        """
        Step 3: Hover over the bar for England.
        Expect to see the following menu of chart options appear.
        Expect to see only single entries, no duplicate menu items.    
        """
        chart_obj.verify_active_chart_tooltip('MAINTABLE_wbody0_f', 'riser!s0!g0!mbar!', england_tooltip, msg='Step 3.1: Verify England tooltip')
        
        """
        Step 4: From the menu, click the link for IBI.
        Expect to see the following output for the IBI link.
        Step 5: Click Close
        """
        active_chart_obj.select_tooltip_in_run_window('riser!s0!g0!mbar!', 'IBI')
        core_util_obj.switch_to_new_window()
        observed_title = self.driver.title.replace(' ','')
        util_obj.asin(expected_infobuild_title, observed_title, "Step 4.1: Verify the infobuild title")
        current_page_url=self.driver.current_url
        util_obj.asin(current_page_url,expected_url,"Step 4.1: verify the url")
        core_util_obj.switch_to_previous_window()
        
        """
        Step 6: Again hover over the bar for England.
        Step 7: From the menu, click the link for Google.
        Expect to see the following output for the Google link.
        """
        chart_obj.wait_for_visible_text(page_load_css, 'ITALY', base_obj.chart_medium_timesleep)
        active_chart_obj.select_tooltip_in_run_window('riser!s0!g0!mbar!', 'Google')
        core_util_obj.switch_to_new_window()
        chart_obj.wait_for_number_of_element("#gb .gb_g", 2, base_obj.chart_medium_timesleep)
        observed_title = self.driver.title
        util_obj.asequal(expected_google_title, observed_title, "Step 7.1: Verify the google title")
        
        """
        Step 8: Logout:
        http://machine:port/{alias}/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()