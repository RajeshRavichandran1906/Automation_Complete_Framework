'''-------------------------------------------------------------------------------------------
Reworked on January 21, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2227439
Test Case Title =  EnvironmentsTree_Menu_Tooltips
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.tools.common.environments import ToolBarMenu, HeaderButtons
from appstudio.lib.basetestcase import BaseTestCase
import unittest

class C2227439_TestClass(BaseTestCase):

    def test_C2227439(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01 : Hover on the icon "View options" on the Environments Tree
            STEP 01 Expected : Tool tip displays: View Options
        """
        EXPECTED_VIEW_OPTION_TOOLTIP = 'View Options'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.ViewOptions, EXPECTED_VIEW_OPTION_TOOLTIP, '01.01')
        
        """
            STEP 02 : Hover on the icon "All Files" on the Environments Tree
            STEP 02 Expected : Tool tip displays: All Files Show all content files
        """
        EXPECTED_ALL_FILES_TOOLTIP = 'All Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.AllFiles, EXPECTED_ALL_FILES_TOOLTIP, '02.01')
        
        """
            STEP 03 : Hover on the icon "Procedure Files" on the Environments Tree
            STEP 03 Expected : Tool tip displays: Procedure Files Show only Procedure files
        """
        EXPECTED_PROCEDURE_FILE_TOOLTIP = 'Procedure Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.ProcedureFiles, EXPECTED_PROCEDURE_FILE_TOOLTIP, '03.01')
        
        """
            STEP 04 : Hover on the icon "Master Files" on the Environments Tree
            STEP 04 Expected : Tool tip displays: Master Files Show only Master files
        """
        EXPECTED_MASTER_FILES_TOOLTIP = 'Master Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.MasterFiles, EXPECTED_MASTER_FILES_TOOLTIP, '04.01')
        
        """
            STEP 05 : Hover on the icon "HTML Files" on the Environments Tree
            STEP 05 Expected : Tool tip displays: HTML Files Show only HTML files
        """
        EXPECTED_MASTER_FILES_TOOLTIP = 'HTML Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.HTMLFiles, EXPECTED_MASTER_FILES_TOOLTIP, '05.01')
        
        """
            STEP 06 : Hover on the icon "Maintain Files" on the Environments Tree
            STEP 06 Expected : Tool tip displays: Maintain Files Show only Maintain files
        """
        EXPECTED_MAINTAIN_FILES_TOOLTIP = 'Maintain Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.MaintainFiles, EXPECTED_MAINTAIN_FILES_TOOLTIP, '06.01')
        
        """
            STEP 07 : Hover on the icon "Image Files" on the Environments Tree
            STEP 07 Expected : Tool tip displays: Image Files Show only Image files
        """
        EXPECTED_IMAGE_FILES_TOOLTIP = 'Image Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.ImageFiles, EXPECTED_IMAGE_FILES_TOOLTIP, '07.01')
        
        """
            STEP 08 : Hover on the icon "ReportCaster Files" on the Environments Tree
            STEP 08 Expected : Tool tip displays: ReportCaster Files Show only ReportCaster files
        """
        EXPECTED_REPORT_CASTER_TOOLTIP = 'ReportCaster Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.ReportCasterFiles, EXPECTED_REPORT_CASTER_TOOLTIP, '08.01')
        
        """
            STEP 09 : Hover on the icon "Library Files" on the Environments Tree
            STEP 09 Expected : Tool tip displays: Library Files Show only Library files
        """
        EXPECTED_LIBRARY_FILES_TOOLTIP = 'Library Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.LibraryFiles, EXPECTED_LIBRARY_FILES_TOOLTIP, '09.01')
        
        """
            STEP 10 : Hover on the icon "Other files" on the Environments Tree
            STEP 10 Expected : Tool tip displays: Other files Show only Other files
        """
        EXPECTED_OTHER_FILES_TOOLTIP = 'Other Files'
        ToolBarMenu.verify_tooltip(ToolBarMenu.Locator.OtherFiles, EXPECTED_OTHER_FILES_TOOLTIP, '10.01')
        
        """
            STEP 11 : Hover on the icon "Window Position" on the Environments Tree
            STEP 11 Expected : Tool tip displays: Window Position
        """
        EXPECTED_WINDOW_POSITION_TOOLTIP = 'Window Position'
        HeaderButtons.verify_tooltip(HeaderButtons.Locator.WindowPosition, EXPECTED_WINDOW_POSITION_TOOLTIP, '11.01')
        
        """
            STEP 12 : Hover on the icon "Auto Hide" on the Environments Tree
            STEP 12 Expected : Tool tip displays: Auto Hide
        """
        EXPECTED_AUTO_HIDE_TOOLTIP = 'Auto Hide'
        HeaderButtons.verify_tooltip(HeaderButtons.Locator.AutoHidePinned, EXPECTED_AUTO_HIDE_TOOLTIP, '12.01')
        
        """
            STEP 13 : Hover on the icon "Close" on the Environments Tree
            STEP 13 Expected : Tool tip displays: Close
        """
        EXPECTED_CLOSE_TOOLTIP = 'Close'
        HeaderButtons.verify_tooltip(HeaderButtons.Locator.Close, EXPECTED_CLOSE_TOOLTIP, '13.01')
        
if __name__=='__main__' :
    unittest.main()