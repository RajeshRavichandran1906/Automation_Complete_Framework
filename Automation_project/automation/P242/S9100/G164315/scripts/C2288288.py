'''-------------------------------------------------------------------------------------------
Reworked on January 12, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288288
Test Case Title =  Verify the contextual menu for item in the tree.
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
import unittest

class C2288288_TestClass(BaseTestCase):
    
    def test_C2288288(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """ 
            COMMON VARIABLES
        """
        EXPECTED_CONTEXT_MENU = ['Impact Analysis', 'New Folder', 'Mode Manager', 'Physical View', 'Security', 'ReportCaster Explorer', 'Refresh Descendants']
        EXPECTED_SUB_CONTEXT_MENU = ['Rules...', 'Rules on this Resource...', 'Effective Policy...']
        WF_FOLDER_PATH = 'Domains'
        USER = 'developer'
        
        """
            STEP 01.01 : Expand a remote configured environment Right click on Domains
        """
        Tree.right_click_on_webfocus_environment_item(USER, WF_FOLDER_PATH)
        
        """
            STEP 01.01 Expected : Verify context menu
        """
        Tree.verify_context_menu(EXPECTED_CONTEXT_MENU, '01.01')
        
        """
            STEP 02.01 : Hover on "Security" icon
            STEP 02.01 Expected : Verify Sub context menu
        """
        Tree.verify_sub_context_menu('Security', EXPECTED_SUB_CONTEXT_MENU, '02.01')
        
if __name__=='__main__' :
    unittest.main()