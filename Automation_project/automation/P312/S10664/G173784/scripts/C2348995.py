'''
Created on Jan 03, 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2348995
Test_Case Name : Paperclipping in Grid
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import visualization
from common.pages import visualization_resultarea, visualization_ribbon
from common.lib import utillity

class C2348995_TestClass(BaseTestCase):

    def test_C2348995(self):
        
        """   
            TESTCASE VARIABLES 
        """
        
        Test_Case_ID='C2348995'
        visual=visualization.Visualization(self.driver)
        utillobj = utillity.UtillityMethods(self.driver)
        visul_result = visualization_resultarea.Visualization_Resultarea(self.driver)
        visul_ribbon=visualization_ribbon.Visualization_Ribbon(self.driver)
        
        def verify_grid_row_label_value(expected_row_labels, expected_row_values, msg):
            actual_row_labels=[label.text.strip() for label in self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1_f svg g[class='rowLabels'] text")]
            actual_row_values=[label.text.strip() for label in self.driver.find_elements_by_css_selector("#MAINTABLE_wbody1_f svg g[class='innerTable'] text")]
            
            actual_list=expected_row_labels+expected_row_values
            expected_list=actual_row_labels+actual_row_values
            print("actual_row_labels",actual_row_labels)
            print("expected_row_labels",expected_row_labels)
            print("actual_list",actual_list)
            print("expected_list",expected_list)
            utillobj.asequal(actual_list, expected_list, msg)
            
        """
            Step 01 : Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=baseapp/wf_retail_lite
        """

        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        """
            Step 02 : Click Change drop down > Grid
        """
        visul_ribbon.change_chart_type('grid')
        visul_result.wait_for_property("#pfjTableChart_1 text[class='title']", 1, 80, string_value='Drag fields here to create grid')
        
        """
            Step 03 : Double click "Revenue", Product, Category" to add fields
        """
        
        visual.double_click_on_datetree_item('Revenue', 1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg g[class='colHeaderScroll']>text", 1, 80, string_value='Revenue')
        
        visual.double_click_on_datetree_item('Product,Category', 1)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg g[class='rowTitle']>text", 1, 80, string_value='Product Category')
        time.sleep(2)
        
        """
            Step 04 : Verify following fields in query and preview
        """
        visul_result.verify_grid_column_heading('MAINTABLE_wbody1_f', ['Product Category', 'Revenue'], 'Step 04.1 : Verify grid table heading')
        expected_row_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_row_values=['$129,608,338.53', '$154,465,702.24', '$103,316,482.12', '$246,073,059.36', '$291,294,933.52', '$78,381,132.81', '$58,053,276.62']
        verify_grid_row_label_value(expected_row_labels, expected_row_values, 'Step 04.1 : Verify following fields in query and preview')
        
        """
            Step 05 : Lasso on last four categories
            Step 06 : Click "Group Product,Category selection"
        """
        visul_result.create_lasso('MAINTABLE_wbody1_f', 'rect', 'rowHeader!mcellFill!r3!c0!', target_tag='rect', target_riser='rowHeader!mcellFill!r6!c0!')
        expected_lasso=['4 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Category Selection']
        visul_result.select_or_verify_lasso_filter(verify=expected_lasso, msg='Step 05.1 : Verify lasso values', select='Group Product,Category Selection')
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg g[class='rowTitle']>text", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 07 : Verify group created and preview updated
            Step 07.1 : Group PRODUCT_CATEGORY_1 is created, group values are merged into 1 row in preview
        """
        visul_result.verify_grid_column_heading('MAINTABLE_wbody1_f', ['PRODUCT_CATEGORY_1', 'Revenue'], 'Step 07.1 : Verify grid table heading')
        expected_row_labels=['Accessories', 'Camcorder', 'Computers', 'Media Player and Stereo Systems and Televisions and 1 more']
        expected_row_values=['$129,608,338.53', '$154,465,702.24', '$103,316,482.12', '$673,802,402.31']
        verify_grid_row_label_value(expected_row_labels, expected_row_values, 'Step 07.2 : Verify group created and preview updated')
        
        """
            Step 08 : Hover on grouped values and verify tool tip values
        """
        expected_tooltip=['PRODUCT_CATEGORY_1:Media Player and Stereo Systems and Televisions and 1 more', 'Revenue:$673,802,402.31', 'Filter Chart', 'Exclude from Chart']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g0!mcellFill!r3!c0!', expected_tooltip, 'Step 08.1 : Verify tool tip values')
        
        """
            Step 09 : Click Run
        """
        visul_ribbon.select_top_toolbar_item('toolbar_run')
        visual.switch_to_new_window()
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg g[class='rowTitle']>text", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 10 : Hover on value and verify tool tip values
        """
        expected_tooltip=['PRODUCT_CATEGORY_1:Camcorder', 'Revenue:$154,465,702.24', 'Filter Chart', 'Exclude from Chart']
        visul_result.verify_default_tooltip_values('MAINTABLE_wbody1_f', 'riser!s0!g0!mcellFill!r1!c0!', expected_tooltip, 'Step 10.1 : Verify tool tip values')
        
        """
            Step 11 : Dismiss run window
        """
        visual.switch_to_previous_window()
        
        """
            Step 12 : Click Save in the toolbar > Save as "C2348995" > Click Save
        """
        visul_ribbon.select_tool_menu_item('menu_save_as')
        utillobj.ibfs_save_as(Test_Case_ID)
        
        """
            Step 13 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        utillobj.infoassist_api_logout()
        
        """
            Step 14 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2348995.fex
        """        
        visual.edit_visualization_using_api(Test_Case_ID)
        visul_result.wait_for_property("#MAINTABLE_wbody1_f svg g[class='rowTitle']>text", 1, 80, string_value='PRODUCT_CATEGORY_1')
        
        """
            Step 14.1 : Verify preview
        """
        visul_result.verify_grid_column_heading('MAINTABLE_wbody1_f', ['PRODUCT_CATEGORY_1', 'Revenue'], 'Step 14.1 : Verify grid table heading')
        verify_grid_row_label_value(expected_row_labels, expected_row_values, 'Step 14.2 : Verify preview data')
        
        """
            Step 15 : Logout using API
        """
        utillobj.infoassist_api_logout()
        
if __name__ == '__main__':
    unittest.main()