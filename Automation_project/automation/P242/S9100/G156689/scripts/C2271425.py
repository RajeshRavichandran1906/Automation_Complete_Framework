'''-------------------------------------------------------------------------------------------
Reworked on January 18, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271425
Test Case Title =  Layout Tab tooltips
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2271425_TestClass(BaseTestCase):

    def test_C2271425(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
       
        """
            STEP 01 : Click on Layout tab. Hover on Margins 
            STEP 01 Expected : Tool tip displays: Margins. Set Margins Options
        """
        EXPECTED_MARGINS_TOOLTIP = "Margins Set margin options"
        Ribbon.select_tab(Ribbon.Locators.LayoutTab.LAYOUT)
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.LayoutTab.PageSetup.Margins, EXPECTED_MARGINS_TOOLTIP, '01.01')
        
        """
            STEP 01.02 : Hover on Report Page
            STEP 01.02 Expected :Tool tip displays: Report Page. Set the report page orientation
        """
        EXPECTED_REPORTPAGE_TOOLTIP = "Report Page Set the report page orientation"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.LayoutTab.PageSetup.ReportPage, EXPECTED_REPORTPAGE_TOOLTIP, '01.02')
        
        """
            STEP 01.03 : Hover on Paper Type
            STEP 01.03 Expected :Tool tip displays: Paper Type. Set the report page size
        """
        EXPECTED_PAPERTYPE_TOOLTIP = "Paper Type Set the report page size"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.LayoutTab.PageSetup.PaperType, EXPECTED_PAPERTYPE_TOOLTIP, '01.03')
        
        """
            STEP 01.04 : Hover on Units
            STEP 01.04 Expected :Tool tip displays:  Units. Set the report page unit size
        """
        EXPECTED_UNITS_TOOLTIP = "Units Set the report page unit size"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.LayoutTab.PageSetup.Units, EXPECTED_UNITS_TOOLTIP, '01.04')
    
        """
            STEP 01.05 :  Page Numbering
            STEP 01.05 Expected :Tool tip displays: Page Numbering. Turn page numbering on of off
        """
        EXPECTED_PAGENUMBERINGL_TOOLTIP = "Page Numbering Turn page numbering on or off"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.LayoutTab.PageSetup.PageNumbering, EXPECTED_PAGENUMBERINGL_TOOLTIP, '01.05')
        
        """
            STEP 02.01  :Hover on Cell Padding
            STEP 01.06 Expected :Tool tip displays:  Cell Padding. Set the amount of space between the gap values in Cascading Style Sheet
        """
        EXPECTED_CELLPADDING_TOOLTIP = "Cell Padding Set the amount of space     between the gap values in the Cascading Style Sheet"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.LayoutTab.Report.CellPadding, EXPECTED_CELLPADDING_TOOLTIP, '01.06', image_size=65)
        
        
if __name__=='__main__' :
    unittest.main()