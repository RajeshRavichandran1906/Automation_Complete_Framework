'''-------------------------------------------------------------------------------------------
Reworked on January 28, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667312
Test Case Title =  TXT Domains Contextual New Menu
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
import unittest

class C6667312_TestClass(BaseTestCase):
    
    def test_C6667312(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """ 
            COMMON VARIABLES
        """
        EXPECTED_SUB_MENU = ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Visualization', 'Alert', 'Reporting Object', 'URL', 'Collaborative Portal', 'Portal Page', 'JavaScript File', 'Cascading Style Sheet', 'WebFOCUS StyleSheet', 'Text Document', 'Schedule', 'Distribution List', 'Library Access List', 'Folder', 'Blog']
        WF_TEXT_FILE_PATH = 'Domains->S9100->TextFile'
        
        """
            STEP 01.01 : Right click TextFile and hover over New.
            STEP 01.01 Expected : Sub menu contains: ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Visualization', 'Alert', 'Reporting Object', 'URL', 'Collaborative Portal', 'Portal Page', 'JavaScript File', 'Cascading Style Sheet', 'WebFOCUS StyleSheet', 'Text Document', 'Schedule', 'Distribution List', 'Library Access List', 'Folder', 'Blog']
        """
        Tree.right_click_on_webfocus_environment_item(WF_TEXT_FILE_PATH)
        Tree.verify_sub_context_menu('New', EXPECTED_SUB_MENU, '01.01')
        
if __name__=='__main__' :
    unittest.main()