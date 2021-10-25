'''-------------------------------------------------------------------------------------------
Reworked on January 11, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667308
Test Case Title =  Verify Context Menu of 'New'.
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
import unittest

class C6667308_TestClass(BaseTestCase):
    
    def test_C6667308(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """ 
            COMMON VARIABLES
        """
        EXPECTED_CONTEXT_MENU = ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Visualization', 'Alert', 'Reporting Object', 'URL', 'Collaborative Portal', 'Portal Page', 'JavaScript File', 'Cascading Style Sheet', 'WebFOCUS StyleSheet', 'Text Document', 'Schedule', 'Distribution List', 'Library Access List', 'Folder', 'Blog']
       
        """
            STEP 01 : Right click New Folder1 under Domains and hover over New
        """
        Tree.right_click_on_webfocus_environment_item()
        
        """
            STEP 01 Expected : Verify context menu
        """
        Tree.verify_sub_context_menu('New', EXPECTED_CONTEXT_MENU, '01.01')
        
if __name__=='__main__' :
    unittest.main()