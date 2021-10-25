'''
Created on July 25, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660/&group_by=cases:section_id&group_id=193304
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2511457
TestCase Name = Verify that Portals Side View is remembered
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility

class C2511457_TestClass(BaseTestCase):

    def test_C2511457(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 190
        folders_css="[data-ibxp-text*='Folders']"
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        content_list=['Content', 'Portals', 'Favorites', 'Mobile Favorites']
        crumb_box_css = ".crumb-box .ibx-label-text"
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        coreutil_obj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Developer User.
                    Verify by default Content View is selected.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 1: Verify by default Content View is selected.")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list, "Step 1.1: Verify content title label folders", label_type='folders')
        
        """Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """ Step 3: Click Portals from the sidebar.
                    Verify Portals View is selected.
        """
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 2: Verify Portals View is selected.", default_selected='Portals')
        crumb_box_text=driver.find_element_by_css_selector(crumb_box_css).text.strip()
        utillobj.asequal('Portals', crumb_box_text, "Step 2.1: Verify Portals View is displayed in Crumb-box.")
        
        """ Step 4: In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User.
                    Verify by default Content View is selected and NOT Portals View.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mridadv', 'mrpassadv')
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 3: Verify by default Content View is selected and NOT Portals View.")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list, "Step 3.1: Verify content title label folders.", label_type='folders')
        
        """ Step 5: In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User.
                    Verify that Portals View is selected.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 4: Verify Portals View is selected.", default_selected='Portals')
        
        """ Step 6: Revert back the Home Page by its default state.
        """
        wfmain_obj.select_content_from_sidebar()
        crumb_elems=driver.find_elements_by_css_selector(crumb_box_css)
        domain_obj=[elem for elem in crumb_elems if elem.text.strip()=='Domains'][0]
        coreutil_obj.left_click(domain_obj)
        
        """ Step 7: In the banner link, click on the top right username > Click Sign Out
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        