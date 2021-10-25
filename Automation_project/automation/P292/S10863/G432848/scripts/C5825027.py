'''
Created on April 17, 2019

@author: Vishnu Priya\Samuel

Test Case = http://172.19.2.180/testrail/index.php?/cases/view/5825027
TestCase Name = Verify share icon appears for report in content area
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C5825027_TestClass(BaseTestCase):

    def test_C5825027(self):
        
        """
        TESTCASE OBJECTS
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        TESTCASE VARIABLES
        """
        fex_name = 'report1'
        pop_top_css = ".pop-top"
        workspaces = "Workspaces"
        repository_folder = workspaces+'->P292_S10863_G193429'
        
        """
        Step 1: Sign in to WebFOCUS as Developer user
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
        
        """
        Step 2: Click on Content view from the sidebar
        """ 
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(locator_obj.REPOSITORY_TREE_CSS,1, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 3: Expand the domain from the tree and click on 'P292_S10863_G193429'
        """  
        main_page_obj.expand_repository_folder(repository_folder)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, 'My Content', main_page_obj.home_page_medium_timesleep)
        
        """
        Step 4: Click on My Content folder from the resource tree> Click on report1
        Verify share icon appear for report1 in content area.
        """
        main_page_obj.expand_repository_folder(repository_folder+'->'+'My Content')
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, fex_name, main_page_obj.home_page_medium_timesleep)
        main_page_obj.verify_item_icon_in_content_area('report1', 'share', '4', 'Pastel_Green')
        main_page_obj.right_click_folder_item_and_select_menu(fex_name, 'Unshare')
        util_obj.synchronize_until_element_disappear(pop_top_css, main_page_obj.home_page_medium_timesleep)
        
        """
        Step 5: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()