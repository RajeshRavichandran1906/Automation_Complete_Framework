"""----------------------------------------------------
Author Name : Robert
Automated on : 04 Aug 2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.utillity import UtillityMethods
from common.wftools.wf_cloud_trail import WFCloudTrail

class C9946801_TestClass(BaseTestCase):
    
    def test_C9946801(self):
        
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        CloudTrail = WFCloudTrail()

        """TESTCASE SPECIFIC FUNCTIONS"""
        
        def verify_email_from_invited_users(step_num, wait_time=300):
            
            mail_sub = "Welcome to WebFOCUS Trial"
            expected_msg = "WebFOCUS is an all-in-one, easy-to-use tool for creating and sharing reports"
            html_content = CloudTrail.Email._get_email_html_content_(mail_sub, wait_time)
            hyperlink = CloudTrail.Email._get_hyperlink_from_email_(html_content, 'GO TO ACCOUNT SET UP')
            actual_msg = CloudTrail.Email._get_email_text_content_(html_content, 'body')
            msg = "Step {0} : Verify your e-mail to start your WebFOCUS Cloud Trial".format(step_num)
            HomePage.Home._utils.asin(expected_msg,actual_msg,msg)
            return hyperlink
        
        
        """TESTCASE VARIABLES"""
        INVITE_USER1_FNAME    = HomePage.Home._core_utils.parseinitfile('invite_user1_first_name')
        INVITE_USER1_LNAME    = HomePage.Home._core_utils.parseinitfile('invite_user1_last_name')
        INVITE_USER1_EMAIL    = HomePage.Home._core_utils.parseinitfile('invite_user1_email')
        INVITE_USER2_FNAME    = HomePage.Home._core_utils.parseinitfile('invite_user2_first_name')
        INVITE_USER2_LNAME    = HomePage.Home._core_utils.parseinitfile('invite_user2_last_name')
        INVITE_USER2_EMAIL    = HomePage.Home._core_utils.parseinitfile('invite_user2_email')
        
        STEP_01 = """
        Step 01 : Log into the Cloud or a machine where this feature is configured
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Step 02 : Click on the Invite button
        """
        HomePage.Banner.click_invite_user()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_02_01 = """
        Step 02.01 : Verify invite user dialog opens up
        """
        utils.synchronize_with_visble_text(".pop-top[role*='dialog'] .ibx-title-bar-caption", "Invite users from your organization to the trial", 60)
        HomePage.ModalDailogs.InviteUser.verify_title("Invite users from your organization to the trial", "02.01")
        utils.capture_screenshot('02.01',STEP_02_01,expected_image_verify=True)
        
        STEP_03 = """
        STEP 03.00 : enter a first name and last name
        """
        HomePage.ModalDailogs.InviteUser.FirstName.enter_text(INVITE_USER1_FNAME)
        HomePage.ModalDailogs.InviteUser.LastName.enter_text(INVITE_USER1_LNAME)
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_04 = """
        STEP 04.00 : enter a valid email address
        """
        HomePage.ModalDailogs.InviteUser.BusinessEmail.enter_text(INVITE_USER1_EMAIL)
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """Click the Invite button
        """
        HomePage.ModalDailogs.InviteUser.InviteButton.click()
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        STEP 05.01 : The dialog will remain
        """
        HomePage.ModalDailogs.InviteUser.verify_title("Invite users from your organization to the trial", "05.01")
        invite_msg_txt_css = "div.invite-form-fill-error-text"
        HomePage.Home._utils.verify_element_text(invite_msg_txt_css, "Invite successfully sent.", msg="Step 05.01 : Verify invite successfully sent msg")
        utils.capture_screenshot('05.01',STEP_05_01, True)
        
        STEP_06 = """
        STEP 06.00 : Go to the email address you used for the invite
        """
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_06_01 = """
        STEP 06.01 : verify you get an email invite stating Welcome to WebFOCUS Trial
        """
        invite_link = verify_email_from_invited_users("06.01", wait_time=300)
        utils.capture_screenshot('06.01',STEP_06_01, True)
        
        STEP_07 = """
        STEP 07.00 : There should be a big button GO TO ACCOUNT SETUP
        """
        HomePage.Home._utils.asin("http",invite_link, "Step 07.02 : Verify email with big button Go To Account Setup")
        utils.capture_screenshot('07.00',STEP_07)
        
        STEP_08 = """
        STEP 08.00 : Click that button
        """
        self.driver.get(invite_link)
        HomePage.Home._utils.wait_for_page_loads(30)
        utils.synchronize_with_visble_text("div.dm-header", "Account Setup", 60)
        utils.capture_screenshot('08.00',STEP_08)
        
        STEP_08_01 = """
        STEP 08.01 : Verify WF account setup page loaded
        """
        HomePage.Home._utils.verify_element_text("div.dm-header", "Account Setup", "Step 08.01 : Verify Account Setup is loaded")
        utils.capture_screenshot('08.01',STEP_08_01, True)
        
        STEP_09 = """
        STEP 09.00 : enter a password/confirm password then continue
        """ 
        password = utils.parseinitfile('mrpass')
        self.driver.find_element_by_id("NewPassName").send_keys(password)
        self.driver.find_element_by_id("ConfirmPassName").send_keys(password)
        self.driver.find_element_by_id("ChgPwdbtnLogin").click()
        utils.capture_screenshot('09.00',STEP_09)
        
        STEP_09_01 = """
        STEP 09.01 : You should be logged into WF
        """
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.verify_top_bar_menus_title(['My Workspace', 'Shared with Me', 'Workspaces', 'Invite User', 'Utilities', 'Help', 'User'], "09.01", "asin")
        utils.capture_screenshot('09.01',STEP_09_01, True)
        
        
        STEP_10 = """
        STEP 10.00 : With this Invited user, invite another account and repeat steps 6-9.
        """
        HomePage.Banner.click_invite_user()
        utils.synchronize_with_visble_text(".pop-top[role*='dialog'] .ibx-title-bar-caption", "Invite users from your organization to the trial", 60)
        HomePage.ModalDailogs.InviteUser.verify_title("Invite users from your organization to the trial", "10.00")
        HomePage.ModalDailogs.InviteUser.FirstName.enter_text(INVITE_USER2_FNAME)
        HomePage.ModalDailogs.InviteUser.LastName.enter_text(INVITE_USER2_LNAME)
        HomePage.ModalDailogs.InviteUser.BusinessEmail.enter_text(INVITE_USER2_EMAIL)
        HomePage.ModalDailogs.InviteUser.InviteButton.click()
        utils.capture_screenshot('10.00',STEP_10)
        
        STEP_10_01 = """
        STEP 10.01 : The dialog will remain
        """
        HomePage.ModalDailogs.InviteUser.verify_title("Invite users from your organization to the trial", "10.01")
        invite_msg_txt_css = "div.invite-form-fill-error-text"
        HomePage.Home._utils.verify_element_text(invite_msg_txt_css, "Invite successfully sent.", msg="Step 10.01 : Verify invite successfully sent msg")
        utils.capture_screenshot('10.01',STEP_10_01, True)
        
        STEP_10_02 = """
        STEP 10.02 : Verify invite email and a big button GO TO ACCOUNT SETUP. Click on that button. Verify WF account setup page is loaded
        """
        invite_link = verify_email_from_invited_users("10.02", wait_time=300)
        HomePage.Home._utils.asin("http",invite_link, "Step 10.02 : Verify email with big button Go To Account Setup" )
        self.driver.get(invite_link)
        utils.synchronize_with_visble_text("div.dm-header", "Account Setup", 60)
        HomePage.Home._utils.verify_element_text("div.dm-header", "Account Setup", "Step 10.02 : Verify Account Setup is loaded")
        utils.capture_screenshot('10.02',STEP_10_02, True)
        
        STEP_10_03 = """
        STEP 10.03 : enter a password/confirm password then continue, you should be logged into WF
        """ 
        password = utils.parseinitfile('mrpass')
        self.driver.find_element_by_id("NewPassName").send_keys(password)
        self.driver.find_element_by_id("ConfirmPassName").send_keys(password)
        self.driver.find_element_by_id("ChgPwdbtnLogin").click()
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.verify_top_bar_menus_title(['My Workspace', 'Shared with Me', 'Workspaces', 'Invite User', 'Utilities', 'Help', 'User'], "11.01", "asin")

        utils.capture_screenshot('10.03',STEP_10_03, True)
        
        STEP_11 = """
        Step 11 In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('11.00',STEP_11)