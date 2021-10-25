"""----------------------------------------------------
Author Name : Robert
Automated on : 16-December-2020
----------------------------------------------------"""

from common.lib.utillity import UtillityMethods
import requests
import unittest
import json

class C9950350_TestClass(unittest.TestCase):
    
    def test_C9950350(self):
        
        """
        TEST CASE VARIABLES
        """
        instance_type = UtillityMethods.parseinitfile(self, 'instance_type').lower()
        if instance_type == "prod":
            sf_token_url = "https://login.salesforce.com/services/oauth2/token?username=webqa@ibi.com&password=Plaza1!@!&grant_type=password&client_id=3MVG9szVa2RxsqBbRKU.pdk6PSFtk77UOCs3EldyrbMMmR_38Y._rqldDewGPPezRfTCCbewNTSUcZ2L1u.DG&client_secret=0F9A0C00AEF887771A4C8271B12625DBCFB0D0FA34F4E86D860CC90EDEB94DE9"
            sf_delete_leads_url ="https://ibi.my.salesforce.com/services/apexrest/deleteLeads"
        
        elif instance_type == "test":
            sf_token_url = "https://test.salesforce.com/services/oauth2/token?username=webqcs@ibi.com.partial&password=Plaza1!@!&grant_type=password&client_id=3MVG9PG9sFc71i9niSy3spF8Y.us0aRbVCUtPA74GBe8MYFXPUpifQL.ECt8KKJy9hnRV_kHnDtzs1iSginP.&client_secret=07692C52280E7983332707B9C25890B1FFCEE42491AC5E7D358A572CDC2A8117"
            sf_delete_leads_url ="https://ibi--partial.my.salesforce.com/services/apexrest/deleteLeads"
        
        else:
            raise KeyError("Invalid instance type")
        
        """
            STEP 01 : Run the POST authorization request to retrieve the bearer token.
            Use the Bearer token in a DELETE request to delete it from Sales Force which inturn deletes it from WP
        """
        
        """ Get authorization token and delete from Salesforce"""
        response = requests.post(sf_token_url) 
        resp=response.text
        token_dict = json.loads(resp)
        access_token = token_dict['access_token']
        hed = {'Authorization': 'Bearer ' + access_token}
        del_status_text = requests.delete(sf_delete_leads_url, headers = hed)
        expected_code = "200"
        
        self.assertEqual(expected_code, str(del_status_text.status_code), "Step 01.01 : Verify the Sales force delete status code")
        
