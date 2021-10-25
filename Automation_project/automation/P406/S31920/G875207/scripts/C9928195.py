"""----------------------------------------------------
Author Name : Robert
Automated on : 05 June 2020
----------------------------------------------------"""
from common.lib.basetestcase import BaseTestCase
from common.wftools.paris_home_page import ParisHomePage
from common.lib.utillity import UtillityMethods

class C9928195_TestClass(BaseTestCase):
    
    def test_C9928195(self):
        
        """TESTCASE OBJECTS"""
        
        HomePage = ParisHomePage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """TESTCASE VARIABLES"""
        assemble_css=".tool-list-menu .tlm-assemble"
        blank_template_btn_css="div[class*='df-tp-item'][title='Blank']"
        pd_page_title_css="div[class*='pd-page-title'] ,ibx-label-text"
        pd_page_title="Page Heading"
        
        STEP_01 = """
        Step 01.00 : Sign into WebFOCUS as Administrator.
        """
        HomePage.invoke_with_login('mrid', 'mrpass')
        utils.capture_screenshot('01.00',STEP_01)
        
        STEP_02 = """
        Step 02.00 : Click on 'Workspaces' tab > Click on 'Workspaces'from the navigation bar
        """
        HomePage.Banner.click_workspaces()
        HomePage.Workspaces.switch_to_frame()
        #HomePage.Workspaces.NavigationBar.select_workspaces()
        utils.capture_screenshot('02.00',STEP_02)
        
        STEP_03 = """
        Step 03.00 : Click on the 'Workspaces' in the tree and Click on 'Retail Samples' workspace in the repository tree
        """
        HomePage.Workspaces.ResourcesTree.select_workspaces()
        HomePage.Workspaces.ResourcesTree.select('Retail Samples')
        utils.capture_screenshot('03.00',STEP_03)
        
        STEP_04 = """
        Step 04.00 : Click '+' menu button on the top toolbar and Click 'Assemble Visualizations'
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.click_plus()
        HomePage.Home._utils.synchronize_with_number_of_element(assemble_css,1,30)
        assemble_elem=HomePage.Home._utils.validate_and_get_webdriver_object(assemble_css,'assemble_visualizatoins')
        HomePage.Home._core_utils.left_click(assemble_elem)
        utils.capture_screenshot('04.00',STEP_04)
        
        STEP_05 = """
        Step 05.00 : Select 'Blank Template' in Choose Template dialog
        """
        HomePage.Home._core_utils.switch_to_new_window()
        HomePage.Home._utils.synchronize_with_number_of_element(blank_template_btn_css,1,30)
        blank_elem=HomePage.Home._utils.validate_and_get_webdriver_object(blank_template_btn_css,'assemble_visualizatoins')
        HomePage.Home._core_utils.left_click(blank_elem)
        utils.capture_screenshot('05.00',STEP_05)
        
        STEP_05_01 = """
        Step 05.01 : Verify that only significant words are capitalized in the heading of the page as 'Page Heading'
        """
        HomePage.Home._utils.synchronize_with_number_of_element(pd_page_title_css,1,30)
        HomePage.Home._utils.verify_element_text(pd_page_title_css, pd_page_title, "Step 05:00 Verify that only significant words are capitalized in the heading of the page as 'Page Heading'")
        utils.capture_screenshot('05.01',STEP_05_01)
        
        STEP_06 = """
        Step 06.00 : Close the Designer Framework tool
        """
        HomePage.Home._core_utils.switch_to_previous_window()
        utils.capture_screenshot('06.00',STEP_06)
        
        STEP_07 = """
        Step 07.00 : In the banner link, click on the top right username > Click Sign Out.
        """
        HomePage.Workspaces.switch_to_default_content()
        HomePage.Banner.sign_out()
        utils.capture_screenshot('07.00',STEP_07)