'''
Created on Feb 20, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2253026
TestCase Name: VIS:Runtime:Drilldown on "By" field followed by drilldown on color display wrong labels and value
'''
import unittest
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase

class C2253028_TestClass(BaseTestCase):

    def test_C2253028(self):
        
        """
        TESTCASE OBJECT
        """
        visual = visualization.Visualization(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253028'
        position=1
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, legend_list, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.1'+' Verify x_axis title')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.2'+' Verify y_axis title')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.3'+' Verify x_axis label')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.4'+' Verify x_axis label')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.5'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class*='"+riser_css+"']", color_name, msg='Step '+stepno+'.6'+' Verify riser color')
            visual.verify_tooltip(riser_css, tooltip_list, msg='Step '+stepno+'.7'+' Verify tooltip')
            visual.verify_legends(legend_list, "#MAINTABLE_wbody1", msg='Step '+stepno+'.8'+' Verify x_axis title')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Add revenue(vertical-axis),Product category(horizontal-axis) and Store business Region to Color
        """
        field_name="Revenue"
        visual.drag_field_from_data_tree_to_query_pane(field_name, position, 'Vertical Axis', position)
        element_css="#MAINTABLE_wbody1_f g text[class='yaxis-title']"
        visual.wait_for_visible_text(element_css, 'Revenue')
           
        field_name="Product,Category"
        visual.drag_field_from_data_tree_to_query_pane(field_name, position, 'Horizontal Axis', position)
        element_css="#MAINTABLE_wbody1_f g text[class='xaxisOrdinal-title']"
        visual.wait_for_visible_text(element_css, 'ProductCategory')
           
        field_name="Store,Business,Region"
        visual.drag_field_from_data_tree_to_query_pane(field_name, position, 'Color', position)
        element_css="#TableChart_1 rect[class^='riser']"
        visual.wait_for_number_of_element(element_css, expected_number=28)
           
        """
        Verify Vertical axis label, horizontal axis label and color legend title:
        Step 03 : Hover over EMEA: Accessories bar.
        Verify tooltip
        """
        x_axis_title=['Product Category']
        y_axis_title=['Revenue']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        color_name=['bar_blue', 'pale_green', 'pale_yellow']
        legend_list=['Store Business Region', 'EMEA', 'North America', 'Oceania', 'South America']
        riser_css=['riser!s0!g0!mbar!', 'riser!s1!g2!mbar!', 'riser!s3!g4!mbar!']
        tooltip_list=['Product Category:Accessories', 'Revenue:$51,791,709.98', 'Store Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Drill down to']
        visual.verify_chart_color_using_get_css_property("[class*='"+riser_css[1]+"']", color_name[1], msg='Step 02.01: Verify riser color')
        visual.verify_chart_color_using_get_css_property("[class*='"+riser_css[2]+"']", color_name[2], msg='Step 02.02: Verify riser color')
        
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, legend_list, tooltip_list, riser_css[0], color_name[0], 28, '02')
        
        """
        Step 4 : Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", expected_number=28)
        
        """
        Step 5 : Hover over on any bar(Media player) and click > Drilldown > Product Subcategory.
        """
        visual.select_tooltip('riser!s0!g3!mbar!', 'Drill down to->Product Subcategory')
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", expected_number=4)   

        """
        Verify category drill down to product subcategory
        """
        x_axis_title=['Product Subcategory']
        y_axis_title=['Revenue']
        x_axis_label=['Blu Ray', 'DVD Players', 'DVD Players - Portable', 'Streaming']
        y_axis_label=['0', '20M', '40M', '60M', '80M', '100M']
        color_name='bar_blue'
        legend_list=['Store Business Region', 'EMEA']
        riser_css='riser!s0!g0!mbar!'
        tooltip_list=['Product Subcategory:Blu Ray', 'Revenue:$93,319,634.69', 'Store Business Region:EMEA', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Category', 'Drill down to']
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, legend_list, tooltip_list, riser_css, color_name, 4, '05')
        
        
        """ion
        Step 6 : hover over on any bar (Blu Ray) and click >Drilldown > store business subregion.
        """
        visual.select_tooltip('riser!s0!g0!mbar!', 'Drill down to->Store Business Sub Region',xoffset=5, yoffset=5)
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", expected_number=3)
        
       
        
        """
        Verify legend title displays as "Store Business Sub Region".
        Step 7 : Hover on light green color bar.
        Verify the tool tip:
        """
        x_axis_title=['Product Subcategory']
        y_axis_title=['Revenue']
        x_axis_label=['Blu Ray']
        y_axis_label=['0', '20M', '40M', '60M', '80M', '100M']
        color_name=['pale_green', 'dark_green']
        legend_list=['Store Business Sub Region', 'Africa', 'Asia', 'Europe']
        riser_css=['riser!s1!g0!mbar!', 'riser!s2!g0!mbar!']
        tooltip_list=['Product Subcategory:Blu Ray', 'Revenue:$5,922,195.46', 'Store Business Sub Region:Asia', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to', 'Drill down to']
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, legend_list, tooltip_list, riser_css[0], color_name[0], 3, '07')
        
        """
        Step 8 : Close the output window
        """
        visual.switch_to_previous_window()
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", expected_number=28)
        
        """
        Step 9 : Click "Save" in the toolbar > Type C2141382 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", expected_number=28)
        
if __name__ == '__main__':
    unittest.main() 