"""----------------------------------------------------
Author Name : Prabhakaran
Automated on : 22-June-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_cloud_trail import WFCloudTrail

class C9946026_TestClass(BaseTestCase):
    
    def test_C9946026(self):
        
        """TESTCASE OBJECTS"""
        
        CloudTrail = WFCloudTrail()
        
        
        STEP_01 = """
            STEP 01 : Access IBI Cloud Analytics (Dev) Trial Page
        """
        CloudTrail.Registation.invoke_page()
        CloudTrail.Registation._utils_.capture_screenshot('01.00', STEP_01)
        
        STEP_01_01 = """
            STEP 01.01 : Verify the following page is displayed
        """ 
        title = "WebFOCUS Free 14-Day Cloud Trial | Information Builders"
        CloudTrail.Registation._utils_.asequal(title, self.driver.title, "Step 01.01 : Verify IBI Cloud Analytics (Dev) Trial Page displayed")
        CloudTrail.Registation._utils_.capture_screenshot('01.01', STEP_01_01, True)
        
        STEP_02 = """
            STEP 02.00 : Click on "See What You Can Build" Button w/out entering any form values
        """
        CloudTrail.Registation.Submit._object_.click()
        CloudTrail.Registation._utils_.capture_screenshot('02.00', STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify msg requiring field values to be entered
        """
        CloudTrail.Registation.State.ErrorMessage.verify_text('State is required.', '02.01')
        CloudTrail.Registation.FirstName.ErrorMessage.verify_text('First Name is required.', '02.02')
        CloudTrail.Registation.LastName.ErrorMessage.verify_text('Last Name is required.', '02.03')
        CloudTrail.Registation.Email.ErrorMessage.verify_text('Email is required.', '02.04')
        CloudTrail.Registation.JobTitle.ErrorMessage.verify_text('Job Title is required.', '02.05')
        CloudTrail.Registation.Company.ErrorMessage.verify_text('Company is required.', '02.06')
        CloudTrail.Registation.TermsConditions.ErrorMessage.verify_text('Please accept the terms and conditions', '02.07')
        CloudTrail.Registation._utils_.capture_screenshot('02.01', STEP_02_01, True)
        