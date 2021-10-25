"""-------------------------------------------------------------------------------------------
Author Name  : RAJESH
Automated On : 27-January-2021
-------------------------------------------------------------------------------------------"""
import time
from selenium.webdriver.common.keys import Keys
from common.lib.basetestcase import BaseTestCase
from common.wftools.designer import Designer as DesignerPage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains as ac

class C9946734_TestClass(BaseTestCase):
    
    def test_C9946734(self):
        
        """
        TEST CASE OBJECTS
        """
        Designer = DesignerPage()
        ActionChains = ac(self.driver)
        
        """
        TEST CASE VAIABLES
        """
        content_name = 'G875236->P452_S31923->Retail Samples->Portal->Small Widgets->Category Sales'
            
        STEP_01 = """
            STEP 01 : Launch new Assemble Visualizations as developer user.
    
            https://machine.ibi.com:port/alias/designer?is508=false&item=IBFS:/WFC/Repository/P452_S31923/G875236&tool=framework&startlocation=IBFS:/WFC/Repository/P452_S31923/G875236&startUpConditions=%7B%27mode%27%3A%27assemble%27%7D
        """
        Designer.API.invoke_assemble_visualizations(credential_keys=('mriddev', 'mrpassdev'))
        Designer._utils.capture_screenshot("01", STEP_01)

        STEP_02 = """
            STEP 02 : Choose the Blank template.
        """
        Designer.Dialog.ChooseTemplate.Common.select('Blank')
        Designer._utils.capture_screenshot("02", STEP_02)
        
        STEP_03 = """
            STEP 03 : Select Include Page Filter checkbox in Settings.
        """
        include_page_filter_css = Designer.PropertiesPanel.Settings._locator.include_page_filters[1]
        include_page_filter= Designer._utils.validate_and_get_webdriver_object(include_page_filter_css, 'include filter')
#         include_page_filter.click()
        Designer._core_utils.left_click(include_page_filter)
        Designer._utils.capture_screenshot("03", STEP_03)
        
        STEP_04 = """
            STEP 04 : Click on the back arrow '<' twice in the Content tree and Navigate to Retail samples --> Portal --> Small Widgets folder;
            Drag and drop Category Sales report onto the page canvas.
        """
        Designer.ResourcesPanel.Content.drag_to_page_section(content_name, x=20, y=10)
        Designer.PageCanvas.Containers.Basic('Category Sales').wait_until_loading_complete(30)
        Designer.PageCanvas.Containers.Basic('Category Sales').switch_to_frame()
#         Designer._webelement.wait_for_element_text(Legend.title, 'Product Category', 60)
        Designer._core_utils.switch_to_default_content()
        Designer._utils.capture_screenshot("04", STEP_04)
        

        STEP_05 = """
            STEP 05 : Right click on empty cell in filter bar;
            Select Add filter controls.
        """
        Designer.PageCanvas.FilterGrid.right_click_on_cell(1)
        Designer.ContextMenu.select('Add filter controls')
        Designer.Dialog.AddFilterControls.wait_for_text('Add', time_out=30)
        Designer._utils.capture_screenshot("05", STEP_05)

        STEP_05_EXPECTED = """
            STEP 05 - Expected : Verify Add filter controls window appears.
        """
        Designer.Dialog.AddFilterControls.verify_title('Add Filter Controls', '05.01')
        Designer._utils.capture_screenshot("05 - Expected", STEP_05_EXPECTED, True)
        
        STEP_06 = """
            STEP 06 : Click Cancel button.
        """
        Designer.Dialog.AddFilterControls.CancelButton.click()
        Designer.Dialog.AddFilterControls.wait_until_invisible(time_out=10)
        Designer._utils.capture_screenshot("06", STEP_06)

        STEP_06_EXPECTED = """
            STEP 06 - Expected : Verify Add filter controls window closed and filter controls are not added to the page.
        """
        Designer.PageCanvas.FilterGrid.verify_displayed('06.01')
        def verify_filter_control(step_num):
            try:
                filter_control_css = Designer.PageCanvas.FilterGrid._locator.controls[1]
                self.driver.find_element_by_css_selector(filter_control_css)
            except NoSuchElementException:
                actual = False
                msg = 'Step {0}: Filter Control is not displayed'.format(step_num)
                Designer._utils.asequal(False, actual, msg)
        verify_filter_control('06.02')
        Designer._utils.capture_screenshot("06 - Expected", STEP_06_EXPECTED, True)

        STEP_07 = """
            STEP 07 : Right click on empty cell in filter bar;
            Select Add filter controls.
        """
        Designer.PageCanvas.FilterGrid.right_click_on_cell(1)
        Designer.ContextMenu.select('Add filter controls')
        Designer.Dialog.AddFilterControls.wait_for_text('Add', time_out=30)
        Designer._utils.capture_screenshot("07", STEP_07)

        STEP_07_EXPECTED = """
            STEP 07 - Expected : Verify Add filter controls window appears.
        """
        Designer.Dialog.AddFilterControls.verify_title('Add Filter Controls', '07.01')
        Designer._utils.capture_screenshot("07 - Expected", STEP_07_EXPECTED, True)

        STEP_08 = """
            STEP 08 : Click on X in top right corner of the Add filter controls window.
        """
        Designer.Dialog.AddFilterControls.close()
        Designer.Dialog.AddFilterControls.wait_until_invisible(time_out=10)
        Designer._utils.capture_screenshot("08", STEP_08)

        STEP_08_EXPECTED = """
            STEP 08 - Expected : Verify Add filter controls window closed and filter controls are not added to the page.
        """
        verify_filter_control('08.01')
        Designer.PageCanvas.FilterGrid.verify_displayed('08.02')
        Designer._utils.capture_screenshot("08 - Expected", STEP_08_EXPECTED, True)

        STEP_09 = """
            STEP 09 : Right click on empty cell in filter bar;
            Select Add filter controls.
        """
        Designer.PageCanvas.FilterGrid.right_click_on_cell(1)
        Designer.ContextMenu.select('Add filter controls')
        Designer.Dialog.AddFilterControls.wait_for_text('Add', time_out=30)
        Designer._utils.capture_screenshot("09", STEP_09)

        STEP_10 = """
            STEP 10 : Click on Exclude optional parameters checkbox.
        """
        Designer.Dialog.AddFilterControls.ExcludeOptionalParameters.check()
        Designer._utils.capture_screenshot("10", STEP_10)

        STEP_10_EXPECTED = """
            STEP 10 - Expected : Verify all optional parameters are unchecked and Add filter controls button is disabled.
        """
        Designer.Dialog.AddFilterControls.ParameterCheckbox.verify_unchecked('10.01')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('PRODUCT_CATEGORY').verify_unchecked('10.02')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('MODEL').verify_unchecked('10.03')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('BUSINESS_REGION').verify_unchecked('10.04')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('STORE_TYPE').verify_unchecked('10.05')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('TIME_DATE').verify_unchecked('10.06')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('TIME_DATE_TO').verify_unchecked('10.07')
        Designer.Dialog.AddFilterControls.AddFilterControlsButton.verify_disabled('10.08')
        Designer._utils.capture_screenshot("10 - Expected", STEP_10_EXPECTED, True)

        STEP_11 = """
            STEP 11 : Click on MODEL control dropdown;
            Press Down arrow for two times and press Up arrow.
        """
        Designer.Dialog.AddFilterControls.click_control_dropdown('MODEL')
        ActionChains.send_keys(Keys.DOWN)
        ActionChains.send_keys(Keys.DOWN)
        ActionChains.send_keys(Keys.UP).perform()
        Designer._utils.capture_screenshot("11", STEP_11)

        STEP_11_EXPECTED = """
            STEP 11 - Expected : Verify user can navigate the drop down options using arrow up/down.
        """
        time.sleep(7)
        button_object = Designer.Dialog.AddFilterControls.ControlDropdownOptions._list_option_object('Dropdown')
        background_color = Designer._utils.get_element_css_propery(button_object, 'background-color')
        msg = "Step 11.01 : Verify user can navigate the drop down options using arrow up/down"
        status = True if background_color in ['rgba(0, 0, 66, 1)', 'rgb(0, 0, 66)'] else False
        Designer._utils.asequal(True, status, msg)
        Designer._utils.capture_screenshot("11 - Expected", STEP_11_EXPECTED, True)

        STEP_12 = """
            STEP 12 : Using Down arrow navigate to Button set;
            Press Enter key.
        """
        ActionChains.reset_actions()
        ActionChains.send_keys(Keys.DOWN)
        ActionChains.send_keys(Keys.ENTER).perform()
        Designer._utils.capture_screenshot("12", STEP_12)

        STEP_12_EXPECTED = """
            STEP 12 - Expected : Verify Button set control selected for Model parameter.
        """
        Designer.Dialog.AddFilterControls.verify_selected_control('MODEL', 'Button set', '12.01')
        Designer._utils.capture_screenshot("12 - Expected", STEP_12_EXPECTED, True)

        STEP_13 = """
            STEP 13 : Check Parameter check box.
        """
        Designer.Dialog.AddFilterControls.ParameterCheckbox.check()
        Designer._utils.capture_screenshot("13", STEP_13)

        STEP_13_EXPECTED = """
            STEP 13 - Expected : Verify all parameters are checked and Add filter controls button is enabled.
        """
        Designer.Dialog.AddFilterControls.ParameterCheckbox.verify_checked("13.01")
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('PRODUCT_CATEGORY').verify_checked('13.02')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('MODEL').verify_checked('13.03')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('BUSINESS_REGION').verify_checked('13.04')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('STORE_TYPE').verify_checked('13.05')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('TIME_DATE').verify_checked('13.06')
        Designer.Dialog.AddFilterControls.ParameterOptionCheckbox('TIME_DATE_TO').verify_checked('13.07')
        Designer.Dialog.AddFilterControls.AddFilterControlsButton.verify_enabled('13.08')
        Designer._utils.capture_screenshot("13 - Expected", STEP_13_EXPECTED, True)

        STEP_14 = """
            STEP 14 : Click on BUSINESS_REGION control dropdown;
            Using Down arrow navigate to Radio and press Space key.
        """
        ActionChains.reset_actions()
        Designer.Dialog.AddFilterControls.click_control_dropdown('BUSINESS_REGION')
        ActionChains.send_keys(Keys.DOWN)
        ActionChains.send_keys(Keys.DOWN)
        ActionChains.send_keys(Keys.SPACE).perform()
        Designer._utils.capture_screenshot("14", STEP_14)

        STEP_14_EXPECTED = """
            STEP 14 - Expected : Verify Radio control selected for BUSINESS_REGION parameter.
        """
        Designer.Dialog.AddFilterControls.verify_selected_control('BUSINESS_REGION', 'Radio', '14.01')
        Designer._utils.capture_screenshot("14 - Expected", STEP_14_EXPECTED, True)

        STEP_15 = """
            STEP 15 : Select Filters side tab;
            Click Add all filters to page button
        """
        Designer.Dialog.AddFilterControls.AddFilterControlsButton.click()
        Designer.Dialog.AddFilterControls.wait_until_invisible(20)
        Designer._utils.capture_screenshot("15", STEP_15)
        
        STEP_15_EXPECTED = """
            STEP 15 - Expected : Verify filter controls are added into the page.
        """
        Designer.PageCanvas.FilterGrid.verify_control_labels(['Category:', 'Product Model:', 'Region:', 'Store Type:', 'From:', 'To:'], '15.01')
        Designer._utils.capture_screenshot("15 - Expected", STEP_15_EXPECTED, True)

        STEP_16 = """
            STEP 16 : Logout WF using API without saving:
            http://machine:port/ibi_apps/service/wf_security_logout.jsp
        """
        Designer.API.logout()
        Designer._utils.capture_screenshot("16", STEP_16)

