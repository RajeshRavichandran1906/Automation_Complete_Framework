"""---------------------------------------------------------------------------------
Author Name : Prabhakaran.
Automated Date : 19-August-19
---------------------------------------------------------------------------------"""
import unittest, time
from common.wftools.login import Login
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_mainpage import Wf_Mainpage

class C6467932_TestClass(BaseTestCase):

    def test_C6467932(self):
        
        """ CLASS OBJECT """
        homepage = Wf_Mainpage(self.driver)
        loginpage = Login(self.driver)
        utils = UtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        retail_samples = "Retail Samples"
        toolbar_css = ".toolbar .crumb-box"
        repository_css = "div[class='ibfs-tree']"
        
        def verify_toolbar_title(step_num):
            expected_toolbar = "Portals"
            actual_toolbar = self.driver.find_element_by_css_selector(toolbar_css).text.strip()
            msg = "Step {0} : Verify the Portal view refreshes but does not jump to the Content View".format(step_num)
            utils.asequal(expected_toolbar, actual_toolbar, msg)
            
        """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User
        """
        loginpage.invoke_home_page('mrid', 'mrpass')
        
        """
            STEP 02 : Click Portals from the sidebar.
        """
        homepage.select_portals_from_sidebar()
        utils.synchronize_with_visble_text(toolbar_css, "Portals", homepage.home_page_medium_timesleep, pause_time=4)
         
        """
            STEP 03 : Right click on 'Retail_Samples' portal > Select 'Unpublish'.
            Verify the Portal view refreshes but does not jump to the Content View.
        """
        time.sleep(15)#giving time for loading to take place
        utils.wait_for_page_loads(homepage.home_page_medium_timesleep)
        homepage.right_click_folder_item_and_select_menu(retail_samples, "Unpublish", item_name_index=5)
        utils.wait_for_page_loads(homepage.home_page_medium_timesleep)
        homepage.verify_content_area_item_publish_or_unpublish(retail_samples, 'unpublish', 'Step 03.00: Verify Retail Samples is unpublished.', index=5)
        verify_toolbar_title("03.01")
         
        """
            STEP 04 : Right click on 'Retail_Samples' portal > Select 'Publish'.
            Verify the Portal view refreshes but does not jump to the Content View.
        """
        homepage.right_click_folder_item_and_select_menu(retail_samples, "Publish", item_name_index=5)
        utils.wait_for_page_loads(homepage.home_page_medium_timesleep)
        homepage.verify_content_area_item_publish_or_unpublish(retail_samples, 'publish', 'Step 04.00: Verify Retail Samples is published.', index=5)
        verify_toolbar_title("04.01")
        
        """
            STEP 05 : Right click on 'Retail_Samples' portal > Select 'Hide'.
            Verify the Portal view refreshes but does not jump to the Content View.
        """
        utils.wait_for_page_loads(homepage.home_page_medium_timesleep)
        homepage.right_click_folder_item_and_select_menu(retail_samples, "Hide", item_name_index=5)
        utils.wait_for_page_loads(homepage.home_page_medium_timesleep)
        homepage.verify_content_area_item_shown_or_hide(retail_samples, 'hide', 'Step 05.00: Verify Retail Samples is Hide.', index=5)
        verify_toolbar_title("05.01")
        
        """
            STEP 06 : Right click on 'Retail_Samples' portal > Select 'Show'
            Verify the Portal view refreshes but does not jump to the Content View.
        """
        utils.wait_for_page_loads(homepage.home_page_medium_timesleep)
        homepage.right_click_folder_item_and_select_menu(retail_samples, "Show", item_name_index=5)
        utils.wait_for_page_loads(homepage.home_page_medium_timesleep)
        homepage.verify_content_area_item_shown_or_hide(retail_samples, 'shown', 'Step 06.00: Verify Retail Samples is Shown.', index=5)
        verify_toolbar_title("06.01")
        homepage.select_content_from_sidebar()
        utils.synchronize_until_element_is_visible(repository_css, homepage.home_page_medium_timesleep)
        
        """
            STEP 07 : In the banner link, click on the top right username > Click Sign Out.
        """
        homepage.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()  