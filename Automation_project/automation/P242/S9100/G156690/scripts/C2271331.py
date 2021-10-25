'''-------------------------------------------------------------------------------------------
Reworked on January 09, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2271331
Test Case Title =  Pages Group
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2271331_TestClass(BaseTestCase):

    def test_C2271331(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            STEP 01 : Hover on "Add"
            STEP 01 Expected : Tool tip displays: Add Add to current chain
        """
        Ribbon.select_tab(Ribbon.Locators.UtilitiesTab.UTILITIES)
        ADD_TOOLTIP = 'Add Add to current chain'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Chaining.Add, ADD_TOOLTIP, '01.01' )

        """
            STEP 02 : Hover on "Remove"
            STEP 02 Expected : Tool tip displays: Remove Remove from current chain
        """
        REMOVE_TOOLTIP = 'Remove Remove from current chain'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Chaining.Remove, REMOVE_TOOLTIP, '02.01')
        
        """
            STEP 03 : Hover on "Show Chain order"
            STEP 03 Expected : Tool tip displays: Show Chain Order Show order in the chain
        """
        SHOW_CHAIN_ORDER_TOOLTIP = 'Show Chain order Show order in the chain'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Chaining.ShowChainOrder, SHOW_CHAIN_ORDER_TOOLTIP, '03.01', crop_x1=38, image_size=55)
        
        """
            STEP 04 : Hover on "Save Document As"
            STEP 04 Expected : Tool tip displays: Save Document As Save Document As
        """
        SAVE_DOCUMENT_AS_TOOLTIP = 'Save Document As Save Document As'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.FileUtility.SaveDocumetAs, SAVE_DOCUMENT_AS_TOOLTIP, '04.01')
        
        """
            STEP 05 : Hover on "Save Page As"
            STEP 05 Expected : Tool tip displays: Save Page As Save Page As
        """
        SAVE_PAGE_AS_TOOLTIP = 'Save Page As Save Page As'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.FileUtility.SavePageAs, SAVE_PAGE_AS_TOOLTIP, '05.01')
        
        """
            STEP 06 : Hover on "Pre-process code"
            STEP 06 Expected : Tool tip displays: Pre-process code Pre-process code
        """
        PRE_PROCESS_CODE = 'Pre-process code Pre-process code'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.FileUtility.PreprocessCode, PRE_PROCESS_CODE, '06.01')
        
        """
            STEP 07 : Hover on "Post-process code"
            STEP 07 Expected : Tool tip displays: Post-process code Post-process code
        """
        POST_PROCESS_CODE = 'Post-process code Post-process code'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.FileUtility.PostprocessCode, POST_PROCESS_CODE, '07.01')
        
        """
            STEP 08 : Hover on "Refresh All"
            STEP 08 Expected : Tool tip displays: Refresh All Refresh All
        """
        REFRESH_ALL = 'Refresh All (Ctrl+F5) Refresh All'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.FileUtility.RefreshAll, REFRESH_ALL, '08.01', crop_x1=40)
        
        """
            STEP 09 : Hover on "Properties"
            STEP 09 Expected : Tool tip displays: Properties Show or hide the Properties panel
        """
        PROPERTIES = 'Properties Show or hide the Properties panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.View.Properties, PROPERTIES, '09.01')
        
        """
            STEP 10 : Hover on 'Settings'
            STEP 10 Expected : Tool tip displays: Settings Show or hide the Settings panel
        """
        SETTINGS = 'Settings Show or hide the Settings panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.View.Settings, SETTINGS, '10.01', image_size=51)
        
        """
            STEP 11 : Hover on "Thumbnails"
            STEP 11 Expected : Tool tip displays: Thumbnails Show or hide the Thumbnails panel
        """
        THUMBNAILS = 'Thumbnails Show or hide the Thumbnails panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.View.Thumbnails, THUMBNAILS, '11.01', image_size=51)
        
if __name__=='__main__' :
    unittest.main()