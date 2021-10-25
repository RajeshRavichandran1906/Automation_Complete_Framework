'''
Created on May 24, 2019

@author: varun
Testcase Name : Apply Font styles to X Axis Labels
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/9318165
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.lib import core_utility
from common.locators.designer_chart_locators import DesignerInsight as insight_locators


class C9318165_TestClass(BaseTestCase):
    def test_C9318165(self):
        """
        Testcase variables
        """
        x_label = ['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW']
        y_label =  ['0', '20K', '40K', '60K', '80K', '100K', '120K']
        x_title = ['COUNTRY : CAR']
        
        """
        Testcase case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api('c9318165')
        
        """
        Step 1: Launch the API with Designer Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&master=ibisamp%2Fcar&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG730863&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element(".wfc-bc-output-div", 1, designer_chart_obj.chart_long_timesleep)
  
        """
        Step 2: Double click on COUNTRY.
        Expand COMP under Dimensions and double click on CAR.
        """
        designer_chart_obj.double_click_on_dimension_field("COUNTRY")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_dimension_field("COMP->CAR")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "CAR", designer_chart_obj.chart_medium_timesleep)
 
        """
        Step 3:Expand COMP, CARREC, BODY in Measures, double click DEALER_COST & RETAIL_COST
        Fields added to query pane and canvas updated.
        """
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->DEALER_COST")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->RETAIL_COST")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "RETAIL_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Horizontal', ['COUNTRY','CAR'], 'Step 3.1: Verify the horizontal bucket')
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['DEALER_COST','RETAIL_COST'], 'Step 3.2: Verify the vertical bucket')
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 3.3')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 3.4')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 3.5')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 5, 4, msg='Step 3.6')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', msg='step 3.7')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s1"]', 'pale_green', msg='step 3.7')
 
        """
        Step 4:Click on Format tab(fa-fa-brush) icon.
        Click on General drop down and Select Axis.
        The following default options for Axis.
        Labels Font and Font Size
        """
        designer_chart_obj.select_query_or_format_tab()
        designer_chart_obj.wait_for_number_of_element(dc_locators.FORMAT_QUICK_ACCESS, 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.select_format_access_option('Axis')
        designer_chart_obj.wait_for_visible_text(dc_locators.LABELS_CSS, 'Rotation', designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_font_name_in_labels('SANS-SERIF', 'Step 4.1: Verify the font name')
        designer_chart_obj.verify_font_size_in_labels('9', 'Step 4.1: Verify the font size')
  
        """
        Step 5: Click on Labels Font drop down and choose TIMES NEW ROMAN.
        """
        designer_chart_obj.select_font_name_in_labels('TIMES NEW ROMAN')
         
        """
        Step 6: Click on Font Size drop down and Select 10 and click on pt drop down and select px.r
        """
        designer_chart_obj.select_font_size_in_labels('10')
        designer_chart_obj.select_font_unit_in_labels('px')
 
        """
        Step 7: Click on Bold and Italic in Labels.
        """
        designer_chart_obj.select_font_style_in_labels('bold')
        designer_chart_obj.select_font_style_in_labels('italic')
 
        """
        Step 8: Click on Labels Font color and Choose Red.
        Selected style is reflected in chart canvas.
        """
        designer_chart_obj.select_font_color_in_labels('#ed1c24')
        designer_chart_obj.verify_axis_style_in_chart_canvas('font-style', 'italic', 'Step 8.1: Verify italic is selected')
        designer_chart_obj.verify_axis_style_in_chart_canvas('font-weight', 'bold', 'Step 8.2: Verify bold is selected')
        designer_chart_obj.verify_axis_style_in_chart_canvas('font-size', '10px', 'Step 8.3: Verify the font size')
        designer_chart_obj.verify_axis_style_in_chart_canvas('font-family', 'TIMES NEW ROMAN', 'Step 8.4: Verify the font family')
         
        """
        Step 9:Click Preview icon from the toolbar.
        Chart displayed in preview mode.
        """
        designer_chart_obj.click_toolbar_item('preview')
        core_util_obj.switch_to_frame(insight_locators.INSIGHT_PREVIEW_FRAME)
        designer_chart_obj.wait_for_number_of_element("#jschart_HOLD_0 [class='riser!s0!g0!mbar!']", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, parent_css='#jschart_HOLD_0', msg='Step 9.1')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, parent_css='#jschart_HOLD_0', msg='Step 9.2')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, parent_css='#jschart_HOLD_0', msg='Step 9.3')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 5, 4, msg='Step 9.4')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', parent_css='#jschart_HOLD_0', msg='step 9.5')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s1"]', 'pale_green', parent_css='#jschart_HOLD_0', msg='step 9.6')
        designer_chart_obj.verify_axis_style_in_chart_preview_window('font-style', 'italic', 'Step 9.7: Verify italic is selected')
        designer_chart_obj.verify_axis_style_in_chart_preview_window('font-weight', 'bold', 'Step 9.8: Verify bold is selected')
        designer_chart_obj.verify_axis_style_in_chart_preview_window('font-size', '10px', 'Step 9.9: Verify the font size')
        designer_chart_obj.verify_axis_style_in_chart_preview_window('font-family', 'TIMES NEW ROMAN', 'Step 9.10: Verify the font family')
        core_util_obj.switch_to_default_content()
         
        """
        Step 10: Hover blue icon from center of the chart > click Return button.
        """
        designer_chart_obj.go_back_to_design_from_preview()
 
        """
        Step 11: Click Save button from toolbar
        Step 12: Enter Title as "C9318165" > click Save.
        """
        designer_chart_obj.save_designer_chart_from_toolbar('C9318165')
         
        """
        Step 13: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        
        """
        Step 14: Restore the C9318165.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2Fc9318165.fex
        Chart restored successfully.
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api('c9318165')
        designer_chart_obj.wait_for_number_of_element(".wfc-bc-output-div", 1, designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 14.1')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 14.2')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 14.3')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 5, 4, msg='Step 14.4')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', msg='step 14.5')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s1"]', 'pale_green', msg='step 14.6')
        designer_chart_obj.verify_axis_style_in_chart_canvas('font-style', 'italic', 'Step 14.7: Verify italic is selected')
        designer_chart_obj.verify_axis_style_in_chart_canvas('font-weight', 'bold', 'Step 14.8: Verify bold is selected')
        designer_chart_obj.verify_axis_style_in_chart_canvas('font-size', '10px', 'Step 14.10: Verify the font size')
        designer_chart_obj.verify_axis_style_in_chart_canvas('font-family', 'TIMES NEW ROMAN', 'Step 14.11: Verify the font family')
        
        """
        Step 15:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()