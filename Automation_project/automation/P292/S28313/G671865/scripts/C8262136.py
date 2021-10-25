'''
Created on December17, 2018

@author: Vpriya
Testcase Name : Create Grid 2-1 personal page
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262136
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity,core_utility
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables
from common.wftools import designer_portal

class C8262136_TestClass(BaseTestCase):
    
    def test_C8262136(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_utility_obj=core_utility.CoreUtillityMethods(self.driver)
        designer_portal_obj=designer_portal.Three_Level(self.driver)
        folder_list=['My Pages']
        expected_templates=['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1']
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3']
        expected_tooltip=["Add content"]
        portal_title = 'V5 Personal Portal_Nav-2'
        project_id=core_utility_obj.parseinitfile('project_id')
        suite_id=core_utility_obj.parseinitfile('suite_id')
        group_id=core_utility_obj.parseinitfile('group_id')
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
                Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G514402 folder.
        """
        main_page_obj.expand_repository_folder('Domains->{0}_{1}->{2}'.format(project_id, suite_id, group_id))
        
        """
        Step 3: Right click on 'V5 Personal Portal_Nav-2' > Run.
                Verify you see a navigation bar with My Pages and a + sign under it.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_title, context_menu_item_path='Run')
        core_utility_obj.switch_to_new_window()
        designer_portal_obj.verify_all_top_folders(folder_list,"Step 3.1:Verify My Pages top folder")
        designer_portal_obj.verify_new_page_plus_icon_from_left_navigation_bar('Step 3.2:Verify you see a navigation bar with + sign under it')
        
        """
        Step 4: Click the + sign
                Verify you see 3 page templates.
        """
        designer_portal_obj.click_new_page_from_left_navigation_bar()
        designer_portal_obj.verify_new_page_templates(expected_templates,"Step 4.1: Verify you see page templates")
        
        """
        Step 5: Click Grid 2-1 template
                Verify the page is loaded with 3 panels and each have a + sign inside of them.
                The top bar of the page on the same line as the header has Share, refresh and delete icons.
        """
        designer_portal_obj.select_new_page_template('Grid 2-1')
        util_obj.synchronize_with_visble_text(".pd-page-title .ibx-label-text", 'Page Heading', main_page_obj.home_page_medium_timesleep)
        designer_portal_obj.verify_all_containers_title(expected_containers_title,"Step 5.1: Verify panels 1, 2, 3 appears.")
        designer_portal_obj.verify_panel_add_content_displayed_in_container('Panel 1',"Step 5.2: Verify panels 1 and a + sign inside.")
        designer_portal_obj.verify_panel_add_content_displayed_in_container('Panel 2',"Step 5.3: Verify panels 2 and a + sign inside.")
        designer_portal_obj.verify_panel_add_content_displayed_in_container('Panel 3',"Step 5.4: Verify panels 3 and a + sign inside.")
        designer_portal_obj.verify_page_header_all_buttons(['Share', 'Refresh', 'Delete'], 'Step 5.5 : Verify page header has Share, refresh and delete icons.')
        
        """
        Step 6: Hover over the + sign
                Verify there is a Add content tool tip.
        """
        designer_portal_obj.verify_panel_add_content_tooltip_in_container('Panel 1', expected_tooltip,"Step 6.1: Verify there is a Add content tool tip")
        
        """ 
        Step 7: Close the 'V5 Personal Portal_Nav-2' run window.
        """
        core_utility_obj.switch_to_previous_window()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 120)
        
        """ 
        Step 8: If not expand, expand 'P292_S19901' domain > G514402 > V5 Personal Portal_Nav-2 > My Pages > click My Content in tree.
                Verify Page 1 appears
        """
        main_page_obj.expand_repository_folder('Domains->{0}_{1}->{2}->{3}->My Pages'.format(project_id, suite_id, group_id, portal_title))
        main_page_obj.expand_repository_folder('My Content', index=1)
        main_page_obj.verify_items_in_grid_view(['Page 1'], 'asin', 'Step 8: Verify P292_S19901>G514402>V5 Personal Portal_Nav-2>My Pages>My Content>Page 1 appears')
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()