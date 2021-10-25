'''-------------------------------------------------------------------------------------------
Reworked on January 31, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288669
Test Case Title =  Add an Environment From Tree
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environment_configuration import WebFocusEnvironmentProperties

class C2288669_TestClass(BaseTestCase):
    
    def test_C2288669(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01.01 : In Environments Tree, right click 'Configured Environments' and select 'Add'
            STEP 01.01 Expected : WebFOCUS Environment Properties window opens.
        """
        WebFocusEnvironmentProperties.invoke_from_environment_tree()
        WebFocusEnvironmentProperties.verify_environment_properties_window_exists('01.01')
        
        """
            STEP 02.01 : Click Cancel.
            STEP 02.01 Expected : Window closes.
        """
        WebFocusEnvironmentProperties.click_on_cancel_button()
        WebFocusEnvironmentProperties.verify_environment_properties_window_not_exists('02.01')
        
if __name__=='__main__' :
    unittest.main()