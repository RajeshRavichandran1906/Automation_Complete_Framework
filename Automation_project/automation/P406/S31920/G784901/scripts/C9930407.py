"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 28 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.javascript import JavaScript
from common.locators.paris_home_page import Workspaces

class C9930407_TestClass(BaseTestCase):
    
    def test_C9930407(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        self._javascript = JavaScript(self.driver)
        
        
        def get_mouse_cursor_by_elem_css(elem_css):
            target_elem = HomePage.Home._utils.validate_and_get_webdriver_object(elem_css, 'CURSOR_ELEMENT_CSS')
            cursor_type=target_elem.value_of_css_property('cursor')
            return cursor_type
        
        def get_mouse_cursor_by_elem(webelement):
            cursor_type=webelement.value_of_css_property('cursor')
            return cursor_type
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Admin User
        """
        HomePage.invoke_with_login('mridadm', 'mrpassadm')
        HomePage.Banner.close_page_message()
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on Workspaces
        """
        HomePage.Banner.click_workspaces()
        
        HomePage.Workspaces.switch_to_frame()
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_03 = """
            STEP 03.00 : Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.NavigationBar.select_workspaces()
        HomePage.Workspaces.ResourcesTree.select('Retail Samples')
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
            STEP 04 : Hover over 'Application' category button
        """
        tab_name = 'APPLICATION'
        
        tab_objects = HomePage.Home._utils.validate_and_get_webdriver_objects_using_locator(Workspaces.ActionBar.tabs, "Action bar tab")
        tab_name_list = [tab.text.strip() for tab in tab_objects]
        print(tab_name_list)
        tab_index = tab_name_list.index(tab_name) if tab_name_list.count(tab_name) else None
        
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.01 : Verify that the mouse should be a Normal select (arrow) cursor
        """
        cursor_type=get_mouse_cursor_by_elem(tab_objects[tab_index])
        HomePage.Home._utils.asequal("default", cursor_type, "Step 04.01 : Verify mouse should be a Normal select (arrow) cursor")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Single left click on 'Portal' action tile
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Portal")
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        STEP_05_01 = """
            STEP 05.01 : Verify 'New Portal' dialog opens
        """
        HomePage.ModalDailogs.V5Portal.verify_title("New Portal", "05.01")
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Click 'Cancel' to close the 'New Portal' dialog
        """
        HomePage.ModalDailogs.V5Portal.CancelButton.click()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_07 = """
            STEP 07 : Single left click on 'Other' category button > Hover over all other action tiles one by one
            (Folder, Upload File, URL, Shortcut and Text Editor)
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        option_list =['Folder', 'Upload File', 'URL', 'Shortcut', 'Text Editor']
        
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.01 : Verify that the mouse should be a Link select (hand) cursor for all the action tiles available under 'Other' category button
        """
        for option_name in option_list:
            option_objects = HomePage.Home._utils.validate_and_get_webdriver_objects_using_locator(Workspaces.ActionBar.tab_options, "Action bar tab options")
            option_index = self._javascript.find_element_index_by_text(option_objects, option_name)
            cursor_type=get_mouse_cursor_by_elem(option_objects[option_index])
            HomePage.Home._utils.asequal("pointer", cursor_type, "Step 07.01 : Verify for " + option_name + "that the mouse should be a Link select (hand) cursor for all the action tiles available under") 

        
        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01, True)


        STEP_08 = """
            STEP 08 : Hover over the plus(+) sign on Retail Samples from the resource tree
        """
        plus_icon_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='Retail Samples']//div[contains(@class,'plus')]"
        webelem = self.driver.find_element_by_xpath(plus_icon_xpath)
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)
        
        STEP_08_01 = """
            STEP 08.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 08.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")
        HomePage.Home._utils.capture_screenshot("08.01", STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Hover the mouse over 'Portal' folder on the content area
        """
        portal_xpath = "//div[contains(@class,'folder-item')]//div[contains(@class,'folder-div')]//div[contains(text(),'Portal')]"
        webelem = self.driver.find_element_by_xpath(portal_xpath)
        HomePage.Home._utils.capture_screenshot("09.00", STEP_09)
        
        STEP_09_01 = """
            STEP 09.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 09.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")
        HomePage.Home._utils.capture_screenshot("09.01", STEP_09_01, True)


        STEP_10 = """
            STEP 10 : Hover over the icon for the 'Portal' folder
        """
        portal_folder_icon_xpath = "(//div[contains(@class,'folder-image-icon')])[6]"
        webelem = self.driver.find_element_by_xpath(portal_folder_icon_xpath)
        HomePage.Home._utils.capture_screenshot("10.00", STEP_10)
        
        STEP_10_01 = """
            STEP 10.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 10.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")
        HomePage.Home._utils.capture_screenshot("10.01", STEP_10_01, True)
        
        STEP_11 = """
            STEP 11 : Double click on Portal > Small Widgets Folder in content area
        """
        HomePage.Workspaces.ContentArea.double_click_on_folder("Portal")
        HomePage.Home._utils.wait_for_page_loads(30)
        HomePage.Workspaces.ContentArea.double_click_on_folder("Small Widgets")
        HomePage.Home._utils.capture_screenshot("11.00", STEP_11)
        
        
        STEP_12 = """
            STEP 12 : Hover over a 'Category Sales' in the content area
        """
        category_sales_xpath = "//div[contains(@class,'file-item')]//div[contains(text(),'Category Sales')]"
        webelem = self.driver.find_element_by_xpath(category_sales_xpath)
        HomePage.Home._utils.capture_screenshot("12.00", STEP_12)
        
        STEP_12_01 = """
            STEP 12.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 12.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")
        
        HomePage.Home._utils.capture_screenshot("12.01", STEP_12_01, True)
        
        STEP_13 = """
            STEP 13 : Hover over the icon for 'Category Sales' in the content area
        """
        category_sales_icon = "(//div[contains(@class,'ds-icon-chart-bar')])[1]"
        webelem = self.driver.find_element_by_xpath(category_sales_icon)
        HomePage.Home._utils.capture_screenshot("13.00", STEP_13)
        
        STEP_13_01 = """
            STEP 13.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 13.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")
        HomePage.Home._utils.capture_screenshot("13.01", STEP_13_01, True)
        
        STEP_14 = """
            STEP 14 : Click on 'List view'
        """
        list_view_button_elem = self.driver.find_element(*HomePage.Workspaces.locators.NavigationBar.list_view)
        list_view_button_elem.click()
        HomePage.Home._utils.capture_screenshot("14.00", STEP_14)
        
        STEP_15 = """
            STEP 15 : Click on 'Portal' folder from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Portal")
        HomePage.Home._utils.capture_screenshot("15.00", STEP_15)
        
        STEP_16 = """
            STEP 16 : Hover the mouse over 'Small Widgets' folder on the content area
        """
        small_widgets_xpath ="//div[contains(@class,'files-box')]//div[contains(text(),'Small Widgets')]"
        webelem = self.driver.find_element_by_xpath(small_widgets_xpath)
        HomePage.Home._utils.capture_screenshot("16.00", STEP_16)
        
        STEP_16_01 = """
            STEP 16.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 16.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")

        HomePage.Home._utils.capture_screenshot("16.01", STEP_16_01, True)
        
        STEP_17 = """
            STEP 17 : Hover over a 'Retail Samples' portal
        """
        retail_samples_xpath = "(//div[contains(@class,'files-box')]//div[normalize-space()='Retail Samples'])[1]"
        webelem = self.driver.find_element_by_xpath(retail_samples_xpath)
        HomePage.Home._utils.capture_screenshot("17.00", STEP_17)
        
        STEP_17_01 = """
            STEP 17.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything.
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 16.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")

        HomePage.Home._utils.capture_screenshot("17.01", STEP_17_01, True)
        
        STEP_18 = """
            STEP 18 : Hover over the available Column titles one by one
            (Title, Summary, Last modified, Size, Published and Shown)
        """
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        option_list =['Title', 'Summary', 'Last modified', 'Size', 'Published', 'Shown']
        
        HomePage.Home._utils.capture_screenshot("18.00", STEP_18)
        
        STEP_18_01 = """
            STEP 18.01 : Verify that the mouse should be a Link select (hand) cursor since single left click performs an action on them.
        """
        for option_name in option_list:
            option_objects = HomePage.Home._utils.validate_and_get_webdriver_objects(".grid-cell-title", "Action bar tab options")
            option_index = self._javascript.find_element_index_by_text(option_objects, option_name)
            cursor_type=get_mouse_cursor_by_elem(option_objects[option_index])
            HomePage.Home._utils.asequal("pointer", cursor_type, "Step 18.01 : Verify for " + option_name + " that the mouse should be a Link select (hand) cursor for all the action tiles available under") 

        HomePage.Home._utils.capture_screenshot("18.01", STEP_18_01, True)
        
        STEP_19 = """
            STEP 19 : Hover over minus(-) sign on Retail Samples from the resource tree
        """
        minus_icon_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='Retail Samples']//div[contains(@class,'minus')]"
        webelem = self.driver.find_element_by_xpath(minus_icon_xpath)

        HomePage.Home._utils.capture_screenshot("19.00", STEP_19)
        
        STEP_19_01 = """
            STEP 19.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 19.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")
        HomePage.Home._utils.capture_screenshot("19.01", STEP_19_01)
        
        STEP_20 = """
            STEP 20 : Hover over 'Charts' folder on the resource tree
        """
        charts_folder_xpath = "//div[@class='ibfs-tree']//div[normalize-space()='Charts']"
        webelem = self.driver.find_element_by_xpath(charts_folder_xpath)
        HomePage.Home._utils.capture_screenshot("20.00", STEP_20)
        
        STEP_20_01 = """
            STEP 20.01 : Verify that the mouse should be a Link select (hand) cursor since single left click performs an action on them.
        """
        cursor_type= get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 20.01 : Verify that the mouse should be a Normal select (arrow) cursor since single left click does not do anything")

        HomePage.Home._utils.capture_screenshot("20.01", STEP_20_01, True)
        
        STEP_21 = """
            STEP 21 : Click on 'Grid view'
        """
        button_elem = self.driver.find_element(*HomePage.Workspaces.locators.NavigationBar.grid_view)
        button_elem.click()
        HomePage.Home._utils.capture_screenshot("21.00", STEP_21)
        
        STEP_22 = """
            STEP 22 : Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("22.00", STEP_22)