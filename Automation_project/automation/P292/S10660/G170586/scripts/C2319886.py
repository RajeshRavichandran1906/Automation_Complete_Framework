'''
Created on Jul 25, 2019

@author: Nirajan

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2319886
TestCase Name = Add content into sections As New Slide
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
import time,pyautogui
from common.lib.javascript import JavaScript

class C2319886_TestClass(BaseTestCase):

    def test_C2319886(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        main_page = Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        core_utils = CoreUtillityMethods(self.driver)
        j_script = JavaScript(self.driver)
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
        Step 5 : Drag Red onto the canvas.
        '''
        pd_design.drag_content_item_to_blank_canvas('Red', 1, content_folder_path = content_folder)
        time.sleep(2)
        
        '''
        Step 6 : Drag Green over Red.
        '''
        pd_design.drag_content_item_to_container('Green', 'Red')
        pd_design.wait_for_visible_text(pop_top_css,'Add content as new tab')
        
        '''
        Step 06.00: Verify a pop up window appears.
        '''
        expected_content_options =['Replace content', 'Add content as new tab', 'Cancel']
        pd_design.verify_add_content_panel_dialog(expected_content_options, msg="Step 06.00 : Verify a pop up window appears")
        
        '''
        Step 7 : Click on Add content dropdown and choose Add content as new slide.
        '''
        pd_design.select_options_from_add_content_dropdown('Add content as new slide')
        utils.synchronize_until_element_disappear(pop_top_css, 9)
        
        '''
        Step 07.00 : A Carousel container should have been created.
        '''
        utils.verify_picture_using_sikuli('C2319886_step_07.png', 'Step 07.00: Verify Carousel container created')
        
        '''
        Step 8 : Mouse hover on the right side of the container.
        '''
        pyautogui.moveTo(552, 350)
        
#         next_slide_elem = self.driver.find_element_by_css_selector('div[tabindex="0"][title="Next slide"]')
#         next_button = next_slide_elem.location
#         utils.mouse_action_using_pyautogui(next_slide_elem, next_button['x'], next_button['y'],'mouse_move', cord_type='middle' )
        
        '''
        Step 08.00 : Verify Next slide arrow is appears.
        '''
        next_slide_elem = self.driver.find_element_by_css_selector('div[tabindex="0"][title="Next slide"]')
        actual = j_script.get_element_before_style_properties(next_slide_elem, 'content').replace('"', '')
        expected = '\ue315'
        utils.asequal(actual,expected,"Step 08.00 : Verify Next slide arrow is appears")
        
        '''
        Step 9 : Click on Next slide.
        '''
        core_utils.left_click(next_slide_elem)
                
        '''
        Step 09.00 : Verify Red is in view.
        '''
        core_utils.switch_to_frame(frame_css="div[aria-label='Carousel Items']>div:nth-child(1) iframe")
        color_attribute=self.driver.find_element_by_css_selector('body').get_attribute('style')
        utils.asequal(color_attribute,'background-color: red;',"Step 09.00 : Verify color in Panel Red")
        core_utils.switch_to_default_content()
               
        '''
        Step 10 : Click on Next slide.
        '''
        core_utils.left_click(next_slide_elem)
        
        '''
        Step 10.00 : Verify Green is in view.
        '''
        core_utils.switch_to_frame(frame_css="div[aria-label='Carousel Items']>div:nth-child(2) iframe")
        color_attribute=self.driver.find_element_by_css_selector('body').get_attribute('style')
        utils.asequal(color_attribute,'background-color: green;',"Step 10.00 : Verify color in Panel green")
        core_utils.switch_to_default_content()
        
        '''
        Step 11 : Click on Previous slide.
        '''
        previous_slide_elem = self.driver.find_element_by_css_selector('div[tabindex="0"][title="Previous slide"]')
        core_utils.left_click(previous_slide_elem)
        
        '''
        Step 11.00 : Verify Red is in view.
        '''
        core_utils.switch_to_frame(frame_css="div[aria-label='Carousel Items']>div:nth-child(1) iframe")
        color_attribute=self.driver.find_element_by_css_selector('body').get_attribute('style')
        utils.asequal(color_attribute,'background-color: red;',"Step 11.00 : Verify color in Panel red")
        core_utils.switch_to_default_content()
        
        '''
        Step 12 : Close Designer without saving.
        '''
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close = False)
        
        '''
        Step 13 : Sign out WF.
        '''
        main_page.signout_from_username_dropdown_menu() 

if __name__ == '__main__':
    unittest.main()