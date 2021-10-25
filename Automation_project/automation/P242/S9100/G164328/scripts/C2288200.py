'''-------------------------------------------------------------------------------------------
Created on January 17, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2288200
Test Case Title =  DataServers Contextual Menu, Manage Adapters, Refresh Descendants
-----------------------------------------------------------------------------------------------'''
from appstudio.tools.common.environments import Detail
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.adapters import Adapters
from appstudio.tools.common.ribbon import Ribbon
from appstudio import settings
import unittest

class C2288200_TestClass(BaseTestCase):

    def test_C2288200(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        EXPECTED_CONTEXT_MENU = ['Manage Adapters', 'Refresh Descendants']
        WF_FOLDER_PATH  = 'Data Servers->EDASERVE'
        MRID = 'mradmin'
        
        """
            STEP 01 : In View Group, uncheck Environments Tree and check Environments Detail
            Collapse Domains, Expand Data Servers. Right click on EDASERVE
        """
        Ribbon.select_tab(Ribbon.Locators.HomeTab.HOME)
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        Detail.right_click_on_webfocus_environment_folder(WF_FOLDER_PATH, mrid=MRID)
        
        """
            STEP 01.Expected : Verify context menu
        """
        Detail.verify_context_menu(EXPECTED_CONTEXT_MENU, '01.01')
        
        """
            STEP 02 : Right click on EDASERVE and click Manage Adapters. Click Cancel
        """
        Detail.select_context_menu('Manage Adapters')
        
        """
            STEP 02.Expected : Manage and Configure Adapters Window is open
        """
        Adapters.verify_manage_adapters_window_open('02.01')
        Adapters.click_on_button(Adapters.Locators.CancelButton)
        
        """
            STEP 03 : Right click on EDASERVE and click Refresh Descendants
        """
        Detail.right_click_on_webfocus_environment_folder(WF_FOLDER_PATH, mrid=MRID)
        Detail.select_context_menu('Refresh Descendants')
        
        """
            STEP 03.Expected : Verify EDASERVE collapsed state
        """
        Detail.verify_webfocus_environment_item_is_collapsed(WF_FOLDER_PATH, '03.01', mrid=MRID)
        
        Ribbon.unselect_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsDetail)
        Ribbon.select_tab_item(Ribbon.Locators.HomeTab.View.EnvironmentsTree)
        
if __name__=='__main__' :
    unittest.main()