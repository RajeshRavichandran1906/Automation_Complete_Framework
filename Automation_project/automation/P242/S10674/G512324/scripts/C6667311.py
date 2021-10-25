'''-------------------------------------------------------------------------------------------
Reworked on January 14, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667311
Test Case Title =  Verify the contextual menu for a folder and a new folder under Domains.
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree, ToolBarMenu
import unittest

class C6667311_TestClass(BaseTestCase):
    
    def test_C6667311(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """ 
            COMMON VARIABLES
        """
        EXPECTED_CONTEXT_MENU = ['Open', 'Open in Text Editor', 'Edit in Windows Associated Tool', 'Run', 'Print', 'Hide', 'Security', 'New', 'Duplicate', 'Copy', 'Rename', 'Delete', 'Properties']
        EXPECTED_SUB_CONTEXT_MENU = ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Visualization', 'Alert', 'Reporting Object', 'URL', 'Collaborative Portal', 'Portal Page', 'JavaScript File', 'Cascading Style Sheet', 'WebFOCUS StyleSheet', 'Text Document', 'Schedule', 'Distribution List', 'Library Access List', 'Folder', 'Blog']
        WF_FOLDER_PATH_DOMAIN = 'Domains->S9100->110045RIA'
       
        """
            STEP 01.01 : In Environments Tree, set Filter to HTML Files Navigate to CC - AppStudio-AS Files Right click on 110045RIA
        """
        ToolBarMenu.select_menu(ToolBarMenu.Locator.HTMLFiles)
        Tree.right_click_on_webfocus_environment_item(WF_FOLDER_PATH_DOMAIN)
        
        """
            STEP 01.01 Expected : Verify context menu
        """
        Tree.verify_context_menu(EXPECTED_CONTEXT_MENU, '01.01')
        
        """
            STEP 02.01 : Right click on '110045RIA' and hover on New
            STEP 02.01 Expected : Verify context menu
        """
        Tree.verify_sub_context_menu('New', EXPECTED_SUB_CONTEXT_MENU, '02.01')
        ToolBarMenu.select_menu(ToolBarMenu.Locator.AllFiles)
        
if __name__=='__main__' :
    unittest.main()
    