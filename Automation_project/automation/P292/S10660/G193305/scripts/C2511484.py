'''
Created on Oct 23, 2018

@author: Nasir

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660/&group_by=cases:section_id&group_id=193305
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2511484
TestCase Name = Verify that chosen and expanded is remembered
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators
from common.lib.global_variables import Global_variables

class C2511484_TestClass(BaseTestCase):

    def test_C2511484(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 190
        selected_folder = "div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected"
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        main_locator=wf_mainpage_locators.WfMainPageLocators
        
        """    1. Sign into WebFOCUS Home Page as Developer User.    """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.wait_for_page_loads(20)
        utillobj.synchronize_with_visble_text(main_locator.CONTENT_CSS, "Content", 60)
        
        """    2. From Domain,select and expand 'P292_S10660' domain > expand 'My Content' folder.    """
        wfmain_obj.expand_repository_folder('P292_S10660->My Content')
        
        """    3. In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User.    """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mridadv', 'mrpassadv')
        utillobj.synchronize_with_number_of_element(main_locator.CONTENT_ICON_CSS, 1, 190)
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(main_locator.REPOSITORY_TREE_CSS, 1, Global_variables.mediumwait)
#         wfmain_obj.verify_repository_folder_icon_plus_minus('P292_S10660', 'expand', "Step 03: Verify that the Resource Tree is in full view", index=0)
        
        """    4. In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User.    """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_number_of_element(selected_folder, 1, long_wait)
        wfmain_obj.verify_repository_folder_icon_plus_minus('P292_S10660', 'collapse', "Step 04: Verify that the 'P292_S10660' domain are still expanded", index=0)
        wfmain_obj.verify_repository_folder_icon_plus_minus('My Content', 'collapse', "Step 04: Verify that the 'My Content' folders are still expanded", index=0)
        
        """    5. Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)    """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(".toolbar", "Workspaces", 60)
        wfmain_obj.click_repository_folder("Workspaces")
        
        """    6. In the banner link, click on the top right username > Click Sign Out.    """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        