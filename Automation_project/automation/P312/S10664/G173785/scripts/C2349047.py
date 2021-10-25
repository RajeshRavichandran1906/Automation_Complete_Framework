'''
Created on Feb 08, 2018

@author: Sowmiya
TestSuite Name : 8202 New Features and product changes for existing functionality 
TestSuite ID : http://172.19.2.180/testrail/index.php?/suites/view/10664&group_by=cases:section_id&group_order=asc&group_id=173783
TestCase ID : 172.19.2.180/testrail/index.php?/cases/view/2349047
TestCase Name: Group added to drill hierarchy when not in query
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2349047_TestClass(BaseTestCase):

    def test_C2349047(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2349047'
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, total_risers, stepno):        
            visual.verify_x_axis_title(x_axis_title, msg='Step '+stepno+'.1'+' Verify x_axis title')
            visual.verify_y_axis_title(y_axis_title, msg='Step '+stepno+'.2'+' Verify x_axis title')
            visual.verify_x_axis_label(x_axis_label, xyz_axis_label_length=10, msg='Step '+stepno+'.3'+' Verify x_axis label')
            visual.verify_y_axis_label(y_axis_label, msg='Step '+stepno+'.4'+' Verify x_axis label')
            visual.verify_number_of_risers("#MAINTABLE_wbody1_f g[class='risers'] [class^='riser']", 1, total_risers, msg='Step '+stepno+'.5'+' Verify number of risers')
            visual.verify_chart_color_using_get_css_property("[class='"+riser_css+"']", color_name, msg='Step '+stepno+'.6'+' Verify riser color')
            visual.verify_tooltip(riser_css, tooltip_list, msg='Step '+stepno+'.7'+' Verify tooltip')
    
        """
        Step 01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
                http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """      
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
        Step 02 : Double click "Cost of Goods", "Product, Category" and "Product, Subcategory"
        """
        visual.double_click_on_datetree_item('Cost of Goods', 1)
        visual.wait_for_visible_text("#TableChart_1 text[class='yaxis-title']", "Cost of Goods")
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser']", 7)
        visual.double_click_on_datetree_item('Product,Subcategory', 1)
        visual.wait_for_number_of_element("#TableChart_1 rect[class^='riser!']", 21)
        
        x_axis_title=['Product Category : Product Subcategory']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories : Charger', 'Accessories : Headphones', 'Accessories : Universal Remote Contr...', 'Camcorder : Handheld', 'Camcorder : Professional', 'Camcorder : Standard', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        tooltip_list=['Product Category:Camcorder', 'Product Subcategory:Professional', 'Cost of Goods:$35,218,308.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        riser_css='riser!s0!g4!mbar!'
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 21, '1')
        
        """
        Step 03 : Lasso first four risers 
        """
        source="#MAINTABLE_wbody1_f [class='riser!s0!g0!mbar!']"
        source_element=self.driver.find_element_by_css_selector(source)
        target="#MAINTABLE_wbody1_f [class='riser!s0!g3!mbar!']"
        target_element=self.driver.find_element_by_css_selector(target)
        visual.create_lasso(source_element, target_element,source_yoffset=30,source_element_location='bottom_middle',target_element_location='middle')
        """
        Step 04 : Click "Group Product, Category Selection" 
        """
         
        visual.select_lasso_tooltip('Group Product,Category Selection')
        visual.wait_for_visible_text("#TableChart_1 text[class='xaxisOrdinal-title']", "PRODUCT_CATEGORY_1 : Product Subcategory")
        """
        Step 05 : Verify Group "PRODUCT_CATEGORY_1" created
        """ 
        x_axis_title=['PRODUCT_CATEGORY_1 : Product Subcategory']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories and Camcorder : Charger', 'Accessories and Camcorder : Handheld', 'Accessories and Camcorder : Headp...', 'Accessories and Camcorder : Profess...', 'Accessories and Camcorder : Standard', 'Accessories and Camcorder : Univers...', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray', 'Media Player : DVD Players', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Boom Box', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : CRT TV', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'Product Subcategory:Standard', 'Cost of Goods:$49,071,633.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        riser_css="riser!s0!g4!mbar!"
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 21, '5')
        
        """
        Step 06 : Right click on "Product, Subcategory" in query pane > Create group 
        """ 
        visual.right_click_on_field_under_query_tree("Product,Subcategory", 1, 'Create Group...')
        parent_css="div[id^='QbDialog'] [class*='active'] [class*='caption']"
        visual.wait_for_number_of_element(parent_css, 1)

        expected_grid_value_list=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming']
        visual.verify_group_grid_values(expected_grid_value_list, msg='Step 6.1 : Verify group values')
        
        """
        Step 07 : Multi select first 5 values and click Group 
        Step 08 : Click OK
        """ 
        value_list_for_group=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players']
        visual.slect_group_grid_values(value_list_for_group)
        visual.create_group_options('Group')
        visual.exit_group_dialog('ok')
        
        visual.wait_for_visible_text("#TableChart_1 text[class='xaxisOrdinal-title']", 'PRODUCT_CATEGORY_1 : PRODUCT_SUBCATEG_1')
         
        """
        Step 09 : Verify following preview displayed
        """
        x_axis_title=['PRODUCT_CATEGORY_1 : PRODUCT_SUBCATEG_1']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories and Camcorder : Blu Ra...', 'Accessories and Camcorder : Handheld', 'Accessories and Camcorder : Headp...', 'Accessories and Camcorder : Profess...', 'Accessories and Camcorder : Standard', 'Accessories and Camcorder : Univers...', 'Computers : Smartphone', 'Computers : Tablet', 'Media Player : Blu Ray and Boom Box...', 'Media Player : DVD Players - Portable', 'Media Player : Streaming', 'Stereo Systems : Blu Ray and Boom B...', 'Stereo Systems : Home Theater Syst...', 'Stereo Systems : Receivers', 'Stereo Systems : Speaker Kits', 'Stereo Systems : iPod Docking Station', 'Televisions : Blu Ray and Boom Box...', 'Televisions : Flat Panel TV', 'Televisions : Portable TV', 'Video Production : Video Editing']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        tooltip_list=['PRODUCT_CATEGORY_1:Accessories and Camcorder', 'PRODUCT_SUBCATEG_1:Standard', 'Cost of Goods:$49,071,633.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to']
        riser_css="riser!s0!g4!mbar!"
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 20, '9')
        
        """
        Step 10 : Multi select "PRODUCT_CATEGORY_1" and "PRODUCT_SUBCATEG_1" in query pane >
        Step 11 : Click Delete
        """
        field_name_list=['PRODUCT_CATEGORY_1','PRODUCT_SUBCATEG_1']
        visual.multiselect_querytree_field(field_name_list, 'Delete')

        """
        Step 12 :Add "Product, Category" to Horizontal Axis
        """
        visual.drag_field_from_data_tree_to_query_pane('Product,Category', 1, 'Horizontal Axis')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f rect[class^='riser!']", 7)
        
        """
        Step 13 : Verify preview following preview displayed
        Step 14 : Hover over on any riser (Ex., Media Player)
        Step 15 : Verify following tooltip values displayed
        """
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        tooltip_list=['Product Category:Media Player', 'Cost of Goods:$190,240,481.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to PRODUCT_CATEGORY_1', 'Drill down to PRODUCT_SUBCATEG_1']
        riser_css="riser!s0!g3!mbar!"
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 7, '13')
        
        """
        Step 16 : Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f rect[class^='riser!']", 7)
        
        """
        Step 17 : Hover over on any riser and verify tooltip values
        Step 18 : Close run window
        """
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        tooltip_list=['Product Category:Stereo Systems', 'Cost of Goods:$205,113,863.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to PRODUCT_CATEGORY_1', 'Drill down to PRODUCT_SUBCATEG_1']
        riser_css="riser!s0!g4!mbar!"
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 7, '17')
        visual.switch_to_previous_window()
        
        """
        Step 19 : Click Save in the toolbar > Save as "C2349047" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 20 : Logout using API
                    http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
        Step 21 : Restore saved fex using API
                    http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349047.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f rect[class^='riser!']", 7)
            
        x_axis_title=['Product Category']
        y_axis_title=['Cost of Goods']
        x_axis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        y_axis_label=['0', '40M', '80M', '120M', '160M', '200M']
        color_name='bar_blue'
        tooltip_list=['Product Category:Stereo Systems', 'Cost of Goods:$205,113,863.00', 'Filter Chart', 'Exclude from Chart', 'Drill up to PRODUCT_CATEGORY_1', 'Drill down to PRODUCT_SUBCATEG_1']
        riser_css="riser!s0!g4!mbar!"
        verify_bar_chart(x_axis_title, y_axis_title, x_axis_label, y_axis_label, tooltip_list, riser_css, color_name, 7, '21')
    
if __name__ == '__main__':
    unittest.main() 