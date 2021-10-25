'''----------------------------------------------------------------------------------------------------
Author Name     : PRABHAKARAN M
Automated On    : 26-JULY-19
Test Case Title : Creating an IBX Page
-----------------------------------------------------------------------------------------------------'''

from common.lib.basetestcase import BaseTestCase
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.wftools.login import Login
from common.lib.javascript import JavaScript
from common.lib import utillity, core_utility 
import time
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class C2319879_TestClass(BaseTestCase):
    
    def test_C2319879(self):
        
        """ CLASS OBJECTS """  
        pd_design = Design(self.driver)
        login = Login(self.driver)
        homepage = Wf_Mainpage(self.driver)
        javascript = JavaScript(self.driver)
        utils = utillity.UtillityMethods(self.driver)
        core_utils = core_utility.CoreUtillityMethods(self.driver)
        
        """ COMMON VARIABLES """
        FOLDER_XPATH = """//div[@class='ibfs-tree']//div[contains(text(),'P292_S10660~!@#$%^&*()_+=-`{}|][":;')]"""
        TEMPLATE_CSS = ".pd-new-page.pop-top"
        
        """
            STEP 01 : Login WF as domain developer.Click on Content view from side bar.
        """
        login.invoke_home_page('mrid', 'mrpass')
        
        """
            STEP 02 : Click on 'P292_S10660~!@#$%^&*()_+=-`{}|][":;'?><,./' domain;
            Choose Page action tile from under Designer category.
        """
        homepage.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        homepage.expand_repository_folder('Domains')
        folder = self.driver.find_element_by_xpath(FOLDER_XPATH)
        javascript.scrollIntoView(folder)
        core_utils.left_click(folder)
        homepage.select_action_bar_tab("Designer")
        homepage.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text(TEMPLATE_CSS, "Blank", 120)
        
        """
            STEP 03 : Click outside the Select a Template dialog
            Verify that you cant click and do anything
        """
        template = self.driver.find_element_by_css_selector(TEMPLATE_CSS)
        expected_location = template.location
        core_utils.python_left_click(template, element_location="bottom_middle", yoffset=120)
        time.sleep(3)
        actual_location = self.driver.find_element_by_css_selector(TEMPLATE_CSS).location
        utils.asequal(expected_location, actual_location, "Step 03.01 : Verify that you can't click and do anything")
        
        """
            STEP 04 : Close Designer without saving
        """
        pd_design.switch_to_previous_window()
        
        """
            STEP 05 : Sign out WF
        """
        