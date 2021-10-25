'''-------------------------------------------------------------------------------------------
Reworked on February 01, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288321
Test Case Title = Verify Security sub-menu in the Folder contextual menu.
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
import unittest

class C2288321_TestClass(BaseTestCase):
    
    def test_C2288321(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
       
        """
            STEP 01 : Login with Developer User ID, Navigate to domain: P242_S9100>G164315
            STEP 02 : In Environments Tree, Right click on P242_S9100>G164315 Domain folder and hover over Security.
        """
        EXPECTED_SECURITY_SUBCONTEXT_MENU = ['Rules on this Resource...', 'Effective Policy...', 'Owner...']
        Tree.right_click_on_webfocus_environment_item()
        Tree.verify_sub_context_menu('Security', EXPECTED_SECURITY_SUBCONTEXT_MENU, '02.01')
        
if __name__=='__main__' :
    unittest.main()