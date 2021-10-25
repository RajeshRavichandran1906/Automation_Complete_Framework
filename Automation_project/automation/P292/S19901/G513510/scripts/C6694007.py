'''
Created on November 27, 2018

@author: Magesh

Testcase Name : Adding personal pages as basic user
Testcase ID : http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6694007
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C6694007_TestClass(BaseTestCase):
    
    def test_C6694007(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        designer_portal_obj=designer_portal.Two_Level_Side(self.driver)
        designer_canvas_obj=designer_portal.Canvas(self.driver)
        
        util_obj = utillity.UtillityMethods(self.driver)
        domains_css = "div[title='Domains'] .ibx-label-text"
        portal_css = "div[title*='V5 Personal Portal'] .ibx-label-text"
        portal_name="V5 Personal Portal"
        folder_name="My Pages"
        expected_item_list=['V5 Personal Portal']
        expected_templates=['Grid 2-1', 'Grid 2-1 Side', 'Grid 3-3-3', 'Grid 4-2-1']
        expected_containers_title=['Panel 1', 'Panel 2', 'Panel 3', 'Panel 4', 'Panel 5', 'Panel 6', 'Panel 7']
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder. 
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(domains_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        
        """ 
        Step 2.1: Verify V5 Personal Portal appear as an item.
        """
        util_obj.synchronize_with_number_of_element(portal_css, 1, 20)
        main_page_obj.verify_items_in_grid_view(expected_item_list, 'asin', "Step:2.1")
        
        """
        Step 3: Right click on 'V5 Personal Portal' > Click Run. 
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run')
        
        """
        Step 3.1: Verify 'V5 Personal Portal' opens in a new tab.
        """
        util_obj.switch_to_window(1)
        actual_page_title = self.driver.title
        expected_page_title = 'V5 Personal Portal'
        util_obj.asequal(expected_page_title, actual_page_title, "Step 3.1. Verify 'V5 Personal Portal' opens in a new tab.")
        
        """
        Step 4. Under My Pages > click + sign.
        """
        designer_portal_obj.click_on_plus_icon_under_the_folder_in_left_sidebar(folder_name)
        
        """
        Step 4.1. Verify you see 3 page templates
        """
        util_obj.synchronize_with_number_of_element(".ibx-dialog-content .np-list .np-item", 4, 30)
        designer_portal_obj.verify_new_page_templates(expected_templates, 'Step 4.1. Verify you see 3 page templates')
        
        """
        Step 5. Click Grid 4-2-1 template
        """
        designer_portal_obj.select_new_page_template('Grid 4-2-1')
        
        """
        Step 5.1. Verify the page is loaded with 7 panels and each have a + sign inside of them the top bar of the page on the same line 
        as the header has Share, refresh and delete icons.
        """
        grid_css=".pd-container-title-bar"
        util_obj.synchronize_with_number_of_element(grid_css, 7, 40)
        designer_canvas_obj.verify_all_containers_title(expected_containers_title, 'Step 5.1. Verify page is loaded with 3 panels')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 1', 'Step 5.1. Verify add button present for Panel 1')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 2', 'Step 5.1. Verify add button present for Panel 2')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 3', 'Step 5.1. Verify add button present for Panel 3')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 4', 'Step 5.1. Verify add button present for Panel 4')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 5', 'Step 5.1. Verify add button present for Panel 5')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 6', 'Step 5.1. Verify add button present for Panel 6')
        designer_canvas_obj.verify_panel_add_content_displayed_in_container('Panel 7', 'Step 5.1. Verify add button present for Panel 7')
        designer_canvas_obj.verify_page_header_specific_buttons(['Share', 'Refresh', 'Delete'], 'Step 5.1. Verify page header has Share, refresh and delete icons')
        
        """
        Step 6. Hover over the + sign
        Step 6.1. Verify there is a Add content tool tip.
        """
        designer_canvas_obj.verify_panel_add_content_tooltip_in_container('Panel 1', 'Add content', 'Step 6.1: Verify Add content tooltip')
        
        """
        Step 7. Close the 'V5 Personal Portal' run window.
        """
        util_obj.switch_to_main_window()
        
        """
        Step 8. In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()        