'''
Created on Sep 26, 2018

@author: vishnu priya.

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/10660&group_by=cases:section_id&group_id=169269&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/2509628
TestCase Name = Verify that scroll bar is displayed in the breadcrumbs menu for HOME page.
'''
import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.pages import wf_mainpage as mainpage
from common.locators import wf_mainpage_locators

class C2509628_TestClass(BaseTestCase):

    def test_C2509628(self):
        
        """
        TESTCASE Objects 
        """
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        mainpage_obj=mainpage.Wf_Mainpage(self.driver)
    
        '''
        TESTCASE VARIABLES
        '''
        files_box_css = wf_mainpage_locators.WfMainPageLocators.FILES_BOX_CSS
        breadcrumb_path1='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples->Reports'
        breadcrumb_path='Workspaces->P292_S10660->G169261->Breadcrumb Trail and Search->Retail Samples'
        
        """ Step 1: Sign in to WebFOCUS as Administrator User..
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        
        """Step 2: Click on Content tree from side bar
        """
        wfmain_obj.select_content_from_sidebar()

        """ Step 3: Expand Domain > P292_S10660 > G169261 > Breadcrumb Trail and Search->Retail Samples'
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path)
        time.sleep(3)
        
        """ Step 4:Click on Reports in the tree
        """
        wfmain_obj.expand_repository_folder(breadcrumb_path1)
        
        """ Step 5:Click on arrow before P292_S10660
            Verify that scroll bar is displayed in the P292_S10660
        """
        mainpage_obj.select_right_arrow_in_crumb_box('Workspaces')
        scroll_css=".ibx-menu-no-icons.bread-menu-scroll-bar.pop-top"
        scroll_obj=utillobj.validate_and_get_webdriver_object(scroll_css, 'Context menu popup css')
        scroll_css_property=scroll_obj.value_of_css_property('overflow-y')
        utillobj.asequal('auto',scroll_css_property,"step 4:verify scroll_css property")
        utillobj.verify_picture_using_sikuli("C2509628.png","Step 4:verify scroll bar in context menu")
        
        """ Step 6: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", 90)
        wfmain_obj.select_option_from_crumb_box('Workspaces')
        
        """ Step 7: In the banner link, click on the top right username > Sign out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()

if __name__ == '__main__':
    unittest.main()  
        