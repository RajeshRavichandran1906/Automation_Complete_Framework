'''
Created on Nov 14, 2018

@author: KK14897

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/19901&group_by=cases:section_id&group_id=520454&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/6779798
TestCase Name = Verify share icon appears for the shared content (personal pages) in the content area 
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.lib.global_variables import Global_variables

class C6779798_TestClass(BaseTestCase):

    def test_C6779798(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        folder_name_path="Domains->P292_S19901_G520454"
        content_css='div[class="ibx-label-glyph ibx-label-icon fa fa-bar-chart"]'
        crumb_css='div[class*="crumb-box ibx-widget ibx-flexbox"]'
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developer User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(content_css, '1', Global_variables.longwait)

        """
        Step 2: Expand the domain from the tree and click on 'P292_S19901_G520454'.
        """
        main_page_obj.expand_repository_folder(folder_name_path) 
        util_obj.synchronize_with_number_of_element(crumb_css, '1', Global_variables.longwait)
        
        """
        Step 3: Double click on 'V5 Portal Share' from the content area
        """
        main_page_obj.double_click_folder_item_and_select_menu('V5 Portal Share')
        time.sleep(Global_variables.longwait)
        
        """
        Step 4: Double click on 'My Pages' folder
        """
        main_page_obj.double_click_folder_item_and_select_menu('My Pages')
        time.sleep(Global_variables.longwait)
        util_obj.synchronize_with_number_of_element("span[class*='ibx-label-overlay home-item-overlay fa fa-share-alt']", 1, 90)
        """
        Step 5: Double click on 'My Content' folder
        """
        main_page_obj.double_click_folder_item_and_select_menu('My Content')
        util_obj.synchronize_with_number_of_element("span[class*='ibx-label-overlay home-item-overlay fa fa-share-alt']", 1, 90)
        time.sleep(Global_variables.longwait)
        """
        Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == "__main__":
    unittest.main()