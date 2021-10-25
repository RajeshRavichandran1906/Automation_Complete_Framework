"""----------------------------------------------------
Author Name : Prabhakaran
Automated on : 04-August-2020
----------------------------------------------------"""

from common.lib.utillity import UtillityMethods
import requests
import unittest

class C9946809_TestClass(unittest.TestCase):
    
    def test_C9946809(self):
        
        """
        TEST CASE VARIABLES
        """
        email_id = UtillityMethods.parseinitfile(self, 'email_id')
        instance_type = UtillityMethods.parseinitfile(self, 'instance_type').lower()
        if instance_type == "prod":
            remove_url = "https://ibapps.informationbuilders.com/salesforceClient/rest/trialController/remove"
        
        elif instance_type == "test":
            remove_url = "http://xsftest.ibi.com/salesforceClient/rest/trialController/remove"
        
        else:
            raise KeyError("Invalid instance type")
        
        """
            STEP 01 : Run the endpoint request to delete the Trial User using the necessary parameters.
            (test)http://xsftest.ibi.com/salesforceClient/rest/trialController/remove
            (production) https://ibapps.informationbuilders.com/salesforceClient/rest/trialController/remove
            JSON parameters: (use the Trial user info found in the link provided in Preconditions for the email used for registration)
            {
            "contEmail" : "user@domain.com" ,
            "featureCode" : "WCT"
            }
            authentication id / password (required for deletion)
            marketing : NWEyMjk0NmI0OGExOWEwY2E1OTk5NTE1
        """
        
        """ Remove the actual cloud trial """
        remove_data = {"contEmail" : email_id, "featureCode" : "WCT"} 
        response = requests.post(remove_url, json=remove_data, auth=("marketing", "NWEyMjk0NmI0OGExOWEwY2E1OTk5NTE1")) 
       
        """
            STEP 01.01 : Check the status message for Success.
        """
        expected_status =  "WebFOCUS trial removal SUCCESS for {0}".format(email_id)
        self.assertIn(expected_status, response.text, "Step 01.01 : Verify the WF trial removal status message for Success")
        