'''
Created on April 11, 2019

@author: Vpriya

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261574
TestCase Name = Shortcut Dialog
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators


class C8261574_TestClass(BaseTestCase):

    def test_C8261574(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
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
        Step 4: Click on Other category button then click Shortcut action tile
        """
        main_page_obj.select_action_bar_tab('Other')
        main_page_obj.select_action_bar_tabs_option('Shortcut')
        util_obj.synchronize_with_visble_text(caption_title_css,'New Shortcut ', main_page_obj.home_page_medium_timesleep)
        
        
        """
        Step 5: Click the Browse button in New Shortcut dialog
        """
        main_page_obj.click_button_on_popup_dialog('Browse')
        
        
        """
        Step 6: Type * in the search box
        Verify that you see Title sort and not Default Sort
        """
        main_page_obj.select_search_input_box_from_resource_dialog(input_text_msg='*')
        util_obj.synchronize_with_visble_text(pop_top_css, expected_sort, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_view_title_labels_from_resource_dialog(expected_sort_list, 'Step 6.1: Verify that you see Title sort and not Default Sort', view_type='grid_view',label_type='folders')
        
        """
        Step 7: Click Cancel in select dialog
        """ 
        main_page_obj.click_button_on_popup_dialog('Cancel')
        
        """
        Step 8: Click Cancel in New Shortcut dialog
        """
        main_page_obj.click_button_on_popup_dialog('Cancel')
        
        """
        Step 9: Sign out WebFocus.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()