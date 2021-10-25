'''
Created on July 20, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660/&group_by=cases:section_id&group_id=193305
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2511458
TestCase Name = Verify that Collapsed Resource Tree is remembered
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2511458_TestClass(BaseTestCase):

    def test_C2511458(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 190
        folders_css="[data-ibxp-text*='Folders']"
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        content_list=['Content', 'Portals', 'Favorites', 'Mobile Favorites']
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        
        """ Step 1: Sign into WebFOCUS Home Page as Developer User.
                    Verify by default Content View is selected.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        wfmain_obj.verify_left_panel(content_list, "Step 1: Verify Side bar(left panel) options")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list, "Step 1.1: Verify content title label folders", label_type='folders')
        
        """Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """ Step 3: Click on Collapse resources tree icon.
                    Verify that the Resource Tree is collapsed.
        """
        wfmain_obj.collapse_resource_tree()
        wfmain_obj.verify_expand_resource_tree(True, 'Step 2: Verify that the Resource Tree is collapsed.')
        
        """ Step 4: In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User.
                    Verify that the Resource Tree is in full view.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mridadv', 'mrpassadv')
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.verify_collapse_resource_tree(True, 'Step 3: Verify that the Resource Tree is collapsed.')
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User.
                    Verify that the Resource Tree is collapsed.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.verify_expand_resource_tree(True, 'Step 4: Verify that the Resource Tree is collapsed.')
        
        """ Step 6: Revert back the Home Page by its default state.
        """
        wfmain_obj.expand_resource_tree()
        
        """ Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        