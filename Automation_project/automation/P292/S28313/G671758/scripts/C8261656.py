'''
Created on March 25,2019

@author: AA14564
Testcase Name : Preliminary Testing for admin/dev
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261656
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C8261656_TestClass(BaseTestCase):
    
    def test_C8261656(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        locator_obj = wf_mainpage_locators.WfMainPageLocators()
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        
        """
        Test case variables
        """
        expected_domain = "V5 Domain Testing"
        domains_text = 'Domains'
        expected_portal = ['V5 portal Nav 1']
        expected_msg = 'Step {0}: Verify V5 portal Nav 1 is available.'
        section_type_ = 'portal'
        
        """
        Step 1: Login WF as wfpenadm1/owasp!@630
        """
        login_obj.invoke_home_page('mrid', 'mrpass')
         
        """ Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(domains_text)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
         
        """ Step 3: Expand 'V5 Domain Testing' domain
                    Verify 'V5 portal Nav 1' is available and the icon appears as below
        """
        main_page_obj.expand_repository_folder(expected_domain)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal[0], main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view(expected_portal, 'asin', expected_msg.format('3'))
        main_page_obj.verify_item_icon_in_content_area(expected_portal[0], section_type_, '3.1')
         
        """ Step 4: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
         
        """ Step 5: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
         
        """ Step 6: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(domains_text)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
         
        """ Step 7: Expand 'V5 Domain Testing' domain
                    Verify 'V5 portal Nav 1' is available and the icon appears as below
        """
        main_page_obj.expand_repository_folder(expected_domain)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal[0], main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_folders_in_grid_view(expected_portal, 'asin', expected_msg.format('7'))
        main_page_obj.verify_item_icon_in_content_area(expected_portal[0], section_type_, '7.1')
         
        """ Step 8: Sign out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        """ Step 9: Login WF as wfpenadv1/owasp!@630
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        
        """ Step 10: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder(domains_text)
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        
        """ Step 11: Expand 'V5 Domain Testing' domain
                     Verify 'V5 portal Nav 1' is available and the icon appears as below
        """
        main_page_obj.expand_repository_folder(expected_domain)
        util_obj.synchronize_with_visble_text(locator_obj.content_area_css, expected_portal[0], main_page_obj.home_page_long_timesleep)
        main_page_obj.verify_items_in_grid_view(expected_portal, 'asin', expected_msg.format('11'))
        main_page_obj.verify_item_icon_in_content_area(expected_portal[0], section_type_, '11.1')
        
        """ Step 12: Sign out WF and close browser 
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()