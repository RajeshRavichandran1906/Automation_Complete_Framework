"""----------------------------------------------------
Author Name : Prabhakaran
Automated on : 04-August-2020
----------------------------------------------------"""

from common.lib.core_utility import CoreUtillityMethods
import requests
import unittest

class C9946808_TestClass(unittest.TestCase):
    
    def test_C9946808(self):
        
        """
        TEST CASE VARIABLES
        """
        email_id = CoreUtillityMethods.parseinitfile(self, 'email_id')
        instance_type = CoreUtillityMethods.parseinitfile(self, 'instance_type').lower()
        if instance_type == "prod":
            create_url = "https://ibapps.informationbuilders.com/salesforceClient/rest/trialController/"
        elif instance_type == "test":
            create_url = "http://xsftest.ibi.com/salesforceClient/rest/trialController/"
        else:
            raise KeyError("Invalid instance type")
        
        """
            STEP 01 : Run the endpoint request to create the Trial User using the necessary parameters.
            (test) http://xsftest.ibi.com/salesforceClient/rest/trialController/
            (production) https://ibapps.informationbuilders.com/salesforceClient/rest/trialController/
            JSON parameters (use the Trial user info found in the link provided in Preconditions for the first 5 values)
            {
            "companyName" : "Big Picture Big Sound",
            "lastName" : "IBIQA",
            "firstName" : "AutoCloud0",
            "title" : "Developer",
            "contEmail" : "todaro3@todaro3.com",
            "state" : "NY",
            "countryCode" : "US",
            "featureCode" : "WCT",
            "sfCampaignId" : "7011K000001pzIPQAY",
            "sfLeadId" : "I",
            "sfContactId": "",
            "contactOID" : "",
            "sendEmail" : "Y",
            "language" : "en",
            "mode" : ""
            }
        """
        create_data  = {
            "companyName" : "IBI",
            "lastName" : "RSCloud",
            "firstName" : "IBIQA",
            "title" : "Auto QA",
            "contEmail" : email_id,
            "state" : "NY",
            "countryCode" : "US",
            "featureCode" : "WCT",
            "sfCampaignId" : "7011K000001pzIPQAY",
            "sfLeadId" : "I",
            "sfContactId": "",
            "contactOID" : "",
            "sendEmail" : "Y",
            "language" : "en",
            "mode" : ""
        }
        response = requests.post(create_url, json=create_data) 
        CoreUtillityMethods.update_config_file(self, 'mrid', email_id)
        
        """
            STEP 01.01 : Check the status message for Success.
        """
        expected_status =  "Trial request SUCCESS: E-mail={0}".format(email_id)
        self.assertIn(expected_status, response.text, "Step 01.01 : Verify the status message for Success")
        