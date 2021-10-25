'''
Created on April 01, 2019

@author: AA14564
Testcase Name : V5:Two Top level does not show all pages under a menu
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8261734
'''

import unittest
import time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib import core_utility
from common.wftools import designer_portal
from common.wftools import page_designer
from common.lib.webfocus.resource_dialog import Resource_Dialog
from common.pages.page_designer_miscelaneous import PageDesignerMiscelaneous as pd_miscelaneous


class C8261734_TestClass(BaseTestCase):
    
    def test_C8261734(self):
        """
        Test case objects
        """
        page_designer_obj = page_designer.Design(self.driver)
        portal_obj = designer_portal.Portal(self.driver)
        portal_banner_obj = designer_portal.Banner(self.driver)
        portal_canvas_obj = designer_portal.Canvas(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        res_dialog_obj = Resource_Dialog(self.driver)
        pd_miscelaneous_obj = pd_miscelaneous(self.driver)
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id= core_util_obj.parseinitfile('group_id')
        folder_name=project_id+'_'+suite_id
        folder_name_path='Domains->'+folder_name+'->'+group_id
        portal_name = 'v5-Twotop'
        
        """
        Test case CSS
        """
        run_page_canvas_css = ".pvd-canvas-area"
        page_canvas_css = "[class*='pd-page-canvas']"
        portal_dialog_css = ".pop-top"
        run_page_folder_css = ".pvd-close-run-left-panel"
        
        '''
        local function
        '''
        def select_page(page_name):
            '''
            Des: This function will select page from run page
            '''
            total_page_obj = util_obj.validate_and_get_webdriver_objects(run_page_folder_css, page_name)
            page_obj = [page for page in total_page_obj if page.is_displayed() and page.text.strip()==page_name][0]
            try:
                core_util_obj.left_click(page_obj)
            except IndexError:
                raise LookupError("{name} page name not found in portal".format(name=page_name)) 
                
        
        """
        Step 1: Login WF as developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(WfMainPageLocators.REPOSITORY_TREE_CSS, main_page_obj.home_page_long_timesleep)
        
        """ Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
                    Select Designer tag and click on Portal tile in action bar
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep )
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Portal', main_page_obj.home_page_medium_timesleep )
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'Title', main_page_obj.home_page_short_timesleep )
         
        """ Step 4: Enter title as 'v5-Twotop' in create portal dialog;
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(edit_value=portal_name)
         
        """ Step 5: Choose 'Two-level top' navigation
        """
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
         
        """ Step 6: Click Create
        """
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
         
        """ Step 7: Click on 'v5-Twotop' in tree and select Folder tile in action bar;
                    Enter title as 'Folder1' and click ok
        """
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, portal_name, main_page_obj.home_page_short_timesleep)
        main_page_obj.expand_repository_folder(portal_name)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Folder', main_page_obj.home_page_short_timesleep)
        main_page_obj.select_action_bar_tabs_option('Folder')
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'Title', main_page_obj.home_page_short_timesleep)
        main_page_obj.enter_new_folder_title_in_popup_dialog('Folder1')
        main_page_obj.click_button_on_popup_dialog('OK')
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Folder1', main_page_obj.home_page_short_timesleep)
         
        """ Step 8: Click on 'v5-Twotop' in tree and select Page tile in action bar
        """
        main_page_obj.expand_repository_folder(portal_name)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Page', main_page_obj.home_page_short_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
         
        """ Step 9: Choose Grid 2-1 template and save page as 'Base Page1'
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_dialog_css, 'Grid 2-1', main_page_obj.home_page_long_timesleep)
        page_designer_obj.select_page_designer_template('Grid 2-1')
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_medium_timesleep)
        page_designer_obj.save_as_page_from_application_menu('Base Page1')
         
        """ Step 10: Click on main menu -> Save as;
                    Enter title as 'FPage1' and save it under P292_S19901-> G520448-> v5-Twotop-> Folder1
        """
        
        pd_miscelaneous_obj.select_page_designer_application_menu('Save as...')
        resource_item_css='{0} #files-box-area'.format(res_dialog_obj.resource_dialog_css)
        util_obj.synchronize_with_visble_text(resource_item_css, 'Folder1', main_page_obj.home_page_long_timesleep)
        res_dialog_obj.select_resource_from_gridview('Folder1', selection_type='double')
        time.sleep(3)
        pd_miscelaneous_obj.page_designer_open_dialog_resources(title='FPage1', ok_button=True)
         
        """ Step 11: Click on main menu -> Save as;
                     Enter title as 'FPage2' and click save as button
        """
        page_designer_obj.save_as_page_from_application_menu('FPage2')
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_medium_timesleep)
         
        """ Step 12: Close designer
        """
        page_designer_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Folder1', main_page_obj.home_page_long_timesleep)
        
        """ Step 13: Right click on 'v5-Twotop' in tree and select Run
                     Verify portal appears as below
        """
        main_page_obj.select_repository_folder_context_menu(portal_name, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(run_page_canvas_css, 'Base Page1', main_page_obj.home_page_long_timesleep)
        portal_banner_obj.verify_portal_top_banner_title('v5-Twotop', 'Step 13: Verify portal banner title.')
        portal_canvas_obj.verify_page_header_title('Page Heading', "Step 13.1: Verify 'Base Page1' page header.")
        portal_canvas_obj.verify_page_header_all_buttons(['Refresh'], "Step 13.2: Verify 'Base Page1' page refresh button.")
        portal_canvas_obj.verify_all_containers_title(['Panel 1', 'Panel 2', 'Panel 3'], "Step 13.3: Verify 'Base Page1' page panels.")
        
        """ Step 14: Click on 'Folder1'
                     Verify FPage1 and FPage2 are available and appears as below
        """
        select_page('Folder1')
        util_obj.synchronize_with_visble_text(run_page_canvas_css, 'FPage1', main_page_obj.home_page_long_timesleep)
        portal_canvas_obj.verify_page_header_title('Page Heading', "Step 14.1: Verify 'Base Page1' page header.")
        portal_canvas_obj.verify_page_header_all_buttons(['Refresh'], "Step 14.2: Verify folder 'Folder1' page 'FPage1' refresh button.")
        portal_canvas_obj.verify_all_containers_title(['Panel 1', 'Panel 2', 'Panel 3'], "Step 14.3: Verify folder 'Folder1' page 'FPage1' panels.")
        select_page('FPage2')
        portal_canvas_obj.verify_page_header_title('Page Heading', "Step 14.4: Verify 'Base Page1' page header.")
        portal_canvas_obj.verify_page_header_all_buttons(['Refresh'], "Step 14.5: Verify folder 'Folder1' page 'FPage1' refresh button.")
        portal_canvas_obj.verify_all_containers_title(['Panel 1', 'Panel 2', 'Panel 3'], "Step 14.6: Verify folder 'Folder1' page 'FPage1' panels.")
        
        """ Step 15: Close portal
        """
        core_util_obj.switch_to_previous_window(window_close=False)
        util_obj.synchronize_with_visble_text(WfMainPageLocators.content_area_css, 'Folder1', main_page_obj.home_page_long_timesleep)
        
        """ Step 16: Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()