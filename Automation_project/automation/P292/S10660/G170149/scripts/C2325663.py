'''
Created on May 21, 2018
Updated on May 25, 2018

@author: KS13172

Test Suite = http://lnxtestrail.ibi.com/testrail/index.php?/suites/view/10660
Test Case = http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325663
TestCase Name = As an Admin User, create each user to test default menu links
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.pages import security_center
from common.lib import utillity
from common.lib import core_utility
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2325663_TestClass(BaseTestCase):

    def test_C2325663(self):
        
        """
        TESTCASE Objects
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        core_utilobj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        security_obj = security_center.Security_Center(driver)
        
        """
        TESTCASE VARIABLES
        """
        Admin_username = 'mrid'
        Admin_password = 'mrpass'
        c_id = Global_variables.current_test_case
        
        """
        Step01: Sign into WebFOCUS Home Page as Administrator
        """
        wftools_login_obj.invoke_home_page(Admin_username, Admin_password)
        
        """
        Step02: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.wait_for_page_loads(wfmain_obj.home_page_medium_timesleep)
        utillobj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, wfmain_obj.home_page_medium_timesleep)
        wfmain_obj.click_repository_folder('Workspaces')
        utillobj.wait_for_page_loads(wfmain_obj.home_page_medium_timesleep)
        
        """
        Step03: In the banner link, click on the top right username
        Step04: Hover the mouse to the option Administration and select Security Center.
        Expected Verify Security Center window opens in a new window appears outside of the main browser.
        Step05: Maximize Security Center window.
        """
        folders_css=".menu-btn div[class*='down']"
        utillobj.synchronize_with_number_of_element(folders_css, 1, wfmain_obj.home_page_long_timesleep)
        wfmain_obj.select_username_dropdown_menu(navigate_path='Administration->Security Center')
        core_utilobj.switch_to_new_window()
        utillobj.asequal(len(driver.window_handles), 2, "Step 03.01: Verify new window opened")
        
        security_manager_css = "#SecurityManagerDialog_tabUserGroups"
        utillobj.synchronize_with_number_of_element(security_manager_css, 1, wfmain_obj.home_page_medium_timesleep)
        utillobj.asequal(driver.title, "Security Center", "Step 03.02: Verify Security Center title displayed in new window")        
        
        """
        Step06: Create five new users and assign to its corresponding Domains/group:
        1.Admin_User assign to Administrators.
        2.Basic_User assign to Retail_Samples/BasicUsers.
        3.Advanced_User assign to Retail_Samples/AdvancedUsers.
        4.Developer_User assign to Retail_Samples/Developers.
        5.Groupadmin_User assign to Retail_Samples/GroupAdmins.
        """
        if Global_variables.browser_name == 'edge' : #y coordinate is not proper in function for edge browser
            availHeight = self.driver.execute_script("return screen.availHeight;")
            innerWidth = self.driver.execute_script("return window.innerHeight ")
            Global_variables.current_working_area_browser_y=availHeight-innerWidth
        security_obj.create_user_('Admin_user_{0}'.format(c_id), group='Administrators', btn= 'create')
        security_obj.close_New_User_dialog()
        add_newuser_icon="#dlgSecurityManager #SecurityManagerDialog_btnNewUser"
        utillobj.synchronize_with_number_of_element(add_newuser_icon, 1, wfmain_obj.home_page_medium_timesleep)
        security_obj.create_user_('Basic_user_{0}'.format(c_id), group='Retail_Samples/BasicUsers', btn= 'create')
        security_obj.close_New_User_dialog()
        add_newuser_icon="#dlgSecurityManager #SecurityManagerDialog_btnNewUser"
        utillobj.synchronize_with_number_of_element(add_newuser_icon, 1, wfmain_obj.home_page_medium_timesleep)
        security_obj.create_user_('Advanced_user_{0}'.format(c_id), group='Retail_Samples/AdvancedUsers', btn= 'create')
        security_obj.close_New_User_dialog()
        utillobj.synchronize_with_number_of_element(add_newuser_icon, 1, wfmain_obj.home_page_medium_timesleep)
        security_obj.create_user_('Developer_user_{0}'.format(c_id), group='Retail_Samples/Developers', btn= 'create')
        security_obj.close_New_User_dialog()
        utillobj.synchronize_with_number_of_element(add_newuser_icon, 1, wfmain_obj.home_page_medium_timesleep)
        security_obj.create_user_('Groupadmin_User_{0}'.format(c_id), group='Retail_Samples/GroupAdmins', btn= 'create')
         
        security_obj.close_New_User_dialog()
        utillobj.synchronize_with_number_of_element(add_newuser_icon, 1, wfmain_obj.home_page_medium_timesleep)
        
        security_obj.verify_user_in_group_('Administrators', ['admin_user_{0}'.format(c_id.lower())], "Step 05.01: Verify Admin user added to group- Administrators")
        time.sleep(3)
        security_obj.verify_user_in_group_('Retail_Samples->BasicUsers', ['basic_user_{0}'.format(c_id.lower())], "Step 05.02: Verify Basic user added to group- Retail_Samples/BasicUsers")
        time.sleep(3)
        security_obj.verify_user_in_group_('Retail_Samples->AdvancedUsers', ['advanced_user_{0}'.format(c_id.lower())], "Step 05.03: Verify Advanced user added to group- Retail_Samples/AdvancedUsers")
        time.sleep(3)
        security_obj.verify_user_in_group_('Retail_Samples->Developers', ['developer_user_{0}'.format(c_id.lower())], "Step 05.04: Verify developer user added to group- Retail_Samples/Developers")
        time.sleep(3)
        security_obj.verify_user_in_group_('Retail_Samples->GroupAdmins', ['groupadmin_user_{0}'.format(c_id.lower())], "Step 05.05: Verify GroupAdmin user added to group- Retail_Samples/GroupAdmins")
        
        """
        Step07: Close Security Center window
        """
        security_obj.close_security_center_window()
        if len(driver.window_handles) != 1:
            time.sleep(45)
        
        """
        Step08: In the banner link, click on the top right username > Click Sign Out.
        """
        core_utilobj.switch_to_previous_window(window_close = False)
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()        