'''
Created on January 4, 2019

@author:Vpriya

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/5832115
TestCase Name = Verify 3D Connected Series Area in others tab under Format menu.
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.lib import utillity
from common.wftools import chart
from common.wftools import active_chart
from selenium.webdriver.support.color import Color

class C5832115_TestClass(BaseTestCase):

    def test_C5832115(self):
        
        """
            TESTCASE variables
        """
        
        active_chart_obj=active_chart.Active_Chart(self.driver)
        chart_obj=chart.Chart(self.driver)
        utill_obj=utillity.UtillityMethods(self.driver)
        preview_parent_css="TableChart_1"
        short_time=45
        expected_xlabel_list=['Biscotti', 'Capuccino', 'Coffee Grinder', 'Coffee Pot', 'Croissant', 'Espresso', 'Latte', 'Mug', 'Scone', 'Thermos']
        expected_Ylabel_list=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        expected_xtitle_list=['Product']
        run_exp_chart_title='Dollar Sales, Unit Sales BY Product'
        expected_legend_list=['Dollar Sales', 'Unit Sales']
        expected_Xlabel_preview=['Capuccino', 'Espresso']
        expected_ylabel_preview=['0', '500,000', '1,000,000', '1,500,000', '2,000,000', '2,500,000', '3,000,000', '3,500,000', '4,000,000']
        blue_preview_risier="#TableChart_1 path[class='riser!s0!g0!mbar!']"
        green_preview_risier="#TableChart_1 path[class='riser!s1!g0!mbar!']"
        expected_legend_list_preview=['Dollar Sales', 'Unit Sales']
        expected_3d_Ylabel_list=['0', '2,000,000', '4,000,000', '6,000,000', '8,000,000', '10,000,000', '12,000,000']
        blue_run_risier="#MAINTABLE_wbody0_f path[class='riser!s0!g0!mbar!']"
        green_run_risier="#MAINTABLE_wbody0_f path[class='riser!s1!g0!mbar!']"
        
        
        """
        Step 1:Sign in to WebFOCUS
        http://machine:port/{alias}
        """
        """
        Step 2:Execute following URL to create Chart
        http://machine:port/{alias}/ia?tool=chart&master=ibisamp/ggsales&item=IBFS%3A%2FWFC%2FRepository%2FS18035%2F
        """
        active_chart_obj.invoke_chart_tool_using_api('ibisamp/ggsales')
        
        
        """
        Step 3:Change output format to Active Reports
        """
        chart_obj.change_output_format_type('active_report')
         
        """
        Step 4:Add fields Product, Dollar Sales, Unit Sales.
        """
        
        field_name1='Product'
        field_name2='Dollar Sales'
        field_name3='Unit Sales'
        
        chart_obj.double_click_on_datetree_item(field_name1,1)
        css1="#"+preview_parent_css+" text[class='xaxisOrdinal-title']"
        chart_obj.wait_for_visible_text(css1, field_name1,short_time)
        
        chart_obj.double_click_on_datetree_item(field_name2,1)
        css2="#"+preview_parent_css+" text[class='yaxis-title']"
        chart_obj.wait_for_visible_text(css2, field_name2,short_time)
        
        chart_obj.double_click_on_datetree_item(field_name3,1)
        css3="#"+preview_parent_css+" text[class='legend-labels!s1!']"
        chart_obj.wait_for_visible_text(css3, field_name3,short_time)
        
        """
        Step 5:Click the Run button.
        Expect to see the following Bar Chart.
        """
        chart_obj.run_chart_from_toptoolbar()
        utill_obj.switch_to_frame(pause=2)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_xlabel_list,msg="Step:5.1")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_Ylabel_list,msg="Step:5.2")
        active_chart_obj.verify_x_axis_title_in_run_window(expected_xtitle_list,msg="Step:5.3")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step:05.04", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list,legend_length=2,msg="Step:05.5")
        active_chart_obj.verify_number_of_risers_in_run_window('rect', 1,20,msg="Step:05.6")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mbar!']", "bar_blue", parent_css='#MAINTABLE_wbody0',msg="Step 05:07")
        active_chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s1!g0!mbar!']", "pale_green", parent_css='#MAINTABLE_wbody0',msg="Step 05:08")
        
        """
        Step 6:Select Format > Other.
        From Select a chart pop up choose 
        3D Bars.
        Click OK.
        Expect to see the Clustered bar chart converted into the Preview pane for 3D connected_series.
        """
        utill_obj.switch_to_default_content()
        chart_obj.select_ia_ribbon_item('Format', 'Other')
        chart_obj.select_other_chart_type('threed', 'threed_connected_series_area', 9)
        active_chart_obj.verify_x_axis_label_in_preview(expected_Xlabel_preview,msg="Step:6.1")
        active_chart_obj.verify_y_axis_label_in_preview(expected_ylabel_preview,msg="Step:6.2")
        active_chart_obj.verify_y_axis_label_in_preview(['Dollar Sales', 'Unit Sales'], parent_css='#TableChart_1', xyz_axis_label_css="text[class*='zaxisOrdinal-labels!']",msg="Step:6.3")
        active_chart_obj.verify_legends_in_preview(expected_legend_list_preview,legend_length=2, msg="Step:6.3")
        blue_risers = utill_obj.validate_and_get_webdriver_objects(blue_preview_risier, 'blue-riser')
        actual_color = Color.from_string(utill_obj.get_element_css_propery(blue_risers[4], 'fill')).rgba
        expected_color = utill_obj.color_picker('bar_blue', 'rgba')
        utill_obj.asequal(actual_color, expected_color, 'Step 3.5: Verify the blue coloured riser')
        green_risers = utill_obj.validate_and_get_webdriver_objects(green_preview_risier, 'green-riser')
        actual_color = Color.from_string(utill_obj.get_element_css_propery(green_risers[4], 'fill')).rgba
        expected_color = utill_obj.color_picker('pale_green', 'rgba')
        utill_obj.asequal( actual_color, expected_color, 'Step 3.6: Verify the green coloured riser')
        
        """
        Step 7:Click the Run button.
        Expect to see the following 3D Bars.
        """
        chart_obj.run_chart_from_toptoolbar()
        utill_obj.switch_to_frame(pause=2)
        active_chart_obj.verify_x_axis_label_in_run_window(expected_xlabel_list,msg="Step:7.1")
        active_chart_obj.verify_y_axis_label_in_run_window(expected_3d_Ylabel_list,msg="Step:7.2")
        active_chart_obj.verify_chart_title(run_exp_chart_title, msg="Step:07.04", parent_css="#MAINTABLE_wbody0_ft")
        active_chart_obj.verify_legends_in_run_window(expected_legend_list,legend_length=2,msg="Step:07.5")
        active_chart_obj.verify_number_of_risers_in_run_window('path', 1,120,msg="Step:07.6")
        blue_risers = utill_obj.validate_and_get_webdriver_objects(blue_run_risier, 'blue-riser')
        actual_color = Color.from_string(utill_obj.get_element_css_propery(blue_risers[4], 'fill')).rgba
        expected_color = utill_obj.color_picker('bar_blue', 'rgba')
        utill_obj.asequal(actual_color, expected_color, 'Step 3.5: Verify the blue coloured riser')
        green_risers = utill_obj.validate_and_get_webdriver_objects(green_run_risier, 'green-riser')
        actual_color = Color.from_string(utill_obj.get_element_css_propery(green_risers[4], 'fill')).rgba
        expected_color = utill_obj.color_picker('pale_green', 'rgba')
        utill_obj.asequal( actual_color, expected_color, 'Step 3.6: Verify the green coloured riser')
        
        
        """
        Step 8:Dismiss the window and logout.
        http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """

if __name__ == '__main__':
    unittest.main()
