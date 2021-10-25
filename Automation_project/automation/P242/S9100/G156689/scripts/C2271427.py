'''-------------------------------------------------------------------------------------------
Reworked on January 18, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271427
Test Case Title =  Image Tab tooltips
-----------------------------------------------------------------------------------------------'''
from appstudio import settings, keywords
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2271427_TestClass(BaseTestCase):

    def test_C2271427(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
       
        """
            STEP 01 : Click on Images tab. Hover on  File
            STEP 01 Expected : Tool tip displays:File. Add a new image from an existing file
        """
        EXPECTED_FILE_TOOLTIP = "File  Add a new image from an existing file"
        Ribbon.select_tab(Ribbon.Locators.ImagesTab.IMAGES)
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.NewImage.File, EXPECTED_FILE_TOOLTIP, '01.01', image_size=90)
        
        """
            STEP 01.02 : Hover on Field
            STEP 01.02 Expected : Tool tip displays:Field. Add a new image using a report field that identifies the image file name
        """
        EXPECTED_FIELD_TOOLTIP = "Field Add a new image using a report  field that identifies the image file name"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.NewImage.Field, EXPECTED_FIELD_TOOLTIP, '01.02', crop_x1=40, image_size=100)
        
        """
            STEP 02.01 : Hover on Image
            STEP 02.01 Expected :Tool tip displays:Current Image. Select an existing image to view or set properties
        """
        EXPECTED_IMAGE_TOOLTIP = "Current Image  Select an existing image to view or set properties"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.CurrentImage.Image, EXPECTED_IMAGE_TOOLTIP, '02.01', location=keywords.MIDDLE_LEFT, xoffset=8)
                                              
        """
            STEP 02.02 : Hover on Delete
            STEP 02.02 Expected :Tool tip displays: Delete. Delete the selected image
        """
        EXPECTED_DELETE_TOOLTIP = "Delete Delete the selected image"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.CurrentImage.Delete, EXPECTED_DELETE_TOOLTIP, '02.02', image_size=80)
    
        """
            STEP 02.03 : Hover on Drill Down
            STEP 02.03 Expected :Tool tip displays: Drill Down. Create a Drill down procedure for the selected image
        """
        EXPECTED_DRILLDOWN_TOOLTIP = "Drill Down  Create a Drill Down procedure for the selected image"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.CurrentImage.DrillDown, EXPECTED_DRILLDOWN_TOOLTIP, '02.03', crop_x1=27, image_size=80)
        
        """
            STEP 03.01  :Hover on Image Location
            STEP 03.01 Expected :Tool tip displays: Image Location. Location of the current image
        """
        EXPECTED_IMAGELOCATION_TOOLTIP = "Image Location Location of the current image"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.CurrentImage.ImageLocation, EXPECTED_IMAGELOCATION_TOOLTIP, '03.01', location=keywords.MIDDLE_LEFT, xoffset=8)
        
        """
            STEP 02.02 : Hover on Popup Desc.
            STEP 02.01 Expected :Tool tip displays: Popup Description. Pop-up description for the current image
        """
        EXPECTED_POPUPDESC_TOOLTIP = "Popup Description  Pop-up description for the current image"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.CurrentImage.PopupDesc, EXPECTED_POPUPDESC_TOOLTIP, '03.02', location=keywords.MIDDLE_LEFT, xoffset=8)
                                              
        """
            STEP 04.01  :Hover on Custom Size
            STEP 04.01 Expected :Tool tip displays: Custom Size. Specify a custom size for the current image
        """
        EXPECTED_CUSTOMSIZE_TOOLTIP = "Custom Size  Specify a custom size for the current image"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.Size.CustomSize, EXPECTED_CUSTOMSIZE_TOOLTIP, '04.01', image_size=90)
        
        """
            STEP 04.02  :Hover on Width
            STEP 04.02 Expected :Tool tip displays: Custom Width. Custom width for the current image
        """
        EXPECTED_WIDTH_TOOLTIP = "Custom Width  Custom width for the current image"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.Size.Width, EXPECTED_WIDTH_TOOLTIP, '04.02', location=keywords.MIDDLE_LEFT, xoffset=8, image_size=90)
                                              
        """
            STEP 04.03  :Hover on Height
            STEP 04.03 Expected :Tool tip displays: Custom Height. Custom height for the current image
        """
        EXPECTED_HEIGHT_TOOLTIP = "Custom Height Custom height for the current image"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.Size.Height, EXPECTED_HEIGHT_TOOLTIP, '04.03', location=keywords.MIDDLE_LEFT, xoffset=8, image_size=100)
                                              
        """
            STEP 05.01  :Hover on Line Break 
            STEP 05.01 Expected :Tool tip displays: Line Break. Create a line break after the current image 
        """
        EXPECTED_LINEBREAK_TOOLTIP = "Line Break Create a line break after the current"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.Options.LineBreak, EXPECTED_LINEBREAK_TOOLTIP, '05.01')
                                        
        """
            STEP 05.02  :Hover on Include As Reference
            STEP 05.02 Expected :Tool tip displays: Include As Reference. Include the current image as a reference
        """
        EXPECTED_INCLUDEASREF_TOOLTIP = "Include as Reference Include the current image as a reference"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.Options.IncludeAsReference, EXPECTED_INCLUDEASREF_TOOLTIP, '05.02')
                                              
        """
            STEP 05.03  :Hover on Preserve Ratio
            STEP 05.03 Expected :Tool tip displays: Preserve Ratio. Preserve the aspect ratio of the image
        """
        EXPECTED_PRESERVERATIO_TOOLTIP = "Preserve Ratio Preserve the aspect ratio of the image"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.Options.PreserveRatio, EXPECTED_PRESERVERATIO_TOOLTIP, '05.03')
                                              
        """
            STEP 05.04  :Hover on Show Images in Design View
            STEP 05.04 Expected :Tool tip displays: Show Images in Design View. Display or hide all images in the Design View
        """
        EXPECTED_SHOWIMAGESDV_TOOLTIP = "Show Images in Design View  Display or hide all images in the Design View"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ImagesTab.Options.ShowImagesDesignView, EXPECTED_SHOWIMAGESDV_TOOLTIP, '05.04', image_size=80)
                                              
if __name__=='__main__' :
    unittest.main()