'''-------------------------------------------------------------------------------------------
Reworked on January 24, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270489
Test Case Title =  Requests & Data Sources Panel
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.html_page import RequestDataSourcesPanel
import unittest

class C2270489_TestClass(BaseTestCase):
    
    def test_C2270489(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01.01 : Click on Requests & Data Sources panel
        """
        RequestDataSourcesPanel.expand_request_datasource_panel()
        
        """
            STEP 01.02 : Hover on Window position icon
            STEP 01.02 : Tool tip displays: Window Position 
        """
        EXPECTED_WINDOW_POSITION_TOOLTIP = 'Window Position'
        RequestDataSourcesPanel.verify_header_button_tooltip(RequestDataSourcesPanel.Locator.HeaderButtons.WindowPosition, EXPECTED_WINDOW_POSITION_TOOLTIP, '01.02')
        
        """
             STEP 01.03 : Hover on Auto Hide icon
             STEP 01.03 : Tool tip displays: Auto Hide
        """
        EXPECTED_AUTO_HIDE_TOOLTIP = 'Auto Hide'
        RequestDataSourcesPanel.verify_header_button_tooltip(RequestDataSourcesPanel.Locator.HeaderButtons.AutoHideUnPin, EXPECTED_AUTO_HIDE_TOOLTIP, '01.03')
         
        """
             STEP 01.04 : Hover on Close icon
             STEP 01.04 : Tool tip displays: Close
        """
        EXPECTED_CLOSE_TOOLTIP = 'Close'
        RequestDataSourcesPanel.verify_header_button_tooltip(RequestDataSourcesPanel.Locator.HeaderButtons.Close, EXPECTED_CLOSE_TOOLTIP, '01.04')
         
        """
            STEP 02.01 : Hover on New icon
            STEP 02.01 : Tool tip displays: New
        """
        EXPECTED_NEW_TOOLTIP = 'New'
        RequestDataSourcesPanel.verify_toolbar_menu_tooltip(RequestDataSourcesPanel.Locator.ToolBar.New, EXPECTED_NEW_TOOLTIP, '02.01')
         
        """
            STEP 03.01 : Hover on Delete icon
            STEP 03.01 : Tool tip displays: Delete
        """
        EXPECTED_DELETE_TOOLTIP = 'Delete'
        RequestDataSourcesPanel.verify_toolbar_menu_tooltip(RequestDataSourcesPanel.Locator.ToolBar.Delete, EXPECTED_DELETE_TOOLTIP, '03.01')
        
        """
            STEP 04.01 : Hover on Refresh icon
            STEP 04.01 : Tool tip displays: Refresh parameters
        """
        EXPECTED_REFRESH_PARAMETERS_TOOLTIP = 'Refresh parameters'
        RequestDataSourcesPanel.verify_toolbar_menu_tooltip(RequestDataSourcesPanel.Locator.ToolBar.RefreshParameters, EXPECTED_REFRESH_PARAMETERS_TOOLTIP, '04.01')
        
        """
            STEP 05.01 : Hover on Input Controls icon
            STEP 05.01 : Tool tip displays: Create Input Controls
        """
        EXPECTED_INPUT_CONTROLS_TOOLTIP = 'Create Input Controls'
        RequestDataSourcesPanel.verify_toolbar_menu_tooltip(RequestDataSourcesPanel.Locator.ToolBar.CreateInputControls, EXPECTED_INPUT_CONTROLS_TOOLTIP, '05.01')
        
        """
            STEP 06.01 : Hover on Save Selection icon
            STEP 06.01 : Tool tip displays: Save Selection
        """
        EXPECTED_SAVE_SELECTION__TOOLTIP = 'Save Selection'
        RequestDataSourcesPanel.verify_toolbar_menu_tooltip(RequestDataSourcesPanel.Locator.ToolBar.SaveSelection, EXPECTED_SAVE_SELECTION__TOOLTIP, '06.01')
        
        """
            STEP 07.01 : Hover on  Clear Selection icon
            STEP 07.01 : Tool tip displays: Clear Selection
        """
        EXPECTED_REQUEST_ACTION_MOVE_DOWN_TOOLTIP = 'Clear Selection'
        RequestDataSourcesPanel.verify_toolbar_menu_tooltip(RequestDataSourcesPanel.Locator.ToolBar.ClearSelection, EXPECTED_REQUEST_ACTION_MOVE_DOWN_TOOLTIP, '07.01')
     
if __name__=='__main__' :
    unittest.main()
