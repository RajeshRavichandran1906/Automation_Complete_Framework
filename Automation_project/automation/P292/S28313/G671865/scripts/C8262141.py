'''
Created on Nov 26, 2018

@author: KK14897

Testcase Name : Delete a personal page
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8262120
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity, core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators


class C8262141_TestClass(BaseTestCase):
    
    def test_C8262141(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        portal_obj = designer_portal.Two_Level_Side(self.driver)
        portal_obj_2 = designer_portal.Three_Level(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        coreutil_obj = core_utility.CoreUtillityMethods(self.driver)
        domains_css = "div[title='Domains'] .ibx-label-text"
        portal_name ='V5 Personal Portal_Nav-2'
        pd_filter_window_css = ".pd-filter-window .ibx-dialog-main-box"
        project_id=coreutil_obj.parseinitfile('project_id')
        suite_id=coreutil_obj.parseinitfile('suite_id')
        group_id=coreutil_obj.parseinitfile('group_id')
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G514402 folder.
        """
        
        main_page_obj.expand_repository_folder('Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id))
        
        """
        Step 3: Right click on 'V5 Personal Portal_Nav-2' > Run. 
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run')
        
        """
        Step 4: Close filter modal window and click delete icon on the top of the page heading. 
                Verify delete warning dialog box displays.
        """
        coreutil_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_filter_window_css, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.click_button_on_popup_dialog("Close")
        portal_obj.delete_page()
        portal_obj.verify_page_delete_dialog_is_displayed("Step 4 : verify_page_delete_dialog_is_displayed")
        portal_obj.verify_page_delete_dialog_message("Are you sure you want to delete 'Change page name' ?","Step 4.1 = verify_page_delete_dialog_message")
        
        """
        Step 5: Click OK.
                Verify 'Change page name' page is deleted. 
        """
        portal_obj.click_ok_button_in_page_delete_dialog()
        portal_obj_2.verify_specific_folder_not_in_top_folders(['Change page name'], msg="Step 5 : Verify folder is deleted")
        
        """
        Step 6: Close the 'V5 Personal Portal_Nav-2' run window. 
        """
        coreutil_obj.switch_to_previous_window()
        
        """
        Step 7: If not expand 'P292_S19901' domain > G514402 > V5 Personal Portal_Nav-2 > My Pages > My Content in tree.
                Verify 'Change page name' page is deleted.
        """
        util_obj.synchronize_with_number_of_element(domains_css, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('{0}_{1}->{2}->{3}->My Pages'.format(project_id, suite_id, group_id, portal_name))
        main_page_obj.expand_repository_folder('My Content', index=1)
        main_page_obj.verify_items_in_grid_view(['Change page name'], 'asnotin', "Step 8: Verify 'Change page name' page is deleted.")
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main() 