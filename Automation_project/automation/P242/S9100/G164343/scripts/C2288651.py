'''-------------------------------------------------------------------------------------------
Reworked on February 01, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288651
Test Case Title =  Properties Description Blank 
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environment_configuration import EnvironmentList
from appstudio.tools.common.environment_configuration import WebFocusEnvironmentProperties

class C2288651_TestClass(BaseTestCase):
    
    def test_C2288651(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
        COMMON VARIABLE :
        """
        EXPECTED_ALERT_MSG = 'Please provide a description for this environment'
        
        """
            STEP 01 : In Home ribbon, click on Environments. Select an environment in the Environments List dialog
        """
        EnvironmentList.invoke_from_ribbon()
        EnvironmentList.select_configured_environment()
        EnvironmentList.click_on_properties_button()
        
        """
            STEP 02  : In WebFOCUS Environment Properties. Delete Description value and leave description blank 
            Click OK
        """
        WebFocusEnvironmentProperties.clear_textbox(WebFocusEnvironmentProperties.Locators.Description)
        WebFocusEnvironmentProperties.click_on_ok_button()
        
        """
            STEP 02 Expected : OK button is disabled
        """
        WebFocusEnvironmentProperties.verify_option_is_disabled(WebFocusEnvironmentProperties.Locators.Ok, '02.01')
        
        """
           STEP 03 : Click WebFOCUS button. Click OK
        """
        WebFocusEnvironmentProperties.select_webfocus()
        
        """
            STEP 03 Expected : Message displays: Please provide a description for this environment.
        """
        WebFocusEnvironmentProperties.verify_alert_window_message(EXPECTED_ALERT_MSG, '03.01')
        WebFocusEnvironmentProperties.click_on_ok_button_in_alert_window()
        
        """
            STEP 04 : Click Data Servers button
            Click Ok in Message window
        """
        WebFocusEnvironmentProperties.select_data_servers()
        WebFocusEnvironmentProperties.click_on_ok_button_in_alert_window()
        
        """
            STEP 04 Expected : OK button is disabled
        """
        WebFocusEnvironmentProperties.verify_option_is_disabled(WebFocusEnvironmentProperties.Locators.Ok, '04.01')
        
        """
            STEP 04.1 : Click Cancel in WebFOCUS Environment Properties window
            Click Cancel in Environments List window
        """
        WebFocusEnvironmentProperties.click_on_cancel_button()
        EnvironmentList.click_on_cancel_button()
        
if __name__=='__main__' :
    unittest.main()