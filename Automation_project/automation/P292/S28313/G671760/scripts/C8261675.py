'''
Created on March 28,2019

@author: varun
Testcase Name : Login advanced user which cannot see Page Testing Style
Testcase link : http://172.19.2.180/testrail/index.php?/cases/view/8261675
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.lib import utillity

class C8261675_TestClass(BaseTestCase):
    
    def test_C8261675(self):
        """
        Test_case objects
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        
        """
        Test case CSS
        """
        repository_css = "div[class='ibfs-tree']"
        
        """
        Step 1: Login WF as wfpendev1/owasp!@630
        """
        login_obj.invoke_home_page('mridadv', 'mrpassadv')
        
        """ 
        Step 2: Click on Content from side bar
        """
        main_page_obj.select_content_from_sidebar()
        
        """
        Step 3: Expand 'V5 Domain Testing';
        Right click on 'v5portal1-1' and select Run
        Verify portal appears as below
        Verify the page 'Page Testing Style' is not available
        """
        util_obj.synchronize_until_element_is_visible(repository_css, main_page_obj.home_page_medium_timesleep)
        main_page_obj.expand_repository_folder('Domains->V5 Domain Testing')
        util_obj.synchronize_with_number_of_element("div[data-ibxp-text=\"Items \"]", 1, main_page_obj.home_page_short_timesleep)
        main_page_obj.verify_items_in_grid_view(['Page Testing Style'], 'asnotin', "Step 3.1: Verify itme is not available")
        
        """
        Step 4: Sign Out WF
        """
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()