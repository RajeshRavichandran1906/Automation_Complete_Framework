'''
Created on Sep 26, 2018

@author: vishnu priya

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2511872
TestCase Name = Select folder in drop down,breadcrumb does not change but tree does
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C2511872_TestClass(BaseTestCase):

    def test_C2511872(self):
        
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

        files_box_css = wf_mainpage_locators.WfMainPageLocators.FILES_BOX_CSS
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples'
        breadcrumb_path1='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Charts'
        breadcrumb_path2='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Visualizations'
        expected_visualizations_item_list= ['Analytical Dashboard', 'Executive Dashboard', 'Sales by Country and Product', 'Store and Product Profits Over Time']

        
        """ Step 1: Sign in to WebFOCUS as Basic User.
        """
        wftools_login_obj.invoke_home_page('mridbas', 'mrpassbas')
        
        """Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()
        
        """ Step 2: Expand Domain > P292_S10660 > G169261 > Breadcrumb Trail and Search > Retail Samples
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        
        """ Step 3:Click on charts in the tree
            Verify breadcrumb trail is "Domains > P292_S10660 > G169261 > Breadcrumb Trail and Search > Retail Samples > Charts"
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path1)
        wfmain_obj.verify_crumb_box(breadcrumb_path1, 'Step 3:verify breadcrumb path for charts')
        
        """ Step 4:Click on > before charts in breadcrumb trail
        """
        """ Step 5:Select visualization
            Verify breadcrumb trail is "Domains > P292_S10660 > G169261 > Breadcrumb Trail and Search > Retail Samples >Visualizations"
            Verify Visualizations folder is selected in tree and items are listed in the content area
        """
        
        wfmain_obj.select_options_form_right_arrow_in_crumb_box('Retail Samples','Visualizations')
        wfmain_obj.verify_crumb_box(breadcrumb_path2, 'Step 5:verify breadcrumb path for Visualizations')
        wfmain_obj.verify_items_in_grid_view(expected_visualizations_item_list, 'asin','Step 5.1 verify items in dashboard views' )
        
        
        """ Step 6:Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", 90)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 6: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()  
        
    