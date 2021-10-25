'''
Created on December 26, 2018

@author: varun
Testcase Name : Adding base pages in V5 Portal
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262146
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools import page_designer

class C8262146_TestClass(BaseTestCase):
    
    def test_C8262146(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        page_designer_obj = page_designer.Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        action_bar_css = "[data-ibxp-text=\"Action Bar\"] .ibx-label-text"
        page_template_css = ".ibx-title-bar-caption .ibx-label-text"
        page_heading_css = ".pd-page-title .ibx-label-text"
        panel_css = ".ibxtool-panel-basic-containers div[data-ibxp-conttype=\"panel\"]"
        toggle_lock_css = ".pd-ps-es-lock-content .ibx-switch-ctrl .round"
        add_button_css = ".cont-es-button .fa-plus-circle"
        
        """
        Test case variables
        """
        new_page_text = 'New Page'
        page_heading_text = 'Page Heading'
        action_bar_text = 'Action Bar'
        portal_name = 'V5 Personal Portal_Nav-2'
        project = core_util_obj.parseinitfile('project_id')
        group = core_util_obj.parseinitfile('group_id')
        suite = core_util_obj.parseinitfile('suite_id')
        expand_respository = '{0}_{1}->{2}->{3}'.format(project,suite,group,portal_name)
        base_page_list = ['Base Page 1','Base Page 2', 'Base Page 3']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S19901' domain > G514402 folder > click on V5 Personal Portal_Nav-2.
        """
        main_page_obj.expand_repository_folder(expand_respository)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_short_timesleep)
        
        """
        Step 3: Click on page action bar > Choose blank template.
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_template_css,new_page_text,base_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_visble_text(page_heading_css,page_heading_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Containers tab > drag and drop Panel container on the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        util_obj.synchronize_with_number_of_element(panel_css, 1, base_obj.home_page_short_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas('Panel',1)
        
        """
        Step 5: From the designer toolbar, click on Properties > toggle off lock content.
        Verify Panel 1 have a + sign inside
        """
        page_designer_obj.click_property()
        util_obj.synchronize_with_number_of_element(toggle_lock_css, 1, base_obj.home_page_short_timesleep)
        lock_button = util_obj.validate_and_get_webdriver_object(toggle_lock_css, "lock_css")
        core_util_obj.python_left_click(lock_button)
        util_obj.synchronize_with_number_of_element(add_button_css, 1, base_obj.home_page_short_timesleep)
        page_designer_obj.verify_panel_add_content_displayed_in_container('Panel 1', "Step 5.1: Verify Panel 1 has a '+' Sign")
        
        """
        Step 6: Click on Save button > enter title as 'Base Page 1' > click save and Click on application menu > Close.
        """
        page_designer_obj.save_page_from_toolbar('Base Page 1')
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_short_timesleep)
        
        """
        Step 7: Click on page action bar > Choose blank template.
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_template_css,new_page_text,base_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_visble_text(page_heading_css,page_heading_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 8: Click on Containers tab > drag and drop tab container on the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        util_obj.synchronize_with_number_of_element(panel_css, 1, base_obj.home_page_short_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas('Tab',1)
        
        """
        Step 9: From the designer toolbar, click on Properties > toggle off lock content.
        Verify Panel 1 have a + sign inside
        """
        page_designer_obj.click_property()
        util_obj.synchronize_with_number_of_element(toggle_lock_css, 1, base_obj.home_page_short_timesleep)
        lock_button = util_obj.validate_and_get_webdriver_object(toggle_lock_css, "lock_css")
        core_util_obj.python_left_click(lock_button)
        util_obj.synchronize_with_number_of_element(add_button_css, 1, base_obj.home_page_short_timesleep)
        page_designer_obj.verify_tab_panel_add_content_displayed_in_container('Panel 1', "Step 9.1: Verify tab 1 has a '+' Sign" )
        
        """
        Step 10: Click on Save button > enter title as 'Base Page 2' > click save and Click on application menu > Close.
        """
        page_designer_obj.save_page_from_toolbar('Base Page 2')
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_short_timesleep)
        
        """
        Step 11: Click on page action bar > Choose blank template. 
        """
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_template_css,new_page_text,base_obj.home_page_medium_timesleep)
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_visble_text(page_heading_css,page_heading_text, base_obj.home_page_medium_timesleep)
        
        """
        Step 12: Click on Containers tab > drag and drop Carousel container on the page canvas.
        """
        page_designer_obj.select_option_from_carousel_items('Containers')
        util_obj.synchronize_with_number_of_element(panel_css, 1, base_obj.home_page_short_timesleep)
        page_designer_obj.drag_container_item_to_blank_canvas('Carousel',1)
        
        """
        Step 13: From the designer toolbar, click on Properties > toggle off lock content.
        Verify Panel 1 have a + sign inside
        """
        page_designer_obj.click_property()
        util_obj.synchronize_with_number_of_element(toggle_lock_css, 1, base_obj.home_page_short_timesleep)
        lock_button = util_obj.validate_and_get_webdriver_object(toggle_lock_css, "lock_css")
        core_util_obj.python_left_click(lock_button)
        util_obj.synchronize_with_number_of_element(add_button_css, 1, base_obj.home_page_short_timesleep)
        page_designer_obj.verify_carousel_panel_add_content_displayed_in_container('Panel 1', "Step 13.1: Verify Carousel has a '+' Sign")
        
        """
        Step 14: Click on Save button > enter title as 'Base Page 3' > click save and Click on application menu > Close.
        Verify Base Page1,2 and 3 are shown in the content area.
        """
        page_designer_obj.save_page_from_toolbar('Base Page 3')
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(action_bar_css, action_bar_text, base_obj.home_page_short_timesleep)
        main_page_obj.verify_items_in_grid_view(base_page_list,'asin' ,"Step 14.1: Verify all 3 pages in the context arean")
        
        """
        Step 15: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()