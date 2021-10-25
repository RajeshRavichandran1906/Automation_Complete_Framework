
'''
Created on Nov 26, 2018

@author: Magesh

Testcase Name : Edit the Page title
Testcase ID : http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/8262119
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity, core_utility

class C8262119_TestClass(BaseTestCase):
    
    def test_C8262119(self):
        
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        portal_obj = designer_portal.Two_Level_Side(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        coreutil_obj = core_utility.CoreUtillityMethods(self.driver)
        domains_css = ".toolbar .crumb-box"
        
        """
        Step 1: Sign into WebFOCUS Home Page as Developers User
        """
        login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """
        Step 2: Expand 'P292_S19901' domain > click on G513510 folder.
        """
        main_page_obj.select_content_from_sidebar()
        util_obj.synchronize_with_number_of_element(domains_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510')
        util_obj.wait_for_page_loads(10, pause_time=4)
         
        """
        Step 3: Right click on 'V5 Personal Portal' > Run. 
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal', 'Run')
        
        """
        Step 4: Double click on 'Page 1' under My Pages. 
        Step 5: Type title as 'Content testing' and hit enter key.
        """
        coreutil_obj.switch_to_new_window()
        util_obj.wait_for_page_loads(25, pause_time=4)
        page_heading=".pvd-container"
        util_obj.synchronize_with_visble_text(page_heading, "Page Heading", 80, pause_time=3)
        portal_obj.rename_page_under_the_folder_in_left_sidebar('My Pages', 'Page 1', 'Content testing')
        
        """
        Verify the title has been changed. 
        """
        portal_obj.verify_pages_under_the_folder_in_left_sidebar('My Pages', expected_pages_list=['Content testing', '+'], msg='Step 5.a: Verify the title has been changed.')
        
        """
        Step 6: Close the 'V5 Personal Portal' run window. 
        Step 7: In the banner link, click on the top right username > Click Sign Out.
        """
        coreutil_obj.switch_to_previous_window()
        main_page_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main() 