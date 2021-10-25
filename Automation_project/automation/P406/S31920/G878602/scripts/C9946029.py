"""----------------------------------------------------
Author Name : Prabhakaran
Automated on : 25-June-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.lib.utillity import UtillityMethods
from common.wftools.wf_cloud_trail import WFCloudTrail
from common.lib.core_utility import CoreUtillityMethods

class C9946029_TestClass(BaseTestCase):
    
    def test_C9946029(self):
        
        """
            TESTCASE OBJECTS
        """
        
        CloudTrail = WFCloudTrail()
        utils = UtillityMethods(self.driver)
        
        """
            STEP 01 : Signin to email account
            STEP 02 : Verify "Your Personal WebFOCUS Environment is Ready" email was received
            STEP 03 : Verify email content
        """
        mail_subject = "Your Personal WebFOCUS Environment Is Ready"
        expected_content = "Your user ID is {0}".format(utils.parseinitfile('email_id'))
        html_content = CloudTrail.Email._get_email_html_content_(mail_subject, 1800)
        env_url = CloudTrail.Email._get_hyperlink_from_email_(html_content, 'Start My Trial')
        url = env_url.split("//")[-1].split("/")
        CoreUtillityMethods.update_config_file(self, 'nodeid', url[0])
        CoreUtillityMethods.update_config_file(self, 'wfcontext', "/" + url[1])
        CoreUtillityMethods.update_config_file(self, 'httpport', "")
        email_content = CloudTrail.Email._get_email_text_content_(html_content, 'body')
        utils.asin(expected_content, email_content, "Step 03.01 : Verify Your Personal WebFOCUS Environment is Ready email was received")
        wf_url = CloudTrail.Email._get_hyperlink_from_email_(html_content, 'Get WebFOCUS Resources')
        
        STEP_04 = """
            STEP 04 : Click on "Get WebFOCUS Resources" Link
        """
        self.driver.get(wf_url)
        utils.wait_for_page_loads(60, pause_time=10)
        utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify landing page
        """
        utils.asequal('WebFOCUS KnowledgeBase', self.driver.title, "STEP 07.01 : Verify Get WebFOCUS Resources page")
        utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_06 = """
            STEP 06 : Click on "Start My Trial"
        """
        self.driver.get(env_url)
        utils.synchronize_with_visble_text("#SignonbtnLogin", 'Sign in', 180)
        utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify WebFOCUS Cloud Sign in Page
        """
        utils.asequal("Sign in to WebFOCUS", self.driver.title, "Step 06.01 : Verify WebFOCUS Cloud Sign in Page")
        utils.capture_screenshot("06.01", STEP_06_01, True)