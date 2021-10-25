'''-------------------------------------------------------------------------------------------
Reworked on January 11, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271052
Test Case Title =  Text Editor
-----------------------------------------------------------------------------------------------'''

from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.environments import Tree
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2271052_TestClass(BaseTestCase):

    def test_C2271052(self):
        
        """
            COMMON VARIABLES
        """
        WF_FOLDER_PATH = 'Data Servers->EDASERVE->Applications->ibisamp->carinstorg.fex'
        CONTEXT_MENU = 'Open in Text Editor'
        
        """
            STEP 01.01 : Launch AppStudio, right click on any FEX from any Domain and click "Open in Text Editor"
        """
        Tree.right_click_on_webfocus_environment_item(WF_FOLDER_PATH)
        Tree.select_context_menu(CONTEXT_MENU)
        
        """
            STEP 02.01 : Hover on "Find" icon
            STEP 02.01 Expected : Find (Ctrl+F) Find the specified text
        """
        FIND_TOOLTIP = 'Find (Ctrl+F) Find the specified text'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Find.Find, FIND_TOOLTIP, '02.01', crop_x1=40, image_size=80)
        
        """
            STEP 02.02 : Hover on "Next" icon
            STEP 02.02 Expected : Find Next (F3) Find the next instance of the specified text 
        """
        NEXT_TOOLTIP = 'Find Next (F3)  Find the next instance of the specified text'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Find.Next, NEXT_TOOLTIP, '02.02', crop_x1=38, image_size=80)
        
        """
            STEP 02.03 : Hover on "Previous" icon
            STEP 02.03 Expected : Find Previous (Shift+F3) Find the previous instance of the specified text
        """
        PREVIOUS_TOOLTIP = 'Find Previous (Shift+F3)  Find the previous instance of the specified text'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Find.Previous, PREVIOUS_TOOLTIP, '02.03', crop_x1=40)
        
        """
            STEP 02.04 : Hover on "Replace" icon
            STEP 02.04 Expected : Replace (Ctrl+H) Replace specific text with different text
        """
        REPLACE_TOOLTIP = 'Replace (Ctrl+H)  Replace specific text with different text'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Find.Replace, REPLACE_TOOLTIP, '02.04')
        
        """
            STEP 02.05 : Hover on "Select All" icon
            STEP 02.05 Expected : Select All (Ctrl+A) Select or deselect the entire document
        """
        SELECT_ALL_TOOLTIP = 'Select All (Ctrl+A)  Select or deselect the entire document'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Find.SelectAll, SELECT_ALL_TOOLTIP, '02.05', image_size=80)
        
        """
            STEP 03.01 : Hover on "Toggle" icon
            STEP 03.01 Expected : Toggle Bookmark (Ctrl+F2) Toggle bookmark on or off 
        """
        TOGGLE_TOOLTIP = 'Toggle Bookmark (Ctrl+F2) Toggle bookmark on or off'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Bookmarks.Toggle, TOGGLE_TOOLTIP, '03.01', image_size=80)
        
        """
            STEP 03.02 : Hover on "Next" icon
            STEP 03.02 Expected : Next Bookmark (F2) Go to the next bookmark 
        """
        NEXT1_TOOLTIP = 'Next Bookmark (F2) Go to the next bookmark'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Bookmarks.Next, NEXT1_TOOLTIP, '03.02')
        
        """
            STEP 03.03 : Hover on "Previous" icon
            STEP 03.03 Expected : Previous Bookmark (Shift+F2) Go to previous bookmark
        """
        PREVIOUS1_TOOLTIP = 'Previous Bookmark (Shift+F2) Go to the previous bookmark'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Bookmarks.Previous, PREVIOUS1_TOOLTIP, '03.03', image_size=80)
        
        """
            STEP 03.04 : Hover on "Delete All" icon
            STEP 03.04 Expected : Delete All (Ctrl+Shift+F2) Delete all bookmarks
        """
        DELETE_ALL_TOOLTIP = 'Delete All (Ctrl+Shift+F2) Delete all bookmarks'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Bookmarks.DeleteAll, DELETE_ALL_TOOLTIP, '03.04')
        
        """
            STEP 04.01 : Hover on "Goto Line"
            STEP 04.01 Expected : Current Line Displays the line number for the cursor position - enter a number to scroll to a new line
        """
        GOTO_LINE_TOOLTIP = 'Current Line  Displays the line number for the cursor position - enter a number to scroll to a new line'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Position.GotoLine, GOTO_LINE_TOOLTIP, '04.01', image_size=80)
        
        """
            STEP 04.02 : Hover on "Show Line Numbers"
            STEP 04.02 Expected : Show Line numbers Turn line numbers on or off
        """
        SHOW_LINE_NUMBERS_TOOLTIP = 'Show Line Numbers Turn line numbers on or off'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Position.ShowLineNumbers, SHOW_LINE_NUMBERS_TOOLTIP, '04.02', image_size=80)
        
        """
            STEP 05.01 : Hover on "Upper" 
            STEP 05.01 Expected : Upper Case (Ctrl+Shift+U) Change the selected text to upper case
        """
        UPPER_TOOLTIP = 'Upper Case (Ctrl+Shift+U)  Change the selected text to upper case'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.CaseComment.Upper, UPPER_TOOLTIP, '05.01', crop_x1=40)
        
        """
            STEP 05.02 : Hover on "Lower" 
            STEP 05.02 Expected : Lower Case (Ctrl+U) Change the selected text to lower case
        """
        LOWER_TOOLTIP = 'Lower Case (Ctrl+U)  Change the selected text to lower case'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.CaseComment.Lower, LOWER_TOOLTIP, '05.02', crop_x1=40)
        
        """
            STEP 05.03 : Hover on "Change Case" 
            STEP 05.03 Expected : Change Case (Alt+F3) Change the case of the selected text
        """
        CHANGE_CASE_TOOLTIP = 'Change Case (Alt+F3)  Change the case of the selected text'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.CaseComment.ChangeCase, CHANGE_CASE_TOOLTIP, '05.03', crop_x1=41, image_size=80)
        
        """
            STEP 05.04 : Hover on "Add Comment" 
            STEP 05.04 Expected : Add Comment (Ctrl+M) Insert a comment marker at the beginning of the selected lines (s)
        """
        ADD_COMMENT_TOOLTIP = 'Add Comment (Ctrl+M)  Insert a comment marker at the beginning of the selected line(s)'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.CaseComment.AddComment, ADD_COMMENT_TOOLTIP, '05.04', crop_x1=28, image_size=82)
        
        """
            STEP 05.05 : Hover on "Remove Comment" 
            STEP 05.05 Expected : Remove Comment (Ctrl+R) Remove a comment marker from the beginning of the selected lines
        """
        REMOVE_COMMENT_TOOLTIP = 'Remove Comment (Ctrl+R)  Remove a comment marker from the beginning of the selected line(s)'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.CaseComment.RemoveComment, REMOVE_COMMENT_TOOLTIP, '05.05', image_size=81)
        
        """
            STEP 06.01 : Hover on "Font Style" 
            STEP 06.01 Expected : Font Style Set syntax font and color options 
        """
        FONT_STYLE_TOOLTIP = 'Font Style Set syntax font and color options'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Options.FontStyle, FONT_STYLE_TOOLTIP, '06.01')
        
        """
            STEP 06.02 : Hover on "Show Whitespace"
            STEP 06.02 Expected : Show Whitespace Characters(Ctrl+Shift+8) Show visual indicators for whitespace characters
        """
        SHOW_WHITESPACE_TOOLTIP = 'Show Whitespace Characters (Ctrl+Shift+8)  Show visual indicators for whitespace characters'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Options.ShowWhitespace, SHOW_WHITESPACE_TOOLTIP, '06.02', image_size=80)
        
        """
            STEP 06.03 : Hover on "Tab Size"
            STEP 06.03 Expected : Tab Size Number of spaces for each tab charcter
        """
        TAB_SIZE_TOOLTIP = 'Tab Size Number of spaces for each tab character'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Options.TabSize, TAB_SIZE_TOOLTIP, '06.03')
        
        """
            STEP 06.04 : Hover on "Tab Options" 
            STEP 06.04 Expected : Tab Options Options for handling tab characters
        """
        TAB_OPTIONS_TOOLTIP = 'Tab Options Options for handling tab characters'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Options.TabOptions, TAB_OPTIONS_TOOLTIP, '06.04', image_size=80)
        
        """
            STEP 06.05 : Hover on "Auto Indent"
            STEP 06.05 Expected : Auto Indent Automatically indent based on syntax
        """
        AUTO_INDENT_TOOLTIP = 'Auto Indent Automatically indent based on  syntax'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Options.AutoIndent, AUTO_INDENT_TOOLTIP, '06.05', image_size=82)
        
        """
            STEP 06.06 : Hover on "Reset All"
            STEP 06.06 Expected : Reset All Reset options to default values
        """
        RESET_ALL_TOOLTIP = 'Reset All Reset options to default values'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.TextEditorTab.Options.ResetAll, RESET_ALL_TOOLTIP, '06.06')
        
if __name__=='__main__' :
    unittest.main()