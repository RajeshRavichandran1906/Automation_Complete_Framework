'''
Created on Feb 26, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10099
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2102945
TestCase Name: If 2 hierarchical dimensions in vis, drilldown on second at runtime displays wrong label
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2102945_TestClass(BaseTestCase):

    def test_C2102945(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2102945'
        visual = visualization.Visualization(self.driver)
        position=1
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.1'+' Verify x_axis title')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.2'+' Verify x_axis title')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.3'+' Verify x_axis label')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.4'+' Verify x_axis label')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.5'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.6'+' Verify riser color')
            visual.verify_tooltip(riser_css, tooltip_list, move_to_tooltip=True, msg='Step '+stepno+'.7'+' Verify tooltip')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Double click 'Cost of Goods', 'Product,Category' & 'Product,Subcategory'
        """
        field_name='Cost of Goods'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='yaxis-labels']"
        visual.wait_for_number_of_element(element_css, expected_number=9)
        
        field_name='Product,Category'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=8)
        
        field_name='Product,Subcategory'
        visual.double_click_on_datetree_item(field_name, position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=22)
        
        x_axis_title=['Product Category : Product Subcategory']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Contr...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        total_risers=21
        color_name='bar_blue'
        tooltip_list=['Product Category:Accessories', 'Product Subcategory:Headphones', 'Cost of Goods:$51,663,564.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, '2')
        
        """
        Step 03 : Run the visualization
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=22)
            
        """
        Step 04 : In output, hover over third bar from left (Accessories:Universal Remote) > Product Subcategory > Drill Down.
                    Verify it displays like follow.
        """
        universal_remote_css='riser!s0!g2!mbar!'
        visual.select_tooltip(universal_remote_css, 'Drill down to->Model')
                    
        x_axis_title=['Product Category : Model']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories : Logitech 1100', 'Accessories : Logitech 900', 'Accessories : Niles Audio RCAHT2', 'Accessories : Niles Audio RCATT2']
        y_axis_label=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        total_risers=4
        color_name='bar_blue'
        tooltip_list=['Product Category:Accessories', 'Model:Logitech 900', 'Cost of Goods:$10,017,859.00', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory', 'Drill down to Product Subcategory']
        riser_css='riser!s0!g1!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, '4')
        
        """
        Step 04 : Logout using API(without saving)
                    http://machine:port/alias/service/wf_security_logout.jsp
        """ 
        visual.switch_to_previous_window()
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal']"
        visual.wait_for_number_of_element(element_css, expected_number=22)        
        visual.save_as_visualization_from_menubar(Test_Case_ID)
#         visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main() 