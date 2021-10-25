'''
Created on Feb 8, 2018

@author: BM13368
TestCase ID:http://172.19.2.180/testrail/index.php?/cases/view/2348951
TestCase Name :Charting 15A: InfoAssist Visualization Integration
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization

class C2348951_TestClass(BaseTestCase):

    def test_C2348951(self):
        """
        TESTCASE VARIABLES
        """
        Test_Case_ID = 'C2348951'
        Restore_fex = 'C2348951_Base'
        driver = self.driver #Driver reference object created
        visual = visualization.Visualization(self.driver)
        
        """
        Step 1:Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2348951_Base.fex
        """
        visual.edit_visualization_using_api(Restore_fex)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, time_out=200)      
        visual.verify_x_axis_title(['PRODUCT_CATEGORY_1'], msg='Step 1.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 1.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 1.3')
        expected_y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 1.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 1.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 1.6")
        expected_tooltip_list=['PRODUCT_CATEGORY_1:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar', expected_tooltip_list, msg='Step 1.7 : Verify tooltip values')
        
        """
        Step 2:Click any riser in preview (Ex. Media player)
        """
        media_player_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class*='riser!s0!g3!mbar']")
        visual.select_chart_component(media_player_elem)
        
        """
        Step 3:Click Rename group PRODUCT_CATEGORY_1
        """
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Group PRODUCT_CATEGORY_1 Selection', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, 'Step 03:01: Verify tooltip values')
        visual.select_lasso_tooltip("Rename group PRODUCT_CATEGORY_1")
        
        """
        Step 4:Enter name "Categories"
        Step 5:Click OK
        """
        visual.rename_grouped_riser_name('PRODUCT_CATEGORY_1', "Categories", close_button_name="OK" )
         
        """
        Step 6:Verify preview , query pane and data pane updated
        Horizontal axis title is changed from PRODUCT_CATEGORY_1 to Categories in preview, in query pane and in data pane.
        """
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, time_out=200)      
        visual.verify_x_axis_title(['Categories'], msg='Step 6.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 6.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 6.3')
        expected_y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 6.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 6.5")
        visual.verify_chart_color_using_get_css_property("[class*='riser!s0!g0!mbar']", "bar_blue", msg="Step 6.6")
        expected_tooltip_list=['Categories:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, msg='Step 6.7 : Verify tooltip values')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Categories', 1, "Step 6.8")
        
        """
        Step 7:Click any riser( Ex., Camcorder) in preview > Review the tooltip
        Tooltip shows group name Categories in Edit and Rename options
        """
        camcorder_elem=driver.find_element_by_css_selector("#MAINTABLE_wbody1 [class='riser!s0!g1!mbar!']")
        visual.select_chart_component(camcorder_elem)
        expected_tooltip_list=['1 point', 'Filter Chart', 'Exclude from Chart', 'Group Categories Selection', 'Edit group Categories', 'Rename group Categories', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_tooltip_list, 'Step 07:01: Verify tooltip values')
        
        """
        Step 8:Click run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 6, 200)
        visual.verify_x_axis_title(['Categories'], msg='Step 09:01: Verify x-axis title')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 09:02:Verify Yaxis title')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 09:03: Verify x-axis label')
        expected_y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 09:04:Verify y-axis labels")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 09:05: Verify number of risers")
        visual.verify_chart_color_using_get_css_property("[class='riser!s0!g0!mbar!']", "bar_blue", msg="Step 09:06:")
        
        """
        Step 9:Hover on Computers riser and verify tooltip values
        """
        
        expected_tooltip_list=['Categories:Computers', 'Cost of Goods:$69,807,664.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g2!mbar!', expected_tooltip_list,'Step 09:07: Verify Tooltip')
        
        """
        Step 10:Close run window
        """
        visual.switch_to_previous_window()
        parent_css="#applicationButton img"
        visual.wait_for_number_of_element(parent_css, 1)
        """
        Step 11:Click IA > Save as "C2348951" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
        Step 12:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
        Step 13:Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348951.fex
        Successfully restored
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        parent_css="#MAINTABLE_wbody1 rect[class^='riser']"
        visual.wait_for_number_of_element(parent_css, 6, time_out=200)      
        visual.verify_x_axis_title(['Categories'], msg='Step 13.1')
        visual.verify_y_axis_title(['Cost of Goods'], msg='Step 13.2')
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions and Video Production']
        visual.verify_x_axis_label(expected_xaxis_label, msg='Step 13.3')
        expected_y_axis_label=['0', '40M', '80M', '120M', '160M', '200M', '240M']
        visual.verify_y_axis_label(expected_y_axis_label, msg="Step 13.4")
        visual.verify_number_of_risers("#MAINTABLE_wbody1_f rect", 1, 6, msg="Step 13.5")
        visual.verify_chart_color_using_get_css_property("[class='riser!s0!g0!mbar!']", "bar_blue", msg="Step 13.6")
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'Categories', 1, "Step 13.7")
        
        expected_tooltip_list=['Categories:Accessories', 'Cost of Goods:$89,753,898.00', 'Filter Chart', 'Exclude from Chart', 'Drill down to Product Category']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip_list, msg='Step 13.8 : Verify tooltip values')
        visual.take_preview_snapshot(Test_Case_ID, '12')
        
        """
        Step 14:Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        
if __name__ == "__main__":
    unittest.main()