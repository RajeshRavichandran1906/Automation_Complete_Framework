"""----------------------------------------------------
Author Name : Prabhakaran
Automated on : 23-June-2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.wf_cloud_trail import WFCloudTrail

class C9946027_TestClass(BaseTestCase):
    
    def test_C9946027(self):
        
        """TESTCASE OBJECTS"""
        
        CloudTrail = WFCloudTrail()
        
        """
            STEP 01 : Signin to email account
            STEP 02 : Verify Email 14 Day WebFOCUS Cloud Analytics Trial Email response from IBI (Kathy Drago)
            STEP 03 : Verify contents of WebFOCUS Cloud Analytics Trial Email
        """
        CloudTrail.Email.verify_content_of_wf_cloud_trial_email('03.01')