'''-------------------------------------------------------------------------------------------
Reworked on January 21, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2223695
Test Case Title =  Home Tab Objects
-----------------------------------------------------------------------------------------------'''
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2223695_TestClass(BaseTestCase):

    def test_C2223695(self):
        
        """
            STEP 01 : Launch App Studio and click X to close '*Welcome to WebFOCUS App Studio* screen
            STEP 01 Expected : Default Ribbon is shown 
        """
        
        """
            STEP 02 : Hover on "Data"
            STEP 02 Expected : Tool tip displays: Data Manage metadata and Data Adapter configurations
        """
        DATA_TOOLTIP = 'Data  Manage metadata and Data Adapter configurations'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.Content.Data, DATA_TOOLTIP, '02.01', image_size=90)
        
        """
            STEP 03 : Hover on "Report"
            STEP 03 Expected : Tool tip displays: Report Wizard Create or open existing report procedures
        """
        REPORT_TOOLTIP = 'Report Wizard  Create or open existing report procedures'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.Content.Report, REPORT_TOOLTIP, '03.01', image_size=80)
        
        """
            STEP 04 : Hover on "Chart"
            STEP 04 Expected : Tool tip displays: Chart Wizard Create or open existing chart procedures
        """
        CHART_TOOLTIP = 'Chart Wizard  create or open existing chart procedures'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.Content.Chart, CHART_TOOLTIP, '04.01')
        
        """
            STEP 05 : Hover on "HTML/Document"
            STEP 05 Expected : Tool tip displays: HTML / Document Create or open existing HTML Pages and Multi-component Documents
        """
        HTML_DOCUMENT_TOOLTIP = 'HTML / Document  Create or open existing HTML Pages and Multi-component Documents'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.Content.HtmlDocument, HTML_DOCUMENT_TOOLTIP, '05.01', image_size=82)
         
        """
            STEP 06 : Hover on "Environments"
            STEP 06 Expected : Tool tip displays: Environments Configuration of WebFOCUS Environments Access
        """
        ENVIRONMENTS_TOOLTIP = 'Environments Configuration of WebFOCUS  Environments Access'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.Utilities.Environments, ENVIRONMENTS_TOOLTIP, '06.01')
        
        """
            STEP 07 : Hover on "Command Console"
            STEP 07 Expected : Tool tip displays: Command Console Facility where interactive WebFOCUS Commands may be entered
        """
        COMMAND_CONSOLE_TOOLTIP = 'Command Console  Facility where interactive WebFOCUS Commands may be entered'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.Utilities.CommandConsole, COMMAND_CONSOLE_TOOLTIP, '07.01', image_size=80)
        
        """
            STEP 08 : Hover on "Environments Tree"
            STEP 08 Expected : Tool tip displays: Toggle Configured Environments Tree  Show or hide the configured Environments Tree panel
        """
        ENVIRONMENT_TREE_TOOLTIP = 'Toggle Configured Environments Tree  Show or hide the Configured Environments Tree panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.View.EnvironmentsTree, ENVIRONMENT_TREE_TOOLTIP, '08.01', image_size=80)
        
        """
            STEP 09 : Hover on "Environments Detail "
            STEP 09 Expected : Tool tip displays: Toggle Configured Environments Detail Show or hide the configured Environments Detail panel
        """
        ENVIRONMENT_DETAILS_TOOLTIP = 'Toggle Configured Environments Detail  Show or hide the Configured Environments Detail panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.View.EnvironmentsDetail, ENVIRONMENT_DETAILS_TOOLTIP, '09.01')
        
        """
            STEP 10 : Hover on "File/Folder"
            STEP 10 Expected : Tool tip displays: Toggle File Properties Show or hide the File Properties panel
        """
        FILE_FOLDER_TOOLTIP = 'Toggle File Properties Show or hide the File Properties panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.View.FileFolderProperties, FILE_FOLDER_TOOLTIP, '10.01')
        
        """
            STEP 11 : Hover on "Procedure View"
            STEP 11 Expected : Tool tip displays: Toggle Procedure View Show or hide the Procedure View panel
        """
        PROCEDURE_VIEW_TOOLTIP = 'Toggle Procedure View Show or hide the Procedure View panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.View.ProcedureView, PROCEDURE_VIEW_TOOLTIP, '11.01')
        
        """
            STEP 12 : Hover on "Context Bar"
            STEP 12 Expected : Tool tip displays: Toggle Context Bar Show or hide the context bar under the ribbon
        """
        CONTEXT_BAR_TOOLTIP = 'Toggle Context Bar  Show or hide the context bar under the ribbon'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.View.ContextBar, CONTEXT_BAR_TOOLTIP, '12.01', image_size=80)
        
        """
            STEP 13 : Hover on "Status Bar"
            STEP 13 Expected : Toggle Status Bar Show/hide the status bar
        """
        STATUS_BAR_TOOLTIP = 'Toggle Status Bar  Show/Hide the status bar at the bottom of the screen'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.View.StatusBar, STATUS_BAR_TOOLTIP, '13.01', image_size=80)
        
        """
            STEP 14 : Hover on "Help Wizard"
            STEP 14 Expected : Toggle the Help Pane Show or hide the Help Pane
        """
        HELP_WIZARD_TOOLTIP = 'Toggle the Help Pane Show or hide the Help Pane'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.View.HelpWizard, HELP_WIZARD_TOOLTIP, '14.01')
        
        """
            STEP 15.01 : Verify the 'Environments Tree'
            STEP 15.01 Expected : Environments Tree (checked by default) 
        """
        Ribbon.verify_tab_item_is_selected(Ribbon.Locators.HomeTab.View.EnvironmentsTree, '15.01')
        
        """
            STEP 15.02 : Verify the 'Environments Detail'
            STEP 15.02 Expected : Environments Deatil (unchecked by default) 
        """
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.EnvironmentsDetail, '15.02')
        
        """
            STEP 15.03 : Verify the 'File/Folder Properties'
            STEP 15.03 Expected : File/Folder Properties (checked by default)
        """
        Ribbon.verify_tab_item_is_selected(Ribbon.Locators.HomeTab.View.FileFolderProperties, '15.03')
        
        """
            STEP 15.04 : Verify the 'Procedure View'
            STEP 15.04 Expected : Procedure View (checked by default) 
        """
        Ribbon.verify_tab_item_is_selected(Ribbon.Locators.HomeTab.View.ProcedureView, '15.04')
        
        """
            STEP 15.05 : Verify the 'Context Bar'
            STEP 15.05 Expected : Context Bar (unchecked by default)
        """
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.ContextBar, '15.05')
        
        """
            STEP 15.06 : Verify the 'Status Bar'
            STEP 15.06 Expected : Status Bar (unchecked by default)
        """
        Ribbon.verify_tab_item_is_unselected(Ribbon.Locators.HomeTab.View.StatusBar, '15.06')
        
        """
            STEP 15.07 : Verify the 'Help Wizard'
            STEP 15.07 Expected : Help Wizard (unchecked by default)
        """
        Ribbon.verify_tab_item_is_selected(Ribbon.Locators.HomeTab.View.StatusBar, '15.07')
        
        """
            STEP 16 : Hover on "Windows"
            STEP 16 Expected : Windows Manage open windows
        """
        WINDOWS_TOOLTIP = 'Windows Manage open windows'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.HomeTab.Window.Windows, WINDOWS_TOOLTIP, '16.01')
        
if __name__=='__main__' :
    unittest.main()