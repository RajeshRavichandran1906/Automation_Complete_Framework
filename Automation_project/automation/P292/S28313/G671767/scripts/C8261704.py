'''
Created on November 13, 2018

@author: Robert
Testcase Name : Verify share icon removed for personal pages after deleting the shared users
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8261704
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login,wf_mainpage
from common.lib import utillity, javascript

class C8261704_TestClass(BaseTestCase):
    
    def test_C8261704(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        js_obj=javascript.JavaScript(self.driver)
        folder_name_path="P292_S19901_G520454->V5 Portal Share->My Pages"
        
        """
        Step 1: Sign in to WebFOCUS as Developer user
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Expand Domain > 'P292_S19901_G520454' domain > 'V5 Portal Share' > 'My Pages' under resource tree
        """
        main_page_obj.expand_repository_folder(folder_name_path)
        util_obj.wait_for_page_loads(10)
        
        """
        Step 2.1. Verify Sharing icon still appears for 'My Content' folder in the content area
        """
        share_css="span[class*='fa fa-share-alt']"
        util_obj.synchronize_with_number_of_element(share_css, 1, 30)
        util_obj.verify_object_visible(share_css, True, 'Step 2.1. Verify Sharing icon')
        share_css_obj=util_obj.validate_and_get_webdriver_object(share_css, 'Share_icon')
        actual_icon=js_obj.get_element_before_style_properties(share_css_obj, 'content').replace('"','').encode()
        print ("actual icon", actual_icon)
        expected_icon = "\uf1e0".encode()
        print ("expected icon",expected_icon)
        
        util_obj.asequal(actual_icon,expected_icon,'Step 2.1. Verify Sharing icon is visible')
        
        """
        Step 3: Double click on 'My Content' folder
        Step 3.1. Verify added 'Page 1' personal page appears without sharing icon in the content area
        """
        main_page_obj.right_click_folder_item_and_select_menu('My Content',  click_option='double_click')
        util_obj.wait_for_page_loads(10)
        content_css="img[src*='pgx.svg']"
        util_obj.synchronize_with_number_of_element(content_css, 1, 30)
        
        util_obj.verify_element_visiblty(element_css=share_css, visible=False, msg='Step 3.1. Verify Page1 appears without sharing icon')
        
        """
        Step 4: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()
    
        