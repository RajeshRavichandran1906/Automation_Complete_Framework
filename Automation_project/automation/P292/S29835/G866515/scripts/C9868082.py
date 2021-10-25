"""--------------------------------------------------------
Author Name : Prabhakaran.
Automated On : 16-September-2019
--------------------------------------------------------"""
from common.wftools.chart import Chart
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase

class C9868082_TestClass(BaseTestCase):

    def test_C9868082(self):
        
        """
            CLASS OBJECTS 
        """
        utils = UtillityMethods(self.driver)
        chart = Chart(self.driver)
        
        """
            VARIABLES
        """
        preview_chart_css = "#TableChart_1"
        run_chart_css = "#jschart_HOLD_0"
        case_id = "C9868082"
        
        """
            STEP 01 : Launch the IA API with chart in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG866514%2F&master=iibisamp%2Fcar&tool=chart
        """
        chart.invoke_chart_tool_using_api("ibisamp/car")
        chart.wait_for_visible_text(preview_chart_css, "Group", chart.chart_long_timesleep)
        
        """
            STEP 02 : Click Format tab > Other > HTML5 extension > Hover over on Sparkline KPI chart
            STEP 03 : Select "Sparkline KPI" > OK
        """
        chart.select_ia_ribbon_item('Format', 'other')
        chart.select_other_chart_type('html5_extension', 'sparkline', 18, verify_selection=False, verify_tooltip='Sparkline KPI')
        chart.wait_for_visible_text(preview_chart_css, 'measures', chart.chart_medium_timesleep)
        
        """
            STEP 03 - Expected : The following chart displayed.
        """
        expected_text = "Revenue+37% LY\n431.7M\nAdd more measures or dimensions"
        actual_text = self.driver.find_element_by_css_selector(preview_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, "Step 03.01 : Verify 'Spark Line' chart text")
        
        """
            STEP 04 : Double click "Country", Drag and drop "Car" to X-Axis, Double click "Dealer_cost" to Measure
        """
        chart.double_click_on_datetree_item('COUNTRY', 1)
        chart.drag_field_from_data_tree_to_query_pane('CAR', 1, 'X-Axis')
        chart.double_click_on_datetree_item('DEALER_COST', 1)
        chart.wait_for_visible_text(preview_chart_css, 'DEALER_COST', chart.chart_medium_timesleep)
        
        """
            STEP 04 - Expected : Fields added to appropriate bucket and canvas updated.
        """
        expected_text = "DEALER_COST+88% COUNTRY\n37.9k"
        query_fields = ['Chart (car)', 'Extension specific buckets', 'Measure', 'DEALER_COST', 'Compare Group', 'COUNTRY', 'X-Axis', 'CAR', 'Multi-graph']
        chart.verify_all_fields_in_query_pane(query_fields, "Step 04.01 : Verify Fields added to appropriate bucket")
        actual_text = self.driver.find_element_by_css_selector(preview_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, "Step 04.02 : Verify 'Spark Line' chart text")
        
        """
            STEP 05 : Click Run button
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(run_chart_css, 'DEALER_COST', chart.chart_medium_timesleep)
        
        """
            STEP 05 - Expected : Chart displayed in run time without error.
        """
        actual_text = self.driver.find_element_by_css_selector(run_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, "Step 05.01 : Verify 'Spark Line' chart text")
        
        """
            STEP 06 : Hover over on risers
            Tooltip value displayed.
        """
        chart.verify_sparkline_chart_tooltip('18,621', '06.01', chart_location='middle_left', xoffset=2)
        chart.switch_to_default_content()
        
        """
            STEP 07 : Click Save icon from the toolbar > Enter title as "C9868082" > Click Save 
        """
        chart.select_ia_toolbar_item('toolbar_save')
        chart.save_file_in_save_dialog(case_id)
        
        """
            STEP 08 : Logout using API - http://machine:port/alias/service/wf_security_logout.jsp
        """
        chart.logout_chart_using_api()
        
        """
            STEP 09 : Run C6390406.fex from domain tree using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S29835%252FG866514%252F&BIP_item=C9868082.fex
        """
        chart.run_fex_using_api_url("P292_S29835/G866514", case_id, mrid='mrid', mrpass='mrpass')
        chart.wait_for_visible_text(run_chart_css, 'DEALER_COST', chart.chart_long_timesleep)
        
        """
            STEP 09 - Expected : Chart displayed in run time window.
        """
        actual_text = self.driver.find_element_by_css_selector(run_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, "Step 09.01 : Verify 'Spark Line' chart text")
        
        """
            STEP 10 : Logout using API
        """
        chart.logout_chart_using_api()
        
        """
            STEP 11 : Restore the fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain:port/alias/ia?is508=false&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG866514%2FC6390406.fex
        """
        chart.edit_fex_using_api_url(None, fex_name=case_id)
        chart.wait_for_visible_text(preview_chart_css, 'DEALER_COST', chart.chart_long_timesleep)
        
        """
            STEP 11 - Expected : Chart restored successfully without error.
        """
        expected_text = "DEALER_COST+88% COUNTRY\n37.9k"
        query_fields = ['Chart (car)', 'Extension specific buckets', 'Measure', 'DEALER_COST', 'Compare Group', 'COUNTRY', 'X-Axis', 'CAR', 'Multi-graph']
        chart.verify_all_fields_in_query_pane(query_fields, "Step 11.01 : Verify Fields added to appropriate bucket")
        actual_text = self.driver.find_element_by_css_selector(preview_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, "Step 11.02 : Verify 'Spark Line' chart text")
        
        """
            STEP 12 : Logout using API
        """
        chart.logout_chart_using_api()