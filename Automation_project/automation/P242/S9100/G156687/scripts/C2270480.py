'''-------------------------------------------------------------------------------------------
Reworked on January 18, 2019
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/C2270480
Test Case Title =  Help Drop Down 
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270480_TestClass(BaseTestCase):
    
    def test_C2270480(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        MENU_LOCATOR = Ribbon.Locators.HelpMenu.Help
        HELP_TOPIC_TOOLTIP = 'Help Topics List Help topics'
        FOCAL_POINT_FORUMS_TOOLTIP  = 'Focal Point Forums Launch the IBI Focal Point website'
        DISPLAY_WELCOME_SCREEN_TOOLTIP = 'Display Welcome Screen Display Welcome Screen'
        RESET_LAYOUT_TOOLTIP = 'Reset Layout  Reset ribbon, style and panels to installed settings'
        ABOUT_TOOLTIP = 'About  Display program information, version number and copyright'
        
        """
            STEP 01 : Hover on 'Help Topics'
            STEP 01 Expected : Tool tip displays: Help Topics List Help Topics
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.HelpMenu.HelpTopics, HELP_TOPIC_TOOLTIP, '01.01', image_size=80)
    
        """
            STEP 02 : Hover on 'Focal Point Forums'
            STEP 02 Expected : Tool tip displays: Focal Point Forums. Launch the IBI Focal Point website
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.HelpMenu.FocalPointsForums, FOCAL_POINT_FORUMS_TOOLTIP, '02.01', image_size=100)
        
        """
            STEP 03 : Hover on 'Display Welcome Screen'
            STEP 03 Expected : Tool tip displays: Display Welcome Screen Display Welcome Screen
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.HelpMenu.DisplayWelcomeScreen, DISPLAY_WELCOME_SCREEN_TOOLTIP, '03.01', image_size=80)
        
        """
            STEP 04 : Hover on 'Reset Layout'
            STEP 04 Expected : Tool tip displays: Reset Layout. Reset ribbon, style and panels to installed settings
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.HelpMenu.ResetLayout, RESET_LAYOUT_TOOLTIP, '04.01',  image_size=80)
        
        """
            STEP 05 : Hover on 'About'
            STEP 05 Expected : Tool tip displays: About Display program information, version number and copyright
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.HelpMenu.About, ABOUT_TOOLTIP, '05.01', image_size=80)
        
if __name__=='__main__' :
    unittest.main()