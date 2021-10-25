'''
Created on May 8, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5831106
TestCase Name = Rename Group After Adding to Filter
'''

import unittest, time
from common.wftools import visualization
from common.lib.basetestcase import BaseTestCase

class C5831106_TestClass(BaseTestCase):

    def test_C5831106(self):
        
        """
        TESTCASE VARIABLES
        """        
        Test_Case_ID = "C5831106"
        metadata_browser_query_variables__css = "#iaMetaDataBrowser td"  
        total_no_of_riser_css = "#MAINTABLE_1 rect[class^='riser']"  
        long_wait_time_in_sec = 120
        medium_wait_time_in_sec = 60
        short_wait_time_in_sec = 30
        yaxis_title_css = "#MAINTABLE_wbody1_f text[class='yaxis-title']"
        xaxis_title_css = "#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']"
#         tooltip_css="[class*='tdgchart-tooltip'][style*='visible']"
        toolbar_run="#topToolBar #runButton img"
        Filter_dialog_ok_button_css = "#avFilterOkBtn"
        no_of_riser=7
        
        visual = visualization.Visualization(self.driver)
        
        def verify_bar_chart(x_title=None, y_title=None, x_label=None,y_label=None,riser_color_css="riser!s0!g0!mbar", riser_color='bar_blue',total_risers=None,step_num=None):
            visual.verify_x_axis_title(x_title, msg='Step ' + step_num + '.01:')
            visual.verify_y_axis_title(y_title, msg='Step ' + step_num + '.02:')
            visual.verify_x_axis_label(x_label, msg='Step ' + step_num + '.03')
            visual.verify_y_axis_label(y_label, msg='Step ' + step_num + '.04')
            visual.verify_number_of_risers('#MAINTABLE_1 rect', 1, total_risers, msg='Step ' + step_num + '.05:')
            visual.verify_chart_color_using_get_css_property("[class*='"+riser_color_css+"']", riser_color,  msg='Step ' + step_num + '.06:')
            
        """
        Step01: Launch the IA API with Visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660&tool=idis&master=baseapp/wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        visual.wait_for_visible_text(metadata_browser_query_variables__css, 'Filters and Variables', long_wait_time_in_sec)
        
        """
        Step02: Double click Revenue and Product,Category
        """
        visual.double_click_on_datetree_item('Revenue', 1)
        visual.wait_for_visible_text(yaxis_title_css, "Revenue", medium_wait_time_in_sec)
        visual.double_click_on_datetree_item('Product,Category', 1)
        visual.wait_for_visible_text(xaxis_title_css, "ProductCategory", medium_wait_time_in_sec)
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, medium_wait_time_in_sec)
        
        """
        Step03: Lasso Accessories, and Camcorder > Group Product,Category
        """
        no_of_riser=6
        step_num='03'
        Accessories_css = "#MAINTABLE_wbody1 [class*='riser!s0!g0!mbar']"
        source_element = self.driver.find_element_by_css_selector(Accessories_css)
        Camcorder_css = "#MAINTABLE_wbody1 [class*='riser!s0!g1!mbar']"
        target_element = self.driver.find_element_by_css_selector(Camcorder_css)
        visual.create_lasso(source_element, target_element, source_xoffset=-35, source_element_location='middle_left')
        visual.select_lasso_tooltip("Group Product,Category Selection")
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec) 
        x_title=['PRODUCT_CATEGORY_1']
        y_title=['Revenue']
        expected_xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        verify_bar_chart(x_title=x_title, y_title=y_title, x_label=expected_xaxis_labels, y_label=expected_yaxis_labels, total_risers=no_of_riser, step_num=step_num)        
        
        """
        Step04: Drag PRODUCT_CATEGORY_1 to filter pane > leave defaults > OK
        """
        visual.drag_and_drop_from_data_tree_to_filter('Dimensions->Sales_Related->PRODUCT_CATEGORY_1', 1)
        visual.wait_for_number_of_element(Filter_dialog_ok_button_css, 1, short_wait_time_in_sec)
        visual.close_filter_dialog('ok')
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, short_wait_time_in_sec)
        visual.verify_field_in_filterbox('PRODUCT_CATEGORY_1', 1, "Step 04.01: Verify PRODUCT_CATEGORY_1 added to filter pane")
        visual.verify_prompt_title('PRODUCT_CATEGORY_1')
        filter_prompt_list_css = "#ar_Prompt_1 [style*='hidden'] tr"
        visual.wait_for_number_of_element(filter_prompt_list_css, 7, medium_wait_time_in_sec)
        expected_prompt_menu_list = ['[All]', 'Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_show_prompt_table_list(expected_prompt_menu_list, msg="Step 04.02: Verify PRODUCT_CATEGORY_1 filter prompt menu list")       
        visual.verify_item_checked_status_in_show_prompt_table('[All]',checked_status=True, msg='Step 04.03: Verify [All] is checked')
        visual.verify_item_checked_status_in_show_prompt_table('Accessories and Camcorder',checked_status=False, msg='Step 04.04: Verify Accessories and Camcorder is unchecked')
        
        """
        Step05: Right click PRODUCT_CATEGORY_1 group in data pane > Edit group
        """     
        
        visual.right_click_on_datetree_item('Dimensions->Sales_Related->Product->Product->PRODUCT_CATEGORY_1', 1, 'Edit Group...')
        group_values_dialog_css = "#dynaGrpsValuesTree tr"
        visual.wait_for_number_of_element(group_values_dialog_css, 9, medium_wait_time_in_sec)
        
        """
        Step06: Change Field name to 'TEST' > OK
        """
        visual.enter_field_text_group('TEST')
        time.sleep(5)
        visual.exit_group_dialog('ok')
        visual.wait_for_visible_text('#queryTreeColumn', 'TEST')
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec)
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'TEST', 1, "Step 06.01: Verify TEST updated to query pane")
        visual.verify_field_in_filterbox('TEST', 1, "Step 06.02: Verify TEST updated to filter pane")
        visual.verify_prompt_title('TEST')
        filter_prompt_list_css = "#ar_Prompt_1 [style*='hidden'] tr"
        visual.wait_for_number_of_element(filter_prompt_list_css, 7, medium_wait_time_in_sec)
        expected_prompt_menu_list = ['[All]', 'Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_show_prompt_table_list(expected_prompt_menu_list, msg="Step 06.03: Verify TEST filter prompt menu list")       
        visual.verify_item_checked_status_in_show_prompt_table('[All]',checked_status=True, msg='Step 06.04: Verify [All] is checked')
        visual.verify_item_checked_status_in_show_prompt_table('Accessories and Camcorder',checked_status=False, msg='Step 06.05: Verify Accessories and Camcorder is unchecked')
        
        """
        Step07: Save visualization with name C5831106
        Step08: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.wait_for_number_of_element(toolbar_run, 1, short_wait_time_in_sec)
        visual.save_visualization_from_top_toolbar(Test_Case_ID)
        visual.wait_for_number_of_element(toolbar_run, 1, short_wait_time_in_sec)
        visual.logout_visualization_using_api()
        
        """Step09:Restore the saved fex using API
        http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10660%2FC5831106.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)        
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec) 
        
        x_title=['TEST']
        y_title=['Revenue']
        expected_xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        step_num='09'
        verify_bar_chart(x_title=x_title, y_title=y_title, x_label=expected_xaxis_labels, y_label=expected_yaxis_labels, total_risers=no_of_riser, step_num=step_num)        
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'TEST', 1, "Step 09.07: Verify TEST updated to query pane")
        visual.verify_field_in_filterbox('TEST', 1, "Step 09.08: Verify TEST updated to filter pane")
        visual.verify_prompt_title('TEST')
        filter_prompt_list_css = "#ar_Prompt_1 [style*='hidden'] tr"
        visual.wait_for_number_of_element(filter_prompt_list_css, 7, medium_wait_time_in_sec)
        expected_prompt_menu_list = ['[All]', 'Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_show_prompt_table_list(expected_prompt_menu_list, msg="Step 09.09: Verify TEST filter prompt menu list")       
        visual.verify_item_checked_status_in_show_prompt_table('[All]',checked_status=True, msg='Step 09.10: Verify [All] is checked')
        visual.verify_item_checked_status_in_show_prompt_table('Accessories and Camcorder',checked_status=False, msg='Step 09.11: Verify Accessories and Camcorder is unchecked')
                
        """
        Step10: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
        Step11: Run visualization with API call
        http://domain.com:port/alias/run.bip?BIP_REQUEST_TYPE=BIP_LAUNCH&BIP_folder=IBFS%253A%252FWFC%252FRepository%2FS10660%2FC5831106.fex
        """
        visual.run_visualization_using_api(Test_Case_ID)
        visual.wait_for_number_of_element(total_no_of_riser_css, no_of_riser, long_wait_time_in_sec) 
        
        x_title=['TEST']
        y_title=['Revenue']
        step_num='11'
        expected_xaxis_labels=['Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        expected_yaxis_labels=['0', '50M', '100M', '150M', '200M', '250M', '300M', '350M']
        verify_bar_chart(x_title=x_title, y_title=y_title, x_label=expected_xaxis_labels, y_label=expected_yaxis_labels, total_risers=no_of_riser, step_num=step_num)        
        visual.verify_prompt_title('TEST','#LOBJPrompt_11')
        expected_prompt_menu_list = ['[All]', 'Accessories and Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production']
        visual.verify_show_prompt_table_list(expected_prompt_menu_list,'#PROMPT_1_cs', msg="Step 11.07: Verify TEST filter prompt menu list")       
        visual.verify_item_checked_status_in_show_prompt_table('[All]','#PROMPT_1_cs',checked_status=True, msg='Step 11.08: Verify [All] is checked')
        visual.verify_item_checked_status_in_show_prompt_table('Accessories and Camcorder','#PROMPT_1_cs',checked_status=False, msg='Step 11.09: Verify Accessories and Camcorder is unchecked')
        
        """
        Step12: Logout using API
        http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()

if __name__ == '__main__':
    unittest.main() 