'''
Created on September 25, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2325138
TestCase Name = Navigate to Breadcrumb Trail and Search/Retail Samples/Visualizations in tree
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2325138_TestClass(BaseTestCase):

    def test_C2325138(self):
        
        """
        TESTCASE Objects 
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        '''
        TESTCASE VARIABLES
        '''
        medium_wait = 60
        tree_css = wf_mainpage_locators.WfMainPageLocators.REPOSITORY_TREE_CSS
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Visualizations'
        selected_folder_under_repository_tree_css = "div[class='ibfs-tree'] div[data-ibfs-path]>div[class*='home-tree-node'].ibfs-item-selected .ibx-label-text"
        expected_visualizations_item_list= ['Analytical Dashboard', 'Executive Dashboard', 'Sales by Country and Product', 'Store and Product Profits Over Time']
        
        """ Step 1: Sign in to WebFOCUS as Basic User.
        """
        wftools_login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """Step 2: Click on Content tree from side bar>click on Domains from the resource tree.
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(tree_css, medium_wait)
        
        """ Step 3: Expand Domain > P292_S10660 > G169261 > Breadcrumb Trail and Search > Retail Samples
        """
        """ Step 4: Click on Visualizations in tree
                    Verify breadcrumb trail is "Domains > Breadcrumb Trail and Search > Retail Samples > Visualizations". 
                    Verify Visualizations is selected in tree and items in Visualizations folder appear in canvas
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        wfmain_obj.verify_crumb_box(breadcrumb_path, 'Step 3')
        selected_folder_under_repository_tree_css = utillobj.validate_and_get_webdriver_object(selected_folder_under_repository_tree_css, 'Selected folder under repository tree')
        utillobj.asequal(breadcrumb_path.split('->')[-1], selected_folder_under_repository_tree_css.text.strip(), "Step 3.1: Verify Visualizations is selected in tree.")
        wfmain_obj.verify_items_in_grid_view(expected_visualizations_item_list, 'asin', 'Step 3.2: Verify Visualizations items in Visualizations folder appear in canvas.')
        
        """ Step 5: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(tree_css, medium_wait)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 6: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        