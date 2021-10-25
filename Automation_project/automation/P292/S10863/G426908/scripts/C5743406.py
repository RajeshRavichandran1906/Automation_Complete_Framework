"""-------------------------------------------------------------------------------------------
Created on July 12, 2019
@author: Vpriya/Rajesh

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/tests/view/22267155&group_by=cases:section_id&group_order=asc&group_id=426908
Test Case Title =  Check Insert section above
-----------------------------------------------------------------------------------------------"""
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools import page_designer
from common.wftools import wf_mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods

class C5743406_TestClass(BaseTestCase):

    def test_C5743406(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = page_designer.Design(self.driver)
        main_page = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
      
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        content_css = "[class*='content-button'][data-ibxp-text='Content']>.ibx-label-text" 
        
        """
            STEP 1 : Login WF as domain developer
        """
        login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text(content_css, "Content", 60)
 
        """
            STEP 2 : Click on Content view from side bar
        """
        main_page.select_content_from_sidebar()

        """
            STEP 3 : Expand 'P292_S10863' domain -> 'G426908' folder;
            Click on Page action tile from under Designer category
        """
        main_page.expand_repository_folder(repository_folder)
        main_page.select_action_bar_tab("Designer")
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        pd_design.wait_for_visible_text("div[class^='pd-new-page']", "Blank")
 
        """
            STEP 4 : Choose blank template
        """
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
 
        """
            STEP 5 : Right mouse click anywhere on the page canvas and choose 'Insert section above' menu
        """
        pd_design.select_page_section_context_menu(1, "Insert section above")
        
        """
            STEP 05.01 : Verify section has been inserted and the second section has been highlighted in red dotted line as below
        """
        pd_design.verify_number_of_page_sections(2, "Step 05.02 : Verify section has been inserted")
        border_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box p'] div[class='pd-selection north']", "North_border css")
        actual_res = border_obj.get_attribute('class')
        msg = "Step 05.02 : Verify second section has been highlighted in red dotted line as below"
        utils.as_notin("hide", actual_res, msg)
        
        border_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box p'] div[class='pd-selection south']", "south_border css")
        actual_res = border_obj.get_attribute('class')
        msg = "Step 05.03 : Verify second section has been highlighted in red dotted line as below"
        utils.as_notin("hide", actual_res, msg)
        
        border_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box p'] div[class='pd-selection east']", "east_border css")
        actual_res = border_obj.get_attribute('class')
        msg = "Step 05.04 : Verify second section has been highlighted in red dotted line as below"
        utils.as_notin("hide", actual_res, msg)
        
        border_obj = utils.validate_and_get_webdriver_object("div[class*='fbx-child-sizing-content-box p'] div[class='pd-selection west']", "west_border css")
        actual_res = border_obj.get_attribute('class')
        msg = "Step 05.05 : Verify second section has been highlighted in red dotted line as below"
        utils.as_notin("hide", actual_res, msg)
        
        """
            STEP 6 : Close page without saving
        """
        pd_design.close_page_designer_without_save_page()
 
        """
            STEP 7 : Sign out WF
        """
        core_utils.switch_to_previous_window(window_close=False)
        main_page.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()