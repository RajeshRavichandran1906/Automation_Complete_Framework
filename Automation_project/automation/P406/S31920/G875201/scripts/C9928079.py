"""----------------------------------------------------
Author Name : Vishnu_priya
Automated on : 20 Jan 2020
----------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.wftools.designer_portal import Two_Level_Side
from common.locators.designer import page_canvas as Locator

class C9928079_TestClass(BaseTestCase):
    
    def test_C9928079(self):
        
        """TESTCASE OBJECTS"""
        HomePage = ParisHomePage(self.driver)
        two_level_portal = Two_Level_Side(self.driver)
        
        
        """TESTCASE VARIABLES"""
        container_css = Locator.Container.containers
        FOLDER_PATH = "P406_S31920->G875201"
        PAGE_FOLDER = 'My Pages'
        EXPECTED_PAGE_TEMPLATES = ['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1']
        EXPECTED_PANELS_TITLE = ['Container 1', 'Container 2', 'Container 3']
        CUSTOM_TEMPLATE_CSS = "div[data-ibx-type='newPageFromTemplate'][class*='pop-top'] .df-tp-list-custom"
        CUSTOM_TEMPLATE_LINK_CSS = "div[data-ibx-type='newPageFromTemplate'][class*='pop-top'] .df-tp-list-custom a"
        CUSTOM_LINK_EXSTING_PAGE = "div[data-ibx-type='newPageFromTemplate'][class*='pop-top'] .np-open"
        
        STEP_01 = """
        Step 01: Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        HomePage.Home._utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
            Step 03 : Navigate to 'P406_S31920' workspace > Double click on 'G875201' folder
        """
        HomePage.Workspaces.ResourcesTree.select(FOLDER_PATH)
        HomePage.Home._utils.capture_screenshot("03.00", STEP_03)
        
        STEP_04 = """
        Right click on 'V5_Sharing' from the content area > Select Run
        """
        HomePage.Workspaces.ContentArea.right_click_on_folder('V5_Sharing')
        HomePage.ContextMenu.select('Run')
        HomePage.Home._utils.capture_screenshot("04.00", STEP_04)
        
        STEP_04_01 = """
        Verify 'V5_Sharing' run in a new window and you see a sidebar with My Pages and a + sign under it.
        Verify 'V5 Sharing' portal run in a new window with the below URL,
        http://machine_name:port/alias/portal/P406_S31920/G875201/V5_Sharing
        Verify 'TBCO' logo is displayed at the right corner of the portal banner and next to the logo, the portal title is displayed as 'V5_Sharing'
        Verify Banner link is displayed at the right corner of the portal banner.
        Verify In the portal canvas, the sidebar is displayed with 'My Pages' underneath of '+' sign and it consists of a 'collapse navigation' icon
        Verify Empty canvas container with 'There are no pages available' content displayed
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.verify_current_url("portal/P406_S31920/G875201/V5_Sharing", "Step 04.01 : Verify new window with the URL")
        HomePage.Home._utils.verify_element_visiblty(element_css="div.pvd-banner-logo", msg="Step 04.02 : Verify TIBCO logo")
        HomePage.Home._utils.verify_element_text(".pvd-portal-title .ibx-label-text", "V5_Sharing", "Step 04.02 : Verify Portal title")
        two_level_portal.verify_folders_in_left_sidebar([PAGE_FOLDER], 'Step 04.03 : Verify new portal open with My Pages folder')
        two_level_portal.verify_pages_under_the_folder_in_left_sidebar(PAGE_FOLDER, ['+'], "Step 04.04 : Verify 'V5 Portal Share' run in a new window and you see a sidebar with My Pages and a + sign under it")
        two_level_portal.verify_blank_canvas_text("Step 04:05 : Verify blank canvas message", "There are no pages available")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01,expected_image_verify=True)
        
        STEP_05 = """
        Click the + sign
        """
        two_level_portal.click_on_plus_icon_under_the_folder_in_left_sidebar(PAGE_FOLDER)
        HomePage.Home._utils.wait_for_page_loads(40, pause_time=10)
        HomePage.Home._utils.capture_screenshot("05.00", STEP_05)
        
        
        STEP_05_01  = """Verify you see New Page dialog with 4-page templates (Grid 2-1, Grid 2-1 side, Grid 3-3-3, and Grid 4-2-1)
        under 'Common' section and a content of 'No Custom Templates Available!' with 'Learn how to create custom templates' hyperlink available under 'Custom' section
        'Learn to an existing page' hyperlink is availble at the bottom of the dialog
        """
        two_level_portal.verify_new_page_templates(EXPECTED_PAGE_TEMPLATES, 'Step 05.01 : Verify you see 4-page templates (Grid 2-1, Grid 2-1 side, Grid 3-3-3, and Grid 4-2-1)')
        CUSTOM_ACTUAL_TEXT = self.driver.find_element_by_css_selector(CUSTOM_TEMPLATE_CSS).text.replace('\n','').strip()
        CUSTOM_LINK_ACTUAL_TEXT = self.driver.find_element_by_css_selector(CUSTOM_TEMPLATE_LINK_CSS).text.replace('\n','').strip()
        CUSTOM_LINK_EP_ACTUAL_TEXT = self.driver.find_element_by_css_selector(CUSTOM_LINK_EXSTING_PAGE).text.replace('\n','').strip()
        HomePage.Home._utils.asequal(CUSTOM_ACTUAL_TEXT,"No Custom Templates Available! Learn how tocreate customtemplates.", "Step 05.02 : Verify Text under Common Section")
        HomePage.Home._utils.asequal(CUSTOM_LINK_ACTUAL_TEXT,"create custom", "Step 05.02 : Verify Link for Create custom")
        HomePage.Home._utils.asequal(CUSTOM_LINK_EP_ACTUAL_TEXT,"Link to an existing page", "Step 05.02 : Verify Link to existingg page")
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
        Choose 'Grid 2-1' template
        """
        two_level_portal.select_new_page_template('Grid 2-1')
        HomePage.Home._utils.synchronize_with_number_of_element(container_css[1], 3, 190)
        HomePage.Home._utils.capture_screenshot("06.00", STEP_06)
        
        
        STEP_06_01 = """
        Verify 'Page1' is created in the sidebar underneath of 'My Pages'
        Potal page is loaded with a three containers namely 'Container 1', 'Container 2',and 'Container 3' with a '+' sign inside the containers.
        Page header displayed with the 'Page Heading' as a title
        Page toolbar is placed at the right corner of the page header with 'Share', 'Refresh', 'Bookmarks with dropdown icon', 'Delete', and 'Export to file with dropdown icon' buttons.
        By default all the page toolbar is in gery color.
        """
        two_level_portal.verify_folders_in_left_sidebar([PAGE_FOLDER], 'Step 06.01 : Verify folders on the left side')
        two_level_portal.verify_all_containers_title(EXPECTED_PANELS_TITLE, 'Step 06.02 : Verify the page is loaded with 3 panels')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[0], 'Step 06.03 : Verify Panel 1 has a + sign')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[1], 'Step 06.04 : Verify Panel 2 has a + sign')
        two_level_portal.verify_panel_add_content_displayed_in_container(EXPECTED_PANELS_TITLE[2], 'Step 06.05 : Verify Panel 3 has a + sign')
        two_level_portal.verify_page_header_title("Page Heading", "Step 06.06 Verify Page Header title")
        
        
        #two_level_portal.verify_page_header_specific_buttons(['Share', 'Refresh', 'Bookmark', 'Delete','Export to file'], "Step 06.06 : Verify page toolbar has 'Share', 'Refresh', 'Delete' buttons")
        two_level_portal.verify_page_header_button_color('Share', 'Step 06.07 : Verify Share button displayed in grey color')
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01,expected_image_verify=True)
        
        STEP_07 = """
        Hover over the mouse to the 'Share' button in the personal page toolbar
        """
        HomePage.Home._utils.capture_screenshot("07.00", STEP_07)
        
        STEP_07_01  = """
        Verify the tooltip shows 'Share'.
        """
        two_level_portal.verify_page_header_button_tooltip("Share", "Step 07.01 : Verify the tooltip shows 'Share'")
        two_level_portal.verify_page_header_button_tooltip("Refresh", "Step 07.01 : Verify the tooltip shows 'Refresh'")
        two_level_portal.verify_page_header_button_tooltip("Bookmarks", "Step 07.01 : Verify the tooltip shows 'Bookmarks'")
        two_level_portal.verify_page_header_button_tooltip("Delete", "Step 07.01 : Verify the tooltip shows 'Delete'")
        two_level_portal.verify_page_header_button_tooltip("Export to file", "Step 07.01 : Verify the tooltip shows 'Export'")
        HomePage.Home._utils.capture_screenshot("07.01", STEP_07_01)
        
        STEP_08 = """
        Close the portal run window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot("08.00", STEP_08)
        
        STEP_09 = """
        Step 09 In the banner link, click on the top right username > Click Sign Out.
        """
        
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('09.00',STEP_09)
        
if __name__ == '__main__':
    unittest.main()