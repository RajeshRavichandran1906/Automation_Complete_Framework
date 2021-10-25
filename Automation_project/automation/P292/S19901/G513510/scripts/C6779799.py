'''
Created on Nov 15, 2018

@author: KK14897

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/19901&group_by=cases:section_id&group_id=520454&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6779799
TestCase Name = Verify UnShared personal page does not shows share icon inside the My Content folder 
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity,core_utility
from common.lib.global_variables import Global_variables

class C6779799_TestClass(BaseTestCase):

    def test_C6779799(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        folder_name_path="Domains->P292_S19901_G520454"
        content_css='div[class="ibx-label-glyph ibx-label-icon fa fa-bar-chart"]'
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(content_css, '1', Global_variables.longwait)

        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'.
        """
        main_page_obj.expand_repository_folder(folder_name_path) 
        util_obj.synchronize_with_number_of_element(crumb_css, '1', Global_variables.longwait)
        
        """
        Step 3: Right click on 'V5 Portal Share' from the content area > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Portal Share','Run') 
        core_utility_obj.switch_to_new_window() 
        time.sleep(Global_variables.longwait)
        """
        Step 4: Click on Share button from the personal page toolbar.
        """
        share_css="div[class^='pd-page-header'] div[class^='pd-header-buttons'] div[class*='button-share']"
        share_button_obj=util_obj.validate_and_get_webdriver_object(share_css,'share_button_css')
        share_button_obj.click()
        
        """
        Step 5: Click X button under Shared with 'autobaseuser08' textbox to unshare the already shared 'autobaseuser08' user > Click OK
        """
        share_dialog_css="div[class^='share-with-others-dialog']"
        util_obj.synchronize_with_number_of_element(share_dialog_css, '1', Global_variables.longwait)
        util_obj.synchronize_with_number_of_element('div[class*="ibx-title-bar-close-button"]', 1, 50)
        util_obj.synchronize_with_number_of_element('input[type="search"]', 1, 50)
        util_obj.synchronize_with_number_of_element('div[class*="sw-item-name"]', 1, 50)
        util_obj.synchronize_with_number_of_element('div[class*="ibx-label-text"]', 1, 50)
        close_obj=util_obj.validate_and_get_webdriver_object('div[class*="sw-close-button"]','Close_button_css')
        close_obj.click()
        OK_obj=util_obj.validate_and_get_webdriver_object('div[class*="ibx-dialog-ok-button"]','Ok_button_css')
        OK_obj.click()
        """
        Step 6: Hover the mouse to the Share button
        """
        obj=self.driver.find_element_by_css_selector(share_css)
        util_obj.click_on_screen(obj, coordinate_type='middle')
        time.sleep(Global_variables.longwait)
        util_obj.synchronize_with_number_of_element(share_css, 1, 50)
       
        """
        Step 7: Close the portal run window.
        """
        core_utility_obj.switch_to_previous_window()
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()