'''-------------------------------------------------------------------------------------------
Reworked on January 12, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667310
Test Case Title =  Sub Folder Contextual New Sub Menu
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
import unittest

class C6667310_TestClass(BaseTestCase):
    
    def test_C6667310(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """ 
            COMMON VARIABLES
        """
        EXPECTED_SUB_CONTEXT_MENU = ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Visualization', 'Alert', 'Reporting Object', 'URL', 'Collaborative Portal', 'Portal Page', 'JavaScript File', 'Cascading Style Sheet', 'WebFOCUS StyleSheet', 'Text Document', 'Schedule', 'Distribution List', 'Library Access List', 'Folder', 'Blog']
       
        """
            STEP 01.01 : In Environments Tree, Domains, right click FWSubfolder and hover over New.
        """
        Tree.right_click_on_webfocus_environment_item()
        
        """
            STEP 01.01 Expected : Verify "New" sub menu includes
        """
        Tree.verify_sub_context_menu('New', EXPECTED_SUB_CONTEXT_MENU, '01.01')
        
if __name__=='__main__' :
    unittest.main()