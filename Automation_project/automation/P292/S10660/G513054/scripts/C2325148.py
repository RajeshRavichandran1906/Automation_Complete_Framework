"""-------------------------------------------------------------------------------------------
Created on November 22, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325148
Test Case Title =  Verify all items that contain the character in the title appear
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login
from common.locators import wf_mainpage_locators

class C2325148_TestClass(BaseTestCase):

    def test_C2325148(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = Login(self.driver)
        wf_home = Wf_Mainpage(self.driver)
        utlis = UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
            COMMON TEST CASE VARIABLES 
        """
        LONG_WAIT_TIME = 120
        MEDIUM_WAIT_TIME = 60
        SHORT_WAIT_TIME= 30
            
        """
            STEP 01 : Sign in to WebFOCUS as Developer User.
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utlis.synchronize_with_visble_text(".left-main-panel .left-main-panel-content-button", 'Content', LONG_WAIT_TIME)
        
        """
            STEP 02 : Click on the Content tree from the sidebar.
        """
        wf_home.select_content_from_sidebar()
        
        """
            STEP 03 : Click on Domains from the tree.
        """
        wf_home.expand_repository_folder('Workspaces')
        utlis.synchronize_with_visble_text(locator_obj.folders_css, 'Folders', SHORT_WAIT_TIME)
        
        """
            STEP 04 : Type x in the search box.
        """
        wf_home.search_input_box_options(input_text_msg='x')
        utlis.synchronize_with_visble_text(".sd-category-buttons .sd-category-button-green", 'P292_S10660', MEDIUM_WAIT_TIME)
        
        """
            STEP 04.1 : Verify that items containing x in the title appear
        """
        wf_home.verify_folders_contain_searched_text_in_grid_view('x', 'Step 04.01 : Verify folders contains "x"')
        wf_home.verify_items_contain_searched_text_in_grid_view('x', 'Step 04.01 : Verify folders contains "x"')
        
        """
            STEP 05 : If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box.
            STEP 06 : Click X to clear the search box.
        """
        wf_home.search_input_box_options(option_type='clear')
        utlis.synchronize_with_visble_text(locator_obj.folders_css, 'Folders', MEDIUM_WAIT_TIME)
        
        """
            STEP 06.1 : Verify search box is cleared and "Search Domains" appears in the box
            STEP 07 : Or else for FF browser, use the backspace to clear the search box.
            STEP 07.1 : Verify search box is cleared and "Search Domains" appears in the box 
        """
        wf_home.verify_search_textbox_value('Search Workspaces', 'Step 06.01 : Verify search box is cleared and "Search Domains" appears in the box')
        
        """
            STEP 08 : In the banner link, click on the top right username > Sign out.
        """
        wf_home.signout_from_username_dropdown_menu()
        