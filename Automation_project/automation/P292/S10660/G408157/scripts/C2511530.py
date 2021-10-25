'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 02-AUGUEST-19
Test Case Title : List view: private item/folder icons need to reflect the grayscale effects
-----------------------------------------------------------------------------------------------------'''
from common.wftools.login import Login
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2511530_TestClass(BaseTestCase):
    
    def test_C2511530(self):
        
        """ CLASS OBJECTS """  
        locator = WfMainPageLocators()
        homepage = Wf_Mainpage(self.driver)
        login = Login(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        published_folder = "G408157_published"
        unpublished_folder = "G408157_unpublished"
        
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
            STEP 03 : Click on "P292_S10660_G408157" from the tree
            Verify that "G408157_unpublished" folder is in grey color and "G408157_published" folder is in yellow color.
        """
        homepage.click_repository_folder("P292_S10660_G408157")
        utils.synchronize_with_visble_text(locator.content_area_css, published_folder, homepage.home_page_short_timesleep)
        homepage.verify_content_area_folder_publish_or_unpublish(published_folder, "publish", "Step 03.01 : Verify that G408157_published folder is in yellow color")
        homepage.verify_content_area_folder_publish_or_unpublish(unpublished_folder, "unpublish", "Step 03.01 : Verify that G408157_unpublished folder is in grey color")
        
        """
            STEP 04 : Double click on "G408157_published" folder.
            Verify that two fexes are "Report2" (Unpublished is in grey color) and "Report1" (Published is in green color)
        """
        homepage.double_click_on_content_area_items(published_folder)
        utils.synchronize_with_visble_text(locator.content_area_css, "Report1", homepage.home_page_short_timesleep)
        homepage.verify_content_area_item_publish_or_unpublish("Report1", "publish", "Step 03.01 : Verify that Report1 fex is in yellow color")
        homepage.verify_content_area_item_publish_or_unpublish("Report2", "unpublish", "Step 03.01 : Verify that Report2 fex is in grey color")
        
        """
            STEP 05 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()