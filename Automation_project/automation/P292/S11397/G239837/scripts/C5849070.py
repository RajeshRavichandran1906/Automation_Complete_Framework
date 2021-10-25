'''
Created on April 3,2019

@author: Niranjan/Samuel
Testcase Name : Verify Drag and Drop folder from tree to tree
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/5849070
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.pages.wf_mainpage import Wf_Mainpage
from common.locators import wf_mainpage_locators

class C5849070_TestClass(BaseTestCase):
    
    def test_C5849070(self):
        
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        main_pages_obj = Wf_Mainpage(self.driver)
        loc_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        ok_button_css = ".pop-top [class*='ibx-dialog-ok-button']"
        pop_up_css = ".pop-top .ibx-dialog-content"
        
        """
        Test case variables
        """
        project_id = core_utill_obj.parseinitfile('project_id')
        suite_id = core_utill_obj.parseinitfile('suite_id')
        group_id= core_utill_obj.parseinitfile('group_id')
        expected_domain = project_id+'_'+suite_id
        expected_folder = group_id
        actual_pop_up = 'Are you sure you wish to move these resources?'
        
        def drag_fex_from_content_area_to_tree(domain_item, tree_item):
            util_obj.synchronize_with_visble_text(loc_obj.content_area_css, domain_item, main_page_obj.home_page_medium_timesleep)
            drag_obj = main_pages_obj.get_domain_folder_item(domain_item)
            core_utill_obj.left_click(drag_obj)
            drag_fex = core_utill_obj.get_web_element_coordinate(drag_obj)
            drop_obj = main_pages_obj.get_repository_folder(tree_item)
            drop_folder = core_utill_obj.get_web_element_coordinate(drop_obj)
            core_utill_obj.drag_and_drop_without_using_click(drag_fex['x'], drag_fex['y'], drop_folder['x'], drop_folder['y'])
         
        """
        Step 1: Sign in to WebFOCUS Home Page as Developer User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """ 
        Step 2: Click Content View from the side bar > Click on Domains from the resource tree
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 3: Click "Retail Sample_1" domain in resource tree
        """
        main_page_obj.expand_repository_folder('Retail Samples_1')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Drag Reports folder and drop it on "P292_S11397"-> G239837 folder in the Tree.
        Verify Warning message displays as "Are you sure you wish to move these resources".
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        main_page_obj.expand_repository_folder('Retail Samples_1')
        drag_fex_from_content_area_to_tree('Reports', expected_folder)
        util_obj.verify_element_text(pop_up_css, actual_pop_up, 'Step 4.1: Verify Warning message displays as Are you sure you wish to move these resources')
        
        """
        Step 5: Click on Yes button
        Verify Reports folder appears under "P292_S11397" -> G239837 folder in the Tree and in content area.
        """
        util_obj.synchronize_with_visble_text(ok_button_css, 'Yes', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Yes')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        main_pages_obj.verify_repository_folders(expected_domain+'->'+expected_folder, ['Reports'], 'Step 5.1: Verify Reports folder appears under "P292_S11397" -> G239837 folder in the Tree')
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        main_page_obj.verify_folders_in_grid_view(['Reports'], 'asin', 'Step 5.2: Verify Reports folder appears under "P292_S11397" -> G239837 folder in the content area')
        
        """
        Step 6: Drag Reports folder from under "P292_S11397"-> G239837 folder and drop it under "Retail Sample_1" domain in the Tree
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        drag_fex_from_content_area_to_tree('Reports', 'Retail Samples_1')
        
        """
        Step 7: Click on Yes button
        Verify Reports folder appears under "Retail Sample_1" domain in the Tree and in content area.
        """
        util_obj.synchronize_with_visble_text(ok_button_css, 'Yes', main_page_obj.home_page_medium_timesleep)
        main_page_obj.click_button_on_popup_dialog('Yes')
        util_obj.synchronize_with_visble_text(loc_obj.content_area_css, 'Designer', main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(expected_domain+'->Retail Samples_1')
        main_page_obj.verify_folders_in_grid_view(['Reports'], 'asin', 'Step 7.1: Verify Reports folder appears under "Retail Sample_1" domain in the Tree and in content area.')
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()