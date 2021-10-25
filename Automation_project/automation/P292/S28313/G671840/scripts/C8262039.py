"""----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------"""

from common.wftools.designer_chart import Designer_Chart
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.chart import Chart

class C8262039_TestClass(BaseTestCase):

    def test_C8262039(self):
        
        """
            CLASS OBJECTS
        """
        designer_chart = Designer_Chart(self.driver)
        utils = UtillityMethods(self.driver)
        chart = Chart(self.driver)
        
        """
            VARIABLES 
        """
        case_id = 'C8262039'
        preview_chart_css = "[id*='chartpreview']"
        run_chart_css = "#jschart_HOLD_0"
        
        """
            STEP 1 : Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
            http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671827%2F&master=ibisamp%2Fcar&tool=chart
        """
        designer_chart.invoke_designer_chart_using_api('ibisamp/car')
        designer_chart.wait_for_visible_text(preview_chart_css, "Group", designer_chart.chart_long_timesleep)
        
        """
            STEP 02 : Select "Sparkline KPI" chart from chart picker component
        """
        designer_chart.select_chart_from_chart_picker('sparkline_kpi', expand=True)
        designer_chart.wait_for_visible_text(preview_chart_css, "Revenue", designer_chart.chart_short_timesleep)
        
        """
            STEP 02 - Expected : The following chart displayed.
        """
        actual_text = self.driver.find_element_by_css_selector(preview_chart_css).text.strip()
        utils.asequal('Revenue+37% LY\n431.7M\nAdd more measures or dimensions', actual_text, 'Step 02.01 : Verify Spark Line Chart')
        
        """
            STEP 03 : Double click "COUNTRY" field to Compare Group. Drag and drop "CAR" to X-Axis
            Double click "DEALER_COST" to Measure
        """
        designer_chart.double_click_on_dimension_field('COUNTRY')
        designer_chart.drag_dimension_field_to_query_bucket('COMP->CAR', 'X-Axis')
        designer_chart.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        designer_chart.wait_for_visible_text(preview_chart_css, "DEALER_COST", designer_chart.chart_short_timesleep)
        
        """
            STEP 03 - Expected : The following Chart in Live Preview
        """
        expected_text = "DEALER_COST+88% COUNTRY\n37.9k"
        actual_text = self.driver.find_element_by_css_selector(preview_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, 'Step 03.01 : Verify Spark Line Chart')
        
        """
            STEP 04 : Click Preview icon from the toolbar.
        """
        designer_chart.click_toolbar_item('preview')
        designer_chart.switch_to_run_preview_frame()
        designer_chart.wait_for_visible_text(run_chart_css, "DEALER_COST", designer_chart.chart_short_timesleep)
        
        """
            STEP 04 - Expected : Chart displayed in preview mode.
        """
        actual_text = self.driver.find_element_by_css_selector(run_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, 'Step 04.01 : Verify Spark Line Chart')
        
        """
            STEP 05 : Hover over on risers. The tooltip value displayed.
        """
        tooltip = '18,621'
        chart.verify_sparkline_chart_tooltip(tooltip, "05.01", chart_location='middle_left', xoffset=2)
        
        """
            STEP 06 : Hover blue icon from the center of the chart > click Return button.
        """
        designer_chart.switch_to_default_content()
        designer_chart.go_back_to_design_from_preview()
        
        """
            STEP 07 : Click Save in the toolbar > Enter Title as "C8262039" > Click Save.
        """
        designer_chart.save_designer_chart_from_toolbar(case_id)
        
        """
            STEP 08 : Logout using API - http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart.api_logout()
        
        """
            STEP 09 : Run the fex from domain tree using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://machine:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%252FP292_S28313%252FG671827%252F&BIP_item=c8262039.fex
        """
        designer_chart.run_designer_chart_using_api(case_id.lower())
        designer_chart.wait_for_visible_text(run_chart_css, "DEALER_COST", designer_chart.chart_long_timesleep)
        
        """
            STEP 09 - Expected : Chart displayed in run time without error.
        """
        actual_text = self.driver.find_element_by_css_selector(run_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, 'Step 09.01 : Verify Spark Line Chart')
        
        """
            STEP 10 : Close the output window
        """
        designer_chart.api_logout()
        
        """
            STEP 11 : Restore the c8262039.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
            http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671827%2Fc8262039.fex
        """
        designer_chart.invoke_designer_chart_in_edit_mode_using_api(case_id.lower())
        designer_chart.wait_for_visible_text(preview_chart_css, "DEALER_COST", designer_chart.chart_long_timesleep)
        
        """
            STEP 11 - Expected : Chart restored successfully.
        """
        actual_text = self.driver.find_element_by_css_selector(preview_chart_css).text.strip()
        utils.asequal(expected_text, actual_text, 'Step 11.01 : Verify Spark Line Chart')
        
        """
            STEP 12 : Logout using API
        """