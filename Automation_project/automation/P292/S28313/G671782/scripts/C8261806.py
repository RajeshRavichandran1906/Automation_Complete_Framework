'''
Created on May 29, 2019

@author: varun
Testcase Name : Apply color from color Palette choices for Axis
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261806
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import core_utility
from common.locators.designer_chart_locators import DesignerInsight as insight_locators
from common.lib.utillity import UtillityMethods

class C8261806_TestClass(BaseTestCase):
    
    def test_C8261806(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
        Test case variables
        """
        x_label = ['EMEA', 'North America', 'Oceania', 'South America']
        y_label = ['0', '100M', '200M', '300M', '400M', '500M']
        x_title = ['Store Business Region']
        y_title = ['Cost of Goods']
        
        """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        
        """
        Step 2: Double click "Store,Business,Region" ; "Cost of Goods".
        """
        designer_chart_obj.double_click_on_dimension_field('Store->Store->Store,Business,Region')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "Store,Business,Region", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field("Sales->Cost of Goods")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "Cost of Goods", designer_chart_obj.chart_medium_timesleep)
        
        """
        Step 3: Select Format >General drop down > Axis
        """
        designer_chart_obj.select_query_or_format_tab()
        designer_chart_obj.select_format_access_option('Axis')
        
        """
        Step 4: Select Color space from X axis Font styling.
        Color picker open with Color Palette opened.
        Step 5: Select Blue color from "Color Palette"
        Selected Blue color reflected in color and in X axis values.
        """
        designer_chart_obj.select_font_color_in_labels('#00a2e8')
        utils.synchronize_with_visble_text("#arpreview_fdmId_11_fmg", "Oceania", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_title_color_in_chart_canvas('deep_sky_blue', 'Step 5.1: Verify blue color in the axis')
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 5.1')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 5.2')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 5.3')
        designer_chart_obj.verify_y_axis_title_in_preview(y_title, msg='Step 5.4')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 2, 2, msg='Step 5.5')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', msg='step 5.6')
        
        """
        Step 6: Click "Preview"
        Selected Blue color reflected in X axis values in run time.
        """
        designer_chart_obj.click_toolbar_item('preview')
        core_util_obj.switch_to_frame(insight_locators.INSIGHT_PREVIEW_FRAME)
        designer_chart_obj.wait_for_number_of_element("#jschart_HOLD_0 [class='riser!s0!g0!mbar!']", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, parent_css='#jschart_HOLD_0', msg='Step 6.1')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, parent_css='#jschart_HOLD_0', msg='Step 6.2')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, parent_css='#jschart_HOLD_0', msg='Step 6.3')
        designer_chart_obj.verify_y_axis_title_in_preview(y_title, parent_css='#jschart_HOLD_0', msg='Step 6.4')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 2, 2, msg='Step 6.5')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', parent_css='#jschart_HOLD_0', msg='step 6.6')
        designer_chart_obj.verify_x_axis_title_color_in_chart_preview('deep_sky_blue', 'Step 6.7: Verify the color in x axis')
        core_util_obj.switch_to_default_content()
        
        """
        Step 7: Click blue icon from center of the chart , click Return button.
        """
        designer_chart_obj.go_back_to_design_from_preview()
        
        """
        Step 8: Click Save icon, enter Title as "C8261806" > click Save.
        """
        designer_chart_obj.save_designer_chart_from_toolbar('C8261806')
        
        """
        Step 9: Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
        
if __name__ == '__main__':
    unittest.main()