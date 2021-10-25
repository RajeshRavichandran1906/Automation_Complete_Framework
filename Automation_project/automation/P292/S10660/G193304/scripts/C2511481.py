'''
Created on Oct 22, 2018

@author: Nasir

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10660&group_by=cases:section_id&group_id=193304&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2511481
TestCase Name = Verify that Favorites Side View is remembered
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility
from common.locators import wf_mainpage_locators
import time

class C2511481_TestClass(BaseTestCase):

    def test_C2511481(self):
        
        """
        TESTCASE VARIABLES
        """
        files_box_css = wf_mainpage_locators.WfMainPageLocators.FILES_BOX_CSS
        content_css=wf_mainpage_locators.WfMainPageLocators.CONTENT_CSS
        content_list=['Content']
        crumb_box_css = ".crumb-box .ibx-label-text"
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        coreutil_obj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """    1. Sign into WebFOCUS Home Page as Developer User.    """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        
        """    2. Click Content from sidebar > Retail Samples > Reports > Right click on "Quantity Sold By Stores" > Add to Favorites.    """
        wfmain_obj.select_content_from_sidebar()
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        utillobj.synchronize_with_visble_text(files_box_css, "Default sort", wfmain_obj.home_page_long_timesleep)
        wfmain_obj.right_click_folder_item_and_select_menu("Quantity Sold By Stores", 'Add to Favorites', 'Retail Samples->Reports')
        utillobj.verify_notify_popup(notify_text="Favorite added", msg='Step 02.01')
        
        """    3. Click Favorites from the sidebar.    """
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_items_in_grid_view(['Quantity Sold By Stores'], 'asin', "Step 03.01: Verify Quantity Sold By Stores item listed under Favorites")
        
        """    4. In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User.    """
        wfmain_obj.signout_from_username_dropdown_menu()
        time.sleep(5)
        wftools_login_obj.invoke_home_page('mridadv', 'mrpassadv')
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        utillobj.synchronize_with_visble_text(content_css, "Content", wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_left_panel(content_list, "Step 04.01: Verify by default Content View is selected and NOT Favorites View", comparision_type='asin')
        
        """    5. In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User.    """
        wfmain_obj.signout_from_username_dropdown_menu()
        time.sleep(5)
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", wfmain_obj.home_page_long_timesleep)
        wfmain_obj.verify_left_panel(content_list, "Step 05.01", default_selected='Favorites', comparision_type='asin')
        wfmain_obj.verify_items_in_grid_view(['Quantity Sold By Stores'], 'asin', "Step 05.02: Verify Quantity Sold By Stores item listed under Favorites")
        
        """    6. Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)    """
        wfmain_obj.select_content_from_sidebar()
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        utillobj.synchronize_with_visble_text(crumb_box_css, "Workspaces", wfmain_obj.home_page_long_timesleep)
        crumb_elems=driver.find_elements_by_css_selector(crumb_box_css)
        domain_obj=[elem for elem in crumb_elems if elem.text.strip()=='Workspaces'][0]
        coreutil_obj.left_click(domain_obj)
        utillobj.wait_for_page_loads(wfmain_obj.home_page_long_timesleep)
        
        """    7. In the banner link, click on the top right username > Click Sign Out.    """
        wfmain_obj.signout_from_username_dropdown_menu()
                
if __name__ == '__main__':
    unittest.main()        