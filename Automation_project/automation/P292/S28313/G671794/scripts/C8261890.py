'''
Created on May 30, 2019

@author: varun
Testcase Name : User can select Theme from the dropdown list
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261890
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.lib import utillity

class C8261890_TestClass(BaseTestCase):
    
    def test_C8261890(self):
        """
        Testcase case objects and variables
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        x_label = ['ALFA ROMEO', 'AUDI', 'BMW', 'DATSUN', 'JAGUAR', 'JENSEN', 'MASERATI', 'PEUGEOT', 'TOYOTA', 'TRIUMPH']
        y_label = ['0', '20K', '40K', '60K', '80K', '100K']
        x_title = ['CAR']
        
        """
        Step 1: Launch the API to create new Designer Chart with the Car file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
  
        """
        Step 2: Double "CAR", "DEALER_COST" and "RETAIL_COST".
        Fields added to query pane and canvas updated.
        """
        designer_chart_obj.double_click_on_dimension_field('COMP->CAR')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "CAR", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->RETAIL_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "RETAIL_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 02.01')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 02.02')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 02.03')
        designer_chart_obj.verify_number_of_risers('.wfc-bc-output-div rect', 2, 10, msg='Step 02.04')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', msg='step 02.05')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s1"]', 'pale_green', msg='step 02.06')
        designer_chart_obj.verify_values_in_querybucket('Horizontal', ['CAR'], 'Step 02.07: Verify the horizontal bucket')
        designer_chart_obj.verify_values_in_querybucket('Vertical', ['DEALER_COST', 'RETAIL_COST'], 'Step 02.08: Verify the vertical bucket')
        
        """
        Step 3: Click on Format tab(fa-fa-brush) icon.
        """
        designer_chart_obj.select_query_or_format_tab()
        
        """
        Step 4: Click on Theme drop down.
        Theme drop down menu list showing the following options.
        """
        designer_chart_obj.wait_for_number_of_element(dc_locators.CHART_THEME_INPUT, 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.select_theme_in_format_tab('Custom...', msg='Step 04.01: Verify the theme list', verify_list=['Designer 2018', 'Light', 'Midnight', 'Custom...'], compare_type='asin')
        
        """
        Step 5: Select Custom... > Select "ENDark.sty" theme > Click Open.
        Selected Dark theme applied on the chart.
        """
        designer_chart_obj.wait_for_number_of_element('.open-dialog-resources.pop-top', 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.select_grid_item_from_open_dialog('ENDark.sty')
        designer_chart_obj.wait_for_number_of_element(".wfc-bc-output-div rect[class='background']", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_background_color_in_chart_canvas('nero', 'Step 05.01: Verify the background color')
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 05.02')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 05.03')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 05.04')
        designer_chart_obj.verify_number_of_risers('.wfc-bc-output-div rect', 2, 10, msg='Step 05.05')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'dark_orange1', msg='step 05.06')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s1"]', 'orange_red', msg='step 05.07')
        
        """
        Step 6: Again click on Theme drop down > select default theme "Designer 2018"
        Chart shows back to its original state properly.
        """
        designer_chart_obj.select_theme_in_format_tab('Designer 2018')
        util_obj.synchronize_until_element_disappear(".wfc-bc-output-div [class='background']", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.wait_for_number_of_element("text[class^='xaxis']", 11, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 06.01')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 06.02')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 06.03')
        designer_chart_obj.verify_number_of_risers('.wfc-bc-output-div rect', 2, 10, msg='Step 06.04')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', msg='step 06.05')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s1"]', 'pale_green', msg='step 06.06')
        
        """
        Step 7: Click Save in the toolbar > Enter title as "C8261890" > Click Save.
        """
        designer_chart_obj.save_designer_chart_from_toolbar('C8261890')
        
        """
        Step 8: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()