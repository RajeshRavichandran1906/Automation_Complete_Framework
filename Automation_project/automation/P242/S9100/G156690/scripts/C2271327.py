'''-------------------------------------------------------------------------------------------
Reworked on January 08, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271327
Test Case Title =  Pages Group
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2271327_TestClass(BaseTestCase):
    
    def test_C2271327(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        NEW_TOOLTIP                 = 'New Add New Page'
        EXISTING_TOOLTIP            = 'Existing Add Existing Page'
        TABLE_OF_CONTENTS_TOOLTIP   = 'Table of Contents Add Table of Contents Page'
        MASTER_TOOLTIP              = 'Master Add Master Page'
        OVERFLOW_TOOLTIP            = 'Overflow Add Overflow Page'
        ADD_DASHBOARD_BAR_TOOLTIP   = 'Add Dashboard Bar Add Dashboard Bar Layout'
        
        """
            STEP 01 : Hover on "New"
            STEP 01 Expected : Tool tip displays: New Add New Page
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Pages.New, NEW_TOOLTIP, '01.01' )
    
        """
            STEP 02 : Hover on "Existing"
            STEP 02 Expected : Tool tip displays: Existing Add Existing Page
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Pages.Existing, EXISTING_TOOLTIP, '02.01')
        
        """
            STEP 03 : Hover on "Table of Contents"
            STEP 03 Expected : Tool tip displays: Table of Contents Add Table of Contents Page
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Pages.TableOfContents, TABLE_OF_CONTENTS_TOOLTIP, '03.01')
        
        """
            STEP 04 : Hover on "Master"
            STEP 04 Expected : Tool tip displays: Master Add Master Page
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Pages.Master, MASTER_TOOLTIP, '04.01')
        
        """
            STEP 05 : Hover on "Overflow"
            STEP 05 Expected : Tool tip displays: Overflow Add Overflow Page
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Pages.Overflow, OVERFLOW_TOOLTIP, '05.01')
        
        """
            STEP 06 : Hover on "Add Dashboard Bar"
            STEP 06 Expected : Tool tip displays: Add Dashboard Bar Add Dashboard Bar Layout
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Pages.AddDashboardBar, ADD_DASHBOARD_BAR_TOOLTIP, '06.01')
        
if __name__=='__main__' :
    unittest.main()