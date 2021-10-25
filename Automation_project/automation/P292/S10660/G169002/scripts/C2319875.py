'''
Created on Jul 30, 2019

@author: Nirajan

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2319875
TestCase Name = Test Content Tab
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
import pyautogui

class C2319875_TestClass(BaseTestCase):

    def test_C2319875(self):
        
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
        Step 1 : Login WF as domain developer;
        Click on Content view from side bar
        '''
        login.invoke_home_page('mriddev', 'mrpassdev')
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
                 
        '''
        Step 2 : Expand 'P292_S10660' domain;
        Click on 'G192932' folder and choose Page action tile from under designer category.
        '''
        main_page.expand_repository_folder(repository_folder)
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Designer", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tab("Designer")
        utils.synchronize_with_visble_text(locator_obj.content_area_css, "Page", main_page.home_page_medium_timesleep)
        main_page.select_action_bar_tabs_option("Page")
        core_utils.switch_to_new_window()
        utils.synchronize_with_visble_text(pop_top_css, 'Blank', main_page.home_page_long_timesleep)
         
        '''
        Step 3 : Choose the Blank template
        '''
        pd_design.select_page_designer_template("Blank")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
         
        '''
        Step 4 : Click Containers tab and drag Panel, Tab, Carousel and Accordion containers onto the page canvas next to each other and drag the Grid under the Panel 1
        '''
        pd_design.select_option_from_carousel_items("Containers")
        pd_design.drag_container_item_to_blank_canvas("Panel", 1)
        pd_design.drag_container_item_to_blank_canvas("Tab", 4)
        pd_design.drag_container_item_to_blank_canvas("Carousel", 7)
        pd_design.drag_container_item_to_blank_canvas("Accordion", 11)
        pd_design.drag_container_item_to_blank_canvas("Grid", 49, element_location='bottom_middle',yoffset=-1 )
        
        '''
        Step 5 : Click the Contents tab
        '''
        pd_design.select_option_from_carousel_items("Content")
        
        '''
        Step 5.00 : Verify the tree appears on the left side panel
        '''
        pd_design.verify_page_domain_tree_node([group_id], msg ='Step 05.00 : Verify the tree appears on the left side panel')
        
        '''
        Step 6 : Right click on "G192932" folder
        '''
        root_folder = utils.validate_and_get_webdriver_object(".pd-tree .tnode-label .ibx-label-text", 'rootfolder')
        core_utils.python_right_click(root_folder)
        
        '''
        Step 6.00 : Verify that the menu options DO NOT show up
        '''
        try:
            utils.validate_and_get_webdriver_object(pop_top_css,'menu option')
            status='menu appear'
        except AttributeError:
            status='menu not appear'
        utils.asequal('menu not appear', status, 'Step 06.00 : Verify menu option')
                
        '''
        Step 7 : Navigate to Retail samples --> Portal > Test Widgets folder.
        '''
        pd_design.collapse_content_folder('{0}->{1}_{2}'.format(group_id, project_id, suite_id))
        content_folder = 'Retail Samples->Portal->Test Widgets'
        
        '''
        Step 8 : Drag the Blue into Panel 1
        '''
        pd_design.drag_content_item_to_container('Blue', 'Panel 1',content_folder_path=content_folder)
                
        '''
        Step 8.00 : Verify that it takes over the whole panel.
        '''
        core_utils.switch_to_frame(frame_css="div[class='pd-container-content pd-cont-relative'] iframe")
        color_attribute=utils.validate_and_get_webdriver_object('body', 'color').get_attribute('style')
        utils.asequal('background-color: blue;', color_attribute, "Step 8.00 : Verify color in Panel blue")
        core_utils.switch_to_default_content()
        
        '''
        Step 8.10 : Verify that the Panel title changed to Blue.
        '''
        expected_list=['Blue', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5']
        pd_design.verify_containers_title( expected_list, msg='Step 8.10 : Verify container titles')
        
        '''
        Step 9 : Drag Grey onto Panel 2
        '''
        pd_design.drag_content_item_to_container('Gray', 'Panel 2')
        
        '''
        Step 9.00 : Verify Grey added into the tab container and the tab title Tab 1 is changed to Grey and the panel title remained as Panel 2.
        '''
        core_utils.switch_to_frame(frame_css=".pd-cont-tab-page iframe")
        color_attribute=utils.validate_and_get_webdriver_object('body', 'color').get_attribute('style')
        utils.asequal('background-color: dimgray;', color_attribute, "Step 9.00 : Verify tab color grey")
        core_utils.switch_to_default_content()
        
        tab_title = utils.validate_and_get_webdriver_object("div[class*='pd-container-tab-pane'] div[role='tab']", "title").text
        utils.asequal('Gray', tab_title, "Step 9.01 : Verify tab title grey")
        
        '''
        Step 10 : Drag Green over Panel 3
        '''
        pd_design.drag_content_item_to_container('Green', 'Panel 3')
        
        '''
        Step 10.00 : Verify that it takes over the whole panel and the panel title is not changed.
        '''
        core_utils.switch_to_frame(frame_css="div[class*='ibx-carousel'] div:nth-child(2)>div[data-ibx-type='pdContent'] iframe")
        color_attribute=utils.validate_and_get_webdriver_object('body', 'color').get_attribute('style')
        utils.asequal('background-color: green;', color_attribute, "Step 10.00 : Verify tab color green")
        core_utils.switch_to_default_content()
        
        expected_list=['Blue', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5']
        pd_design.verify_containers_title( expected_list, msg='Step 10.01 : Verify container titles')
        
        '''
        Step 11 : Drag Red over Panel 4
        '''
        pd_design.drag_content_item_to_container('Red', 'Panel 4')
        
        '''
        Step 11.00 : Verify that Area 1 is replaced with Red and the content added and the panel title remained as Panel 4
        '''
        core_utils.switch_to_frame(frame_css = 'div[class*="accordion-page"]>div:nth-child(2)>div[data-ibx-type="pdContent"] iframe')
        color_attribute=utils.validate_and_get_webdriver_object('body', 'color').get_attribute('style')
        utils.asequal('background-color: red;', color_attribute, "Step 10.02 : Verify tab color red")
        core_utils.switch_to_default_content()
        
        tab_title = utils.validate_and_get_webdriver_object('.pd-cont-accordion-pane div[class*="ibx-accordion"] div[role="tab"] .ibx-label-text', 'title').text
        utils.asequal('Red', tab_title, "Step 11.00 : Verify accordian title as red")
        
        expected_list=['Blue', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5']
        pd_design.verify_containers_title( expected_list, msg='Step 11.01 : Verify container titles')
        
        '''
        Step 12 : Drag Yellow next to Panel 5
        Step 12.00 : Verify that it takes over the whole panel.
        '''
        pd_design.drag_content_item_to_section_cell_and_verify_drop_color('Yellow', 64, '12.00')
        
        '''
        Step 12.01 : Verify that the Panel title changed to Yellow
        '''
        expected_list=['Blue', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Yellow']
        pd_design.verify_containers_title( expected_list, msg='Step 12.01 : Verify container titles')
        
        '''
        Step 13 : Highlight Silver and drag it onto Test Widgets folder.
        '''
        drag = utils.validate_and_get_webdriver_object("div[class='tnode-children ibx-widget ibx-flexbox ibx-flexbox-vertical fbx-block fbx-column fbx-nowrap fbx-justify-content-start fbx-justify-items-start fbx-align-items-start fbx-align-content-start fbx-child-sizing-content-box']>div:nth-child(7)", "drag")
        dragvalue = core_utils.get_web_element_coordinate(drag)
        drop = utils.validate_and_get_webdriver_object("div[class='tnode-label ibx-widget ibx-flexbox ibx-label icon-left fbx-inline fbx-row fbx-nowrap fbx-justify-content-start fbx-justify-items-start fbx-align-items-center fbx-align-content-center fbx-child-sizing-content-box ibx-sm-selectable'] div[class='ibx-label-text']","drop")
        dropvalue = core_utils.get_web_element_coordinate(drop)
        pyautogui.mouseDown(dragvalue['x'], dragvalue['y'], duration=1)
        pyautogui.moveTo(dropvalue['x'], dropvalue['y'], duration=1)
        pyautogui.mouseUp(dropvalue['x'], dropvalue['y'])
        
        '''
        Step 13.00 : Verify that you are not allowed to make such action and nothing happens.
        '''
        file_check = utils.validate_and_get_webdriver_object('div[class="tnode-children ibx-widget ibx-flexbox ibx-flexbox-vertical fbx-block fbx-column fbx-nowrap fbx-justify-content-start fbx-justify-items-start fbx-align-items-start fbx-align-content-start fbx-child-sizing-content-box"]', 'filecheck')
        actual_list = file_check.text.split('\n')
        expected_list = ['Blue', 'Gray', 'Green', 'Red', 'Silver', 'Yellow', 'Test Widget']
        utils.asequal(expected_list, actual_list, "Step 13.00 : Verify that you are not allowed to make such action and nothing happens")
        
        '''
        Step 14 : Close designer without saving.
        '''
        pd_design.close_page_designer_without_save_page()
        core_utils.switch_to_previous_window(window_close = False)
        
        '''
        Step 15 : Sign out WF.
        '''
        main_page.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()