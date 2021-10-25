'''
Created on March 29, 2019

@author: varun
Testcase Name : IE11: Signing out of V5 portal - URL points to some /{soft-context}/workbench
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261732
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility
from common.wftools import designer_portal
from common.wftools import page_designer

class C8261732_TestClass(BaseTestCase):
    
    def test_C8261732(self):
        """
        Test case objects
        """
        page_designer_obj = page_designer.Design(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path=folder_name+'->'+group_id
        portal_name = 'v5-explorer'
        left_panel_items = ['Content', 'Portals', 'Favorites', 'Ask WebFOCUS']
        home_page_title = 'Home Page'
        
        """
        Test case CSS
        """
        page_heading_title = ".pd-page-title .ibx-label-text"
        domains_css = "div[title=\"Domains\"] .ibx-label-text"
        portal_dialog_css = ".create-pvd-dialog .ibx-title-bar-caption .ibx-label-text"
        new_page_template = ".ibx-dialog-title-box .ibx-title-bar-caption .ibx-label-text"
        frame_css = "[class$='iframe-frame']"
        
        """
        Step 1: Login WF as developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
         
        """
        Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
         
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal tile in action bar
        """
        util_obj.synchronize_with_visble_text(domains_css, 'Domains', main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep )
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'New Portal', main_page_obj.home_page_short_timesleep )
          
        """
        Step 4: Enter title as 'v5-explorer' in create portal dialog and click Create
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_name)
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
           
        """
        Step 5: Click on 'v5-explorer' and select Page tile in action bar
        """
        main_page_obj.expand_repository_folder(portal_name)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(new_page_template, 'New Page', main_page_obj.home_page_medium_timesleep)
          
        """
        Step 6: Choose blank template
        """
        page_designer_obj.select_page_designer_template('Blank')
        util_obj.synchronize_with_visble_text(page_heading_title, 'Page Heading', main_page_obj.home_page_medium_timesleep)
          
        """
        Step 7: Click on Repository widgets from under Content tab
        """
        page_designer_obj.expand_and_collapse_repository_widgets_tab('expand')
          
        """
        Step 8: Drag and drop Explorer to the canvas
        Verify explorer in page canvas shows the current domain->portal we are in the content tree, content area and the breadcrumb shows 
        Domains > P292_S19901 > G520448 as below
        """
        page_designer_obj.drag_repository_widgets_item_to_blank_canvas('Explorer', 1)
        core_util_obj.switch_to_frame(frame_css=frame_css)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_crumb_box('Domains->P292_S19901->G520448->v5-explorer', 'Step 8: Verify the Crumb box')
        core_util_obj.switch_to_default_content()
          
        """
        Step 9: Save page as 'epage1'
        """
        page_designer_obj.save_page_from_toolbar('epage1')
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.ACTION_BAR_CSS, 1, main_page_obj.home_page_medium_timesleep)
          
        """
        Step 10: Right click on 'v5-explorer' and select Publish
        """
        main_page_obj.select_repository_folder_context_menu(portal_name, 'Publish')
          
        """
        Step 11: Right click on 'v5-explorer' and select Run
        Verify portal runs with explorer that shows the current domain->portal we are in the content tree, content area and the breadcrumb shows 
        Domains > P292_S19901 > G520448 as below
        """
        main_page_obj.select_repository_folder_context_menu(portal_name, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_heading_title, 'Page Heading', main_page_obj.home_page_medium_timesleep)
        core_util_obj.switch_to_frame(frame_css=frame_css)
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_crumb_box('Domains->P292_S19901->G520448->v5-explorer', 'Step 8: Verify the Crumb box')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'epage1', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_items_in_grid_view(['epage1'], 'asin', 'Step 8.1: Verify epage is present in the content area')
        main_page_obj.verify_content_area_item_publish_or_unpublish('epage1', 'publish', 'Step 8.2: Verify the epage item is published')
        core_util_obj.switch_to_default_content()
         
        """
        Step 12: Close portal
        Verify user is in Home page
        """
        core_util_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'epage1', main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_left_panel(left_panel_items, 'Step 12: Verify the left panel')
        observed_title = self.driver.title
        util_obj.asin(home_page_title, observed_title, 'Step 12.1: Verify the home page title')
         
        """
        Step 13: Sign out WF
        You should now be on the Home page tab.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        """
        Step 14: Login WF as administrator
        Verify user is in Home page
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        main_page_obj.select_content_from_sidebar()
        main_page_obj.verify_left_panel(left_panel_items, 'Step 14: Verify the left panel')
        observed_title = self.driver.title
        util_obj.asin(home_page_title, observed_title, 'Step 14.1: Verify the home page title')

        """
        Step 15: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()       
        
        