'''
Created on Feb, 06 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349080
Test_Case Name : Undo delete Group from query

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2349080_TestClass(BaseTestCase):

    def test_C2349080(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349080'
        Edit_Case_ID='C2349080_Base'
        visual=Visualization(self.driver)
        
        def verify_bar_chart(total_risers, expected_legends, step_num):
            expected_yaxis_label=['0', '0.2B', '0.4B', '0.6B', '0.8B', '1B', '1.2B']
            visual.verify_y_axis_title(['Revenue'], msg='Step ' + step_num + '.1')
            visual.verify_y_axis_label(expected_yaxis_label, msg='Step ' + step_num + '.4')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + step_num + '.3')
            visual.verify_legends(expected_legends, msg='Step ' + step_num + '.4')
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step ' + step_num + '.5 ' )
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s1!g0!mbar!']", 'bar_green',  msg='Step ' + step_num + '.6 ' )
                    
        """
            Step 01 : Restore saved fex using API (edit the domain, port and alias of the URL - do not use the URL as is):
                      http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FP312%2FS10664_paperclipping_1%2FC2349080_Base.fex
        """
        visual.edit_visualization_using_api(Edit_Case_ID)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-labels!m6!']", "1.2B", 30)
        
        """
            Step 02 : Drag and drop "Product,Category" to Color bucket
        """
        visual.drag_field_from_data_tree_to_query_pane('Product,Category', 1, 'Color')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='legend-labels!s0!']", "Accessories", 30)
        
        """
            Step 02.1 : Verify output
        """
        verify_bar_chart(7, ['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '02')
        
        """
            Step 03 : Lasso "Camcorder" and "Computers" color >
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s1!g0!mbar!']")
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s2!g0!mbar!']")
        visual.create_lasso(source_element, target_element)
        
        """
            Step 04 : Click "Group Product,Category selection"
        """
        visual.verify_lasso_tooltip(['2 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection'], msg='Step 04.1 : Verify lasso tooltip values')
        visual.select_lasso_tooltip('Group Product,Category Selection')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='legend-labels!s1!']", "CamcorderandComputers", 30)
        
        """
            Step 05 : Verify "PRODUCT_CATEGORY_2 " created and preview updated
            A group is created in color bucket and is named PRODUCT_CATEGORY_2. Group also appears in data pane and as define in the fex.
        """
        verify_bar_chart(6, ['PRODUCT_CATEGORY_2', 'Accessories', 'Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '04')
        visual.verify_field_listed_under_querytree('Color BY', 'PRODUCT_CATEGORY_2', 1, 'Step 04.7 ')
        visual.verify_field_listed_under_datatree('Customer', 'PRODUCT_CATEGORY_1', 1, 'Stpe 04.8 ')
        visual.verify_field_listed_under_datatree('Customer', 'PRODUCT_CATEGORY_2', 2, 'Stpe 04.9 ')
        
        """
            Step 06 : Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='legend-labels!s1!']", "CamcorderandComputers", 30)
        
        """
            Step 06.1 : Verify output in run window
        """
        verify_bar_chart(6, ['PRODUCT_CATEGORY_2', 'Accessories', 'Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '06')
        visual.take_run_window_snapshot(Test_Case_ID, '06')
        
        """
            Step 07 : Hover on "Camcorder and computers" color and verify tooltip values
        """
        expected_tooltip=['Revenue:$257,782,184.36', 'PRODUCT_CATEGORY_2:Camcorder and Computers', 'Filter Chart', 'Exclude from Chart']
        visual.verify_tooltip("riser!s1!g0!mbar!", expected_tooltip, msg='Step 07.1 : Verify Camcorder and computers" verify tooltip values')
        
        """
            Step 08 : Close run window
        """
        visual.switch_to_previous_window()
        
        """
            Step 09 : Click IA > Save as "C2349080" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 10 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            Step 11 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349080.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='legend-labels!s1!']", "CamcorderandComputers", 30)
        
        """
            Step 11.1 : Verify Restored successfully
        """
        verify_bar_chart(6, ['PRODUCT_CATEGORY_2', 'Accessories', 'Camcorder and Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], '11')
        visual.verify_field_listed_under_querytree('Color BY', 'PRODUCT_CATEGORY_2', 1, 'Step 11.7 ')
        visual.verify_field_listed_under_datatree('Customer', 'PRODUCT_CATEGORY_1', 1, 'Stpe 11.8 ')
        visual.verify_field_listed_under_datatree('Customer', 'PRODUCT_CATEGORY_2', 2, 'Stpe 11.9 ')
        visual.take_preview_snapshot(Test_Case_ID, '11')
        
        """
            Step 12 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main()