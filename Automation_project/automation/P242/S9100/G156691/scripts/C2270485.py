'''-------------------------------------------------------------------------------------------
Reworked on January 17, 2019
@author: Prasanth

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270485
Test Case Title =  Utilities Tab
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270485_TestClass(BaseTestCase):

    def test_C2270485(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
       
        """
            STEP 01 : Click on Utilities tab and check Thumbnails from the View group 
                      Hover on "Add"
            STEP 01 Expected : Tool tip displays: Add Add to current chain
        """
        EXPECTED_ADD_TOOLTIP = "Add Add to current chain"
        Ribbon.select_tab(Ribbon.Locators.UtilitiesTab.UTILITIES)
        Ribbon.select_tab_item(Ribbon.Locators.UtilitiesTab.View.Thumbnails)
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Chaining.Add, EXPECTED_ADD_TOOLTIP, '01.01')
        
        """
            STEP 02 : Hover on "Remove"
            STEP 02 : Tool tip displays: Remove Remove from current chain
        """
        EXPECTED_REMOVE_TOOLTIP = 'Remove Remove from current chain'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Chaining.Remove, EXPECTED_REMOVE_TOOLTIP, '02.01')
        
        """
            STEP 03 : Hover on "Sync"
            STEP 03 : Tool tip displays: Sync Synchronize to Active Reports
        """
        EXPECTED_SYNC_TOOLTIP = "Sync Synchronize to Active Report"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.ActiveReports.Sync, EXPECTED_SYNC_TOOLTIP, '03.01', image_size=80)
        
        """
            STEP 04 :Hover on "Show"
            STEP 04 : Tool tip displays: Show Show synchronized reports
        """
        EXPECTED_SHOW_TOOLTIP = "Show Show synchronized reports"
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.ActiveReports.Show, EXPECTED_SHOW_TOOLTIP, '04.01', image_size=65)
        
        """
            STEP 05 : Hover on "Unlock"
            STEP 05 : Tool tip displays: Unlock Unlock Template
        """
        EXPECTED_UNLOCK_TOOLTIP = 'Unlock Unlock Template'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Template.Unlock, EXPECTED_UNLOCK_TOOLTIP, '05.01')
        
        """
            STEP 06 : Hover on "Report Set"
            STEP 06 : Tool tip displays: Report Set Insert Report Set
        """
        EXPECTED_REPORT_SET_TOOLTIP = 'Report Set Insert Report Set'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Template.ReportSet, EXPECTED_REPORT_SET_TOOLTIP, '06.01', crop_x1=40)
        
        """
            STEP 07 : Hover on "Visibility"
            STEP 07 : Tool tip displays: Visibility Toggle visibility
        """
        EXPECTED_VISIBILITY_TOOLTIP = 'Visibility Toggle visibility'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Miscellaneous.Visibility, EXPECTED_VISIBILITY_TOOLTIP, '07.01', image_size=90)
        
        """
            STEP 08 : Hover on Tab Order
            STEP 08 : Tool tip displays: Tab Oder Edit the tab order of the controls on the form
        """
        EXPECTED_TAB_ORDER_TOOLTIP = 'Tab Order (Ctrl+D)  Edit the tab order of the controls on the form'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Miscellaneous.TabOrder, EXPECTED_TAB_ORDER_TOOLTIP, '08.01', crop_x1=40, image_size=80)
        
        """
            STEP 09 :  Hover on "Delete Container"
            STEP 09 : Tool tip displays: Delete Container Delete Container Only
        """
        EXPECTED_DELETE_TOOLTIP = 'Delete Container (Ctrl+Delete) Delete Container Only'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Miscellaneous.DeleteContainer, EXPECTED_DELETE_TOOLTIP, '09.01', image_size=80)
        
        """
            STEP 10 : Hover on "Refresh All"
            STEP 10 : Tool tip displays: Refresh All Refresh All
        """
        EXPECTED_REFRESH_TOOLTIP = 'Refresh All Refresh All'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Miscellaneous.RefreshAl, EXPECTED_REFRESH_TOOLTIP, '10.01', image_size=80)
        
        """
            STEP 11 : Hover on "Internet Explorer"
            STEP 11 : Tool tip displays: Internet Explorer Internet Explorer
        """
        EXPECTED_IE_TOOLTIP = 'Internet Explorer Internet Explorer'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Preview.InternetExplorer, EXPECTED_IE_TOOLTIP, '11.01', image_size=70)
        
        """
            STEP 12 : Hover on "Chrome"
            STEP 12 : Tool tip displays: Chrome Chrome
        """
        EXPECTED_CHROME_TOOLTIP = 'Chrome Chrome'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Preview.Chrome, EXPECTED_CHROME_TOOLTIP, '12.01', image_size=80)
        
        """
            STEP 13 : Hover on "Firefox"
            STEP 13 :Tool tip displays: Firefox Firefox
        """
        EXPECTED_FIREFOX_TOOLTIP = 'Firefox Firefox'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Preview.Firefox, EXPECTED_FIREFOX_TOOLTIP, '13.01')
        
        """
            STEP 14 : Hover on "Edge"
            STEP 14 : Tool tip displays: Edge Edge
        """
        EXPECTED_EDGE_TOOLTIP = 'Edge Edge'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Preview.Edge, EXPECTED_EDGE_TOOLTIP, '14.01', image_size=80)
        
        """
            STEP 15 : Hover on "Preview Runtime"
            STEP 15 : Tool tip displays: Preview Runtime Preview Runtime
        """
        EXPECTED_PREVIEW_TOOLTIP = 'Preview Runtime Preview Runtime'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.Preview.PreviewRuntime, EXPECTED_PREVIEW_TOOLTIP, '15.01', image_size=90)
        
        """
            STEP 16 : Hover on "Properties"
            STEP 16 : Tool tip displays: Properties Show or hide the Properties panel
        """
        EXPECTED_PROPERTIES_TOOLTIP = 'Properties Show or hide the Properties panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.View.Properties, EXPECTED_PROPERTIES_TOOLTIP, '16.01')
        
        """
            STEP 17 : Hover on "Settings"
            STEP 17 : Tool tip displays: Settings Show or hide the Settings panel
        """
        EXPECTED_SETTINGS_TOOLTIP = 'Settinas Show or hide the Settings panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.View.Settings, EXPECTED_SETTINGS_TOOLTIP, '17.01')
        
        """
            STEP 18 : Hover on "Thumbnails"
            STEP 18 : Tool tip displays: Thumbnails Show or hide the Thumbnails panel
        """
        EXPECTED_THUMBNAILS_TOOLTIP = 'Thumbnails Show or hide the Thumbnails panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.View.Thumbnails, EXPECTED_THUMBNAILS_TOOLTIP, '18.01', image_size=60)
        
        """
            STEP 19 : Hover on "Tasks & Animations"
            STEP 19 : Tool tip displays: Tasks & Animations Show or hide the Tasks & Animations panel
        """
        EXPECTED_TASK_ANIMATION_TOOLTIP = 'Tasks & Animations  Show or hide the Tasks & Animations panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.View.TasksAnimations, EXPECTED_TASK_ANIMATION_TOOLTIP, '19.01', image_size=72)
        
        """
            STEP 20 : Hover on "Requests & Data Sources"
            STEP 20 : Tool tip displays: Requests & Data Sources Show or hide the Requests & Data Sources panel
        """
        EXPECTED_REQ_DATA_TOOLTIP = 'Requests & Data Sources  Show or hide the Requests & Data Sources panel'
        Ribbon.verify_tab_item_tooltip_text(Ribbon.Locators.UtilitiesTab.View.RequestsDataSources, EXPECTED_REQ_DATA_TOOLTIP, '20.01')
        
if __name__=='__main__' :
    unittest.main()