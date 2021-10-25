'''-------------------------------------------------------------------------------------------
Reworked on January 25, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270773
Test Case Title =  EnvironmentsDetail_Menu_Tooltips
-----------------------------------------------------------------------------------------------'''

from appstudio.tools.common.ribbon import Ribbon
from appstudio.tools.report import Report
from appstudio.lib.basetestcase import BaseTestCase
from appstudio import settings
import unittest

class C2271422_TestClass(BaseTestCase):

    def test_C2271422(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01 : Right click on folder, select New->Report, select ibisamp, click on car. mas and clcik Finish
        """
        Report.create_new_report_from_webfocus_environments_tree('ibisamp', 'car.mas')
        """
            STEP 02 : Hover on Filter
            STEP 02 Expected : Tool tip displays: Filter Create/edit a selection expression
        """
        EXPECTED_FILTER_TOOLTIP = 'Filter  Create/edit a selection expression'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Filter.Filter, EXPECTED_FILTER_TOOLTIP, '02.01', crop_x1=38, image_size=80)
        
        """
            STEP 03 : Hover on Header & Footer
            STEP 03 Expected : Tool tip displays: Header & Footer Manage report headers and footers
        """
        EXPECTED_HEADER_FOOTER_TOOLTIP = 'Header & Footer  Manage report headers and footers'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Report.HeaderFooter, EXPECTED_HEADER_FOOTER_TOOLTIP, '03.01')
        
        """
            STEP 04 : Hover on Column Total
            STEP 04 Expected : Tool tip displays: Column Total Manage column totals
        """
        EXPECTED_COLUMN_TOTAL_TOOLTIP = 'Column Total Manage column totals'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Report.ColumnTotal, EXPECTED_COLUMN_TOTAL_TOOLTIP, '04.01', crop_x1=30, image_size=80)
        
        """
            STEP 05 : Hover on Row Total
            STEP 05 Expected : Tool tip displays: Row Total Manage row total
        """
        EXPECTED_ROW_TOTAL_TOOLTIP = 'Row Total Manage row totals'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Report.RowTotal, EXPECTED_ROW_TOTAL_TOOLTIP, '05.01')
        
        """
            STEP 06 : Hover on Precision Report
            STEP 06 Expected : Tool tip displays: Precision Report Convert to Precision Report layout
        """
        EXPECTED_PRECISION_TOOLTIP = 'Precision Report Convert to Precision Report layout'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Report.PrecisionReport, EXPECTED_PRECISION_TOOLTIP, '06.01')
        
        """
            STEP 07 : Hover on Compound Document
            STEP 07 Expected : Tool tip displays: Compound Document Build a Compound Document
        """
        EXPECTED_COMPOUND_DOCUMENT_TOOLTIP = 'Compound Document Build a Compound Document'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Report.CompoundDocument, EXPECTED_COMPOUND_DOCUMENT_TOOLTIP, '07.01', crop_x1=29, image_size=90)
        
        """
            STEP 08 : Hover on Universal Concatenation
            STEP 08 Expected : Tool tip displays: Universal Concatenation Concatenate additional data sources to the report
        """
        EXPECTED_UNIVERSAL_CONCATENATION_TOOLTIP = 'Universal Concatenation  Concatenate additional data sources to the report'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Report.UniversalConcatenation, EXPECTED_UNIVERSAL_CONCATENATION_TOOLTIP, '08.01', image_size=80)
        
        """
            STEP 09 : Hover on Sorted Data
            STEP 09 Expected : Tool tip displays: Sorted Data Assumes the data is already sorted in the database
        """
        EXPECTED_SORTED_DATA_TOOLTIP = 'Sorted Data  Assumes the data is already sorted in the database'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Report.SortedData, EXPECTED_SORTED_DATA_TOOLTIP, '09.01', crop_x1=29, image_size=80)
        
        """
            STEP 10 : Hover on Custom Field Placement
            STEP 10 Expected : Tool tip displays: Custom Field Placement Allow sort fields to be moved from their default location
        """
        EXPECTED_CUSTOM_FIELD_PLACEMENT_TOOLTIP = 'Custom Field Placement  Allows sort fields to be moved from their default location'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Report.CustomFieldPlacement, EXPECTED_CUSTOM_FIELD_PLACEMENT_TOOLTIP, '10.01', crop_x1=29, image_size=80)
        
        """
            STEP 11 : Hover on None
            STEP 11 Expected : Tool tip displays: Traffic Lights Current condition for styling and drill downs
        """
        EXPECTED_NONE_TOOLTIP = 'Traffic Lights  Current condition for styling and drill downs'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.TrafficLights.TrafficLights, EXPECTED_NONE_TOOLTIP, '11.01', crop_x1=29, image_size=80)
        
        """
            STEP 12 : Hover on Change Theme
            STEP 12 Expected : Tool tip displays: Change Theme Swap out one theme for another
        """
        EXPECTED_CHANGE_THEME_TOOLTIP = 'Change Theme Swap out one theme for another'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.ChangeTheme, EXPECTED_CHANGE_THEME_TOOLTIP, '12.01', image_size=80)
        
        """
            STEP 13 : Hover on Manage Theme
            STEP 13 Expected : Tool tip displays: Manage Theme Select multiple theme files and order them
        """
        EXPECTED_MANAGE_THEME_TOOLTIP = 'Manage Theme Select multiple theme files and  order them'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.ManageTheme, EXPECTED_MANAGE_THEME_TOOLTIP, '13.01')
        
        """
            STEP 14 : Hover on Save Theme
            STEP 14 Expected : Tool tip displays: Save Theme Save current styling as a reusable theme
        """
        EXPECTED_SAVE_THEME_TOOLTIP = 'Save Theme  Save current styling as a reusable theme'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.SaveTheme, EXPECTED_SAVE_THEME_TOOLTIP, '14.01', image_size=80)
        
        """
            STEP 15 : Hover on Scope
            STEP 15 Expected : Tool tip displays: Scope Select what report styles are displayed/changed by the other style controls
        """
        EXPECTED_SCOPE_TOOLTIP = 'Scope  Select what report styles are displayed/changed by the other style controls'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Scope, EXPECTED_SCOPE_TOOLTIP, '15.01', image_size=80)
        
        """
            STEP 16.01 : Hover on Bold
            STEP 16.01 Expected : Tool tip displays: Bold Apply Bold Style
        """
        EXPECTED_BOLD_TOOLTIP = 'Bold Apply bold style'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Bold, EXPECTED_BOLD_TOOLTIP, '16.01', crop_x1=29, image_size=80) 
        
        """
            STEP 16.02 : Hover on Italic
            STEP 16.02 Expected : Tool tip displays: Italic Apply Italic Style
        """
        EXPECTED_ITALIC_TOOLTIP = 'Italic Apply italic style'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Italic, EXPECTED_ITALIC_TOOLTIP, '16.02', crop_x1=26, image_size=80) 
        
        """
            STEP 16.03 : Hover on Underline
            STEP 16.03 Expected : Tool tip displays: Underline Apply Underline Style
        """
        EXPECTED_UNDERLINE_TOOLTIP = 'Underline Apply underline style'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Underline, EXPECTED_UNDERLINE_TOOLTIP, '16.03', crop_x1=29, image_size=80) 
        
        """
            STEP 16.04 : Hover on No Underline
            STEP 16.04 Expected : Tool tip displays: No Underline Do not display underlines, even for drilldowns
        """
        EXPECTED_NO_UNDERLINE_TOOLTIP = 'No Underline  Do not display underlines, even for drill downs'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.NoUnderline, EXPECTED_NO_UNDERLINE_TOOLTIP, '16.04') 
        
        """
            STEP 17.01 : Hover on Left
            STEP 17.01 Expected : Tool tip displays: Left Apply left justification
        """
        EXPECTED_LEFT_TOOLTIP = 'Left Apply left justification'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Left, EXPECTED_LEFT_TOOLTIP, '17.01') 
        
        """
            STEP 17.02 : Hover on Center
            STEP 17.02 Expected : Tool tip displays: Center Apply center justification
        """
        EXPECTED_CENTER_TOOLTIP = 'Center Apply center justification'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Center, EXPECTED_CENTER_TOOLTIP, '17.02') 
        
        """
            STEP 17.03 : Hover on Right
            STEP 17.03 Expected : Tool tip displays: Right Apply right justification
        """
        EXPECTED_RIGHT_TOOLTIP = 'Right Apply right justification'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Right, EXPECTED_RIGHT_TOOLTIP, '17.03') 
        
        """
            STEP 17.04 : Hover on Default
            STEP 17.04 Expected : Tool tip displays: Apply default justification (numerics to right and alpha to the left)
        """
        EXPECTED_DEFAULT_TOOLTIP = 'Default  Apply default justification (numerics ro the right and alphas to the left)'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Default, EXPECTED_DEFAULT_TOOLTIP, '17.04', crop_x1=29, image_size=80)
        
        """
            STEP 18.01 : Hover on Report Width
            STEP 18.01 Expected : Tool tip displays: Report Width Set report width options
        """
        EXPECTED_REPORT_WIDTH_TOOLTIP = 'Report Width Set report width options'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.ReportWidth, EXPECTED_REPORT_WIDTH_TOOLTIP, '18.01', image_size=80)
        
        """
            STEP 18.02 : Hover on Copy Style
            STEP 18.02 Expected : Tool tip displays: Copy Style Copy the current style settings
        """
        EXPECTED_COPY_STYLE_TOOLTIP = 'Copy Style Copy the current style settings'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.CopyStyle, EXPECTED_COPY_STYLE_TOOLTIP, '18.02', crop_x1=29, image_size=80)
        
        """
            STEP 18.03 : Hover on Paste Style
            STEP 18.03 Expected : Tool tip displays: Paste Style Paste the copied style settings
        """
        EXPECTED_PASTE_STYLE_TOOLTIP = 'Paste Style Paste the copied style settings'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.PasteStyle, EXPECTED_PASTE_STYLE_TOOLTIP, '18.03', image_size=80)
        
        """
            STEP 19.01 : Hover on Arial
            STEP 19.01 Expected : Tool tip displays: Font Name set the font name
        """
        EXPECTED_ARIAL_TOOLTIP = 'Font Name Set the font name'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Arial, EXPECTED_ARIAL_TOOLTIP, '19.01')  
        
        """
            STEP 19.02 : Hover on Color
            STEP 19.02 Expected : Tool tip displays: Color Set the font color
        """
        EXPECTED_COLOR_TOOLTIP = 'Color Set the font color'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Color, EXPECTED_COLOR_TOOLTIP, '19.02', crop_x1=29, image_size=80)   
        
        """
            STEP 19.03 : Hover on Background Color
            STEP 19.03 Expected : Tool tip displays: Background Color Set the background color
        """
        EXPECTED_BACKGROUND_COLOR_TOOLTIP = 'Background Color Set the background color'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.BackgroundColor, EXPECTED_BACKGROUND_COLOR_TOOLTIP, '19.03', crop_x1=29, image_size=80)   
        
        """
            STEP 19.04 : Hover on Defaults
            STEP 19.04 Expected : Tool tip displays: Defaults Restore style settings to default values
        """
        EXPECTED_DEFAULT_TOOLTIP = 'Defaults  Restore style settings to default values'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.Defaults, EXPECTED_DEFAULT_TOOLTIP, '19.04', crop_x1=29, image_size=80)    
        
        """
            STEP 19.05 : Hover on Border/Grid
            STEP 19.05 Expected : Tool tip displays: Borders/Grid Turn on Borders or Grid lines
        """
        EXPECTED_BORDER_GRID_TOOLTIP = 'Borders/Grid Turn on Borders or Grid lines'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.BorderGrid, EXPECTED_BORDER_GRID_TOOLTIP, '19.05')  
        
        """
            STEP 19.06 : Hover on User style
            STEP 19.06 Expected : Tool tip displays: User Style Set User Format Style Blocks
        """
        EXPECTED_USER_STYLE_TOOLTIP = 'User Format Set User Format Style Blocks'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Style.UserStyle, EXPECTED_USER_STYLE_TOOLTIP, '19.06') 
        
        """
            STEP 19.07 : Hover on Drill Down Links
            STEP 19.07 Expected : Tool tip displays: Drill Down Create a Drill Down procedure
        """
        EXPECTED_DRILL_DOWN_TOOLTIP = 'Drill Down Create a Drill Down procedure'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ReportTab.Links.DrillDown, EXPECTED_DRILL_DOWN_TOOLTIP, '19.07', image_size=80) 
        
if __name__=='__main__' :
    unittest.main()

