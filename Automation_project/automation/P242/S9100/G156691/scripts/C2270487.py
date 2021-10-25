'''-------------------------------------------------------------------------------------------
Reworked on January 24, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270487
Test Case Title =  Settings Panel
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.tools.html_page import SettingsPanel
from appstudio.lib.basetestcase import BaseTestCase
import unittest

class C2270487_TestClass(BaseTestCase):
    
    def test_C2270487(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01.01 : Click on Settings panel
        """
        SettingsPanel.expand_settings_panel()
        
        """
            STEP 01.02 : Hover on Window position icon
            STEP 01.02 : Tool tip displays: Window Position 
        """
        EXPECTED_WINDOW_POSITION_TOOLTIP = 'Window Position'
        SettingsPanel.verify_header_button_tooltip(SettingsPanel.Locator.HeaderButtons.WindowPosition, EXPECTED_WINDOW_POSITION_TOOLTIP, '01.02')
        
        """
             STEP 01.03 : Hover on Auto Hide icon
             STEP 01.03 : Tool tip displays: Auto Hide
        """
        EXPECTED_AUTO_HIDE_TOOLTIP = 'Auto Hide'
        SettingsPanel.verify_header_button_tooltip(SettingsPanel.Locator.HeaderButtons.AutoHideUnPin, EXPECTED_AUTO_HIDE_TOOLTIP, '01.03')
         
        """
             STEP 01.04 : Hover on Close icon
             STEP 01.04 : Tool tip displays: Close
        """
        EXPECTED_CLOSE_TOOLTIP = 'Close'
        SettingsPanel.verify_header_button_tooltip(SettingsPanel.Locator.HeaderButtons.Close, EXPECTED_CLOSE_TOOLTIP, '01.04')
         
        """
            STEP 02.01 : Hover on CSS icon
            STEP 02.01 : Tool tip displays: CSS...
        """
        EXPECTED_CSS_TOOLTIP = 'CSS...'
        SettingsPanel.verify_toolbar_menu_tooltip(SettingsPanel.Locator.ManageCssScripts.Css, EXPECTED_CSS_TOOLTIP, '02.01')
         
        """
            STEP 03.01 : Hover on JS icon 
            STEP 03.01 : Tool tip displays: JavaScript
        """
        EXPECTED_JAVASCRIPT_TOOLTIP = 'JavaScript'
        SettingsPanel.verify_toolbar_menu_tooltip(SettingsPanel.Locator.ManageCssScripts.JavaScript, EXPECTED_JAVASCRIPT_TOOLTIP, '03.01')
        
        """
            STEP 04.01 : Hover "Delete" icon next to "Items may be dragged into the desired order"
            STEP 04.01 : Tool tip displays: Delete
        """
        EXPECTED_DELETE_TOOLTIP = 'Delete'
        SettingsPanel.verify_toolbar_menu_tooltip(SettingsPanel.Locator.ManageCssScripts.Delete, EXPECTED_DELETE_TOOLTIP, '04.01')
        
        """
            STEP 05.01 : Hover "Move Item Up" icon next to "Items may be dragged into the desired order"
            STEP 05.01 : Tool tip displays: Move Item Up
        """
        EXPECTED_MOVE_ITEM_UP_TOOLTIP = 'Move Item Up'
        SettingsPanel.verify_toolbar_menu_tooltip(SettingsPanel.Locator.ManageCssScripts.MoveItemUp, EXPECTED_MOVE_ITEM_UP_TOOLTIP, '05.01')
        
        """
            STEP 06.01 : Hover "Move Item Down" icon next to "Items may be dragged into the desired order"
            STEP 06.01 : Tool tip displays: Move Item Down
        """
        EXPECTED_MOVE_ITEM_DOWN_TOOLTIP = 'Move Item Down'
        SettingsPanel.verify_toolbar_menu_tooltip(SettingsPanel.Locator.ManageCssScripts.MoveItemDown, EXPECTED_MOVE_ITEM_DOWN_TOOLTIP, '06.01')
        
        """
            STEP 07.01 : Hover New icon under "List of"
            STEP 07.01 : Tool tip displays: New 
        """
        EXPECTED_LIST_OF_NEW_TOOLTIP = 'New'
        SettingsPanel.verify_toolbar_menu_tooltip(SettingsPanel.Locator.ManageCssScripts.ListOfNew, EXPECTED_LIST_OF_NEW_TOOLTIP, '07.01')
        
        """
            STEP 08.01 : Hover Delete icon under "List of"
            STEP 08.01 : Tool tip displays: Delete
        """
        EXPECTED_LIST_OF_DELETE_TOOLTIP = 'Delete'
        SettingsPanel.verify_toolbar_menu_tooltip(SettingsPanel.Locator.ManageCssScripts.ListOfDelete, EXPECTED_LIST_OF_DELETE_TOOLTIP, '08.01')
        
        """
            STEP 09.01 : Hover Toggle icon under "List of"
            STEP 09.01 : Tool tip displays: Toggle selected layer visibility
        """
        EXPECTED_LIST_OF_TOGGLE_TOOLTIP = 'Toggle selected layer visibility'
        SettingsPanel.verify_toolbar_menu_tooltip(SettingsPanel.Locator.ManageCssScripts.ListOfToggle, EXPECTED_LIST_OF_TOGGLE_TOOLTIP, '09.01')
        
if __name__=='__main__' :
    unittest.main()