'''
Created on December 6, 2018

@author: varun
Testcase Name : Verify base pages are reflects in run mode as developer user 
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6742427
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity
from common.lib import core_utility

class C6742427_TestClass(BaseTestCase):
    
    def test_C6742427(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Two_Level_Side(self.driver)
        canvas_obj = designer_portal.Canvas(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        expected_portal_title = 'V5 Personal Portal'
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Expand 'P292_S19901' domain > G513510 folder
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        
        """
        Step 3: Right click on 'V5 Personal Portal' > Run.
        Verify Base Page 1, Base Page 2 and Base Page 3 are appears in the side bar.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal','Run')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, expected_portal_title,45)
        portal_obj.verify_page_name_in_from_top_folder('Base Page 1', 'Step 3.1: Verify Base Page 1 is present')
        portal_obj.verify_page_name_in_from_top_folder('Base Page 2', 'Step 3.2: Verify Base Page 2 is present')
        portal_obj.verify_page_name_in_from_top_folder('Base Page 3', 'Step 3.3: Verify Base Page 3 is present')
        
        """
        Step 4: Click on Base Page 1.
        Verify Panel 1 (panel container) with a + sign inside on them.
        """
        portal_obj.select_page_from_top_folder('Base Page 1')
        portal_obj.verify_all_containers_title(['Panel 1'], 'Step 4.1: Verify Panel 1 is available')
        canvas_obj.verify_panel_add_content_displayed_in_container('Panel 1', 'Step 4.2: Verify Plus icon in Panel 1')
        
        """
        Step 5: Click on Base Page 2.
        Verify Panel 1 (tab container) with a + sign inside on them.
        """
        portal_obj.select_page_from_top_folder('Base Page 2')
        portal_obj.verify_all_containers_title(['Panel 1'], 'Step 5.1: Verify Panel 1 is available')
        canvas_obj.verify_tab_list_in_container('Panel 1', ['Tab 1'], 'Step 5.2: Verify Tab 1 is Present')
        canvas_obj.verify_panel_add_content_displayed_in_container('Panel 1', 'Step 5.3: Verify Plus icon in Panel 1')
        
        """
        Step 6: Click on Base Page 3
        Verify Panel 1 (carousel container) with a + sign inside on them.
        """
        portal_obj.select_page_from_top_folder('Base Page 3')
        portal_obj.verify_all_containers_title(['Panel 1'], 'Step 6.1: Verify Panel 1 is available')
        canvas_obj.verify_number_of_slide_in_carousel_panel_container('Panel 1', 1, 'Step 6.2: Verify Carousal slide is present')
        canvas_obj.verify_panel_add_content_displayed_in_container('Panel 1', 'Step 6.3: Verify Plus icon in Panel 1')
        
        """
        Step 7: Close the 'V5 Personal Portal' run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()