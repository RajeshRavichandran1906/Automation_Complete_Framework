'''
Created on Feb 27, 2018
@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2102951
Test_Case Name : Exclude from chart is not working if the Filter Prompt and Chart dimension are of same field
'''

import unittest
from common.lib import utillity
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData

class C2102951_TestClass(BaseTestCase):

    def test_C2102951(self):
        
        utillobj = utillity.UtillityMethods(self.driver)
    
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        long_wait_time_in_sec = 120
        short_wait_time_in_sec = 60
        yaxis_title_css = "#MAINTABLE_wbody1_f text[class='yaxis-title']"
        xaxis_title_css = "#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
        Filter_dialog_ok_button_css = "#avFilterOkBtn"
        no_of_riser=7
        
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title,y_title,x_label, y_label,riser,riser_color_css,total_risers,tooltip, step_num):
            visual.verify_x_axis_title(x_title, msg='Step ' + step_num + '.11')
            visual.verify_y_axis_title(y_title, msg='Step ' + step_num + '.12')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.13')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.14')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step ' + step_num + '.15')
            visual.verify_chart_color_using_get_css_property("[class*='"+riser_color_css+"']", 'bar_blue',  msg='Step ' + step_num + '.16')
            visual.verify_tooltip(riser, tooltip, msg='Step ' + step_num + '.17:'+' Verify riser tooltip')
            
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        utillobj.wait_for_page_loads(20)
        
        """
        Step02: Add Product Category and Cost of Goods to Canvas
        """
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text(xaxis_title_css, "ProductCategory", 45)
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text(yaxis_title_css, "CostofGoods", 45)
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        
        """
        Step03: Add Product Category to Filter, accept default and click Ok.
        """
        CoreMetaData.collapse_data_field_section(self, 'Filters and Variables')
        visual.right_click_on_datetree_item('Product,Category', 1, "Filter")
        visual.wait_for_number_of_element(Filter_dialog_ok_button_css, 1, short_wait_time_in_sec)
        visual.close_filter_dialog('ok')
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, short_wait_time_in_sec)
        visual.verify_field_in_filterbox('Product,Category', 1, "Step 03.01: Verify query added to filter pane")
        
        """
        Step04: Hover over on bar and choose Exclude from Chart.
        """     
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, short_wait_time_in_sec)   
        MediaPlayer_riser_css="riser!s0!g3!mbar"
        visual.select_tooltip(MediaPlayer_riser_css, "Exclude from Chart")
        
        """
        Step05: Verify the preview.
        """
        no_of_riser=6
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec) 
        expected_prompt_list=['[All]', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_show_prompt_table_list(expected_prompt_list, msg="Step 05.01: Verify Show prompt table list")
        visual.verify_item_checked_status_in_show_prompt_table('Media Player',checked_status=False, msg='Step 05.02:Verify Media Player is unchecked')
        x_title=['Product Category']
        y_title=['Cost of Goods']
        expected_xaxis_labels=['Accessories', 'Camcorder', 'Computers', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        Accessories_riser="riser!s0!g0!mbar"
        Accessories_tooltip=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        step_num='05'
        verify_bar_chart(x_title, y_title, expected_xaxis_labels, expected_yaxis_labels, Accessories_riser, Accessories_riser, no_of_riser, Accessories_tooltip, step_num)        
        
#         visual.take_preview_snapshot(Test_Case_ID, '05')        
                 
        """
        Step05: Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
#         visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main()        