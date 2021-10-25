'''
Created on Nov 26, 2018

@author: BM13368
Testcase ID : http://172.19.2.180/testrail/index.php?/cases/view/8262121
Testcase Name : Adding folders in V5 Portal as developer user
'''
import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login
from common.wftools import wf_mainpage
from common.lib import utillity

class C8262121_TestClass(BaseTestCase):
    
    def test_C8262121(self):
        """
        CLASS OBJECTS
        """
        login_o = login.Login(self.driver)
        main_page_o = wf_mainpage.Wf_Mainpage(self.driver)
        util_o = utillity.UtillityMethods(self.driver)
        
        """
        TESTCASE VARIBALE
        """
        folder_path='Domains->P292_S19901->G513510->V5 Personal Portal'
        folder_name1='Folder 1'
        folder_name2='Folder 2'
        folder_name3='Folder 3'
        folder_css=".create-new-folder"
        
        """
        CSS
        """
        folders_css="[data-ibxp-text='Folders']"
        crumb_css = "div[data-ibx-type=\"breadCrumbTrail\"]"
        
        """
            Step 1: Sign into WebFOCUS Home Page as Developers User.
        """
        login_o.invoke_home_page('mriddev', 'mrpassdev')
 
        """
            Step 2: Expand 'P292_S19901' domain > G513510 folder > click on V5 Personal Portal.
        """
        main_page_o.select_content_from_sidebar()
        util_o.synchronize_with_number_of_element(crumb_css, 1, 45)
        main_page_o.expand_repository_folder(folder_path)
        
        
        """
            Step 3: Click on folder action bar and give "Folder 1" as title > click OK.
        """
        main_page_o.select_action_bar_tabs_option('Folder')
#         main_page_o.select_ribbon_button('Folder',repository_section_area='web content')
        util_o.synchronize_with_number_of_element(folder_css, 1, 20)
        main_page_o.create_new_folder(folder_name1)
        util_o.synchronize_with_visble_text(folders_css, 'Folders', 25)
        """
            Step 4: Click on folder action bar and give "Folder 2" as title > click OK.
        """
        main_page_o.select_action_bar_tabs_option('Folder')
#         main_page_o.select_ribbon_button('Folder',repository_section_area='web content')
        util_o.synchronize_with_number_of_element(folder_css, 1, 20)
        main_page_o.create_new_folder(folder_name2)
        util_o.synchronize_with_visble_text(folders_css, 'Folders', 25)
        
        
        """
            Step 5: Click on folder action bar and give "Folder 3" as title > click OK.
            Verify Folder 1,2 and 3 are shown in the content area.
        """
        main_page_o.select_action_bar_tabs_option('Folder')
#         main_page_o.select_ribbon_button('Folder',repository_section_area='web content')
        util_o.synchronize_with_number_of_element(folder_css, 1, 20)
        main_page_o.create_new_folder(folder_name3)
        util_o.synchronize_with_visble_text(folders_css, 'Folders', 25)
        
        """
            Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        main_page_o.signout_from_username_dropdown_menu()


if __name__ == "__main__":
    unittest.main()