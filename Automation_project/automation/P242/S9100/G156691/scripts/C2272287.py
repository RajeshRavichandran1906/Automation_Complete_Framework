'''-------------------------------------------------------------------------------------------
Reworked on January 22, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2272287
Test Case Title =  Properties Panel
-----------------------------------------------------------------------------------------------'''
from appstudio.tools import html_page as HtmlPage
from appstudio.lib.basetestcase import BaseTestCase
import unittest

class C2272287_TestClass(BaseTestCase):
    
    def test_C2272287(self):
        
        """
            COMMON TEST CASE VARIABLES 
        """
        PropertiesPanelLocators = HtmlPage.PropertiesPanel.Locator
        
        """
            STEP 01.01 : Click on Properties panel.
            STEP 01.01 Expected : Properties panel should get expand
        """
        HtmlPage.PropertiesPanel.expand_properties_panel()
        
        """
            STEP 01.02 : Hover on Window position icon
            STEP 01.02 Expected : Tool tip displays: "Window Position"
        """
        WINDOW_POSITION_TOOLTIP = 'Window Position'
        HtmlPage.PropertiesPanel.verify_header_button_tooltip(PropertiesPanelLocators.HeaderButtons.WindowPosition, WINDOW_POSITION_TOOLTIP, '01.02')
        
        """
            STEP 01.03 : Hover on Auto Hide icon
            STEP 01.03 Expected : Tool tip displays: "Auto Hide"
        """
        AUTO_HIDE_TOOLTIP = 'Auto Hide'
        HtmlPage.PropertiesPanel.verify_header_button_tooltip(PropertiesPanelLocators.HeaderButtons.AutoHideUnPin, AUTO_HIDE_TOOLTIP, '01.03')
        
        """
            STEP 01.04 : Hover on Close icon
            STEP 01.04 Expected : Tool tip displays: "Close"
        """
        CLOSE_TOOLTIP = 'Close'
        HtmlPage.PropertiesPanel.verify_header_button_tooltip(PropertiesPanelLocators.HeaderButtons.Close, CLOSE_TOOLTIP, '01.04')
        
        """
            STEP 02.01 : Hover on Catagorized icon
            STEP 02.01 Expected : Tool tip displays: "Categorized"
        """
        CATAGORIZED_TOOLTIP = 'Categorized'
        HtmlPage.PropertiesPanel.verify_toolbar_menu_tooltip(PropertiesPanelLocators.ToolBarMenu.Categorized, CATAGORIZED_TOOLTIP, '02.01')
        
        """
            STEP 02.02 : Hover on Alphabetical icon
            STEP 02.02 Expected : Tool tip displays: "Alphabetical"
        """
        ALPHABETICAL_TOOLTIP = 'Alphabetical'
        HtmlPage.PropertiesPanel.verify_toolbar_menu_tooltip(PropertiesPanelLocators.ToolBarMenu.Alphabetical, ALPHABETICAL_TOOLTIP, '02.02')
        
        """
            STEP 02.03 : Hover on Display content icon
            STEP 02.03 Expected : Tool tip displays: Display contents of the selected item Properties
        """
        DISPLAY_CONTENT_TOOLTIP ='Display contents of the selected item Properties'
        HtmlPage.PropertiesPanel.verify_toolbar_menu_tooltip(PropertiesPanelLocators.ToolBarMenu.Properties, DISPLAY_CONTENT_TOOLTIP, '02.03')
        
        """
            STEP 02.04 : Hover on Events icon
            STEP 02.04 Expected : Tool tip displays: Events
        """
        EVENT_TOOLTIP = 'Events'
        HtmlPage.PropertiesPanel.verify_toolbar_menu_tooltip(PropertiesPanelLocators.ToolBarMenu.Events, EVENT_TOOLTIP, '02.04')
        
if __name__=='__main__' :
    unittest.main()