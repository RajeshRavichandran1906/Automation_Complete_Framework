'''
Created on Oct 22, 2018

@author: Nasir

Test Suite = http://172.19.2.180/testrail/index.php?/suites/view/10660&group_by=cases:section_id&group_id=193304&group_order=asc
Test Case = http://172.19.2.180/testrail/index.php?/cases/view/2511482
TestCase Name = Verify that Mobile Favorites Side View is remembered
'''

import unittest
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility

class C2511482_TestClass(BaseTestCase):

    def test_C2511482(self):
        
        """
        TESTCASE VARIABLES
        """
        long_wait = 190
        folders_css="[data-ibxp-text*='Folders']"
        content_list=['Content', 'Portals', 'Favorites', 'Mobile Favorites']
        crumb_box_css = ".crumb-box .ibx-label-text"
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        coreutil_obj = core_utility.CoreUtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        
        """    1. Sign into WebFOCUS Home Page as Developer User.    """
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 01a: Verify by default Content View is selected.")
        
        """    2. Click Content from sidebar > Retail Samples > Charts > Right click on "Sales Insights" > Add to Mobile Favorites.    """
        wfmain_obj.right_click_folder_item_and_select_menu("Sales Insights", 'Add to Mobile Favorites', 'Retail Samples->Charts')
        utillobj.verify_notify_popup(notify_text="Mobile Favorite added", msg='Step 02')
        
        """    3. Click Mobile Favorites from the sidebar.    """
        wfmain_obj.select_mobilefavorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Mobile Favorites", long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 03a: Verify Mobile Favorites View is selected.", default_selected='Mobile Favorites')
        wfmain_obj.verify_items_in_grid_view(['Sales Insights'], 'asin', "Step 03b: Verify Sales Insights item listed under Mobile Favorites")
        
        """    4. In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Advanced User.    """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mridadv', 'mrpassadv')
        utillobj.synchronize_with_number_of_element(folders_css, 1, long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 04a: Verify by default Content View is selected and NOT Mobile Favorites View")
        
        """    5. In the banner link, click on the top right username > Click Sign Out and Sign back into WebFOCUS Home Page as Developer User.    """
        wfmain_obj.signout_from_username_dropdown_menu()
        wftools_login_obj.invoke_home_page('mriddev', 'mrpassdev')
        utillobj.synchronize_with_visble_text(crumb_box_css, "Mobile Favorites", long_wait)
        wfmain_obj.verify_left_panel(content_list, "Step 4a: Verify Mobile Favorites view is selected.", default_selected='Mobile Favorites')
        wfmain_obj.verify_items_in_grid_view(['Sales Insights'], 'asin', "Step 04b: Verify Sales Insights item listed under Mobile Favorites")
        
        """    6. Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)    """
        wfmain_obj.select_content_from_sidebar()
        crumb_elems=driver.find_elements_by_css_selector(crumb_box_css)
        domain_obj=[elem for elem in crumb_elems if elem.text.strip()=='Domains'][0]
        coreutil_obj.left_click(domain_obj)
        
        """    7. In the banner link, click on the top right username > Click Sign Out.    """
        wfmain_obj.signout_from_username_dropdown_menu()
        
        
if __name__ == '__main__':
    unittest.main()        