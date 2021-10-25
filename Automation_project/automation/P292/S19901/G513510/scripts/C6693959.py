'''
Created on Nov 26, 2018

@author: Vpriya

Testcase Name : Delete a personal page
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6693959
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import wf_mainpage
from common.wftools import login
from common.wftools import designer_portal
from common.lib import utillity, core_utility


class C6693959_TestClass(BaseTestCase):
    
    def test_C6693959(self):
        """
        Test_case variables
        """
        login_obj = login.Login(self.driver)
        main_page_obj = wf_mainpage.Wf_Mainpage(self.driver)
        portal_obj = designer_portal.Two_Level_Side(self.driver)
        util_obj = utillity.UtillityMethods(self.driver)
        coreutil_obj = core_utility.CoreUtillityMethods(self.driver)
        domains_css = "div[title='Domains'] .ibx-label-text"
        
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
        
        """
        Step 3: Right click on 'V5 Personal Portal' > Run. 
        """
        main_page_obj.right_click_folder_item_and_select_menu('V5 Personal Portal', 'Run')
        
        """
        Step 4: Click delete icon on the top of the page heading.. 
        Verify delete warning dialog box displays.
        """
        coreutil_obj.switch_to_new_window()
        portal_obj.delete_page()
        portal_obj.verify_page_delete_dialog_is_displayed("Step 4:")
        portal_obj.verify_page_delete_dialog_message("Are you sure you want to delete 'Content testing' ?","Step 4.1")
        """
        Step 5: Click OK.
        Verify 'Content testing' page is deleted 
        """
        
        portal_obj.click_ok_button_in_page_delete_dialog()
        portal_obj.verify_pages_not_displayed_under_the_folder_in_left_sidebar('My Pages','Content testing','Step 5')
        
        
        """
        Step 6: Close the 'V5 Personal Portal' run window. 
        """
        coreutil_obj.switch_to_previous_window()
        
        """
        Step 7: If not expand 'P292_S19901' domain > G513510 > V5 Personal Portal > My Pages > My Content in tree.
        Verify 'Content testing' page is deleted.
        """
        util_obj.synchronize_with_number_of_element(domains_css, 1, 45)
        main_page_obj.expand_repository_folder('Domains->P292_S19901->G513510->V5 Personal Portal->My Pages->My Content')
        main_page_obj.expand_repository_folders_and_verify('Domains->P292_S19901->G513510->V5 Personal Portal->My Pages->My Content', ['Content testing'], "step 7:",comparion_type='asnotin')
        
        
        """
        Step 8: In the banner link, click on the top right username > Click Sign Out.
        """
        
        main_page_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main() 