'''
Created on November 21,2018

@author: Vpriya

Test Suite =http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=193250&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/7279892
TestCase Name = Verify content area toggles from List View to Grid View
'''

import unittest
from common.locators.wf_mainpage_locators import WfMainPageLocators
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity

class C7279892_TestClass(BaseTestCase):

    def test_C7279892(self):
        
        """
        TESTCASE VARIABLES
        """
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        breadcrumb_path='P292_S10660->G193250'    
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        locator = WfMainPageLocators()
        expected_list=['Alerts', 'Blogs', 'Charts', 'InfoAssist', 'Mode Manager', 'Page Designer', 'Portals', 'Report Library', 'ReportCaster', 'Shortcuts', 'sub1', 'Test Resources', 'Text Editor', 'Uploaded Files', 'URLs', 'Visualizations']
        
        """ Step 1: Sign in to WebFOCUS as Developer User.
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
                
        """Step 2: Click on the Content tree from the sidebar.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_number_of_element(locator.REPOSITORY_TREE_CSS,1, wfmain_obj.home_page_long_timesleep)
        
        """ Step 3: Expand Domain > 'P292_S10660' domain
        """
        """ Step 4: Click on 'G193250' folder from the tree
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        switch_to_list=self.driver.find_element_by_css_selector('div[title="Switch to grid view"]')
        if switch_to_list.is_displayed()==True:
            wfmain_obj.select_grid_view()
        utillobj.synchronize_with_visble_text("div.files-box-files", "Alerts", wfmain_obj.home_page_long_timesleep)
        
        """ Step 5: Click on toggle grid button to switch to grid view.
            Verify that all the subfolders are displayed in the grid view as same in the screenshot
        """
        
        wfmain_obj.verify_folders_in_grid_view(expected_list, 'asequal',"Step:5")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list,"Step 5.1 verify title",label_type='folders')
        
        """ Step 6: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        