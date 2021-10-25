'''
Created on April 11, 2019

@author: Vpriya

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261574
TestCase Name = Save Dialog
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib import core_utility
from common.wftools import page_designer
from common.locators import wf_mainpage_locators


class C8261575_TestClass(BaseTestCase):

    def test_C8261575(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        core_utill_obj=core_utility.CoreUtillityMethods(self.driver)
        page_designer_obj=page_designer.Design(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        repository_folder = 'Domains->Retail Samples'
        
        """
        TESTCASE CSS
        """
        caption_title_css=".ibx-title-bar-caption"
        pop_top_css = ".pop-top"
        expected_sort = 'Title'
        expected_sort_list = ['Folders', 'Title', 'arrow_upward']
        save_css="div[title='Save']"
        
        """
        Step 1: Sign in to WebFOCUS as Developer
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content View from the side bar
        """  
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Click on "Retail samples"
        """
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'Reports', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on Other category button then click Text Editor action tile
        """
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.select_action_bar_tabs_option('Text Editor')
        util_obj.synchronize_with_visble_text(caption_title_css,'New Text Resource ', main_page_obj.home_page_medium_timesleep)
        
        
        """
        Step 5: Click fex in New Text Resource dialog
        """
        main_page_obj.click_button_on_popup_dialog('FOCEXEC (fex)')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_until_element_is_visible(save_css,main_page_obj.home_page_medium_timesleep)
        save_elem=util_obj.validate_and_get_webdriver_object(save_css,'Text_editor_save')
        core_utill_obj.python_left_click(save_elem)
        util_obj.synchronize_until_element_is_visible('.sd-files-box-files',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 6: Type * in the search box
        Verify that you see Title sort and not Default Sort
        """
        main_page_obj.select_search_input_box_from_resource_dialog(input_text_msg='*')
        util_obj.synchronize_with_visble_text(pop_top_css, expected_sort, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_view_title_labels_from_resource_dialog(expected_sort_list, 'Step 6.1: Verify that you see Title sort and not Default Sort', view_type='grid_view',label_type='folders')
        
        """
        Step 7: Click Cancel in save as dialog and close the editor window
        """ 
        main_page_obj.click_button_on_popup_dialog('Cancel')
        core_utill_obj.switch_to_previous_window()
        
        """
        Step 8: Click on Designer category button then click Page action tile
        """
        
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'Designer',main_page_obj.home_page_medium_timesleep)
        main_page_obj.select_action_bar_tab("Designer")
        main_page_obj.select_action_bar_tabs_option('Page')
        core_utill_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(caption_title_css,'New Page', main_page_obj.home_page_medium_timesleep)
        

        """
        Step 9: Select Blank template and click Save in toolbar
        """
        page_designer_obj.select_page_designer_template('Blank')
        page_designer_obj.click_toolbar_save()
        util_obj.synchronize_until_element_is_visible('.sd-files-box-files',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 10:Type * in the search box
        """
        """
        Verify that you see Title sort and not Default Sort
        """
        main_page_obj.select_search_input_box_from_resource_dialog(input_text_msg='*')
        util_obj.synchronize_with_visble_text(pop_top_css, expected_sort, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_view_title_labels_from_resource_dialog(expected_sort_list, 'Step 6.1: Verify that you see Title sort and not Default Sort', view_type='grid_view',label_type='folders')
        
        """
        Step 11:Click Cancel in save dialog and close the designer window
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        core_utill_obj.switch_to_previous_window()
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css,'Designer',main_page_obj.home_page_medium_timesleep)
        
        """
        Step 12:Sign out WebFocus.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()