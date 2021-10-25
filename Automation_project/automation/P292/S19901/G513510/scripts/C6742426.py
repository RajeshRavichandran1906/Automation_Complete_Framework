'''
Created on Nov 26, 2018

@author: KK14897
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/6742426
Testcase Name : Verify pages inside the folders are reflects in run mode as developer user
'''
import unittest,time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.wftools.designer_portal import Two_Level_Side
from common.lib import utillity
from common.lib import core_utility

class C6742426_TestClass(BaseTestCase):
    
    def test_C6742426(self):
        """
        CLASS OBJECTS
        """
        login_o = login.Login(self.driver)
        main_page_o = wf_mainpage.Wf_Mainpage(self.driver)
        util_o = utillity.UtillityMethods(self.driver)
        two_level_o=Two_Level_Side(self.driver)
        core_utill_o=core_utility.CoreUtillityMethods(self.driver)
        
        """
        TESTCASE VARIBALE
        """
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        folder_path='Domains->P292_S19901->G513510->V5 Personal Portal'
        expected_folders_list=['Folder 1','Folder 2','Folder 3']
        
        """
            Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_o.invoke_home_page('mriddev', 'mrpassdev')
 
        """
            Step 2: Expand 'P292_S19901' domain > G513510 folder.
        """
        main_page_o.select_content_from_sidebar()
        util_o.synchronize_with_number_of_element(crumb_css, 1, 45)
        
        """
            Step 3: Right click on 'V5 Personal Portal' > Run.
        """
        main_page_o.select_repository_folder_context_menu(folder_path, 'Run')
        
        """
            Verify Folder 1 , Folder 2 and Folder 3 are appears in the side bar.
        """
        core_utill_o.switch_to_new_window()
        two_level_o.verify_specific_folders_in_left_sidebar(expected_folders_list, "Step 3:01: Verify Folder 1,Folder 2 and Fodler 3 are available in side bar")
        
        """
            Step 4: Click drop down on Folder 1 in the navigation bar.
        """
        #portal_sidebar_obj.expand_or_collapse_folder("Folder 3", "Expand")
        #two_level_o.expand_folder_in_left_sidebar("Folder 1")
        #two_level_o.collapse_folder_in_left_sidebar("Folder 1")
        time.sleep(5)
        expected_pages_list_1=['Test page 1.1','Test page 1.2']
        two_level_o.verify_specific_pages_under_the_folder_in_left_sidebar("Folder 1", expected_pages_list_1, msg='step 04: verify pages in Folder 1')
        
        """
            Step 5: Click drop down on Folder 2 in the navigation bar.
        """
        two_level_o.expand_folder_in_left_sidebar("Folder 2")
        expected_pages_list_2=['Test page 2.1','Test page 2.2']
        two_level_o.verify_specific_pages_under_the_folder_in_left_sidebar("Folder 2", expected_pages_list_2, msg='step 05: verify pages in Folder 2')
        
        """
            Step 6: Click drop down on Folder 3 in the navigation bar.
        """
        two_level_o.expand_folder_in_left_sidebar("Folder 3")
        expected_pages_list_3=['Test page 3.1','Test page 3.2']
        two_level_o.verify_specific_pages_under_the_folder_in_left_sidebar("Folder 3", expected_pages_list_3, msg='step 06: verify pages in Folder 3')
        """
            Step 7: Close the 'V5 Personal Portal' run window.
        """
        core_utill_o.switch_to_previous_window()
        
        """
            Step 8 : In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_o.signout_from_username_dropdown_menu()

if __name__ == "__main__":
    unittest.main()