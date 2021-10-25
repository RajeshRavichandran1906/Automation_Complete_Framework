"""-------------------------------------------------------------------------------------------
Created on October 25, 2018
@author: Nasir

Test Case Link  =  http://172.19.2.180/testrail/index.php?/cases/view/8261551
Test Case Title =  Test Run menu 
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.core_utility import CoreUtillityMethods
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C8261551_TestClass(BaseTestCase):

    def test_C8261551(self):        
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id = utils.parseinitfile('project_id')
        suite_id = utils.parseinitfile('suite_id')
        group_id = utils.parseinitfile('group_id')
        ITEM_NAME = 'Portal for Context Menu Testing'
        EXPECTED_URL = 'portal/{0}_{1}/{2}/Portal_for_Context_Menu_Testing'.format(project_id, suite_id, group_id)
        PAGE_TITLE_CSS = '.pvd-portal-title'
        File_box_css="div.files-box"
        
        """    1. Sign into WebFOCUS Home Page as Admin User    """
        wf_login.invoke_home_page('mrid', 'mrpass')
        
        """    2. Click Content View from the sidebar > Click on Domains from the resource tree    """
        utils.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, wf_home.home_page_long_timesleep)
        wf_home.select_content_from_sidebar()
        utils.wait_for_page_loads(10)
        utils.synchronize_with_visble_text(WfMainPageLocators.content_area_css, "Folder", wf_home.home_page_medium_timesleep)
        utils.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, wf_home.home_page_medium_timesleep)
        wf_home.select_option_from_crumb_box('Domains')
        
        """    3. Click on Portal View from the sidebar    """
        wf_home.select_portals_from_sidebar()
        utils.synchronize_with_visble_text(File_box_css, 'Portal for Context Menu Testing', wf_home.home_page_medium_timesleep)
        
        """    4. Right click on 'Portal for Context Menu Testing' > Click Run
        Verify that 'Portal for Context Menu Testing' portal run in a new tab and its URL as 'http://machine name:port/alias/portal/P292_S19901/G513445/Portal_for_Context_Menu_Testing'    """
        wf_home.right_click_folder_item_and_select_menu('Portal for Context Menu Testing', 'Run')
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(PAGE_TITLE_CSS, ITEM_NAME, 20)
        ACTUAL_URL = self.driver.current_url
        ACTUAL_PAGE_TITLE = utils.validate_and_get_webdriver_object(PAGE_TITLE_CSS, 'Page title').text.strip()
        utils.asin(EXPECTED_URL, ACTUAL_URL, 'Step 04.01 : Verify V5 portal opens')
        utils.asequal(ACTUAL_PAGE_TITLE, ITEM_NAME, "Step 04.02 : Verify that 'Portal for Context Menu Testing' opens in a new tab")
        
        """    5. Close the 'Portal for Context Menu Testing' portal run window    """
        core_utils.switch_to_previous_window()
        
        """    6. In the banner link, click on the top right username > Click Sign Out.    """
        wf_home.signout_from_username_dropdown_menu()
        
        
        
if __name__ == '__main__':
    unittest.main()        