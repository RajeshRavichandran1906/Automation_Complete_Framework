"""-------------------------------------------------------------------------------------------
Created on November 22, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2325151
Test Case Title =  Search folder - upper case 
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login
from common.locators import wf_mainpage_locators

class C2325151_TestClass(BaseTestCase):

    def test_C2325151(self):
        
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
        SHORT_WAIT_TIME= 60
            
        """
            STEP 01 : Sign in to WebFOCUS as Developer User.
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utlis.synchronize_with_visble_text(".left-main-panel .left-main-panel-content-button", 'Content', 120)
    
        """
            STEP 02 : Click on the Content tree from the sidebar.
        """
        wf_home.select_content_from_sidebar()
        
        """
            STEP 03 : Expand Domain > P292_S10660>G169261>Breadcrumb Trail and Search>Retail Samples > Click on "Visualizations" from the tree
        """
        wf_home.select_option_from_crumb_box("Workspaces")
        wf_home.expand_repository_folder('P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Visualizations')
        utlis.synchronize_with_visble_text(locator_obj.files_item_css, 'Analytical Dashboard', SHORT_WAIT_TIME)
        
        """
            STEP 04 : Click on the search text box and type 'DASH' in the search box.
        """
        utlis.wait_for_page_loads(5, 3, 3)
        wf_home.search_input_box_options(input_text_msg='DASH')
        utlis.synchronize_with_number_of_element(locator_obj.files_item_css, 2, SHORT_WAIT_TIME)
        
        """
            STEP 04.1 : Verify two reports (Analytical Dashboard and Executive Dashboard) are appears
        """
        wf_home.verify_items_in_grid_view(['Analytical Dashboard', 'Executive Dashboard'], 'as_List_equal', 'Step 04.01 : Verify two reports (Analytical Dashboard and Executive Dashboard) are appears')
        
        """
            STEP 05 : If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box.
            STEP 06 : Click X to clear the search box.
        """
        wf_home.search_input_box_options(option_type='clear')
        utlis.synchronize_with_visble_text(".create-new-box .ibx-tab-button", 'Common', SHORT_WAIT_TIME)
        
        """
            STEP 06.1 : Verify search box is cleared and "Search Visualizations" appears in the box
            STEP 07.0   : Or else for FF browser, use the backspace to clear the search box.
            STEP 07.1 : Verify search box is cleared and "Search Visualizations" appears in the box 
        """
        wf_home.verify_search_textbox_value('Search Visualizations', 'Step 06.01 : Verify search box is cleared and "Search Visualizations" appears in the box')
        
        """
            STEP 08 : Type 'DASH' in the search box
        """
        wf_home.search_input_box_options(input_text_msg='DASH')
        utlis.synchronize_with_number_of_element(locator_obj.files_item_css, 2, SHORT_WAIT_TIME)
        
        """
            STEP 08.1: Verify two reports (Analytical Dashboard and Executive Dashboard) are appears
        """
        wf_home.verify_items_in_grid_view(['Analytical Dashboard', 'Executive Dashboard'], 'as_List_equal', 'Step 08.01 : Verify two reports (Analytical Dashboard and Executive Dashboard) are appears')
        
        """
            STEP 09 : If it is chrome, IE 11 and Edge browsers, Hover over the mouse to the search box
            STEP 10 : Click X to clear the search box
        """
        wf_home.search_input_box_options(option_type='clear')
        utlis.synchronize_with_visble_text(".create-new-box .ibx-tab-button", 'Common', SHORT_WAIT_TIME)
        
        """"
            STEP 10.1 : Verify search box is cleared and "Search Visualizations" appears in the box
            STEP 11 : Or else for FF browser, use the backspace to clear the search box
            STEP 11.1 : Verify search box is cleared and "Search Visualizations" appears in the box
        """
        wf_home.verify_search_textbox_value('Search Visualizations', 'Step 11.01 : Verify search box is cleared and "Search Visualizations" appears in the box')
         
        """
            STEP 12 : In the banner link, click on the top right username > Sign out.
        """
        wf_home.signout_from_username_dropdown_menu()
        