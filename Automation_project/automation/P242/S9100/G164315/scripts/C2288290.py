'''-------------------------------------------------------------------------------------------
Reworked on January 30, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288290
Test Case Title =  Controls Tab
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
import unittest

class C2270483_TestClass(BaseTestCase):
    
    settings.AppStudio.CLOSE_CANVAS = False

    def test_C2270483(self):
        
        """
            STEP 01 : Login with Developer User ID, Navigate to domain: P242_S9100>G164315
            STEP 02 : Right click on P242_S9100>G164315 Domain and select New Folder
        """
        Tree.right_click_on_webfocus_environment_item()
        Tree.select_context_menu('New->Folder')
        
        """
            STEP 02 : Expected : If Domains was not expanded, it expands upon this selection. A folder with title New Folder1 (or n+1) is added to list of folders with the folder title in edit mode. 
        """
        EXPECTED_VALUE = ''
        Tree.verify_edited_value_of_webfocus_environment_item(EXPECTED_VALUE, '02.01' )
        
        """
            STEP 03 : Click anywhere to disable the Edit mode
        """
        
if __name__=='__main__' :
    unittest.main()
