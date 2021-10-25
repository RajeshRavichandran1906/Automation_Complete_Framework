'''
Created on June 07, 2019.

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5853151
TestCase Name = Check settings for tabbed panels with content
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage, chart
from common.lib import utillity
from common.locators import wf_mainpage_locators, page_designer_design, page_designer_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design

class C5853151_TestClass(BaseTestCase):

    def test_C5853151(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_util_obj = CoreUtillityMethods(self.driver)
        page_designer_obj = Design(self.driver)
        pd_locator_obj = page_designer_design.ToolBar()
        page_designer_locator_obj = page_designer_locators.PageDesigner()
        chart_obj = chart.Chart(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        edit_fex_name = 'C5853149'
        repository_folder = 'Workspaces->P292_S11397->G435441'
        report_action_bar = 'Report'
        panel1_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html']
        panel2_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Gray.html']
        panel3_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Green.html']
        panel4_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Red.html']
        panel5_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Category_Sales.fex']
        panel5_resource_label_value_1 = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Discount_by_Region.fex']
        panel6_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Sales_Trend.fex']
        panel6_resource_label_value_1 = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Profit_by_Category.fex']
        expected_parameters_label_value_list = ['Parameters/Filters', 'None']
        expected_parameters_label_value_list_1 = ['Parameters/Filters', 'PRODUCT_CATEGORY MODEL BUSINESS_REGION STORE_TYPE TIME_DATE TIME_DATE_TO']
        sleep_time = 5
        
        """
        TESTCASE CSS
        """
        info_mode_css = "div[title='Info mode'].ibxtool-toolbar-button"
        resource_css = "div[class*='pdcnt-resource']"
        parameters_css = "div[class*='pdcnt-parameters']"
        add_content_css = "div[data-ibx-type='ibxDialog'][class*='pop-top'] div[data-ibx-type='ibxHSplitMenuButton']:not([style*='none'])>div[class='ibx-label-text']"
        
        """
        Step 01.00: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 02.00: Click on Content View from the side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 03.00: Navigate to the folder P292_S11397/G435441;
        """
        main_page_obj.expand_repository_folder(repository_folder)
        
        """
        Right click on 'C5853149' and choose Edit
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(edit_fex_name, context_menu_item_path='Edit')
        sleep(sleep_time)
        
        """
        Step 04.00: Navigate to Retail Samples > Portal > Small Widgets from the tree;
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(page_designer_locator_obj.PD_PANEL_CSS, 7, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.collapse_content_folder('G435441->P292_S11397')
        sleep(sleep_time)
        
        """
        Drag and drop 'Discount by Region' over panel 5 , Click on Add content;
        """
        page_designer_obj.select_container("Category Sales")
        page_designer_obj.drag_content_item_to_container("Discount by Region", "Category Sales", content_folder_path="Retail Samples->Portal->Small Widgets")
        util_obj.synchronize_with_visble_text(add_content_css, 'Add content as new tab', main_page_obj.home_page_short_timesleep)
        add_content_obj = util_obj.validate_and_get_webdriver_object(add_content_css, 'Add content as new tab')
        core_util_obj.left_click(add_content_obj)
        sleep(sleep_time)
        
        """
        Drag and drop 'Regional Profit by Category' over panel 6, Click on Add content
        """
        page_designer_obj.collapse_content_folder('Small Widgets')
        page_designer_obj.select_container("Regional Sales Trend")
        page_designer_obj.drag_content_item_to_container("Regional Profit by Category", "Regional Sales Trend", content_folder_path="Small Widgets")
        util_obj.synchronize_with_visble_text(add_content_css, 'Add content as new tab', main_page_obj.home_page_short_timesleep)
        add_content_obj = util_obj.validate_and_get_webdriver_object(add_content_css, 'Add content as new tab')
        core_util_obj.left_click(add_content_obj)
        sleep(sleep_time)
        
        """
        Step 04.01: Verify that the middle 2 panels are populated with the tabbed containers as below
        """
        '''Panel 5'''
        page_designer_obj.switch_to_container_frame('Category Sales')
        riser_css="#jschart_HOLD_0 rect[class^='riser']"
        util_obj.synchronize_with_number_of_element(riser_css, 16, main_page_obj.home_page_short_timesleep)
        chart_obj.verify_x_axis_title_in_preview(expected_title_list=['Sale Quarter', 'Store Region'], parent_css="#jschart_HOLD_0", msg="Step 04.01a")
        chart_obj.verify_z_axis_label_in_preview(expected_label_list=['EMEA', 'North America', 'Oceania', 'South America'], parent_css="#jschart_HOLD_0", xyz_axis_label_css="svg g g g text[class^='zaxisOrdinal']", msg="Step 04.01b")
        chart_obj.verify_number_of_chart_segment("jschart_HOLD_0", 16, msg="Step 04.01c: verify number of line segments available", custom_css="rect[class^='riser']")
        core_util_obj.switch_to_default_content()
        
        '''Panel 6'''
        page_designer_obj.switch_to_container_frame('Regional Sales Trend')
        riser_css="#jschart_HOLD_0 rect[class^='riser']"
        util_obj.synchronize_with_number_of_element(riser_css, 28, main_page_obj.home_page_short_timesleep)
        chart_obj.verify_x_axis_title_in_preview(expected_title_list=['Product Category'], parent_css="#jschart_HOLD_0", msg="Step 04.02a")
        chart_obj.verify_y_axis_title_in_preview(expected_title_list=['Gross Profit'], parent_css="#jschart_HOLD_0", msg="Step 04.02b")
        chart_obj.verify_x_axis_label_in_preview(expected_label_list=['Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], parent_css="#jschart_HOLD_0", msg="Step 04.02c")
        chart_obj.verify_y_axis_label_in_preview(expected_label_list=['0', '20M', '40M', '60M', '80M', '100M'], parent_css="#jschart_HOLD_0", msg="Step 04.02d")
        chart_obj.verify_number_of_chart_segment("jschart_HOLD_0", 28, msg="Step 04.02e: verify number of line segments available", custom_css="rect[class^='riser']")
        core_util_obj.switch_to_default_content()
        
        """
        Step 05.00: From the designer toolbar click on info mode button.
        """
        util_obj.synchronize_with_number_of_element(pd_locator_obj.INFO_MODE_BUTTON_CSS, 1, main_page_obj.home_page_medium_timesleep)
        info_mode_obj = util_obj.validate_and_get_webdriver_object(pd_locator_obj.INFO_MODE_BUTTON_CSS, 'info mode icon')
        core_util_obj.left_click(info_mode_obj)
        sleep(sleep_time)
        
        """
        Step 05.01: Verify blue background appears after clicking info mode button.
        """
        util_obj.verify_element_color_using_css_property(pd_locator_obj.INFO_MODE_BUTTON_CSS, 'summer_sky1', msg='Step 05.01: Verify blue background appears after clicking info mode button.', attribute='background-color')
        
        """
        Step 05.02: Verify that the path location is shown for all the contents in first four panels and the path location and parameters are shown for the contents in middle two panels.
        """
        util_obj.synchronize_with_number_of_element(page_designer_locator_obj.PD_CONTAINER_CSS, 7, main_page_obj.home_page_medium_timesleep)
        
        '''Panel 1, Panel 2, Panel 3, Panel 4'''
        for i, expected_resource_label_value_list in zip(range(1,5), [panel1_resource_label_value, panel2_resource_label_value, panel3_resource_label_value, panel4_resource_label_value]):
            page_designer_obj.verify_resource_label_value(i, expected_resource_label_value_list, step_num="05.02a.0"+str(i))
            page_designer_obj.verify_parameters_label_value(i, expected_parameters_label_value_list, step_num="05.02b.0"+str(i))
        
        '''Panel 5, Panel 6'''
        for j, expected_resource_label_value_list in zip(range(5,7), [panel5_resource_label_value_1, panel6_resource_label_value_1]):
            page_designer_obj.verify_resource_label_value(j, expected_resource_label_value_list, step_num="05.02c.0"+str(j))
            page_designer_obj.verify_parameters_label_value(j, expected_parameters_label_value_list_1, step_num="05.02b.0"+str(j))
            
        """
        Step 06.00: Click on each tab in panel 5 and 6.
        """
        page_designer_obj.tab_container('Category Sales').select_tab('Category Sales')
        sleep(sleep_time)
        page_designer_obj.tab_container('Regional Sales Trend').select_tab('Regional Sales Trend')
        sleep(sleep_time)
        
        """
        Step 06.01: Verify that each tab shows path location and parameters for the contents in middle two panels. 
        """
        '''Panel 5, Panel 6'''
        for k, expected_resource_label_value_list in zip(range(5,7), [panel5_resource_label_value, panel6_resource_label_value]):
            page_designer_obj.verify_resource_label_value(k, expected_resource_label_value_list, step_num="06.01a.0"+str(k))
            page_designer_obj.verify_parameters_label_value(k, expected_parameters_label_value_list_1, step_num="06.01b.0"+str(k))
        
        """
        Step 07.00: Click info mode button. 
        """
        core_util_obj.left_click(info_mode_obj)
        #Once after clicking the infomode button, moving mouse cursor away from it, inorder to verify the background color.
        help_btn_obj = util_obj.validate_and_get_webdriver_object(pd_locator_obj.HELP_BUTTON_CSS, 'help button')
        core_util_obj.move_to_element(help_btn_obj)
        sleep(sleep_time)

        """
        Step 07.01: Verify blue background disappears.
        """
        util_obj.verify_element_color_using_css_property(info_mode_css, 'nero', msg='Step 07.01: Verify blue background disappears.', attribute='background-color')
        
        """
        Step 07.02: Verify that all the panels back to its default state.
        """
        '''Panel 1, Panel 2, Panel 3, Panel 4, Panel 5, Panel 6, Panel 7'''
        for l in range(1,8):
            resource_element_css = page_designer_locator_obj.PD_PANEL_CSS+" [data-ibxp-title$='TITLE_'"+str(l)+"] "+resource_css
            parameters_element_css = page_designer_locator_obj.PD_PANEL_CSS+" [data-ibxp-title$='TITLE_'"+str(l)+"] "+parameters_css
            for m, n in zip([resource_element_css, parameters_element_css], ['resource label value', 'parameters_element label value']):
                util_obj.verify_element_visiblty(element_css=m, visible=False, msg="Step 07.02.0"+str(l)+": Verify that all the panels back to its default state and "+n+" is disabled.")
        
        """
        Step 08.00: Close the Page Designer from application menu and click No
        """ 
        page_designer_obj.close_page_designer_without_save_page()
        
        """
        Step 09.00: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()  