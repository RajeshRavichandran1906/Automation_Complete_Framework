"""-------------------------------------------------------------------------------------------
Author Name  : JR11467
Automated On : 10-November-2020
-------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
import keyboard
from selenium.webdriver.common.by import By
from common.lib.javascript import JavaScript
from common.wftools.chart import Chart

class C9930641_TestClass(BaseTestCase):
    
    def test_C9930641(self):
        
        """
        TEST CASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        jsobj = JavaScript(self.driver)
        chart_obj = Chart(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        DF_DEFAULT_MESSAGE_BOX = ".base-canvas .messageLabel .ibx-label-text"
        DF_SAVEBTN_CSS = ".ds-header .btn-save"
        DF_SAVE_DIALOG_SAVE_CSS = ".open-dialog-resources .ibx-dialog-ok-button"
        DF_CRUMB_RETAIL_SAMPLES = ".open-dialog-resources div.crumb-button[title='Retail Samples']"

        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS as Administrator
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        HomePage.Home._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.double_click("Workspaces")
        HomePage.Workspaces.NavigationBar.select_workspaces()
        HomePage.Home._utils.capture_screenshot("02", STEP_02)

        STEP_03 = """
            STEP 03 : Click on 'My Workspaces' from the resource tree > Click on 'Visualize Data'
        """
        
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Workspaces.ContentArea.delete_file_if_exists("Visualization 1")
        HomePage.Workspaces.ResourcesTree.select("My Workspace")
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_visualize_data()
        HomePage.Home._utils.capture_screenshot("03", STEP_03)
 
        STEP_04 = """
            STEP 04 : Click on the 'My Workspace' drop-down > Select 'Retail Samples' workspace
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.wait_for_page_loads(30, pause_time=2)
        HomePage.Home._utils.synchronize_with_visble_text("div[class*='select-data-source ibx-widget']", 'Type', 100)

#         HomePage.Home._utils.synchronize_with_number_of_element(".select-data-source [title='Show Menu']", 1, 10)
        show_menu_btn = HomePage.Home._utils.validate_and_get_webdriver_object(".select-data-source [title='Show Menu']", 'SHOW_MENU_BTN')
        show_menu_btn.click()
        HomePage.Home._utils.wait_for_page_loads(30)
        context_menu_text_elem = self.driver.find_element_by_xpath("//*[contains(@class,'pop-top')]//*[text()= 'Retail Samples']")
        jsobj.scrollIntoView(context_menu_text_elem)
        HomePage.Home._utils.wait_for_page_loads(10)
        HomePage.ContextMenu.select('Retail Samples')
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("04", STEP_04)
 
        STEP_05 = """
            STEP 05 : Double click on 'retail_samples' application folder > Choose 'wf_retail_lite > Click Select
        """
#         elem=self.driver.find_element_by_css_selector("div[class='dgrid-cell'][title='retail_samples']")
#         jsobj.scrollIntoView(elem)
        HomePage.Home._utils.synchronize_until_element_is_visible("div[class='dgrid-cell'][title]", 30)
        element_obj = self.driver.find_elements_by_css_selector("div[class='dgrid-cell'][title]")
        elem = HomePage.Home._core_utils.get_element_object_by_text(element_obj, 'retail_samples')
        HomePage.Home._core_utils.double_click(elem)
        HomePage.Home._utils.wait_for_page_loads(30)
         
#         rs_elem=self.driver.find_element_by_css_selector("div[class='dgrid-cell'][title='wf_retail_lite']")
#         jsobj.scrollIntoView(rs_elem)
        HomePage.Home._utils.synchronize_until_element_is_visible("div[class='dgrid-cell'][title]", 30)
        element_obj = self.driver.find_elements_by_css_selector("div[class='dgrid-cell'][title]")
        rs_elem = HomePage.Home._core_utils.get_element_object_by_text(element_obj, 'wf_retail_lite')
        rs_elem.click()
 
        ok_btn_elem=self.driver.find_element_by_css_selector(".select-data-source .ibx-dialog-ok-button")
        ok_btn_elem.click()
        HomePage.Home._utils.capture_screenshot("05", STEP_05)
 
        STEP_06 = """
            STEP 06 : Double click on the 'Discount' field
        """
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Home._utils.synchronize_with_visble_text(DF_DEFAULT_MESSAGE_BOX, "Drop measures & dimensions here",30)
        search_box_elem = HomePage.Home._utils.validate_and_get_webdriver_object(".resource-box .wfc-mdfp-search", "SEARCH_BOX")
        search_box_elem.click()
        keyboard.write("Discount", delay=1)
        discount_elem = self.driver.find_element(By.XPATH, '//*[(text()="Discount")]')
        HomePage.Home._core_utils.python_doubble_click(discount_elem)
        HomePage.Home._utils.wait_for_page_loads(40)
        HomePage.Home._utils.capture_screenshot("06", STEP_06)
 
        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify the following output
        """
        HomePage.Home._utils.synchronize_with_number_of_element("[class='riser!s0!g0!mbar!']", 1, 30)
        y_axis_label = ['0', '10M', '20M', '30M', '40M', '50M', '60M']
        HomePage.Home._utils.wait_for_page_loads(20,pause_time=5)
        chart_obj.verify_y_axis_title_in_run_window(['Discount'], parent_css='.chartPanel ', msg="Step 06.01 : Verify Chart title")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label, parent_css='', msg="Step 06.01 : Verify Chart labels")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='.chartPanel ', msg="Step 06.01 : Verify Chart color")
         
        HomePage.Home._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)
 
        STEP_07 = """
            STEP 07 : Click 'Save' from the toolbar
        """
        logo_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVEBTN_CSS, "DF_SAVEBTN_CSS")
        logo_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.capture_screenshot("07", STEP_07)
 
        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Save dialog opens and it navigates to 'Workspaces > Retail Samples' path
        """
        HomePage.Home._utils.synchronize_with_number_of_element(DF_SAVE_DIALOG_SAVE_CSS, 1, 30)
        HomePage.Home._utils.verify_element_visiblty(element_css=DF_CRUMB_RETAIL_SAMPLES, msg="Step 07.01 : Verify Save dialog opens and navigates to Workspaces -> Retail Samples path")
        HomePage.Home._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)
 
        STEP_08 = """
            STEP 08 : Click Save > Close the 'Designer Framework' tool
        """
        btn_elem = HomePage.Home._utils.validate_and_get_webdriver_objects(DF_SAVE_DIALOG_SAVE_CSS, "DF_SAVE_DIALOG_SAVE_CSS")
        btn_elem[0].click()
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("08", STEP_08)
 
        STEP_09 = """
            STEP 09 : Expand 'My Workspaces' under resource tree > Click on 'My Content' folder
        """
        HomePage.Workspaces.ResourcesTree.expand('My Workspace')
        HomePage.Workspaces.ResourcesTree.select('My Content')
 
        HomePage.Home._utils.capture_screenshot("09", STEP_09)
 
        STEP_09_EXPECTED = """
            STEP 09 - Expected : Verify that 'Visualization 1' is not available under 'My Content' folder
        """
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Workspaces.ContentArea.verify_files(['Visualization 1'], "09.01", 'asnotin')
        HomePage.Home._utils.capture_screenshot("09 - Expected", STEP_09_EXPECTED, True)

        STEP_10 = """
            STEP 10 : Click on 'Retail Samples' workspace
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples')
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify that 'Visualization 1' is available
        """
        HomePage.Workspaces.ContentArea.verify_files(['Visualization 1'], "10.01", 'asin')
        HomePage.Home._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Double click on 'Visualization 1'
        """
        HomePage.Workspaces.ContentArea.double_click_on_file('Visualization 1')
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Home._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify 'Visualization 1' runs successfully without any error
        """
        HomePage.RunWindow.wait_for_visible(30)
        HomePage.RunWindow.switch_to_frame()
        y_axis_label = ['0', '10M', '20M', '30M', '40M', '50M', '60M']
        HomePage.Home._utils.synchronize_with_number_of_element("[class='riser!s0!g0!mbar!']", 1, 30)
        chart_obj.verify_y_axis_title_in_run_window(['Discount'], parent_css='.chartPanel ', msg="Step 11.01 : Verify Chart title")
        chart_obj.verify_y_axis_label_in_run_window(y_axis_label, parent_css='', msg="Step 11.01 : Verify Chart labels")
        chart_obj.verify_chart_color_using_get_css_property_in_run_window("[class='riser!s0!g0!mbar!']", 'bar_blue', parent_css='.chartPanel ', msg="Step 11.01 : Verify Chart color")
        HomePage.Home._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Close the run window
        """
        HomePage.RunWindow.switch_to_default_content()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Workspaces.switch_to_frame()
        HomePage.RunWindow.close()
        HomePage.Home._utils.capture_screenshot("12", STEP_12)

        STEP_13 = """
            STEP 13 : In the banner link, click on the top right username > Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("13", STEP_13)

