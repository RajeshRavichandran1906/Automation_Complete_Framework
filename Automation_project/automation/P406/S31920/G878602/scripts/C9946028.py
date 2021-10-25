"""----------------------------------------------------
Author Name : Prabhakaran
Automated on : 24-June-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.wf_cloud_trail import WFCloudTrail

class C9946028_TestClass(BaseTestCase):
    
    def test_C9946028(self):
        
        """
            TESTCASE OBJECTS
        """
        
        CloudTrail = WFCloudTrail()
        utils = UtillityMethods(self.driver)
        emailid = utils.parseinitfile('email_id')
        cloud_provider = utils.parseinitfile('cloud_provider')
        
        """
            CSS SELECTORS
        """
        form = "#mainForm"
        us_east_radio_btn_css = "table[id^='mainForm:'] td:nth-child(1) span.ui-icon-blank"
        
        """
            STEP 01 : Signin to email account
            STEP 02 : Verify Email to Start the WebFOCUS Cloud Trial
            STEP 03 : Verify content of Email to Start the WebFOCUS Cloud Trial
        """
        verification_link = CloudTrail.Email.verify_email_to_start_wf_cloud_trail('03.01')
        
        STEP_04 = """
            STEP 04 : Click on Verify your Email Link
        """
        self.driver.get(verification_link)
        utils.synchronize_with_visble_text(form, emailid, 60)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 ="""
            STEP 04.01 : Verify the WebFOCUS Cloud Trial Confirmation page
        """
        actual_text = self.driver.find_element_by_css_selector(form).text
        utils.asin(emailid, actual_text, "STEP 04.01 : Verify the WebFOCUS Cloud Trial Confirmation page")
        utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Enter Password & Re-enter Password for "QA" Email used during registration
        """
        try:
            if cloud_provider == "aws":
                if self.driver.find_element_by_css_selector(us_east_radio_btn_css).is_displayed():
                    self.driver.find_element_by_css_selector(us_east_radio_btn_css).click()
        except:
            pass
            
        password = utils.parseinitfile('mrpass')
        self.driver.find_element_by_id("mainForm:pw1").send_keys(password)
        self.driver.find_element_by_id("mainForm:pw2").send_keys(password)
        utils.capture_screenshot("05.00", STEP_05)
        
        STEP_06 = """
            STEP 06 : Click Submit
        """
        content_css = "div[id^='mainForm']>table"
        
        self.driver.find_element_by_id("mainForm:btnEas2").click()
            
        utils.wait_for_page_loads(60)
        utils.synchronize_with_visble_text(content_css, emailid, 60)
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify Cloud Environment Setup Confirmation
        """
        actual_content = self.driver.find_element_by_css_selector(content_css).text.replace("\n", " ")
        expected_content = "Thank you. You will receive an e-mail within one hour"
        utils.asin(expected_content, actual_content, "STEP 06.01 : Verify Cloud Environment Setup Confirmation")
        utils.capture_screenshot("06.01", STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Click on "WebFOCUS KnowledgeBase" Link
        """
        css = content_css + " a[href*='kb.information']"
        self.driver.find_element_by_css_selector(css).click()
        utils.wait_for_page_loads(60, pause_time=10)
        utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify landing page
        """
        utils.asequal('WebFOCUS KnowledgeBase', self.driver.title, "STEP 07.01 : Verify landing page")
        utils.capture_screenshot("07.01", STEP_07_01, True)
        self.driver.close()