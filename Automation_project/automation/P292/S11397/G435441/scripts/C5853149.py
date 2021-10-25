'''
Created on June 04, 2019.

@author: Magesh

Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/5853149
TestCase Name = Check Settings for regular panels with content
'''

import unittest
from time import sleep
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage, chart
from common.lib import utillity
from common.locators import wf_mainpage_locators, page_designer_design, page_designer_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.lib.global_variables import Global_variables

class C5853149_TestClass(BaseTestCase):

    def test_C5853149(self):
        
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
        fex_name = 'C5853145'
        repository_folder = 'Workspaces->P292_S11397->G435441'
        report_action_bar = 'Report'
        panel1_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Blue.html']
        panel2_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Gray.html']
        panel3_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Green.html']
        panel4_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Test_Widgets/Red.html']
        panel5_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Category_Sales.fex']
        panel6_resource_label_value = ['Reference Path', 'IBFS:/WFC/Repository/Retail_Samples/Portal/Small_Widgets/Regional_Sales_Trend.fex']
        expected_parameters_label_value_list = ['Parameters/Filters', 'None']
        expected_parameters_label_value_list1 = ['Parameters/Filters', 'PRODUCT_CATEGORY MODEL BUSINESS_REGION STORE_TYPE TIME_DATE TIME_DATE_TO']
        sleep_time = 5
        
        """
        TESTCASE CSS
        """
        info_mode_css = "div[title='Info mode'].ibxtool-toolbar-button"
        resource_css = "div[class*='pdcnt-resource']"
        parameters_css = "div[class*='pdcnt-parameters']"
        
        """
        Step 01.00: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 02.00: Click on Content View from the side bar
        """  
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_long_timesleep)
        
        """
        Step 03.00: Navigate to the folder P292_S11397/G435441;
        """
        main_page_obj.expand_repository_folder(repository_folder)
        
        """
        Right click on 'C5853145' and choose Edit
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, report_action_bar, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, context_menu_item_path='Edit')
        
        """
        Step 05.00: Navigate to Retail Samples > Portal > Test Widgets from the tree;
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(page_designer_locator_obj.PD_PANEL_CSS, 7, main_page_obj.home_page_long_timesleep)
        page_designer_obj.collapse_content_folder('G435441->P292_S11397')
        sleep(sleep_time)
        
        """
        Drag and drop Blue,Gray,Green and Red widgets to the first four panels
        """
        page_designer_obj.drag_content_item_to_container("Blue", "Panel 1", content_folder_path="Retail Samples->Portal->Test Widgets")
        page_designer_obj.collapse_content_folder('Test Widgets->Portal->Retail Samples')
        page_designer_obj.drag_content_item_to_container("Gray", "Panel 2", content_folder_path="Retail Samples->Portal->Test Widgets")
        page_designer_obj.collapse_content_folder('Test Widgets->Portal->Retail Samples')
        page_designer_obj.drag_content_item_to_container("Green", "Panel 3", content_folder_path="Retail Samples->Portal->Test Widgets")
        page_designer_obj.collapse_content_folder('Test Widgets->Portal->Retail Samples')
        page_designer_obj.drag_content_item_to_container("Red", "Panel 4", content_folder_path="Retail Samples->Portal->Test Widgets")
        
        """
        Step 04.01: Verify that the four panels are populated with contents as below
        """
        #Panel1
        page_designer_obj.switch_to_container_frame('Blue')
        panel1_bg_color_obj = util_obj.validate_and_get_webdriver_object("html>body[style]", 'Panel1 background color')
        actual_color=util_obj.get_element_css_propery(panel1_bg_color_obj, attrib='background-color')
        if Global_variables.browser_name == 'firefox':
            expected_color=util_obj.color_picker('blue', 'rgb')
        else:
            expected_color=util_obj.color_picker('blue', 'rgba')
        util_obj.asequal(expected_color, actual_color, 'Step 04.01a: Verify blue background in panel1')
        core_util_obj.switch_to_default_content()
        
        #Panel2
        page_designer_obj.switch_to_container_frame('Gray')
        panel2_bg_color_obj = util_obj.validate_and_get_webdriver_object("html>body[style]", 'Panel2 background color')
        actual_color=util_obj.get_element_css_propery(panel2_bg_color_obj, attrib='background-color')
        if Global_variables.browser_name == 'firefox':
            expected_color=util_obj.color_picker('dim_gray1', 'rgb')
        else:
            expected_color=util_obj.color_picker('dim_gray1', 'rgba')
        util_obj.asequal(expected_color, actual_color, 'Step 04.01b: Verify gray background in panel2')
        core_util_obj.switch_to_default_content()
        
        #Panel3
        page_designer_obj.switch_to_container_frame('Green')
        panel3_bg_color_obj = util_obj.validate_and_get_webdriver_object("html>body[style]", 'Panel3 background color')
        actual_color=util_obj.get_element_css_propery(panel3_bg_color_obj, attrib='background-color')
        if Global_variables.browser_name == 'firefox':
            expected_color=util_obj.color_picker('green', 'rgb')
        else:
            expected_color=util_obj.color_picker('green', 'rgba')
        util_obj.asequal(expected_color, actual_color, 'Step 04.01c: Verify green background in panel3')
        core_util_obj.switch_to_default_content()
        
        #Panel4
        page_designer_obj.switch_to_container_frame('Red')
        panel4_bg_color_obj = util_obj.validate_and_get_webdriver_object("html>body[style]", 'Panel4 background color')
        actual_color=util_obj.get_element_css_propery(panel4_bg_color_obj, attrib='background-color')
        if Global_variables.browser_name == 'firefox':
            expected_color=util_obj.color_picker('red', 'rgb')
        else:
            expected_color=util_obj.color_picker('red', 'rgba')
        util_obj.asequal(expected_color, actual_color, 'Step 04.01d: Verify red background in panel4')
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
        Step 05.02: Verify that the path location is shown for all the contents in first four panels as below
        """
        util_obj.synchronize_with_number_of_element(page_designer_locator_obj.PD_PANEL_CSS, 7, main_page_obj.home_page_medium_timesleep)
        for i, expected_resource_label_value_list in zip(range(1,5), [panel1_resource_label_value, panel2_resource_label_value, panel3_resource_label_value, panel4_resource_label_value]):
            page_designer_obj.verify_resource_label_value(i, expected_resource_label_value_list, step_num="05.02a.0"+str(i))
            page_designer_obj.verify_parameters_label_value(i, expected_parameters_label_value_list, step_num="05.02b.0"+str(i))
        
        """
        Step 06.00: Click info mode button. 
        """
        core_util_obj.left_click(info_mode_obj)
        #Once after clicking the infomode button, moving mouse cursor away from it, inorder to verify the background color.
        help_btn_obj = util_obj.validate_and_get_webdriver_object(pd_locator_obj.HELP_BUTTON_CSS, 'help button')
        core_util_obj.move_to_element(help_btn_obj)
        sleep(sleep_time)

        """
        Step 06.01: Verify blue background disappears.
        """
        util_obj.verify_element_color_using_css_property(info_mode_css, 'nero', msg='Step 06.01: Verify blue background disappears.', attribute='background-color')
        
        """
        Step 06.02: Verify that all the panels back to its default state.
        """
        for i in range(1,8):
            resource_element_css = page_designer_locator_obj.PD_PANEL_CSS+" [data-ibxp-title$='TITLE_'"+str(i)+"] "+resource_css
            parameters_element_css = page_designer_locator_obj.PD_PANEL_CSS+" [data-ibxp-title$='TITLE_'"+str(i)+"] "+parameters_css
            for j, k in zip([resource_element_css, parameters_element_css], ['resource label value', 'parameters_element label value']):
                util_obj.verify_element_visiblty(element_css=j, visible=False, msg="Step 06.02.0"+str(i)+": Verify that all the panels back to its default state and "+k+" is disabled.")
        
        """
        Step 07.00: Navigate to Retail Samples > Portal > Small Widgets from the tree;
        """
        page_designer_obj.collapse_content_folder('Test Widgets')
        sleep(sleep_time)
        
        """
        Drag and drop 'Category Sales' and 'Regional Sales' to the middle 2 panels.
        """
        page_designer_obj.select_container("Panel 5")
        page_designer_obj.drag_content_item_to_container("Category Sales", "Panel 5", content_folder_path="Small Widgets")
        sleep(sleep_time)
        page_designer_obj.collapse_content_folder('Small Widgets')
        page_designer_obj.select_container("Panel 6")
        page_designer_obj.drag_content_item_to_container("Regional Sales Trend", "Panel 6", content_folder_path="Small Widgets")
        sleep(sleep_time)
        
        """
        Step 07.01: Verify that the two panels are populated with the content.
        """
        page_designer_obj.switch_to_container_frame('Category Sales')
        total_label_css="#jschart_HOLD_0 text[class^='totalLabel!']"
        util_obj.synchronize_with_visble_text(total_label_css, '1.1B', main_page_obj.home_page_short_timesleep)
        chart_obj.verify_pie_label_in_single_group_in_preview(expected_label_list=['Revenue'], parent_css="#jschart_HOLD_0", msg="Step 07.01a")
        chart_obj.verify_number_of_pie_segments("#jschart_HOLD_0", 1, 7, msg="Step 07.01b")
        core_util_obj.switch_to_default_content()
        
        page_designer_obj.switch_to_container_frame('Regional Sales Trend')
        chart_obj.verify_x_axis_title_in_preview(expected_title_list=['Month'], parent_css="#jschart_HOLD_0", msg="Step 07.01a")
        chart_obj.verify_y_axis_title_in_preview(expected_title_list=['Revenue'], parent_css="#jschart_HOLD_0", msg="Step 07.01b")
        chart_obj.verify_x_axis_label_in_preview(expected_label_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], parent_css="#jschart_HOLD_0", msg="Step 07.01c")
        chart_obj.verify_y_axis_label_in_preview(expected_label_list=['0', '10M', '20M', '30M', '40M', '50M', '60M', '70M'], parent_css="#jschart_HOLD_0", msg="Step 07.01d")
        chart_obj.verify_number_of_chart_segment("jschart_HOLD_0", 4, msg="Step 07.01e: verify number of line segments available", custom_css="path[class^='riser']")
        core_util_obj.switch_to_default_content()
        
        """
        Step 08.00: Click info mode button.
        """
        util_obj.synchronize_with_number_of_element(pd_locator_obj.INFO_MODE_BUTTON_CSS, 1, main_page_obj.home_page_medium_timesleep)
        info_mode_obj = util_obj.validate_and_get_webdriver_object(pd_locator_obj.INFO_MODE_BUTTON_CSS, 'info mode icon')
        core_util_obj.left_click(info_mode_obj)
        sleep(sleep_time)
        
        """
        Step 08.01: Verify that the path location and parameters are shown for the contents in middle two panels.
        """
        util_obj.synchronize_with_number_of_element(page_designer_locator_obj.PD_PANEL_CSS, 7, main_page_obj.home_page_medium_timesleep)
        for i, expected_resource_label_value_list in zip(range(5, 7), [panel5_resource_label_value, panel6_resource_label_value]):
            page_designer_obj.verify_resource_label_value(i, expected_resource_label_value_list, step_num="08.01a.0"+str(i))
            page_designer_obj.verify_parameters_label_value(i, expected_parameters_label_value_list1, step_num="08.01b.0"+str(i))
           
        """
        Step 09.00: Click info mode button. 
        """
        core_util_obj.left_click(info_mode_obj)
        sleep(sleep_time)
        
        """
        Step 09.01: Verify that all the panels back to its default state.
        """
        for i in range(1,8):
            resource_element_css = page_designer_locator_obj.PD_PANEL_CSS+" [data-ibxp-title$='TITLE_'"+str(i)+"] "+resource_css
            parameters_element_css = page_designer_locator_obj.PD_PANEL_CSS+" [data-ibxp-title$='TITLE_'"+str(i)+"] "+parameters_css
            for j, k in zip([resource_element_css, parameters_element_css], ['resource label value', 'parameters_element label value']):
                util_obj.verify_element_visiblty(element_css=j, visible=False, msg="Step 09.01.0"+str(i)+": Verify that all the panels back to its default state and "+k+" is disabled.")
        
        """
        Step 10.00: Close the Page Designer from application menu and click No
        """ 
        page_designer_obj.close_page_designer_without_save_page()
        
        """
        Step 11.00: In the banner link, click on the top right username > Click Sign Out.
        """ 
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_short_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
      
if __name__ == '__main__':
    unittest.main()