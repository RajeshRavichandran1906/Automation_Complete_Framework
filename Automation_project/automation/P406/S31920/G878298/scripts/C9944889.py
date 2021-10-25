"""-------------------------------------------------------------------------------------------
Author Name : Robert
Automated On : 16 July 2020
-----------------------------------------------------------------------------------------------"""

from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage

class C9944889_TestClass(BaseTestCase):
    
    def test_C9944889(self):
        
        """
        TESTCASE OBJECTS
        """
        HomePage = ParisHomePage(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        BLOG_NAME = "C9944889"
        BLOG_FILE_LIST = [BLOG_NAME]
        BLOG_TEXT = "This is a new blog"
        ADD_COMMENT_CSS = ".annotations_new"
        
        STEP_01 = """
            STEP 01 : Sign into WebFOCUS Home Page as Developer User
        """
        HomePage.invoke_with_login('mriddev','mrpassdev')
        HomePage.Home._utils.capture_screenshot('01.00', STEP_01)
        
        STEP_02 = """
            STEP 02 : Click on 'Workspaces' view > Click on 'Workspaces' from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Home._utils.capture_screenshot('02.00', STEP_02)
        
        STEP_03 = """
        Expand the 'Workspaces' > 'P406_S31920' Workspace > 'G878309' folder >Click on 'Blog Testing' folder
        """
        HomePage.Workspaces.ResourcesTree.select("Workspaces->P406_S31920->G878309->Blog Testing")
        HomePage.Home._utils.capture_screenshot('03.00', STEP_03)
        
        STEP_04="""Click on 'Blog Testing' folder from the resource tree
        """
        HomePage.Workspaces.ContentArea.delete_file_if_exists(BLOG_NAME)
        HomePage.Workspaces.ActionBar.select_tab("OTHER")
        HomePage.Workspaces.ActionBar.select_tab_option("Blog")
        HomePage.Home._utils.capture_screenshot('04.00', STEP_04)
 
        STEP_04_01 = """Verify the following
        New Blog' dialog box opens
        The cursor is in the Title text box by default and it is highlighted
        Cancel button gets enabled and the OK button gets disabled
        """
        HomePage.ModalDailogs.Blog.verify_title("New Blog", "4.01")
        HomePage.ModalDailogs.Blog.Title.verify_border_color('malibu', '04.02')
        HomePage.ModalDailogs.Blog.CancelButton.verify_enabled("04.03")
        HomePage.ModalDailogs.Blog.OKButton.verify_disabled("04.04")
        HomePage.Home._utils.capture_screenshot("04.01", STEP_04_01, expected_image_verify = True)

        STEP_05 = """Enter 'C9944889' in the title and Summary as 'This is a new blog'
        """
        HomePage.ModalDailogs.Blog.Title.enter_text(BLOG_NAME)
        HomePage.ModalDailogs.Blog.Summary.enter_text(BLOG_TEXT)
        HomePage.Home._utils.capture_screenshot('05.00', STEP_05)

        STEP_05_01="""Verify that entering text in the 'Title' entry box gets reflected in the 'Name' entry box as 'Testing_URL_Action_Tile'
        """
        HomePage.ModalDailogs.Blog.Title.verify_text(BLOG_NAME,'05.01')
        HomePage.ModalDailogs.Blog.Summary.verify_text(BLOG_TEXT, '05.02')
        HomePage.Home._utils.capture_screenshot("05.01", STEP_05_01, expected_image_verify = True)
        
        STEP_06 = """Click on the Cancel button
        """
        HomePage.ModalDailogs.Blog.CancelButton.click()
        HomePage.Home._utils.capture_screenshot('06.00', STEP_06)
        
        STEP_06_01 = """Verify that the 'New Blog' dialog closes and 'C9944889' blog has NOT been created in the content area
        """
        HomePage.ModalDailogs.Blog.verify_closed("06.01")
        HomePage.Home._utils.capture_screenshot("06.01", STEP_06_01, expected_image_verify = True)
        
        STEP_07 = """Again, click on 'Blog' action tile > Enter 'C9944889' in the title and Summary as 'This is a new blog
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Blog")
        HomePage.ModalDailogs.Blog.Title.enter_text(BLOG_NAME)
        HomePage.ModalDailogs.Blog.Summary.enter_text(BLOG_TEXT)
        HomePage.Home._utils.capture_screenshot('07.00', STEP_07)
        
        STEP_08 = """Click the OK button
        """
        HomePage.ModalDailogs.Blog.OKButton.click()
        HomePage.Home._utils.capture_screenshot('08.00', STEP_08)
        
        STEP_08_01 = """
        Verify that 'Comments' opens in a new window
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Home._core_utils.switch_to_new_window()
        actual_title = self.driver.title
        msg = "Step 08.01 : Verify Comments opens in a new window"
        HomePage.Home._utils.asin("Comments", actual_title, msg)
        HomePage.Home._utils.capture_screenshot('08.01', STEP_08_01)
        msg="Step 08.02 : Verify Add comment text"
        HomePage.Home._utils.verify_element_text(ADD_COMMENT_CSS, "Add comment...", msg)
        HomePage.Home._utils.capture_screenshot("08.01", STEP_08_01, expected_image_verify = True)
        
        STEP_09 = """Close 'Comments' window
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        HomePage.Home._utils.capture_screenshot('09.00', STEP_09)
        
        STEP_09_01 = """Verify 'C9944889' blog has been created in the content area the same as below:
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files(BLOG_FILE_LIST,"09.01")
        HomePage.Home._utils.capture_screenshot("09.01", STEP_09_01, expected_image_verify = True)
        
        STEP_10 = """Hover over the 'C9944889' blog
        """
        HomePage.Home._utils.capture_screenshot("10.00", STEP_10)
       
        STEP_10_01 = """Verify that the summary displayed as 'This is a new blog'
        """
        HomePage.Workspaces.ContentArea.verify_file_summary(BLOG_NAME, "This is a new blog", "10.01")
        HomePage.Home._utils.capture_screenshot("10.01", STEP_10_01, expected_image_verify = True)
        
        STEP_11 = """Right-click on 'C9944889' > Publish
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(BLOG_NAME)
        HomePage.ContextMenu.select("Publish")
        HomePage.Workspaces.ResourcesTree.select("Blog Testing")
        HomePage.Home._utils.wait_for_page_loads(20)
        HomePage.Home._utils.capture_screenshot("11.00", STEP_11)
        
        STEP_11_01 = """Verify that 'C9944889' blog gets published
        """
        blog_elem=HomePage.Workspaces.ContentArea._get_file_object_(BLOG_NAME)
        actual_class=blog_elem.get_attribute("class")
        msg="STEP 11.01 : Verify item is published"
        HomePage.Home._utils.asin("file-item-published", actual_class,msg)
        
        HomePage.Home._utils.capture_screenshot("11.01", STEP_11_01, expected_image_verify = True)
        
        STEP_12 = """Right-click on 'C9944889' > Delete
        """
        HomePage.Workspaces.ContentArea.right_click_on_file(BLOG_NAME)
        HomePage.ContextMenu.select("Delete")
        HomePage.ModalDailogs.Alert.OKButton.click()
        HomePage.Home._utils.capture_screenshot("12.01", STEP_12)
        
        STEP_12_01 = """Verify that 'C9944889' blog gets deleted
        """
        HomePage.Workspaces.ContentArea.verify_files(BLOG_FILE_LIST,"12.01", "asnotin")
        HomePage.Home._utils.capture_screenshot("12.01", STEP_12_01, expected_image_verify = True)
        STEP_13 = """
            STEP 13 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        HomePage.Home._utils.capture_screenshot('13.00', STEP_13)
        