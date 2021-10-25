'''-------------------------------------------------------------------------------------------
Reworked on January 14, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288298
Test Case Title =  Verify the contextual menu for a folder and a new folder under Domains.
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
import unittest

class C2288298_TestClass(BaseTestCase):
    
    def test_C2288298(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """ 
            COMMON VARIABLES
        """
        EXPECTED_CONTEXT_MENU_PUBLIC_FOLDER = ['']
        EXPECTED_CONTEXT_MENU_NEW_FOLDER1 = ['']
        WF_FOLDER_PATH_NEW_FOLDER_1= 'P242_S9100>G164315->New Folder1'
       
        """
            STEP 01.01 : Login with Developer User ID, Navigate to domain: P242_S9100>G164315
            STEP 02.01 : Right click on Domain folder P242_S9100>G164315
        """
        Tree.right_click_on_webfocus_environment_item()
        
        """
            STEP 02.01 Expected : Verify context menu
        """
        Tree.verify_context_menu(EXPECTED_CONTEXT_MENU_PUBLIC_FOLDER, '02.01')
        
        """
            STEP 03.01 : Navigate to domain: P242_S9100_G164315 and Right click on New Folder1 under Domains
        """
        Tree.right_click_on_webfocus_environment_item(WF_FOLDER_PATH_NEW_FOLDER_1)
        
        """
            STEP 03.01 Expected : Verify context menu
        """
        Tree.verify_context_menu(EXPECTED_CONTEXT_MENU_NEW_FOLDER1, '03.01')
        
if __name__=='__main__' :
    unittest.main()