'''
Created on Nov 2, 2018

@author: Vpriya
Testcase Name : Edit portal without my pages and alias
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779492
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage, designer_portal
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C6779492_TestClass(BaseTestCase):
    
    def test_C6779492(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        portals_css = "div[title=\"Portals\"] .ibx-label-text"
        folder_css=".content-title-label"
        folder_name_path="P292_S19901->G520448"
        edit_portal_css = ".ibx-title-bar-caption .ibx-label-text"
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        expected_list=['v5-alias-test2']
        expected_context_menu_item_list=['unpublish']
        expected_title = "v5-alias-test2"
        content_area_text = "There are no pages available"
        content_area_css = ".files-no-search-results .ibx-label-text"
        user_css = ".pvd-menu-admin .ibx-label-text"
        user_name_parsed = core_util_obj.parseinitfile('mriddev')
        
        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
        Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Select Designer tag and click on Portal tile in action bar..
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', Global_variables.mediumwait)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """
        Step 4: Enter title as 'v5-alias-test2';
        Name input box is filled automatically as 'v5-alias-test2'
 
        """
        util_obj.synchronize_with_visble_text(edit_portal_css, 'New Portal', Global_variables.mediumwait)
        designer_portal_obj.title_textbox_in_new_or_edit_portal_dialog('v5-alias-test2')
        designer_portal_obj.name_textbox_in_new_or_edit_portal_dialog(None,verify_value='v5-alias-test2',current_mode='enable', label_text='Name',focused=None,step_number='step :4.2 Name verification')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog('portal/P292_S19901/G520448/v5-alias-test2',step_number='4.3')
        
        """
        Step 5. Click on Theme dropdown;
        Select 'Midnight' theme
        """
        designer_portal_obj.theme_dropdown_in_new_or_edit_portal_dialog('Midnight', step_number='5')
        
        """
        Step 6 Enter the alias as '123'
        """
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(edit_value='123')
        
        """
        Step 7: Click Create.
        Verify Warning message appears as below.
        """
        designer_portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        designer_portal_obj.verify_alert_message_in_portal_dialog("Alias already exists", "7.1","persian_red4")
        
        """
        Step 8: Enter alias as 'abc123ABC+_)*&^%$#@!'
        """
        designer_portal_obj.alias_textbox_in_new_or_edit_portal_dialog(edit_value='abc123ABC+_)*&^%$#@!')
        designer_portal_obj.url_textbox_in_new_or_edit_portal_dialog('portal/abc123ABC_@!',step_number='8.1')
        
        """
        Step 9: Click Create
        Verify 'Create Portal' dialog is closed;
        v5-alias-test2' portal folder is created under P292_S19901 domain > G520448 folder in content tree;
        Portal is unpublished, title appears in Italic in content tree;
        verify portal icon in content area.
        """ 
        designer_portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        designer_portal_obj.verify_portal_dialog_open_or_close("close","Step 9.1:Verify dialog node is close")
        main_page_obj.verify_items_in_grid_view(expected_list, 'asin',"Step 9.2 verify folder is under the content tree" )
        main_page_obj.verify_repository_folder_publish_or_unpublish('v5-alias-test2', 'unpublish', "Step 9.3")
        main_page_obj.verify_repository_folder_font_style('v5-alias-test2', 'italic','Step 9.4 verify font style')
        main_page_obj.verify_item_icon_in_content_area('v5-alias-test2', 'portal', "Step 9.5 item icon verification")
        
        """
        Step 10: Right click on v5-alias-test2'' portal from content area and select Publish.
        """
        main_page_obj.right_click_folder_item_and_select_menu('v5-alias-test2', 'Publish')
        main_page_obj.verify_item_icon_in_content_area('v5-alias-test2', 'portal', "Step 10 item icon in blue colour", 'blue')
        
        """
        Step 11: Right click on v5-alias-test2'' portal from content area
        Verify Publish menu no longer appears only Unpublish menu appears.
        """
        main_page_obj.verify_repository_folder_context_menu('v5-alias-test2', expected_context_menu_item_list,'11')
        
        """
        Step 12: Right click on 'v5-alias-test2' portal from content area and select Run.
        Verify URL: http://machine_name:port/alias/portal/abc123ABC_%25@!
        Verify portal run mode appears as below
        """
        main_page_obj.right_click_folder_item_and_select_menu('v5-alias-test2','Run')
        util_obj.synchronize_with_visble_text(portals_css, 'Portals',30)
        core_util_obj.switch_to_new_window()
        util_obj.verify_current_url('portal/P292_S19901/G520448/v5-navigation-test3', 'Step 9.1: URL verification in new window')
        title_css = ".pvd-portal-title .ibx-label-text"
        title_name = util_obj.validate_and_get_webdriver_object(title_css, 'title-css').text.strip()
        util_obj.asequal(title_name,expected_title,"Step 9.2: Title verification")
        content_area_text_search = util_obj.validate_and_get_webdriver_object(content_area_css, 'content-text-css').text.strip()
        util_obj.asequal(content_area_text,content_area_text_search,"Step 9.4: Content area text verification")
        user_name = util_obj.validate_and_get_webdriver_object(user_css, 'username-text-css').text.strip()
        util_obj.asequal(user_name_parsed,user_name,"Step 9.5: Username text verification")
        util_obj.verify_picture_using_sikuli("info_build_logo.png","Step 9.5: Verify the Infobuilders icon logo")
        
        """
        Step 13: Close portal.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 14: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()


if __name__ == '__main__':
    unittest.main()
    
        