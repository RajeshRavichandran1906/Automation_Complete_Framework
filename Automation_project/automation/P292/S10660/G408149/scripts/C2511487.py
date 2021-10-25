'''
Created on May 9, 2019

@author: varun

Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2511487
TestCase Name = Verify that Collapsed Side Bar /Tree are remembered
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators.wf_mainpage_locators import WfMainPageLocators

class C2511487_TestClass(BaseTestCase):

    def test_C2511487(self):
        """
        Test case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Step 1: Sign into WebFOCUS as Developer user.
        Verify that the Content view is chosen at the start
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        main_page_obj.verify_left_panel(['Content'], msg='Step 1.1: Verify that content is selected', comparision_type='asin')
        
        """
        Step 2: Click the Collapse Side Bar icon
        Verify that the Sidebar get collapsed
        """
        main_page_obj.collapse_side_bar()
        main_page_obj.verify_left_panel(['Content'], msg='Step 2.1: Verify that content is not visible', default_selected='', comparision_type='asnotin')
        
        """
        Step 3: Sign out and sign back in as an adv user
        Verify that content is the one chosen and then side bar is in full view
        """
        main_page_obj.signout_from_username_dropdown_menu()
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_left_panel(['Content'], msg='Step 1.1: Verify that content is selected and sidebar is open', comparision_type='asin')
        
        """
        Step 4: Sign out and sign back in as the original user
        Verify that the side bar is collapsed
        """
        main_page_obj.signout_from_username_dropdown_menu()
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_left_panel(['Content'], msg='Step 4.1: Verify that side bar is collapsed', default_selected='', comparision_type='asnotin')
        
        """
        Step 5: Click the Collapse Resource Tree icon
        """
        main_page_obj.collapse_resource_tree()
        
        """
        Step 6: Sign out and sign back in as an adv user
        Verify that the Tree is in full view
        """
        main_page_obj.signout_from_username_dropdown_menu()
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        util_obj.verify_object_visible(".left-pane .ibfs-tree", True, "Step 6.1: Verify tree is visible")
        
        """
        Step 7: Sign out and sign back in as the original user
        Verify that the Tree and Side bar are collapsed
        """
        main_page_obj.signout_from_username_dropdown_menu()
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        util_obj.synchronize_with_number_of_element(WfMainPageLocators.CONTENT_ICON_CSS, 1, main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_left_panel(['Content'], msg='Step 7.1: Verify that side bar is collapsed', default_selected='', comparision_type='asnotin')
        util_obj.verify_object_visible(".left-pane .ibfs-tree", False, "Step 7.2: Verify tree is not visible")
        main_page_obj.expand_side_bar()
        
        """
        Step 8: In the banner link, click on the top right username > Click Signout.
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        