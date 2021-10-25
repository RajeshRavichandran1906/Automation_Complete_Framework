'''-------------------------------------------------------------------------------------------
Reworked on February 04, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288655
Test Case Title =  Environment Properties Client Path
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environment_configuration import EnvironmentList
from appstudio.tools.common.environment_configuration import WebFocusEnvironmentProperties

class C2288655_TestClass(BaseTestCase):
    
    def test_C2288655(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
        COMMON VARIABLE :
        """
        EXPECTED_ALERT_MSG = 'Please provide the client path value, or check the "Use Default" button'
        
        """
            STEP 01.01 : In Home ribbon, click Environments
        """
        EnvironmentList.invoke_from_ribbon()
        
        """
            STEP 01.02 : Select an environment and click Properties
        """
        EnvironmentList.select_configured_environment()
        EnvironmentList.click_on_properties_button()
        
        """
            STEP 01.03 : Uncheck Use Default. Delete Client Path value. Click OK in WebFocus Environment properties.
        """
        WebFocusEnvironmentProperties.uncheck_option(WebFocusEnvironmentProperties.Locators.WebComponentTab.UseDefault)
        WebFocusEnvironmentProperties.clear_textbox(WebFocusEnvironmentProperties.Locators.WebComponentTab.ClientPath)
        WebFocusEnvironmentProperties.click_on_ok_button()
       
        """
            STEP 01 Expected : Message displays 'Please provide the client path value, or check the "Use Default" button
        """
        WebFocusEnvironmentProperties.verify_alert_window_message(EXPECTED_ALERT_MSG, '01.01')
        
        """
            STEP 02 : Click OK in Message prompt. Click Cancel
            Click Cancel in Environments List window
        """
        WebFocusEnvironmentProperties.click_on_ok_button_in_alert_window()
        WebFocusEnvironmentProperties.click_on_cancel_button()
        EnvironmentList.click_on_cancel_button()
        
if __name__=='__main__' :
    unittest.main()