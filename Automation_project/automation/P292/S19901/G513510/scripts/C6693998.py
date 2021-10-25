'''
Created on November 27, 2018

@author: Robert
Testcase Name : Add personal pages in run mode as developer user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6693998
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.pages import portal_sidebar
from common.lib import utillity

class C6693998_TestClass(BaseTestCase):
    
    def test_C6693998(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        designer_portal_obj=designer_portal.Two_Level_Side(self.driver)
        portal_sidebar_obj=portal_sidebar.Two_Level_SideBar(self.driver)
        
        util_obj = utillity.UtillityMethods(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        portal_name="V5 Personal Portal"
        folder_name="My Pages"
        expected_pages_list=["Page 1", "Page 2", "Page 3", "+"]
        expected_folders_list=["My Pages"]
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 20)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        
        """
        Step 3: Right click on 'V5 Personal Portal' > Run.
        """
        main_page_obj.right_click_folder_item_and_select_menu(portal_name, 'Run')
        
        """
        Step 3.1. Verify you see a side bar with My Pages and a + sign under it.
        """
        util_obj.switch_to_window(1)
        
        """
        Step 4. Click on My Pages > click + sign > choose 'Grid2-1' template
        """
        designer_portal_obj.click_on_plus_icon_under_the_folder_in_left_sidebar(folder_name)
        
        util_obj.synchronize_with_number_of_element(" .ibx-dialog-content .np-list .np-item", 4, 30)
        designer_portal_obj.select_new_page_template('Grid 2-1')
        
        """
        Step 5.1. Click + sign > choose 'Grid 3-3-3' template. 
        """
        refresh_btn="div[class*='ibx-label-glyph'][class*='ibx-label-icon'][class*='fa fa-refresh']"
        util_obj.synchronize_with_number_of_element(refresh_btn, 1, 20)
        
        designer_portal_obj.click_on_plus_icon_under_the_folder_in_left_sidebar(folder_name)
        util_obj.synchronize_with_number_of_element(" .ibx-dialog-content .np-list .np-item", 4, 30)
        designer_portal_obj.select_new_page_template('Grid 3-3-3')
        
        """
        Step 6. Click +sign > choose 'Grid 4-2-1' template.
        Step 6.1. Verify that the personal pages(Page 1,2 and 3) are appears at the end of the list
        """
        refresh_btn="div[class*='ibx-label-glyph'][class*='ibx-label-icon'][class*='fa fa-refresh']"
        util_obj.synchronize_with_number_of_element(refresh_btn, 2, 20)
        designer_portal_obj.click_on_plus_icon_under_the_folder_in_left_sidebar(folder_name)
        
        util_obj.synchronize_with_number_of_element(" .ibx-dialog-content .np-list .np-item", 4, 30)
        designer_portal_obj.select_new_page_template('Grid 4-2-1')
        
        refresh_btn="div[class*='ibx-label-glyph'][class*='ibx-label-icon'][class*='fa fa-refresh']"
        util_obj.synchronize_with_number_of_element(refresh_btn, 3, 20)
        
        portal_sidebar_obj.verify_folders(expected_folders_list, 'Step 6.1. Verify folders in sidebar', 'asin')
        portal_sidebar_obj.verify_pages_in_folder(folder_name, expected_pages_list, 'Step 6.1. Verify pages inside folder', 'asin')        
        
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