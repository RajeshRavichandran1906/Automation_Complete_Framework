"""-------------------------------------------------------------------------------------------
Created on August 21, 2019
@author: Niranjan

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667716
Test Case Title =  AUTHZ_BasicUser:Check WebFOCUS Online Help and Change Password functionality
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.core_utility import CoreUtillityMethods
from common.lib import global_variables
import time

class C6667716_TestClass(BaseTestCase):

    def test_C6667716(self):
        
        """
            Test case objects    
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()
        core_utils = CoreUtillityMethods(self.driver)
        gv = global_variables.Global_variables()
        
        """
            STEP 1 : Sign into WebFOCUS Home Page as Basic User.
        """
        login.invoke_home_page("mridbas", "mrpassbas")
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 2 : In the banner link, click on the top right username > Help > click WebFOCUS Online Help.
        """
        main_page.select_username_dropdown_menu(navigate_path="Help->WebFOCUS Online Help")
        core_utils.switch_to_new_window()
        time.sleep(15)
        core_utils.switch_to_frame(frame_css="frame[name='HelpFrame']")
        
        """
            STEP 2.1 : Verify Help page opens in a new tab with an index on the left.
        """
        index_obj = utils.validate_and_get_webdriver_object("frame[name='NavFrame']", "Index css")
        actual_result = index_obj.location['x']
        msg = "Step 2.1 : Verify Help page opens in a new tab with an index on the left."
        utils.asequal(actual_result, 0, msg)
        
        """
            STEP 3 : Close Help tab.
        """
        core_utils.switch_to_previous_window(window_close=True)
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 4 : In the banner link, click on the top right username > Change Password.
        """
        main_page.select_username_dropdown_menu(navigate_path="Change Password")
        utils.synchronize_with_visble_text("div.change-old-password", "Password", main_page.home_page_medium_timesleep)
        
        """
            STEP 4.1 : Verify Change Password dialog box opens with a background transparent gray layer over the rest of the WebFOCUS Home Page.
        """
        change_pass_obj = utils.validate_and_get_webdriver_object("div.change-old-password", "Change Password")
        actual_result = change_pass_obj.is_displayed()
        msg = "Step 4.1 : Verify Change Password dialog box opens with a background transparent gray layer over the rest of the WebFOCUS Home Page."
        utils.asequal(True, actual_result, msg)
        
        background_obj = utils.validate_and_get_webdriver_object("div.ibx-popup-glass-pane", "Back ground css")
        actual_result = background_obj.value_of_css_property("background-color")
        msg = "Step 4.2 : Verify Change Password dialog box opens with a background transparent gray layer over the rest of the WebFOCUS Home Page."
        if gv.browser_name == 'chrome':
            utils.asequal("rgba(0, 0, 0, 1)", actual_result, msg)
        else:
            utils.asequal("rgb(0, 0, 0)", actual_result, msg)
            
        actual_result = background_obj.value_of_css_property("opacity")
        msg = "Step 4.3 : Verify Change Password dialog box opens with a background transparent gray layer over the rest of the WebFOCUS Home Page."
        utils.asequal("0.5", actual_result, msg)
        
        """
            STEP 5 : Enter Values in,
            Old Password: password 
            New Password: password2
            Confirm New Password: password2
            Click OK button.
            STEP 5.1 : Verify the window should disappear and displays a confirmation message "Your Password has been changed" with a background transparent green layer over the message.
        """
        main_page.change_password("password", "password2")
        
        """
            STEP 6 : In the banner link, click on the top right username > Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
        """
            STEP 7 : Sign into WebFOCUS Home Page as Basic User with the new password.
        """
        login.invoke_home_page('mridbasnew', 'mrpassbasnew')
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 7.1 : Verify WebFOCUS Home Page opens without any error.
        """
        content_obj = utils.validate_and_get_webdriver_object(locator.CONTENT_CSS, "Content css")
        actual_result = content_obj.is_displayed()
        msg = "Step 7.1 : Verify WebFOCUS Home Page opens without any error."
        utils.asequal(True, actual_result, msg)
        
        """
            STEP 8 : Again, from the banner link click on the top right username > Change Password.
        """
        main_page.select_username_dropdown_menu(navigate_path="Change Password")
        utils.synchronize_with_visble_text("div.change-old-password", "Password", main_page.home_page_medium_timesleep)
        
        """
            STEP 9 : Revert back to its Old Password by enter Values in,
            Old Password: password2
            New Password: password 
            Confirm New Password: password
            Click OK button.
            STEP 9.1 : Verify the window should disappear and displays a confirmation message "Your Password has been changed" with a background transparent green layer over the message.
        """
        main_page.change_password("password2", "password")
        
        """
            STEP 10 : In the banner link, click on the top right username > Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        
        """
            STEP 11 : Sign into WebFOCUS Home Page as Basic User with the new password.
        """
        login.invoke_home_page('mridbas', 'mrpassbas')
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        
        """
            STEP 11.1 : Verify the password is revert back to its old password & WebFOCUS Home Page opens without any error.
        """
        content_obj = utils.validate_and_get_webdriver_object(locator.CONTENT_CSS, "Content css")
        actual_result = content_obj.is_displayed()
        msg = "Step 11.1 : Verify the password is revert back to its old password & WebFOCUS Home Page opens without any error."
        utils.asequal(True, actual_result, msg)
        
        """
            STEP 12 : In the banner link, click on the top right username > Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
                
if __name__ == '__main__':
    unittest.main()