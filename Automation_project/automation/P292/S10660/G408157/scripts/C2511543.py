'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 02-AUGUEST-19
Test Case Title : Publish and Shown options are missing from list view
-----------------------------------------------------------------------------------------------------'''
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools.login import Login

class C2511543_TestClass(BaseTestCase):
    
    def test_C2511543(self):
        
        """ CLASS OBJECTS """  
        locator = WfMainPageLocators()
        homepage = Wf_Mainpage(self.driver)
        login = Login(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        login.invoke_home_page("mrid", "mrpass")
        
        """
            STEP 02 : Click Content View from the sidebar > Click on Domains from the resource tree
        """
        homepage.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, homepage.home_page_short_timesleep)
        
        """
            STEP 03 : Click toggle button to switch to List View.
        """
        homepage.select_list_view()
        utils.synchronize_with_visble_text(locator.content_area_css, "Title", homepage.home_page_short_timesleep)
        
        """
            STEP 04 : Click on Retail Sample domain.
        """
        homepage.click_repository_folder("Retail Samples")
        utils.synchronize_with_visble_text(locator.content_area_css, "Portal", homepage.home_page_medium_timesleep)
        
        """
            STEP 05 : Click on "Choose columns" button.
            Verify "Published" and "Shown" options appears in drop down list.
        """
        msg = "Step 05.01 : Verify 'Published' and 'Shown' options appears in drop down list"
        homepage.select_choose_columns_in_list_view()
        homepage.verify_choose_columns_context_menu_items(['Published', 'Shown'], msg, comparision_type='asin')
        homepage.select_grid_view()
        
        """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()