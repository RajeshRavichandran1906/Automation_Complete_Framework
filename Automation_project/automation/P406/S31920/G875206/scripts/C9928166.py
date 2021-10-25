"""----------------------------------------------------
Author Name : vishnu_priya
Automated on : 20 Jan 2020
----------------------------------------------------"""
import unittest
from common.lib.utillity import UtillityMethods
from common.lib.basetestcase import BaseTestCase
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.paris_home_page import ParisHomePage
from common.pages.wf_mainpage import Wf_Mainpage

class C9928166_TestClass(BaseTestCase):
    
    def test_C9928166(self):
        
        """TESTCASE OBJECTS"""       
        utils = UtillityMethods(self.driver)
        HomePage = ParisHomePage(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        home = Wf_Mainpage(self.driver)

        STEP_01 = """
        Step 01.Sign into WebFOCUS Home Page as dev User.
        """
        HomePage.invoke_with_login('mrdevid', 'mrdevpass')
        utils.capture_screenshot('01.00',STEP_01)

        STEP_02 = """
        Step 02.Click on 'Workspaces' tab > Click on 'Workspaces' from the resource tree
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
        Step 03.Expand the 'Workspaces' from the tree and Click on Retail Samples from the resource tree
        """
        HomePage.Workspaces.ResourcesTree.select("Retail Samples")
        HomePage.Workspaces.ContentArea.delete_file_if_exists("C9928166")
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_04 = """
        Step 04 Click on 'Other' category button
        """
        HomePage.Workspaces.ActionBar.select_tab('OTHER')
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """Click on 'Blog' action bar under 'Other' category
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Blog")
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        Step 05.01 Verification -Verify that the cursor is in the Title box by default
        Also, Verify that the OK button is disabled until you start to enter a title
        """
        active_css = HomePage.ModalDailogs.Blog._locator_.textbox_css.format('Title')
        active_element_same = self.driver.find_element_by_css_selector(active_css)
        active_title_element = self.driver.switch_to.active_element
        if active_element_same == active_title_element:
            status = True
        else:
            status = False
        utils.asequal(status, True, 'Step 05.01 : Verify cursor in title text box')
        HomePage.ModalDailogs.Blog.OKButton.verify_disabled('05.02')
        utils.capture_screenshot('05.01',STEP_05_01,expected_image_verify=True)
        
        STEP_06 = """
        Step 06 Enter 'C9928166' in the title
        Enter "This is Test blog" in the summary
        """
        HomePage.ModalDailogs.Blog.Title.enter_text('C9928166')
        HomePage.ModalDailogs.Blog.Summary.enter_text("This is Test blog")
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_07 = """Click the cancel button
        """
        HomePage.ModalDailogs.Blog.CancelButton.click()
        utils.capture_screenshot('07.00',STEP_07)
        
        STEP_07_01 = """Verify that the blog dialog closes and the blog has NOT been created
        """
        try: 
            status = utils.validate_and_get_webdriver_object(".pop-top[role*='dialog']", 'modal dialog').is_displayed()
        except AttributeError:
            status = True
        utils.asequal(status, True, 'Step 07.01 : Verify blog dialog closed')
        HomePage.Workspaces.ContentArea.verify_files(['C9928166'], '07.02', 'asnotin')
        utils.capture_screenshot('07.01',STEP_07_01, expected_image_verify=True)
        
        STEP_08 = """Again Click on 'Blog' action bar
        """
        HomePage.Workspaces.ActionBar.select_tab_option("Blog")
        utils.capture_screenshot('08.00',STEP_08)
        
        STEP_09 = """Enter 'C9928166' in the title
        Enter "This is Test blog" in the summary and click Ok
        """
        HomePage.ModalDailogs.Blog.Title.enter_text('C9928166')
        HomePage.ModalDailogs.Blog.Summary.enter_text("This is Test blog")
        HomePage.ModalDailogs.Blog.OKButton.click()
        utils.capture_screenshot('09.00',STEP_09)
        
        STEP_09_01 = """
        Verification - Verify 'Comments' window opens
        """
        core_utils.switch_to_new_window()
        utils.verify_current_tab_name('Comments', 'Step 09.01 : Verify comments window opens')
        utils.capture_screenshot('09.00',STEP_09_01, expected_image_verify=True)
        
        
        STEP_10_00 = """
        Close that window
        """
        core_utils.switch_to_previous_window()
        core_utils.switch_to_default_content()
        utils.capture_screenshot('10.00',STEP_10_00)
        
        STEP_10_01 = """
        Verify 'C9928166' is displayed in content area
        """
        HomePage.Workspaces.switch_to_frame()
        HomePage.Workspaces.ContentArea.verify_files(["C9928166"],'10.01')
        utils.capture_screenshot('10.00',STEP_10_01, expected_image_verify=True)
        
        STEP_11 = """
        Step 11 Hover over 'C9928166'
        """
        
        retun_obj=home.get_domain_folder_item('C9928166')
        core_utils.python_move_to_element(retun_obj)
        utils.capture_screenshot('11.00',STEP_11)
        
        STEP_11_01 = """
        Verification - Verify that you see the summary
        """
        HomePage.Workspaces.ContentArea.verify_file_summary('C9928166', "This is Test blog", "11.01")
        utils.capture_screenshot('11.00',STEP_11_01,expected_image_verify=True)
        
        STEP_12 = """Right click on 'C9928166' > Delete > Ok
        """
        HomePage.Workspaces.ContentArea.delete_file('C9928166')
        utils.capture_screenshot('12.00',STEP_12)
        
        STEP_13 = """
        Step 13  In the banner link, click on the top right username > Click Signout.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('13.00',STEP_13)
        
if __name__ == "__main__":
    unittest.main()