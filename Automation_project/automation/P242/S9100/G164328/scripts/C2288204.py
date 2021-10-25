'''-------------------------------------------------------------------------------------------
Created on January 10, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288204
Test Case Title =  Applications Contextual New Menu, Sub Menu
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Detail
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2288204_TestClass(BaseTestCase):

    def test_C2288204(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        EXPECTED_CONTEXT_MENU = ['New', 'Rename', 'Delete', 'Properties', 'Refresh Descendants']
        EXPECTED_SUB_CONTEXT_MENU = ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Synonym', 'Synonym via Metadata Canvas', 'Define Function Library', 'Upload Data', 'WebFOCUS StyleSheet', 'Text Document', 'XML Document with ESRI Configuration', 'Application Directory']
        WF_FOLDER_PATH  = 'Data Servers->EDASERVE->Applications->baseapp'
      
        """
            STEP 01 : In Environments Detail, EDASERVE Right click baseapp
        """
        Ribbon.select_tab(Ribbon.Locators.HomeTab.HOME)
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        Detail.right_click_on_webfocus_environment_folder(WF_FOLDER_PATH)
        
        """
            STEP 01.Expected : Verify context menu
        """
        Detail.verify_context_menu(EXPECTED_CONTEXT_MENU, '01.01')
        
        """
            STEP 02 : In Environments Detail, EDASERVE. Right click baseapp and hover New
            STEP 02.Expected : Verify sub context menu
        """
        Detail.verify_sub_context_menu('New', EXPECTED_SUB_CONTEXT_MENU, '02.01')
        
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        
if __name__=='__main__' :
    unittest.main()