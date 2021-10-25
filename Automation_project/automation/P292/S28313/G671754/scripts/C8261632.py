'''
Created on April 5th, 2019

@author: vpriya
Testcase Name : Create Portal
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261632
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.wftools import designer_portal
from common.locators import wf_mainpage_locators
from common.lib import utillity


class C8261632_TestClass(BaseTestCase):
    
    def test_C8261632(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        designer_obj = designer_portal.Portal(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        dialog_css = ".ibx-dialog-content"
        
        """
        Step 1: Login WF as developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content view from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand 'P292_S19901' domain-> Click on 'G671753' folder;
        Select Designer tag and click on Portal..
        """
        main_page_obj.expand_repository_folder("P292_S19901->G671753")
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'Designer',base_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_number_of_element(dialog_css,1, base_obj.home_page_medium_timesleep)
        
        """
        Step 4: Enter title as 'v5portal1dev'' 
        Verify Name field gets automatically filled up as 'v5portal1dev'
        """
        designer_obj.title_textbox_in_new_or_edit_portal_dialog('v5portal1dev')
        designer_obj.name_textbox_in_new_or_edit_portal_dialog(verify_value='v5portal1dev',step_number='4.1')
        
        """
        Step 5: Click on 'Create My Pages menu' check box
        """
        
        designer_obj.create_my_pages_menu_checkbox_inside_new_or_edit_portal_dialog(select_checkbox='check',step_number='step 5.1')
        
        """
        Step 6: Click Create
        """
        designer_obj.create_button_inside_new_or_edit_portal_dialog(select_button='True')
        
        """
        Step 7:Right click on 'v5portal1dev' and click on Publish
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'v5portal1dev',base_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('v5portal1dev','Publish')
        
        """
        Verify portal in content area appears as below
        """
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'v5portal1dev',base_obj.home_page_medium_timesleep)
        main_page_obj.verify_content_area_folder_publish_or_unpublish(folder_name='v5portal1dev', folder_status='publish', msg='Step 7.1 verify the portal in content area')
        main_page_obj.verify_folder_icon_in_content_area(folder_name='v5portal1dev', icon_type='portal', step_number='7.2', verify_color_name='bar_blue')
        
        """
        Step 8:Signout WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()