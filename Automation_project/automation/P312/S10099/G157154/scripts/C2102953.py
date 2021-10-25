'''
Created on Feb 23, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2102953
TestCase Name: Restore Original doesn't restore correctly
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2102953_TestClass(BaseTestCase):

    def test_C2102953(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2102953'
        visual = visualization.Visualization(self.driver)
        position=1
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.1')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.2')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.3')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.4')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.5')
            visual.verify_chart_color_using_get_css_property("[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.6')
            visual.verify_tooltip(riser_css, tooltip_list, move_to_tooltip=True, msg='Step '+stepno+'.7'+' Verify tooltip')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Double click "Cost of Goods" & "Product, Category"
        """
        field_name='Cost of Goods'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='yaxis-labels']"
        visual.wait_for_number_of_element(element_css, expected_number=9)
        
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=8)
        
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        total_risers=7
        color_name='bar_blue'
        camcorder_tooltip_list=['Product Category:Camcorder', 'Cost of Goods:$104,866,857.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        camcorder_riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, camcorder_tooltip_list, camcorder_riser_css, color_name, total_risers, '2')
        
        """
        Step 03 : Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=8)
            
        """
        Step 04 : Hover over on Media player riser
        Step 05 : Click "Drill down to Product, Subcategory"
        """
        media_player_css='riser!s0!g3!mbar!'
        visual.select_tooltip(media_player_css, 'Drill down to Product Subcategory')
        
        """
        Step 06 : Verify "Product, subcategory" values displayed
        """
        x_axis_title=['Product Subcategory']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        total_risers=4
        color_name='bar_blue'
        blu_ray_tooltip_list=['Product Subcategory:Blu Ray', 'Cost of Goods:$181,112,921.00', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Category', 'Drill down to Model']
        blu_ray_riser_css='riser!s0!g0!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, blu_ray_tooltip_list, blu_ray_riser_css, color_name, total_risers, '6')
        
        """
        Step 07 : Select Restore to Original from the UI(2nd icon) at the bottom right of output window.
        """
        visual.select_bottom_right_run_menu_options('reset')
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=8)        
        
        """
        Step 08 : Verify chart restored to Product, Category
        """
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        total_risers=7
        color_name='bar_blue'
        access_tooltip_list=['Product Category:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        access_riser_css='riser!s0!g0!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, access_tooltip_list, access_riser_css, color_name, total_risers, '8')
        
        """
        Step 09 : Close run window
        """
        visual.switch_to_previous_window()
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=8)  
        
        """
        Step 10 : Logout using API(without saving)
                    http://machine:port/alias/service/wf_security_logout.jsp
        """     
        visual.save_as_visualization_from_menubar(Test_Case_ID)
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main() 