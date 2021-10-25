'''-------------------------------------------------------------------------------------------
Reworked on January 23, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270488
Test Case Title =  Tasks & Animations Panel
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.html_page import TaskAnimationPanel
import unittest

class C2270488_TestClass(BaseTestCase):
    
    settings.AppStudio.CLOSE_CANVAS = False

    def test_C2270488(self):
        
        """
            STEP 01.01 : Click on Tasks & Animations panel
        """
        TaskAnimationPanel.expand_task_animation_panel()
        
        """
            STEP 01.02 : Hover on Window position icon
            STEP 01.02 : Tool tip displays: Window Position 
        """
        EXPECTED_WINDOW_POSITION_TOOLTIP = 'Window Position'
        TaskAnimationPanel.verify_header_button_tooltip(TaskAnimationPanel.Locator.HeaderButtons.WindowPosition, EXPECTED_WINDOW_POSITION_TOOLTIP, '01.02')
        
        """
             STEP 01.03 : Hover on Auto Hide icon
             STEP 01.03 : Tool tip displays: Auto Hide
        """
        EXPECTED_AUTO_HIDE_TOOLTIP = 'Auto Hide'
        TaskAnimationPanel.verify_header_button_tooltip(TaskAnimationPanel.Locator.HeaderButtons.AutoHideUnPin, EXPECTED_AUTO_HIDE_TOOLTIP, '01.03')
         
        """
             STEP 01.04 : Hover on Close icon
             STEP 01.04 : Tool tip displays: Close
        """
        EXPECTED_CLOSE_TOOLTIP = 'Close'
        TaskAnimationPanel.verify_header_button_tooltip(TaskAnimationPanel.Locator.HeaderButtons.Close, EXPECTED_CLOSE_TOOLTIP, '01.04')
         
        """
            STEP 02.01 : Hover on New icon
            STEP 02.01 : Tool tip displays: New
        """
        EXPECTED_TASK_NEW_TOOLTIP = 'New'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.Tasks.ListOfNew, EXPECTED_TASK_NEW_TOOLTIP, '02.01')
         
        """
            STEP 02.02 : Hover on Delete icon
            STEP 02.02 : Tool tip displays: Delete
        """
        EXPECTED_TASK_DELETE_TOOLTIP = 'Delete'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.Tasks.ListOfDelete, EXPECTED_TASK_DELETE_TOOLTIP, '02.02')
        
        """
            STEP 03.01 : Hover on Requests selections icon
            STEP 03.01 : Tool tip displays: Requests selections
        """
        EXPECTED_REQUEST_SELECTIONS_TOOLTIP = 'Requests  selections'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.Tasks.RequestActionsSelections, EXPECTED_REQUEST_SELECTIONS_TOOLTIP, '03.01')
        
        """
            STEP 03.02 : Hover on Delete icon
            STEP 03.02 : Tool tip displays: Delete
        """
        EXPECTED_REQUEST_ACTION_DELETE_TOOLTIP = 'Delete'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.Tasks.RequestActionsDelete, EXPECTED_REQUEST_ACTION_DELETE_TOOLTIP, '03.02')
        
        """
            STEP 03.03 : Hover on Move up icon
            STEP 03.03 : Tool tip displays: Move up
        """
        EXPECTED_REQUEST_ACTION_MOVE_UP_TOOLTIP = 'Move up'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.Tasks.RequestActionsMoveUp, EXPECTED_REQUEST_ACTION_MOVE_UP_TOOLTIP, '03.03')
        
        """
            STEP 03.04 : Hover on Move down icon
            STEP 03.04 : Tool tip displays: Move down
        """
        EXPECTED_REQUEST_ACTION_MOVE_DOWN_TOOLTIP = 'Move down'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.Tasks.RequestActionsMoveDown, EXPECTED_REQUEST_ACTION_MOVE_DOWN_TOOLTIP, '03.04')
        
        """
            STEP 04.01 : Hover on New icon
            STEP 04.01 : Tool tip displays: New
        """
        EXPECTED_JQUERY_ANIMATIONS_NEW_TOOLTIP = 'New'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.ListOfNew, EXPECTED_JQUERY_ANIMATIONS_NEW_TOOLTIP, '04.01')
        
        """
            STEP 04.02 : Hover on Delete icon
            STEP 04.02 : Tool tip displays: Delete
        """
        EXPECTED_JQUERY_ANIMATIONS_DELETE_TOOLTIP = 'Delete'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.ListOfDelete, EXPECTED_JQUERY_ANIMATIONS_DELETE_TOOLTIP, '04.02')
        
        """
            STEP 04.03 : Hover on Requests selections icon
            STEP 04.03 : Tool tip displays: Add canvas selection
        """
        EXPECTED_JQUERY_ANIMATIONS_REQUEST_SELECTION_TOOLTIP = 'Add canvas selection'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.RequestSelection, EXPECTED_JQUERY_ANIMATIONS_REQUEST_SELECTION_TOOLTIP, '04.03')
        
        """
            STEP 04.04 : Hover on Add from list icon
            STEP 04.04 : Tool tip displays: Add from list
        """
        EXPECTED_ADD_FROM_LIST_TOOLTIP = 'Add from list'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.AddFromList, EXPECTED_ADD_FROM_LIST_TOOLTIP, '04.04')
        
        """
            STEP 04.05 : Hover on Delete icon
            STEP 04.05 : Tool tip displays: Remove
        """
        EXPECTED_JQUERY_ANIMATION_DELETE_TOOLTIP = 'Remove'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.Remove, EXPECTED_JQUERY_ANIMATION_DELETE_TOOLTIP, '04.05')
        
        """
            STEP 05.01 : Hover on Use location icon
            STEP 05.01 : Tool tip displays: Use location of selected target
        """
        EXPECTED_USE_LOCATION_TOOLTIP = 'Use location of selected target'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.LocationSettingUseLocation, EXPECTED_USE_LOCATION_TOOLTIP, '05.01')
        
        """
            STEP 05.02 : Hover on Start location icon
            STEP 05.02 : Tool tip displays: Start location setting
        """
        EXPECTED_START_LOCATION_TOOLTIP = 'Start location setting'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.LocationSettingStartLocation, EXPECTED_START_LOCATION_TOOLTIP, '05.02')
        
        """
            STEP 05.03 : Hover on Set location icon
            STEP 05.03 : Tool tip displays: Set location setting
        """
        EXPECTED_SET_LOCATION_TOOLTIP = 'Set location setting'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.LocationSettingSetLocation, EXPECTED_SET_LOCATION_TOOLTIP, '05.03')
        
        """
            STEP 05.04 : Hover on Cancel icon
            STEP 05.04 : Tool tip displays: Cancel setting
        """
        EXPECTED_CANCEL_SETTINGS_TOOLTIP = 'Cancel setting'
        TaskAnimationPanel.verify_properties_tooltip(TaskAnimationPanel.Locator.JqueryAnimations.LocationSettingCancel, EXPECTED_CANCEL_SETTINGS_TOOLTIP, '05.04')
        
if __name__=='__main__' :
    unittest.main()
