'''-------------------------------------------------------------------------------------------
Reworked on January 18, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271426
Test Case Title =  Verify the contextual menu for a folder and a new folder under Domains.
-----------------------------------------------------------------------------------------------'''
from appstudio import settings, keywords
from appstudio.lib.basetestcase import BaseTestCase
import unittest
from appstudio.tools.common.ribbon import Ribbon

class C2271426_TestClass(BaseTestCase):
    
    def test_C2271426(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01.01 : Click on "View" tab
        """
        Ribbon.select_tab(Ribbon.Locators.ViewTab.VIEW)
    
        """
            STEP 01.02 : Hover on "Dimension"
            STEP 01.02 Expected : Tool tip displays: Dimension View View the hierarchical structure of the data  
        """
        DIMENSION_TOOLTIP = 'Dimension View  View the hierarchical structure of the data'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.ObjectInspector.Dimension, DIMENSION_TOOLTIP, '01.02', image_size=80)
        
        """
            STEP 01.03 : Hover on "List"
            STEP 01.03 Expected : Tool tip displays: List View View fields in a list
        """
        LIST_TOOLTIP = 'List View View fields in a list'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.ObjectInspector.List, LIST_TOOLTIP, '01.03')
        
        """
            STEP 01.04 : Hover on "Tree"
            STEP 01.04 Expected : Tool tip displays: Forecast Add a Forecast column to the report
        """
        TREE_TOOLTIP = 'Tree View View fields by type'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.ObjectInspector.Tree, TREE_TOOLTIP, '01.04', crop_x1=40)
        
        """
            STEP 02.01 : Hover on "Qualified Fields"
            STEP 02.01 Expected : Tool tip displays: Show Qualified Fields Displays any list of field names as qualified filed names, which include data source and table names
        """
        QUALIFIED_TOOLTIP = 'Show Qualified Fields  Displays any list of field names as qualified field names, which includes data source and table names'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.ObjectInspector.QualifiedFields, QUALIFIED_TOOLTIP, '02.01', image_size=82)
        
        """
            STEP 02.02 : Hover on "Details Section"
            STEP 02.02 Expected : Tool tip displays: Field Details Section. Display the field details section in the Object Inspector field tab
        """
        DETAILS_SECTION_TOOLTIP = 'Field Details Section  Display the field details section in the Object Inspector field tab'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.ObjectInspector.DetailsSection, DETAILS_SECTION_TOOLTIP, '02.02', crop_x1=27, image_size=80)
        
        """
            STEP 03.01 : Hover on "Boundaries"
            STEP 03.01 Expected : Tool tip displays: Boundaries Display the boundaries for report objects, such as headings and footings
        """
        BOUNDARIES_TOOLTIP = 'Boundaries  Display the boundaries for report objects, such as headings and footings'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.General.Boundaries, BOUNDARIES_TOOLTIP, '03.01', image_size=80)
        
        """
            STEP 03.02 : Hover on "Test Data"
            STEP 03.02 Expected : Tool tip displays: Test Data Display test data for report objects when designing a report
        """
        TEST_DATA_TOOLTIP = 'Test Data  Display test data for report objects when designing a report'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.General.TestData, TEST_DATA_TOOLTIP, '03.02', image_size=90)
        
        """
            STEP 03.03 : Hover on "Show Field Tooltips"
            STEP 03.03 Expected : Tool tip displays: Tooltips for Fields Display tooltips for fields when designing a report
        """
        SHOW_FIELD_TOOLTIP = 'Tooltips for Fields  Display tooltips for fields when designing a report'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.General.ShowFieldTooltips, SHOW_FIELD_TOOLTIP, '03.03', image_size=80)
        
        """
            STEP 03.04 : Hover on "Show Invisible Fields"
            STEP 03.04 Expected : Tool tip displays: Invisible Fields. Display hidden fields
        """
        SHOW_INVISIBLE_TOOLTIP = 'Invisible Fields Display hidden fields'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.General.ShowInvisibleFields, SHOW_INVISIBLE_TOOLTIP, '03.04')
        
        """
            STEP 03.05 : Hover on "Show Ruler"
            STEP 03.05 Expected : Tool tip displays: Show Ruler Display a standard ruler at the top and side of the report canvas
        """
        SHOW_RULER_TOOLTIP = 'Show Ruler  Display a standard ruler at the top and side of the report canvas'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.General.ShowRuler, SHOW_RULER_TOOLTIP, '03.05', image_size=80)
        
        """
            STEP 04.01 : Hover on "Limit Field Lengths"
            STEP 04.01 Expected : Tool tip displays: Limit Fields Lengths. Limit the maximum length 
        """
        LIMIT_FIELD_LENGTH_TOOLTIP = 'Limit Field Lengths Limit the maximum length of a field or maximum number of characters that can appear in the report'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.FieldLength.LimitFieldLengths, LIMIT_FIELD_LENGTH_TOOLTIP, '04.01', image_size=80)
        
        """
            STEP 04.02 : Hover on "Field Length Limit"
            STEP 04.02 Expected : Tool tip displays: Field Length Limit Enter the maximum length of a field or maximum number of characters that can appear in the report 
        """
        FIELD_LENGTH_LIMIT_TOOLTIP = 'Field Length Limit  Enter the maximum length of a field or maximum number of characters that can appear in the report'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.FieldLength.FieldLengthLimit, FIELD_LENGTH_LIMIT_TOOLTIP, '04.02', image_size=80)
        
        """
            STEP 04.03 : Hover on "2"
            STEP 04.03 Expected : Tool tip displays: Repetitions Select the number of test data instances that appear for a field
        """
        REPETITIONS_TOOLTIP = 'Repetitions Select the number of test data instances that appear for a field'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.Repetitions.Repetitions, REPETITIONS_TOOLTIP, '04.03', location=keywords.MIDDLE_RIGHT, xoffset=-7, image_size=80)
        
        """
            STEP 04.04 : Hover on "100"
            STEP 04.04 Expected : Tool tip displays: Zoom Level Select or specify the size (magnification/scale) of the report canvas
        """
        ZOOM_LEVEL_TOOLTIP = 'Zoom Level Select or specify the size (magnification/scale) of the report canvas'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.Zoom.Zoom, ZOOM_LEVEL_TOOLTIP, '04.04', location=keywords.MIDDLE_RIGHT, xoffset=-7, image_size=80)
        
        """
            STEP 05.01 : Hover on "View Generated SQL"
            STEP 05.01 Expected : Tool tip displays: View Generated SQL. View the SQL generated for this RDBMS-based report
        """
        VIEW_GENERATED_SQL_TOOLTIP = 'View Generated SQL  View the SQL generated for this RDBMS-based report'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.Sql.ViewGeneratedSql, VIEW_GENERATED_SQL_TOOLTIP, '05.01', crop_x1=40, image_size=65)
        
        """
            STEP 05.02 : Hover on "Width"
            STEP 05.02 Expected : Tool tip displays: Virtual Screen Size Width Width (in pixels) of the report area that displays on screen for HTML output
        """
        WIDTH_TOOLTIP= 'Virtual Screen Size Width  Width (in pixels) of the report area that displays on screen for HTML output'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.VirtualScreenSize.Width, WIDTH_TOOLTIP, '05.02', image_size=90, xoffset=-5)
        
        """
            STEP 05.03 : Hover on "Height"
            STEP 05.03 Expected : Tool tip displays: Virtual Screen Size Height. Height (in pixels) of the report area that displays on screen for HTML output
        """
        HEIGHT_TOOLTIP = 'Virtual Screen Size Height  Height (in pixels) of the report area that displays on screen for HTML output'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.ViewTab.VirtualScreenSize.Height, HEIGHT_TOOLTIP, '05.03', image_size=80, xoffset=-5)
        
if __name__=='__main__' :
    unittest.main()