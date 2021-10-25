'''-------------------------------------------------------------------------------------------
Reworked on January 31, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288642
Test Case Title =  Add an Environment From Tree
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common import environment_configuration as EnvironmentConfiguration

class C2288642_TestClass(BaseTestCase):
    
    def test_C2288642(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01 : In Home ribbon, click Environments
            Click Add in the Environments List window
        """
        EnvironmentConfiguration.EnvironmentList.invoke_from_ribbon()
        EnvironmentConfiguration.EnvironmentList.click_on_add_button()
        
        """
            STEP 02.01 : Web Component Authentication section 
            STEP 02.01 Expected : Click Drop down next to None 
            STEP 02.02 : Click on any space in WebFOCUS Environment Properties
        """
        EXPECTED_AUTHENTICATION_LIST = ['None', 'IWA', 'Kerberos', 'SAML', 'CAS', 'Basic', 'Browser-based Login', 'ClearTrust', 'SiteMinder', 'WebSEAL', 'Oracle Access Manager']
        EnvironmentConfiguration.WebFocusEnvironmentProperties.verify_web_component_authentication_list(EXPECTED_AUTHENTICATION_LIST, '02.01')
        
        """
           STEP 02.01 : Click on X in WebFOCUS Environment Properties
        """
        EnvironmentConfiguration.WebFocusEnvironmentProperties.close()
        
if __name__=='__main__' :
    unittest.main()