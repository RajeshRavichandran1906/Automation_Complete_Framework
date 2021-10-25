'''
Created on November 1, 2018

@author: Robert
Testcase Name : Create portal with Three level navigation
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6779499
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage,designer_portal
from common.pages import portal_designer
from common.lib import utillity

class C6779499_TestClass(BaseTestCase):
    
    def test_C6779499(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Portal(self.driver)
        portal_designer_obj=portal_designer.Portal_Designer(self.driver)
        folder_name_path="P292_S19901->G520448"
        expected_title="v5-navigation-test2"
        designer_css=".ibx-tab-button:nth-child(3) .ibx-label-text"
        edit_portal_css = ".ibx-title-bar-caption .ibx-label-text"
        menu_id_bar="div[class*='menu-admin ibx-widget']"
        
        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(menu_id_bar, 1, 60)
        
        """
        Step 2: Click on Content tree from side bar.
        """
        main_page_obj.select_option_from_crumb_box("Domains")
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3. Expand 'P292_S19901' domain-> Click on 'G520448' folder;
        Step 3.1. Select Designer tag and click on Portal tile in action bar.
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.synchronize_with_visble_text(designer_css, 'Designer', 30)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        
        """ 
        Step 4. Enter title as 'v5-navigation-test1'
        Step 4.1. Name input box is filled automatically as 'v5-navigation-test1'
        """
        util_obj.synchronize_with_visble_text(edit_portal_css, 'New Portal', 30)
        portal_designer_obj.create_or_edit_portal('Title', 'text_box', expected_title, navigation_type='Two-level-side', expire_time=90)
        portal_designer_obj.verify_portal_dialog('Name', 'text_box', expected_title, 'Step 4.1: Verify Name label automatically filled')

        """
        Step 5. Choose Two-level side navigation if not selected by default
        """
        #designer_portal_obj.verify_portal_dialog(label_name, property_type, property_value, msg, navigation_type, placeholder)   
        portal_designer_obj.create_or_edit_portal('Navigation', 'radio_button', 'check', navigation_type='Three-level') 

        """ 
        Step 6. Click Create
        Step 6.1. Verify 'New Portal' dialog is closed;
        Step 6.2. Portal title appears in Italic;
        Step 6.3. Portal is unpublished.
        """
        designer_portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button=True)
        util_obj.synchronize_until_element_disappear(".pop-top", 20)
        designer_portal_obj.verify_portal_dialog_open_or_close("close", "Step 6. Verify dialog closed")
        folder_name_list=['v5-navigation-test1']
        main_page_obj.expand_repository_folders_and_verify(folder_name_path, folder_name_list, 'Step 6.1: Verify repository folders')
        main_page_obj.verify_content_area_folder_publish_or_unpublish(expected_title, 'unpublish', 'Step 6.2: Verify folder published')
        main_page_obj.verify_repository_folder_font_style(expected_title, 'italic', 'Step 6.3: Verify font is italic in content tree')
        
        """
        Step 7: Signout WF.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        