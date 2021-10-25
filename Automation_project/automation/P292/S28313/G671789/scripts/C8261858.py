'''
Created on May 17, 2019

@author: vpriya
Testcase Name : Adding variables to heading and footing
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261858
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import designer_chart
from common.lib import utillity

class C8261858_TestClass(BaseTestCase):
    
    def test_C8261858(self):
        """
        Test case objects
        """
        designer_chart_obj = designer_chart.Designer_Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        
        
        """
        Test case variables
        """
        x_axis_label_css="text[class*='xaxisOrdinal-labels!']"
        y_axis_label_css="text[class*='yaxis-labels!']"
        
        """
        Step 1: Launch the API to create new Designer Chart with the CAR file
        http://machine:port/ibi_apps/designer?&item=IBFS%3A%2FWFC%2FRepository%2FP292_S28313%2FG671774%
        2F&master=baseapp%2Fwf_retail_lite&tool=chart
        """
        designer_chart_obj.invoke_designer_chart_using_api('baseapp/wf_retail_lite')
        designer_chart_obj.wait_for_number_of_element("div[id^='chartpreview']", 1, designer_chart_obj.chart_long_timesleep)
        
        """
        Step 2: Add Product,Category and Revenue to the chart, Click on Variables tab
        """
        designer_chart_obj.double_click_on_dimension_field('Product->Product->Product,Category')
        utill_obj.synchronize_with_number_of_element(x_axis_label_css,7,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.double_click_on_measures_field('Sales->Revenue')
        utill_obj.synchronize_with_number_of_element(y_axis_label_css,8,designer_chart_obj.home_page_long_timesleep)
        designer_chart_obj.select_fields_or_variables_in_datapane('Variables')
        
        
        """
        Step 3: Select and Drag Today's date (default form) to the chart heading and drop it, 
        click next to &DATE and add 5 spaces, Drag Today's date (mm/dd/yyyy), drop it
        click next to &DATEMDYY and add 5 spaces, Drag Today's date (yyyy/mm/dd), drop it
        click next to &DATEYYMD and add 5 spaces, Drag Today's date (dd/mm/yyyy), drop it
        click next to &DATEDMYY and add 5 spaces, Drag Time of Day, drop it
        """
        designer_chart_obj.drag_variables_to_header("Today's date (default format)")
        designer_chart_obj.drag_variables_to_header("Today's date (mm/dd/yyyy)",text_to_enter= '     ')
        designer_chart_obj.drag_variables_to_header("Today's date (yyyy/mm/dd)",text_to_enter='     ')
        designer_chart_obj.drag_variables_to_header("Today's date (dd/mm/yyyy)",text_to_enter='     ')
        designer_chart_obj.drag_variables_to_header("Time of Day (hh:mm:ss)",text_to_enter='     ')
        
        """
        Step 4: click on Show options and select footing
        """
        designer_chart_obj.select_layout_option("Footing")
        
        """
        Step 5: Select and Drag Today's date (default form) to the chart footing and drop it, 
        click next to &DATE and add 5 spaces, Drag Today's date (mm/dd/yyyy), drop it
        click next to &DATEMDYY and add 5 spaces, Drag Today's date (yyyy/mm/dd), drop it
        click next to &DATEYYMD and add 5 spaces, Drag Today's date (dd/mm/yyyy), drop it
        click next to &DATEDMYY and add 5 spaces, Drag Time of Day, drop it
        """
        
        designer_chart_obj.drag_variables_to_footer("Today's date (default format)")
        designer_chart_obj.drag_variables_to_footer("Today's date (mm/dd/yyyy)",text_to_enter='     ')
        designer_chart_obj.drag_variables_to_footer("Today's date (yyyy/mm/dd)",text_to_enter='     ')
        designer_chart_obj.drag_variables_to_footer("Today's date (dd/mm/yyyy)",text_to_enter='     ')
        designer_chart_obj.drag_variables_to_footer("Time of Day (hh:mm:ss)",text_to_enter='     ')
        
        """
        Step 6:Click close icon for footing..
        """
        designer_chart_obj.close_heading_or_footing_toolbar()
        
        """
        Step 7: Run the chart and verify the heading and footing contain all the date values and time of day
        """ 
        
        designer_chart_obj.click_toolbar_item('preview')
        designer_chart_obj.verify_date_time_format_in_heading(0, 'Step 07.01: Verify the heading mm/dd/yy', date_time_format='mm/dd/yy')
        designer_chart_obj.verify_date_time_format_in_heading(1, 'Step 07.02: Verify the heading mm/dd/yyyy', date_time_format='mm/dd/yyyy')
        designer_chart_obj.verify_date_time_format_in_heading(2, 'Step 07.03: Verify the heading yyyy/mm/dd', date_time_format='yyyy/mm/dd')
        designer_chart_obj.verify_date_time_format_in_heading(3, 'Step 07.04: Verify the heading dd/mm/yyyy', date_time_format='dd/mm/yyyy')
        designer_chart_obj.verify_date_time_format_in_heading(4, 'Step 07.05: Verify the heading dd/mm/yyyy', date_time_format='hh.mm.ss')
        designer_chart_obj.verify_date_time_format_in_footing(0, 'Step 07.06: Verify the footing mm/dd/yy', date_time_format='mm/dd/yy')
        designer_chart_obj.verify_date_time_format_in_footing(1, 'Step 07.07: Verify the footing mm/dd/yyyy', date_time_format='mm/dd/yyyy')
        designer_chart_obj.verify_date_time_format_in_footing(2, 'Step 07.08: Verify the footing yyyy/mm/dd', date_time_format='yyyy/mm/dd')
        designer_chart_obj.verify_date_time_format_in_footing(3, 'Step 07.09: Verify the footing dd/mm/yyyy', date_time_format='dd/mm/yyyy')
        designer_chart_obj.verify_date_time_format_in_footing(4, 'Step 07.10: Verify the footing dd/mm/yyyy', date_time_format='hh.mm.ss')
        designer_chart_obj.go_back_to_design_from_preview()
        
        """
        Step 8: Sign out using API:
        http://machine:port/ibi_apps/service/wf_security_logout.jsp.
        """
        
if __name__ == '__main__':
    unittest.main()