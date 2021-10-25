'''
Created on May 10, 2019

@author: vpriya
Testcase Name : Apply Rotation to X Axis Labels
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/9318167
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity
from common.lib import core_utility 
from common.locators import designer_chart_locators


class C9318167_TestClass(BaseTestCase):
    
    def test_C9318167(self):
        
        
        """
        Testcase case objects
        """
        designer_chart_obj=designer_chart.Designer_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        insight_loc_obj=designer_chart_locators.DesignerInsight()
        
        """
        Test case variables
        """
        x_axis_label_css="text[class*='xaxisOrdinal-labels!']"
        y_axis_label_css="text[class*='yaxis-labels!']"
        legend_label_css="[class*='legend-labels!']"
        Rotate_css="g text[class*='xaxisOrdinal-labels!'][transform*='-45']"
        Rotate_css_degress="g text[class*='xaxisOrdinal-labels!'][transform*='90']"
        Run_parent_css="#jschart_HOLD_0"
        expected_x_label_list=['ENGLAND : JAGUAR', 'ENGLAND : JENSEN', 'ENGLAND : TRIUMPH', 'FRANCE : PEUGEOT', 'ITALY : ALFA ROMEO', 
                                      'ITALY : MASERATI', 'JAPAN : DATSUN', 'JAPAN : TOYOTA', 'W GERMANY : AUDI', 'W GERMANY : BMW']
        expected_Y_label_list=['0', '20K', '40K', '60K', '80K', '100K', '120K']
        expected_X_title_list=['COUNTRY : CAR']
        expected_legend_list=['DEALER_COST', 'RETAIL_COST']
        
        
        """
        Step 1:Launch the IA API with Chart (edit the domain, port and alias of the URL - do not use the URL as is):
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG730863%2F&master=ibisamp%2Fcar&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
 
        """
        Step 2:Double click on COUNTRY.
        Expand COMP under Dimensions and double click on CAR.
        """
        designer_chart_obj.double_click_on_dimension_field("COUNTRY")
        utill_obj.synchronize_with_number_of_element(x_axis_label_css,5,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_dimension_field("COMP->CAR")
        utill_obj.synchronize_with_number_of_element(x_axis_label_css,10,designer_chart_obj.home_page_long_timesleep)
        
        """
        Step 3:Expand COMP, CARREC, BODY in Measures, double click DEALER_COST & RETAIL_COST
        Fields added to query pane and canvas updated.
        """
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->DEALER_COST")
        utill_obj.synchronize_with_number_of_element(y_axis_label_css,7,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field("COMP->CARREC->BODY->RETAIL_COST")
        utill_obj.synchronize_with_number_of_element(legend_label_css,2,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(expected_x_label_list,msg="Step 03:01 verify the x axis title")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_Y_label_list,msg="Step 03:02 verify the y axis title")
        designer_chart_obj.verify_x_axis_title_in_preview(expected_X_title_list,msg="Step 03:03 verify the x_title_list")
        designer_chart_obj.verify_legends_in_preview(expected_legend_list,legend_length=2, msg="Step 03:04 verify legends in design")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g9!mbar!"]', 'bar_blue', msg="Step 03:05 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s1!g9!mbar!"]', 'pale_green', msg="Step 03:06 verify the chart colour")
        
        """
        Step 4:Click on Format tab(fa-fa-brush) icon.
        Click on General drop down and Select Axis.
        """
        designer_chart_obj.select_query_or_format_tab()
        utill_obj.synchronize_until_element_is_visible(".wfc-chart-quick-access-menu", designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.select_format_access_option("Axis")
        utill_obj.synchronize_until_element_is_visible("div[data-ibx-name='chartAxisMenu']", designer_chart_obj.home_page_long_timesleep)
        
 
        """
        Step 5:Click on Rotation drop down > Select "45 Degrees"
        Preview updated with X Axis Labels rotated 45 Degrees.
        """
        designer_chart_obj.change_labels_options('Rotation', '45 Degrees')
        time.sleep(5)
        utill_obj.synchronize_with_number_of_element(Rotate_css,10,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_axis_rotation_in_chart_canvas('rotate(-45)', 'Step 5.1')


        """
        Step 6:Click on Rotation drop down > Select "Normal"
        Preview updated with X Axis Labels rotated to Normal.
        """
        designer_chart_obj.change_labels_options('Rotation', 'Normal')
        time.sleep(5)
        utill_obj.synchronize_until_element_disappear(Rotate_css,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_axis_rotation_in_chart_canvas('rotate', 'Step 6.1',compare_type='asnotin')
        

        """
        Step 7:Click on Rotation drop down> Select "Automatic"
        Preview updated with X Axis Labels rotated to Automatic.
        """
        designer_chart_obj.change_labels_options('Rotation', 'Automatic')
        time.sleep(10)
        utill_obj.synchronize_until_element_disappear(Rotate_css,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_axis_rotation_in_chart_canvas('rotate(-90)', 'Step 7.1')


        """
        Step 8:Click on Rotation drop down and Choose "90 Degrees"
        Preview updated with X Axis Labels rotated 90 Degrees.
        """
        designer_chart_obj.change_labels_options('Rotation', '90 Degrees')
        time.sleep(5)
        utill_obj.synchronize_with_number_of_element(Rotate_css_degress,10,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_axis_rotation_in_chart_canvas('rotate(-90)', 'Step 8.1')


        """
        Step 9:Click Preview icon from the toolbar.
        Chart displayed in preview mode.
        """
        designer_chart_obj.click_toolbar_item("Preview")
        core_utill_obj.switch_to_frame(insight_loc_obj.INSIGHT_PREVIEW_FRAME)
        utill_obj.synchronize_until_element_is_visible(Run_parent_css,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_title_in_preview(expected_X_title_list, parent_css="#jschart_HOLD_0", msg="Step 09:01 verify the x axis title")
        designer_chart_obj.verify_x_axis_label_in_preview(expected_x_label_list, parent_css="#jschart_HOLD_0", msg="Step 09:02 verify the x label list")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_Y_label_list, parent_css="#jschart_HOLD_0", msg="Step 09:03 verify the y label list")
        designer_chart_obj.verify_legends_in_preview(expected_legend_list,parent_css="#jschart_HOLD_0",legend_length=2, msg="Step 09:04 verify legends in design")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g9!mbar!"]', 'bar_blue', parent_css="#jschart_HOLD_0",msg="Step 09:05 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s1!g9!mbar!"]', 'pale_green', parent_css="#jschart_HOLD_0",msg="Step 09:06 verify the chart colour")
        designer_chart_obj.verify_axis_rotation_in_chart_preview('rotate(90)', 'Step 9.7',compare_type='asnotin')


        """
        Step 10:Hover blue icon from center of the chart > click Return button.
        """
        core_utill_obj.switch_to_default_content()
        designer_chart_obj.go_back_to_design_from_preview()
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)

 
        """
        Step 11:Click Save button from toolbar
        """
        """
        Step 12:Enter Title as "C9318167" > click Save.
        """
        designer_chart_obj.save_designer_chart_from_toolbar("C9318167")


        """
        Step 13:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """

        designer_chart_obj.api_logout()

 
        """
        Step 14:Restore the C9318167.fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        
        http://machine:port/alias/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S29835%2FG730863%2Fc9318167.fex
        
        Chart restored successfully.
        """
        
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api("c9318167")
        utill_obj.synchronize_with_number_of_element(legend_label_css,2,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(expected_x_label_list,msg="14:01 verify the x axis title")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_Y_label_list,msg="Step 14:02 verify the y axis title")
        designer_chart_obj.verify_x_axis_title_in_preview(expected_X_title_list,msg="Step 14:03 verify the x_title_list")
        designer_chart_obj.verify_legends_in_preview(expected_legend_list,legend_length=2, msg="Step 14:04 verify legends in design")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g9!mbar!"]', 'bar_blue', msg="Step 14:05 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s1!g9!mbar!"]', 'pale_green', msg="Step 14:06 verify the chart colour")
        designer_chart_obj.verify_axis_rotation_in_chart_canvas('rotate(90)', 'Step 14.7',compare_type='asnotin')

        """
        Step 15:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        designer_chart_obj.api_logout()
 
       
if __name__ == '__main__':
    unittest.main()