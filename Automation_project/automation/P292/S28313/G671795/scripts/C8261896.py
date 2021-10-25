'''
Created on June 3, 2019

@author: Vpriya
Testcase Name : Deisgner chart themes as Default, Light & Midnight .sty
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261896
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.locators.designer_chart_locators import DesignerChart as dc_locators
from common.lib import utillity

class C8261896_TestClass(BaseTestCase):
    
    def test_C8261896(self):
        """
        Testcase case objects and variables
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utillity_obj=utillity.UtillityMethods(self.driver)
        
        x_label = ['ENGLAND', 'FRANCE', 'ITALY', 'JAPAN', 'W GERMANY']
        y_label = ['0', '10K', '20K', '30K', '40K', '50K', '60K']
        x_title = ['COUNTRY']
        y_title=['DEALER_COST']
        color_label=['0', '14.7K', '29.4K', '44K', '58.8K', '73.5K', '88.2K']
        
        
        """
        Step 1: Launch the API to create new Designer Chart with the Car file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S29835/G730863&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api("ibisamp/car")
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
  
        """
        Step 2: Double click COUNTRY, DEALER_COST.
        """
        designer_chart_obj.double_click_on_dimension_field('COUNTRY')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "COUNTRY", designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.double_click_on_measures_field('COMP->CARREC->BODY->DEALER_COST')
        designer_chart_obj.wait_for_visible_text(".wfc-bucket-display-box", "DEALER_COST", designer_chart_obj.chart_medium_timesleep)
        
        
        """
        Step 3:Add SALES to Color bucket.
        Color scale displayed according to theme.
        """
        designer_chart_obj.drag_measure_field_to_query_bucket('SALES', 'Color')
        designer_chart_obj.wait_for_number_of_element(".legendColorScale", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(x_label, msg='Step 03.1')
        designer_chart_obj.verify_y_axis_label_in_preview(y_label, msg='Step 03.2')
        designer_chart_obj.verify_x_axis_title_in_preview(x_title, msg='Step 03.3')
        designer_chart_obj.verify_y_axis_title_in_preview(y_title,msg='Step 03.3')
        designer_chart_obj.verify_number_of_risers('rect[class^="riser!"]', 1,5, msg='Step 03.4')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g0!mbar!"]', 'Solitude', msg='step 03.5')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g1!mbar!"]', 'Solitude', msg='step 03.6')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g2!mbar!"]', 'French_Pass', msg='step 03.7')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g3!mbar!"]', 'Cobalt', msg='step 03.8')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g3!mbar!"]', 'Cobalt', msg='step 03.9')
        designer_chart_obj.verify_x_axis_label_in_preview(color_label,xyz_axis_label_css="text[class^='colorScale-labels!']",msg='Step 03.10')
        
        
        """
        Step 4: Click on Format tab (fa fa-brush) icon.
        Under General tab > Default Theme is selected.
        """
        designer_chart_obj.select_query_or_format_tab()
        utillity_obj.synchronize_until_element_is_visible(dc_locators.CHART_THEME_INPUT +" input", designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_theme_in_format_tab('Designer 2018',"Step 04.1 verify the default theme in format tab")
        
        """
        Step 5: Click Default Theme drop down > select Light.
        Chart updated with selected theme.
        """  
        designer_chart_obj.select_theme_in_format_tab('Light', 'Step 05.1: Verify the themes', verify_list=['Designer 2018', 'Light', 'Midnight', 'Custom...'], compare_type='asin')
        designer_chart_obj.wait_for_number_of_element("rect[fill*='#B30000'][class='riser!s0!g4!mbar!']", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g0!mbar!"]', 'pale_yellow3', msg='step 05.1')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g1!mbar!"]', 'pale_yellow3', msg='step 05.2')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g2!mbar!"]', 'Macaroni_Cheese_1', msg='step 05.3')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g3!mbar!"]', 'Free_Speech_Red', msg='step 05.3')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g4!mbar!"]', 'Free_Speech_Red', msg='step 05.3')
        
        """
        Step 6: Click Theme drop down > select Midnight.
        Chart updated with selected theme.
        """
        designer_chart_obj.select_theme_in_format_tab('Midnight', 'Step 06.1: Verify the themes', verify_list=['Designer 2018', 'Light', 'Midnight', 'Custom...'], compare_type='asin')
        designer_chart_obj.wait_for_number_of_element("rect[fill*='#1C1E61'][class='riser!s0!g4!mbar!']", 1, designer_chart_obj.chart_medium_timesleep)
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g0!mbar!"]', 'copper', msg='step 06.1')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g1!mbar!"]', 'Kournikova', msg='step 06.2')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g2!mbar!"]', 'Cranberry', msg='step 06.3')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g3!mbar!"]', 'Midnight_blue', msg='step 06.4')
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class^="riser!s0!g4!mbar!"]', 'Midnight_blue', msg='step 06.5')
        
        """
        Step 7: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
       
if __name__ == '__main__':
    unittest.main()