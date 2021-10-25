'''
Created on May 27, 2019

@author: Vpriya
Testcase Name : Apply Font and Font Size to Legend Label and Legend Title
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/9318169
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.lib import core_utility
from common.lib import utillity
from common.locators.designer_chart_locators import DesignerInsight as insight_locators


class C9318169_TestClass(BaseTestCase):
    
    def test_C9318169(self):
        
        """
        Testcase variables
        """
        
        Run_parent_css = "#jschart_HOLD_0"
        x_label = ['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW']
        y_label =  ['0', '20K', '40K', '60K', '80K', '100K', '120K']
        x_title = ['COUNTRY : CAR']
        riser_list_preview = ['rect[class^="riser!s0"]','rect[class^="riser!s1"]','rect[class^="riser!s5"]','rect[class^="riser!s4"]','rect[class^="riser!s3!g4!mbar!"]','rect[class^="riser!s2!g4!mbar!"]']
        color_list_preview = ['bar_blue', 'pale_green', 'orange', 'brick_red', 'pale_yellow_2','dark_green']
        expected_legend_list=['DEALER_COST : 100 LS 2 DOOR AUTO', 'RETAIL_COST : 100 LS 2 DOOR AUTO', 'DEALER_COST : 2000 4 DOOR BERLINA', 'RETAIL_COST : 2000 4 DOOR BERLINA', 'DEALER_COST : 2000 GT VELOCE', 'RETAIL_COST : 2000 GT VELOCE', 'DEALER_COST : 2000 SPIDER VELOCE', 'RETAIL_COST : 2000 SPIDER VELOCE', 'DEALER_COST : 2002 2 DOOR', 'RETAIL_COST : 2002 2 DOOR', 'DEALER_COST : 2002 2 DOOR AUTO', 'RETAIL_COST : 2002 2 DOOR AUTO', 'DEALER_COST : 3.0 SI 4 DOOR', 'RETAIL_COST : 3.0 SI 4 DOOR', 'DEALER_COST : 3.0 SI 4 DOOR AUTO', 'RETAIL_COST : 3.0 SI 4 DOOR AUTO', 'DEALER_COST : 504 4 DOOR', 'RETAIL_COST : 504 4 DOOR', 'DEALER_COST : 530I 4 DOOR', 'RETAIL_COST : 530I 4 DOOR', 'DEALER_COST : 530I 4 DOOR AUTO', 'RETAIL_COST : 530I 4 DOOR AUTO', 'DEALER_COST : B210 2 DOOR AUTO', 'RETAIL_COST : B210 2 DOOR AUTO', 'DEALER_COST : COROLLA 4 DOOR DIX AUTO', 'RETAIL_COST : COROLLA 4 DOOR DIX AUTO', 'DEALER_COST : DORA 2 DOOR', 'RETAIL_COST : DORA 2 DOOR', 'DEALER_COST : INTERCEPTOR III', 'RETAIL_COST : INTERCEPTOR III', 'DEALER_COST : TR7', 
                  'RETAIL_COST : TR7', 'DEALER_COST : V12XKE AUTO', 'RETAIL_COST : V12XKE AUTO', 'DEALER_COST : XJ12L AUTO', 'RETAIL_COST : XJ12L AUTO']
        
        
        def verify_color(riser_list, color_list, step_num):
            for index, name in enumerate(color_list, 0):
                designer_chart_obj.verify_chart_color_using_get_css_property_in_preview(riser_list[index], name, msg='step {0}.{1}'.format(step_num, index))

        """
        Testcase case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        utillity_obj=utillity.UtillityMethods(self.driver)
        insight_loc_obj=insight_locators()
        
        """
        Step 1: Launch the API with Designer Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&master=ibisamp%2Fcar&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG730863&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
  
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
        Drag and drop MODEL to Color bucket.
        Fields added to query pane and canvas updated.
        """
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->DEALER_COST")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->RETAIL_COST")
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "RETAIL_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.drag_dimension_field_to_query_bucket('CARREC->MODEL','Color')
        designer_chart_obj.verify_values_in_querybucket('Horizontal', ['COUNTRY','CAR'], 'Step 3.1: Verify the horizontal bucket')
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['DEALER_COST','RETAIL_COST'], 'Step 3.2: Verify the vertical bucket')
        designer_chart_obj.verify_values_in_querybucket('Color', ['MODEL'], msg='Step 3.3 verify the color bucket')
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 3.3')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 3.4')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 3.5')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 36, 1, msg='Step 3.6')
        designer_chart_obj.verify_legends_in_preview(expected_legend_list,msg="Step 3.7")
        verify_color(riser_list_preview,color_list_preview,'3.7')
        
 
        """
        Step 4:Click on Format tab(fa-fa-brush) icon.
        Click on General drop down > Select Legend option..
        The following default options for legends.
        Labels Font and Font Size
        """
        designer_chart_obj.select_query_or_format_tab()
        designer_chart_obj.wait_for_number_of_element(dc_locators.FORMAT_QUICK_ACCESS, 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.select_format_access_option('Legend')
        designer_chart_obj.wait_for_visible_text(dc_locators.LEGEND_LABELS_CSS, 'Labels', designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_font_size_in_legend_labels('7.5', msg="step 04:01 verify the default font name")
        designer_chart_obj.verify_font_name_in_legend_labels("SANS-SERIF", msg="step 04:02 verify the default font name")
        
  
        """
        Step 5: Click on Labels Font drop down > Choose TIMES NEW ROMAN.
        Click on Font Size drop down > Select 10 and click on pt drop down >Select px.
        Selected style is reflected in chart.
        """
        designer_chart_obj.select_font_name_in_legend_labels("TIMES NEW ROMAN")
        designer_chart_obj.select_font_size_in_legend_labels("10")
        designer_chart_obj.select_font_unit_in_legend_labels('px')
        utillity_obj.synchronize_until_element_is_visible(".legend text[font-size='10px']",designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_legend_style_in_canvas("fill", "#505050",msg="Step 05.1")
        designer_chart_obj.verify_legend_style_in_canvas("font-size", "10px", msg="Step 05.2")
        designer_chart_obj.verify_legend_style_in_canvas("font-family", 'TIMES NEW ROMAN', msg="Step 05.3")
        
        
        """
        Step 6:Expand Titles option.
        Show title option is no longer available under Titles option.
        """
        designer_chart_obj.verify_show_title_in_legend_labels('Step 6.1: Verify the label is not present')
        
        """
        Step 7:Click Preview icon from the toolbar.
        Chart displayed in preview mode. 
        """
        designer_chart_obj.click_toolbar_item("preview")
        core_utility_obj.switch_to_frame(insight_loc_obj.INSIGHT_PREVIEW_FRAME)
        utillity_obj.synchronize_until_element_is_visible(Run_parent_css,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_legend_style_in_preview("fill", "#505050",msg="Step 07.1")
        designer_chart_obj.verify_legend_style_in_preview("font-size", "10px", msg="Step 07.2")
        designer_chart_obj.verify_legend_style_in_preview("font-family", 'TIMES NEW ROMAN', msg="Step 07.3")
        
        """
        Step 8: Hover blue icon from center of the chart > click Return button.
        """
        core_utility_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
 
        """
        Step 9: Click Save button from toolbar
        Step 10: Enter Title as "C9318169" > click Save.
        """
        designer_chart_obj.save_designer_chart_from_toolbar('c9318169')
         
        """
        Step 11: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
        
        """
        Step 12: Restore the C9318165.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%2Fc9318165.fex
        Chart restored successfully.
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api('c9318169')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 3.3')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 3.4')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 3.5')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 36, 1, msg='Step 3.6')
        designer_chart_obj.verify_legends_in_preview(expected_legend_list,msg="Step 3.7")
        verify_color(riser_list_preview,color_list_preview,'3.7')
        designer_chart_obj.verify_legend_style_in_canvas("fill", "#505050",msg="Step 12.1")
        designer_chart_obj.verify_legend_style_in_canvas("font-size", "10px", msg="Step 12.2")
        designer_chart_obj.verify_legend_style_in_canvas("font-family", 'TIMES NEW ROMAN', msg="Step 12.3")
        
        
        """
        Step 13:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()