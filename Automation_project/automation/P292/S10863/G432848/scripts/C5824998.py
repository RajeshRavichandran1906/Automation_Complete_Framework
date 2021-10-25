'''
Created on April 16, 2019

@author: Varun

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5824998
TestCase Name = Verify Sharing UI opens
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login 
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib import javascript

class C5824998_TestClass(BaseTestCase):

    def test_C5824998(self):
        """
        TESTCASE VARIABLES
        """
        js_obj = javascript.JavaScript(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        drop_down_css = ".share-with-div-toolbar .Share-with-menu-btn  .ds-icon-caret-down"
        share_element_css = ".share-with-div-toolbar .share-with-txt-search input"
        
        """ 
        Step 1: Login WF as domain developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from the sidebar and Click on Domain from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        main_page_obj.click_repository_folder('Workspaces')
        
        """
        Step 3: Expand the domain from the tree and click on 'P292_S10863_G193429'
        """
        main_page_obj.expand_repository_folder('Workspaces->P292_S10863_G193429')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Folders\"]", 1, main_page_obj.home_page_short_timesleep)
        
        """
        Step 4: Click on My Content from the tree
        Verify report1 appears in the content area
        """
        main_page_obj.click_repository_folder('My Content')
        util_obj.synchronize_with_visble_text("div[data-ibxp-text=\"Items \"]", 'Items', main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_items_in_grid_view(['report1'], 'asin', 'Step 4: Verify report1 in the content area')
        
        """
        Step 5: Right click on report1 and select Share with...
        Verify 'Share with Others' window appears with the following options:
        1. 'Enter users and groups' search box is empty with the dropdown control, 
        2. OK button is disabled and Cancel button is enabled by default,
        3. Share with everyone checkbox.
        """
        main_page_obj.right_click_folder_item_and_select_menu('report1', 'Share with...')
        util_obj.synchronize_with_visble_text(".ibx-title-bar-caption", 'Share with Others', main_page_obj.report_short_timesleep)
        share_text = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(share_element_css,"Share_text" ), 'value')
        util_obj.asequal('', share_text, "Step 5.1: Verify the textbox is empty")
        drop_down_button = util_obj.validate_and_get_webdriver_object(drop_down_css, 'drop-down')
        drop_down_button_content = js_obj.get_element_before_style_properties(drop_down_button, 'content').replace('"', '')
        util_obj.asequal('\uea73', drop_down_button_content, "Step 5.2: Verify the drop down is present")
        ok_button_status = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(".ibx-dialog-ok-button",'ok'),'aria-disabled')
        util_obj.asequal('true', ok_button_status, "Step 5.3: Verify ok button is disabled")
        cancel_button_status = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(".ibx-dialog-cancel-button",'cancel'),'aria-disabled')
        util_obj.asequal('false', cancel_button_status, "Step 5.4: Verify cancel button is enabled")
        check_box_status = util_obj.get_element_attribute(util_obj.validate_and_get_webdriver_object(".share_with_everyone",'checkbox'),'role')
        util_obj.asequal('checkbox',check_box_status, "Step 5.5: Verify share with everyone checkbox is present")
        
        """
        Step 6: Click Cancel button to close the Share with Others window
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()