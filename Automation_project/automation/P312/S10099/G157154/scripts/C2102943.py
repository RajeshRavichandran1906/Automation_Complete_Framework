'''
Created on Feb 28, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2102943
Test_Case Name : Filter without value is created when filter on cell in heatmap
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.lib import utillity

class C2102943_TestClass(BaseTestCase):

    def test_C2102943(self):
        
        Test_Case_ID = "C2102943"
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        long_wait_time_in_sec = 120
        short_wait_time_in_sec = 60
        xaxis_title_css = "#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        no_of_riser=244
        
        util_obj= utillity.UtillityMethods(self.driver)
        visual = visualization.Visualization(self.driver)
        
        def verify_heatmap_chart(xy_axis_title, xaxis_label, zaxis_label, legend_list, riser, riser_color_css, total_risers, tooltip, step_num):
            visual.verify_x_axis_title(xy_axis_title, msg='Step ' + step_num + '.1:'+' Verify X and Y axis titles')
            visual.verify_x_axis_label(xaxis_label, msg='Step ' + step_num + '.2'+' Verify X label')
            visual.verify_z_axis_label(zaxis_label, msg='Step ' + step_num + '.3'+' Verify Z label')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step ' + step_num + '.4:'+' Verify number of risers')
            visual.verify_legends(legend_list, msg='Step ' + step_num + '.5'+' Verify the legends')
            visual.verify_chart_color_using_get_css_property("[class*='"+riser_color_css+"']", 'persian_red',  msg='Step ' + step_num + '.6:'+' Verify riser color')
            visual.verify_tooltip(riser, tooltip, msg='Step ' + step_num + '.7:'+' Verify riser tooltip')
            
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        util_obj.wait_for_page_loads(20)
        
        """
        Step02: Click Change > Heatmap
        """
        visual.change_chart_type('heatmap')
        
        """
        Step03: Add Product,Subategory to Horizontal axis
        Step04: Add Sale,Month to Vertical axis
        Step05: Add Revenue to Color bucket
        """
        visual.right_click_on_datetree_item('Product,Subcategory', 1, 'Add To Query->Horizontal Axis')
        visual.wait_for_visible_text(xaxis_title_css, "ProductSubcategory", short_wait_time_in_sec)
        visual.right_click_on_datetree_item('Sale,Month', 1, 'Add To Query->Vertical Axis')
        visual.double_click_on_datetree_item('Sale,Month', 1)
        visual.wait_for_number_of_element(xaxis_title_css, 2, short_wait_time_in_sec)
        
        visual.right_click_on_datetree_item('Revenue', 1, 'Add To Query->Color')
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        
        """
        Step06: Hover over a value > Filter Chart
        """       
        CRTTV_3rdMonth_css="riser!s2!g2!mbar"
        visual.select_tooltip(CRTTV_3rdMonth_css, "Filter Chart")
        no_of_riser=1
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, short_wait_time_in_sec)
        
        """
        Step07: Notice the preview is displays like below
        """
        xy_axis_title = ['Product Subcategory', 'Sale Month']
        xaxis_label = ['CRT TV']
        zaxis_label = ['3']
        legend_list = ['Revenue', '232K', '234.6K', '237.2K', '239.8K', '242.4K']
        CRTTV_3rdMonth_riser_css = "riser!s0!g0!mbar"
        tooltip = ['Revenue:$232,000.79', 'Sale Month:3', 'Product Subcategory:CRT TV', 'Drill up to', 'Drill down to']
        step_num = "07"
        verify_heatmap_chart(xy_axis_title, xaxis_label, zaxis_label, legend_list, CRTTV_3rdMonth_riser_css, CRTTV_3rdMonth_riser_css, no_of_riser, tooltip, step_num)
        
#         visual.take_preview_snapshot(Test_Case_ID, '07')        
                 
        """
        Step08: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        
