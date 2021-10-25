'''
Created on April 17, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5825000
TestCase Name = Verify search for users functionality
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility

class C5825000_TestClass(BaseTestCase):

    def test_C5825000(self):
        """
        TESTCASE VARIABLES
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        drop_down_css = ".share-with-div-toolbar .Share-with-menu-btn  .ds-icon-caret-down"
        share_element_css = ".share-with-div-toolbar .share-with-txt-search input"
        users_css = "div[data-ibx-name=\"miModeUser\"]"
        
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
        Step 5: Click on drop-down in the search box > Choose Users in the drop-down list.
        """
        drop_down_element = util_obj.validate_and_get_webdriver_object(drop_down_css, 'drop-down')
        core_util_obj.left_click(drop_down_element)
        core_util_obj.left_click(util_obj.validate_and_get_webdriver_object(users_css, 'users'))
        
        """
        Step 6: Enter 'autodevuser82' in the 'Enter users' search box.
        Verify users contains with the name dev ('autodevuser82') appears with its description and email address if we added
        """
        text_box = util_obj.validate_and_get_webdriver_object(share_element_css,'text-box')
        text_box.send_keys('autodevuser82')
        util_obj.synchronize_with_number_of_element(".share-with-container-dialog .item-user-group", 1, main_page_obj.home_page_medium_timesleep)
        drop_down_text = util_obj.validate_and_get_webdriver_object(".share-with-container-dialog .item-user-group", 'drop_down_text').text
        util_obj.asequal('autodevuser82\nautodevuser82(auto@devmail.com)',drop_down_text, "Step 6.1: Verify the drop down text")
        
        """
        Step 7: Click Cancel button to close the Share with Others window.
        """
        cancel_button = util_obj.validate_and_get_webdriver_object(".ibx-dialog-cancel-button", "cancelbutton")
        core_util_obj.left_click(cancel_button)
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()