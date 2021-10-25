'''
Created on September 05, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491057&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6468077
TestCase Name = Verify Side Bar show only Favorites option
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity
from common.locators import wf_mainpage_locators

class C6468077_TestClass(BaseTestCase):

    def test_C6468077(self):
        
        """
        TESTCASE VARIABLES
        """
        content_list=['Favorites']
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS

        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Developer User.
                    Verify sidebar listed Favorites option:
        """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(content_css, "Content", 60)
        
        wfmain_obj.verify_left_panel(content_list, "Step 1: Verify Side bar(left panel) options", comparision_type='asin')
        utillobj.verify_picture_using_sikuli("favourites.png", "Step 1.1: Verify favorites image is displayed")
           
        """ Step 2: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        