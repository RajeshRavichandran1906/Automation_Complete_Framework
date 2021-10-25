'''
Created on April 16, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5824999
TestCase Name = Verify drop down list options in search box 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility

class C5824999_TestClass(BaseTestCase):

    def test_C5824999(self):
        """
        TESTCASE VARIABLES
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        drop_down_css = ".share-with-div-toolbar .Share-with-menu-btn  .ds-icon-caret-down"
        share_element_css = ".share-with-div-toolbar .share-with-txt-search input"
        user_elements_css = ".Share-with-others-menu div[data-ibx-type=\"ibxCheckMenuItem\"]"
        user_list = ['Users', 'Groups', 'Users/Groups']
        group_css = "div[data-ibx-name=\"miModeGroup\"]"
        users_css = "div[data-ibx-name=\"miModeUser\"]"
        user_group_css = "div[data-ibx-name=\"miModeUserGroup\"]"
        
        """ 
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from the sidebar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand the domain from the tree and click on 'P292_S10863_G193429'.
        """
        main_page_obj.expand_repository_folder('Workspaces->P292_S10863_G193429')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Folders\"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 4: Click on My Content folder > Right click on report1 > Select Share with...
        """
        main_page_obj.click_repository_folder('My Content')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Items \"]", 'Items', main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('report1', 'Share with...')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'Share with Others', main_page_obj.report_short_timesleep)
        
        """
        Step 5: Click on drop-down in the search box.
        Verify Users, Groups and Users/groups (By default checked) are appears
        """
        drop_down_element = util_obj.validate_and_get_webdriver_object(drop_down_css, 'drop-down')
        core_util_obj.left_click(drop_down_element)
        user_elements = util_obj.validate_and_get_webdriver_objects(user_elements_css, "user-elements")
        user_elements_text = [element.text for element in user_elements]
        util_obj.asequal(user_list, user_elements_text, "Step 5.1: Verify the userlist is same")
        user_group_check = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(user_group_css,'userg'), 'aria-selected')
        util_obj.asequal('true', user_group_check, "Step 5.2: Verify user group is checked")
        
        """
        Step 6: Click on Users in the drop-down list.
        Verify Users is checked, 'Enter users' appears in the search box and the drop-down lists still appear
        """
        core_util_obj.left_click(util_obj.validate_and_get_webdriver_object(users_css, 'users'))
        users_check = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(users_css,'users'), 'aria-selected')
        util_obj.asequal('true', users_check, "Step 6.1: Verify users is checked")
        placeholder_text = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(share_element_css,'text-box'), 'placeholder')
        util_obj.asequal('Enter users', placeholder_text, "Step 6.2: Verify the placholder text")
        util_obj.verify_object_visible(drop_down_css, True, "Step 6.3: Verify the dropdown is visible")
        
        
        """
        Step 7: Click on Groups in the drop-down list.
        Verify Groups is checked, 'Enter groups' appears in the search box and the drop-down lists still appear
        """
        core_util_obj.left_click(util_obj.validate_and_get_webdriver_object(group_css, 'group'))
        group_check = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(group_css,'users'), 'aria-selected')
        util_obj.asequal('true', group_check, "Step 7.1: Verify groups is checked")
        placeholder_text = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(share_element_css,'text-box'), 'placeholder')
        util_obj.asequal('Enter groups', placeholder_text, "Step 7.2: Verify the placholder text")
        util_obj.verify_object_visible(drop_down_css, True, "Step 7.3: Verify the dropdown is visible")
        
        """
        Step 8: Click on Users/Groups in the drop-down list.
        Verify Users/Groups is checked, 'Enter users/groups' appears in the search box and the drop-down lists still appear
        """
        core_util_obj.left_click(util_obj.validate_and_get_webdriver_object(user_group_css, 'userg'))
        group_check = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(user_group_css,'userg'), 'aria-selected')
        util_obj.asequal('true', group_check, "Step 8.1: Verify users/groups is checked")
        placeholder_text = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(share_element_css,'text-box'), 'placeholder')
        util_obj.asequal('Enter users and groups', placeholder_text, "Step 8.2: Verify the placholder text")
        util_obj.verify_object_visible(drop_down_css, True, "Step 8.3: Verify the dropdown is visible")
        pop_element = util_obj.validate_and_get_webdriver_object('.share-with-container', 'pop-up')
        core_util_obj.left_click(pop_element)
        
        """
        Step 9: Click Cancel button to close the Share with Others window.
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        
        """
        Step 10: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()