'''
Created on April 1,2019

@author: Niranjan
Testcase Name : V5 Alias issues: Alias is still being used after the entry was cleared
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261731
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.locators import wf_mainpage_locators
from common.wftools import designer_portal

class C8261731_TestClass(BaseTestCase):
    
    def test_C8261731(self):
        
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        loc_obj = wf_mainpage_locators.WfMainPageLocators()
        design_por_obj = designer_portal.Portal(self.driver)
        portal_banner_obj = designer_portal.Banner(self.driver)
        portal_canvas_obj = designer_portal.Canvas(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        user_name_css = "div[class*='pvd-menu-admin']"
        url_css = '.pvd-url'
        page_canvas_css = '#pagespane'
        
        """
        Test case variables
        """
        expected_domain = "P292_S19901"
        expected_folder = 'G520448'
        portal = 'v5-alias'
        url = "portal/P292_S19901/G520448/v5-alias"
        url_with_alias = 'portal/testalias'
        expected_user_name = 'autodevuser88'
        
        """
        Step 1: Login WF as developer
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
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal tile in action bar    
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Portal',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 4: Enter title as 'v5-alias' in create portal dialog
        Verify URL : http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias
        """
        design_por_obj.title_textbox_in_new_or_edit_portal_dialog(portal)
        design_por_obj.url_textbox_in_new_or_edit_portal_dialog(url, step_number='4.1')
        
        """
        Step 5: Enter alias 'testalias'
        Verify URL: http://machine_name:port/alias/portal/testalias
        """
        design_por_obj.alias_textbox_in_new_or_edit_portal_dialog('testalias')
        util_obj.synchronize_until_element_is_visible(url_css, main_page_obj.home_page_short_timesleep)
        design_por_obj.url_textbox_in_new_or_edit_portal_dialog(url_with_alias, step_number='5.1')
        
        """
        Step 6: Click Create
        """
        design_por_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 7: Right click on 'v5-alias' and select Run
        Verify URL: http://machine_name:port/alias/portal/testalias
        Verify portal appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_long_timesleep)
        util_obj.verify_current_url(url_with_alias, 'Step 7.1: Verify URL: http://machine_name:port/alias/portal/testalias')
        portal_banner_obj.verify_portal_top_banner_title(portal, 'Step 7.2: Verify portal banner title')
        portal_canvas_obj.verify_blank_canvas_text('Step 7.3: Verify canvas text')
        util_obj.verify_element_text(user_name_css, expected_user_name, 'Step 7.4: Verify login user name')
        util_obj.verify_picture_using_sikuli('info_build_logo.png', 'Step 7.5: Verify informating builder logo')
        util_obj.verify_picture_using_sikuli('user_icon.png', 'Step 7.6: Verify login icon')
        
        """
        Step 8: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 9: Right click on 'v5-alias' and select Edit
        """
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(portal, 'Edit')
        
        """
        Step 10: Remove alias
        Verify URL : http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias
        """
        design_por_obj.alias_textbox_in_new_or_edit_portal_dialog('')
        util_obj.synchronize_until_element_is_visible(url_css, main_page_obj.home_page_short_timesleep)
        design_por_obj.url_textbox_in_new_or_edit_portal_dialog(url, step_number='10.1')
        
        """
        Step 11: Click save
        """
        design_por_obj.save_button_inside_new_or_edit_portal_dialog(select_button=True)   
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
           
        """
        Step 12: Right click on 'v5-alias' and select Run
        Verify URL : http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias
        Verify portal appears as below
        """  
        main_page_obj.right_click_folder_item_and_select_menu(portal, 'Run')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(page_canvas_css, main_page_obj.home_page_long_timesleep)
        util_obj.verify_current_url(url, 'Step 12.1: Verify URL: http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias')
        portal_banner_obj.verify_portal_top_banner_title(portal, 'Step 12.2: Verify portal banner title')
        portal_canvas_obj.verify_blank_canvas_text('Step 12.3: Verify canvas text')
        util_obj.verify_element_text(user_name_css, expected_user_name, 'Step 12.4: Verify login user name')
        util_obj.verify_picture_using_sikuli('info_build_logo.png', 'Step 12.5: Verify informating builder logo')
        util_obj.verify_picture_using_sikuli('user_icon.png', 'Step 12.6: Verify login icon')
        
        """
        Step 13: Close portal
        """
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 14: Signout WF
        """
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer',main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()