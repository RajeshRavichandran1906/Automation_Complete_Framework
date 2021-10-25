'''-------------------------------------------------------------------------------------------
Reworked on February 04, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288654
Test Case Title =  Environment Properties HTML Alias
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environment_configuration import EnvironmentList
from appstudio.tools.common.environment_configuration import WebFocusEnvironmentProperties

class C2288654_TestClass(BaseTestCase):
    
    def test_C2288654(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
        COMMON VARIABLE :
        """
        EXPECTED_ALERT_MSG = 'Please provide the HTML alias value, or check the "Use Default" button'
        
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
            STEP 01.03 : Uncheck Use Default. Delete HTML Alias value. Click the WebFOCUS
        """
        WebFocusEnvironmentProperties.uncheck_option(WebFocusEnvironmentProperties.Locators.WebComponentTab.UseDefault)
        WebFocusEnvironmentProperties.clear_textbox(WebFocusEnvironmentProperties.Locators.WebComponentTab.HtmlAlias)
        WebFocusEnvironmentProperties.select_webfocus()
       
        """
            STEP 01 Expected : Message displays 'Please provide the HTML alias value, or check the "Use Default" button'
        """
        WebFocusEnvironmentProperties.verify_alert_window_message(EXPECTED_ALERT_MSG, '01.01')
        
        """
            STEP 02 Click OK. Click Cancel in WebFOCUS Environment Properties
            Click Cancel in Environments List window
        """
        WebFocusEnvironmentProperties.click_on_ok_button_in_alert_window()
        WebFocusEnvironmentProperties.click_on_cancel_button()
        EnvironmentList.click_on_cancel_button()
        
if __name__=='__main__' :
    unittest.main()