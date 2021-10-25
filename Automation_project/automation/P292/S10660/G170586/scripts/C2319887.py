'''
Created on Jul 25, 2019

@author: Nirajan

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2319887
TestCase Name = Add content into sections As New Accordion Area 
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
import time

class C2319887_TestClass(BaseTestCase):

    def test_C2319887(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
            COMMON TEST CASE VARIABLES 
        """
        project_id  = core_utils.parseinitfile('project_id')
        suite_id    = core_utils.parseinitfile('suite_id')
        group_id    = core_utils.parseinitfile('group_id')
        repository_folder = 'Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id)
        
        """
        TESTCASE CSS
        """
        pop_top_css = ".pop-top"       
        
        '''
        Step 1 : Login WF as domain developer.
                 Click on Content view from side bar.
        '''
        login.invoke_home_page('mrid', 'mrpass')
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
       
        '''
        Step 2 : Expand 'P292_S10660' domain;
        Click on 'G192933' folder and choose Page action tile from under designer category.
        '''
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
 
        '''
        Step 3 : Choose Blank template.
        '''
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        '''
        Step 4 : Click on "G192933 > P292_S10660" domain to go two level up in Content tree;
                 Navigate to Retail samples --> Portal --> Test Widgets folder.
        '''
        pd_design.collapse_content_folder('{0}->{1}_{2}'.format(group_id, project_id, suite_id))
        content_folder = 'Retail Samples->Portal->Test Widgets'
        
        '''
        Step 5 : Drag Gray onto the canvas.
        '''
        pd_design.drag_content_item_to_blank_canvas('Gray', 1, content_folder_path = content_folder)
        time.sleep(2)
        
        '''
        Step 6 : Drag Yellow over Gray.
        '''
        pd_design.drag_content_item_to_container('Yellow', 'Gray')
        pd_design.wait_for_visible_text(pop_top_css,'Add content as new tab')
        
        '''
        Step 06.00: Verify a pop up window appears.
        '''
        expected_content_options =['Replace content', 'Add content as new tab', 'Cancel']
        pd_design.verify_add_content_panel_dialog(expected_content_options, msg="Step 06.00 : Verify a pop up window appears")
        
        '''
        Step 7 : Click on Add content dropdown and choose Add content as new accordion area.
        '''
        pd_design.select_options_from_add_content_dropdown('Add content as new accordion area')
        utils.synchronize_until_element_disappear(pop_top_css, 9)
        
        '''
        Step 07.00 : A new Accordion Container is created.
        '''
        pd_design.accordion_container("Gray").verify_area_title(['Gray', 'Yellow'], "07.01: A new Accordion Container is created")
        
        '''
        Step 8 : Close Designer without saving.
        '''
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close = False)
        
        '''
        Step 9 : Sign out WF.
        '''
        main_page.signout_from_username_dropdown_menu() 

if __name__ == '__main__':
    unittest.main()