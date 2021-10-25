'''
Created on Jan 3, 2019

@author: Varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5857186
TestCase Name = AHTML:JSCHART: few advanced chart types throws error - 144459
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.lib.core_utility import CoreUtillityMethods
from common.lib.base import BasePage

class C5857186_TestClass(BaseTestCase):

    def test_C5857186(self):
        """
        TESTCASE Object's
        """
        base_obj = BasePage(self.driver)
        active_chart_obj = Active_Chart(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case variables
        """
        advanced_items = ['Column','StackedColumn','PercentColumn','Column Depth','Stacked Depth','Percent Depth','3D Column']
        project = core_util_obj.parseinitfile('project_id')
        suite = core_util_obj.parseinitfile('suite_id')
        group = core_util_obj.parseinitfile('group_id')
        folder_path = "{0}_{1}/{2}".format(project, suite, group)
        
        """
        Test case css
        """
        chart_tool_css = "#wall1 div[id^='chticon']"
        
        """ 
        Step 1: Login to WebFOCUS environment using the below link:
        http://machine:port/{alias}
        Step 2: Run the 144459.fex using the below API link:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S10032/G168200&BIP_item=142140.fex
        """
        active_chart_obj.run_fex_using_api_url(folder_path,fex_name='144459', mrid='mrid', mrpass='mrpass')
        
        """
        Step 3: Click advanced chart icon from chart window toolbar.
        """
        active_chart_obj.click_chart_menu_bar_items('MAINTABLE_0', 5)
        
        """
        Step 4: Select chart tab
        """
        active_chart_obj.select_chart_rollup_tab('Charts')
        active_chart_obj.wait_for_number_of_element(chart_tool_css, 35, base_obj.chart_short_timesleep)
        
        """
        Step 5: Verify that below charts displayed clearly without an error.
        """
        active_chart_obj.verify_items_in_advanced_chart_menu(advanced_items,'asin','Step 5.1: Verify Advanced chart')
        
        """
        Step 6: Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()