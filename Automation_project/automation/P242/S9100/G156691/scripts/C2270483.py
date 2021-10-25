'''-------------------------------------------------------------------------------------------
Reworked on January 09, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270483
Test Case Title =  Controls Tab
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270483_TestClass(BaseTestCase):
    
    settings.AppStudio.CLOSE_CANVAS = False

    def test_C2270483(self):
        
        """
            STEP 01 : Click on Controls tab and Hover on Edit Box
            STEP 01 Expected : Tool tip displays: Edit Box  Insert Edit Box
        """
        Ribbon.select_tab(Ribbon.Locators.ControlsTab.CONTROLS)
        EXPECTED_EDIT_BOX_TOOLTIP = 'Edit Box Insert Edit Box'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.EditBox, EXPECTED_EDIT_BOX_TOOLTIP, '01.01', image_size=80)
        
        """
            STEP 02 : Hover on Hidden
            STEP 02 : Tool tip displays: Hidden Insert Hidden
        """
        EXPECTED_HIDDEN_TOOLTIP = 'Hidden Insert Hidden'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Hidden, EXPECTED_HIDDEN_TOOLTIP, '02.01')
        
        """
            STEP 03 : Hover on Drop Down
            STEP 03 : Tool tip displays: Drop Down Insert Drop Down
        """
        EXPECTED_DROP_DOWN_TOOLTIP = 'Drop Down Insert Drop Down'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.DropDown, EXPECTED_DROP_DOWN_TOOLTIP, '03.01')
        
        """
            STEP 04 : Hover on List Box
            STEP 04 : Tool tip displays: List Box Insert List Box
        """
        EXPECTED_LIST_BOX_TOOLTIP = 'List Box Insert List Box'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.ListBox, EXPECTED_LIST_BOX_TOOLTIP, '04.01')
        
        """
            STEP 05 : Hover on Double list
            STEP 05 : Tool tip displays: Double list Insert Double list
        """
        EXPECTED_DOUBLE_LIST_TOOLTIP = 'Double list        Insert Double List'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Doublelist, EXPECTED_DOUBLE_LIST_TOOLTIP, '05.01')
        
        """
            STEP 06 : Hover on Radio Button
            STEP 06 : Tool tip displays: Radio Button Insert Radio Button
        """
        EXPECTED_RADIO_BUTTON_TOOLTIP = 'Radio Button Insert Radio Button'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.RadioButton, EXPECTED_RADIO_BUTTON_TOOLTIP, '06.01')
        
        """
            STEP 07 : Hover on Check Box
            STEP 07 : Tool tip displays: Check Box Insert Check Box
        """
        EXPECTED_CHECK_BOX_TOOLTIP = 'Check Box Insert Check Box'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.CheckBox, EXPECTED_CHECK_BOX_TOOLTIP, '07.01')
        
        """
            STEP 08 : Hover on Text Area
            STEP 08 : Tool tip displays: Text Area Insert Text Area
        """
        EXPECTED_TEXT_AREA_TOOLTIP = 'Text Area Insert Text area'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.TextArea, EXPECTED_TEXT_AREA_TOOLTIP, '08.01')
        
        """
            STEP 09 : Hover on Tree
            STEP 09 : Tool tip displays: Tree Insert Single source Tree
        """
        EXPECTED_TREE_TOOLTIP = 'Tree Insert Single source Tree'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Tree, EXPECTED_TREE_TOOLTIP, '09.01', crop_x1=40, image_size=80)
        
        """
            STEP 10 : Hover on Tree Sub-menu Single source Tree control
            STEP 10 : Tool tip displays: Tree Insert Single source Tree 
        """
        EXPECTED_SINGLE_SOURCE_TREE_TOOLTIP = 'Tree Insert Single source Tree'
        Ribbon.verify_tab_item_submenu_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Tree, Ribbon.Locators.ControlsTab.Controls.Tree_SingleSource, EXPECTED_SINGLE_SOURCE_TREE_TOOLTIP, '10.01')
        
        """
            STEP 11 : Hover on Sub-menu Mutli source Tree control
            STEP 11 : Tool tip displays: Multi source Tree Insert Multi source Tree
        """
        EXPECTED_MULTI_SOURCE_TREE_TOOLTIP = 'Multi source Tree Insert Multi source Tree'
        Ribbon.verify_tab_item_submenu_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Tree, Ribbon.Locators.ControlsTab.Controls.Tree_MultiSource, EXPECTED_MULTI_SOURCE_TREE_TOOLTIP, '11.01')
        
        """
            STEP 12 : Hover on Calendar
            STEP 12 : Tool tip displays: Calendar Insert Calendar
        """
        EXPECTED_CALENDER_TOOLTIP = 'Calendar Insert Calendar'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Calendar, EXPECTED_CALENDER_TOOLTIP, '12.01')
        
        """
            STEP 13 : Hover on Slider
            STEP 13 : Tool tip displays: Horizontal Slider Insert Horizontal Slider
        """
        EXPECTED_SLIDER_TOOLTIP = 'Horizontal Slider Insert Horizontal Slider'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Slider, EXPECTED_SLIDER_TOOLTIP, '13.01', image_size=80)
        
        """
            STEP 14 : Hover on Slider Sub-menu Horizontal
            STEP 14 : Tool tip displays: Horizontal Slider Insert Horizontal Slider
        """
        EXPECTED_SLIDER_SUBMENU_HORIZANTAL_TOOLTIP = 'Horizontal Slider Insert Horizontal Slider'
        Ribbon.verify_tab_item_submenu_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Slider, Ribbon.Locators.ControlsTab.Controls.Slider_Horizontal, EXPECTED_SLIDER_SUBMENU_HORIZANTAL_TOOLTIP, '14.01')
        
        """
            STEP 15 : Hover on Slider Sub-menu Vertical
            STEP 15 : Tool tip displays: Vertical Slider Insert Vertical Slider
        """
        EXPECTED_SLIDER_SUBMENU_VERTICAL_TOOLTIP = 'Vertical Slider Insert Vertical Slider'
        Ribbon.verify_tab_item_submenu_tooltip_text(Ribbon.Locators.ControlsTab.Controls.Slider, Ribbon.Locators.ControlsTab.Controls.Slider_Vertical, EXPECTED_SLIDER_SUBMENU_VERTICAL_TOOLTIP, '15.01', image_size=80)
        
if __name__=='__main__' :
    unittest.main()
