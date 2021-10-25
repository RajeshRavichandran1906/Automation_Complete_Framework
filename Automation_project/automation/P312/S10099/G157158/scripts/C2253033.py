'''
Created on Feb 22, 2018

@author: Sowmiya
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2253033
TestCase Name: Field improperly appearing on Drill menu in Visualization
'''
import unittest
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase
from common.pages.core_metadata import CoreMetaData

class C2253033_TestClass(BaseTestCase):

    def test_C2253033(self):
        
        """
        Class Objects
        """
        core_meta = CoreMetaData(self.driver)
        visual = visualization.Visualization(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253033'
        position=1
        
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : In Home tab > Select Change drop down > Click on Bubble chart.
        """
        visual.change_chart_type('bubble_chart')
        
        """
        Step 03 : Drag and drop "Quantity,Sold" to Vertical Axis and "Revenue" to Horizontal Axis.
        """
        visual.drag_field_from_data_tree_to_query_pane('Quantity,Sold', position, 'Vertical Axis', position)
        element_css="#MAINTABLE_wbody1_f g[class='markers'] circle[class^='riser']"
        visual.wait_for_number_of_element(element_css, expected_number=1)
        visual.drag_field_from_data_tree_to_query_pane('Revenue', position, 'Horizontal Axis', position)
        element_css="[class*='xaxisNumeric-title']"
        visual.wait_for_number_of_element(element_css, expected_number=1)
        
        """
        Step 04 : Place "Gross Profit" to Size, "Product Name" to Detail and "Product,Category" to Color.
        """
        visual.right_click_on_datetree_item('Gross Profit', 1, 'Add To Query->Size')
        element_css="#MAINTABLE_wbody1_f svg g text[class^='sizeLegend']"
        visual.wait_for_number_of_element(element_css, expected_number=2)
        
        core_meta.collapse_data_field_section('Filters and Variables')
        
        visual.right_click_on_datetree_item('Product Name', 1, 'Add To Query->Detail')
        element_css="#MAINTABLE_wbody1_f g[class='markers'] circle[class^='riser']"
        visual.wait_for_number_of_element(element_css, expected_number=157)
        
        visual.right_click_on_datetree_item('Product,Category', 1, 'Add To Query->Color')
        element_css="#MAINTABLE_wbody1_f svg g text[class^='legend-label']"
        visual.wait_for_number_of_element(element_css, expected_number=7)
        
        """
        Verify label values (Revenue, Quantity,Sold) and color legend title (Product,category)
        """
        x_axis_title=['Revenue']
        y_axis_title=['Quantity Sold']
        x_axis_label=['0', '4M', '8M', '12M', '16M']
        y_axis_label=['0', '10K', '20K', '30K', '40K', '50K', '60K']
        color_name='dark_green'
        legend_list=['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production', 'Gross Profit']
        riser_css='riser!s2!g9!mmarker!'
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 circle[class*='riser!s2!g9!mmarker!']", expected_number=1)
        visual.verify_x_axis_title(x_axis_title, msg='Step 04.01: Verify x_axis title')
        visual.verify_y_axis_title(y_axis_title, msg='Step 04.02: Verify x_axis title')
        visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step 04.03: Verify x_axis label')
        visual.verify_y_axis_label(y_axis_label, msg='Step 04.04: Verify x_axis label')
        visual.verify_chart_color_using_get_css_property("circle[class='"+riser_css+"']", color_name, msg='Step 04.05: Verify riser color')
        visual.verify_legends(legend_list, legend_length=8, msg='Step 04.06')
              
        """
        Step 5 : Hover on any bubble.
        Example: Hover on product name of "Sony Xperia 16 GB 9.4-Inch Tablet S" bubble.
        Verify the tool tip:
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        tooltip_list=['Revenue:$6,002,404.30', 'Quantity Sold:20,931', 'Gross Profit:$2,381,341.30', 'Product Category:Computers', 'Product Name:Sony Xperia 16 GB 9.4-Inch Tablet S', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Subcategory']
        riser_css='riser!s2!g9!mmarker!'
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 circle[class*='riser!s2!g9!mmarker!']", expected_number=1)
        visual.verify_tooltip(riser_css, tooltip_list, msg='Step 05.01: Verify tooltip')
        
        """
        Step 6 : Close the output window.
        """
        visual.switch_to_previous_window()
        
        """
        Step 7 : Click "Save" in the toolbar > Type C2141611 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 8 : Logout of the IA API using the following URL.
        """
        
if __name__ == '__main__':
    unittest.main() 