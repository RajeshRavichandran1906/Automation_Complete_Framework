'''-------------------------------------------------------------------------------------------
Reworked on February 04, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288656
Test Case Title =  Environment Properties Default
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environment_configuration import EnvironmentList
from appstudio.tools.common.environment_configuration import WebFocusEnvironmentProperties

class C2288656_TestClass(BaseTestCase):
    
    def test_C2288656(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01 : In Home ribbon, click Environments. Select an environment and click Properties
        """
        EnvironmentList.invoke_from_ribbon()
        EnvironmentList.select_configured_environment()
        EnvironmentList.click_on_properties_button()
        
        """
            STEP 01 Expected : HTML Alias and Client Path are repopulated with values disabled
        """
        WebFocusEnvironmentProperties.verify_option_is_disabled(WebFocusEnvironmentProperties.Locators.WebComponentTab.HtmlAlias, '01.01')
        WebFocusEnvironmentProperties.verify_option_is_disabled(WebFocusEnvironmentProperties.Locators.WebComponentTab.ClientPath, '01.02')
       
        """
            STEP 02 : Uncheck Use Default
        """
        WebFocusEnvironmentProperties.uncheck_option(WebFocusEnvironmentProperties.Locators.WebComponentTab.UseDefault)
        
        """
            STEP 02 Expected : HTML Alias and Client Path are repopulated with values enabled
        """
        WebFocusEnvironmentProperties.verify_option_is_enabled(WebFocusEnvironmentProperties.Locators.WebComponentTab.HtmlAlias, '02.01')
        WebFocusEnvironmentProperties.verify_option_is_enabled(WebFocusEnvironmentProperties.Locators.WebComponentTab.ClientPath, '02.02')
        
        """
            STEP 03 : Click Cancel in WebFOCUS Environment Properties
            Click Cancel in Environments List window
        """
        WebFocusEnvironmentProperties.click_on_cancel_button()
        EnvironmentList.click_on_cancel_button()
        
if __name__=='__main__' :
    unittest.main()