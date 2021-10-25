'''
Created on March 27,2019

@author: varun
Testcase Name : Test Widgets\Explorer - Page Style and Page Heading Style
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261670
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.page_designer import Design
from common.wftools.page_designer import Preview

class C8261670_TestClass(BaseTestCase):
    
    def test_C8261670(self):
        """
        Test_case objects
        """
        page_preview_obj = Preview(self.driver)
        page_designer_obj = Design(self.driver)
        login_obj = Login(self.driver)
        main_page_obj = Wf_Mainpage(self.driver)
        util_obj = UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        collapse_button_css = ".tree-button-box .tree-collapse-button"
        page_title_css = ".pd-page-title"
        
        """
        Test case variables
        """
        midnight_blue_list = ["linear-gradient","toright","rgb(77,64,112)", "rgb(67,110,164)"]
        expected_heading_styles = ['Normal', 'Heading 1', 'Heading 2', 'Heading 3', 'Heading 4', 'Heading 5', 'Title', 'Subtitle']
        
        """
        Step 1: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ 
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'V5 Domain Testing';
        Click on 'v5portal1' and select Page tile from action bar
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Workspaces->V5 Domain Testing->v5portal1')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Action Bar\"]", 'Action Bar', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
         
        """
        Step 4: Choose Blank template
        """
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'New Page', main_page_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
         
        """
        Step 5: Click on Repository Widgets
        """
        page_designer_obj.expand_and_collapse_repository_widgets_tab('expand')
         
        """
        Step 6: Drag Explorer icon to the page canvas
        Verify page appears with explorer as below
        """
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas('Explorer', 1)
        page_designer_obj.switch_to_container_frame('Panel 1')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_crumb_box('Workspaces->V5 Domain Testing->v5portal1', "Step 6.1: Verify the crumb box")
         
        """
        Step 7: Click Preview.
        """
        core_util_obj.switch_to_default_content()
        page_designer_obj.click_preview()
         
        """
        Step 8: Collapse resource tree in Explorer widget.
        """
        util_obj.synchronize_with_number_of_element("div[class*='pd-preview-button']", 1, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.switch_to_container_frame('Panel 1')
        collapse_button=util_obj.validate_and_get_webdriver_object(collapse_button_css, "collapse-button")
        core_util_obj.left_click(collapse_button)
        show_collapse_button = util_obj.validate_and_get_webdriver_object(".tree-button-box2 .tree-showcollapse-button", "show-collapse").text.strip()
        util_obj.asequal(show_collapse_button, 'keyboard_arrow_right', "Step 8.1: Verify the tree is collapsed")
         
        """
        Step 9: Click <- to get back to design mode
        """
        core_util_obj.switch_to_default_content()
        page_preview_obj.go_back_to_design_from_preview()
         
        """
        Step 10: Click on Properties tab
        """
        page_designer_obj.click_property()
         
        """
        Step 11: Click on Style.
        """
        page_designer_obj.select_property_tab('style') 
         
        """
        Step 12: Select Style 2.
        Verify styling has been applied as below
        """
        style_two = util_obj.validate_and_get_webdriver_object("div[data-ibxp-user-value=\"pd-style-color2\"]", "stylebuttontwo")
        core_util_obj.left_click(style_two)
        actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-container-title-bar", "page_tab"), 'background').strip().replace(' ','')
        for index_, item in enumerate(["rgb(51,122,183)"], 1):
            util_obj.asin(item, actual_color, "Step 12.{0}: Verify styling has been changed ot style 2".format(index_))
         
        """
        Step 13: Select Style 5.
        Verify that you don't see the Folders widget;
        Verify styling has been applied as below
        """
        style_five = util_obj.validate_and_get_webdriver_object("div[data-ibxp-user-value=\"pd-style-color5\"]", "stylebuttonfive")
        core_util_obj.left_click(style_five)
        actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-container-title-bar", "page_tab"), 'background').strip().replace(' ','')
        for index_, item in enumerate(["rgb(240,173,78)"], 1):
            util_obj.asin(item, actual_color, "Step 13.{0}: Verify styling has been changed ot style 2".format(index_))
        repository_widgets = util_obj.validate_and_get_webdriver_object(".pd-repository-widgets .ibxtool-panel-basic-containers","widgets").text.lower().strip()
        util_obj.as_notin("folders", repository_widgets, "Step 13.1: Verify folders not in repository widgets")
         
        """
        Step 14: Click on Page Heading.
        Verify Page Heading Style appears as below:
        """
        page_heading = util_obj.validate_and_get_webdriver_object(".pd-page-title", "page_title")
        core_util_obj.left_click(page_heading)
        heading_styles_obj = util_obj.validate_and_get_webdriver_objects(".pd-heading-style-btn", "heading styles")
        observed_heading_styles = [element.text for element in heading_styles_obj]
        util_obj.as_List_equal(observed_heading_styles, expected_heading_styles, "Step 14.1: Verify the heading styles")
         
        """
        Step 15: Click on Theme drop down and choose Light
        Verify styling has been applied as below
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Light')
        actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page", "page_tab"), 'background').strip().replace(' ','')
        for index_, item in enumerate(["rgb(255,255,255)"], 1):
            util_obj.asin(item, actual_color, "Step 15.{0}: Verify whether background has Light theme".format(index_))
         
        """
        Step 16: Click on Theme drop down and choose Midnight
        """
        page_designer_obj.select_property_tab_style_option('Page Style', 'drop_down', 'Theme', 'Midnight')
        actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page", "page_tab"), 'background').strip().replace(' ','')
        for index_, item in enumerate(midnight_blue_list, 1):
            util_obj.asin(item, actual_color, "Step 16.{0}: Verify whether background has Midnight theme".format(index_))
             
        """
        Step 17: Choose 'Heading 1' from under Page Heading Style
        Verify styling has been applied as below
        """
        heading_one = util_obj.validate_and_get_webdriver_object("div[data-ibxp-user-value=\"pd-style-heading1\"]", "heading one")
        core_util_obj.left_click(heading_one)
        observed_font_size = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(page_title_css, "page_tab"), 'font-size')
        util_obj.asequal('48px', observed_font_size, "Step 17: Verify the heading 1 has been applied")
         
        """
        Step 18: Choose 'Heading 5' from under Page Heading Style
        Verify styling has been applied as below
        """
        heading_five = util_obj.validate_and_get_webdriver_object("div[data-ibxp-user-value=\"pd-style-heading5\"]", "heading five")
        core_util_obj.left_click(heading_five)
        observed_font_size = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(page_title_css, "page_tab"), 'font-size')
        util_obj.asequal('16px', observed_font_size, "Step 18: Verify the heading 5 has been applied")
         
        """
        Step 19: Change Heading Style to Title    
        Verify styling has been applied as below
        """
        title_obj = util_obj.validate_and_get_webdriver_object("div[data-ibxp-user-value=\"pd-style-title\"]", "title")
        core_util_obj.left_click(title_obj)
        observed_font_weight = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(page_title_css, "page_tab"), 'font-weight')
        util_obj.asequal('700', observed_font_weight, "Step 19: Verify the title has been applied")
         
        """
        Step 20: Change Heading Style to Subtitle
        Verify styling has been applied as below
        """
        subtitle_obj = util_obj.validate_and_get_webdriver_object("div[data-ibxp-user-value=\"pd-style-subtitle\"]", "subtitle")
        core_util_obj.left_click(subtitle_obj)
        observed_font_size = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(page_title_css, "page_tab"), 'font-size')
        util_obj.asequal('12px', observed_font_size, "Step 20: Verify the subtitle has been applied")
         
        """
        Step 21: Click Save;
        Enter 'Page Testing Style' and click on save button
        """
        page_designer_obj.save_page_from_toolbar('Page Testing Style')
         
        """
        Step 22: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 23: Right click on 'Page Testing Style' and select Run in New Window
        Verify page appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu('Page Testing Style', 'Run')
        core_util_obj.switch_to_frame(".ibx-iframe-frame")
        page_designer_obj.switch_to_container_frame('Panel 1')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_crumb_box('Workspaces->V5 Domain Testing->v5portal1', "Step 23.1: Verify the crumb box")
        main_page_obj.verify_items_in_grid_view(['Page Testing Style'], 'asin', "Step 23.2: Verify item is present")
        core_util_obj.switch_to_default_content()
        core_util_obj.switch_to_frame(".ibx-iframe-frame")
        observed_font_size = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(page_title_css, "page_tab"), 'font-size')
        util_obj.asequal('12px', observed_font_size, "Step 23.3: Verify the subtitle has been applied")
        actual_color = util_obj.get_element_css_propery(util_obj.validate_and_get_webdriver_object(".pd-page", "page_tab"), 'background').strip().replace(' ','')
        for index_, item in enumerate(midnight_blue_list, 4):
            util_obj.asin(item, actual_color, "Step 23.{0}: Verify whether background has Midnight theme".format(index_))
        core_util_obj.switch_to_default_content()
        close_button = util_obj.validate_and_get_webdriver_object("div[title='Close']", 'closebutton')
        core_util_obj.left_click(close_button)
        
        """
        Step 24: Right click on 'Page Testing Style' and select Publish
        """
        main_page_obj.right_click_folder_item_and_select_menu('Page Testing Style', 'Publish')
        
        """
        Step 25: Sign Out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()