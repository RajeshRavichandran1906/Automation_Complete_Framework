'''
Created on March 26,2019

@author: AA14564
Testcase Name : Create page with Grid 2-1 templates and change Page Theme to Light
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261663
'''
import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools import page_designer
from common.lib.webfocus import designer_canvas
from common.locators.page_designer_design import ToolBar

class C8261663_TestClass(BaseTestCase):
    
    def test_C8261663(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        design_canvas = designer_canvas.Designer_Canvas(self.driver)
        toolbar_obj = ToolBar()
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        page_canvas_css = "[class*='pd-page-canvas']"
        pop_up_dialog_css = ".pop-top"
        style_tab_css ="div[class^='pd-style-tab-page']"
        frame_css = "[src*='V5_Domain_Testing']"
        close_css ="{0}  [class*='close-button']".format(pop_up_dialog_css)
        
        """
        Test case variables
        """
        expected_domain = "V5 Domain Testing"
        expected_portal = 'v5portal1'
        expected_page_heading = ['Page Heading']
        expected_header_button = ['Refresh']
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
        Step 3: Expand 'V5 Domain Testing';
                Click on v5portal1 and select Page tile from action bar
        """
        main_page_obj.expand_repository_folder('{0}->{1}'.format(expected_domain, expected_portal))
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_long_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        
        """
        Step 4: Choose Grid 2-1 template
        """
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_up_dialog_css, 'Grid 2-1', main_page_obj.home_page_long_timesleep)
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: Click on Properties pane -> Style
        """
        util_obj.synchronize_until_element_is_visible(toolbar_obj.PROPERTY_BUTTON_CSS, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.click_property()
        util_obj.synchronize_until_element_is_visible(toolbar_obj.PROPERTY_TAB_CSS.format('Format'), main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_property_tab('Style')
        util_obj.synchronize_with_visble_text(style_tab_css, 'Theme', main_page_obj.home_page_long_timesleep)
        
        """
        Step 6: Click on Theme drop down and select 'Light'
                Verify light theme has been selected as below
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Light')
        time.sleep(3)
        page_designer_obj.verify_setting_tab_properties('Page Style', ['Theme=Light', 'Margin=off', 'Maximum width=off'], 'Step 6: Verify light theme has been selected as below', property_tab_name='style')
        
        """
        Step 7: Click save;
                Enter 'Page Grid 2-1' and click save button
        """
        page_designer_obj.save_page_from_toolbar('Page Grid 2-1')
        
        """
        Step 8: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        
        """
        Step 9: Right click on 'Page Grid 2-1' and click Run
                Verify page appears as below
        """
        core_utill_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page Grid 2-1', main_page_obj.home_page_long_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('Page Grid 2-1', 'Run')
        util_obj.synchronize_with_visble_text(pop_up_dialog_css, 'Page Grid 2-1', main_page_obj.home_page_long_timesleep)
        util_obj.synchronize_until_element_is_visible(frame_css, main_page_obj.home_page_medium_timesleep)
        core_utill_obj.switch_to_frame(frame_css)
        page_designer_obj.verify_page_heading_title(expected_page_heading, 'Step 9.1 : Verify page heading')
        header_buttons = design_canvas.get_page_header_visible_buttons()
        util_obj.verify_list_values(expected_header_button, header_buttons, 'Step 9.2 : Verify refresh button available', 'asin')
        page_designer_obj.verify_containers_title(expected_panel_list, "Step 9.3 : Verify containers title")
        core_utill_obj.switch_to_default_content()
        
        """
        Step 10: Close page
        """
        core_utill_obj.left_click(util_obj.validate_and_get_webdriver_object(close_css, 'Run close button'))
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_long_timesleep)
        
        """
        Step 11: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()