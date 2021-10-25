'''
Created on may 14, 2019

@author: Vpriya
Testcase Name : Add two measures and change the widget menu option to Split axis, Blended axis
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8261777
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity

class C8261777_TestClass(BaseTestCase):
    
    def test_C8261777(self):
        """
        Test_case variables
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utillity_obj=utillity.UtillityMethods(self.driver)
        
        x_axis_label_css="text[class*='xaxisOrdinal-labels!']"
        y_axis_label_css="text[class*='yaxis-labels!']"
        expected_x_label_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_Y_label_list=['0', '40', '80', '120', '160', '200']
        expected_split_X_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_Y1_label_list=['0', '60M', '120M', '180M', '240M']
        expected_Y2_label_list=['0', '87.5M', '175M', '262.5M', '350M']
        expected_blend_y_label_list=['0', '100M', '200M', '300M', '400M', '500M', '600M']
        
        """
        Step 1:Launch API link to create new Designer Chart using baseapp/wf_retail_lite
        http://machine:port/ibi_apps/designer?is508=false&master=baseapp%2Fwf_retail_lite&tool=chart&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313_G671774&tool=chart
        Verify new Designer Chart Created
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_text_in_heading(['Chart', 'Heading'],'Step"01.02')
        designer_chart_obj.verify_x_axis_label_in_preview(expected_x_label_list,msg="Step 01:03 verify the x axis title")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_Y_label_list,msg="Step 01:04 verify the y axis title")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', msg="Step 01:05 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s1!g0!mbar!"]', 'pale_green', msg="Step 01:06 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s2!g0!mbar!"]', 'dark_green', msg="Step 01:07 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s3!g0!mbar!"]', 'pale_yellow_2', msg="Step 01:08 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s4!g0!mbar!"]', 'brick_red', msg="Step 01:09 verify the chart colour")
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] rect[class*='riser!']", 5, 5, msg="Step 01:10 verify the number of risers")


        """
        Step 2:Expand Product and Double click Product Category.
        Expand Sales and Double click Cost of Goods, Revenue
        """
        designer_chart_obj.double_click_on_dimension_field("Product->Product->Product,Category")
        utillity_obj.synchronize_with_number_of_element(x_axis_label_css,7,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field("Sales->Cost of Goods")
        utillity_obj.synchronize_with_number_of_element(y_axis_label_css,7,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field("Revenue")
        utillity_obj.synchronize_with_number_of_element(".legend text",2,designer_chart_obj.home_page_long_timesleep)
 
        """
        Step 3:Click on the Menu Widget for Vertical Bucket
        """
        """
        Step 4:Select Split Axis option
        Verify the canvas splits into two graphs
        """
        designer_chart_obj.select_item_from_query_menu_widget("Vertical","Split axis")
        utillity_obj.synchronize_with_number_of_element('rect[class*="riser"]',14,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_number_of_risers(".chart-canvas rect[class*='riser!']", 1, 14, "Step 04:01 verify the number of risers")
        designer_chart_obj.verify_x_axis_label_in_preview(expected_split_X_label_list,msg="Step 04:02 verify the x axis title")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_Y1_label_list,msg="Step 04:03 verify the y axis title")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_Y2_label_list,xyz_axis_label_css="svg > g text[class^='y2axis-labels']",msg="Step 04:04 verify the y axis label")
        designer_chart_obj.verify_y_axis_title_in_preview(["Cost of Goods"], msg="Step 04:05 verify the y axis title")
        designer_chart_obj.verify_y_axis_title_in_preview(["Revenue"], x_or_y_axis_title_css="text[class='y2axis-title']",msg="Step 04:06 verify the y2 axis title")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g5!ay1!mbar!"]', 'bar_blue', msg="Step 04:07 verify the chart colour")
        designer_chart_obj.verify_text_in_heading(['Chart', 'Heading'],'Step"04.08')

        """
        Step 5:Click on the Menu Widget for Vertical Bucket > Select Blended Axis option
        Verify the canvas now blends the graphs into one.
        """
        designer_chart_obj.select_item_from_query_menu_widget("Vertical","Blended axis")
        utillity_obj.synchronize_until_element_disappear("text[class='y2axis-title']",designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.verify_number_of_risers(".chart-canvas rect[class*='riser!']", 1, 14, "Step 04:01 verify the number of risers")
        designer_chart_obj.verify_x_axis_label_in_preview(expected_split_X_label_list,msg="Step 04:02 verify the x axis title")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_blend_y_label_list,msg="Step 05:03 verify the y axis label")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', msg="Step 05:04 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s1!g0!mbar!"]', 'pale_green', msg="Step 05:05 verify the chart colour")
        designer_chart_obj.verify_text_in_heading(['Chart', 'Heading'],'Step"05.06')
        
        
        """
        Step 6:Click Application menu > Close > click No.
        """

        designer_chart_obj.close_designer_chart_from_application_menu()

        """
        Step 7:Launch the IA API to logout.
        http://machine:port/alias/service/wf_security_logout.jsp
        """
             
        
if __name__ == '__main__':
    unittest.main()