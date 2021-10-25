'''
Created on March 29,2019

@author: Niranjan
Testcase Name : Move v5 portal across domains/subfolders
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261730
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.lib import core_utility
from common.pages.wf_mainpage import Wf_Mainpage

class C8261730_TestClass(BaseTestCase):
    
    def test_C8261730(self):
        
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utill_obj = core_utility.CoreUtillityMethods(self.driver)
        main_pages_obj = Wf_Mainpage(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        content_area_css = "div[class*='files-box-files']"
        
        """
        Test case variables
        """
        expected_domain = "P292_S19901"
        expected_folder = 'G520448'
        
        def drag_drop_portal_from_resource_tree_to_content_area(tree_content):
            main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
            drag_obj = main_pages_obj.get_repository_folder('v5-navigation-test2')
#             drag_portal = core_utill_obj.get_web_element_coordinate(drag_obj)
            main_page_obj.expand_repository_folder(expected_domain+'->'+tree_content)
            
            drop_obj = util_obj.validate_and_get_webdriver_object(content_area_css, 'drop_obj')
            drop_portal = core_utill_obj.get_web_element_coordinate(drop_obj)
            drag_portal = core_utill_obj.get_web_element_coordinate(drag_obj)
            util_obj.drag_drop_on_screen(sx_offset=drag_portal['x'], sy_offset=drag_portal['y'], tx_offset=drop_portal['x'], ty_offset=drop_portal['y'])
        
        def drag_drop_portal_from_content_area_to_resource_tree(tree_content):
            main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
            drag_obj = main_pages_obj.get_domain_folder_item('v5-navigation-test2')
            
            drop_obj = main_pages_obj.get_repository_folder(tree_content)
            drop_portal = core_utill_obj.get_web_element_coordinate(drop_obj)
            drag_portal = core_utill_obj.get_web_element_coordinate(drag_obj)
            util_obj.drag_drop_on_screen(sx_offset=drag_portal['x'], sy_offset=drag_portal['y'], tx_offset=drop_portal['x'], ty_offset=drop_portal['y'])
            
        """
        Step 1: Login WF new home page as domain developer
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """ 
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains')
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """ 
        Step 3: Expand 'P292_S19901' domain-> Click on 'G520448' folder
        'v5-navigation-test2' portal is available under G520448 folder in both Content tree and in content area.
        """
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_folders_in_grid_view(['v5-navigation-test2'], 'asin', "Step 3.1: 'v5-navigation-test2' portal is available under G520448 folder in content area")
        main_pages_obj.verify_repository_folders(expected_domain+'->'+expected_folder, ['v5-navigation-test2'], "Step 3.2: 'v5-navigation-test2' portal is available under G520448 folder in content tree")
        
        """
        Step 4: Drag 'v5-navigation-test2' portal from resource tree and drop it under 'P292_S19901' domain-> My content folder in the content area
        Verify portal is not removed from under 'P292_S19901' domain in resource tree and not available in the content area under 'My Content' folder too
        """
        drag_drop_portal_from_resource_tree_to_content_area('My Content')
        main_pages_obj.verify_repository_folders(expected_domain+'->'+expected_folder, ['v5-navigation-test2'], 'Step 4.1: Verify portal is not removed from under P292_S19901 domain in resource tree')
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder+'->'+'My Content')
        main_page_obj.verify_folders_in_grid_view(['v5-navigation-test2'], 'asnotin', 'Step 4.2: Verify portal not available in the content area under My Content folder too')
        
        """
        Step 5: Drag 'v5-navigation-test2' portal from the resource tree and drop it under Public folder from the content area
        Verify portal is not removed from under 'P292_S19901' domain in resource tree and not available in the content area under 'Public' folder too
        """
        drag_drop_portal_from_resource_tree_to_content_area('Public')
        main_pages_obj.verify_repository_folders(expected_domain+'->'+expected_folder, ['v5-navigation-test2'], 'Step 5.1: Verify portal is not removed from under P292_S19901 domain in resource tree')
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder+'->'+'Public')
        main_page_obj.verify_folders_in_grid_view(['v5-navigation-test2'], 'asnotin', 'Step 5.2: Verify portal not available in the content area under Public folder too')
        
        """
        Step 6: Drag 'v5-navigation-test2' portal from content area and drop it under 'P292_S19901' domain-> My content folder in the resource tree
        Verify portal is not removed from under 'P292_S19901' domain in the content area and not available in the resource tree under 'My Content' folder too
        """
        drag_drop_portal_from_content_area_to_resource_tree('My Content')
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        main_page_obj.verify_folders_in_grid_view(['v5-navigation-test2'], 'asin', 'Step 6.1: Verify portal is not removed from under P292_S19901 domain in the content area')
        main_pages_obj.collapse_repository_folders(expected_folder)
        main_pages_obj.verify_repository_folders(expected_domain+'->'+'My Content', ['v5-navigation-test2'], 'Step 6.2: Verify portal not available in the resource tree under My Content folder too', comparion_type='asnotin')        
        
        """
        Step 7: Drag 'v5-navigation-test2' portal from the content area and drop it under Public folder in the resource tree
        Verify portal is not removed from under 'P292_S19901' domain in the content area and not available in the resource tree under 'Public' folder too
        """
        drag_drop_portal_from_content_area_to_resource_tree('Public')
        main_page_obj.expand_repository_folder(expected_domain+'->'+expected_folder)
        main_page_obj.verify_folders_in_grid_view(['v5-navigation-test2'], 'asin', 'Step 7.1: Verify portal is not removed from under P292_S19901 domain in the content area')
        main_pages_obj.collapse_repository_folders(expected_folder)
        main_pages_obj.verify_repository_folders(expected_domain+'->'+'Public', ['v5-navigation-test2'], 'Step 7.2: Verify portal not available in the resource tree under Public folder too', comparion_type='asnotin')
        
        """
        Step 8: Signout WF
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()