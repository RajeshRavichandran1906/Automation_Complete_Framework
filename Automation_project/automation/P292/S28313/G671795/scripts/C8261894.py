'''
Created on May 31, 2019

@author: varun
Testcase Name : Test select Theme from the dropdown list and will reflect on the Char
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261894
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators

class C8261894_TestClass(BaseTestCase):
    
    def test_C8261894(self):
        """
        Testcase case objects and variables
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
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
        Step 2: Double click "CAR", "DEALER_COST", "RETAIL_COST" and COUNTRY in the color bucket
        Fields added to appropriate buckets and canvas updated.
        """
        designer_chart_obj.double_click_on_dimension_field('COMP->CAR')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "CAR", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->RETAIL_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "RETAIL_COST", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.drag_dimension_field_to_query_bucket("COUNTRY", "Color")
        designer_chart_obj.wait_for_number_of_element("rect[fill='#e1542b'][class^='riser!s4!g0!']", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 02.01')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 02.02')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 02.03')
        designer_chart_obj.verify_number_of_risers('.wfc-bc-output-div rect', 2, 10, msg='Step 02.04')
#         designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 5, 4, msg='Step 2.4')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'bar_blue', msg='step 02.05')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s1"]', 'pale_green', msg='step 02.06')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s4"]', 'sunset_orange', msg='step 02.07')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s5"]', 'light_brick', msg='step 02.08')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s8"]', 'moss_green', msg='step 02.09')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s9"]', 'pale_yellow1', msg='step 02.10')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s6"]', 'periwinkle_gray', msg='step 02.11')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s7"]', 'tea_green', msg='step 02.12')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s2"]', 'med_green', msg='step 02.13')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s3"]', 'pale_yellow', msg='step 02.14')
        
        """
        Step 3: Click on Format tab (fa fa-brush) icon.
        """
        designer_chart_obj.select_query_or_format_tab()
        
        """
        Step 4: Click on Theme dropdown .
        The following themes are shown from dropdown.
        Step 5: Select"Midnight" from the drop down.
        Selected theme is reflected in Canvas.
        """  
        designer_chart_obj.wait_for_number_of_element(dc_locators.FORMAT_QUICK_ACCESS, 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.select_theme_in_format_tab('Midnight', 'Step 04.01: Verify the themes', verify_list=['Designer 2018', 'Light', 'Midnight', 'Custom...'], compare_type='asin')
        designer_chart_obj.wait_for_number_of_element("rect[fill='#FFD990'][class^='riser!s4!g0!']", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s4"]', 'caramel', msg='step 05.01')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s5"]', 'summer_sky_blue', msg='step 05.02')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s8"]', 'lavender_pink', msg='step 05.03')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s9"]', 'rosebud', msg='step 05.04')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s6"]', 'water_leaf', msg='step 05.05')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s7"]', 'pale_cornflower_blue', msg='step 05.06')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0"]', 'puerto_rico', msg='step 05.07')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s1"]', 'cornflower', msg='step 05.08')
        
        """
        Step 6: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()