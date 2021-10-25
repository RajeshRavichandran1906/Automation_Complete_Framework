"""----------------------------------------------------
Author Name  : Prabhakaran
Automated on : 21 July 2020
----------------------------------------------------"""
import keyboard
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9927892_TestClass(BaseTestCase):
    
    def test_C9927892(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)

        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login('mriddev', 'mrpassdev')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click Workspaces > Click on workspaces from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
            STEP 03 : Right click on 'Retail Samples_1' workspace from the tree
        """
        HomePage.Workspaces.ResourcesTree.expand_workspaces()
        HomePage.Workspaces.ResourcesTree.right_click('Retail Samples_1')
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_03_01 = """
            STEP 03_01 : Verify that the context menu shows Ctrl+V after Paste option (By default disabled)
        """
        HomePage.ContextMenu.verify_disabled_options(['Paste Ctrl+V'], '03.01', 'asin')
        HomePage.Home._utils.capture_screenshot('03.01', STEP_03_01, True)
        
        STEP_04 = """
            STEP 04 : Right click on the 'Reports' folder from the content area
        """
        HomePage.Workspaces.ResourcesTree.right_click('Retail Samples_1->Reports')
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
        
        STEP_04_01 = """
            STEP 04_01 : Verify that the context menu shows the following
            Ctrl+X after Cut option
            Ctrl+C after Copy option
            Ctrl+V after Paste option (By default disabled)
            DEL after Delete option
        """
        HomePage.ContextMenu.verify(['Cut Ctrl+X', 'Copy Ctrl+C', 'Paste Ctrl+V', 'Delete DEL'], '04.01', 'asin')
        HomePage.ContextMenu.verify_disabled_options(['Paste Ctrl+V'], '04.02', 'asin')
        HomePage.Home._utils.capture_screenshot('04.01', STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Click Reports folder under Retail Sample_1 workspace in tree
            Click on "Margin by Product Category" in content area and press "Ctrl+C" from the keyboard.
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER') #Click on OTHER tab to close current context menu
        HomePage.Workspaces.ResourcesTree.select('Retail Samples_1->Reports')
        HomePage.Workspaces.ContentArea.select_file('Margin by Product Category')
        keyboard.press_and_release('ctrl+c')
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)
        
        STEP_06 = """
            STEP 06 : Click anywhere on the empty canvas then press "Ctrl+V" in keyboard
        """
        file_obj = HomePage.Workspaces.ContentArea._get_file_object_('Margin by Product Category')
        HomePage.Home._core_utils.python_left_click(file_obj, 'top_right', xoffset=5, yoffset=-5)
        keyboard.press_and_release('ctrl+v')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Margin by Product Category_1", 60)
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """
            STEP 06.01 : Verified "Margin by Product Category" is copied
        """
        HomePage.Workspaces.ContentArea.verify_files(['Margin by Product Category_1'], '06.01')
        HomePage.Home._utils.capture_screenshot('06.01', STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Click on charts folder under Retail Sample_1 workspace in tree select "Arc - Sales by Region" and press "Ctrl+X" in keyboard
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples_1->Charts')
        HomePage.Workspaces.ContentArea.select_file('Arc - Sales by Region')
        keyboard.press_and_release('ctrl+c')
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_08 = """
            STEP 08 : Click on Reports folder under Retail Sample_1 workspace in tree and click on the content area anywhere in the empty canvas then press "Ctrl+V"
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples_1->Reports')
        file_obj = self.driver.find_element_by_css_selector(HomePage.Workspaces.ContentArea.locators.content_area_css)
        HomePage.Home._core_utils.python_left_click(file_obj, 'top_middle', yoffset=5)
        keyboard.press_and_release('ctrl+v')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Arc - Sales by Region", 60)
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify item is being cut and pasted to new location
        """
        HomePage.Workspaces.ContentArea.verify_files(['Arc - Sales by Region'], '08.01')
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Click Reports folder right click on "Arc - Sales by Region" and select copy
            and click Charts folder in tree click on the content area and press "Ctrl+V"
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples_1->Reports')
        HomePage.Workspaces.ContentArea.right_click_on_file('Arc - Sales by Region')
        HomePage.ContextMenu.select('Copy')
        HomePage.Workspaces.ResourcesTree.select('Retail Samples_1->Charts')
        file_obj = self.driver.find_element_by_css_selector(HomePage.Workspaces.ContentArea.locators.content_area_css)
        HomePage.Home._core_utils.python_left_click(file_obj, 'top_middle', yoffset=5)
        keyboard.press_and_release('ctrl+v')
        HomePage.Home._utils.synchronize_with_visble_text(HomePage.Workspaces.ContentArea.locators.content_area_css, "Arc - Sales by Region_1", 60)
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify the chart is being pasted properly under Charts folder
        """
        HomePage.Workspaces.ContentArea.verify_files(['Arc - Sales by Region_1'], '09.01')
        HomePage.Home._utils.capture_screenshot('09.01', STEP_09_01, True)
        
        STEP_10 = """
            STEP 10.00 : Click on Reports folder under Retail Sample_1 in tree and click "Arc - Sales by Region" from the keyboard press Delete key
        """
        HomePage.Workspaces.ResourcesTree.select('Retail Samples_1->Reports')
        HomePage.Workspaces.ContentArea.select_file('Arc - Sales by Region')
        keyboard.press_and_release('del')
        HomePage.ModalDailogs.Alert.wait_for_appear()
        HomePage.Home._utils.capture_screenshot('10.00', STEP_10)
        
        STEP_10_01 = """
            STEP 10.01 : Verified confirmation deletion message appearing Arc - Sales by Region chart is deleted
        """
        HomePage.ModalDailogs.Alert.verify_title('Delete', '10.01')
        HomePage.ModalDailogs.Alert.verify_message("Are you sure you want to delete 'Arc - Sales by Region' ?", '10.02')
        HomePage.Home._utils.capture_screenshot('10.01', STEP_10_01, True)
        
        STEP_11 = """
            STEP 11.00 : Click Cancel
        """
        HomePage.ModalDailogs.Alert.CancelButton.click()
        HomePage.ModalDailogs.Alert.wait_for_diappear()
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._utils.capture_screenshot('11.00', STEP_11)
        
        STEP_12 = """
            STEP 12.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('12.00', STEP_12)