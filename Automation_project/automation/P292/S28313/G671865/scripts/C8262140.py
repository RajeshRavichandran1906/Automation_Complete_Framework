'''
Created on December 19, 2018

@author: varun
Testcase Name : Edit the Page title
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262140
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.core_utility import CoreUtillityMethods
from common.wftools.designer_portal import Three_Level

class C8262140_TestClass(BaseTestCase):
    
    def test_C8262140(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        side_bar_obj = Three_Level(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        core_util_obj = CoreUtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        pd_filter_window_css = ".pd-filter-window .ibx-dialog-main-box"
        
        """
        Test case variables
        """
        project = core_util_obj.parseinitfile('project_id')
        suite = core_util_obj.parseinitfile('suite_id')
        group = core_util_obj.parseinitfile('group_id')
        suite_folder = project + '_' + suite
        expand_repository = suite_folder + '-' + '>' + group 
        print(expand_repository)
        portal_name = 'V5 Personal Portal_Nav-2'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G514402 folder.
        """
        main_page_obj.expand_repository_folder(expand_repository)
        
        """
        Step 3: Right click on 'V5 Personal Portal_Nav-2' > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_number_of_element(pd_filter_window_css, 1, base_obj.home_page_long_timesleep)
        
        """
        Step 4: Close filter modal window and Double click on 'Page 1' under My Pages. 
        Step 5: Type title as 'Change page name' and hit enter key.
        Verify the title has been changed.
        """
        main_page_obj.click_button_on_popup_dialog('Close')
        side_bar_obj.rename_page_from_left_navigation_bar('Page 1','Change page name' )
        side_bar_obj.verify_items_in_left_navigation_bar(['Change page name'], 'Step 5.1: Verify the title has been changed')
        
        """
        Step 6: Close the 'V5 Personal Portal_Nav-2' run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out. 
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    