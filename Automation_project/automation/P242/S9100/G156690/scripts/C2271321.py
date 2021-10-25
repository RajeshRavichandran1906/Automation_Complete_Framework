'''-------------------------------------------------------------------------------------------
Created on September 05, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271321
Test Case Title =  Components Group
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
from appstudio.tools.common.ribbon import Ribbon
from appstudio.tools import document as Document
import unittest

class C2271321_TestClass(BaseTestCase):

    def test_C2271321(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        REPORT_TOOLTIP = 'Report Insert New Report'
        CHART_TOOLTIP  = 'Chart Insert New Chart'
        IMAGE_TOOLTIP  = 'Image Insert Image'
        TEXT_TOOLTIP   = 'Text Insert Text'
        LINE_TOOLTIP   = 'Line Insert Line'
        
        """
            STEP 01 : Launch AppStudio, right click on any folder, New->HTML/Document , 
            select Document(PDF, Excel...) radio button, click Next, click Finish
        """
        Tree.right_click_on_webfocus_environment_item()
        Tree.select_context_menu('New->HTML/Document')
        Document.WizardWindow.select_file_type(Document.WizardWindow.Locators.HtmlDocumentWizard.FileType.Document)
        Document.WizardWindow.select_file_type(Document.WizardWindow.Locators.HtmlDocumentWizard.Buttons.Next)
        Document.WizardWindow.select_file_type(Document.WizardWindow.Locators.HtmlDocumentWizard.Buttons.Finish)
        
        """
            STEP 01 Expected : Insert Tab is the default
        """
        Ribbon.verify_tab_is_selected(Ribbon.Locators.InsertTab.INSERT, '01.01')
        
        """
            STEP 02 : Hover on Report
            STEP 02 Expected : Tool tip displays: Report Insert New Report
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Components.Report, REPORT_TOOLTIP, '02.01')
        
        """
            STEP 03 : Hover on Chart
            STEP 03 Expected : Tool tip displays: Tool tip displays: Chart Insert New Chart
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Components.Chart, CHART_TOOLTIP, '03.01')
        
        """
            STEP 04 : Hover on Image
            STEP 04 Expected : Tool tip displays: Tool tip displays: Image Insert Image
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Components.Image, IMAGE_TOOLTIP, '04.01', image_size=70)
        
        """
            STEP 05 : Hover on Text
            STEP 05 Expected : Tool tip displays: Text Insert Text
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Components.Text, TEXT_TOOLTIP, '05.01')
        
        """
            STEP 06 : Hover on Line
            STEP 06 Expected : Tool tip displays: Line Insert Line
        """
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.InsertTab.Components.Line, LINE_TOOLTIP, '06.01', crop_x1=40)
        
if __name__=='__main__' :
    unittest.main()