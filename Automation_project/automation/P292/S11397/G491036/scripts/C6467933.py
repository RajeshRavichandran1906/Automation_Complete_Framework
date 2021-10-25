'''
Created on July 18, 2018

@author: AA14564

Test Suite = http://lnxtestrail.ibi.com/testrail//index.php?/suites/view/11397&group_by=cases:section_id&group_id=491036&group_order=asc
Test Case = http://lnxtestrail.ibi.com/testrail//index.php?/cases/view/6467933
TestCase Name = Verify Open item location for Portals w/ Admin user
'''

import unittest, time
from common.lib.basetestcase import BaseTestCase
from common.wftools import login, wf_mainpage
from common.lib import utillity, core_utility

class C6467933_TestClass(BaseTestCase):

    def test_C6467933(self):
        
        """
        TESTCASE VARIABLES
        """
        medium_wait = 145
        crumb_box_css = ".crumb-box .ibx-label-text"
        repository_css = "div[class='ibfs-tree']"
        expected_label_content_folders_list = ['Folders', 'Default sort', 'arrow_upward']
        content_list=['Content', 'Portals', 'Favorites', 'Ask WebFOCUS']
        context_menu_options = ['Open item location']
        expected_portals = ['1TestV3', 'V4 Portal']
        retail_sample_path='Retail Samples'
        retail_sample_item='Demo Videos'
        portal_path="Workspaces->P292_S10660->G193250->Portals->V4 Portals"
        
        driver = self.driver #Driver reference object created
        utillobj = utillity.UtillityMethods(driver)
        wftools_login_obj = login.Login(driver)
        wfmain_obj = wf_mainpage.Wf_Mainpage(driver)
        coreutil_obj=core_utility.CoreUtillityMethods(driver)
        
        """ Step 1: Sign into WebFOCUS Home Page as Admin User.
        """
        wftools_login_obj.invoke_home_page('mrid', 'mrpass')
        
        """ Step 2: Click Portals from the sidebar.
        """
        wfmain_obj.select_portals_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Portals", medium_wait)
        
        """ Step 3: Right click on '1TestV3' Portal.
                    Verify 'Open item location' is not available.
        """
        time.sleep(15)#giving time for loading to take place
        utillobj.wait_for_page_loads(wfmain_obj.home_page_medium_timesleep)
        wfmain_obj.verify_repository_folder_item_context_menu(expected_portals[0], context_menu_options, msg="Step 03.01", comparision_type='asnotin')
        coreutil_obj.python_left_click(utillobj.validate_and_get_webdriver_object(".main-panel .left-main-panel","left panel"))
        
        
        """ Step 4: Right click on 'V4 Portal'.
                    Verify 'Open item location' is available.
        """
        wfmain_obj.verify_repository_folder_item_context_menu(expected_portals[1], context_menu_options, msg="Step 04.01", comparision_type='asin')
        coreutil_obj.python_left_click(utillobj.validate_and_get_webdriver_object(".main-panel .left-main-panel","left panel"))
        
        
        """ Step 5: Click 'Open item location'
                    Verify that you are on the content view and in the folder where the portal resides.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(expected_portals[1], 'Open item location')
        wfmain_obj.verify_left_panel(content_list, "Step 05.01: Verify that you are on the content view.")
        wfmain_obj.verify_grid_view_title_labels(expected_label_content_folders_list, "Step 05.02: Verify content title label folders", label_type='folders')
        wfmain_obj.verify_items_in_grid_view([expected_portals[1]], 'asin', "Step 05.03: Verify {0} portal resides in {1} under content view".format(expected_portals[1], portal_path))
        
        """ Step 6: Click Content from the sidebar and click on 'Retail Samples' under Domains.
        """
        """ Step 7: Right click on 'Demo Videos' > 'Add to Favorites'.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(retail_sample_item, 'Add to Favorites', folder_path=retail_sample_path)
        
        """ Step 8: Click Favorites from the sidebar.Right click on 'Demo Videos'.
                    Verify that 'Open item location' is not available.
        """
        wfmain_obj.select_favorites_from_sidebar()
        utillobj.synchronize_with_visble_text(crumb_box_css, "Favorites", medium_wait)
        utillobj.synchronize_with_visble_text('div .content-box', 'Demo Videos', medium_wait)
        wfmain_obj.verify_repository_folder_item_context_menu(retail_sample_item, context_menu_options, msg="Step 08.01", comparision_type='asnotin')
        
        """ Step 9: Click 'Remove from Favorites'
                    Verify 'Demo Videos' has been removed from Favorites.
        """
        wfmain_obj.right_click_folder_item_and_select_menu(retail_sample_item, 'Remove from Favorites')
        utillobj.synchronize_with_visble_text(".files-box-files .ibx-label-text", "Your Favorites will appear here", medium_wait)
        wfmain_obj.verify_items_in_grid_view([retail_sample_item], 'asnotin', "Step 09.01: Verify {0} not in grid view".format(retail_sample_item))
        
        """ Step 10: Revert back the Home Page by its default state (Click content from side bar and click on Domain from navigation bar)
        """
        wfmain_obj.select_content_from_sidebar()
        utillobj.synchronize_until_element_is_visible(repository_css, wfmain_obj.home_page_medium_timesleep)
        
        """ Step 11: In the banner link, click on the top right username > Click Sign Out.
        """
        wfmain_obj.signout_from_username_dropdown_menu()
        
if __name__ == '__main__':
    unittest.main()        