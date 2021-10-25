'''
Created on December 18, 2018

@author: varun
Testcase Name : Portal Creation using Navigation 3
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262155
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import base
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.wftools.designer_portal import Portal

class C8262155_TestClass(BaseTestCase):
    
    def test_C8262155(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        base_obj = base.BasePage(self.driver)
        portal_obj = Portal(self.driver)
        
        """
        Test case CSS
        """
        dialog_box_css = ".ibx-dialog-main-box .ibx-dialog-title-box"
        
        """
        Test case variables
        """
        portal_name = 'V5 Personal Portal_Nav-3'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User.
        Click on Content tree from side bar.
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        util_obj.synchronize_with_number_of_element(locator_obj.CONTENT_CSS, 1, base_obj.home_page_medium_timesleep)
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1,base_obj.home_page_medium_timesleep)
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G517783 folder. 
        """
        main_page_obj.expand_repository_folder('P292_S19901->G517783')
        
        """
        Step 3: Click on Designer category button > Click on Portal action bar.
        Verify New Portal dialog box opens.
        """
        main_page_obj.select_action_bar_tab('Designer')
        main_page_obj.select_action_bar_tabs_option('Portal')
        util_obj.synchronize_with_number_of_element(dialog_box_css, 1 , base_obj.home_page_medium_timesleep)
        portal_obj.verify_portal_dialog_open_or_close('open', "Step 3.1: Verify Portal Dialog box opens")
        
        """
        Step 4: Enter Title 'V5 Personal Portal_Nav-3' and Choose Navigation 3
        """
        portal_obj.title_textbox_in_new_or_edit_portal_dialog(portal_name)
        portal_obj.two_level_top_navigation_radiobutton_in_new_or_edit_portal_dialog(select_type='check')
        
        """
        Step 5: Click Create.
        Verify 'V5 Personal Portal_Nav-3' appears as a folder and is not published
        """
        portal_obj.create_button_inside_new_or_edit_portal_dialog(select_button="True")
        main_page_obj.verify_folders_in_grid_view([portal_name],'asin', 'Step 5.1: Verify the Portal is available in content area')
        main_page_obj.verify_content_area_folder_publish_or_unpublish(portal_name,'unpublish','Step 5.2: Verify Portal is unpublished')
        
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()