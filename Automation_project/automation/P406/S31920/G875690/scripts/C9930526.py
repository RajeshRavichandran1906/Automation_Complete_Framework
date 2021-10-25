"""-------------------------------------------------------------------------------------------
Author Name : Prabhakaran
Automated On : 05 August 2020
-----------------------------------------------------------------------------------------------"""

from common.wftools.chart import Chart
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9930526_TestClass(BaseTestCase):
    
    def test_C9930526(self):
        
        """
        TESTCASE OBJECTS
        """
        chart = Chart(self.driver)
        HomePage = ParisHomePage(self.driver)
        
        STEP_01 = """
            STEP 01 : Sign in to WebFOCUS as Author user
        """
        HomePage.invoke_with_login('mridauth','mrpassauth')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on "Workspaces" view
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Click on "Getting Started" folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select('Getting Started')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Explore", 30)
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04 = """
            STEP 04 : Right-click "Explore Sales Data" from the content area > Select "Run"> "Run Deferred" option
        """
        ok_btn_css = "#okButton"
        HomePage.Workspaces.ContentArea.right_click_on_file('Explore Sales Data')
        HomePage.ContextMenu.select('Run...->Run deferred')
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_until_element_is_visible(ok_btn_css, 60)
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify 'Deferred Report Description' dialogue as same below:
        """
        HomePage.Home._utils.verify_element_text("div#deferMsg>div", "Deferred Report Description", "Step 04.01 : Verify 'Deferred Report Description' label")
        description = self.driver.find_element_by_id("new_description").get_attribute('value')
        HomePage.Home._utils.asequal(description, "Explore Sales Data", "Step 04.02 : Verify Deferred Report Description")
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Click "OK"
        """
        deferred_link_css = "#deferMsg a[href]"
        ok_btn = self.driver.find_element_by_css_selector(ok_btn_css)
        HomePage.Home._core_utils.left_click(ok_btn)
        HomePage.Home._utils.synchronize_with_visble_text(deferred_link_css, "Deferred", 60)
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify Deferred Report Notification displays with successfully submitted for deferred processing
        """
        HomePage.Home._utils.verify_element_text(deferred_link_css, "Deferred Report Status", "Step 05.01 : Verify Deferred Report Notification displays with successfully submitted for deferred processing")
        HomePage.Home._utils.capture_screenshot('05.01', STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Click on the "Deferred Report Status link"
        """
        view_btn_css = "a[href]>img[title='View']"
        status_link = self.driver.find_element_by_css_selector(deferred_link_css)
        HomePage.Home._core_utils.left_click(status_link)
        HomePage.Home._utils.synchronize_until_element_is_visible(view_btn_css, 60)
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verify 'Deferred Report Status' opens and 'Explore Sales Data' report has been successfully submitted
        """
        HomePage.Home._utils.verify_element_text("span[title='Getting Started/']", "Explore Sales Data", "Step 06.01 : Verify 'Deferred Report Status' opens and 'Explore Sales Data' report has been successfully submitted")
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Click the "View" button > Maximize the new window
        """
        view_btn = self.driver.find_element_by_css_selector(view_btn_css)
        HomePage.Home._core_utils.left_click(view_btn)
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_visble_text("#jschart_HOLD_0", "Revenue", 120)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify 'Explore Sales Data' run in a new window without any error
        """
        chart.verify_x_axis_title_in_run_window(['Sale Date Month'], msg='Step 07.01')
        chart.verify_y_axis_title_in_run_window(['Revenue'], msg='Step 07.02')
        chart.verify_legends_in_run_window(['Product Category', 'Accessories', 'Camcorder', 'Computers', 'Media Player', 'Stereo Systems', 'Televisions', 'Video Production'], msg='Step 07.03')
        HomePage.Home._utils.capture_screenshot('07.01', STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Close 'Chart1' run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_09 = """
            STEP 09 : Close 'Deferred Report Status' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._core_utils.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_10 = """
            STEP 10 : Sign out WF.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        