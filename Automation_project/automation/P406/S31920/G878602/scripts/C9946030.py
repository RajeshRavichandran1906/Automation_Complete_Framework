"""----------------------------------------------------
Author Name : Robert
Automated on : 22 June 2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.utillity import UtillityMethods, core_utilobj

from datetime import date, timedelta

class C9946030_TestClass(BaseTestCase):
    
    def test_C9946030(self):
        
        
        """TESTCASE SPECIFIC FUNCTIONS"""
        
        def return_new_date_with_days(noofdays):
            today = date.today()
            new_date=timedelta(days=noofdays)+today
            new_date_formatted=new_date.strftime("%Y-%m-%d")
            return(new_date_formatted)

        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = core_utilobj(self.driver)
        
        """TESTCASE VARIABLES"""
        
        LICENCE_MSG_CSS="div.post-message-text .ibx-label-text"
        USER_NAME_CSS = "div.hpreboot-top-bar [title ='User']"
        USER_NAME= core_utils.parseinitfile('mrid')
        NO_OF_DAYS=14
        LICENCE_MSG="License key will expire in 14 days on "+return_new_date_with_days(NO_OF_DAYS)
        
        STEP_01 = """
        Step 01.SignIn to WebFOCUS Cloud Trial with Registration Email
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Step 02.Verify License Expiration in 13 days
        """
        
        utils.verify_element_text(LICENCE_MSG_CSS, LICENCE_MSG, msg="Step 02 : Verify Licence Expiration message for 13 days")
        utils.capture_screenshot('02.00',STEP_02,expected_image_verify=True)
        
        STEP_03 = """Verify Expiration day is exactly 14 days after Environment is made available
        """
        utils.verify_element_text(LICENCE_MSG_CSS, LICENCE_MSG, msg="Step 03 : Verify Expiration day is exactly 14 days after Environment is made available")
        utils.capture_screenshot('03.00',STEP_03,expected_image_verify=True)

        STEP_04 = """Verify Email ID is displayed for user Logged in
        """
        utils.verify_element_text(USER_NAME_CSS, USER_NAME, msg="Step 04 : Verify Email ID is displayed for user Logged in")
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """
        Step 5 In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('05.00',STEP_05)