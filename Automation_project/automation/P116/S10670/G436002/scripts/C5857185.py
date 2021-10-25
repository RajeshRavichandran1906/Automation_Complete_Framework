'''
Created on Jan 3, 2019

@author: Vpriya

Test Case =  http://172.19.2.180/testrail/index.php?/suites/view/10670&group_by=cases:section_id&group_id=436002&group_order=asc
TestCase Name = AHTML:JSCHART: Advanced Chart types icons are not shown - 142140
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import active_report
from common.wftools import active_chart
from common.lib.core_utility import CoreUtillityMethods

class C5857185_TestClass(BaseTestCase):

    def test_C5857185(self):
        
        """
            TESTCASE VARIABLES
        """
        active_report_obj=active_report.Active_Report(self.driver)
        active_chart_obj=active_chart.Active_Chart(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        folder_path = '{0}_{1}/{2}'.format(project_id, suite_id, group_id)
        page_load_css = '#ITableData0 tr:nth-child(1) td:nth-child(1)'
        fex_name="142140.fex"
        
        """
        Step:01Login to WebFOCUS environment using the below link:
        http://machine:port/{alias}
        """ 
        """
        Step:02
        Run the 142140.fex using the below API link:
        http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS:/WFC/Repository/P116_S10032/G168200&BIP_item=142140.fex
        """
        active_report_obj.run_active_report_using_api(fex_name, column_css=page_load_css, synchronize_visible_element_text='COUNTRY', repository_path=folder_path)
        
        """
        Step:03
        Once report opened click on any field eg: Seats click dropdown and select Chart/Rollup Tool
        """
        active_report_obj.select_menu_items('ITableData0', 3,'Chart/Rollup Tool')
        
        """
        Step:04
        Now click on Chart button from Chart/Rollup Tool.
        """
        active_chart_obj.select_chart_rollup_tab('Charts')
        
        """
        Step:05
        Verify the chart type icons are visible.
        """
        active_chart_obj.verify_items_in_advanced_chart_menu(['Bar','Stacked Bar','Percent Bar','Column','StackedColumn','PercentColumn','Column Depth'], 'asin', 'Step 3.1: Verify bar under the advanced chart menu')
        
        """
        Step:06
        Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        """



if __name__ == '__main__':
    unittest.main()