'''-------------------------------------------------------------------------------------------
Reworked on January 31, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8784826
Test Case Title =  Domains Contextual Menu
-----------------------------------------------------------------------------------------------'''
import unittest
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree

class C8784826_TestClass(BaseTestCase):
    
    def test_C8784826(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
        COMMON VARIABLES
        """
        EXPECTED_CONTEXT_MENU = ['Impact Analysis', 'New', 'Upload Data', 'Unpublish', 'Hide', 'Security', 'Duplicate', 'Copy', 'Rename', 'Delete', 'ReportCaster Explorer', 'Source Control', 'Properties', 'Refresh Descendants']
        EXPECTED_SUB_CONTEXT_MENU = ['Rules...', 'Rules on this Resource...', 'Effective Policy...', 'Owner...']
        
        """
            STEP 01 : Login with Administrator User Navigate to domain: P242_S21365>G728722
            STEP 02 : Right click on P242_S21365>G728722 Domains area
        """
        Tree.right_click_on_webfocus_environment_item()
        
        """
            STEP 02 Expected : Verify context menu 
        """
        Tree.verify_context_menu(EXPECTED_CONTEXT_MENU, '02.01')
        
        """
            STEP 03 : Hover Security Click anywhere to close menu and sub-menu
            STEP 03 : Expected :  Verify Security sub menu 
        """
        Tree.verify_sub_context_menu('Security', EXPECTED_SUB_CONTEXT_MENU, '03.01')
        Tree.dismiss_context_menu()
        
if __name__=='__main__' :
    unittest.main()        
        