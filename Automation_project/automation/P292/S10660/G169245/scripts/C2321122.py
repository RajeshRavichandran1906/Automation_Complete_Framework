'''
Created on Jul 24, 2019

@author: Aftab

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2321122
TestCase Name = Test Label position with Label Alignment
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools.login import Login
from common.wftools.page_designer import Design,Preview,Run
from common.wftools.wf_mainpage import Wf_Mainpage
from common.lib.utillity import UtillityMethods
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators
import time

class C2321122_TestClass(BaseTestCase):

    def test_C2321122(self):
        
        """
            CLASS OBJECTS 
        """
        login = Login(self.driver)
        pd_design = Design(self.driver)
        pd_preview = Preview(self.driver)
        pd_run = Run(self.driver)
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
        quick_filter_css = "[title='Quick filter']"
        
        def select_align_label(position= 'left'):
            align_value= 'Align label '+position
            align_value_select = "div[title="+"'"+align_value+"'"+"]"
            align_enable = self.driver.find_element_by_css_selector(align_value_select)
            core_utils.left_click(align_enable)
            time.sleep(2)
            
        def select_position_label(position):
            position_value_select = "div[title="+"'"+position+"'"+"]"
            position_enable = self.driver.find_element_by_css_selector(position_value_select)
            core_utils.left_click(position_enable)
            time.sleep(2)
            
        '''
        Step 1 : Login WF as domain developer.
        '''
        login.invoke_home_page('mriddev', 'mrpassdev')
         
        '''
        Step 2 : Click on Content view from side bar.
        '''
        main_page.select_content_from_sidebar()
        utils.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page.home_page_long_timesleep)
       
        '''
        Step 3 : Expand 'P292_S10660' domain;
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
        Step 4 : Choose Grid 2-1 template.
        '''
        pd_design.select_page_designer_template("Grid 2-1")
        pd_design.wait_for_visible_text(".pd-page-header", "Page")
        
        '''
        Step 5 : Drag and drop Category Sales report into Panel 1, present in Retail Samples > Portal > Small Widgets folder.
        '''
        pd_design.collapse_content_folder('{0}->{1}_{2}'.format(group_id, project_id, suite_id))
        content_folder = 'Retail Samples->Portal->Small Widgets'
        pd_design.drag_content_item_to_container('Category Sales', 'Panel 1', content_folder_path = content_folder)
        
        '''
        Step 6 : Click on quick filter.
        '''
        pd_design.click_quick_filter()
        utils.synchronize_until_element_disappear(quick_filter_css, main_page.home_page_long_timesleep)
        
        '''
        Step 7 : Click on "Category:" control and Open the properties panel.
        '''
        pd_design.select_filter_control_panel(1)
        pd_design.click_property()
        
        '''
        Step 8 : Select Style tab in Properties and select "Align label left" in Label Alignment.
        '''
        pd_design.select_property_tab('style')
        select_align_label('left')
        
        ''''
        Step 08.00 : Verify "Category:" filter control label aligned to left.
        '''
        utils.verify_picture_using_sikuli("C2321122_step08.png", "Step 08.00 : Verify filter control label aligned to the left")
        
        '''
        Step 9 : Click on "Product Model:" filter control and select "Label left" in Label Position and "Align label left" in Label Alignment.
        '''
        pd_design.select_filter_control_panel(2)
        select_position_label('Label left')
        select_align_label('left')
        
        '''
        Step 09.00 : Verify style applied in the filter control.
        '''
        utils.verify_picture_using_sikuli("C2321122_step09.png", "Step 09.00 : Verify style applied in the filter control.")
        
        '''
        Step 10 : Click on "Region:" filter control and select "Label right" in Label Position and "Align label right" in Label Alignment.
        '''
        pd_design.select_filter_control_panel(3)
        select_position_label('Label right')
        select_align_label('right')
        
        '''
        Step 10.00 : Verify style applied in the filter control.
        '''
        utils.verify_picture_using_sikuli("C2321122_step10.png", "Step 10.00 : Verify style applied in the filter control.")
        
        '''
        Step 11 : Click on "Store Type:" filter control and select "Hide Label" in Label Position.
        '''
        pd_design.select_filter_control_panel(4)
        select_position_label('Hide label')
        
        '''
        Step 11.00 : Verify filter control label is not visible and Label Alignment section is disabled.
        '''
        utils.verify_picture_using_sikuli("C2321122_step11.png", "Step 11.00 : Verify filter control label is not visible and Label Alignment section is disabled.")
        
        '''
        Step 12 : Click on "From:" filter control and select "Align label right" in Label Alignment.
        '''
        pd_design.select_filter_control_panel(5)
        select_align_label('right')
        
        '''
        Step 12.00 : Verify style applied in the filter control.
        '''
        utils.verify_picture_using_sikuli("C2321122_step12.png", "Step 12.00 : Verify style applied in the filter control.")
        
        '''
        Step 13 : Click preview.
        '''
        pd_design.click_preview()
        
        '''
        Step 13.00 : Verify applied style retained in page preview.
        '''
        pd_preview.wait_for_visible_text("div[data-ibx-type='pdFilterGrid']", 'Category:')
        utils.verify_picture_using_sikuli("C2321122_step13.png", "Step 13.00 : Verify applied style retained in page preview.")
        
        '''
        Step 14 : Return back to designer.
        '''
        pd_preview.go_back_to_design_from_preview()   
          
        '''
        Step 15 : Save page designer as "C2321122" and close the designer.
        '''  
        pd_design.save_page_from_toolbar('C2321122')
        pd_design.close_page_designer_from_application_menu()
        core_utils.switch_to_previous_window(window_close = False)
        
        '''
        Step 16 : Run "C2321122" page.
        '''
        pd_design.run_page_designer('C2321122')
        
        '''
        Step 17 : Close run window.
        '''     
        pd_run.close_homepage_run_window()
                 
        '''
        Step 18 : Sign out WF.
        '''
        main_page.signout_from_username_dropdown_menu() 

if __name__ == '__main__':
    unittest.main()