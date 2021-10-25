'''-------------------------------------------------------------------------------------------
Reworked on January 17, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270484
Test Case Title =  Positioning Tab
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270484_TestClass(BaseTestCase):

    def test_C2270484(self):
       
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01 : Click on Positioning tab and hover on "Left" 
            STEP 01 Expected : Tool tip displays: Left Align Left
        """
        Ribbon.select_tab(Ribbon.Locators.PositioningTab.POSITIONING)
        LEFT_TOOLTIP = 'Left Align Left'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Left, LEFT_TOOLTIP, '01.01', crop_x1=40, image_size=80)
        
        
        """
            STEP 02 : Hover on "Right"
            STEP 02 Expected : Tool tip displays: Right Align Right
        """
        RIGHT_TOOLTIP = 'Right Align Right'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Right, RIGHT_TOOLTIP, '02.01', crop_x1=40, image_size=80)

        """
            STEP 03 : Hover on "Top"
            STEP 03 Expected : Tool tip displays: Top Align Top
        """
        TOP_TOOLTIP = 'Top Align Top'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Top, TOP_TOOLTIP, '03.01', crop_x1=40, image_size=80)
          
        """
            STEP 04 : Hover on "Bottom"
            STEP 04 Expected : Tool tip displays: Bottom Align Bottom 
        """
        BOTTOM_TOOLTIP = 'Bottom Align Bottom'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Bottom, BOTTOM_TOOLTIP, '04.01')
          
        """
            STEP 05 : Hover on "Center"
            STEP 05 Expected : Tool tip displays: Center Align center edges of the selected items with the dominant item
        """
        CENTER_TOOLTIP = 'Center  Align center edges of the selected items with the dominant item'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Center, CENTER_TOOLTIP, '05.01', crop_x1=40, image_size=80)
          
        """
            STEP 06 : Hover on "Middle"
            STEP 06 Expected : Tool tip displays: Middle Align middle edges of the selected items with the dominant item
        """
        MIDDLE_TOOLTIP = 'Middle  Align middle edges of the selected items with the dominant item'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.Middle, MIDDLE_TOOLTIP, '06.01', crop_x1=40, image_size=80)
          
        """
            STEP 07 : Hover on "Same Width"
            STEP 07 Expected : Tool tip displays: Same Width Align Same Width 
        """
        SAME_WIDTH_TOOLTIP = 'Same Width Align Same Width'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.SameWidth, SAME_WIDTH_TOOLTIP, '07.01', crop_x1=40, image_size=80)
          
        """
            STEP 08 : Hover on "Same Height"                     
            STEP 08 Expected : Tool tip displays: Same Height Align Same Height
        """
        SAME_HEIGHT_TOOLTIP = 'Same Height Align Same Height'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.SameHeight, SAME_HEIGHT_TOOLTIP, '08.01', crop_x1=40, image_size=80)
          
        """
            STEP 09 : Hover on "Same Size"
            STEP 09 Expected : Tool tip displays: Same Size Align Same Size
        """
        SAME_SIZE_TOOLTIP = 'Same Size Align Same Size'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.SameSize, SAME_SIZE_TOOLTIP, '09.01', crop_x1=40, image_size=80)
          
        """
            STEP 10 : Hover on 'Toggles Grid'
            STEP 10 Expected : Tool tip displays: Toggles Grid Toggles Grid
        """
        TOGGLE_GRID_TOOLTIP = 'Toggles Grid Toggles Grid'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.TogglesGrid, TOGGLE_GRID_TOOLTIP, '10.01')
          
        """
            STEP 11 : Hover on "Drag and Drop"
            STEP 11 Expected : Tool tip displays: Drag and Drop Toggle Drag and Drop
        """
        DRAG_AND_DROP_TOOLTIP = 'Drag and Drop Toggle Drag and Drop'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Positioning.DragandDrop, DRAG_AND_DROP_TOOLTIP, '11.01', image_size=80)
        
        """
            STEP 12 : Hover on "Top Left"
            STEP 12 Expected : Tool tip displays: Top Left Relate Left
        """
        TOP_LEFT_TOOLTIP = 'Top Left Relate Top Left'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.TopLeft, TOP_LEFT_TOOLTIP, '12.01', crop_x1=40, image_size=80, )
        
        """
            STEP 13 : Hover on "Top Right"
            STEP 13 Expected : Tool tip displays: Top Right Relate Top Right
        """
        TOP_RIGHT_TOOLTIP = 'Top Right Relate Top Right'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.TopRight, TOP_RIGHT_TOOLTIP, '13.01', crop_x1=40, image_size=80)
        
        """
            STEP 14 : Hover on "Bottom Right"
            STEP 14 Expected : Tool tip displays: Bottom Right Relate Bottom Right
        """
        BOTTOM_RIGHT_TOOLTIP = 'Bottom Right Relate Bottom Right'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.BottomRight, BOTTOM_RIGHT_TOOLTIP, '14.01', crop_x1=40, image_size=80)
        
        """
            STEP 15 : Hover on "Bottom Left"
            STEP 15 Expected : Tool tip displays: Bottom Left Relate Bottom Left
        """
        BOTTOM_LEFT_TOOLTIP = 'Bottom Left Relate Bottom Left'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.BottomLeft, BOTTOM_LEFT_TOOLTIP, '15.01', crop_x1=40, image_size=80)
        
        """
            STEP 16 : Hover on "Break"
            STEP 16 Expected : Tool tip displays: Break Break Relationship
        """
        BREAK_TOOLTIP = 'Break Break a relationship'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.Break, BREAK_TOOLTIP, '16.01', image_size=80)
        
        """
            STEP 17 : Hover on "Show"
            STEP 17 Expected : Tool tip displays: Show Show relationships between selected elements
        """
        SHOW_TOOLTIP = 'Show  Show relationships between selected elements'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.Relationships.Show, SHOW_TOOLTIP, '17.01', crop_x1=40, image_size=80)
        
        """
            STEP 18 : Hover on "Left"
            STEP 18 Expected : Tool tip displays: Left Left Text Alignment
        """
        LEFT_TOOLTIP = 'Left Left Text Alignment'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.TextAlignMent.Left, LEFT_TOOLTIP, '18.01')
        
        """
            STEP 19 : Hover on "Center"
            STEP 19 Expected : Tool tip displays: Center Center Text Alignment
        """
        CENTER_TOOLTIP = 'Center     Center Text Alignment'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.TextAlignMent.Center, CENTER_TOOLTIP, '19.01')
        
        """
            STEP 20 : Hover on "Right"
            STEP 20 Expected : Tool tip displays: Right Right Text Alignment
        """
        RIGHT_TOOLTIP = 'Right Right Text Alignment'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.TextAlignMent.Right, RIGHT_TOOLTIP, '20.01')
        
        """
            STEP 21 : Hover on "Full Justification"
            STEP 21 Expected : Tool tip displays: Full Justification Full Justification
        """
        FULL_JUSTIFICATION_TOOLTIP = 'Full Justification     Full Justification'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.PositioningTab.TextAlignMent.FullJustification, FULL_JUSTIFICATION_TOOLTIP, '21.01')
        
        """
            STEP 22 : Close HTMLPage1
        """
if __name__=='__main__' :
    unittest.main()