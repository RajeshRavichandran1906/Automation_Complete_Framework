'''
Created on March 29,2019

@author: AA14564
Testcase Name : Test Portal Themes to change other settings with Pages Themes(different styles in container and heading)
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261672
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools.designer_portal import Two_Level_Side
from common.lib.webfocus.designer_canvas import Designer_Canvas
from common.wftools import page_designer
from common.wftools.designer_portal import Portal
from common.locators.page_designer_locators import PageDesigner
from common.lib.global_variables import Global_variables
import time

class C8261672_TestClass(BaseTestCase):
    
    def test_C8261672(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        design_canvas = Designer_Canvas(self.driver)
        two_level_side_obj = Two_Level_Side(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        designer_portal_obj = Portal(self.driver)
        pd_locators_obj = PageDesigner()
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        run_page_canvas_css = ".pvd-canvas-area"
        page_css = ".pd-page-runner"
        popup_css = ".pop-top"
        containers_title_css=pd_locators_obj.PD_CONTAINER_CSS + " .pd-container-title-bar"
        
        """
        Test case variables
        """
        expected_domain = "V5 Domain Testing"
        expected_portal = 'v5portal-themes'
        page1 = 'Page 1 light_style3_style6'
        page2 = 'Page 1 midnight_style2_style5'
        page3 = 'Page 2 default_heading1_style4_style7'
        folder_name = 'v5folder1' 
        expected_panel_list = ["Panel 1", "Panel 2", "Panel 3"]

        '''
        local function
        '''
        def get_panel_title_object_color_attribute(panel_name):
            '''
            Description : This function will return panel title 'color' and 'background-color'
            '''
            panel_object = util_obj.validate_and_get_webdriver_object(containers_title_css, panel_name+' Title', parent_object=design_canvas.get_container_parent_object(panel_name))
            panel_color = util_obj.get_element_css_propery(panel_object, 'color').strip().replace(' ','')
            panel_background_color = util_obj.get_element_css_propery(panel_object, 'background-color').strip().replace(' ','')
            return [panel_color, panel_background_color]
            
        
        """
        Step 1: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'V5 Domain Testing' 
                Right click on 'v5portal-themes' and click Run;
                Click on 'Page 1 light_style3_style6'
                Verify page appears as below
        """
        main_page_obj.expand_repository_folder('{0}'.format(expected_domain))
        util_obj.wait_for_page_loads(10)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal, main_page_obj.home_page_long_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(expected_portal, context_menu_item_path='Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(run_page_canvas_css, page1, main_page_obj.home_page_long_timesleep)
        two_level_side_obj.select_page_from_top_folder(page1)
        if Global_variables.browser_name == 'chrome':
            Caramel_light_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color6', 'Run page')
            actual_color = Caramel_light_ele.value_of_css_property('background').strip().replace(' ', '')
            expected_color = 'rgba(0,0,0,0)linear-gradient(rgba(255,217,144,0.5)0%,rgba(255,217,144,0.8)100%)repeatscroll0%0%/autopadding-boxborder-box'
            util_obj.asequal(actual_color, expected_color, 'Step 03.00: Verify the panel 2 have Caramel color')
            eastern_blue_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color3', 'Run page')
            actual_color = [x.value_of_css_property('background').strip().replace(' ','') for x in eastern_blue_ele]
            expected_color = ['rgba(0,0,0,0)linear-gradient(rgba(4,129,151,0.4)0%,rgba(0,197,221,0.7)100%)repeatscroll0%0%/autopadding-boxborder-box', 'rgba(0,0,0,0)linear-gradient(rgba(4,129,151,0.4)0%,rgba(0,197,221,0.7)100%)repeatscroll0%0%/autopadding-boxborder-box']
            util_obj.asequal(actual_color, expected_color, 'Step 03.01: Verify the panel 1 and panel 3 have Eastern Blue color')
            page_theme = util_obj.validate_and_get_webdriver_object(page_css, 'Run page')
            actual_color = page_theme.value_of_css_property('background').strip().replace(' ','')
            expected_color = 'rgba(0,0,0,0)linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)repeatscroll0%0%/autopadding-boxborder-box'
            util_obj.asequal(actual_color, expected_color, 'Step 03.02: Verify the page theme')
        else:
            time.sleep(15)
            Caramel_light_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color6', 'Run page')
            actual_color = Caramel_light_ele.value_of_css_property('background-image').strip().replace(' ', '')
            expected_color = 'linear-gradient(rgba(255,217,144,0.5)0%,rgba(255,217,144,0.8)100%)'
            util_obj.wait_for_page_loads(20)
            util_obj.asequal(actual_color, expected_color, 'Step 03.00: Verify the panel 2 have Caramel color')
            eastern_blue_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color3', 'Run page')
            actual_color = [x.value_of_css_property('background-image').strip().replace(' ','') for x in eastern_blue_ele]
            expected_color = ['linear-gradient(rgba(4,129,151,0.4)0%,rgba(0,197,221,0.7)100%)', 'linear-gradient(rgba(4,129,151,0.4)0%,rgba(0,197,221,0.7)100%)']
            util_obj.asequal(actual_color, expected_color, 'Step 03.01: Verify the panel 1 and panel 3 have Eastern Blue color')
            page_theme = util_obj.validate_and_get_webdriver_object(page_css, 'Run page')
            actual_color = page_theme.value_of_css_property('background-image').strip().replace(' ','')
            expected_color = 'linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)'
            util_obj.asequal(actual_color, expected_color, 'Step 03.02: Verify the page theme')
        page_designer_obj.verify_containers_title(expected_panel_list, "Step 03.03: Verify containers title")
        two_level_side_obj.verify_page_name_in_from_top_folder(page1, "Step 03.04: Verify page appears as below")
        two_level_side_obj.verify_page_name_in_from_top_folder(page2, "Step 03.05: Verify page appears as below")
        two_level_side_obj.verify_folders_in_left_sidebar([folder_name], "Step 03.06: Verify page appears as below",assert_type='asin')
        
        """
        Step 4: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal, main_page_obj.home_page_long_timesleep)
        
        """
        Step 5: Right click on 'v5portal-themes' and click Edit
                Verify Midnight theme has been selected as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(expected_portal, context_menu_item_path='Edit')
        util_obj.synchronize_with_visble_text(popup_css, 'Theme', main_page_obj.home_page_long_timesleep)
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Midnight', step_number='05.00')
        
        """
        Step 6: Click on Theme drop down and select 'Designer 2018'
                Verify Designer 2018 theme has been selected as below
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Designer 2018')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='06.00')
        
        """
        Step 7: Click save
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
        time.sleep(5)
        
        """
        Step 8: Right click on 'v5portal-themes' and click Run;
                Click on 'Page 1 light_style3_style6'
                Verify page appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(expected_portal, context_menu_item_path='Run')
        util_obj.wait_for_page_loads(10)
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(run_page_canvas_css, page1, main_page_obj.home_page_long_timesleep)
        two_level_side_obj.select_page_from_top_folder(page1)
        color_ele = util_obj.validate_and_get_webdriver_objects('.pd-container-content', 'Run page')
        content_color = [x.value_of_css_property('background-color').strip().replace(' ','') for x in color_ele]
        expected_color = ['rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)']
        util_obj.asequal(content_color, expected_color, 'Step 08.01: Verify all 3 panel content color in page')
        color_ele = util_obj.validate_and_get_webdriver_objects('.pd-container-title-bar', 'Run page')
        title_color = [x.value_of_css_property('background-color').strip().replace(' ','') for x in color_ele]
        if Global_variables.browser_name == 'chrome':
            expected_color = ['rgba(92,184,92,1)', 'rgba(217,83,79,1)', 'rgba(92,184,92,1)']
        else:
            expected_color = ['rgb(92,184,92)', 'rgb(217,83,79)', 'rgb(92,184,92)']
        util_obj.asequal(title_color, expected_color, 'Step 08.02: Verify all 3 panel title color in page')
        page_designer_obj.verify_containers_title(expected_panel_list, "Step 08.03: Verify containers title")
        two_level_side_obj.verify_page_name_in_from_top_folder(page1, "Step 08.04: Verify page appears as below")
        two_level_side_obj.verify_page_name_in_from_top_folder(page2, "Step 08.05: Verify page appears as below")
        two_level_side_obj.verify_folders_in_left_sidebar([folder_name], "Step 08.06: Verify page appears as below",assert_type='asin')
        
        """
        Step 9: Click on 'Page 1 Midnight_style2_style5'
                Verify page appears as below
        """
        two_level_side_obj.select_page_from_top_folder(page2)      
        color_ele = util_obj.validate_and_get_webdriver_objects('.pd-container-content', 'Run page')
        content_color = [x.value_of_css_property('background-color').strip().replace(' ','') for x in color_ele if x.is_displayed()]
        expected_color = ['rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)']
        util_obj.asequal(content_color, expected_color, 'Step 09.00: Verify all 3 panel content color in page')
        color_ele = util_obj.validate_and_get_webdriver_objects('.pd-container-title-bar', 'Run page')
        title_color = [x.value_of_css_property('background-color').strip().replace(' ','') for x in color_ele if x.is_displayed()]
        if Global_variables.browser_name == 'chrome':
            expected_color = ['rgba(51,122,183,1)', 'rgba(240,173,78,1)', 'rgba(51,122,183,1)']
        else:
            expected_color = ['rgb(51,122,183)', 'rgb(240,173,78)', 'rgb(51,122,183)']
        util_obj.asequal(title_color, expected_color, 'Step 09.01: Verify all 3 panel title color in page')
        page_designer_obj.verify_containers_title(expected_panel_list, "Step 09.02: Verify containers title")
        
        """
        Step 10: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal, main_page_obj.home_page_long_timesleep)
        
        """
        Step 11: Right click on 'v5portal-themes' and click Edit
                 Verify Designer 2018 theme has been selected as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(expected_portal, context_menu_item_path='Edit')
        util_obj.synchronize_with_visble_text(popup_css, 'Theme', main_page_obj.home_page_long_timesleep)
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Designer 2018', step_number='11.00')
        
        """
        Step 12: Click on Theme drop down and select 'Light'
                 Verify light theme has been selected as below
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Light')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Light', step_number='12.00')
        
        """
        Step 13: Click save
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        
        """
        Step 14: Right click on 'v5portal-themes' and click Run;
                 Click on 'Page 1 light_style3_style6'
                 Verify page appears as below
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(expected_portal, context_menu_item_path='Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(run_page_canvas_css, page1, main_page_obj.home_page_long_timesleep)
        two_level_side_obj.select_page_from_top_folder(page1)
        misty_rose_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color6', 'Run page')
        actual_color = misty_rose_ele.value_of_css_property('background-color').strip().replace(' ', '')
        if Global_variables.browser_name == 'chrome':
            expected_color = 'rgba(252,231,227,1)'
        else:
            time.sleep(5)
            expected_color = 'rgb(252,231,227)'
        util_obj.asequal(actual_color, expected_color, 'Step 14.00: Verify panel 2 color in page')
        
        panache_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color3', 'Run page')
        actual_color = [x.value_of_css_property('background-color').strip().replace(' ', '') for x in panache_ele]
        if Global_variables.browser_name == 'chrome':
            expected_color = ['rgba(245,253,241,1)', 'rgba(245,253,241,1)']
        else:
            time.sleep(5)
            expected_color = ['rgb(245,253,241)', 'rgb(245,253,241)']
        util_obj.asequal(actual_color, expected_color, 'Step 14.01: Verify panel 1 and panel 3 color in page')
        page_designer_obj.verify_containers_title(expected_panel_list, "Step 14.02: Verify containers title")
        two_level_side_obj.verify_page_name_in_from_top_folder(page1, "Step 14.03: Verify page appears as below")
        two_level_side_obj.verify_page_name_in_from_top_folder(page2, "Step 14.04: Verify page appears as below")
        two_level_side_obj.verify_folders_in_left_sidebar([folder_name], "Step 14.05: Verify page appears as below",assert_type='asin')
        
        """
        Step 15: Expand 'v5folder1';
                 Click on 'Page 2 default_heading1_style4_style7'
                 Verify page appears as below
        """
        two_level_side_obj.select_page_from_folder_in_left_sidebar(folder_name, page3)
        night_rider_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color7', 'Run page')
        actual_color = night_rider_ele.value_of_css_property('background-color').strip().replace(' ', '')
        if Global_variables.browser_name == 'chrome':
            expected_color = 'rgba(48,48,48,1)'
        else:
            time.sleep(5)
            expected_color = 'rgb(48,48,48)'
        util_obj.asequal(actual_color, expected_color, 'Step 15.00: Verify panel 2 color in page')
        
        azure_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color4', 'Run page')
        actual_color = [x.value_of_css_property('background-color').strip().replace(' ', '') for x in azure_ele]
        if Global_variables.browser_name == 'chrome':
            expected_color = ['rgba(233,247,248,1)', 'rgba(233,247,248,1)']
        else:
            time.sleep(5)
            expected_color = ['rgb(233,247,248)', 'rgb(233,247,248)']
        util_obj.asequal(actual_color, expected_color, 'Step 15.01: Verify panel 1 and panel 3 color in page')
        page_designer_obj.verify_containers_title(expected_panel_list, "Step 15.02: Verify containers title")
        
        """
        Step 16: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal, main_page_obj.home_page_long_timesleep)
        
        """
        Step 17: Right click on 'v5portal-themes' and click Edit
                 Verify light theme has been selected as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(expected_portal, context_menu_item_path='Edit')
        util_obj.synchronize_with_visble_text(popup_css, 'Theme', main_page_obj.home_page_long_timesleep)
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Light', step_number='17.00')
        
        """
        Step 18: Click on Theme drop down and select 'Midnight'
                 Verify Midnight theme has been selected as below
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(select_theme='Midnight')
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog(verify_theme='Midnight', step_number='18.00')
        
        """
        Step 19: Click save
        """
        designer_portal_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.wait_for_page_loads(10)
        
        """
        Step 20" Right click on 'v5portal-themes' and click Run;
                 Expand 'v5folder1';
                 Click on 'Page 2 default_heading1_style4_style7'
                 Verify page appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(expected_portal, context_menu_item_path='Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(run_page_canvas_css, page1, main_page_obj.home_page_long_timesleep)
        two_level_side_obj.select_page_from_folder_in_left_sidebar(folder_name, page3)
        if Global_variables.browser_name == 'chrome':
            black_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color7', 'Run page')
            actual_color = black_ele.value_of_css_property('background').strip().replace(' ', '')
            expected_color = 'rgba(0,0,0,0)linear-gradient(rgba(0,0,0,0.2)0%,rgba(0,0,0,0.1)100%)repeatscroll0%0%/autopadding-boxborder-box'
            util_obj.asequal(actual_color, expected_color, 'Step 20.00: Verify the panel 2 have black color')
            conflower_blue_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color4', 'Run page')
            actual_color = [x.value_of_css_property('background').strip().replace(' ','') for x in conflower_blue_ele]
            expected_color = ['rgba(0,0,0,0)linear-gradient(rgba(80,80,200,0.4)0%,rgba(99,137,244,0.8)100%)repeatscroll0%0%/autopadding-boxborder-box', 'rgba(0,0,0,0)linear-gradient(rgba(80,80,200,0.4)0%,rgba(99,137,244,0.8)100%)repeatscroll0%0%/autopadding-boxborder-box']
            util_obj.asequal(actual_color, expected_color, 'Step 20.01: Verify the panel 1 and panel 3 have Cornflower Blue color')
            page_theme = util_obj.validate_and_get_webdriver_object(page_css, 'Run page')
            actual_color = page_theme.value_of_css_property('background').strip().replace(' ','')
            expected_color = 'rgba(0,0,0,0)linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)repeatscroll0%0%/autopadding-boxborder-box'
            util_obj.asequal(actual_color, expected_color, 'Step 20.02: Verify the page theme')
        else:
            time.sleep(10)
            black_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color7', 'Run page')
            actual_color = black_ele.value_of_css_property('background-image').strip().replace(' ', '')
            expected_color = 'linear-gradient(rgba(0,0,0,0.2)0%,rgba(0,0,0,0.1)100%)'
            util_obj.asequal(actual_color, expected_color, 'Step 20.00: Verify the panel 2 have black color')
            conflower_blue_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color4', 'Run page')
            actual_color = [x.value_of_css_property('background-image').strip().replace(' ','') for x in conflower_blue_ele]
            expected_color = ['linear-gradient(rgba(80,80,200,0.4)0%,rgba(99,137,244,0.8)100%)', 'linear-gradient(rgba(80,80,200,0.4)0%,rgba(99,137,244,0.8)100%)']
            util_obj.asequal(actual_color, expected_color, 'Step 20.01: Verify the panel 1 and panel 3 have Cornflower Blue color')
            page_theme = util_obj.validate_and_get_webdriver_object(page_css, 'Run page')
            actual_color = page_theme.value_of_css_property('background-image').strip().replace(' ','')
            expected_color = 'linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)'
            util_obj.asequal(actual_color, expected_color, 'Step 20.02: Verify the page theme')
        two_level_side_obj.verify_page_name_in_from_top_folder(page1, "Step 20.03: Verify page appears as below")
        two_level_side_obj.verify_page_name_in_from_top_folder(page2, "Step 20.04: Verify page appears as below")
        two_level_side_obj.verify_folders_in_left_sidebar([folder_name], "Step 20.05: Verify page appears as below",assert_type='asin')
        
        """
        Step 21: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal, main_page_obj.home_page_long_timesleep)
        
        """
        Step 22: Sign Out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()
    