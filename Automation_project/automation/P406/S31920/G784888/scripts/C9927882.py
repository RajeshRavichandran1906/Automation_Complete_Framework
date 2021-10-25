"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 21 February 2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927882_TestClass(BaseTestCase):
    
    def test_C9927882(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
       
        def verify_window_title(expected_window_title, step):
            HomePage.Home._core_utils.switch_to_new_window()
            current_window_title = self.driver.title
            HomePage.Home._utils.asequal(current_window_title, expected_window_title, step)
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS as Administrator.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on the 'Settings' icon in the Banner link.
        """
        HomePage.Banner.click_settings()
        HomePage.Home._utils.capture_screenshot('02.00',STEP_02)
        
        STEP_02_01 = """
            STEP 02.01 : Verify the following options are displayed:
            1.Security Center
            2.Administration Console
            3.WebFOCUS Server
            4.Magnify Console
            5.Manage Private Resources
            6.Normal View (By default check off)
            7.Administration View
        """
        expected_menus = ['Security Center', 'Administration Console', 'WebFOCUS Server', 'Magnify Console', 'Manage Private Resources', 'Normal view', 'Administration view']
        HomePage.ContextMenu.verify(expected_menus, '02.01')
        HomePage.ContextMenu.verify_selected_options(['Normal view'], '02.02')
        HomePage.Home._utils.capture_screenshot('02.01',STEP_02_01, True)
                
        STEP_03 = """
            STEP 03 : Click on the 'Settings' icon >Click on 'Security Center'
        """
        HomePage.ContextMenu.select('Security Center')
        HomePage.Home._utils.capture_screenshot('03.00',STEP_03)
        
        STEP_03_01 = """
            STEP 03.01 : Verification - Verify it opens 'Security Center' in a new window
        """
        expected_window_title = 'Security Center'
        verify_window_title(expected_window_title, 'Step 03.01 : Verify "security center" new window opens')
        HomePage.Home._utils.capture_screenshot('03.01',STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Close the 'Security Center' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """
            STEP 05 : Click on the 'Settings' icon >Click on 'Administration Console'
        """
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select('Administration Console')
        HomePage.Home._utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verification - Verify it brings up the 'Administration Console' in a new tab
        """
        expected_window_title = 'Administration Console'
        verify_window_title(expected_window_title, 'Step 05.01 : Verify "Administration Console" new window opens')
        HomePage.Home._utils.capture_screenshot('05.01',STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Close the 'Administration Console' tab
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('06.00',STEP_06)
        
        STEP_07 = """
            STEP 07 : Click on the 'Settings' icon >Click on 'WebFOCUS Server'
        """
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select('WebFOCUS Server')
        HomePage.Home._utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verification - Verify it brings up the 'WebFOCUS Server Console' in a new tab
        """
        app_css = "#WcMultiframesContentView-1"
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text(app_css, 'Applications', 60)
        actual_text = self.driver.find_element_by_css_selector(app_css).text.strip()
        HomePage.Home._utils.asequal(actual_text, 'Applications', 'Step 07.01 : Verify "WebFOCUS Server Console" new window opens')
        HomePage.Home._utils.capture_screenshot('07.01',STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Close the 'WebFOCUS Server' tab
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('08.00',STEP_08)
        
        STEP_09 = """
            STEP 09 : Click on the 'Settings' icon >Click on 'Magnify Console'
        """
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select('Magnify Console')
        HomePage.Home._utils.capture_screenshot('09.00',STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verification - Verify it brings up the 'Magnify Console' in a new tab
        """
        expected_window_title = 'Magnify Console'
        verify_window_title(expected_window_title, 'Step 09.01 : Verify "Magnify Console" new window opens')
        HomePage.Home._utils.capture_screenshot('09.01',STEP_09_01, True)
        
        STEP_10 = """
            STEP 10 : Close the 'Magnify Console' tab
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('10.00',STEP_10)
        
        STEP_11 = """
            STEP 11 : Click on the 'Settings' icon >Click on 'Manage Private Resources'
        """
        HomePage.Banner.click_settings()
        HomePage.ContextMenu.select('Manage Private Resources')
        HomePage.Home._utils.capture_screenshot('11.00',STEP_11)
        
        STEP_11_01 = """
            STEP 11.01 : Verification - Verify it brings up the 'Manage Private Resources' in a new tab with the GROUPS and USERS nodes
        """
        expected_window_title = 'Manage Private Resources'
        verify_window_title(expected_window_title, 'Step 11.01 : Verify "Manage Private Resources" new window opens')
        node_elements = HomePage.Home._utils.validate_and_get_webdriver_objects('#mpUserGroupTree table>tbody>tr', 'node of Manage Private Resources')
        node_elements.remove(node_elements[-1])
        actual_node_values = [x.text for x in node_elements]
        expected_node_value = ['Groups', 'USERS']
        HomePage.Home._utils.asequal(actual_node_values, expected_node_value, 'Step 11.02 : Verify GROUPS and USERS nodes')
        HomePage.Home._utils.capture_screenshot('11.01',STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Close the 'Manage Private Resources' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('12.00',STEP_12)
        
        STEP_13 = """
            STEP 13 : In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('13.00',STEP_13)