'''
Created on November 26, 2018

@author: Robert
Testcase Name : Create Grid 2-1 personal page
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262115
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.pages import wf_mainpage as pages
from common.pages import portal_sidebar
from common.lib import utillity, core_utility

class C8262115_TestClass(BaseTestCase):
    
    def test_C8262115(self):
       
        """
        Test_case variables
        """
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        pages_obj = pages.Wf_Mainpage(self.driver)
        designer_portal_obj=designer_portal.Two_Level_Side(self.driver)
        designer_canvas_obj=designer_portal.Canvas(self.driver)
        portal_sidebar_obj=portal_sidebar.Two_Level_SideBar(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        portal_name="V5 Personal Portal"
        folder_name="My Pages"
        expected_pages_list=["+"]
        expected_folders_list=["My Pages"]
        expected_templates=['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1']
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3']
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.wait_for_page_loads(30, pause_time=4)
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 20)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        util_obj.wait_for_page_loads(10, pause_time=2)

        """
        Step 3: Right click on 'V5 Personal Portal' > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run')
        
        """
        Step 3.1. Verify you see a side bar with My Pages and a + sign under it.
        """
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text('.bundle-folder-wrapper', 'My Pages', main_page_obj.home_page_long_timesleep)
        portal_sidebar_obj.verify_folders(expected_folders_list, 'Step 3.1. Verify folders in sidebar', 'asin')
        portal_sidebar_obj.verify_pages_in_folder(folder_name, expected_pages_list, 'Step 3.1. Verify pages inside folder', 'asin')        
        
        """
        Step 4. Click the + sign
        """
        designer_portal_obj.click_on_plus_icon_under_the_folder_in_left_sidebar(folder_name)
        
        """
        Step 4.1. Verify you see 3 page templates.
        """
        util_obj.synchronize_with_number_of_element(" .ibx-dialog-content .np-list .np-item", 4, 30)
        designer_portal_obj.verify_new_page_templates(expected_templates, 'Step 4.1. Verify the templates')
        
        """
        Step 5. Click Grid 2-1 template
        """
        designer_portal_obj.select_new_page_template('Grid 2-1')
        
        """
        Step 5.1. Verify the page is loaded with 3 panels and each have a + sign inside of them the top bar of the page on the same line 
        as the header has Share, refresh and delete icons.
        """
        page_heading=".pvd-container"
        util_obj.synchronize_with_visble_text(page_heading, "Page Heading", 80, pause_time=3)
        designer_canvas_obj.verify_all_containers_title(expected_containers_title, 'Step 5.1. Verify page is loaded with 3 panels')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 1', 'Step 5.1. Verify add button present for Panel 1')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 2', 'Step 5.1. Verify add button present for Panel 2')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 3', 'Step 5.1. Verify add button present for Panel 3')
        designer_canvas_obj.verify_page_header_specific_buttons(['Share', 'Refresh', 'Delete'], 'Step 5.1. Verify page header icons')
        
        """
        Step 6. Hover over the + sign
        Step 6.1. Verify there is a Add content tool tip.
        """
        designer_canvas_obj.verify_panel_add_content_tooltip_in_container('Panel 1', 'Add Content', msg='Step 6. Verify Add content tooltip')
        
        """
        Step 7. Close the 'V5 Personal Portal' run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 8. If not expand 'P292_S19901' domain > G513510 > V5 Personal Portal > My Pages > My Content in tree.
        """
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510->'+portal_name+'->My Pages->My Content')
        elem=pages_obj.get_repository_folder('My Content',1)
        core_utility.CoreUtillityMethods.left_click(self, elem)
        action_css="[data-ibxp-text=\"Action Bar\"] .ibx-label-text"
        util_obj.synchronize_with_visble_text(action_css,'Action Bar', 30)
        """
        Step 8.1. Verify Page 1 appears
        """
        expected_list=['Page 1']
        main_page_obj.verify_items_in_grid_view(expected_list, 'asin', 'Step 8.1. Verify Page 1 appears')
        
        """
        Step 9. In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()
        