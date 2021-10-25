'''
Created on March 27,2019

@author: AA14564
Testcase Name : Create page with Grid 2-1 Side templates and change Page Theme to Midnight
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261671
'''
import unittest
from common.lib.global_variables import Global_variables
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools.designer_portal import Two_Level_Side
from common.wftools import page_designer


class C8261671_TestClass(BaseTestCase):
    
    def test_C8261671(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        two_level_side_obj = Two_Level_Side(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        run_page_canvas_css = ".pvd-canvas-area"
        page_css = ".pd-page-runner"
        
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
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 3: Expand 'V5 Domain Testing' ;
                Right click on 'v5portal-themes' and select Run;
                Click on 'Page 1 light_style3_style6'
                Verify page appears as below
        """
        main_page_obj.expand_repository_folder('{0}'.format(expected_domain))
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
            Caramel_light_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color6', 'Run page')
            actual_color = Caramel_light_ele.value_of_css_property('background-image').strip().replace(' ', '')
            expected_color = 'linear-gradient(rgba(255,217,144,0.5)0%,rgba(255,217,144,0.8)100%)'
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
           
        """ 
        Step 4: Click on 'Page 1 midnight_style2_style5'
                Verify page appears as below
        """
        two_level_side_obj.select_page_from_top_folder(page2)
        if Global_variables.browser_name == 'chrome':
            sweet_pink_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color5', 'Run page')
            actual_color = sweet_pink_ele.value_of_css_property('background').strip().replace(' ', '')
            expected_color = 'rgba(0,0,0,0)linear-gradient(rgba(249,144,144,0.4)0%,rgba(249,144,144,0.6)100%)repeatscroll0%0%/autopadding-boxborder-box'
            util_obj.asequal(actual_color, expected_color, 'Step 04.00: Verify the panel 2 have Sweet Pink color')
            summer_sky_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color2', 'Run page')
            actual_color = [x.value_of_css_property('background').strip().replace(' ','') for x in summer_sky_ele]
            expected_color = ['rgba(0,0,0,0)linear-gradient(rgba(1,96,178,0.4)0%,rgba(32,157,225,0.7)100%)repeatscroll0%0%/autopadding-boxborder-box', 'rgba(0,0,0,0)linear-gradient(rgba(1,96,178,0.4)0%,rgba(32,157,225,0.7)100%)repeatscroll0%0%/autopadding-boxborder-box']
            util_obj.asequal(actual_color, expected_color, 'Step 04.01: Verify the panel 1 and panel 3 have Summer Sky color')
            page_theme = util_obj.validate_and_get_webdriver_object(page_css, 'Run page')
            actual_color = page_theme.value_of_css_property('background').strip().replace(' ','')
            expected_color = 'rgba(0,0,0,0)linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)repeatscroll0%0%/autopadding-boxborder-box'
            util_obj.asequal(actual_color, expected_color, 'Step 04.02: Verify the page theme')
        else:
            sweet_pink_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color5', 'Run page')
            actual_color = sweet_pink_ele.value_of_css_property('background-image').strip().replace(' ', '')
            expected_color = 'linear-gradient(rgba(249,144,144,0.4)0%,rgba(249,144,144,0.6)100%)'
            util_obj.asequal(actual_color, expected_color, 'Step 04.00: Verify the panel 2 have Sweet Pink color')
            summer_sky_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color2', 'Run page')
            actual_color = [x.value_of_css_property('background-image').strip().replace(' ','') for x in summer_sky_ele]
            expected_color = ['linear-gradient(rgba(1,96,178,0.4)0%,rgba(32,157,225,0.7)100%)', 'linear-gradient(rgba(1,96,178,0.4)0%,rgba(32,157,225,0.7)100%)']
            util_obj.asequal(actual_color, expected_color, 'Step 04.01: Verify the panel 1 and panel 3 have Summer Sky color')
            page_theme = util_obj.validate_and_get_webdriver_object(page_css, 'Run page')
            actual_color = page_theme.value_of_css_property('background-image').strip().replace(' ','')
            expected_color = 'linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)'
            util_obj.asequal(actual_color, expected_color, 'Step 04.02: Verify the page theme')
        page_designer_obj.verify_containers_title(expected_panel_list, "Step 04.03: Verify containers title")
        
        """ 
        Step 5: Expand 'v5folder1';
                Click on 'Page 2 default_heading1_style4_style7'
                Verify page appears as below
        """
        two_level_side_obj.select_page_from_folder_in_left_sidebar(folder_name, page3)
        if Global_variables.browser_name == 'chrome':
            black_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color7', 'Run page')
            actual_color = black_ele.value_of_css_property('background').strip().replace(' ', '')
            expected_color = 'rgba(0,0,0,0)linear-gradient(rgba(0,0,0,0.2)0%,rgba(0,0,0,0.1)100%)repeatscroll0%0%/autopadding-boxborder-box'
            util_obj.asequal(actual_color, expected_color, 'Step 05.00: Verify the panel 2 have black color')
            conflower_blue_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color4', 'Run page')
            actual_color = [x.value_of_css_property('background').strip().replace(' ','') for x in conflower_blue_ele]
            expected_color = ['rgba(0,0,0,0)linear-gradient(rgba(80,80,200,0.4)0%,rgba(99,137,244,0.8)100%)repeatscroll0%0%/autopadding-boxborder-box', 'rgba(0,0,0,0)linear-gradient(rgba(80,80,200,0.4)0%,rgba(99,137,244,0.8)100%)repeatscroll0%0%/autopadding-boxborder-box']
            util_obj.asequal(actual_color, expected_color, 'Step 05.01: Verify the panel 1 and panel 3 have Cornflower Blue color')
            page_theme = util_obj.validate_and_get_webdriver_object(page_css, 'Run page')
            actual_color = page_theme.value_of_css_property('background').strip().replace(' ','')
            expected_color = 'rgba(0,0,0,0)linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)repeatscroll0%0%/autopadding-boxborder-box'
            util_obj.asequal(actual_color, expected_color, 'Step 05.02: Verify the page theme')
        else:
            black_ele = util_obj.validate_and_get_webdriver_object('.pd-container.pd-style-color7', 'Run page')
            actual_color = black_ele.value_of_css_property('background-image').strip().replace(' ', '')
            expected_color = 'linear-gradient(rgba(0,0,0,0.2)0%,rgba(0,0,0,0.1)100%)'
            util_obj.asequal(actual_color, expected_color, 'Step 05.00: Verify the panel 2 have black color')
            conflower_blue_ele = util_obj.validate_and_get_webdriver_objects('.pd-container.pd-style-color4', 'Run page')
            actual_color = [x.value_of_css_property('background-image').strip().replace(' ','') for x in conflower_blue_ele]
            expected_color = ['linear-gradient(rgba(80,80,200,0.4)0%,rgba(99,137,244,0.8)100%)', 'linear-gradient(rgba(80,80,200,0.4)0%,rgba(99,137,244,0.8)100%)']
            util_obj.asequal(actual_color, expected_color, 'Step 05.01: Verify the panel 1 and panel 3 have Cornflower Blue color')
            page_theme = util_obj.validate_and_get_webdriver_object(page_css, 'Run page')
            actual_color = page_theme.value_of_css_property('background-image').strip().replace(' ','')
            expected_color = 'linear-gradient(toright,rgb(77,64,112)0%,rgb(67,110,164)100%)'
            util_obj.asequal(actual_color, expected_color, 'Step 05.02: Verify the page theme')
        page_designer_obj.verify_containers_title(expected_panel_list, "Step 05.03: Verify containers title")
        
        """ 
        Step 6: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal, main_page_obj.home_page_long_timesleep)
        
        """ 
        Step 7: Sign Out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()