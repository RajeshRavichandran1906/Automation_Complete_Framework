"""----------------------------------------------------------------
Author Name : Prabhakaran M
Automated On : 04-August-2019 
----------------------------------------------------------------"""

from common.lib.core_utility import CoreUtillityMethods
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.login import Login

class C2321150_TestClass(BaseTestCase):

    def test_C2321150(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        
        """
            VARIABLES
        """
        domin_folder = "P292_S10660"
        group_folder = "G169275"
        content_area_css = ".files-box"
        banner_css = ".home-banner .banner-group-spacer"
        
        STEP_01 = """
            STEP 01 : Invoke WF Home Page as Developer user
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        homepage.select_content_from_sidebar()
        utils.synchronize_with_visble_text('.toolbar', 'Domains', homepage.home_page_long_timesleep)
        utils.capture_screenshot("01.01", STEP_01)
        
        STEP_02 = """
            STEP 01 : Under Domains >> Right click on domain "P292_S10660" from repository tree. 
            Verify under context menu user can see Expand/Collapse option from the repository tree
        """
        homepage.verify_repository_folder_context_menu(domin_folder, ['Collapse'], msg="Step 02.01", comparision_type='asin')
        utils.capture_screenshot("02.01", STEP_02, True)
        
        STEP_03 = """
            STEP 03 : Click on Domain Node >> Right click on domain "P292_S10660" from content area.
            Verify under context menu user can only see the Open option from the content area
        """
        banner = self.driver.find_element_by_css_selector(banner_css)
        core_utils.left_click(banner)
        homepage.expand_repository_folder("Domains")
        utils.synchronize_with_visble_text(content_area_css, domin_folder,  homepage.home_page_short_timesleep)
        homepage.verify_repository_folder_item_context_menu(domin_folder, ['Open'], msg="Step 03.01", comparision_type='asin')
        utils.capture_screenshot("03.01", STEP_03, True)
        
        STEP_04 = """
            STEP 04 : Under Domains >> Expand "P292_S10660" >> Right click on folder "G169275" from repository tree. 
            Verify under context menu user can see Expand/Collapse option from the repository tree.
        """
        folder_path = domin_folder + "->" + group_folder
        homepage.verify_repository_folder_context_menu(folder_path, ['Collapse'], msg="Step 04.01", comparision_type='asin')
        utils.capture_screenshot("04.01", STEP_04, True)
        
        STEP_05 = """
            STEP 05 : Click on Domain Node >> Open domain "P292_S10660" >> Right click on folder "G169275" from content area. 
            Verify under context menu user can only see the Open option from the content area.
        """
        banner = self.driver.find_element_by_css_selector(banner_css)
        core_utils.left_click(banner)
        homepage.expand_repository_folder(domin_folder)
        utils.synchronize_with_visble_text(content_area_css, group_folder,  homepage.home_page_short_timesleep)
        homepage.verify_repository_folder_item_context_menu(group_folder, ['Open'], msg="Step 05.01", comparision_type='asin')
        utils.capture_screenshot("05.01", STEP_05, True)
        
        STEP_06 = """
            STEP 06 : In the banner link, click on the top right username > Sign Out
        """
        homepage.signout_from_username_dropdown_menu()
        utils.capture_screenshot("06.01", STEP_06)