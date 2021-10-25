'''
Created on May 5th, 2018

@author: BM13368
Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10032&group_by=cases:section_id&group_order=asc&group_id=157266
TestCase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2511617
TestCase Name : Report:Verify that user is able to run a simple AHTML report
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.pages import visualization_resultarea,active_miscelaneous, active_chart_rollup
from common.wftools import active_report
from common.lib import utillity

class C2511617_TestClass(BaseTestCase):

    def test_C2511617(self):
        """
        TESTCASE VARIABLES
        """
        result_obj = visualization_resultarea.Visualization_Resultarea(self.driver)
        miscelanousobj =active_miscelaneous.Active_Miscelaneous(self.driver)
        active_reportobj=active_report.Active_Report(self.driver)
        active_chartrollupobj=active_chart_rollup.Active_Chart_Rollup(self.driver)
        utillobj=utillity.UtillityMethods(self.driver)
        fex_name ="AHTML_JSCHART.fex"
        
        """
            Step 1:Sign in to WebFOCUS as a Basic user
            http://machine:port/{alias}
            Step 2:Expand folder P292_S10032_G193334
            Execute the following URL:
            http://machine:port/{alias}/run.bip?BIP_REQUEST_TYPE=BIP_RUN&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S10032_G193334%252FAHTMLON&BIP_item=AHTML_JSCHART.fex
        """
        active_reportobj.run_active_report_using_api(fex_name, column_css="#MAINTABLE_wbody0_f [class='xaxisOrdinal-title']", synchronize_visible_element_text="COUNTRY")
        
        """
            Step 3:Verify the report is generated.
            Verify the Bar Chart contains pairs of Bars for each Country.
            Chart toolbar is present on the top.
        """
        result_obj.verify_number_of_risers("#MAINTABLE_wbody0_f rect", 1, 20, "Step 03:01: Verify number of risers")
        result_obj.verify_xaxis_title("MAINTABLE_wbody0_f", "COUNTRY", "Step 03:02: Verify x-axis title")
        result_obj.verify_legends(['DEALER_COST','RETAIL_COST'], "#MAINTABLE_wbody0_f", msg="Step 03:03:Verify chart legends")
        expected_label_list=['0','10K','20K','30K','40K','50K','60K']
        result_obj.verify_xyz_labels(expected_label_list, "#MAINTABLE_wbody0_f", "[class*='yaxis-labels']", msg="Step 03:04:Verify y-axis labels")
        expected_xaxis_label_list=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        result_obj.verify_xyz_labels(expected_xaxis_label_list, "#MAINTABLE_wbody0_f", "[class^='xaxisOrdinal-labels']", msg="Step 03:05:Verify x-axis labels")
        expected_toolbar_menu_list=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        miscelanousobj.verify_acitive_chart_toolbar("#MAINTABLE_wmenu0", expected_toolbar_menu_list, "Step 03:06:Verify active chart toolbarmenu")
        miscelanousobj.verify_chart_title_("#MAINTABLE_wbody0_ft", "DEALER_COST, RETAIL_COST by COUNTRY", "Step 03:07:Verify chart title")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 03:08:Verify bar color")
        
        """
            Step 4:Click on first icon and select Add Y > RETAIL_COST to remove that field from the chart.
            Verify user is able to remove Y-axis fields.
        """
        
        active_chartrollupobj.select_chartmenubar_option('MAINTABLE_0', 0, 'Add (Y)->RETAIL_COST', 0, custom_css='cpop')
        
        """
        Verify only Dealer_Cost is displayed on Bar chart.
        """
        result_obj.verify_number_of_risers("#MAINTABLE_wbody0_f rect", 1, 10, "Step 03:01: Verify number of risers")
        result_obj.verify_legends(['DEALER_COST'], "#MAINTABLE_wbody0_f", msg="Step 03:02:Verify chart legends")
        expected_label_list=['0','10K','20K','30K','40K','50K','60K']
        result_obj.verify_xyz_labels(expected_label_list, "#MAINTABLE_wbody0_f", "[class*='yaxis-labels']", msg="Step 03:03:Verify y-axis labels")
        expected_xaxis_label_list=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        result_obj.verify_xyz_labels(expected_xaxis_label_list, "#MAINTABLE_wbody0_f", "[class^='xaxisOrdinal-labels']", msg="Step 03:04:Verify x-axis labels")
        expected_toolbar_menu_list=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        miscelanousobj.verify_acitive_chart_toolbar("#MAINTABLE_wmenu0", expected_toolbar_menu_list, "Step 03:05:Verify active chart toolbarmenu")
        miscelanousobj.verify_chart_title_("#MAINTABLE_wbody0_ft", "DEALER_COST by COUNTRY", "Step 03:06:Verify chart title")
        utillobj.verify_chart_color("MAINTABLE_wbody0_f", "riser!s0!g0!mbar!", "cerulean_blue", "Step 03:07:Verify bar color")
        
        """
            Step 5:Click Scatter chart option from the toolbar.
            Verify chart type is changed from Bar to Scatter without any error.
        """
        active_chartrollupobj.click_chart_menu_bar_items('MAINTABLE_wmenu0', 4)
        result_obj.verify_number_of_risers("#MAINTABLE_wbody0_f path[class^='riser']", 1, 5, "Step 05:01: Verify number of risers")
        result_obj.verify_legends(['DEALER_COST'], "#MAINTABLE_wbody0_f", msg="Step 05:02:Verify chart legends")
        expected_label_list=['0','10K','20K','30K','40K','50K','60K']
        result_obj.verify_xyz_labels(expected_label_list, "#MAINTABLE_wbody0_f", "[class*='yaxis-labels']", msg="Step 05:03:Verify y-axis labels")
        expected_xaxis_label_list=['ENGLAND','FRANCE','ITALY','JAPAN','W GERMANY']
        result_obj.verify_xyz_labels(expected_xaxis_label_list, "#MAINTABLE_wbody0_f", "[class^='xaxisOrdinal-labels']", msg="Step 05:04:Verify x-axis labels")
        expected_toolbar_menu_list=['More Options', 'Column', 'Pie', 'Line', 'Scatter', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum']
        miscelanousobj.verify_acitive_chart_toolbar("#MAINTABLE_wmenu0", expected_toolbar_menu_list, "Step 05:05:Verify active chart toolbarmenu")
        miscelanousobj.verify_chart_title_("#MAINTABLE_wbody0_ft", "DEALER_COST by COUNTRY", "Step 05:06:Verify chart title")
        
        """
            Step 6:Dismiss the window and logout.
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == "__main__":
    unittest.main()