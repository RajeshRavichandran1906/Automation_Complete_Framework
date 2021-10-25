'''
Created on Jun 25, 2019

@author: Aftab

Test Case : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5823682
TestCase Name : Insight - Convert Chart to Report while Insight is enabled returns Action Failed error
'''

import unittest
from common.wftools.chart import Chart
from common.wftools import report
from common.lib.basetestcase import BaseTestCase

class C5823682_TestClass(BaseTestCase):

    def test_C5823682(self):
        
        """
            CLASS OBJECTS 
        """
        chart_obj= Chart(self.driver)
        report_obj = report.Report(self.driver)
                
        """
            TESTCASE ID Variable 
        """
        format_css = "#FormatTab"
        querypane_css = "#queryBoxColumn"
        case_id = 'C5823682'
        DATA_SET_NAME1 = case_id + '_DataSet_01.xlsx'
        DATA_SET_NAME2 = case_id + '_DataSet_02.xlsx'
        
        """
        1: Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
           http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP309_S10666%2FG169735&tool=chart&master=baseapp/wf_retail_lite
        """
        chart_obj.invoke_chart_tool_using_api("baseapp/wf_retail_lite")

        """
        2 : Double click fields "Product,Category", "Cost of Goods"
        """
        chart_obj.double_click_on_datetree_item('Product,Category', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Product,Category")
        chart_obj.double_click_on_datetree_item('Cost of Goods', 1)
        chart_obj.wait_for_visible_text(querypane_css,"Cost of Goods")
 
        """
        2:01: Verify the canvas,
        """
        chart_obj.verify_number_of_risers('#pfjTableChart_1 rect', 1, 7, msg='Step 2.01')
        
        """
        3 : Select the Format Tab
        4 : Click "Insight" (Under 'Run with' group)
        """
        chart_obj.select_ia_ribbon_item("Format", "run_with")
        chart_obj.wait_for_visible_text(format_css, "Run with")
        chart_obj.select_ia_ribbon_item("Format", "insight") 
        
        """
        5 : Select "Report" under the Format Tab to convert Chart to Report
        """
        chart_obj.select_ia_ribbon_item("Format", "report")
        chart_obj.wait_for_visible_text(format_css, "Destination")
        
        """
        6 : Verify no error is displayed, verify fields from original chart are displayed in the Report
        """
        #report_obj.create_acrossreport_data_set_in_preview('TableChart_1', 2, 2, 7, 2, DATA_SET_NAME1)
        report_obj.verify_across_report_data_set_in_preview('TableChart_1', 2, 2, 7, 2, DATA_SET_NAME1, msg="Verify report data")

        """
        7 : Select Save from QAT
        8 : Enter "C5823682" in title
        9 : Click Save
        """
        chart_obj.select_item_in_top_toolbar('save')
        chart_obj.save_file_in_save_dialog('C5823682')        
        
        """
        10 : Logout:
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart_obj.api_logout()
 
        """
        11 : Restore the saved Fex:
        http://machine:port/ibi_apps/ia?item=IBFS:/WFC/Repository/P309_S10666/G169735/C5823682.fex&tool=Report
        """
        report_obj.edit_fex_using_api_url('C5823682')

        """
        12 : Verify the canvas
        """
        #report_obj.create_acrossreport_data_set_in_preview('TableChart_1', 2, 2, 7, 2, DATA_SET_NAME2)
        report_obj.verify_across_report_data_set_in_preview('TableChart_1', 2, 2, 7, 2, DATA_SET_NAME2, msg="Verify report data")

        """
        13 : Logout:
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        report_obj.api_logout()
        
if __name__ == '__main__':
    unittest.main()