'''
Created on Dec 26, 2018

@author: Magesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6419838
Test Case Title =  Verify Pyramid Chart in others tab under Format menu.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.active_chart import Active_Chart
from common.wftools import chart
from common.lib import utillity

class C6419838_TestClass(BaseTestCase):

    def test_C6419838(self):
       
        """
        CLASS OBJECTS
        """
        active_chart = Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        
        """
        COMMON VARIABLES
        """
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 40
        SHORT_TIME = 10
        preview_parent_css="TableChart_1"
        
        """
        STEP 01 : Log in to WebFOCUS http://machine:port/{alias}
        STEP 02 : Execute following URL to create Chart 
        http://machine:port/{alias}/ia?tool=chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FP116%2FS7074%2F
        """
        active_chart.invoke_chart_tool_using_api('ibisamp/ggsales')
        active_chart.wait_for_visible_text("text[class='legend-labels!s0!']", 'Series 0', LONG_WAIT_TIME)
        
        """
        Change output format to Active Reports
        """
        active_chart.change_output_format_type('active_report')
        active_chart.wait_for_visible_text("#HomeFormatType", 'Active Report', SHORT_TIME)
        
        """
        Expect to see the following Live Preview pane, with the default Vertical Column Bar Chart on the canvas
        """
        active_chart.verify_x_axis_label_in_preview(['Group 0', 'Group 1', 'Group 2', 'Group 3', 'Group 4'], msg='Step 02.01')
        active_chart.verify_y_axis_label_in_preview(['0', '10', '20', '30', '40', '50'], msg='Step 02.02')
        active_chart.verify_legends_in_preview(['Series 0', 'Series 1', 'Series 2', 'Series 3', 'Series 4'], msg='Step 02.03')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 25, msg='Step 02.04: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#TableChart_1', msg='Step 02.05')
        
        """
        STEP 03 : Add fields Product, Dollar Sales.
        """
        active_chart.double_click_on_datetree_item('Product', 1)
        active_chart.wait_for_visible_text("text[class^='xaxis'][class$='title']", 'Product', MEDIUM_WAIT_TIME)
        
        active_chart.double_click_on_datetree_item('Dollar Sales', 1)
        active_chart.wait_for_visible_text("text[class='yaxis-title']", 'Dollar Sales', MEDIUM_WAIT_TIME)
        
        """
        STEP 03.1 : Expect to see the following Preview.
        """
        active_chart.verify_x_axis_label_in_preview(['Capuccino', 'Espresso'], msg='Step 03.01')
        active_chart.verify_y_axis_label_in_preview(['0', '0.5M', '1M', '1.5M', '2M', '2.5M', '3M', '3.5M', '4M'], msg='Step 03.02')
        active_chart.verify_x_axis_title_in_preview(['Product'], msg='Step 03.3')
        active_chart.verify_y_axis_title_in_preview(['Dollar Sales'], msg='Step 03.4')
        active_chart.verify_number_of_risers_in_preview('rect', 1, 2, msg='Step 03.5: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#pfjTableChart_1', msg='Step 03.6')
        
        """
        STEP 04 : Click the Run button.
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f rect[class*='riser!']", 10, MEDIUM_WAIT_TIME)
        
        """
        STEP 04.1 : Expect to see the following Bar Chart.
        """
        active_chart.verify_x_axis_label_in_run_window(['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], msg='Step 04.1')
        active_chart.verify_y_axis_label_in_run_window(['0', '2M', '4M', '6M', '8M', '10M', '12M'], msg='Step 04.2')
        active_chart.verify_number_of_risers_in_run_window('rect', 1, 10, msg='Step 04.3: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("rect[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='#MAINTABLE_wbody0', msg='Step 04.4')
        active_chart.verify_x_axis_title_in_run_window(['Product'], msg='Step 04.5')
        active_chart.verify_y_axis_title_in_run_window(['Dollar Sales'], msg='Step 04.6')
        active_chart.verify_chart_title('Dollar Sales BY Product', msg='Step 04.7', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 04.8', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
        
        """
        Step 05 : Select Format > Other.
        Select the Special chart menu group.
        From the Special charts, select Pyramid Chart.
        Click OK.
        """
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        active_chart.select_other_chart_type('special', 'pyramid', 7)
        active_chart.wait_for_number_of_element("#"+preview_parent_css+" path[class*='riser!']", 2, MEDIUM_WAIT_TIME)
        
        """
        STEP 05.1 : Expect to see the Clustered bar chart converted into the Preview pane for Pyramid Chart.
        """
        utillobj.verify_element_text('#pfjTableChart_1 text[transform]','Dollar Sales', msg='Step 05.1: Verify x-axis title')
        active_chart.verify_legends_in_preview(['Product', 'Capuccino', 'Espresso'], msg='Step 05.2')
        active_chart.verify_number_of_risers('#TableChart_1 path', 2, 1, msg='Step 05.3: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mriser!']", 'bar_blue', parent_css='#pfjTableChart_1', msg='Step 05.4')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!mriser!']", 'pale_green', parent_css='#pfjTableChart_1', msg='Step 05.5')
        
        """
        STEP 06 : Click the Run button.
        """
        active_chart.run_chart_from_toptoolbar()
        active_chart.switch_to_frame()
        active_chart.wait_for_number_of_element("#MAINTABLE_wbody0_f path[class*='riser!']", 10, MEDIUM_WAIT_TIME)
        
        """
        STEP 06.1 : Expect to see the following Pyramid Chart.
        """
        utillobj.verify_element_text('#MAINTABLE_wbody0_f text[transform]','Dollar Sales', msg='Step 06.1: Verify x-axis title')
        active_chart.verify_number_of_risers_in_run_window('path', 10, 1, msg='Step 06.2: Verify number of bar risers')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s0!g0!mriser!']", 'bar_blue', parent_css='#MAINTABLE_wbody0_f', msg='Step 06.3')
        active_chart.verify_chart_color_using_get_css_property_in_preview("path[class='riser!s1!g0!mriser!']", 'pale_green', parent_css='#MAINTABLE_wbody0_f', msg='Step 06.4')
        active_chart.verify_legends_in_run_window(['Product', 'Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos'], msg='Step 06.5')
        active_chart.verify_chart_title('Dollar Sales BY Product', msg='Step 06.6', parent_css='#MAINTABLE_wbody0_ft')
        active_chart.verify_active_chart_toolbar(['More Options', 'Advanced Chart', 'Original Chart', 'Aggregation', 'Sum'], msg='Step 06.7', parent_css='#MAINTABLE_wmenu0')
        active_chart.switch_to_default_content()
        
        """
        Step 07 : Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        
if __name__ == '__main__':
    unittest.main()