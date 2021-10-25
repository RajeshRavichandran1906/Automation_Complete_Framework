'''-------------------------------------------------------------------------------------------
Reworked on January 11, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271329
Test Case Title =  Positioning Tab
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2271329_TestClass(BaseTestCase):

    def test_C2271329(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
       
        """
            STEP 01 : Click on Positioning tab and hover on "Left"
            STEP 01 Expected : Tool tip displays: Left Align Left
        """
        EXPECTED_LEFT_ALIGN_TOOLTIP = "Left Align Left"
        Ribbon.select_tab(Ribbon.Locators.PositioningTab.POSITIONING)
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Left, EXPECTED_LEFT_ALIGN_TOOLTIP, '01.01', crop_x1=40)
        
        """
            STEP 02 : Hover on "Right"
            STEP 02 : Tool tip displays: Right Align Right
        """
        EXPECTED_RIGHT_ALIGN_TOOLTIP = 'Right Align Right'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Right, EXPECTED_RIGHT_ALIGN_TOOLTIP, '02.01', crop_x1=40, image_size=80)
        
        """
            STEP 03 : Hover on "Top"
            STEP 03 : Tool tip displays: Top Align Top
        """
        EXPECTED_TOP_ALIGN_TOOLTIP = 'Top Align Top'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Top, EXPECTED_TOP_ALIGN_TOOLTIP, '03.01', crop_x1=40)
        
        """
            STEP 04 : Hover on "Bottom"
            STEP 04 : Tool tip displays: Bottom Align Bottom
        """
        EXPECTED_BOTTOM_ALIGN_TOOLTIP = 'Bottom Align Bottom'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Bottom, EXPECTED_BOTTOM_ALIGN_TOOLTIP, '04.01')
        
        """
            STEP 05 : Hover on "Center"
            STEP 05 : Tool tip displays: Center Align center edges of the selected items with the dominant item
        """
        EXPECTED_CENTER_ALIGN_TOOLTIP = 'Center  Align center edges of the selected items with the dominant item'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Center, EXPECTED_CENTER_ALIGN_TOOLTIP, '05.01', crop_x1=38, image_size=80)
        
        """
            STEP 06 : Hover on "Middle"
            STEP 06 : Tool tip displays: Middle Align middle edges of the selected items with the dominant item
        """
        EXPECTED_MIDDLE_ALIGN_TOOLTIP = 'Align middle edges of the selected items with the dominant item'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Middle, EXPECTED_MIDDLE_ALIGN_TOOLTIP, '06.01', crop_x1=40, crop_y1=20)
        
        """
            STEP 07 : Hover on "Same Width"
            STEP 07 : Tool tip displays: Same Width Align Same Width
        """
        EXPECTED_SAME_WIDTH_ALIGN_TOOLTIP = 'Same Width Align Same Width'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.SameWidth, EXPECTED_SAME_WIDTH_ALIGN_TOOLTIP, '07.01', crop_x1=40)
        
        """
            STEP 08 : Hover on "Same Height"
            STEP 08 : Tool tip displays: Same Height Align same Height
        """
        EXPECTED_SAME_HEIGHT_ALIGN_TOOLTIP = 'Same Height Align Same Height'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.SameHeight, EXPECTED_SAME_HEIGHT_ALIGN_TOOLTIP, '08.01', crop_x1=45)
        
        """
            STEP 09 :  "Same Size"
            STEP 09 : Tool tip displays: Same Size Align Same Size
        """
        EXPECTED_SAME_SIZE_ALIGN_TOOLTIP = 'Same Size Align Same Size'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.SameSize, EXPECTED_SAME_SIZE_ALIGN_TOOLTIP, '09.01', crop_x1=40)
        
        """
            STEP 10 : Hover on "Toggles Grid"
            STEP 10 : Tool tip displays:Toggles Grid Toggles Grid
        """
        EXPECTED_TOGGLES_GRID_TOOLTIP = 'Toggles Grid Toggles Grid'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.TogglesGrid, EXPECTED_TOGGLES_GRID_TOOLTIP, '10.01')
        
        """
            STEP 11 : Hover on "Bottom Left"
            STEP 11 : Tool tip displays: Bottom Left Relate Bottom Left
        """
        EXPECTED_BOTTOM_LEFT_TOOLTIP = 'Bottom Left Relate Bottom Left'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.BottomLeft, EXPECTED_BOTTOM_LEFT_TOOLTIP, '11.01', crop_x1=40)
        
        """
            STEP 12 : Hover on "Break"
            STEP 12 : Tool tip displays: Break Break Relationship
        """
        EXPECTED_BREAK_TOOLTIP = 'Break Break a relationship'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.Break, EXPECTED_BREAK_TOOLTIP, '12.01')
        
        """
            STEP 13 : Hover on "Show"
            STEP 13 :Show relationships between selected elements
        """
        EXPECTED_SHOW_TOOLTIP = 'show  show relationships between selected elements'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.Show, EXPECTED_SHOW_TOOLTIP, '13.01', crop_x1=45)
        
        """
            STEP 14 : Hover on "Left"
            STEP 14 : Left Left Text Alignment
        """
        EXPECTED_LEFT_TOOLTIP = 'Left Left Text Alignment'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.TextAlignMent.Left, EXPECTED_LEFT_TOOLTIP, '14.01', image_size=400)
        
        """
            STEP 15 : Hover on "Center"
            STEP 15 : Center Center Text Alignment
        """
        EXPECTED_CENTER_TOOLTIP = 'Center     Center Text Alignment'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.TextAlignMent.Center, EXPECTED_CENTER_TOOLTIP, '15.01')
        
        """
            STEP 16 : Hover on "Right"
            STEP 16 : Right Right Text Alignment
        """
        EXPECTED_RIGHT_TOOLTIP = 'Right Right Text Alignment'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.TextAlignMent.Right, EXPECTED_RIGHT_TOOLTIP, '16.01')
        
        """
            STEP 17 : Hover on "Full Justification"
            STEP 17 : Full Justification Full Justification
        """
        EXPECTED_FULL_JUSTIFY_TOOLTIP = 'Full Justification     Full Justification'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.TextAlignMent.FullJustification, EXPECTED_FULL_JUSTIFY_TOOLTIP, '17.01')
        
if __name__=='__main__' :
    unittest.main()