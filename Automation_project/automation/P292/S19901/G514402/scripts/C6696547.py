'''
Created on December 18, 2018

@author: KK14897
Testcase Name : Add Content to page with no requirements parameters as basic user
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6696547
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity
from common.lib import core_utility
from common.locators.portal_designer import Vfive_Designer

class C6696547_TestClass(BaseTestCase):
    
    def test_C6696547(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        core_util_obj = core_utility.CoreUtillityMethods(self.driver)
        portal_obj = designer_portal.Two_Level_Side(self.driver)
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        expected_portal_title = 'V5 Personal Portal_Nav-2'
        portal_title_css = ".pvd-portal-title .ibx-label-text"
        page_container_css = ".pd-container-title"
        resource_box_css = ".open-dialog-resources .ibx-title-bar-caption .ibx-label-text"
        resource_text = 'Select Item'
        container_css = ".pd-container-title .ibx-label-text"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Basic User.
        """
        login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G514402')
        
        """
        Step 3: Run the portal by double click on 'V5 Personal Portal_Nav-2'.
        Verify 'V5 Personal Portal_Nav-2' opens in a new tab.
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal_Nav-2',click_option='double_click')
        core_util_obj.switch_to_new_window()
        util_obj.synchronize_with_visble_text(portal_title_css, expected_portal_title,45)
        observed_title = util_obj.validate_and_get_webdriver_object(portal_title_css, "Title css").text
        util_obj.asequal(expected_portal_title,observed_title,"Step 3.1: Verify the portal opens in a new window")
        
        """
        Step 4: Click the + sign inside the Panel1 to add the content
        Verify Select Item browse window appears.
        """
        util_obj.synchronize_with_number_of_element(page_container_css, 7,60)
        portal_obj.click_on_panel_add_content_button_in_container('Panel 1')
        util_obj.synchronize_with_visble_text(resource_box_css,resource_text,50)
        dialog_box_element = util_obj.validate_and_get_webdriver_object(resource_box_css, "dialog_title").text
        util_obj.asequal(dialog_box_element,resource_text,"Step 4.1: Verify selection window opens")
        
        """
        Step 5: Double click on 'Retail Samples' > 'Portals' > 'Small Widgets' > 'Category Sales'.
        Verify the content appears and NO modal window as the controls are not required and title changed as 'Category Sales' for Panel 1
        """
        portal_obj.select_repository_file_using_add_content_using_crumb_in_panel_container('Domain','Retail Samples->Portal->Small Widgets->Category Sales')
        parent_obj = util_obj.validate_and_get_webdriver_object(Vfive_Designer.current_page, 'current page')
        util_obj.synchronize_with_visble_text_within_parent_object(parent_obj,container_css, 'Category Sales', 50)
        portal_obj.verify_specific_containers_title(['Category Sales'], 'Step 5.1: Verify Category Sales is Present')
        
        """
        Step 6: Close the 'V5 Personal Portal_Nav-2' run window.
        """
        core_util_obj.switch_to_previous_window()
        
        """
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()