'''
Created on Feb 27, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2102820
TestCase Name: Hiding the Visibility with 2 dimensions, doesn't display correct output
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2102820_TestClass(BaseTestCase):

    def test_C2102820(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2102820'
        restore_fex='C2102820_Repro'
        visual = visualization.Visualization(self.driver)
        position=1
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.1'+' Verify x_axis title')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.2'+' Verify y_axis title')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.3'+' Verify x_axis label')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.4'+' Verify y_axis label')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.5'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.6'+' Verify riser color')
            visual.verify_tooltip(riser_css, tooltip_list, msg='Step '+stepno+'.7'+' Verify tooltip')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                    http://domain.com:port/alias/ia?item=IBFS:/WFC/Repository/S10099/C2102820_Repro.fex&tool=idis
        """      
        visual.edit_visualization_using_api(restore_fex)
        
        """
        Step 02 : Add "Product,Category" to Horizontal axis
        """
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal-label']"
        visual.wait_for_number_of_element(element_css, expected_number=21)
        
        field_name='Product,Category'
        visual.drag_field_from_data_tree_to_query_pane(field_name, position, 'Horizontal Axis', position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal-label']"
        visual.wait_for_number_of_element(element_css, expected_number=21)
        
        x_axis_title=['Product Category : Product Subcategory']
        y_axis_title=['Revenue']
        x_axis_label=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Contr...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        total_risers=21
        color_name='bar_blue'
        headphones_tooltip_list=['Product Category:Accessories', 'Product Subcategory:Headphones', 'Revenue:$76,186,587.97', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        headphones_riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, headphones_tooltip_list, headphones_riser_css, color_name, total_risers, '2')
        
        """
        Step 03 : Right Click on Product SubCategory in Query Pane and change Visibility to Hide
        """
        visual.right_click_on_field_under_query_tree('Product,Subcategory', position, 'Visibility->Hide')
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal-label']"
        visual.wait_for_number_of_element(element_css, expected_number=21)
        
        x_axis_title=['Product Category']
        y_axis_title=['Revenue']
        x_axis_label=['Accessories', 'Accessories', 'Accessories', 'Camcorder', 'Camcorder', 'Camcorder', 'Computers', 'Computers', 'Media Player', 'Media Player', 'Media Player', 'Media Player', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Televisions', 'Televisions', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        total_risers=21
        color_name='bar_blue'
        headphones_tooltip_list=['Product Category:Accessories', 'Revenue:$76,186,587.97', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        headphones_riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, headphones_tooltip_list, headphones_riser_css, color_name, total_risers, '3')
        
        """
        Step 04 : Click Run and verify output
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal-label']"
        visual.wait_for_number_of_element(element_css, expected_number=21)        
        
        x_axis_title=['Product Category']
        y_axis_title=['Revenue']
        x_axis_label=['Accessories', 'Accessories', 'Accessories', 'Camcorder', 'Camcorder', 'Camcorder', 'Computers', 'Computers', 'Media Player', 'Media Player', 'Media Player', 'Media Player', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Stereo Systems', 'Televisions', 'Televisions', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M', '280M']
        total_risers=21
        color_name='bar_blue'
        access_tooltip_list=['Product Category:Accessories', 'Revenue:$76,186,587.97', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        access_riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, access_tooltip_list, access_riser_css, color_name, total_risers, '4')
        
        visual.switch_to_previous_window()
        
        """
        Step 05 : Launch the IA API to logout.
                    http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
#         visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main()