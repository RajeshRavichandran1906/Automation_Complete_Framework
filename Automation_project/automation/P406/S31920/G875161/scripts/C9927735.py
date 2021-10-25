"""-------------------------------------------------------------------------------------------
Author Name  : PM14587
Automated On : 15-September-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927735_TestClass(BaseTestCase):
    
    def test_C9927735(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin user.
        """
        HomePage.invoke_with_login('mridadm','mrpassadm')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on the 'Utilities' icon in the banner link.
        """
        HomePage.Banner.click_utilities()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_02_EXPECTED = """
            STEP 02 - Expected : Verify the following options are displayed:
            1. Deferred Status
            2. Stop Requests
            3. Session Viewer
            4. ReportCaster Explorer
            5. ReportCaster Status
            6. Change Management >
              1.Import
              2.Export
            7. Magnify Search Page
            8. WebFOCUS Infographics
        """
        utilities_options = ['Deferred Status', 'Stop Requests', 'Session Viewer', 'ReportCaster Explorer', 'ReportCaster Status', 'Change Management', 'Magnify Search Page', 'WebFOCUS Infographics']
        HomePage.ContextMenu.verify(utilities_options, "02.01")
        HomePage.ContextMenu.verify(['Import', 'Export'], "02.02", menu_path="Change Management")
        HomePage.Home._utils.capture_screenshot("02 - Expected", STEP_02_EXPECTED, True)

        STEP_03 = """
            STEP 03 : Click on Workspaces tab > Expand 'P406_S31920' > Click on the 'G875161' folder from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select("P406_S31920->G875161")
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Stop_Request", 30)
        HomePage.Home._utils.capture_screenshot("03", STEP_03)

        STEP_04 = """
            STEP 04 : Right-click on 'Stop_Request' fex > Select 'Run' > Close the run window
        """
        HomePage.Workspaces.ContentArea.right_click_on_file("Stop_Request")
        HomePage.ContextMenu.select("Run")
        HomePage.RunWindow.close()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot("04", STEP_04)

        STEP_05 = """
            STEP 05 : Click on the 'Utilities' icon > Click on 'Stop Request'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select("Stop Requests")
        HomePage.ModalDailogs.Alert.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify that 'Stop Requests' popup stating '1 request(s) stopped'
        """
        HomePage.ModalDailogs.Alert.verify_title("Stop Requests", "05.01")
        HomePage.ModalDailogs.Alert.verify_message("1 request(s) stopped.", "05.02")
        HomePage.Home._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)

        STEP_06 = """
            STEP 06 : Click the 'OK' button to close the 'Stop Request' popup
        """
        HomePage.ModalDailogs.Alert.close()
        HomePage.Home._utils.capture_screenshot("06", STEP_06)

        STEP_07 = """
            STEP 07 : Click on the 'Utilities' icon > Click on 'Deferred Status'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('Deferred Status')
        HomePage.Home._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify the following 'Deferred Report Status' window gets displayed.
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_tab_name("Deferred Report Status","Step 07.01 : Verify the 'Deferred Report Status' window gets displayed.")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Close the 'Deferred Report Status' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)

        STEP_09 = """
            STEP 09 : Click on the 'Utilities' icon > Click on 'Session Viewer'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('Session Viewer')
        HomePage.Home._utils.capture_screenshot("09", STEP_09)

        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify the following 'Session Viewer' window gets displayed with the URL http://machine_name:port/alias/util/wfsessionviewer.jsp
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_url('util/wfsessionviewer.jsp',"Step 09.01 : Verify the session viewer URL")
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Close the 'Session Viewer' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_11 = """
            STEP 11 : Click on the 'Utilities' icon > Click on 'Report Caster Explorer'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('ReportCaster Explorer')
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify the following 'Report Caster Explorer' window gets displayed with the URL http://machine_name:port/alias/rcex.rc
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_url('rcex.rc',"Step 11.01 : Verify the session viewer URL")
        HomePage.Home._utils.verify_current_tab_name("TIBCO WebFOCUS Schedule Explorer",'Step 11.02 : Verify the window displayed with Report Caster Explorer')
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the 'Report Caster Explorer' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : Click on the 'Utilities' icon > Click on 'Report Caster Status'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('ReportCaster Status')
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify the following 'Report Caster Status' window gets displayed with the URL http://machine_name:port/alias/rcc.rc
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_url('rcc.rc',"Step 13.01 : Verify Report Caster Status URL")
        HomePage.Home._utils.verify_current_tab_name("TIBCO WebFOCUS Schedule Status",'Step 13.02 : Verify the window displayed with ReportCaster Status')
        HomePage.Home._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Close the 'Report Caster Status' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("14", STEP_14)

        STEP_15 = """
            STEP 15 : Click on the 'Utilities' icon > Hover over mouse to 'Change Management' > Click on 'Import'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select("Change Management->Import")
        HomePage.ModalDailogs.Import.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("15", STEP_15)

        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify Import dialog gets displayed
        """
        HomePage.ModalDailogs.Import.verify_title("Import", "15.01")
        HomePage.Home._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Close import dialog
        """
        HomePage.ModalDailogs.Import.close()
        HomePage.Home._utils.capture_screenshot("16", STEP_16)

        STEP_17 = """
            STEP 17 : Click on the 'Utilities' icon > Hover over mouse to 'Change Management' > Click on 'Export'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select("Change Management->Export")
        HomePage.ModalDailogs.Import.wait_for_appear()
        HomePage.Home._utils.capture_screenshot("17", STEP_17)

        STEP_17_EXPECTED = """
            STEP 17 - Expected : Verify Export dialog gets displayed
        """
        HomePage.ModalDailogs.Import.verify_title("Export", "17.01")
        HomePage.Home._utils.capture_screenshot("17 - Expected", STEP_17_EXPECTED, True)

        STEP_18 = """
            STEP 18 : Close import dialog
        """
        HomePage.ModalDailogs.Import.close()
        HomePage.Home._utils.capture_screenshot("18", STEP_18)

        STEP_19 = """
            STEP 19 : Click on the 'Utilities' icon > Click on 'Magnify Search Page'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('Magnify Search Page')
        HomePage.Home._utils.capture_screenshot("19", STEP_19)

        STEP_19_EXPECTED = """
            STEP 19 - Expected : Verify the following 'Magnify Search Page' window gets displayed with the URL http://machine_name:port/alias/search
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_url('search',"Step 19.01 : Verify magnify Search Page URL")
        HomePage.Home._utils.capture_screenshot("19 - Expected", STEP_19_EXPECTED, True)

        STEP_20 = """
            STEP 20 : Close the 'Magnify Search Page' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("20", STEP_20)

        STEP_21 = """
            STEP 21 : Click on the 'Utilities' icon > Click on 'WebFOCUS Infographics'
        """
        HomePage.Banner.click_utilities()
        HomePage.ContextMenu.select('WebFOCUS Infographics')
        HomePage.Home._utils.capture_screenshot("21", STEP_21)

        STEP_21_EXPECTED = """
            STEP 21 - Expected : Verify the 'easel.ly | create and share visual ideas using infographics' 'webfocus.easel.ly' window gets displayed with the URL https://webfocus.easel.ly/
        """
        HomePage.Home._core_utils.switch_to_new_window()
        current_url = self.driver.current_url
        HomePage.Home._utils.verify_current_tab_name('easel.ly | create and share visual ideas using infographics',"Step 21.01 : Verify webfocus infographics Page URL")
        HomePage.Home._utils.asequal(current_url,'https://webfocus.easel.ly/','Step 21.02 : Verify the infographics URl')
        HomePage.Home._utils.capture_screenshot("21 - Expected", STEP_21_EXPECTED, True)

        STEP_22 = """
            STEP 22 : Close the 'webfocus.easel.ly' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("22", STEP_22)

        STEP_23 = """
            STEP 23 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("23", STEP_23)