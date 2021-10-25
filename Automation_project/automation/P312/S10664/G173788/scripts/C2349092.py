'''
Created on Feb, 08 2018

@author: Prabhakaran

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10664
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2349092
Test_Case Name : Filter/exclude group

'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.visualization import Visualization

class C2349092_TestClass(BaseTestCase):

    def test_C2349092(self):
        
        """   
            TESTCASE VARIABLES 
        """
        Test_Case_ID='C2349092'
        visual=Visualization(self.driver)
        
        def verify_bar_chart(xaxis_title, xaxis_labels, yaxis_labels, total_risers, step_num):
            visual.verify_x_axis_title(xaxis_title, msg='Step ' + step_num + '.1')
            visual.verify_y_axis_title(['Gross Profit'], msg='Step ' + step_num + '.2')
            visual.verify_x_axis_label(xaxis_labels,  xyz_axis_label_length=30,  msg='Step ' + step_num + '.3')
            visual.verify_y_axis_label(yaxis_labels, msg='Step ' + step_num + '.4')
            visual.verify_number_of_risers('#MAINTABLE_wbody1_f rect', 1, total_risers, msg='Step ' + step_num + '.5')
            visual.verify_chart_color_using_get_css_property("rect[class='riser!s0!g0!mbar!']", 'lochmara',  msg='Step ' + step_num + '.6 ' )
           
        """
            Step 01 : Launch the IA API with visualization in edit mode (edit the domain, port and alias of the URL - do not use the URL as is):
            http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664&tool=idis&master=wf_retail_lite
        """
        visual.invoke_visualization_using_api('baseapp/wf_retail_lite')
        
        """
            Step 02 : Double click "Gross Profit" and "Product, Subcategory"
        """
        visual.double_click_on_datetree_item('Gross Profit', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='yaxis-title']", "GrossProfit", 20)
        
        visual.double_click_on_datetree_item('Product,Subcategory', 1)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "ProductSubcategory", 20)
        
        """
            Step 02.1 : Verify preview
        """
        expected_xaxis_lables=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV', 'Handheld', 'Headphones', 'Home Theater Systems', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yaxis_labels=['0', '10M', '20M', '30M', '40M', '50M', '60M']
        verify_bar_chart(['Product Subcategory'], expected_xaxis_lables, expected_yaxis_labels, 21, '02')
        """
            Step 03 : Lasso few riser
        """
        source_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g6!mbar!']")
        target_element=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g9!mbar!']")
        visual.create_lasso(source_element, target_element)
        visual.verify_lasso_tooltip(['4 points', 'Filter Chart', 'Exclude from Chart', 'Group Product,Subcategory Selection'], 'Step 03.1 : Verify lasso tooltip')
        
        """
            Step 04 : Click "Group Product, Subcategory Selection"
        """
        visual.select_lasso_tooltip('Group Product,Subcategory Selection')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-title']", "PRODUCT_SUBCATEG_1", 30)
        
        """
            Step 05 : Verify group created
        """
        expected_xaxis_lables=['Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV and Handheld and Head...', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        verify_bar_chart(['PRODUCT_SUBCATEG_1'], expected_xaxis_lables, expected_yaxis_labels, 18, '05')
        visual.verify_field_listed_under_querytree('Horizontal Axis', 'PRODUCT_SUBCATEG_1', 1, 'Step 04.7 ')
        visual.verify_field_listed_under_datatree('Customer', 'PRODUCT_SUBCATEG_1', 1, 'Stpe 04.8 ')
        
        """
            Step 06 : Multi select "Blue ray", Flat panel TV and Handheld a...", "ipod Docking station" riser >
        """
        blue_ray=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g0!mbar!']")
        flat_tv=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g6!mbar!']")
        ipad=self.driver.find_element_by_css_selector("#MAINTABLE_wbody1_f rect[class='riser!s0!g17!mbar!']")
        visual.multi_select_chart_component([blue_ray, flat_tv, ipad])
        expected_lasso_tooltip=['3 points', 'Filter Chart', 'Exclude from Chart', 'Merge with Flat Panel TV and Handheld...', 'Edit group PRODUCT_SUBCATEG_1', 'Rename group PRODUCT_SUBCATEG_1', 'Ungroup All']
        visual.verify_lasso_tooltip(expected_lasso_tooltip, 'Step 06.1 : Verify lasso tooltip')
        
        """
            Step 07 : Click Filter chart
        """
        visual.select_lasso_tooltip('Filter Chart')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g2!mgroupLabel!']", "iPodDockingStation", 25)
        
        """
            Step 08 : Verify preview and filter pane updated
        """
        expected_xaxis_lables=['Blu Ray', 'Flat Panel TV and Handheld and Headphones and 1 more', 'iPod Docking Station']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        verify_bar_chart(['PRODUCT_SUBCATEG_1'], expected_xaxis_lables, expected_yaxis_labels, 3, '08') 
        visual.verify_field_in_filterbox('PRODUCT_SUBCATEG_1', 1, 'Step 08.1 ')
        
        """
            Step 09 : Hover on Blue ray riser 
        """
        expected_tooltip=['PRODUCT_SUBCATEG_1:Blu Ray', 'Gross Profit:$51,771,195.13', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Product Subcategory']
        visual.verify_tooltip('riser!s0!g0!mbar!', expected_tooltip, msg='Step 09.1 : Verify Blue ray riser tooltip values')
        
        """
            Step 10 : Click "Exclude from chart"
        """
        visual.select_tooltip('riser!s0!g0!mbar!', 'Exclude from Chart')
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g1!mgroupLabel!']", "iPodDockingStation", 25)
        
        """
            Step 11 : Verify preview updated
        """
        expected_xaxis_lables=['Flat Panel TV and Handheld and Headphones and 1 more', 'iPod Docking Station']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        verify_bar_chart(['PRODUCT_SUBCATEG_1'], expected_xaxis_lables, expected_yaxis_labels, 2, '11') 
        
        """
            Step 12 : Right click on "PRODUCT_SUBCATEG_1" > Edit in filter box
        """
        visual.right_click_on_field_in_filterbox('PRODUCT_SUBCATEG_1', 1, 'Edit...')
        
        """
            Step 13 : Click Show prompt check box
            Step 14 : Click OK
        """
        visual.deselect_filter_show_prompt_checkbox('alpha', None)
        visual.close_filter_dialog('ok')
        visual.wait_for_visible_text("#ar_Prompt_1 .arFilterButton", "PRODUCT_SUBCATEG_1", 15)
        
        """
            Step 15  : Verify prompt added to prompt panel
        """
        expected_items_list=['[All]', 'Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV and Handheld and Headphones and 1 more', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        visual.verify_show_prompt_table_list(expected_items_list, msg='Step 15.1 :')
        visual.verify_item_checked_status_in_show_prompt_table('Flat Panel TV and Handheld and Headphones and 1 more', msg='Step 15.2 :')
        visual.verify_item_checked_status_in_show_prompt_table('iPod Docking Station', msg='Step 15.3 :')
        
        """
            Step 16 : Click Run
        """
        visual.run_visualization_from_toptoolbar()
        visual.switch_to_new_window()
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g1!mgroupLabel!']", "iPodDockingStation", 25)
        
        """
            Step 16.1 : Verify run window output
        """
        expected_xaxis_lables=['Flat Panel TV and Handheld and Headphones and 1 more', 'iPod Docking Station']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        verify_bar_chart(['PRODUCT_SUBCATEG_1'], expected_xaxis_lables, expected_yaxis_labels, 2, '16')
        expected_items_list=['[All]', 'Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV and Handheld and Headphones and 1 more', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        visual.verify_show_prompt_table_list(expected_items_list, parent_prompt_css='#PROMPT_1_cs', msg='Step 16.7 :')
        visual.verify_item_checked_status_in_show_prompt_table('Flat Panel TV and Handheld and Headphones and 1 more', parent_prompt_css='#PROMPT_1_cs', msg='Step 16.8 :')
        visual.verify_item_checked_status_in_show_prompt_table('iPod Docking Station', parent_prompt_css='#PROMPT_1_cs', msg='Step 16.9 :')
        
        """
            Step 17 : Hover on "Flat panel TV and Handheld and Headphones and 1 more" riser >
        """
        expected_tooltip=['PRODUCT_SUBCATEG_1:Flat Panel TV and Handheld and Headphones and 1 more', 'Gross Profit:$89,733,273.87', 'Filter Chart', 'Exclude from Chart', 'Drill up to Product Category', 'Drill down to Product Subcategory']
        visual.verify_tooltip("riser!s0!g0!mbar!", expected_tooltip, msg='Step 17.1 : Verify Flat panel TV and Handheld and Headphones riser tooltip values')
        
        """
            Step 18 : Click Filter chart
        """
        visual.select_tooltip('riser!s0!g0!mbar!', 'Filter Chart')
        visual.wait_for_number_of_element("#MAINTABLE_wbody1_f rect[class*='riser!s']", 1, 15)
        
        """
            Step 19 : Verify chart and prompt updated
        """
        expected_xaxis_lables=['Flat Panel TV and Handheld and Headphones and 1 more']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        verify_bar_chart(['PRODUCT_SUBCATEG_1'], expected_xaxis_lables, expected_yaxis_labels, 1, '19')
        expected_items_list=['[All]', 'Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV and Handheld and Headphones and 1 more', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        visual.verify_show_prompt_table_list(expected_items_list, parent_prompt_css='#PROMPT_1_cs', msg='Step 16.7 :')
        visual.verify_item_checked_status_in_show_prompt_table('Flat Panel TV and Handheld and Headphones and 1 more', parent_prompt_css='#PROMPT_1_cs', msg='Step 16.8 :')
        visual.verify_item_checked_status_in_show_prompt_table('iPod Docking Station', parent_prompt_css='#PROMPT_1_cs', checked_status=False, msg='Step 16.9 :')
        visual.take_run_window_snapshot(Test_Case_ID, '19')
        
        """
            Step 20  : Close run window
        """
        visual.switch_to_previous_window()
        
        """
            Step 21 : Click Save in the toolbar > Save as "C2349092" > Click Save
        """
        visual.save_as_visualization_from_menubar(Test_Case_ID)
        
        """
            Step 22 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
        """
            Step 23 : Restore saved fex using API http://domain.com:port/alias/ia?&item=IBFS%3A%2FWFC%2FRepository%2FS10664%2FC2349092.fex
        """
        visual.edit_visualization_using_api(Test_Case_ID)
        visual.wait_for_visible_text("#MAINTABLE_wbody1_f text[class='xaxisOrdinal-labels!g1!mgroupLabel!']", "iPodDockingStation", 25)
        
        """
            Step 23.1 : Restored successfully
        """
        expected_xaxis_lables=['Flat Panel TV and Handheld and Headphones and 1 more', 'iPod Docking Station']
        expected_yaxis_labels=['0', '20M', '40M', '60M', '80M', '100M']
        verify_bar_chart(['PRODUCT_SUBCATEG_1'], expected_xaxis_lables, expected_yaxis_labels, 2, '23')
        expected_items_list=['[All]', 'Blu Ray', 'Boom Box', 'CRT TV', 'Charger', 'DVD Players', 'DVD Players - Portable', 'Flat Panel TV and Handheld and Headphones and 1 more', 'Portable TV', 'Professional', 'Receivers', 'Smartphone', 'Speaker Kits', 'Standard', 'Streaming', 'Tablet', 'Universal Remote Controls', 'Video Editing', 'iPod Docking Station']
        visual.verify_show_prompt_table_list(expected_items_list, msg='Step 23.7 :')
        visual.verify_item_checked_status_in_show_prompt_table('Flat Panel TV and Handheld and Headphones and 1 more', msg='Step 23.8 :')
        visual.verify_item_checked_status_in_show_prompt_table('iPod Docking Station', msg='Step 23.9 :')
        visual.take_preview_snapshot(Test_Case_ID, '23')
            
        """
            Step 24 : Logout using API http://machine:port/alias/service/wf_security_logout.jsp
        """
        visual.logout_visualization_using_api()
        
if __name__ == '__main__':
    unittest.main()