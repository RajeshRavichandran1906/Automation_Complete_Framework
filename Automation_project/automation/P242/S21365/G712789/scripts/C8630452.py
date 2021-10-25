'''-------------------------------------------------------------------------------------------
Created on January 14, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8630452
Test Case Title =  SubApplication Contextual Menu, New Application, New Menu
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Detail
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C8630452_TestClass(BaseTestCase):

    def test_C8630452(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        MRID = 'mradmin'
        EXPECTED_CONTEXT_MENU = ['New', 'Duplicate', 'Copy', 'Rename', 'Delete', 'Properties', 'Refresh Descendants']
        EXPECTED_SUB_CONTEXT_MENU = ['Procedure', 'Procedure via Text Editor', 'Report', 'SQL Report', 'Chart', 'SQL Chart', 'HTML/Document', 'Synonym', 'Synonym via Metadata Canvas', 'Define Function Library', 'Upload Data', 'WebFOCUS StyleSheet', 'Text Document', 'XML Document with ESRI Configuration', 'Application Directory']
        WF_FOLDER_PATH  = 'Data Servers->EDASERVE->Applications->baseapp'
        
        """
            STEP 01 : In Environments Detail, Data Server->EDASERVE->Applications>baseapp
            Right click baseapp and select New->Application Directory and Hit Enter
        """
        Ribbon.select_tab(Ribbon.Locators.HomeTab.HOME)
        
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        
        Detail.right_click_on_webfocus_environment_folder(WF_FOLDER_PATH, mrid=MRID)
        Detail.select_context_menu('New->Application Directory')
        Detail.hit_enter()
        
        """
            STEP 01.Expected : Verify new Application Directory is created
        """
        Detail.verify_specific_webfocus_environment_items(WF_FOLDER_PATH, ['newapp'], '01.01', mrid=MRID)
        
        """
            STEP 02 : Right click on newapp
        """
        Detail.right_click_on_webfocus_environment_folder(WF_FOLDER_PATH + '->newapp', mrid=MRID)
    
        """
            STEP 02.Expected : Verify newapp context menu
        """
        Detail.verify_context_menu(EXPECTED_CONTEXT_MENU, '02.01')
        
        """
            STEP 03 : Right click on newapp and hover over New
            STEP 03.Expected : Verify newapp sub context menu
        """
        Detail.verify_sub_context_menu('New', EXPECTED_SUB_CONTEXT_MENU, '03.01')
    
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        
if __name__=='__main__' :
    unittest.main()