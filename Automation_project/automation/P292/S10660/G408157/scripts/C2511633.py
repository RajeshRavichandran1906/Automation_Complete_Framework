'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 05-AUGUEST-19
Test Case Title : Sort on Published and Shown not working in Grid and List views
-----------------------------------------------------------------------------------------------------'''
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.core_utility import CoreUtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2511633_TestClass(BaseTestCase):
    
    def test_C2511633(self):
        
        """ CLASS OBJECTS """  
        locator = WfMainPageLocators()
        homepage = Wf_Mainpage(self.driver)
        login = Login(self.driver)
        utils = UtillityMethods(self.driver)
        coreutils = CoreUtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        expected_content_items1 = ['My Content', 'G408157_published', 'G408157_unpublished', 'Hidden Content', 'Publish and Hide', 'Unpublish and Show']
        expected_content_items2 = ['G408157_published', 'Hidden Content', 'My Content', 'G408157_unpublished', 'Publish and Hide', 'Unpublish and Show']
        published_title_css = ".files-box-files-title div[data-ibxp-text='Published']"
        list_view_files_css = ".files-listing:not([style*='none']) .files-box-files-row .grid-cell-data[title]"
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        login.invoke_home_page("mrid", "mrpass")
        
        """
            STEP 02 : Click Content View from the sidebar > Click on Domains from the resource tree.
            Click on "P292_S10660_G408157" from the tree.
        """
        homepage.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, homepage.home_page_short_timesleep)
        homepage.expand_repository_folder("P292_S10660_G408157")
        utils.synchronize_with_visble_text(locator.content_area_css, "G408157_published", homepage.home_page_medium_timesleep)
        
        """
            STEP 03 : Click toggle button to switch to List View.
            Verify sort:
            My Content
            G408157_published
            G408157_unpublished
            Hidden Content
            Publish and Hide
            Unpublish and Show
        """
        homepage.select_list_view()
        utils.synchronize_with_visble_text(locator.content_area_css, "Title", homepage.home_page_short_timesleep)
        actual_files = [file.text.strip() for file in self.driver.find_elements_by_css_selector(list_view_files_css)]
        utils.verify_list_values(expected_content_items1, actual_files, "Step 03.01 : Verify publish sort", "asin")
        
        """
            STEP 04 : Click Published heading to sort.
            Verify down arrow appears next to Published and sort is:
            G408157_published
            Hidden Content
            My Content
            G408157_unpublished
            Publish and Hide
            Unpublish and Show
        """
        published_title = self.driver.find_element_by_css_selector(published_title_css)
        coreutils.left_click(published_title)
        actual_files = [file.text.strip() for file in self.driver.find_elements_by_css_selector(list_view_files_css)]
        utils.verify_list_values(expected_content_items2, actual_files, "Step 04.01 : Verify publish sort", "asin")
        
        """
            STEP 05 : Click Published heading to sort again.
            Verify up arrow appears next to Published and sort is:
            My Content
            G408157_unpublished
            G408157_published
            Hidden Content
            Unpublish and Show
            Publish and Hide
        """
        published_title = self.driver.find_element_by_css_selector(published_title_css)
        coreutils.left_click(published_title)
        actual_files = [file.text.strip() for file in self.driver.find_elements_by_css_selector(list_view_files_css)]
        utils.verify_list_values(expected_content_items1, actual_files, "Step 05.01 : Verify publish sort", "asin")
        
        """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.select_grid_view()
        homepage.signout_from_username_dropdown_menu()