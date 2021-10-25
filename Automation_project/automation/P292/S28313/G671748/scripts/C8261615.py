'''
Created on January 08, 2019

@author: KK14897
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261615
Testcase Name : Upload zip file
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C8261615_TestClass(BaseTestCase):


    def test_C8261615(self):
        """
        TESTCASE_OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        TESTCASE VARIABLES
        """
        domain_folder='Retail Samples'
        
        
        """
        Step 1: Sign into WebFOCUS Home Page as Admin User
        """
        login_obj.invoke_home_page('mrid','mrpassbas')
        
        """
        Step 2: Click Content View from the side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
        main_page_obj.select_option_from_crumb_box('Domains')
        
        """
        Step 3: Click on Retail Samples from the resource tree
        """
        main_page_obj.click_repository_folder(domain_folder)
        
        """
        Step 4:Click on 'Other' category
        """
        main_page_obj.select_action_bar_tab('Other')
        
        """
        Step 5 : Click on 'Upload File' action bar
        """
        main_page_obj.select_action_bar_tabs_option('Upload File')
        
        """
        Step 6 : Select 'Home_Thumbnail.zip' from the location mentioned in the preconditions and click on Open button
        Verify that the Upload completed prompt is displayed
        """
        main_page_obj.upload_file_using_action_bar(["Home_Thumbnail.zip"])
        main_page_obj.verify_upload_message("Home_Thumbnail.zip", "Home_Thumbnail.zip Upload completed", "Step 06: Verify upload message")
        
        """
        Step 7 : Close the Upload completed prompt
        Verify that the file 'Home_Thumbnail.zip' have been uploaded
        """
        main_page_obj.click_button_on_popup_dialog("Close")
        main_page_obj.verify_items_in_grid_view(['Home_Thumbnail'], 'asin', 'Step 07 : Verify that the file Home_Thumbnail.zip have been uploaded')
        
        """
        Step 8 : Right click on 'Home_Thumbnail.zip' > delete > Ok
        Verify that the file 'Home_Thumbnail.zip' is removed from content area
        """
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, 190)
        main_page_obj.right_click_folder_item_and_select_menu("Home_Thumbnail", "Delete")
        util_obj.synchronize_with_number_of_element("[class*='ibx-title-bar-caption']", 1, 20)
        main_page_obj.click_button_on_popup_dialog("OK")
        main_page_obj.verify_items_in_grid_view(['Home_Thumbnail'], 'asnotin', 'Step 08.2 : Verify File deleted')
        
        """
        Step 9: In the banner link, click on the top right username > Click Sign Out
        """
        main_page_obj.signout_from_username_dropdown_menu()

if __name__ == "__main__":
    unittest.main()