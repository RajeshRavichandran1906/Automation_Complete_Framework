'''-------------------------------------------------------------------------------------------
Reworked on January 22, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270490
Test Case Title =  Properties Panel
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.tools import html_page as HtmlPage
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270490_TestClass(BaseTestCase):

    def test_C2270490(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        
        ThumbnailPanelLocators = HtmlPage.ThumbnailsPanel.Locator
        
        """
            STEP 01.01 : Click on Thumbnails panel
        """
        HtmlPage.ThumbnailsPanel.collapse_panel_by_click_on_workspace() #Collapse panel if already expanded
        Ribbon.select_tab(Ribbon.Locators.UtilitiesTab.UTILITIES)
        Ribbon.select_tab_item(Ribbon.Locators.UtilitiesTab.View.Thumbnails)
        
        """
            STEP 01.02 : Hover on Window position icon
            STEP 01.02 Expected : Tool tip displays: "Window Position"
        """
        WINDOW_POSITION_TOOLTIP = 'Window Position'
        HtmlPage.ThumbnailsPanel.verify_header_button_tooltip(ThumbnailPanelLocators.HeaderButtons.WindowPosition, WINDOW_POSITION_TOOLTIP, '01.02')
        
        """
            STEP 02.01 : Hover on Auto Hide icon
            STEP 02.01 Expected : Tool tip displays: "Auto Hide"
        """
        AUTO_HIDE_TOOLTIP = 'Auto Hide'
        HtmlPage.ThumbnailsPanel.verify_header_button_tooltip(ThumbnailPanelLocators.HeaderButtons.AutoHidePinned, AUTO_HIDE_TOOLTIP, '02.01')
        
        """
            STEP 03.01 : Hover on Close icon
            STEP 03.01 Expected : Tool tip displays: "Close"
        """
        CLOSE_TOOLTIP = 'Close'
        HtmlPage.ThumbnailsPanel.verify_header_button_tooltip(ThumbnailPanelLocators.HeaderButtons.Close, CLOSE_TOOLTIP, '03.01')
        
        """
            STEP 04.01 : Click on Utilities tab and unchecked Thumbnails from the View group
            STEP 04.01 Expected : Thumbnail should be unchecked
        """
        Ribbon.unselect_tab_item(Ribbon.Locators.UtilitiesTab.View.Thumbnails)
       
if __name__=='__main__' :
    unittest.main()