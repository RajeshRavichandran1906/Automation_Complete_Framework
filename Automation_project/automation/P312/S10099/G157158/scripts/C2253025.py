'''
Created on Feb 17, 2018

@author: Sowmiya
TestSuite ID : http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2253025
TestCase Name: If 2 hierarchical dimensions in vis, drilldown on second at runtime displays wrong label
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2253025_TestClass(BaseTestCase):

    def test_C2253025(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2253025'
        visual = visualization.Visualization(self.driver)
        position=1
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.1'+' Verify x_axis title')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.2'+' Verify x_axis title')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.3'+' Verify x_axis label')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.4'+' Verify x_axis label')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.5'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("rect[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.6'+' Verify riser color')
            visual.verify_tooltip(riser_css, tooltip_list, msg='Step '+stepno+'.7'+' Verify tooltip')
            
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Double click 'Cost of Goods', 'Product,Category' & 'Product,Subcategory'
        """
        visual.double_click_on_datetree_item('Cost of Goods', position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='yaxis-lab']"
        visual.wait_for_number_of_element(element_css, expected_number=9)
        
        visual.double_click_on_datetree_item('Product,Category', position)
        element_css="#MAINTABLE_wbody1_f svg g text[class^='xaxisOrdinal-lab']"
        visual.wait_for_number_of_element(element_css, expected_number=7)
        
        visual.double_click_on_datetree_item('Product,Subcategory', position)
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 21)
        
        """
        Step 03 : Verify label values
        """
        x_axis_title=['Product Category : Product Subcategory']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Contr...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        tooltip_list=['Product Category:Camcorder', 'Product Subcategory:Professional', 'Cost of Goods:$35,218,308.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        riser_css='riser!s0!g4!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 21, '3')
        
        """
        Step 04 : Verify query pane
        """
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Category', position, msg='Step 4.1')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Product,Subcategory', position+position, msg='Step 4.2')
        visual.verify_field_listed_under_querytree('Vertical Axis', 'Cost of Goods', position, msg='Step 4.3')
        
        """
        Step 05 : Verify first and last 2 bar values (Product Category:Product Subcategory:Cost of Goods)
        """
        x_axis_title=['Product Category : Product Subcategory']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Contr...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        riser_css='riser!s0!g1!mbar!'
        tooltip_list=['Product Category:Accessories', 'Product Subcategory:Headphones', 'Cost of Goods:$51,663,564.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 21, '5')
        
        """
        Step 06 : Click Run in the toolbar
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_1 rect[class^='riser']", 21)
        
        x_axis_title=['Product Category : Product Subcategory']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Contr...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        tooltip_list=['Product Category:Camcorder', 'Product Subcategory:Professional', 'Cost of Goods:$35,218,308.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        riser_css='riser!s0!g4!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 21, '6')
        
        """
        Step 07 : hover over third bar from left (Accessories:Universal Remote) > Drill Down > Model
        """
        visual.select_tooltip('riser!s0!g2!mbar!', 'Drill down to->Model')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1 rect[class^='riser']", 4)
        
        """
        Step 08 : Verify horizontal axis label changed to product category:Model
        Step 09 : Verify tooltip values of all bar risers
        """
        x_axis_title=['Product Category : Model']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories : Logitech 1100', 'Accessories : Logitech 900', 'Accessories : Niles Audio RCAHT2', 'Accessories : Niles Audio RCATT2']
        y_axis_label=['0', '2M', '4M', '6M', '8M', '10M', '12M']
        color_name='bar_blue'
        riser_css='riser!s0!g0!mbar!'
        tooltip_list=['Product Category:Accessories', 'Model:Logitech 1100', 'Cost of Goods:$7,783,440.00', 'Filter Chart', 'Exclude from Chart', 'Remove Filter', 'Drill up to Product Subcategory', 'Drill down to Product Subcategory']
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 4, '9')
        
        visual.take_run_window_snapshot(Test_Case_ID, '9')
        
        """
        Step 10 : Close the output window
        """
        visual.switch_to_previous_window()
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 21)
        
        """
        Step 11 : Click "Save" in the toolbar > Type C2141378 > Click "Save" in the Save As dialog
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
if __name__ == '__main__':
    unittest.main() 