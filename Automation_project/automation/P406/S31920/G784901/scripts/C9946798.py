"""-------------------------------------------------------------------------------------------
Author Name  : Robert
Automated On : 29 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.javascript import JavaScript
from common.locators.paris_home_page import Banner, Workspaces, Home, MyWorkspace
from _sqlite3 import Cursor


class C9946798_TestClass(BaseTestCase):
    
    def test_C9946798(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        File = 'Visualization Example'
        self._javascript = JavaScript(self.driver)
        
        """
        TESCASE VARIABLES
        """
        BANNER_LIST = ['Utilities', 'Settings', 'Help', 'User']
        SECTION_LIST = ['RECENTS', 'FAVORITES', 'PORTALS']
        
        
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
        HomePage.Home._utils.capture_screenshot("01.00", STEP_01) ,
        
        STEP_02 = """
            STEP 02 : Hover over 'WebFOCUS' view
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object_using_locator(Banner.home, "WF Home Logo")
        HomePage.Home._utils.capture_screenshot("02.00", STEP_02)
        
        STEP_02_01 = """
            STEP 02.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        cursor_type=get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("pointer", cursor_type, "Step 02.01 : Verify that the mouse should be a Link select (hand) cursor")
        
        HomePage.Home._utils.capture_screenshot("02.01", STEP_02_01, True)
        
        STEP_03 = """
            STEP 03 : Hover over 'My Workspace' view
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object_using_locator(Banner.my_workspace, "My Workspace")
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_03_01 = """
            STEP 03.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        cursor_type=get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("pointer", cursor_type, "Step 03.01 : Verify that the mouse should be a Link select (hand) cursor")
        
        HomePage.Home._utils.capture_screenshot("03.01", STEP_03_01, True)
                                                
                                                
        STEP_04 = """
            STEP 04 : Hover over 'Shared with Me' view
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object_using_locator(Banner.shared_with_me, "Shared With Me")
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
            STEP 04.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        cursor_type=get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("pointer", cursor_type, "Step 04.01 : Verify that the mouse should be a Link select (hand) cursor")
        
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, True)
        
        STEP_05 = """
            STEP 05 : Single left click on 'Workspaces' view > Hover over 'Workspaces' view
        """
        HomePage.Banner.click_workspaces()
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object_using_locator(Banner.workspaces, "Workspaces")
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        
        STEP_05_01 = """
            STEP 05.1 : Verify that the mouse should be a Normal select (arrow) cursor.
        """
        cursor_type=get_mouse_cursor_by_elem(webelem)
        HomePage.Home._utils.asequal("default", cursor_type, "Step 05.01 : Verify that the mouse should be a Normal select (arrow) cursor.")
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, True)
        
        STEP_06 = """
            STEP 06 : Single left click on 'WebFOCUS' view > Hover over all the banner links one by one (Utilities, Settings, Help and User)
        """
        HomePage.Banner.click_home()
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        STEP_06_01 = """
            STEP 06.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        for option_name in BANNER_LIST:
            option_object = HomePage.Home._utils.validate_and_get_webdriver_object("div[title='"+option_name+"'] div[class*='ibx-label-icon']", "Banner items")
            cursor_type=get_mouse_cursor_by_elem(option_object)
            HomePage.Home._utils.asequal("pointer", cursor_type, "Step 06.01 : Verify for " + option_name + "that the mouse should be a Link select (hand) cursor") 

        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01, True)
        
        STEP_07 = """
            STEP 07 : Hover over '[+]' button
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object_using_locator(Banner.plus_icon, "Plus Icon")
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01 = """
            STEP 07.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        class_str=webelem.get_attribute("class")
        class_list=class_str.split(" ")
        exp_list=['ibx-label', 'icon-left', 'fbx-inline', 'fbx-row', 'fbx-align-items-center']
        s1 = set(exp_list)
        s2 = set(class_list)
        bool_val = s1.issubset(s2)
        cursor_type=get_mouse_cursor_by_elem_css('.icon-left')
        
        if bool_val and cursor_type=="pointer":
            print("Step 07.01 : Verify that the mouse should be a Link select (hand) cursor - PASSED")
        else:
            print("Step 07.01 : Verify that the mouse should be a Link select (hand) cursor - FAILED")
              
#         cursor_type=get_mouse_cursor_by_elem(webelem)
#         HomePage.Home._utils.asequal("pointer", cursor_type, "Step 07.01 : Verify that the mouse should be a Link select (hand) cursor")

        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01, True)
        
        STEP_08 = """
            STEP 08 : Hover over 'Get Data' button
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object_using_locator(Banner.get_data, "Get Data")
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)
        
        STEP_08_01 = """
            STEP 08.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        class_str=webelem.get_attribute("class")
        class_list=class_str.split(" ")
        exp_list=['ibx-label', 'fbx-inline', 'fbx-row', 'fbx-align-items-center', 'fbx-align-content-center']
        s1 = set(exp_list)
        s2 = set(class_list)
        bool_val = s1.issubset(s2)
        cursor_type=get_mouse_cursor_by_elem_css('.fbx-inline')
        
        if bool_val and cursor_type=="pointer":
            print("Step 08.01 : Verify that the mouse should be a Link select (hand) cursor - PASSED")
        else:
            print("Step 08.01 : Verify that the mouse should be a Link select (hand) cursor - FAILED")
#         cursor_type=get_mouse_cursor_by_elem(webelem)
#         HomePage.Home._utils.asequal("pointer", cursor_type, "Step 08.01 : Verify that the mouse should be a Link select (hand) cursor")

        HomePage.Home._utils.capture_screenshot("08.01", STEP_08_01, True)
        
        STEP_09 = """
            STEP 09 : Hover over 'Visualize Data' button
        """
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object_using_locator(Banner.visualize_data, "Visualize Data")
        HomePage.Home._utils.capture_screenshot("09.00", STEP_09)
        
        STEP_09_01 = """
            STEP 09.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        class_str=webelem.get_attribute("class")
        class_list=class_str.split(" ")
        exp_list=['ibx-label', 'fbx-inline', 'fbx-row', 'fbx-align-items-center', 'fbx-align-content-center']
        s1 = set(exp_list)
        s2 = set(class_list)
        bool_val = s1.issubset(s2)
        cursor_type=get_mouse_cursor_by_elem_css('.fbx-inline')
        
        if bool_val and cursor_type=="pointer":
            print("Step 09.01 : Verify that the mouse should be a Link select (hand) cursor - PASSED")
        else:
            print("Step 09.01 : Verify that the mouse should be a Link select (hand) cursor - FAILED")
#         cursor_type=get_mouse_cursor_by_elem(webelem)
#         HomePage.Home._utils.asequal("pointer", cursor_type, "Step 09.01 : Verify that the mouse should be a Link select (hand) cursor")

        HomePage.Home._utils.capture_screenshot("09.01", STEP_09_01, True)
        
        STEP_10 = """
            STEP 10 : Hover over the sections one by one (RECENTS, FAVORITES and PORTALS)
        """
        HomePage.Home._utils.capture_screenshot("10.00", STEP_10)
        
        STEP_10_01 = """
            STEP 10.1 : Verify that the mouse should be a Normal select (arrow) cursor
        """
        for item in SECTION_LIST:
            section_title_css = "div.home-view div[title='"+item+"']"
            cursor_type = get_mouse_cursor_by_elem_css(section_title_css)
            HomePage.Home._utils.asequal("default", cursor_type, "Step 10.01 : Verify for " + item +" that the mouse should be Normal select (arrow) cursor")

        HomePage.Home._utils.capture_screenshot("10.01", STEP_10_01, True)
        
        STEP_11 = """
            STEP 11 : Hover over 'VIEW ALL' link in FAVORITES section
        """
        view_all_button = "div.home-favorites div[title='VIEW ALL']"

        
        HomePage.Home._utils.capture_screenshot("11.00", STEP_11)
        
        STEP_11_01 = """
            STEP 11.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        cursor_type = get_mouse_cursor_by_elem_css(view_all_button)
        HomePage.Home._utils.asequal("pointer", cursor_type, "Step 11.01 : Verify for " + item +" that the mouse should be a Link select (hand) cursor")
        HomePage.Home._utils.capture_screenshot("11.01", STEP_11_01, True)
        
        STEP_12 = """
            STEP 12 : Single left click on 'VIEW ALL' link in FAVORITES section
        """
        viewall_elem = HomePage.Home._utils.validate_and_get_webdriver_object(view_all_button,"VIEW ALL")
        viewall_elem.click()
        
        HomePage.Home._utils.capture_screenshot("12.00", STEP_12)
        
        STEP_12_01 = """
            STEP 12.1 : Verify 'VIEW ALL' window opens
        """
        view_all_displayed_css = ".home-view:not([style*='none']) .view-all-items-results"
        view_all_window = HomePage.Home._utils.validate_and_get_webdriver_object(view_all_displayed_css,"VIEW ALL RESULTS")
        HomePage.Home._utils.verify_element_visiblty(element=view_all_window, visible=True, msg="Step 12.01 : Verify VIEW ALL winow opens")
        HomePage.Home._utils.capture_screenshot("12.01", STEP_12_01, True)
        
        STEP_13 = """
            STEP 13 : Hover over the available Column titles one by one
            (Type, Title, Summary, Tags, and Created On)

        """
        option_list =['Type', 'Title', 'Summary', 'Tags', 'Created On']
        col_title_css = ".dgrid-header-col:not([style*='none']) div.ibx-label-text"
        HomePage.Home._utils.capture_screenshot("13.00", STEP_13)
        
        STEP_13_01 = """
            STEP 13.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        for option_name in option_list:
            option_objects = HomePage.Home._utils.validate_and_get_webdriver_objects(col_title_css, "Column title")
            option_index = self._javascript.find_element_index_by_text(option_objects, option_name)
            cursor_type=get_mouse_cursor_by_elem(option_objects[option_index])
            HomePage.Home._utils.asequal("pointer", cursor_type, "Step 13.01 : Verify for " + option_name + " that the mouse should be a Link select (hand) cursor for all the action tiles available under") 

        HomePage.Home._utils.capture_screenshot("13.01", STEP_13_01, True)
        
        STEP_14 = """
            STEP 14 : Hover over back arrow
        """
        left_arrow = "div.homepage-content:not([style*='none']) .view-all-area .wf-left-arrow"
        cursor_type=get_mouse_cursor_by_elem_css(left_arrow)
        
        HomePage.Home._utils.capture_screenshot("14.00", STEP_14)
        
        STEP_14_01 = """
            STEP 14.1 : Verify that the mouse should be a Link select (hand) cursor
        """
        HomePage.Home._utils.asequal("pointer", cursor_type, "Step 14.01 : Verify that the mouse should be a Link select (hand) cursor for all the action tiles available under")
        
        HomePage.Home._utils.capture_screenshot("14.01", STEP_14_01, True)
        
        STEP_15 = """
            STEP 15 : single left click on the back arrow
        """
        HomePage.Home._utils.capture_screenshot("15.00", STEP_15)
        webelem = HomePage.Home._utils.validate_and_get_webdriver_object(left_arrow, "Left Arrow")
        webelem.click()
        
        STEP_15_01 = """
            STEP 15.1 : Verify it switch back to 'WebFOCUS Home' view
        """
        section_title_css = "div.home-view div[title='RECENTS']"
        HomePage.Home._utils.verify_element_visiblty(element=view_all_window, visible=False, msg="Step 15.01 : Verify it closed View All window")
        HomePage.Home._utils.wait_for_page_loads(50)
        HomePage.Home._utils.verify_element_visiblty(element_css=section_title_css, visible=True, msg="Step 15.01 : Verify it switch back to WF Home")
        
        HomePage.Home._utils.capture_screenshot("15.01", STEP_15_01, True)        
        
        STEP_16 = """
            STEP 16 : Sign Out
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot("16.00", STEP_16)