'''
Created on October 31, 2018

@author: Vpriya
Testcase Name : Edit portal without my pages and alias
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779491
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage, designer_portal
from common.lib import utillity,core_utility

class C6779493_TestClass(BaseTestCase):
    
    def test_C6779493(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        Crumb_css=".crumb-box"
        Long_wait=90
        medium_wait=40
        folder_css=".content-title-label"
        folder_name_path="P292_S19901->G520448"
        portals_css = "div[title=\"Portals\"] .ibx-label-text"
        expected_title = "v5-alias-test2"
        content_area_text = "There are no pages available"
        content_area_css = ".files-no-search-results .ibx-label-text"
        user_css = ".pvd-menu-admin .ibx-label-text"
        user_name_parsed = core_util_obj.parseinitfile('mriddev')
        pop_top_css=".pop-top [data-ibx-name='vbMain'] [data-ibxp-text='Banner']"

        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(Crumb_css, '1', Long_wait)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_option_from_crumb_box("Domains")
        util_obj.synchronize_with_number_of_element(folder_css, '1', medium_wait)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(Crumb_css, '1', medium_wait)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Right click on 'v5-alias-test2' portal and select Edit
        Edit portal dialog appears;
        Verify below.
        Title and name appears as 'v5-alias-test2';
        Alias is not empty, shows 'abc123ABC+_)*&^%$#@!'
        Banner switch is on;
        Show portal title in banner box is checked;
        Logo stays Not selected;
        Two-level navigation is selected;
        Theme should be 'Midnight';
        URL: http://machinename:port/alias/portal/abc123ABC_@!
        Save button is highlighted and disabled by default;
        Cancel button is enabled.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        main_page_obj.right_click_folder_item_and_select_menu('v5-alias-test2','Edit')
        util_obj.synchronize_with_number_of_element(pop_top_css, '1', medium_wait)
        designer_portal_obj.verify_portal_dialog('Edit Portal','label_text', 'Edit Portal','Step 4: verify edit label')
        designer_portal_obj.verify_portal_dialog('Title', 'text_box', 'v5-alias-test2', 'Step 4.1: verify title label')
        designer_portal_obj.verify_portal_dialog('Name', 'text_box', 'v5-alias-test2', 'Step 4.2: verify Name label')
        designer_portal_obj.verify_portal_dialog('Alias', 'text_box', 'abc123ABC_%@!', 'Step 4.3: verify Alias label')
        designer_portal_obj.verify_portal_dialog('Banner', 'toggle_button', 'check', 'Step 4.3: verify Banner toggle button')
        designer_portal_obj.verify_portal_dialog('Show portal title', 'checkbox', 'check', 'Step 4.4: verify Show portal title')
        designer_portal_obj.verify_portal_dialog('Logo', 'text_box', '', 'Step 4.5: Logo Verification',placeholder='Not Selected')
        designer_portal_obj.verify_portal_dialog('Navigation', 'radio_button','check', 'Step 4.6: Navigation Verification')
        designer_portal_obj.verify_portal_dialog('Theme', 'drop_down', 'Midnight','Step 4.7: verify Theme drop_down')
        designer_portal_obj.verify_portal_dialog('URL','text_box','portal/P292_S19901/G520448/abc123ABC_%@!','Step 4.8 verify url')
        designer_portal_obj.verify_portal_dialog_content_enable_disable('Save', 'button', 'disable', 'Step 4.9. Verify Save button disabled')
        designer_portal_obj.verify_portal_dialog_content_enable_disable('Cancel', 'button', 'enable', 'Step 4.10. Verify cancel button is enable')
        
        
        """
        Step 4.Remove Alias
        Verify URL: http://machine_name:port/alias/portal/P292_S19901/G520448/v5-alias-test2
        """
        designer_portal_obj.create_or_edit_portal('Alias','text_box','')
        designer_portal_obj.verify_portal_dialog('URL','text_box','portal/P292_S19901/G520448/v5-alias-test2','Step 4.1 verify url updated with alias')
        
        """
        Step 5. Click on X to close.
        Edit portal dialog closes.
        """
        designer_portal_obj.close_portal_dialog('Cancel')
        util_obj.synchronize_with_number_of_element(folder_css, '1', medium_wait)
        designer_portal_obj.verify_portal_dialog_open_or_close("close","Step 4:Verify dialog node is close")
        
        """Step 6:Right click on 'v5-alias-test2' portal from content tree and select Run.
        """
    
        main_page_obj.right_click_folder_item_and_select_menu('v5-alias-test2', 'Run')
        util_obj.synchronize_with_visble_text(portals_css, 'Portals',30)
        core_util_obj.switch_to_new_window()
        util_obj.verify_current_url('portal/P292_S19901/G520448/v5-alias-test2', 'Step 9.1: URL verification in new window')
        title_css = ".pvd-portal-title .ibx-label-text"
        title_name = util_obj.validate_and_get_webdriver_object(title_css, 'title-css').text.strip()
        util_obj.asequal(title_name,expected_title,"Step 9.2: Title verification")
        content_area_text_search = util_obj.validate_and_get_webdriver_object(content_area_css, 'content-text-css').text.strip()
        util_obj.asequal(content_area_text,content_area_text_search,"Step 9.4: Content area text verification")
        user_name = util_obj.validate_and_get_webdriver_object(user_css, 'username-text-css').text.strip()
        util_obj.asequal(user_name_parsed,user_name,"Step 9.5: Username text verification")
        util_obj.verify_picture_using_sikuli("info_build_logo.png","Step 9.5: Verify the Infobuilders icon logo")
        core_util_obj.switch_to_previous_window()
        
        
        """
        Step 7: Close portal.
        """
        designer_portal_obj.close_portal_dialog('Close')
        
        """
        Step 8: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()