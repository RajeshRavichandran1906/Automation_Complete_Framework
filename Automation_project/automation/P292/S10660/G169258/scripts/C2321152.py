'''
Created on Sep 04, 2019

@author: Niranjan

Test case link: http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2321152
Test case name: Repository Tree:Verify Items change to Bright blue color when its selected.
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.locators.wf_mainpage_locators import WfMainPageLocators
import time

class C2321152_TestClass(BaseTestCase):

    def test_C2321152(self):
        
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
            STEP 02 : Click on "Domains" node.
        """
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
        
        main_page.expand_repository_folder("Domains")
        utils.capture_screenshot("02.01", Step2)
        
        Step3 = """
            STEP 03 : Select domain Retail_Samples under repository tree.
            Verify the selected domain will turn to bright blue color as an indication that it is selected.
        """
        main_page.expand_repository_folder("Domains->Retail Samples")
        time.sleep(15)
        retail_samples_obj = utils.validate_and_get_webdriver_object("div.ibx-widget div[class$='ibfs-item-selected']", "Retail Samples css")
        actual_result = retail_samples_obj.value_of_css_property("background-color")
        msg = "Step 03.01 : Verify the selected domain will turn to bright blue color as an indication that it is selected."
        utils.asequal("rgba(53, 184, 254, 0.4)", actual_result, msg)
        utils.capture_screenshot("03.01", Step3, expected_image_verify = True)
        
        Step4 = """
            STEP 04 : Under Retail_Samples domain >> Select sub-folder "Charts"
            Verify the selected folder will turn to bright blue color as an indication that it is selected.
        """
        main_page.expand_repository_folder("Domains->Retail Samples->Charts")
        time.sleep(15)
        charts_obj = utils.validate_and_get_webdriver_object("div.ibx-widget div[class$='ibfs-item-selected']", "chart css")
        actual_result = charts_obj.value_of_css_property("background-color")
        msg = "Step 04.01 : Verify the selected folder will turn to bright blue color as an indication that it is selected."
        utils.asequal("rgba(53, 184, 254, 0.4)", actual_result, msg)
        utils.capture_screenshot("04.01", Step4, expected_image_verify = True)
        
        Step5 = """
            STEP 05 : In the banner link, click on the top right username > Sign Out.
        """
        main_page.signout_from_username_dropdown_menu()
        utils.capture_screenshot("05.01", Step5)
 
if __name__ == '__main__':
    unittest.main()