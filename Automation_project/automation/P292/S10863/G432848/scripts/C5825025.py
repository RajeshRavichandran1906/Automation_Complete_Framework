'''
Created on April 17, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5825025
TestCase Name = Verify a user or group can be deleted in UI
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.lib import javascript

class C5825025_TestClass(BaseTestCase):

    def test_C5825025(self):
        """
        TESTCASE VARIABLES
        """
        js_obj = javascript.JavaScript(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        drop_down_css = ".share-with-div-toolbar .Share-with-menu-btn  .ds-icon-caret-down"
        share_element_css = ".share-with-div-toolbar .share-with-txt-search input"
        pop_top_css = ".pop-top"
        fex_name = 'report1'

        
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
        Verify 'Share with Others' dialog opens with the following options:
        1.X button is displays at the top right corner of the dialog box
        2.Enter users and groups' search box with the dropdown control is empty
        3.Under shared with it shows 'autobaseuser08' and 'autoadvuser04' user
        4.Share with everyone checkbox
        5.OK button is disabled
        6.Cancel button is enabled
        """
        main_page_obj.click_repository_folder('My Content')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Items \"]", 'Items', main_page_obj.home_page_short_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu('report1', 'Share with...')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'Share with Others', main_page_obj.report_short_timesleep)
        close_button = util_obj.validate_and_get_webdriver_object(".ibx-title-bar-close-button","close")
        close_coordinate = core_util_obj.get_web_element_coordinate(close_button)
        title = util_obj.validate_and_get_webdriver_object(".ibx-title-bar-caption","title")
        title_coordinate = core_util_obj.get_web_element_coordinate(title)
        util_obj.as_LE(title_coordinate['x'], close_coordinate['x'], "Step 4.1: Verify the close button is in the right of title")
        text_box = util_obj.validate_and_get_webdriver_object(share_element_css,'text-box')
        text_box_coordinate = core_util_obj.get_web_element_coordinate(text_box)
        util_obj.as_LE(close_coordinate['y'],text_box_coordinate['y'], "Step 4.2: Verify the close coordinate on the top of search box")
        share_text = util_obj.get_element_attribute(text_box, 'value')
        util_obj.asequal('', share_text, "Step 4.3: Verify the textbox is empty")
        drop_down_button = util_obj.validate_and_get_webdriver_object(drop_down_css, 'drop-down')
        drop_down_button_content = js_obj.get_element_before_style_properties(drop_down_button, 'content').replace('"', '')
        util_obj.asequal('\uea73', drop_down_button_content, "Step 4.4: Verify the drop down is present")
        ok_button_status = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok'),'aria-disabled')
        util_obj.asequal('true', ok_button_status, "Step 4.5: Verify ok button is disabled")
        cancel_button_status = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(".ibx-dialog-cancel-button",'cancel'),'aria-disabled')
        util_obj.asequal('false', cancel_button_status, "Step 4.6: Verify cancel button is enabled")
        check_box_status = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(".share_with_everyone",'checkbox'),'role')
        util_obj.asequal('checkbox',check_box_status, "Step 4.7: Verify share with everyone checkbox is present")
        container_text = util_obj.validate_and_get_webdriver_object(".share-with-container", 'container-text').text.strip()
        util_obj.asin('autoadvuser04', container_text, "Step 4.8: Verify autoadvuser04 is present in share items ")
        util_obj.asin('autobasuser08', container_text, "Step 4.9: Verify autobasuser08 is present")
        
        """
        Step 5: Click X button under Shared with 'autobaseuser08' textbox to unshare the already shared 'autobaseuser08' user > Click OK
        Verify 'Share with Others' window gets closed
        """
        share_item_obj = util_obj.validate_and_get_webdriver_objects(".share-with-item", "share_items")
        for item in share_item_obj:
            if 'autobasuser08' in item.text.strip():
                close_button = util_obj.validate_and_get_webdriver_object(".sw-close-button", 'close-button', item)
                core_util_obj.left_click(close_button)
        core_util_obj.left_click(util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button", 'ok-button'))
        util_obj.verify_object_visible(".share-with-container", False, "Step 5.1: Verify the share tab is not visible")
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, 'Unshare')
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()