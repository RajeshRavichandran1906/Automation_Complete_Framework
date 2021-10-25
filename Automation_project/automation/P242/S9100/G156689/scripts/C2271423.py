'''-------------------------------------------------------------------------------------------
Reworked on January 17, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271423
Test Case Title =  Format Tab tooltips
-----------------------------------------------------------------------------------------------'''
from appstudio import settings, keywords
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2271423_TestClass(BaseTestCase):

    def test_C2271423(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
       
        """
            STEP 01 : Click on Format tab. Hover on HTML 
            STEP 01 Expected : Tool tip displays: HTML. Create an HTML report
        """
        EXPECTED_HTML_TOOLTIP = "HTML Create an HTML report"
        Ribbon.select_tab(Ribbon.Locators.FormatTab.FORMAT)
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.Html, EXPECTED_HTML_TOOLTIP, '01.01', image_size=80)
        
        """
            STEP 01.02 : Hover on Active Report 
            STEP 01.02 Expected :Tool tip displays: HTML. Create an Active Report
        """
        EXPECTED_AHTML_TOOLTIP = "HTML Analytic Document  Create an HTML Anatytic Document"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.ActiveReport, EXPECTED_AHTML_TOOLTIP, '01.02', crop_x1=40)
        
        """
            STEP 01.03 : Hover on PDF 
            STEP 01.03 Expected :Tool tip displays: HTML. Create a PDF report
        """
        EXPECTED_PDF_TOOLTIP = "PDF Create a PDF report"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.Pdf, EXPECTED_PDF_TOOLTIP, '01.03', crop_x1=40)
        
        """
            STEP 01.04 : Hover on Active PDF
            STEP 01.04 Expected :Tool tip displays:  HTML. Create a PDF report for Adobe Falsh Player
        """
        EXPECTED_APDF_TOOLTIP = "PDF Analytic Document Create a PDF Analytic Document"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.ActivePdf, EXPECTED_APDF_TOOLTIP, '01.04')
    
        """
            STEP 01.05 : Hover on Excel
            STEP 01.05 Expected :Tool tip displays: HTML. Create an Excel report
        """
        EXPECTED_EXCEL_TOOLTIP = "Excel Create an Excel report"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.Excel, EXPECTED_EXCEL_TOOLTIP, '01.05')
        
        """
            STEP 01.06  :Hover on PowerPoint
            STEP 01.06 Expected :Tool tip displays:  HTML. Create an PowerPoint report
        """
        EXPECTED_POWERPOINT_TOOLTIP = "PowerPoint Create a PowerPoint report"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.PowerPoint, EXPECTED_POWERPOINT_TOOLTIP, '01.06')
        
        """
            STEP 02.01 : Hover on Output Format
            STEP 02.01 Expected :Tool tip displays:  Output Format. Select the Report output format
        """
        EXPECTED_OUTPUTFORMAT_TOOLTIP = "Output Format Select the Report output format"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.OutputFormat, EXPECTED_OUTPUTFORMAT_TOOLTIP, '02.01', image_size=80)
        
        """
            STEP 02.02 Hover on Output Format Options
            STEP 02.02 Expected :Tool tip displays:   Set options for the current Output Format
        """
        EXPECTED_OUTPUT_FORMAT_OPTIONS_TOOLTIP = "Output Format Options  Set options for the current report Output Format"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.OutputFormatOptions, EXPECTED_OUTPUT_FORMAT_OPTIONS_TOOLTIP, '02.02', image_size=80)
        
        """
            STEP 02.03 :Hover on Destination (PCHOLD)
            STEP 02.03 Expected :Tool tip displays: Destination. Destination of the report output
        """
        EXPECTED_DESTINATION_TOOLTIP = "Destination Destination of the report output"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.OutputTypes.DestinationPchold, EXPECTED_DESTINATION_TOOLTIP, '02.03')
        
        """
            STEP 03.01 : Hover on Table of Contents
            STEP 03.01 Expected :Tool tip displays: Table of Contents. Add a table of contents
        """
        EXPECTED_TOC_TOOLTIP = "Table of Contents Add a table of contents"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Navigation.TableOfContents, EXPECTED_TOC_TOOLTIP, '03.01')
        
        """
            STEP 03.02 : Hover on Freeze
            STEP 03.02 Expected :Tool tip displays: Freeze. Freeze position of headings, footings, titles, or totals when scrolling data
        """
        EXPECTED_FREEZE_TOOLTIP = "Freeze  Freeze position of headings, footings, titles or totals when scrolling data"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Navigation.Freeze, EXPECTED_FREEZE_TOOLTIP, '03.02', crop_x1=40, image_size=80)
        
        """
            STEP 03.03 : Hover on On-Demand Paging
            STEP 03.03 Expected :Tool tip displays: On-Demand Paging. Start display of report data before all pages are ready
        """
        EXPECTED_ODP_TOOLTIP = "On-Demand Paging  Start display of report data before all pages are ready"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Navigation.OnDemandPaging, EXPECTED_ODP_TOOLTIP, '03.03', image_size=85)
        
        """
            STEP 03.04 : Hover on Autodrill
            STEP 03.04 Expected :Tool tip displays: Auto Drill. Create an automatic drill down
        """
        EXPECTED_AUTODRILL_TOOLTIP = "Auto Drill Create an automatic drilldown"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Navigation.AutoDrill, EXPECTED_AUTODRILL_TOOLTIP, '03.04', image_size=80)
        
        """
            STEP 04.01 : Hover on Popup Desc.
            STEP 04.01 Expected :Tool tip displays: Popup Desc. Enable pop-up field descriptions for column titles 
        """
        EXPECTED_POPUP_TOOLTIP = "Popup Desc.  Enable pop-up field descriptions for column titles"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Features.PopupDesc, EXPECTED_POPUP_TOOLTIP, '04.01', image_size=80)
        
        """
            STEP 04.02 : Hover on Accordion Report
            STEP 04.02 Expected :Tool tip displays: Accordion. Create an accordion report
        """
        EXPECTED_ACCORDION_TOOLTIP = "Accordion Create an accordion report"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Features.AccordionReport, EXPECTED_ACCORDION_TOOLTIP, '04.02')
        
        """
            STEP 04.03 : Hover on Repeat Sort Value
            STEP 04.03 Expected :Tool tip displays: Repeat Sort Value. Display repeated sort values 
        """
        EXPECTED_REPEAT_SORT_TOOLTIP = "Repeat Sort Value Display repeated sort values"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Features.RepeatSortValue, EXPECTED_REPEAT_SORT_TOOLTIP, '04.03')
        
        """
            STEP 04.04 :Hover on arrow next to Default
            STEP 04.04 Expected :Tool tip displays: Lines per Page. Set the number of lines displayed on each report page 
        """
        EXPECTED_LPP_TOOLTIP = "Lines per Page  Set the number of lines displayed on each report page"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Features.LinesPerPage, EXPECTED_LPP_TOOLTIP, '04.04', location=keywords.MIDDLE_RIGHT, xoffset=-5, image_size=80)
        
        """
            STEP 04.05 : Hover on Accessibility
            STEP 04.05 Expected :Tool tip displays: Accessibility. Set Section 508 Accessibility options
        """
        EXPECTED_ACCESSBILITY_TOOLTIP = "Accessibility  Set Section 508 Accessibility options"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Features.Accessibility, EXPECTED_ACCESSBILITY_TOOLTIP, '04.05', image_size=80)
        
        """
            STEP 04.06 : Hover on Mailing Labels
            STEP 04.06 Expected :Tool tip displays: Mailing Labels. Set options for mailing labels
        """
        EXPECTED_MAILING_TOOLTIP = "Mailing Labels Set options for mailing labels"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.FormatTab.Features.MailingLables, EXPECTED_MAILING_TOOLTIP, '04.06', image_size=80)
        
        
if __name__=='__main__' :
    unittest.main()