'''
Created on October 24, 2018

@author: varun
Testcase Name : Portal Menu Defaults
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261525
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.pages import wf_mainpage as pages
from common.lib import utillity
import pyautogui
from common.lib.global_variables import Global_variables
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261525_TestClass(BaseTestCase):
    
    def test_C8261525(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        pages_obj = pages.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_visble_text('div.crumb-box', 'Workspaces', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        
        """
        Step 3: If not expand Domains > click on 'P292_S19901' > 'G513445' folder from the resource tree
        """
        main_page_obj.expand_repository_folder('P292_S19901->G513445')
        util_obj.wait_for_page_loads(10)
        
        """
        Step 4: Right click on 'Portal for Context Menu Testing'
        """
        verify_list = ['Open', 'Run', 'Edit', 'Customizations', 'Paste Ctrl+V', 'Delete DEL', 'Add to Favorites', 'Unpublish', 'Hide', 'Security', 'Properties']
        main_page_obj.verify_repository_folder_item_context_menu('Portal for Context Menu Testing', verify_list,msg="Step 4:")
        
        """
        Step 5: Hover over Customization menu
        """
        sub_menu_css = "div[data-ibx-name=\"foMenuItemMyCustomizations\"]"
        pages_obj.select_context_menu_item('Customizations')
        util_obj.synchronize_with_number_of_element(sub_menu_css, 1, Global_variables.shortwait)
        pages_obj.verify_context_menu_item(['Remove my customizations', 'Remove customizations for all users'], msg="Step 5: Verify that the following options are displayed under Customizations.")
        x_position,y_position = pyautogui.position()
        y_position += 20
        pyautogui.mouseDown(x_position,y_position)
        
        """
        Step 6: Hover over Security Menu
        """
        sub_menu_css = "div[data-ibx-name=\"foMenuItemRules\"]"
        pages_obj.select_context_menu_item('Security')
        util_obj.synchronize_with_number_of_element(sub_menu_css, 1, Global_variables.shortwait)
        pages_obj.verify_context_menu_item(['Rules...', 'Rules on this resource...', 'Effective policy...', 'Owner...'], msg="Step 6: Verify that the following options are displayed under Customizations.")
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()