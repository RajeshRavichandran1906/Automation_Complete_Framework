"""-------------------------------------------------------------------------------------------
Created on October 25, 2018
@author: Prabhakaran

Test Case Link  =  http://lnxtestrail.ibi.com/testrail/index.php?/cases/view/6986644
Test Case Title =  Test expand menu using Developers
-----------------------------------------------------------------------------------------------"""

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib.utillity import UtillityMethods

class C6986644_TestClass(BaseTestCase):

    def test_C6986644(self):
        
        """
            CLASS OBJECTS 
        """
        wf_login = login.Login(self.driver)
        wf_home = wf_mainpage.Wf_Mainpage(self.driver)
        utils = UtillityMethods(self.driver)
        
        """
            COMMON TEST CASE VARIABLES 
        """
        
        EXPECTED_BREAD_CRUMB = 'Domains->P292_S19901->G513445->Portal for Context Menu Testing'
        ITEM_NAME = 'Portal for Context Menu Testing'
        FOLDER_PATH = 'P292_S19901->G513445'
        expected_options_list=['Folder', 'Workbook', 'Page','Shortcut']
        
        
        """
            STEP 01 : Sign into WebFOCUS Home Page as Developers User
        """
        wf_login.invoke_home_page('mriddev', 'mrpassdev')
        utils.synchronize_with_visble_text("div[title^='Content']", 'Content', 80)
        
        """
            STEP 02 : Click on a Content tree from side bar>click on Domains from the resource tree. 
        """
        wf_home.select_content_from_sidebar()
        utils.synchronize_with_visble_text("div[title='Domains']", 'Domains', 5)
        
        """
            STEP 03 : If not expand Domains > 'P292_S19901' > 'G513445' folder from the resource tree
            STEP 04 : Right click on 'Portal for Context Menu Testing' > click Expand from the Resource Tree
            Verify that 'Portal for Context Menu Testing' folder gets expanded from the Resource tree
        """
        wf_home.expand_repository_folder(FOLDER_PATH)
        wf_home.select_repository_folder_context_menu('Portal for Context Menu Testing','Expand',verification_state='collapse')
        wf_home.verify_repository_folder_icon_plus_minus(ITEM_NAME, 'collapse', 'Step 04.01 : Verify minus icon shows after expand portal for Context Menu Testing')
        
        """
            STEP 05 : Verify that 'Portal for Context Menu Testing' folder gets expanded from the Resource tree
            Verify based on the breadcrumb user inside the 'Portal for Context Menu Testing' folder and breadcrumb as 'Domains > P292_S19901 > G513445 > Portal for Context Menu Testing'
        """ 
        wf_home.verify_crumb_box(EXPECTED_BREAD_CRUMB, 'Step 05.01 : Verify bread crumb path')
        wf_home.verify_action_bar_tab_all_options(expected_options_list,'Step 4.4:')

        """
            STEP 06 : In the banner link, click on the top right username > Click Sign Out.
        """       
        wf_home.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        