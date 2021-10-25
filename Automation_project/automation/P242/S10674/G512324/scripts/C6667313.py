'''-------------------------------------------------------------------------------------------
Reworked on January 28, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6667313
Test Case Title =  FEX Domains Contextual Menu, New Menu
-----------------------------------------------------------------------------------------------'''
from appstudio.tools.common import environments as Environments
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.report import Canvas
from appstudio import settings
import unittest

class C6667313_TestClass(BaseTestCase):
    
    def test_C6667313(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """ 
            COMMON VARIABLES
        """
        EnvironmentsToolBarMenuLocator= Environments.ToolBarMenu.Locator
        EXPECTED_UNPUBLISH_CONTEXT_MENU = ['Open', 'Open in Text Editor', 'Edit in Windows Associated Tool', 'Run', 'Run Deferred', 'Schedule', 'Print', 'Hide', 'Security', 'New', 'Duplicate', 'Copy', 'Rename', 'Delete', 'Properties']
        EXPECTED_PUBLISH_CONTEXT_MENU = ['Open', 'Open in Text Editor', 'Edit in Windows Associated Tool', 'Run', 'Run Deferred', 'Schedule', 'Print', 'Unpublish', 'Hide', 'Security', 'New', 'Duplicate', 'Copy', 'Rename', 'Delete', 'Properties']
        EXPECTED_FILE_CONTEXT_MENU = ['Schedule', 'Print', 'Unpublish', 'Hide', 'Security', 'New', 'Duplicate', 'Copy', 'Properties']
        EXPECTED_SUBCONTEXT_MENU = ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Visualization', 'Alert', 'Reporting Object', 'URL', 'Collaborative Portal', 'Portal Page', 'JavaScript File', 'Cascading Style Sheet', 'WebFOCUS StyleSheet', 'Text Document', 'Schedule', 'Distribution List', 'Library Access List', 'Folder', 'Blog']
        WF_FOLDER_FILE_PATH = 'Domains->S9100'
        WF_FEX_FILE_PATH = 'Domains->S9100->AS-2260'
        WF_UNPUBLISH = 'Unpublish'
        WF_PUBLISH = 'Publish'
       
        """
            STEP 01.01 : In Environments Tree, set Filters to Procedure Files
        """
        Environments.ToolBarMenu.select_menu(EnvironmentsToolBarMenuLocator.ProcedureFiles)
         
        """
            STEP 01.02 : Right click on AS Framework and select Unpublish
        """
        Environments.Tree.right_click_on_webfocus_environment_item(WF_FOLDER_FILE_PATH)
        Environments.Tree.select_context_menu(WF_UNPUBLISH)
         
        """
            STEP 01.03 : Right click on AS-2260
            STEP 01.03 Expected : Contextual menu includes: : 
        """
        Environments.Tree.right_click_on_webfocus_environment_item(WF_FEX_FILE_PATH)
        Environments.Tree.verify_context_menu(EXPECTED_UNPUBLISH_CONTEXT_MENU, '01.03')
        Environments.Tree.dismiss_context_menu()
         
        """
            STEP 02.01 : Right click on AS Framework and select Publish 
        """
        Environments.Tree.right_click_on_webfocus_environment_item(WF_FOLDER_FILE_PATH)
        Environments.Tree.select_context_menu(WF_PUBLISH)
         
        """
            STEP 02.02 : Right click on AS-2260
            STEP 02.02 Expected : Contextual menu includes: : 
        """
        Environments.Tree.right_click_on_webfocus_environment_item(WF_FEX_FILE_PATH)
        Environments.Tree.verify_context_menu(EXPECTED_PUBLISH_CONTEXT_MENU, '02.02')
        Environments.Tree.dismiss_context_menu()
        
        """
            STEP 03.01 : Double click on AS-2260
            STEP 03.01 Expected : Contextual menu includes: : 
        """
        Environments.Tree.double_click_on_webfocus_environment_item(WF_FEX_FILE_PATH)
        Environments.Tree.right_click_on_webfocus_environment_item(WF_FEX_FILE_PATH)
        Environments.Tree.verify_context_menu(EXPECTED_FILE_CONTEXT_MENU, '03.01')
        Environments.Tree.dismiss_context_menu()
        
        """
            STEP 03.02 : Close AS-2260 tab
        """
        Canvas.close_report_canvas()
        
        """
            STEP 04.01 : Right click on AS-2260 and hover New
        """
        Environments.Tree.right_click_on_webfocus_environment_item(WF_FEX_FILE_PATH)
        Environments.Tree.verify_sub_context_menu('New', EXPECTED_SUBCONTEXT_MENU, '04.01')
        
        Environments.ToolBarMenu.select_menu(EnvironmentsToolBarMenuLocator.AllFiles)
        
if __name__=='__main__' :
    unittest.main()