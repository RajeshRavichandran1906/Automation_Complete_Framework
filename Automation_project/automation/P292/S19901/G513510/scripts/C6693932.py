'''
Created on November 26, 2018

@author: varun
Testcase Name : Portal Creation using Navigation 1
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6693932
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity

class C6693932_TestClass(BaseTestCase):
    
    def test_C6693932(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        designer_obj = designer_portal.Portal(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        dialog_css = ".ibx-dialog-content"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        
        """
        Step 3: Click on Designer category button > Click on Portal action bar.
        Verify New Portal dialog box opens.
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_number_of_element(dialog_css,1, 30)
        designer_obj.verify_portal_dialog_open_or_close('open', 'Step 3.1: Verify portal dialog box open')
        
        """
        Step 4: Enter Title 'V5 Personal Portal' 
        Verify that by default "Navigation 1" (Two-level side) is selected
        """
        designer_obj.title_textbox_in_new_or_edit_portal_dialog('V5 Personal Portal')
        designer_obj.two_level_side_navigation_radiobutton_in_new_or_edit_portal_dialog(verify_navigation='check',step_number='4.1')
        
        """
        Step 5: Click Create.
        Verify 'V5 Personal Portal' appears as a folder and is not published
        """
        designer_obj.create_button_inside_new_or_edit_portal_dialog(select_button='True')
        main_page_obj.verify_folders_in_grid_view(['V5 Personal Portal'], comparision_type='asin', msg='Step 5.1: V5 folder appears')
        main_page_obj.verify_content_area_folder_publish_or_unpublish('V5 Personal Portal', 'unpublish', msg='Step 5.2: Verify Portal unpublished')
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()