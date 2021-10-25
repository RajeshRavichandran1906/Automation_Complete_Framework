'''
Created on December 17, 2018

@author:Vpriya

Testcase Name : Portal Creation using Navigation 2
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8262134
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.global_variables import Global_variables

class C8262134_TestClass(BaseTestCase):
    
    def test_C8262134(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        designer_obj = designer_portal.Portal(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        dialog_css = ".ibx-dialog-content"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G514402 folder.
        """
        
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G514402')
        
        """
        Step 3: Click on Designer category button > Click on Portal action bar.
        Verify New Portal dialog box opens.
        """
        main_page_obj.select_action_bar_tab('Designer')
        designer_obj.delete_portal_if_exists("V5 Personal Portal_Nav-2")
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_number_of_element(dialog_css,1, 30)
        designer_obj.verify_portal_dialog_open_or_close('open', 'Step 3.1: Verify portal dialog box open')
        
        """
        Step 4: Enter Title 'V5 Personal Portal_Nav-2' 
        Enter Title 'V5 Personal Portal_Nav-2' and select "Three-level" Navigation.
        """
        designer_obj.title_textbox_in_new_or_edit_portal_dialog('V5 Personal Portal_Nav-2')
        designer_obj.three_level_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check',step_number='4.1')
        
        """
        Step 5: Click Create.
        Verify 'V5 Personal Portal_Nav-2' appears as a folder and is not published
        """
        designer_obj.create_button_inside_new_or_edit_portal_dialog(select_button='True')
        main_page_obj.verify_folders_in_grid_view(['V5 Personal Portal_Nav-2'], comparision_type='asin', msg='Step 5.1: V5 folder appears')
        main_page_obj.verify_content_area_folder_publish_or_unpublish('V5 Personal Portal_Nav-2', 'unpublish', msg='Step 5.2: Verify Portal unpublished')
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()