'''-------------------------------------------------------------------------------------------
Created on January 11, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2288270
Test Case Title =  MAS Data Servers Contextual Menu, New Menu
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Detail
from appstudio.tools.common.environments import ToolBarMenu
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2288270_TestClass(BaseTestCase):

    def test_C2288270(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        EXPECTED_CONTEXT_MENU = ['Open', 'Create Report', 'Create Chart', 'Open in Text Editor', 'Edit in Windows Associated Tool', 'Refresh Synonym', 'Sample Data', 'Impact Analysis', 'Print', 'Check', 'Edit Access File as Text', 'New', 'Duplicate', 'Copy', 'Rename', 'Delete', 'Properties']
        EXPECTED_SUB_CONTEXT_MENU = ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Synonym', 'Synonym via Metadata Canvas', 'Define Function Library', 'Upload Data', 'WebFOCUS StyleSheet', 'Text Document', 'XML Document with ESRI Configuration', 'Application Directory']
        WF_FOLDER_PATH  = 'Data Servers->EDASERVE->Applications->ibisamp'
        FILE_NAME = 'car.mas'
       
        """
            STEP 01 : In Environments Detail, set Filter to Master Files
            Navigate to Data Servers->EDASERVE->Applications->ibisamp
            Right click on car.mas
        """
        Ribbon.select_tab(Ribbon.Locators.HomeTab.HOME)
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        ToolBarMenu.select_menu(ToolBarMenu.Locator.MasterFiles)
        Detail.right_click_on_webfocus_environment_folder_file(FILE_NAME, WF_FOLDER_PATH)
        
        """
            STEP 01.Expected : Verify context menu
        """
        Detail.verify_context_menu(EXPECTED_CONTEXT_MENU, '01.01')
        
        """
            STEP 02 : Right click on car.mas and hover New
            STEP 02.Expected : Verify sub context menu
        """
        Detail.verify_sub_context_menu('New', EXPECTED_SUB_CONTEXT_MENU, '02.01')
        
        ToolBarMenu.select_menu(ToolBarMenu.Locator.AllFiles)
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        
if __name__=='__main__' :
    unittest.main()