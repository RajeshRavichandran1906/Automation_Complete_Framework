'''-------------------------------------------------------------------------------------------
Reworked on January 24, 2019
@author: Prabhakaran

Test Case Link   =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/8784522
Test Case Title  =  Home Tab Objects
-----------------------------------------------------------------------------------------------'''
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C8784522_TestClass(BaseTestCase):

    def test_C8784522(self):
        
        """
        COMMON VARIABLES
        """
        RibbonLocators = Ribbon.Locators
        
        """
            STEP 01 : Launch App Studio and click X to close '*Welcome to WebFOCUS App Studio* screen
            STEP 01 Expected : Default Ribbon is shown 
        """
        
        """
            STEP 02 : Hover over the Create icon
            STEP 02 Expected : Tool tip displays: Create Create a Data Source Definition
        """
        CREATE_TOOLTIP = 'Create Create a Data Source Definition'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Data.Create, CREATE_TOOLTIP, '02.01')
        
        """
            STEP 03 : Hover over the Design icon
            STEP 03 Expected : Tool tip displays: Design Design Data Source Definitions
        """
        DESIGN_TOOLTIP = 'Design Design Data Source Definitions'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Data.Design, DESIGN_TOOLTIP, '03.01')
        
        """
            STEP 04 : Hover over the Open icon
            STEP 04 Expected : Tool tip displays: Open Open a existing Data Source Definition
        """
        OPEN_TOOLTIP = 'Open  Open an existing Data Source Definition'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Data.Open, OPEN_TOOLTIP, '04.01', image_size=67)
        
        """
            STEP 05 : Hover over the Upload Data icon
            STEP 05 Expected : Tool tip displays: Upload Data Upload data files from your local machine to server application folders
        """
        UPLOAD_TOOLTIP = 'Upload Data Upload data files from your local machine to server application folders'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Data.UploadData, UPLOAD_TOOLTIP, '05.01', image_size=80)
         
        """
            STEP 06 : Hover over the More icon
            STEP 06 Expected : Tool tip displays: More Additional Data functions
        """
        MORE_TOOLTIP = 'More Additional Data functions'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Data.More, MORE_TOOLTIP, '06.01')
        
        """
            STEP 07 : Hover over the Report icon
            STEP 07 Expected : Tool tip displays : Report Wizard Create or open existing report procedures
        """
        REPORT_TOOLTIP = 'Report Wizard  Create or open existing report procedures'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Content.Report, REPORT_TOOLTIP, '07.01', image_size=80)
        
        """
            STEP 08 : Hover over the Chart icon
            STEP 08 Expected : Tool tip displays: Chart Wizard Create or open existing chart procedures
        """
        CHART_TOOLTIP = 'Chart Wizard  create or open existing chart procedures'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Content.Chart, CHART_TOOLTIP, '08.01')
        
        """
            STEP 09 : Hover over the HTML/Document icon
            STEP 09 Expected : Tool tip displays: HTML / Document Create or open existing HTML Pages and Multi-component Documents
        """
        HTMLDOCUMENT_TOOLTIP = 'HTML / Document  Create or open existing HTML Pages and Multi-component Documents'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Content.HtmlDocument, HTMLDOCUMENT_TOOLTIP, '09.01', image_size=85)
        
        """
            STEP 10 : Hover the mouse over the Connect icon in Home ribbon
            STEP 10 Expected : Tool tip displays:Connect Add new or manage existing adapter connections
        """
        CONNECT_TOOLTIP = 'Connect  Add new or manage existing adapter connections'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Configuration.Connect, CONNECT_TOOLTIP, '10.01', image_size=80)
        
        """
            STEP 11 : Hover the mouse over the Environments icon in Home ribbon
            STEP 11 Expected : Tool tip displays : Environments Configuration of WebFOCUS Environments Access
        """
        ENVIROMENTS_TOOLTIP = 'Environments  Configuration of WebFOCUS Environments Access'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.Configuration.Environments, ENVIROMENTS_TOOLTIP, '11.01', crop_x1=40, image_size=80)
        
        """
            STEP 12 : Hover mouse over Environments Tree in the Home ribbon
            STEP 12 Expected : Tool tip displays: Toggle Configured Environments Tree Show or hide the configured Environments Tree panel
        """
        ENVIROMENTSTREE_TOOLTIP = 'Toggle Configured Environments Tree  Show or hide the Configured Environments Tree panel'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.View.EnvironmentsTree, ENVIROMENTSTREE_TOOLTIP, '12.01', image_size=80)
        
        """
            STEP 13 : Hover mouse over Environments Detail in the Home ribbon
            STEP 13 Expected : Tool tip displays: Toggle Configured Environments Detail Show or hide the configured Environments Detail panel
        """
        ENVIROMENTSDETAIL_TOOLTIP = 'Toggle Configured Environments Detail  Show or hide the Configured Environments Detail panel'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.View.EnvironmentsDetail, ENVIROMENTSDETAIL_TOOLTIP, '13.01', image_size=80)
        
        """
            STEP 14 : Hover over File/Folder Properties in the Home ribbon.
            STEP 14 Expected : Tool tip displays: Toggle File Properties Show or hide the File Properties panel
        """
        FILEFOLDER_TOOLTIP = 'Toggle File Properties  Show or hide the File Properties panel'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.View.FileFolderProperties, FILEFOLDER_TOOLTIP, '14.01', crop_x1=25, image_size=65)
        
        """
            STEP 15 : Hover mouse over the Procedure View in the Home ribbon
            STEP 15 Expected : Tool tip displays:  Toggle Procedure View Show or hide the Procedure View panel
        """
        PROCEDURE_TOOLTIP = 'Toggle Procedure View  Show or hide the Procedure View panel'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.View.ProcedureView, PROCEDURE_TOOLTIP, '15.01', image_size=65)
        
        """
            STEP 16 : Hover mouse over the Context Bar in the Home ribbon
            STEP 16 Expected : Tooltip displays : Toggle Context Bar Show or hide the context bar under the ribbon
        """
        CONTEXTBAR_TOOLTIP = 'Toggle Context Bar  Show or hide the context bar under the ribbon'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.View.ContextBar, CONTEXTBAR_TOOLTIP, '16.01', image_size=70)
        
        """
            STEP 17 : Hover mouse over the Status Bar in the Home ribbon
            STEP 17 Expected : Tooltip displays: Toggle Status Bar Show or hide the status bar
        """
        STATUSBAR_TOOLTIP = 'Toggle Status Bar  Show/Hide the status bar at the bottom of the screen'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.View.StatusBar, STATUSBAR_TOOLTIP, '17.01', image_size=65)
        
        """
            STEP 18 : Hover mouse over the Help Wizard in the Home ribbon
            STEP 18 Expected : Tooltip displays : Toggle the Help Pane Show or hide the Help Pane
        """
        HELP_TOOLTIP = 'Toggle the Help Pane Show or hide the Help Pane'
        Ribbon.verify_tab_item_tooltip_text(RibbonLocators.HomeTab.View.HelpWizard, HELP_TOOLTIP, '18.01', image_size=55)
        
if __name__=='__main__' :
    unittest.main()