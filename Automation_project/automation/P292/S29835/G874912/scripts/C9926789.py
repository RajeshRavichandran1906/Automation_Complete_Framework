"""----------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 01-October-2019
----------------------------------------------------------------"""

from common.lib.core_utility import CoreUtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.chart import Chart

class C9926789_TestClass(BaseTestCase):
    
    def test_C9926789(self):
        
        """ 
            CLASS OBJECTS 
        """
        chart = Chart(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            VARIABLES
        """
        run_chart_css = "#jschart_HOLD_0"
        preview_chart_css = "#pfjTableChart_1"
        layers_css = ".TableOfContentsButton"
        layer_content_css = ".TableOfContentsContainer:not([style*='hidden'])"
        layer_context_text = "Layers\nWorld Countries\nOpacity"
        
        """
            STEP 01 : Launch IA Chart using wfretail.mas in developer user.
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG840058%2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        chart.invoke_chart_tool_using_api("baseapp/wf_retail_lite")
        chart.wait_for_visible_text(preview_chart_css, "Group", chart.chart_long_timesleep)
        
        """
            STEP 02 : Select Format tab > Click "Choropleth map" in Chart Types group
        """
        chart.select_ia_ribbon_item('Format', 'choropleth')
        chart.wait_for_visible_text(preview_chart_css, "Esri", chart.chart_medium_timesleep)
        
        """
            STEP 03 : Double click "Cost of Goods" and "Store,Country"
        """
        chart.double_click_on_datetree_item('Cost of Goods', 1)
        chart.double_click_on_datetree_item('Store,Country', 1)
        chart.wait_for_visible_text(preview_chart_css, "Cost of Goods", chart.chart_long_timesleep+30)
        
        """
            STEP 03 - Expected : Fields added to query pane and map updated in canvas.
        """
        legends = ['Cost of Goods', '0M', '98M', '196M', '294M', '392M']
        query_fields = ['Chart (wf_retail_lite)', 'Location', 'Layer', 'Store,Country', 'Metric', 'Color', 'Cost of Goods', 'Tooltip', 'Multi-graph']
        chart.verify_all_fields_in_query_pane(query_fields, "Step 03.01 : Verify fields added to query pane")
        chart.verify_legends_in_preview(legends, msg="Step 03.02")
        chart.verify_number_of_risers(preview_chart_css + " path", 1, 34, msg="Step 03.03")
        chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g13!mregion!']", "persian_red3", msg="Step 03.04 ")
        
        """
            STEP 04 : Click "Layers" TOC in Live Preview
        """
        layer = utils.validate_and_get_webdriver_object(layers_css, "Esri map layers button")
        core_utils.left_click(layer)
        chart.wait_for_visible_text(layer_content_css, 'Layers', chart.chart_short_timesleep)
        
        """
            STEP 04 - Expected : The "Layers" displayed correctly
        """
        actual_content = utils.validate_and_get_webdriver_object(layer_content_css, "Esri map layers content").text.strip()
        utils.asequal(layer_context_text, actual_content, "Step 04.01 : Verify 'Layers' displayed correctly")
        
        """
            STEP 05 : Click "Run" button.
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(run_chart_css, "Cost of Goods", chart.chart_long_timesleep)
        
        """
            STEP 06 - Click "Layers".
        """
        layer = utils.validate_and_get_webdriver_object(layers_css, "Esri map layers button")
        core_utils.left_click(layer)
        chart.wait_for_visible_text(layer_content_css, 'Layers', chart.chart_short_timesleep)
        
        """
            STEP 06 - Expected : The "Layers" is displayed correctly.
        """
        actual_content = utils.validate_and_get_webdriver_object(layer_content_css, "Esri map layers content").text.strip()
        utils.asequal(layer_context_text, actual_content, "Step 06.01 : Verify 'Layers' displayed correctly")
        
        """
            STEP 07 : Close the run tab.
        """
        chart.switch_to_default_content()
        
        """
            STEP 08 : Click "Proportional Symbol map" in the Format tab
        """
        chart.select_ia_ribbon_item('Format', 'proportional_symbol')
        utils.synchronize_until_element_is_visible(preview_chart_css + " circle[class='riser!s0!g33!mregion!']", chart.chart_long_timesleep)
        
        """
            STEP 08 - Expected : "Layers" still opened after converting to proportional map
        """
        actual_content = utils.validate_and_get_webdriver_object(layer_content_css, "Esri map layers content").text.strip()
        utils.asequal(layer_context_text, actual_content, "Step 08.01 : Verify 'Layers' still opened after converting to proportional map")
        
        """
            STEP 09 : Click "Run" button
        """
        chart.run_chart_from_toptoolbar()
        chart.switch_to_frame()
        chart.wait_for_visible_text(run_chart_css, "Cost of Goods", chart.chart_long_timesleep)
        
        """
            STEP 10 : Click "Layers"
        """
        layer = utils.validate_and_get_webdriver_object(layers_css, "Esri map layers button")
        core_utils.left_click(layer)
        chart.wait_for_visible_text(layer_content_css, 'Layers', chart.chart_short_timesleep)
        
        """
            STEP 10 - Expected : The "Layers" is displayed correctly
        """
        actual_content = utils.validate_and_get_webdriver_object(layer_content_css, "Esri map layers content").text.strip()
        utils.asequal(layer_context_text, actual_content, "Step 08.01 : Verify 'Layers' is displayed correctly")
        
        """
            STEP 11 : Logout using API - http://machine:port/alias/service/wf_security_logout.jsp
        """
        