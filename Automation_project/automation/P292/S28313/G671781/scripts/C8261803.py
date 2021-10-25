'''
Created on May 31, 2019

@author: Vpriya
Testcase Name : Select any chart under chart picker and verify canvas reflects choice
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261803
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity

class C8261803_TestClass(BaseTestCase):
    
    def test_C8261803(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utillity_obj=utillity.UtillityMethods(self.driver)
        
        """
        Test case variables
        """
        expected_x_label_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_Y_label_list=['0', '40', '80', '120', '160', '200']
        ring_pie_label_css="text[class='totalLabel!g4!mtotalLabel!']"
        expected_pie_label_list=['75', '100', '125', '150', '175']
        expected_pie_group_label_list=['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4']
        expected_scatter_x_axis_label=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        expected_scatter_y_axis_label=['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5']
        
        """
        Step 1:Launch the API to create new Designer Chart with the CAR file
        http://machine:port/{alias}/designer?&item=IBFS:/WFC/Repository/P292_S28313/G671774&master=ibisamp/car&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('ibisamp/car')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
 
        """
        Step 2:Verify "Vertical stacked bar" is the first chart in Chart picker and it displayed by default on canvas
        """
        designer_chart_obj.verify_chart_index_on_chart_picker('vertical_stacked_bar', 0 , 'Step 02.01')
        designer_chart_obj.verify_text_in_heading(['Chart', 'Heading'],'Step"02.02')
        designer_chart_obj.verify_x_axis_label_in_preview(expected_x_label_list,msg="Step 02:03 verify the x axis title")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_Y_label_list,msg="Step 02:04 verify the y axis title")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s0!g0!mbar!"]', 'bar_blue', msg="Step 02:05 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s1!g0!mbar!"]', 'pale_green', msg="Step 02:06 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s2!g0!mbar!"]', 'dark_green', msg="Step 02:07 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s3!g0!mbar!"]', 'pale_yellow_2', msg="Step 02:08 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('rect[class="riser!s4!g0!mbar!"]', 'brick_red', msg="Step 02:09 verify the chart colour")
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] rect[class*='riser!']", 5, 5, msg="Step 02:10 verify the number of risers")
        
        """
        Step 3:Select Ring Pie
        Verify Ring pie is added to canvas
        """
        
        designer_chart_obj.select_chart_from_chart_picker("ring_pie")
        utillity_obj.synchronize_with_visble_text(ring_pie_label_css,"175",designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_text_in_heading(['Chart', 'Heading'],'Step"03.01')
        designer_chart_obj.verify_x_axis_label_in_preview(expected_pie_label_list,xyz_axis_label_css="svg > g text[class*='totalLabel']",msg="Step 03:02 verify the x axis title")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_pie_group_label_list,xyz_axis_label_css="svg > g text[class*='pieLabel!']",msg="Step 03:03 verify the y axis title")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('path[class="riser!s0!g2!mwedge!"]', 'bar_blue', msg="Step 03:04 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('path[class="riser!s1!g2!mwedge!"]', 'pale_green', msg="Step 03:05 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('path[class="riser!s2!g2!mwedge!"]', 'dark_green', msg="Step 03:06 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('path[class="riser!s3!g2!mwedge!"]', 'pale_yellow_2', msg="Step 03:07 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview('path[class="riser!s4!g2!mwedge!"]', 'brick_red', msg="Step 03:08 verify the chart colour")
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] path[class*='riser!']", 5, 5, msg="Step 03:09 verify the number of risers")
        

        """
        Step 4:Select Scatter Chart
        Verify Scatter chart is added to canvas
        """
        designer_chart_obj.select_chart_from_chart_picker("scatter_bubble")
        utillity_obj.synchronize_until_element_is_visible("circle[class='riser!s1!g2!mmarker!']",designer_chart_obj.chart_long_timesleep)
        designer_chart_obj.verify_x_axis_label_in_preview(expected_scatter_x_axis_label,xyz_axis_label_css="svg > g text[class*='xaxisNumeric-labels!']",msg="Step 04:01 verify the x axis label")
        designer_chart_obj.verify_y_axis_label_in_preview(expected_scatter_y_axis_label,xyz_axis_label_css="svg > g text[class*='yaxis-labels!']",msg="Step 04:02 verify the y axis label")
        designer_chart_obj.verify_number_of_risers("[id*='chartpreview'] circle[class*='riser!']", 1, 6, msg="Step 04:03 verify the number of risers")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview("circle[class='riser!s1!g2!mmarker!']", 'pale_green', msg="Step 04:04 verify the chart colour")
        designer_chart_obj.verify_chart_color_using_get_css_property_in_preview("circle[class='riser!s0!g2!mmarker!']", 'bar_blue', msg="Step 04:05 verify the chart colour")

        """
        Step 5:Click Application menu > Close > click No.
        """
        designer_chart_obj.close_designer_chart_from_application_menu()

 
        """
        Step 6:Logout using API:
        http://machine:port/alias/service/wf_security_logout.jsp.
        """
        
if __name__ == '__main__':
    unittest.main()