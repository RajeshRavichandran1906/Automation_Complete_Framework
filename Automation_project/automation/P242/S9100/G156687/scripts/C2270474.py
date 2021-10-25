'''-------------------------------------------------------------------------------------------
Reworked on January 14, 2019
@author: Pradheep

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/2270474
Test Case Title =  Pages Group
-----------------------------------------------------------------------------------------------'''
from appstudio import settings
from appstudio.lib.basetestcase import BaseTestCase
from appstudio.tools.common.ribbon import Ribbon
import unittest

class C2270474_TestClass(BaseTestCase):
    
    def test_C2270474(self):
        
        settings.AppStudio.CLOSE_CANVAS = False
        
        """
            COMMON TEST CASE VARIABLES 
        """
        MENU_LOCATOR = Ribbon.Locators.WebFOCUSAdministrationMenu.WebFOCUSAdministration
        WEBFOCUS_ADMISNISTRATION_CONSOLE_TOOLTIP = 'WebFOCUS Administration Console  Administration of the WebFOCUS environment'
        REPORTING_SERVER_CONSOLE_TOOLTIP = 'Reporting Server Console  Administration of the WebFOCUS Reporting Server'
        SECURITY_CENTER_TOOLTIP = 'WebFOCUS Security Center  Administration of WebFOCUS security settings'
        BI_PORTAL_TOOLTIP = 'WebFOCUS BI Portal Launch the WebFOCUS BI Portal'
        DEFERRED_STATUS_TOOLTIP = 'WebFOCUS Deferred Status  Administration of WebFOCUS Deferred Status'
        REPORT_CASTER_CONSOLE_TOOLTIP = 'WebFOCUS ReportCaster Console  Launch the WebFOCUS ReportCaster Console'
        SESSION_VIEWER_TOOLTIP = 'WebFOCUS Session Viewer Launch the WebFOCUS Session Viewer'
        
        """
            STEP 01 : Hover on "WebFOCUS Administration Console"
            STEP 01 Expected : Tool tip displays: WebFOCUS Administration Console Administration of the WebFOCUS environment
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.WebFOCUSAdministrationMenu.WebFOCUSAdministrationConsole, WEBFOCUS_ADMISNISTRATION_CONSOLE_TOOLTIP, '01.01', image_size=80)
    
        """
            STEP 02 : Hover on "Reporting Server Console"
            STEP 02 Expected : Tool tip displays: Reporting Server Console Administration of the WebFOCUS Reporting Server
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.WebFOCUSAdministrationMenu.ReportingServerConsole, REPORTING_SERVER_CONSOLE_TOOLTIP, '02.01', image_size=80)
        
        """
            STEP 03 : Hover on "Security Center"
            STEP 03 Expected : Tool tip displays: WebFOCUS Security Center Administration of WebFOCUS security settings
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.WebFOCUSAdministrationMenu.SecurityCenter, SECURITY_CENTER_TOOLTIP, '03.01', image_size=80)
        
        """
            STEP 04 : Hover on "BI Portal"
            STEP 04 Expected : Tool tip displays: WebFOCUS BI Portal Launch the WebFOCUS BI Portal
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.WebFOCUSAdministrationMenu.BIPortal, BI_PORTAL_TOOLTIP, '04.01',  image_size=80)
        
        """
            STEP 05 : Hover on "Deferred Status"
            STEP 05 Expected : Tool tip displays: WebFOCUS Deferred Status Administration of WebFOCUS Deferred Status
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.WebFOCUSAdministrationMenu.DeferredStatus, DEFERRED_STATUS_TOOLTIP, '05.01', image_size=80)
        
        """
            STEP 06 : Hover on "ReportCaster Console"
            STEP 06 Expected : Tool tip displays: WebFOCUS ReportCaster Console Launch the WebFOCUS ReportCaster Console
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.WebFOCUSAdministrationMenu.ReportCasterConsole, REPORT_CASTER_CONSOLE_TOOLTIP, '06.01', image_size=80)
        
        """
            STEP 07 : Hover on "Session Viewer"
            STEP 07 Expected : Tool tip displays: Tool tip displays: WebFOCUS Session Viewer Launch the WebFOCUS Session Viewer
        """
        Ribbon.verify_menu_option_tooltip_text(MENU_LOCATOR, Ribbon.Locators.WebFOCUSAdministrationMenu.SessionViewer, SESSION_VIEWER_TOOLTIP, '07.01', image_size=80)
        
if __name__=='__main__' :
    unittest.main()