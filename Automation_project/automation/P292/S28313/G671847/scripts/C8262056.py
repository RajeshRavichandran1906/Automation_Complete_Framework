'''
Created on April 16, 2019

@author: AA14564
Testcase Name : UC:Unable to Save ANY changes after editing page
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262056
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools.page_designer import Design
from common.lib import utillity
from common.lib.core_utility import CoreUtillityMethods
from common.locators import wf_mainpage_locators

class C8262056_TestClass(BaseTestCase):
    
    def test_C8262056(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        pd_obj = Design(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        pop_up_dialog_css = ".pop-top"
        page_designer_content_tree_css = ".pd-tree"
        page_designer_canvas_css = "div.pd-page-canvas"
        
        """
        Test case variables
        """
        project_id = core_util_obj.parseinitfile('project_id')
        suite_id = core_util_obj.parseinitfile('suite_id')
        group_id = core_util_obj.parseinitfile('group_id')
        container_title_list = ['Margin by Product Category', 'Category Sales']
        page_name = 'PD-1225'
        
        """
        Step 1: Login WF as domain developer
        """ 
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Click on Content View from side bar
        """ 
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_repository_folder('Domains')
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on 'P292_S28313' domain -> G671847 folder
        """ 
        main_page_obj.click_repository_folder('{0}_{1}->{2}'.format(project_id, suite_id, group_id))
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Page action tile from under Designer category
        """ 
        main_page_obj.select_action_bar_tab('Designer')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Page', main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tabs_option('Page')
         
        """
        Step 5: Choose blank template.
        """ 
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(pop_up_dialog_css, 'Blank', main_page_obj.home_page_medium_timesleep)
        pd_obj.select_page_designer_template('Blank')
        """
        Step 6: Drag and drop 'Margin by Product Category' from under Retail Samples -> Report to the page canvas
        """ 
        util_obj.synchronize_until_element_is_visible(page_designer_content_tree_css, main_page_obj.home_page_medium_timesleep)
        pd_obj.collapse_content_folder('{0}->{1}_{2}'.format(group_id, project_id, suite_id))
        util_obj.synchronize_until_element_is_visible(page_designer_content_tree_css, main_page_obj.home_page_medium_timesleep)
        pd_obj.drag_content_item_to_blank_canvas('Margin by Product Category', 1, content_folder_path='Retail Samples->Reports')
        util_obj.synchronize_with_visble_text(page_designer_canvas_css, 'Margin by Product Category', main_page_obj.home_page_medium_timesleep)
        pd_obj.verify_containers_title([container_title_list[0]], "Step 6: verify panel 'Margin by Product Category' appear.")
         
        """
        Step 7: Save page as 'PD-1225' and close Page designer
        """ 
        pd_obj.save_page_from_toolbar(page_name)
        util_obj.synchronize_with_visble_text(page_designer_canvas_css, 'Margin by Product Category', main_page_obj.home_page_medium_timesleep)
        pd_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 8: Right click on 'PD-1225' from content area and select edit
                Verify 'Margin by Product Category' report still appears
        """ 
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, page_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(page_name, context_menu_item_path='Edit')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_designer_canvas_css, 'Margin by Product Category', main_page_obj.home_page_medium_timesleep)
        pd_obj.verify_containers_title([container_title_list[0]], "Step 8: verify panel 'Margin by Product Category' appear.")
        
        """
        Step 9: Drag and drop 'Category Sales' from under Retail Samples -> Portal -> Small widget to the page canvas
        """ 
        pd_obj.collapse_content_folder('{0}->{1}_{2}'.format(group_id, project_id, suite_id))
        util_obj.synchronize_until_element_is_visible(page_designer_content_tree_css, main_page_obj.home_page_medium_timesleep)
        pd_obj.drag_content_item_to_blank_canvas('Category Sales', 7, content_folder_path='Retail Samples->Portal->Small Widgets')
        util_obj.synchronize_with_visble_text(page_designer_canvas_css, 'Category Sales', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10: Click on Save icon and close Page designer
        """ 
        pd_obj.click_toolbar_save()
        pd_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 11: Right click on 'PD-1225' from content area and select edit
                 Verify both reports are still there.
        """ 
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, page_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.right_click_folder_item_and_select_menu(page_name, context_menu_item_path='Edit')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(page_designer_canvas_css, 'Margin by Product Category', main_page_obj.home_page_medium_timesleep)
        util_obj.synchronize_with_visble_text(page_designer_canvas_css, 'Category Sales', main_page_obj.home_page_medium_timesleep)
        pd_obj.verify_containers_title(container_title_list, "Step 11: verify panel 'Margin by Product Category' appear.")
        
        """
        Step 12: Close page designer
        """ 
        pd_obj.close_page_designer_from_application_menu()
        core_util_obj.switch_to_previous_window(window_close=False)
        
        """
        Step 13: Signout WF 
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()