"""-------------------------------------------------------------------------------------------
Created on October 23, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2511486
Test Case Title =  Verify Columns added are remembered
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C2511486_TestClass(BaseTestCase):

    def test_C2511486(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils=CoreUtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        CONTENT_LIST = ['Content', 'Portals', 'Favorites']
        DEV_USER_EXPECTED_LIST_CONTENT_LABLES1 = ['Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown']
        DEV_USER_EXPECTED_LIST_CONTENT_LABLES2 = ['Title', 'Name', 'Summary', 'Last modified', 'Size', 'Published', 'Shown']
        ADV_USER_EXPECTED_LIST_CONTENT_LABLES = ['Title', 'Summary', 'Last modified', 'Size']
        LIST_VIEW_CSS = "[class*='fa fa-list']"
        GRID_VIEW_CSS = "[class*='fa fa-th']"
    
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User.
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text("div[title^='Content']", 'Content', 80)
        if self.driver.find_element_by_css_selector("[class*='fa fa-list']").is_displayed()==False:
            grid_object=utils.validate_and_get_webdriver_object("[class*='fa fa-th']", "GRID_VIEW_CSS")
            core_utils.left_click(grid_object)
        
        """
            STEP 01.1 : Verify by default Content View is selected and displayed in Grid View.
        """
        wf_home.verify_left_panel(CONTENT_LIST, "Step 01.01 : Verify by default Content View is selected", comparision_type='asin')
        utils.verify_object_visible(LIST_VIEW_CSS, True, "Step 01.02 : Verify grid view image is displaying")
        
        """
            STEP 02 : Click toggle button list view.
        """
        wf_home.select_list_view()
        
        """
            STEP 02.1 : Verify content area shows in list view.
        """
        utils.verify_object_visible(GRID_VIEW_CSS, True, "Step 02.01 : Verify grid view image is displaying")
        wf_home.verify_list_view_title_labels(DEV_USER_EXPECTED_LIST_CONTENT_LABLES1, "Step 02.2: Verify list view titles")
        
        """
            STEP 03 : Click sorting tool option. Add Name.
        """
        wf_home.select_list_view_columns(['Name'])
        
        """
            STEP 04 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User.
        """
        wf_home.signout_from_username_dropdown_menu()
        wf_login.invoke_home_page('mridadv', 'mrpassadv')
        utils.synchronize_with_visble_text(".crumb-box [title='Workspaces']", 'Workspaces', 40)
        
        """
            STEP 04.1 : Verify by default Content View is selected and displayed in Grid View..
        """
        wf_home.verify_left_panel(CONTENT_LIST, "Step 04.01 : Verify by default Content View is selected", comparision_type='asin')
        utils.verify_object_visible(LIST_VIEW_CSS, True, "Step 04.03 : Verify list view image is displaying")
        
        """
            STEP 05 : Click toggle button.
        """
        wf_home.select_list_view()
        
        """
            STEP 05.1 : Verify content area shows in list view. Name is not showing.
        """
        utils.verify_object_visible(GRID_VIEW_CSS, True, "Step 05.01 : Verify grid view image is displaying")
        wf_home.verify_list_view_title_labels(ADV_USER_EXPECTED_LIST_CONTENT_LABLES, "Step 05.2 : Verify content area shows in list view. Name is not showing")
        
        """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User.
        """
        wf_home.signout_from_username_dropdown_menu()
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(".crumb-box [title='Workspaces']", 'Workspaces', 40)
        
        """
            STEP 06.1 : Verify content area shows in list view with the added Name option.
        """
        wf_home.verify_left_panel(CONTENT_LIST, "Step 06.01 : Verify by default Content View is selected", comparision_type='asin')
        utils.verify_object_visible(GRID_VIEW_CSS, True, "Step 06.02 : Verify grid view image is displaying")
        wf_home.verify_list_view_title_labels(DEV_USER_EXPECTED_LIST_CONTENT_LABLES2, "Step 06.3 : Verify content area shows in list view with the added Name option")
        
        """
            STEP 07 : Revert back the Home Page by its default state (Click content from the sidebar, click on Domain from navigation bar and change into Grid View )
        """
        wf_home.select_content_from_sidebar()
        wf_home.select_grid_view()
        
        """
            STEP 08 : In the banner link, click on the top right username > Click Sign Out.
        """       
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        