'''-------------------------------------------------------------------------------------------
Reworked on January 10, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270482
Test Case Title =  Components Tab
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
from appstudio.tools.common.ribbon import Ribbon
from appstudio.tools import document as Document
import unittest

class C2270482_TestClass(BaseTestCase):

    def test_C2270482(self):
       
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01 : Launch AppStudio, right click on any folder, New->HTML/Document , 
            click Next, click Finish. Hover on "Report"
        """
        Tree.right_click_on_webfocus_environment_item()
        Tree.select_context_menu('New->HTML/Document')
        Document.WizardWindow.select_file_type(Document.WizardWindow.Locators.HtmlDocumentWizard.Buttons.Next)
        Document.WizardWindow.select_file_type(Document.WizardWindow.Locators.HtmlDocumentWizard.Buttons.Finish)

        REPORT_TOOLTIP = 'Report Insert New Report'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Reports.Report, REPORT_TOOLTIP, '01.01')
        
        """
            STEP 02 : Hover on "Chart"
            STEP 02 Expected : Tool tip displays: Chart Insert New Chart
        """
        CHART_TOOLTIP = 'Chart Insert New Chart'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Reports.Chart, CHART_TOOLTIP, '02.01')

        """
            STEP 03 : Hover on "Image"
            STEP 03 Expected : Tool tip displays: Image Insert Image
        """
        IMAGE_TOOLTIP = 'Image Insert Image'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Image, IMAGE_TOOLTIP, '03.01', image_size=51)
          
        """
            STEP 04 : Hover on "Hyperlink"
            STEP 04 Expected : Tool tip displays: Hyperlink Insert Hyperlink
        """
        HYPERLINK_TOOLTIP = 'Hyperlink Insert Hyperlink'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Hyperlink, HYPERLINK_TOOLTIP, '04.01')
          
        """
            STEP 05 : Hover on "Button"
            STEP 05 Expected : Tool tip displays: Button Insert Push Button
        """
        BUTTON_TOOLTIP = 'Button Insert Push Button'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Button, BUTTON_TOOLTIP, '05.01')
          
        """
            STEP 06 : Hover on "Reset"
            STEP 06 Expected : Tool tip displays: Reset Insert Reset Button
        """
        RESET_TOOLTIP = 'Insert Reset Button'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Reset, RESET_TOOLTIP, '06.01')
          
        """
            STEP 07 : Hover on "Save Selection"
            STEP 07 Expected : Tool tip displays: Save Selection Insert Save Selection Button
        """
        SAVE_SELECTION_TOOLTIP = 'Save Selection Insert Save Selection Button'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.SaveSelection, SAVE_SELECTION_TOOLTIP, '07.01')
          
        """
            STEP 08 : Hover on "Label"                     
            STEP 08 Expected : Tool tip displays: Label Insert Label
        """
        LABEL_TOOLTIP = 'Label Insert Label'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Label, LABEL_TOOLTIP, '08.01', image_size=70)
          
        """
            STEP 09 : Hover on "Text"
            STEP 09 Expected : Tool tip displays: Text Insert Text
        """
        TEXT_TOOLTIP = 'Text Insert Text'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Text, TEXT_TOOLTIP, '09.01')
          
        """
            STEP 10 : Hover on 'Line'
            STEP 10 Expected : Tool tip displays: Line Insert Line
        """
        LINE_TOOLTIP = 'Line Insert Line'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Line, LINE_TOOLTIP, '10.01', crop_x1=40)
          
        """
            STEP 11 : Hover on "Menu"
            STEP 11 Expected : Tool tip displays: Horizontal Menu Insert Horizontal Menu
        """
        MENU_TOOLTIP = 'Horizontal Menu Insert Horizontal Menu'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Menu, MENU_TOOLTIP, '11.01')
        
        """
            STEP 12 : Hover on "Table"
            STEP 12 Expected : Tool tip displays: Table Insert Table
        """
        TABLE_TOOLTIP = 'Table     Insert Table'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Table, TABLE_TOOLTIP, '12.01')
        
        """
            STEP 13 : Hover on "Grid"
            STEP 13 Expected : Tool tip displays: Grid Insert Grid
        """
        GRID_TOOLTIP = 'Grid Insert Grid'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.GenericElements.Grid, GRID_TOOLTIP, '13.01', image_size=80)
        
        """
            STEP 14 : Hover on "Form"
            STEP 14 Expected : Tool tip displays: Form Insert new Form 
        """
        FORM_TOOLTIP = 'Form Insert new form'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Containers.Form, FORM_TOOLTIP, '14.01')
        
        """
            STEP 15 : Hover on "Tab"
            STEP 15 Expected : Tool tip displays: Tab Insert Tab
        """
        TAB_TOOLTIP = 'Tab Insert Tab'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Containers.Tab, TAB_TOOLTIP, '15.01')
        
        """
            STEP 16 : Hover on "Accordion"
            STEP 16 Expected : Tool tip displays: Vertical Accordion Insert Vertical Accordion
        """
        ACCORDION_TOOLTIP = 'Vertical Accordion Insert Vertical Accordion'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Containers.Accordion, ACCORDION_TOOLTIP, '16.01')
        
        """
            STEP 17 : Hover on "Window"
            STEP 17 Expected : Tool tip displays: Window Insert Window
        """
        WINDOW_TOOLTIP = 'Window Insert Window'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Containers.Window, WINDOW_TOOLTIP, '17.01', image_size=51)
        
        """
            STEP 18 : Hover on "Output Widget"
            STEP 18 Expected : Tool tip displays: Output Widget Output Widget 
        """
        OUTPUT_WIDGET_TOOLTIP = 'Output Widget        Output Widget'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Containers.OutputWidget, OUTPUT_WIDGET_TOOLTIP, '18.01', image_size=80)
        
        """
            STEP 19 : Hover on "Maintain Data App"
            STEP 19 Expected : Tool tip displays: Maintain Data App Maintain Data App Window
        """
        MAINTAIN_DATA_APP_TOOLTIP = 'Maintain Data App Maintain Data App Window'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Containers.MaintainDataApp, MAINTAIN_DATA_APP_TOOLTIP, '19.01')
        
        """
            STEP 20 : Hover on "Group Box"
            STEP 20 Expected : Tool tip displays: Group Box Insert Group Box
        """
        GROUP_BOX_TOOLTIP = 'Group Box Insert Group Box'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Containers.GroupBox, GROUP_BOX_TOOLTIP, '20.01', image_size=80)
        
        """
            STEP 21 : Hover on "Panel"
            STEP 21 Expected : Tool tip displays: Panel Insert Panel 
        """
        PANEL_TOOLTIP = 'Panel Insert Panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Containers.Panel, PANEL_TOOLTIP, '21.01', image_size=80)
        
        """
            STEP 22 : Hover on "Frame"
            STEP 22 Expected : Tool tip displays: Frame Insert Frame
        """
        FRAME_TOOLTIP = 'Frame Insert Frame'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Objects.Frame, FRAME_TOOLTIP, '22.01', image_size=51)
        
        """
            STEP 23 : Hover on "Flash"
            STEP 23 Expected : Tool tip displays: Flash Insert Flash Content 
        """
        FLASH_TOOLTIP = 'Flash Insert Flash Content'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Objects.Flash, FLASH_TOOLTIP, '23.01')
        
        """
            STEP 24 : Hover on "Map"
            STEP 24 Expected : Tool tip displays: Map Insert Map
        """
        MAP_TOOLTIP = 'Map     Insert Map'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Objects.Map, MAP_TOOLTIP, '24.01', image_size=81)
        
        """
            STEP 25 : Hover on "GIS Flex Viewer"
            STEP 25 Expected : Tool tip displays: GIS Flex Viewer...Insert GIS Flex Viewer...
        """
        GIS_FLEX_VIEWER_TOOLTIP = 'GIS Flex Viewer...       Insert GIS Flex Viewer...'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Objects.GISFlexViewer, GIS_FLEX_VIEWER_TOOLTIP, '25.01', image_size=51)
        
        """
            STEP 26 : Hover on "</> HTML"
            STEP 26 Expected : Tool tip displays: HTML Insert HTML Object
        """
        HTML_TOOLTIP = 'HTML Insert HTML Object'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Objects.HTML, HTML_TOOLTIP, '26.01', crop_x1=40)
    
        """
            STEP 27 : Hover on "ESRI Map"
            STEP 27 Expected : Tool tip displays: ESRI Map Insert ESRI Map
        """
        ESRI_MAP_TOOLTIP = 'ESRI Map Insert ESRI Map'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ComponentsTab.Objects.ESRIMap, ESRI_MAP_TOOLTIP, '27.01')
        
if __name__=='__main__' :
    unittest.main()