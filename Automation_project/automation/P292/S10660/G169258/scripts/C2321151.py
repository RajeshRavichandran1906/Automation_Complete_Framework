'''
Created on Sep 04, 2019

@author: Prabhakaran

Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2321151
Test case name: Repository Tree:Verify Double click on folders from Tree will expand/Collapse folder.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
import time

class C2321151_TestClass(BaseTestCase):

    def test_C2321151(self):
        
        """
        CLASS OBJECTS
        """
        login = Login(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        locator = WfMainPageLocators()


        Step1 = """
            STEP 01 : Invoke WF Home Page as Developer user.
        """
        login.invoke_home_page("mriddev", "mrpassdev")
        utils.synchronize_with_visble_text(locator.CONTENT_CSS, "Content", main_page.home_page_long_timesleep)
        utils.capture_screenshot("01.01", Step1)
        
        Step2 = """
            STEP 02 : Click on Domains node.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        main_page.select_option_from_crumb_box("Domains")
        time.sleep(15)
        utils.capture_screenshot("02.01", Step2)
        
        Step3 = """
            STEP 03 : Under Repository tree >> Double click on "Retail_Samples" domain.
            Verify the domain folder will be Expanded & the contents underneath it are displayed under repository tree.
        """
        content_list = ['My Content', 'Charts', 'Documents', 'InfoApps', 'Mobile', 'Portal', 'Reports', 'Search', 'Visualizations', 'Hidden Content']
        main_page.expand_repository_folders_and_verify("Domains->Retail Samples", content_list, "Step 03.01 : Verify the domain folder will be Expanded & the contents underneath it are displayed under repository tree.")
        utils.capture_screenshot("03.01", Step3, expected_image_verify = True)

        Step4 = """
            STEP 04 : From Repository tree >> Again double click on "Retail_Samples" domain.
            Verify the domain folder will be Collapsed & the contents underneath wont be displayed under repository tree.
        """
        main_page.collapse_repository_folders_and_verify("Retail Samples", content_list, "Step 04.01 = Verify the domain folder will be Collapsed & the contents underneath wont be displayed under repository tree.", comparion_type="asnotin")
        utils.capture_screenshot("04.01", Step4, expected_image_verify = True)
        
        Step5 = """
            STEP 05 : In the banner link, click on the top right username > Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        utils.capture_screenshot("05.01", Step5)
        
if __name__ == '__main__':
    unittest.main()
