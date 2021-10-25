'''
Created on Feb, 08 2018

@author: Robert

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2327826
Test_Case Name : Cannot delete group from data pane while in use
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2327826_TestClass(BaseTestCase):

    def test_C2327826(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2327826'
        visual=Visualization(self.driver)
        
        def verify_bar_chart(expected_xaxis_title, expected_xaxis_label, total_risers, step_num):
            expected_yaxis_label=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
            visual.verify_y_axis_title(['Revenue'], msg='Step ' + step_num + '.1')
            visual.verify_x_axis_title(expected_xaxis_title, msg='Step ' + step_num + '.2')
            visual.verify_x_axis_label(expected_xaxis_label, msg='Step ' + step_num + '.3')
            visual.verify_y_axis_label(expected_yaxis_label, msg='Step ' + step_num + '.4')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + step_num + '.5')
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step ' + step_num + '.6' )
            
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        time.sleep(3)
         
        """
            Step 02. Add "Revenue" and "Product,Category"
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "Revenue", 30)
        
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductCategory", 30)
        time.sleep(3)
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 7, 300)
        
        """
            Step 02.1 : Verify preview
        """
        expected_xaxis_label=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        verify_bar_chart(['Product Category'], expected_xaxis_label, 7, '02')
        
        """
            Step 3. Select "Accessories" and "Camcorder" risers
            Step 4. Click "Group Product,Category Selection"
        """
        
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g0!mbar!']")
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g1!mbar!']")
        
        visual.multi_select_chart_component([source_element, target_element])
        visual.wait_for_visible_text("[class*='tdgchart-tooltip'][style*='visible'] span[class*='tdgchart-tooltip-pad']", '2 points', 15)
        
        visual.verify_lasso_tooltip(['2 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection'], 'Step 03.1 : Verify multiple select tooltip')
        
        visual.select_lasso_tooltip('Group Product,Category Selection')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "PRODUCT_CATEGORY_1", 60)
        
        """
            Step 5. Select "Televisions" riser
            Step 6. Verify the tooltip
        
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1 rect[class*='riser!s0!g4!mbar!']")
        visual.multi_select_chart_component([source_element])
        
        visual.wait_for_visible_text("[class*='tdgchart-tooltip'][style*='visible'] span[class*='tdgchart-tooltip-pad']", '1 point', 15)
        visual.verify_lasso_tooltip(['1 point', 'Filter Chart', 'Exclude from Chart', 'Group PRODUCT_CATEGORY_1 Selection', 'Edit group PRODUCT_CATEGORY_1', 'Rename group PRODUCT_CATEGORY_1', 'Ungroup All'], 'Step 06.1 : Verify tooltip at Televisions')
        
        """
            Step 7. Click "Group PRODUCT_CATEGORY_1 Selection"
            Step 8. Right click "PRODUCT_CATEGORY_1" in query pane
            Step 9. Click "Edit group"

        """
        visual.select_lasso_tooltip('Group PRODUCT_CATEGORY_1 Selection')
        time.sleep(10)
        
        visual.right_click_on_field_under_query_tree('PRODUCT_CATEGORY_1', 1, 'Edit Group...')
        
        """
            Step 10. Verify "Televisions" is now a new group and was not added to existing group

        """
        button_css = "div[id^='QbDialog'] [class*='active'] [id='dynaGrpsCancelBtn'] img"
        visual.wait_for_number_of_element(button_css, 1)
        expected_group_dialog_list=['Accessories and Camcorder', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Televisions', 'Video Production']
        visual.verify_group_grid_values(expected_group_dialog_list, "Step 10:01:Verify group list")
        
        """
            Step 11 : select "Video production" > Add to drop down >
            Step 12 : Click "Televisions"
        """
        extnd_list=['Video Production']
        visual.extend_existing_group(extnd_list, 'Televisions')
        """
            Step 13. Verify "Video production" added to "Televisions" group
            Step 14. Click OK
        """
        expected_group_dialog_list=['Accessories and Camcorder', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Televisions', 'Video Production']
        visual.verify_group_grid_values(expected_group_dialog_list, "Step 13:01:Verify group list")
        visual.exit_group_dialog('ok')
        
        """
            Step 15. Verify following preview displayed
        """
        parent_css="#MAINTABLE_wbody1 svg g text[class*='mgroupLabel']"
        visual.wait_for_number_of_element(parent_css, 5, 300)
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions']
        verify_bar_chart(['PRODUCT_CATEGORY_1'], expected_xaxis_label, 5, '15')
        
        """
            Step 16. Click Run
            Step 17. Verify following run time displayed
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", 'PRODUCT_CATEGORY_1', 120)
        
        expected_xaxis_label=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions']
        verify_bar_chart(['PRODUCT_CATEGORY_1'], expected_xaxis_label, 5, '17')
        visual.take_run_window_snapshot(Test_Case_ID, '17')
        visual.switch_to_previous_window()
        
        """
            18. Dismiss run window
            19. Logout using API (without saving)
        """
        visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main()