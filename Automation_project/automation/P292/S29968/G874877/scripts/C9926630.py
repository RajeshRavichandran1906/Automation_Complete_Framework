"""-------------------------------------------------------------------------------------------
Created on September 13, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/9926630
Test Case Title =  HTML5 chart extension with Sparkline KPI Large
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.chart import Chart
import time

class C9926630_TestClass(BaseTestCase):

    def test_C9926630(self):
        
        """
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        preview_chart_css = "#TableChart_1"
        ok_button_css = "#qbSelectChartTypeDlgOkBtn"
        querytree_css = "#queryTreeWindow"
        
        """
            STEP 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29968%2FG874876%2F&master=ibisamp%2Fcar&tool=chart
        """
        chart.invoke_chart_tool_using_api("ibisamp/car")
        chart.wait_for_visible_text(preview_chart_css, "Group", chart.chart_long_timesleep)
        
        """
            STEP 02 : Click Format tab > Other > HTML5 extension > Hover over on KPI with Sparkline Large chart
            Tooltip displayed "KPI with Sparkline large"
        """
        chart.select_ia_ribbon_item("Format", "other")
        chart.wait_for_visible_text(ok_button_css, "OK")
        chart.select_other_chart_type("html5_extension", "kpi_with_sparkline", 19, verify_selection = False, verify_tooltip = "KPI with Sparkline Large")
        chart.wait_for_visible_text("#pfjTableChart_1", "Add")
        
        """
            STEP 03 : Select "KPI with Sparkline Large" > Click OK button.
            The following chart displayed.
        """
        utils.verify_picture_using_sikuli("C9926630_step3.png", "Step 03.01 : The following chart displayed.")
        
        """
            STEP 04 : Double click "Country" field to add "Group" bucket
            Drag and drop "Car" to X-Axis bucket
            Double click "Dealer_cost" to add "Key Measure" bucket
            Fields added to appropriate bucket and canvas updated.
        """
        chart.double_click_on_datetree_item("COUNTRY", 1)
        chart.wait_for_visible_text(querytree_css, "COUNTRY")
        
        chart.drag_field_from_data_tree_to_query_pane("CAR", 1, "X-Axis", 1)
        chart.wait_for_visible_text(querytree_css, "CAR")
        
        chart.double_click_on_datetree_item("DEALER_COST", 1)
        chart.wait_for_visible_text(querytree_css, "DEALER_COST")
        
        chart.verify_all_fields_in_query_pane(['Chart (car)', 'Extension specific buckets', 'Key Measure', 'DEALER_COST', 'Group', 'COUNTRY', 'X-Axis', 'CAR', 'Multi-graph'], msg = 'Step 04.01 : Fields added to appropriate bucket and canvas updated.')
        
        chart_obj = utils.validate_and_get_webdriver_object("#pfjTableChart_1", "Chart css")
        actual_result = chart_obj.text
        msg = "Step 04.02 : Fields added to appropriate bucket and canvas updated."
        expected_result = 'ENGLANDFRANCEITALYJAPANW GERMANY\nDEALER_COST CAR 37.9k'
        utils.asequal(expected_result, actual_result, msg)
        
        utils.verify_picture_using_sikuli("C9926630_step4.png", "Step 04.03 : Fields added to appropriate bucket and canvas updated.")
        
        """
            STEP 05 : Click Run button.
            Chart displayed in run time without error.
        """
        chart.run_chart_from_toptoolbar()
        utils.verify_picture_using_sikuli("C9926630_step4.png", "Step 05.01 : Chart displayed in run time without error.")
        chart.switch_to_frame()
        chart.wait_for_visible_text("#jschart_HOLD_0", "ENGLAND")
        
        """
            STEP 06 : Select "JAPAN" link
            The following output displayed for JAPAN value.
        """ 
        japanlink_obj = utils.validate_and_get_webdriver_object('#jschart_HOLD_0 div[class="kpi-table-nav"] a[class="kpi-table-nav-pill"]:nth-child(4)', "Japan link css")
        core_utils.python_left_click(japanlink_obj)
        time.sleep(10)
        chart.switch_to_default_content()
        utils.verify_picture_using_sikuli("C9926630_step6.png", "Step 06.01 : The following output displayed for JAPAN value")
        
        """
            STEP 07 : Click Save icon from the toolbar > Enter title as "C6390407" > Click Save button.
        """
        chart.select_item_in_top_toolbar("save")
        chart.wait_for_visible_text("#IbfsOpenFileDialog7_btnCancel", "Cancel")
        
        chart.save_file_in_save_dialog("C6390407")
        utils.synchronize_until_element_disappear("#IbfsOpenFileDialog7_btnCancel", 10)
        
        """
            STEP 08 : Logout using API   
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        
        """
            STEP 09 : Run C6390407.fex from domain tree using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S11397%252FG435181%252F&BIP_item=C6390407.fex
            Chart displayed in run window.
        """
        chart.run_fex_using_api_url("P292_S29835/G866514", "C6390407", mrid = "mrid", mrpass = "mrpass")
        chart.wait_for_visible_text("#jschart_HOLD_0", "ENGLAND")
        
        utils.verify_picture_using_sikuli("C9926630_step9.png", "Step 09.01 : Chart displayed in run window")
        
        """
            STEP 10 : Hover over on risers
            Tooltip value displayed
        """
        chart.verify_sparkline_chart_tooltip("18,621", "10.01", chart_location='middle_left', xoffset=4)
        
        """
            STEP 11 : Logout using API
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        
        """
            STEP 12 : Restore C6390407.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S11397%2FG435181%2FC6390407.fex
            Chart restored successfully without error.
        """
        chart.edit_fex_using_api_url("P292_S29835/G866514", fex_name = "C6390407", mrid = "mrid", mrpass = "mrpass")
        chart.wait_for_visible_text("#pfjTableChart_1", "ENGLAND")
        
        utils.verify_picture_using_sikuli("C9926630_step4.png", "Step 12.01 : Chart restored successfully without error")
        
        """
            STEP 13 : Logout using AP
            http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.api_logout()
        
if __name__ == '__main__':
    unittest.main()