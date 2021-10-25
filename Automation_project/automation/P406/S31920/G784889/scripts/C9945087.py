"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 01-Sep-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.paris_home_page import ParisHomePage

class C9945087_TestClass(BaseTestCase):
    
    def test_C9945087(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User..
        """
        HomePage.invoke_with_login("mriddev", "mrpassdev")
        utils.wait_for_page_loads(100)
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the 'Help' icon in the banner link.
        """
        HomePage.Banner.click_help()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the following options are displayed:
            1.WebFocus Online Help
            2.Technical Resources
            3.Community
            4.About WebFOCUS
            5.License
            6.TIBCO Software Inc.
        """
        help_options = ['WebFOCUS Online Help', 'Technical Resources', 'Community', 'About WebFOCUS', 'License', 'TIBCO Software Inc.']
        HomePage.ContextMenu.verify(help_options, "02.01")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on 'WebFOCUS Online Help'
        """
        HomePage.ContextMenu.select("WebFOCUS Online Help")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_03_EXPECTED = """
            STEP 03 - Expected : Verify 'WebFOCUS Online Help' open in a new window without any issues
        """
        HomePage.Home._utils.asin("TIBCO WebFOCUS",self.driver.title, "Step 03.01 : Verify 'Help -' open in a new window without any issues")
        HomePage.Home._utils.asin("Online Help", self.driver.title,  "Step 03.01 : Verify 'Help -' open in a new window without any issues")
        HomePage.Home._core_utils.switch_to_frame("#indexFrameset frame[name='HelpFrame']")
        HomePage.Home._core_utils.switch_to_frame("#helpFrameset frame[name='NavFrame']")
        HomePage.Home._core_utils.switch_to_frame("#navFrameset frame[name='ViewsFrame']")
        HomePage.Home._core_utils.switch_to_frame("iframe[name='toc']")
        HomePage.Home._core_utils.switch_to_frame("#viewFrameset frame[name='tocViewFrame']")
        actual_text = self.driver.find_element_by_css_selector("a[title$='Online Help']").text.strip()
        HomePage.Home._utils.asin("TIBCO WebFOCUS", actual_text, "Step 03.02 : Verify 'Help -' open in a new window without any issues")
        HomePage.Home._utils.asin("Online Help", actual_text, "Step 03.02 : Verify 'Help -' open in a new window without any issues")
        HomePage.Home._utils.capture_screenshot("03 - Expected", STEP_03_EXPECTED, True)

        STEP_04 = """
            STEP 04 : Close the 'Help' window.
        """
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on 'Help' icon > Click on 'Technical Resources'.
        """
        HomePage.Banner.click_help()
        HomePage.ContextMenu.select("Technical Resources")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify 'WebFOCUS KnowledgeBase' open in a new window with the following URL: 
            'https://kb.informationbuilders.com'
        """
        tr_url = "https://kb.informationbuilders.com/"
        HomePage.Home._utils.asequal(tr_url, self.driver.current_url, "Step 05.01 : Verify 'WebFOCUS KnowledgeBase' open in a new window")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Close the 'WebFOCUS KnowledgeBase' window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on 'Help' icon > Click on 'Community'.
        """
        HomePage.Banner.click_help()
        HomePage.ContextMenu.select("Community")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the 'Information Builders Community|Information Builders' open in a new window with the following URL: 
            https://www.informationbuilders.com/support/wf_dev_center
        """
        community_url = "https://ibi.influitive.com/users/sign_in"
        HomePage.Home._utils.asequal(community_url, self.driver.current_url, "Step 07.01 : Verify the 'Information Builders Community' open in a new window")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Close the 'Information Builders Community|Information Builders' window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on 'Help' icon > Click on 'About WebFOCUS'.
        """
        HomePage.Banner.click_help()
        HomePage.ContextMenu.select("About WebFOCUS")
        HomePage.ModalDailogs.AboutWebFOCUS.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify 'About WebFOCUS' dialog opens with the following:
            1.Edition
            2.Product release
            3.Service pack
            4.Package name
            5.Release ID
            6.Build/GEN number
            7.Build/GEN date
            8.Application Server
        """
        labels = ['Edition', 'Product release', 'Service pack', 'Package name', 'Release ID', 'Build/GEN number', 'Build/GEN date', 'Application Server']
        HomePage.ModalDailogs.AboutWebFOCUS.verify_labels(labels, "09.01")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click 'OK' to Close the "About WebFOCUS" dialog..
        """
        HomePage.ModalDailogs.AboutWebFOCUS.OKButton.click()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on 'Help' icon > Click on 'License'.
        """
        HomePage.Banner.click_help()
        HomePage.ContextMenu.select("License")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify '3rd Party Information' open in a new window with the following URL: 
            http://machine_name:port/alias/licenseinfopage.jsp
        """
        license_url = "https://docs.tibco.com/products/tibco-ibi/license"
        HomePage.Home._utils.asequal(license_url, self.driver.current_url, "Step 11.01 : Verify '3rd Party Information' open in a new window")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the '3rd Party Information' window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click on 'Help' icon > Click on 'TIBCO Software Inc.'.
        """
        HomePage.Banner.click_help()
        HomePage.ContextMenu.select("TIBCO Software Inc.")
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify 'Business Intelligence and Data Management Software' open in a new window with the following URL: 
            https://www.tibco.com/
        """
        ibi_url = "https://www.tibco.com/"
        HomePage.Home._utils.asequal(ibi_url, self.driver.current_url, "Step 13.01 : Verify 'Business Intelligence and Data Management Software' open in a new window")
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Close the 'Business Intelligence and Data Management Software' window.
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)