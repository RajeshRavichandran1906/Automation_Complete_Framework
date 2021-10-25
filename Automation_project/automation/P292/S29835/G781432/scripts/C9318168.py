'''
Created on May 28, 2019

@author: varun
Testcase Name : Create Bin based on a calculated field
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/9318168
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity
from common.lib import core_utility
from common.locators.designer_chart_locators import DesignerInsight as insight_locators


class C9318168_TestClass(BaseTestCase):
    
    def test_C9318168(self):
        """
        Testcase case objects and variables
        """
        util_obj = utillity.UtillityMethods(self.driver)
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        calculation_dialog = ".wfc-calculator-dialog"
        x_label = ['ENGLAND : .00', 'ENGLAND : 1,000.00', 'ENGLAND : 2,000.00', 'FRANCE : .00', 'ITALY : 1,000.00', 'ITALY : 6,000.00', 'JAPAN : .00', 'W GERMANY : .00', 'W GERMANY : 1,000.00', 'W GERMANY : 3,000.00']
        y_label = ['0', '20K', '40K', '60K', '80K', '100K']
        x_title = ['COUNTRY : Profit_BIN_1']
        y_title = ['SALES']
        
        """
        Step 1: Launch the API to create new Designer Chart with the Car file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
  
        """
        Step 2: Click "New Calculation.." from Measure menu
        New Calculation dialog is displayed
        """
        designer_chart_obj.select_new_calculation_from_dimensions_or_measures('measures')
        designer_chart_obj.wait_for_number_of_element(calculation_dialog, 1, designer_chart_obj.chart_medium_timesleep)
        util_obj.verify_object_visible(calculation_dialog, True, 'Step 2.1: Verify the new clculation is displayed')
        
        """
        Step 3: Change field name from "Calculation_1" to "Profit"
        """
        designer_chart_obj.edit_calculation_dialog_name('Profit')
 
        """
        Step 4: Double click CAR.BODY.RETAIL_COST - CAR.BODY.DEALER_COST
        Verify the following dialog
        """
        designer_chart_obj.double_click_on_calculation_fields('COMP->CARREC->BODY->RETAIL_COST')
        designer_chart_obj.click_operator_from_new_calculation('-')
        designer_chart_obj.double_click_on_calculation_fields('DEALER_COST')
        designer_chart_obj.verify_dialog_box_in_calculation('CAR.BODY.RETAIL_COST - CAR.BODY.DEALER_COST', 'Step 4.1: Verify the dialog')
        
        """
        Step 5: Click OK
        Verify a field "Profit" added to the BODY segment of the Measures group
        """
        designer_chart_obj.click_button_on_calculation('OK')
        designer_chart_obj.verify_element_added_in_measures('Step 5.1: Verify profit is added ', 'COMP->CARREC->BODY->Profit', 'Profit')

        """
        Step 6: Right click on Profit -> Select "Bin values"
        """
        designer_chart_obj.right_click_on_measures_field('Profit', 'Bin values')
        designer_chart_obj.wait_for_number_of_element('div[data-ibx-type="binvalues"]', 1, designer_chart_obj.chart_medium_timesleep)
        
        """
        Step 7: Enter value "1000" under Bin Width > Click Value radio button > Click OK
        Verify a field "Profit_BIN_1" added to the Body segment of the Dimensions group.
        """
        designer_chart_obj.edit_bin_values_in_measures(bin_width_text=1000, show_as='Value')
        designer_chart_obj.verify_element_added_in_dimensions('Step 7.1: Verify profit is added ', 'COMP->CARREC->BODY->Profit_BIN_1', 'Profit_BIN_1')
        
        """
        Step 8: Double click "Country", "Profit_BIN_1" and "Sales"
        """
        designer_chart_obj.double_click_on_dimension_field('COUNTRY')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_dimension_field('Profit_BIN_1')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "Profit_BIN_1", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->SALES')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "SALES", designer_chart_obj.chart_medium_timesleep)
        
        """
        Step 9: Click Save and Enter title as "C9318168" > Save
        """
        designer_chart_obj.save_designer_chart_from_toolbar('C9318168')
        
        """
        Step 10: Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """
        designer_chart_obj.api_logout()
        
        """
        Step 11: Restore the saved Chart Designer using API link.
        http://machine:port/alias/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863/c9318168.fex
        Verify restore successful with Bin field
        """
        designer_chart_obj.invoke_designer_chart_in_edit_mode_using_api('c9318168')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_values_in_querybucket('Horizontal', ['COUNTRY','Profit_BIN_1'], 'Step 11.1: Verify the horizontal bucket')
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['SALES'], 'Step 11.2: Verify the vertical bucket')
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 11.3')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 11.4')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 11.5')
        designer_chart_obj.verify_y_axis_title_in_preview(y_title, msg='Step 11.6')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 5, 2, msg='Step 11.7')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', msg='step 11.8')
        
        """
        Step 12: Click Preview
        Verify output 
        """
        designer_chart_obj.click_toolbar_item('preview')
        core_util_obj.switch_to_frame(insight_locators.INSIGHT_PREVIEW_FRAME)
        designer_chart_obj.wait_for_number_of_element("#jschart_HOLD_0 [class='riser!s0!g0!mbar!']", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, parent_css='#jschart_HOLD_0', msg='Step 12.1')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, parent_css='#jschart_HOLD_0', msg='Step 12.2')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, parent_css='#jschart_HOLD_0', msg='Step 12.3')
        designer_chart_obj.verify_y_axis_title_in_preview(y_title, parent_css='#jschart_HOLD_0', msg='Step 12.4')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 5, 2, msg='Step 12.5')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g2"]', 'bar_blue', parent_css='#jschart_HOLD_0', msg='step 12.6')
        core_util_obj.switch_to_default_content()
        
        """
        Step 13: Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()